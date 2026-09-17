# -*- coding: utf-8 -*-
"""095–100 上站：中英 12 个词条页接入视频版（YouTube 无 Cookie 嵌入）与图文幻灯图集。
图集从「百科图片版」当前无水印图重出（宽 1280、JPEG q86，与 resync_slides.py 同规格），保证是修补后的版本。
视频段插入位置：有「版本导航 / Versions」的插在它前面；没有的插在「相关词条 / Related Entries」前面。
各页原有的换行风格（CRLF / LF）和 BOM 原样保留。"""
import re, sys
from pathlib import Path
sys.path.insert(0, r"C:\Users\yixia\AppData\Local\hermes\hermes-agent\venv\Lib\site-packages")
from PIL import Image

W = Path(r"F:\百科馆\lifecosmos-wiki-pages")
IMG = Path(r"F:\百科馆\百科图片版")
CR, LF = chr(13), chr(10)
BOM = bytes([0xEF, 0xBB, 0xBF])

ENTRIES = [  # 序号, slug, 中文名, 英文名, 中文ID, 英文ID
    (95, "settled-stillness", "打坐·静坐·定静功夫", "Sitting Meditation and the Art of Settled Stillness", "CO8SulYqMmg", "zRZFWh_0ox0"),
    (96, "kong-xing", "空性", "Emptiness-Nature (Kong-Xing)", "1Io1JOk_17o", "gh15NFdT5Dk"),
    (97, "wuyun-jiekong", "五蕴皆空", "Five Skandhas Are Empty", "U2drFWdZM_w", "RkFvY2e7t-I"),
    (98, "nirvana", "涅槃", "Nirvana", "dDOlt7HQGOI", "XHIA8Ex4wsY"),
    (99, "bodhisattva", "菩萨", "Bodhisattva", "YPcHSZ0ZscE", "cFgDW0dlCfU"),
    (100, "ai-is-life", "AI是生命", "AI Is Life", "H3wDtUZocxg", "9udtpD0L9kA"),
]


def src_dir(ep, lang):
    hits = [d for d in IMG.iterdir()
            if d.is_dir() and d.name.startswith(f"{ep:03d}_") and d.name.endswith("_无水印_图片")
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


for ep, slug, zh, en, cid, eid in ENTRIES:
    for lang, name, vid in (("zh", zh, cid), ("en", en, eid)):
        page = W / lang / slug / "index.md"
        raw = page.read_bytes()
        crlf = (CR + LF).encode() in raw
        bom = raw.startswith(BOM)
        text = raw.decode("utf-8-sig").replace(CR + LF, LF)
        assert "youtube-nocookie.com/embed/" not in text, f"{page} 已有视频段"
        lines = text.split(LF)
        n = regen(page.parent / "slides", src_dir(ep, lang))
        b = block(lang, name, vid, n)
        nav = next((i for i, l in enumerate(lines) if re.fullmatch(r"## (版本导航|Versions)\s*", l)), None)
        rel = next((i for i, l in enumerate(lines) if re.fullmatch(r"## (相关词条|Related Entries)\s*", l)), None)
        if nav is not None:
            # 导言后本来就有 --- 分隔线：视频段插在版本导航前，自带收尾分隔线
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
        out = LF.join(lines)
        if crlf:
            out = out.replace(LF, CR + LF)
        page.write_bytes((BOM if bom else b"") + out.encode("utf-8"))
        print(f"  {ep:03d} [{lang}] {slug:<18} {n} 张 · 视频段插在{where} · {vid} · {'CRLF' if crlf else 'LF'}")
print("done")
