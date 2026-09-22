# -*- coding: utf-8 -*-
"""113/114＋115英文（⚠ 114 第 6 页已于 2026-09-22 删除，重跑本脚本会恢复成 14 页，跑完要再删 p06 并前移）：pptx → 原版归档 → 去水印 → 无水印 PDF → 图片版 → video-pilot slides。（SOP 阶段3 pptx 路线）"""
import io, re, shutil, sys, zipfile
from pathlib import Path
from PIL import Image
import fitz, importlib.util
sys.stdout.reconfigure(encoding="utf-8")
spec = importlib.util.spec_from_file_location("wm", r"F:\百科馆\小工具\PDF去水印\PDF去水印.pyw")
wm = importlib.util.module_from_spec(spec); spec.loader.exec_module(wm)
ROOT = Path(r"F:\百科馆"); DL = Path(r"E:\下载")
PDF_DIR, RAW_DIR, IMG_DIR = ROOT / "百科PDF版", ROOT / "百科PDF版" / "原版", ROOT / "百科图片版"
VP = ROOT / r"lifecosmos-wiki-pages\video-pilot"
JOBS = [
    ("Wealth_Beyond_Currency.pptx",   "113_Lifechanyuans_View_on_Money（生命禅院金钱观）", "slides_jqg"),
    ("Life_Beyond_Money.pptx",        "113_Lifechanyuans_View_on_Money",               "slides_jqg_en"),
    ("Life_Zen_Civilization.pptx",    "114_Civilization_Overview（文明（总论））",         "slides_wmzl"),
    ("Civilization_3.0 (1).pptx",     "114_Civilization_Overview",                     "slides_wmzl_en"),
    ("Civilization_3.0.pptx",         "115_Civilizational_Leap",                       "slides_wmys_en"),
]
def page_pngs(pptx):
    z = zipfile.ZipFile(pptx)
    nums = sorted(int(re.search(r"slide(\d+)\.xml$", n).group(1)) for n in z.namelist() if re.fullmatch(r"ppt/slides/slide\d+\.xml", n))
    out = []
    for n in nums:
        rels = z.read("ppt/slides/_rels/slide%d.xml.rels" % n).decode("utf-8")
        names = [m for m in re.findall(r'Target="\.\./media/([^"]+)"', rels) if m.lower().endswith((".png", ".jpg", ".jpeg"))]
        assert len(names) == 1
        out.append(Image.open(io.BytesIO(z.read("ppt/media/" + names[0]))).convert("RGB"))
    return out
def to_pdf(images, dst):
    doc = fitz.open()
    for im in images:
        w, h = im.size
        pg = doc.new_page(width=w * 0.48, height=h * 0.48)
        buf = io.BytesIO(); im.save(buf, "JPEG", quality=92)
        pg.insert_image(fitz.Rect(0, 0, pg.rect.width, pg.rect.height), stream=buf.getvalue())
    doc.save(dst, deflate=True); doc.close()
for src, base, sd in JOBS:
    pages = page_pngs(DL / src)
    shutil.copy2(DL / src, RAW_DIR / (base + ".pptx")); to_pdf(pages, RAW_DIR / (base + ".pdf"))
    cleaned = [wm.remove_corner_watermark(im)[0].convert("RGB") for im in pages]
    to_pdf(cleaned, PDF_DIR / (base + "_无水印.pdf"))
    d = IMG_DIR / (base + "_无水印_图片"); d.mkdir(exist_ok=True)
    for i, im in enumerate(cleaned, 1):
        im.resize((2560, round(im.height * 2560 / im.width)), Image.LANCZOS).save(d / ("%s_无水印_%02d.jpg" % (base, i)), quality=87)
    (VP / sd).mkdir(exist_ok=True)
    for i, im in enumerate(cleaned, 1):
        im.save(VP / sd / ("slide_%02d.png" % i))
    print("✓ %s ← %s：%d 页 → 原版/无水印PDF/图片版/%s" % (base, src, len(pages), sd))
