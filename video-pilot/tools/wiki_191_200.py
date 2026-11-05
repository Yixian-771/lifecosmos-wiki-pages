# -*- coding: utf-8 -*-
"""185–190 上站（174 与 173 同页，第二段视频追加在 173 图集之后）
131–138 上站（全部新词条，插入视频段＋图集）。原 121–130 说明：
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
    (191, "material-thinking", "物质思维", "Material Thinking", "oRHCqQKOWss", "3nm8IsIVoCI", False),
    (192, "good-evil-108", "善恶和108善108恶", "Good, Evil, and the 108 Evils & 108 Virtues", "FW4u1OT6m3s", "FnKRDafc8IY", False),
    (193, "yin-shi-ao-mi", "饮食奥秘", "The Mysteries of Food and Diet", "jxtpEUQzeHU", "6Hng4HDEj5c", False),
    (194, "hundun-baby", "浑沌元初", "Hundun Baby", "j1NlSh2Dmvg", "hjD6F2u-BBM", False),
    (195, "retained-info-realm", "滞留信息间", "Retained Information Space", "ZpjN4ZQRW_k", "nZnFRUASFyE", False),
    (196, "romantic-love-and-sexuality", "情爱·性爱", "Romantic Love and Sexuality", "sHriUKEvVl8", "sFdaPGXKV-w", False),
    (197, "imagery-thinking", "形象思维", "Imagery Thinking", "Yf3r4BscExA", "D8YiXMk4WiM", False),
    (198, "shao-si-gua-yu", "少私寡欲·宠辱不惊", "Minimal Desires, Unshaken Composure", "pzZT5LzQHZg", "7nB_1oL2SYI", False),
    (199, "mahjong-hundun-culture", "麻将与浑沌文化", "Mahjong and Hundun Culture", "qnwyhVWqV8o", "qgRXz5Lxdx8", False),
    (200, "life-trajectory", "人生轨迹", "Life Trajectory", "KJWiY1FIZeY", "0bSMrKhUkhQ", False),
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
            if "youtube-nocookie.com/embed/" in text:
                print(f"  {ep:03d} [{lang}] 已有视频段，跳过"); continue
            lines = text.split(LF)
            b = block(lang, name, vid, n)
            nav = next((i for i, l in enumerate(lines) if re.fullmatch(r"## (版本导航|Versions)\s*", l)), None)
            rel = next((i for i, l in enumerate(lines) if re.match(r"(## (相关词条|Related [Ee]ntries)\s*$|\*\*(相关词条|关联词条|Related [Ee]ntries|Related [Tt]erms?)[：:]?\*\*[：:]?)", l)), None)
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


