# -*- coding: utf-8 -*-
"""131–138 上站（全部新词条，插入视频段＋图集）。原 121–130 说明：
· 121–128 已有视频段，但嵌的是旧版视频 → 换成重渲后的新 ID，并按「百科图片版」当前图重出图集（页数变了同步清单）。
· 129、130 新词条 → 插入视频段（YouTube 无 Cookie 嵌入）＋图集。
各页原有的换行风格（CRLF / LF）和 BOM 原样保留。"""
import re, sys
from pathlib import Path
sys.path.insert(0, r"C:\Users\yixia\AppData\Local\hermes\hermes-agent\venv\Lib\site-packages")
from PIL import Image

W = Path(r"F:\百科馆\lifecosmos-wiki-pages")
IMG = Path(r"F:\百科馆\百科图片版")
CR, LF = chr(13), chr(10)
BOM = bytes([0xEF, 0xBB, 0xBF])

ENTRIES = [  # 序号, slug, 中文名, 英文名, 中文ID, 英文ID, 是否已有视频段
    (131, "tianming", "天命", "Tianming (Heavenly Mandate)", "sacYI0GZsz0", "dn3jJy-bexw", False),
    (132, "tianfu", "天赋", "Natural Talent (Tianfu)", "eAmOyPW7sS0", "fS_pWIUtcu0", False),
    (133, "tianxing", "天性", "Innate Nature (Tianxing)", "15C-ZGxkb84", "FMNOHpyUViw", False),
    (134, "tiancai", "天才", "Genius (Tiancai)", "Ftj3wSzw418", "E6PWKK1byfs", False),
    (135, "eighteen-grades-of-life", "人生十八品", "Eighteen Grades of Life", "KxLDjl4RczY", "CPwOgwgn6tY", False),
    (136, "eight-life-principles", "人生的八大纲领·八大玄机·八大天机·八大迷", "Eight Life Principles", "7UIrl2KdlVI", "wtVE_lY8fbs", False),
    (137, "worry-free-life", "无忧人生", "Worry-Free Life", "S57PBGDQhjA", "GSMkB_k14cI", False),
    (138, "knowledge-wisdom-spirituality", "知识·智慧·灵性", "Knowledge, Wisdom and Spirituality", "t4nNICFAMP4", "rCNTfQkAHmY", False),
]


def src_dir(ep, lang):
    hits = [d for d in IMG.iterdir()
            if d.is_dir() and d.name.startswith(f"{ep:03d}_") and d.name.endswith("_无水印_图片")
            and "_Zhi" not in d.name
            and (("（" in d.name) == (lang == "zh"))]
    assert len(hits) == 1, f"{ep:03d} [{lang}] 源目录不唯一: {[h.name for h in hits]}"
    return hits[0]


def regen(dst, src):
    jpgs = sorted(src.glob("*.jpg"))
    assert jpgs, src
    dst.mkdir(parents=True, exist_ok=True)
    for old in dst.glob("*.jpg"):
        old.unlink()
    for i, p in enumerate(jpgs, 1):
        im = Image.open(p).convert("RGB")
        im = im.resize((1280, round(im.height * 1280 / im.width)), Image.LANCZOS)
        im.save(dst / f"{i:02d}.jpg", "JPEG", quality=86, optimize=True)
    return len(jpgs)


def block(lang, name, vid, n):
    L = []
    if lang == "zh":
        L += ["## 视频版", "", '<div style="max-width:760px">',
              f'<iframe style="width:100%;aspect-ratio:4/3;border:0" src="https://www.youtube-nocookie.com/embed/{vid}" '
              f'title="{name}（生命禅院百科·视频版）" allowfullscreen></iframe>', "</div>", "",
              f'??? info "📖 图文幻灯（{n} 张，点击展开）"', ""]
        L += [f"    ![幻灯 {i:02d}](slides/{i:02d}.jpg)" for i in range(1, n + 1)]
    else:
        L += ["## Video", "", '<div style="max-width:760px">',
              f'<iframe style="width:100%;aspect-ratio:4/3;border:0" src="https://www.youtube-nocookie.com/embed/{vid}" '
              f'title="{name} (Lifechanyuan Encyclopedia video)" allowfullscreen></iframe>', "</div>", "",
              "## Slides", "", f'??? info "📖 Illustrated slides ({n} pages, click to expand)"', ""]
        L += [f"    ![slide {i:02d}](slides/{i:02d}.jpg)" for i in range(1, n + 1)]
    return L


def read(page):
    raw = page.read_bytes()
    crlf = (CR + LF).encode() in raw
    bom = raw.startswith(BOM)
    return raw.decode("utf-8-sig").replace(CR + LF, LF), crlf, bom


def write(page, text, crlf, bom):
    if crlf:
        text = text.replace(LF, CR + LF)
    page.write_bytes((BOM if bom else b"") + text.encode("utf-8"))


def fix_list(text, lang, n):
    tag = "幻灯" if lang == "zh" else "slide"
    lines = text.split(LF)
    idx = [i for i, l in enumerate(lines) if re.match(rf"^\s*!\[{tag} \d+\]\(slides/\d+\.jpg\)\s*$", l)]
    assert idx and idx[-1] - idx[0] + 1 == len(idx), "图集清单找不到或不连续"
    if len(idx) == n:
        return text, False
    indent = re.match(r"^(\s*)", lines[idx[0]]).group(1)
    lines[idx[0]:idx[-1] + 1] = [f"{indent}![{tag} {i:02d}](slides/{i:02d}.jpg)" for i in range(1, n + 1)]
    for i, l in enumerate(lines):
        if "??? info" in l and ("张，点击展开" in l or "click to expand" in l):
            lines[i] = (re.sub(r"（\d+ 张", f"（{n} 张", l) if lang == "zh" else re.sub(r"\(\d+ pages", f"({n} pages", l))
    return LF.join(lines), True


for ep, slug, zh, en, cid, eid, has in ENTRIES:
    for lang, name, vid in (("zh", zh, cid), ("en", en, eid)):
        page = W / lang / slug / "index.md"
        text, crlf, bom = read(page)
        n = regen(page.parent / "slides", src_dir(ep, lang))
        if has:
            m = re.findall(r"youtube-nocookie\.com/embed/([A-Za-z0-9_-]+)", text)
            assert len(m) == 1, f"{page} 视频段数量异常: {m}"
            old = m[0]
            text = text.replace(f"embed/{old}", f"embed/{vid}")
            text, changed = fix_list(text, lang, n)
            write(page, text, crlf, bom)
            print(f"  {ep:03d} [{lang}] {slug:<32} 换 ID {old} → {vid} · {n} 张{' · 清单页数已改' if changed else ''}")
        else:
            assert "youtube-nocookie.com/embed/" not in text, f"{page} 已有视频段"
            lines = text.split(LF)
            b = block(lang, name, vid, n)
            nav = next((i for i, l in enumerate(lines) if re.fullmatch(r"## (版本导航|Versions)\s*", l)), None)
            rel = next((i for i, l in enumerate(lines) if re.fullmatch(r"## (相关词条|Related Entries)\s*", l)), None)
            if nav is not None:
                lines[nav:nav] = b + ["", "---", ""]
                where = "版本导航前"
            else:
                assert rel is not None, f"{page} 找不到插入点"
                k = rel
                while k > 0 and lines[k - 1].strip() == "":
                    k -= 1
                prev = lines[k - 1].strip() if k > 0 else ""
                lead = [""] if prev == "---" else ["", "---", ""]
                lines[k:rel] = lead + b + ["", "---", ""]
                where = "相关词条前"
            write(page, LF.join(lines), crlf, bom)
            print(f"  {ep:03d} [{lang}] {slug:<32} 新增视频段（{where}）· {n} 张 · {vid}")
print("done")
