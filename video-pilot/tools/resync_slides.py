# -*- coding: utf-8 -*-
"""把 wiki 里停在旧版的幻灯图集重新从「百科图片版」当前无水印图生成，
并在页数变了的时候同步 index.md 的图集清单。
规格沿用 wiki_update.py：宽 1280、JPEG q86；中文 ![幻灯 NN]，英文 ![slide NN]。
"""
import argparse, re, sys
from pathlib import Path
sys.path.insert(0, r"C:\Users\yixia\AppData\Local\hermes\hermes-agent\venv\Lib\site-packages")
from PIL import Image

W = Path(r'F:\百科馆\lifecosmos-wiki-pages')
IMG = Path(r'F:\百科馆\百科图片版')
SLIDE_W = 1280

TARGETS = [
    (61, 'path-beyond-spacetime', ['zh']),
    (64, 'negative-universe', ['zh', 'en']),
    (65, 'antimatter-world', ['zh', 'en']),
    (66, 'antimatter-structure', ['zh', 'en']),
    (67, 'high-life-spaces', ['zh', 'en']),
    (69, 'dream-state', ['zh', 'en']),
    (72, 'jinghuaxinling', ['zh', 'en']),
    (73, 'suixing-er-dong', ['zh', 'en']),
    (74, 'illuminate-mind-see-nature', ['zh', 'en']),
    (75, 'letting-go', ['zh', 'en']),
    (76, 'gratitude', ['zh', 'en']),
    (77, 'humility', ['zh', 'en']),
]

def src_dir(ep, lang):
    hits = []
    for d in IMG.iterdir():
        if d.is_dir() and re.match(rf'^{ep:03d}_', d.name) and d.name.endswith('_无水印_图片'):
            if ('（' in d.name) == (lang == 'zh'):
                hits.append(d)
    if len(hits) != 1:
        sys.exit(f'!! {ep:03d} [{lang}] 源目录不唯一: {[h.name for h in hits]}')
    return hits[0]

def regen(dst, src, dry):
    jpgs = sorted(src.glob('*.jpg'))
    if not jpgs:
        sys.exit(f'!! {src} 里没有 jpg')
    if not dry:
        dst.mkdir(parents=True, exist_ok=True)
        for i, p in enumerate(jpgs, 1):
            im = Image.open(p).convert('RGB')
            im = im.resize((SLIDE_W, round(im.height * SLIDE_W / im.width)), Image.LANCZOS)
            im.save(dst / f'{i:02d}.jpg', 'JPEG', quality=86, optimize=True)
        for old in dst.glob('*.jpg'):          # 页数变少时清掉多余的
            if int(old.stem) > len(jpgs):
                old.unlink()
    return len(jpgs)

def fix_md(p, lang, n, dry):
    """图集页数变了：改 ??? info 那行的数字 + 重排 ![...] 清单。"""
    t = p.read_text(encoding='utf-8-sig')
    tag = '幻灯' if lang == 'zh' else 'slide'
    lines = t.splitlines()
    idx = [i for i, l in enumerate(lines)
           if re.match(rf'^\s*!\[{tag} \d+\]\(slides/\d+\.jpg\)\s*$', l)]
    if not idx:
        sys.exit(f'!! {p} 里找不到图集清单')
    if idx[-1] - idx[0] + 1 != len(idx):
        sys.exit(f'!! {p} 图集清单不连续')
    if len(idx) == n:
        return False
    indent = re.match(r'^(\s*)', lines[idx[0]]).group(1)
    new = [f'{indent}![{tag} {i:02d}](slides/{i:02d}.jpg)' for i in range(1, n + 1)]
    lines[idx[0]:idx[-1] + 1] = new
    for i, l in enumerate(lines):
        if '??? info' in l and ('张，点击展开' in l or 'click to expand' in l):
            lines[i] = (re.sub(r'（\d+ 张', f'（{n} 张', l) if lang == 'zh'
                        else re.sub(r'\(\d+ pages', f'({n} pages', l))
    if not dry:
        p.write_text('\n'.join(lines) + ('\n' if t.endswith('\n') else ''), encoding='utf-8')
    return True

ap = argparse.ArgumentParser(); ap.add_argument('--dry-run', action='store_true')
a = ap.parse_args()
tot = 0
for ep, slug, langs in TARGETS:
    for lang in langs:
        page = W / lang / slug / 'index.md'
        dst = page.parent / 'slides'
        old = len(list(dst.glob('*.jpg')))
        n = regen(dst, src_dir(ep, lang), a.dry_run)
        note = ''
        if old != n:
            fix_md(page, lang, n, a.dry_run)
            note = f'  ← 页数 {old} → {n}，index.md 清单已改'
        print(f'  {ep:03d} [{lang}] {slug:<28} {n} 张{note}')
        tot += 1
print(f'\n{"[dry-run] " if a.dry_run else ""}重出 {tot} 套图集')
