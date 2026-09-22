# -*- coding: utf-8 -*-
"""113/114＋115英文 幻灯修补（114 已删第 6 页，页键仍按 pptx 原页号，save 时自动前移）。每页从 百科PDF版\原版 的 pptx 重取＋去水印再修，可反复跑。
用法：python fix_113114.py [页键 ...]   不给参数就全修。页键形如 jqg03、wmzl_en12。"""
import io, re, sys, zipfile, importlib.util
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, str(Path(__file__).parent))
from movelines import move_lines  # noqa: E402
spec = importlib.util.spec_from_file_location("wm", r"F:\百科馆\小工具\PDF去水印\PDF去水印.pyw")
wm = importlib.util.module_from_spec(spec); spec.loader.exec_module(wm)
RAW = Path(r"F:\百科馆\百科PDF版\原版")
VP = Path(r"F:\百科馆\lifecosmos-wiki-pages\video-pilot")
PREV = Path(r"E:\CodexData\temp\claude\F-----\1dd2e699-d90b-4dbc-8e68-c3718168f1e9\scratchpad\pptx113\fix")
PREV.mkdir(parents=True, exist_ok=True)
DECK = {"jqg": "113_Lifechanyuans_View_on_Money（生命禅院金钱观）", "jqg_en": "113_Lifechanyuans_View_on_Money",
        "wmzl": "114_Civilization_Overview（文明（总论））", "wmzl_en": "114_Civilization_Overview",
        "wmys_en": "115_Civilizational_Leap"}
SANS = r"C:\Windows\Fonts\NotoSansSC-VF.ttf"
SERIF = r"C:\Windows\Fonts\NotoSerifSC-VF.ttf"


def fresh(code, pg):
    z = zipfile.ZipFile(RAW / (DECK[code] + ".pptx"))
    rels = z.read("ppt/slides/_rels/slide%d.xml.rels" % pg).decode("utf-8")
    name = [m for m in re.findall(r'Target="\.\./media/([^"]+)"', rels) if m.lower().endswith((".png", ".jpg", ".jpeg"))][0]
    im = Image.open(io.BytesIO(z.read("ppt/media/" + name))).convert("RGB")
    return np.asarray(wm.remove_corner_watermark(im)[0].convert("RGB")).astype(float)


# 114 第 6 页（东海老人的话）2026-09-22 用户决定整页删除，之后各页前移一位；pptx 原版仍是 14 页
DROP = {"wmzl": 6, "wmzl_en": 6}


def out_no(code, pg):
    d = DROP.get(code)
    return pg - 1 if d and pg > d else pg


def save(a, code, pg):
    assert DROP.get(code) != pg, "此页已删除"
    Image.fromarray(np.clip(a, 0, 255).astype(np.uint8)).save(VP / ("slides_" + code) / ("slide_%02d.png" % out_no(code, pg)))


# ---------- 背景拟合：二次曲面，迭代剔除文字等离群点 ----------
def _design(X, Y):
    X = X.ravel().astype(float); Y = Y.ravel().astype(float)
    return np.stack([np.ones(X.size), X, Y, X * X, X * Y, Y * Y], 1)


def fit_bg(a, ring, exclude=None, iters=3, tol=7.0):
    """ring=(x0,y0,x1,y1) 内拟合平滑背景，返回可在任意坐标求值的函数；exclude 区域不参与拟合。"""
    X0, Y0, X1, Y1 = ring
    yy, xx = np.mgrid[Y0:Y1, X0:X1]
    sub = a[Y0:Y1, X0:X1]
    use = np.ones(xx.shape, bool)
    if exclude:
        ex0, ey0, ex1, ey1 = exclude
        use &= ~((xx >= ex0) & (xx < ex1) & (yy >= ey0) & (yy < ey1))
    coef = None
    for _ in range(iters):
        D = _design(xx[use], yy[use])
        coef = [np.linalg.lstsq(D, sub[..., c][use], rcond=None)[0] for c in range(3)]
        pred = np.stack([(_design(xx, yy) @ coef[c]).reshape(xx.shape) for c in range(3)], -1)
        res = np.abs(sub - pred).max(-1)
        use &= res < tol
    def ev(box):
        x0, y0, x1, y1 = box
        by, bx = np.mgrid[y0:y1, x0:x1]
        return np.stack([(_design(bx, by) @ coef[c]).reshape(by.shape) for c in range(3)], -1)
    return ev


def erase_box(a, box, ring, feather=4):
    """box 整块换成拟合背景（纯天空上的字），四边羽化。"""
    ev = fit_bg(a, ring, exclude=box)
    x0, y0, x1, y1 = box
    fill = ev(box)
    m = np.ones((y1 - y0, x1 - x0))
    r = np.linspace(0, 1, feather + 2)[1:-1]
    m[:feather] *= r[:, None]; m[-feather:] *= r[::-1, None]
    m[:, :feather] *= r[None]; m[:, -feather:] *= r[::-1][None]
    a[y0:y1, x0:x1] = a[y0:y1, x0:x1] * (1 - m[..., None]) + fill * m[..., None]


def move_text(a, band, ring, moves, thr=18):
    """band 内按段平移"字"：只动字形像素，背景保持原样。
    字形 = 与局部背景（中值滤波）差异大于 thr 的像素（向外扩 1 像素带上抗锯齿边）。
    做法：先把 band 里所有字形像素用局部背景补掉，再把各段字形（含抗锯齿，按 alpha 合成）贴到新位置。"""
    X0, Y0, X1, Y1 = band
    reg = a[Y0:Y1, X0:X1].copy()
    g = reg.mean(-1)
    bgl = np.stack([np.asarray(Image.fromarray(np.clip(reg[..., c], 0, 255).astype(np.uint8)).filter(ImageFilter.MedianFilter(15)), float) for c in range(3)], -1)
    diff = np.abs(reg - bgl).max(-1)
    alpha = np.clip((diff - thr * 0.5) / thr, 0, 1)
    alpha = np.maximum(alpha, np.asarray(Image.fromarray((alpha * 255).astype(np.uint8)).filter(ImageFilter.MaxFilter(3)), float) / 255 * 0.6)
    # 背景：字形处用中值背景
    clean = reg * (1 - alpha[..., None]) + bgl * alpha[..., None]
    out = clean.copy()
    for sx0, sx1, dx, dy in moves:
        lx0, lx1 = sx0 - X0, sx1 - X0
        seg = reg[:, lx0:lx1]; al = alpha[:, lx0:lx1]
        h, w = al.shape
        ty0, tx0 = dy, lx0 + dx
        ys0, ys1 = max(0, ty0), min(out.shape[0], ty0 + h)
        xs0, xs1 = max(0, tx0), min(out.shape[1], tx0 + w)
        sseg = seg[ys0 - ty0:ys1 - ty0, xs0 - tx0:xs1 - tx0]
        sal = al[ys0 - ty0:ys1 - ty0, xs0 - tx0:xs1 - tx0][..., None]
        out[ys0:ys1, xs0:xs1] = out[ys0:ys1, xs0:xs1] * (1 - sal) + sseg * sal
    a[Y0:Y1, X0:X1] = out


def inpaint(a, mask, grow=1):
    """mask 为 True 的像素用周围已知像素向内扩散补上（细笔画文字、细线）。"""
    m = mask.copy()
    for _ in range(grow):
        m = m | np.roll(m, 1, 0) | np.roll(m, -1, 0) | np.roll(m, 1, 1) | np.roll(m, -1, 1)
    known = ~m
    out = a.copy()
    out[m] = 0
    while m.any():
        acc = np.zeros_like(out); cnt = np.zeros(m.shape)
        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):
                if dx == 0 and dy == 0:
                    continue
                k = np.roll(np.roll(known, dy, 0), dx, 1)
                v = np.roll(np.roll(out, dy, 0), dx, 1)
                acc += v * k[..., None]; cnt += k
        can = m & (cnt > 0)
        out[can] = acc[can] / cnt[can][..., None]
        known = known | can; m = m & ~can
    a[:] = out


def white_text_mask(a, box, thr=35, satmax=0.18):
    x0, y0, x1, y1 = box
    reg = a[y0:y1, x0:x1]
    g = reg.mean(-1)
    bl = np.asarray(Image.fromarray(g.astype(np.uint8)).filter(ImageFilter.GaussianBlur(6)), float)
    mx, mn = reg.max(-1), reg.min(-1)
    sat = (mx - mn) / np.maximum(mx, 1)
    m = np.zeros(a.shape[:2], bool)
    m[y0:y1, x0:x1] = (g - bl > thr * 0.4) & (g > 175) & (sat < satmax)
    return m


def glow_subtract(a, box, ring, blur=18, k=1.0, satmax=0.45):
    """减掉平滑亮光（太阳光晕）、保留细节。"""
    ev = fit_bg(a, ring, exclude=box, tol=12)
    bx0, by0, bx1, by1 = box
    fill = ev(box)
    reg = a[by0:by1, bx0:bx1]
    B = np.asarray(Image.fromarray(np.clip(reg, 0, 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(blur)), float)
    excess = np.clip(B - fill, 0, None)
    mx = reg.max(-1); mn = reg.min(-1)
    sat = (mx - mn) / np.maximum(mx, 1)
    w = np.clip(1 - sat / satmax, 0, 1)
    fe = 16; r = np.linspace(0, 1, fe + 2)[1:-1]
    H, W = a.shape[:2]
    e = np.ones(w.shape)
    if by0 > 0: e[:fe] *= r[:, None]
    if by1 < H: e[-fe:] *= r[::-1, None]
    if bx0 > 0: e[:, :fe] *= r[None]
    if bx1 < W: e[:, -fe:] *= r[::-1][None]
    a[by0:by1, bx0:bx1] = reg - k * excess * (w * e)[..., None]


def sun_flatten(a, cx, cy, R, sky_ring, k=1.0):
    """太阳压平：在 sky_ring（天空环带）里按“像天空”的像素拟合天空色；
    以 (cx,cy) 为心、R 为半径，把“亮出天空”的平滑部分按径向权重扣掉（中心全扣、边缘渐隐），细节保留。"""
    H, W = a.shape[:2]
    X0, Y0, X1, Y1 = sky_ring
    yy, xx = np.mgrid[Y0:Y1, X0:X1]
    sub = a[Y0:Y1, X0:X1]
    d = np.hypot(xx - cx, yy - cy)
    use = (d > R * 0.95) & (sub[..., 2] > sub[..., 0] + 25)
    D = _design(xx[use], yy[use])
    coef = [np.linalg.lstsq(D, sub[..., c][use], rcond=None)[0] for c in range(3)]
    x0, y0, x1, y1 = max(0, int(cx - R)), max(0, int(cy - R)), min(W, int(cx + R)), min(H, int(cy + R))
    by, bx = np.mgrid[y0:y1, x0:x1]
    sky = np.stack([(_design(bx, by) @ coef[c]).reshape(by.shape) for c in range(3)], -1)
    reg = a[y0:y1, x0:x1]
    B = np.asarray(Image.fromarray(np.clip(reg, 0, 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(14)), float)
    excess = B - sky
    excess = np.clip(excess, 0, None)
    rr = np.hypot(bx - cx, by - cy) / R
    w = np.clip(1 - rr, 0, 1)
    w = w * w * (3 - 2 * w)
    w = np.clip(w * 1.6, 0, 1)
    mx = reg.max(-1); mn = reg.min(-1)
    sat = (mx - mn) / np.maximum(mx, 1)
    keep = np.clip((sat - 0.35) / 0.25, 0, 1)  # 高饱和的（花、草）少扣
    a[y0:y1, x0:x1] = reg - k * excess * (w * (1 - keep))[..., None]


def texture_fill(a, mask, dx, dy, feather=3):
    """mask 区域用 (dx,dy) 平移处的纹理覆盖，边缘羽化。"""
    m = np.asarray(Image.fromarray((mask * 255).astype(np.uint8)).filter(ImageFilter.MaxFilter(3)).filter(ImageFilter.GaussianBlur(feather)), float) / 255
    H, W = a.shape[:2]
    ys = np.clip(np.arange(H) + dy, 0, H - 1)
    xs = np.clip(np.arange(W) + dx, 0, W - 1)
    src = a[ys][:, xs]  # src[y, x] = a[y+dy, x+dx]
    a[:] = a * (1 - m[..., None]) + src * m[..., None]


def draw_text(a, items):
    """items=[(x, y, text, font, fill, anchor)]，直接画到数组上。"""
    im = Image.fromarray(np.clip(a, 0, 255).astype(np.uint8))
    d = ImageDraw.Draw(im)
    for x, y, t, f, fill, anc in items:
        d.text((x, y), t, font=f, fill=fill, anchor=anc)
    a[:] = np.asarray(im).astype(float)


def font(path, size, var):
    f = ImageFont.truetype(path, size)
    f.set_variation_by_name(var)
    return f


# ---------- 各页修补 ----------
def jqg03(a):
    """竖排正文漏了「精神财富，最后」：擦掉第4、5列，重排成三列。"""
    erase_box(a, (222, 84, 306, 440), (150, 60, 360, 450))
    f = font(SANS, 24, b"Medium")
    text = "人首先要追求心灵财富，其次是精神财富，最后是物质财富；三大财富缺一不可。"
    cols = [text[0:14], text[14:28], text[28:]]
    xs = [286.5, 243, 199.5]
    items = []
    base = 91 + 20.5  # 原图首字字顶 y=91，24 号字基线约在字顶下 20.5
    for cx, col in zip(xs, cols):
        for i, ch in enumerate(col):
            adv = f.getlength(ch)
            lift = 7 if ch in "，；。" else 0  # 原图标点在格子左侧偏中，不贴下一个字
            items.append((cx - adv / 2, base + i * 24.3 - lift, ch, f, (0, 24, 38), "ls"))
    draw_text(a, items)


def jqg11(a):
    """太阳进画面（左上），减光晕。"""
    sun_flatten(a, 301, 38, 380, (0, 0, 1000, 460), k=0.72)


def jqg12(a):
    """中文版上多印的英文标签 Spiritual / Soul。"""
    for box, (dx, dy) in [((134, 80, 232, 112), (0, 34)), ((1186, 577, 1237, 601), (42, -28))]:
        x0, y0, x1, y1 = box
        m = np.zeros(a.shape[:2]); m[y0:y1, x0:x1] = 1
        texture_fill(a, m, dx, dy, feather=3)


def wmzl07(a):
    """正文字号太小、字形画坏：擦掉重排，字号放大。"""
    erase_box(a, (462, 100, 918, 196), (380, 88, 1000, 215))
    f = font(SERIF, 18, b"Medium")
    items = [(688, 108, "自由至高无上，自由度显示了一个生命所处的层次：", f, (250, 250, 250), "mt"),
             (688, 134, "自由度越大，越接近天堂；自由度越小，越接近地狱。", f, (250, 250, 250), "mt"),
             (688, 170, "文明社会的一个最大特征，是公民获得了充分且高度的自由。", f, (250, 250, 250), "mt")]
    draw_text(a, items)


def wmzl12(a):
    """第二行是乱码行：删掉，第三、四行上移一行。"""
    move_lines(a, [(209, 239), (240, 270), (271, 303)], [(1, 170, 1210, 0, -31), (2, 170, 1210, 0, -31)], (150, 1230))


def wmzl_en01(a):
    glow_subtract(a, (0, 0, 380, 260), (0, 0, 560, 330), blur=24)


def wmzl_en04(a):
    """右侧重复的一条 Protecting the weak…：三行字清掉（行背景插值），不贴回。"""
    # 深色字形掩码（相对行内中位数暗 25 以上）扩 2 像素，向内扩散补
    g = a.mean(-1)
    box = (1108, 236, 1346, 304)
    x0, y0, x1, y1 = box
    reg = g[y0:y1, x0:x1]
    bl = np.asarray(Image.fromarray(np.clip(g, 0, 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(10)), float)[y0:y1, x0:x1]
    m = np.zeros(g.shape, bool)
    m[y0:y1, x0:x1] = (bl - reg) > 12
    inpaint(a, m, grow=2)


def wmzl_en09(a):
    """第二行行尾多一个 fighting：删掉并把该行重新居中。"""
    move_lines(a, [(151, 186)], [(0, 214, 1050, 52, 0)], (180, 1200))


def wmzl_en12(a):
    """第五行多出乱词 sht：删掉、右半截左移，再居中。"""
    move_lines(a, [(262, 295)], [(0, 240, 594, 19, 0), (0, 634, 1140, -19, 0)], (200, 1180))


def wmys_en08(a):
    """太阳进画面（右上）。"""
    # 太阳盘及光晕在纯天空上：整块换成拟合天空（排除山体），再羽化
    erase_box(a, (1060, 40, 1300, 260), (960, 0, 1376, 300), feather=40)


def wmys_en10(a):
    """中间多了一条白色竖分隔线（x 686-689，y 330 往下）：用左右两侧像素横向插值补。"""
    x0, x1 = 684, 692
    for y in range(320, a.shape[0]):
        l, r = a[y, x0 - 1], a[y, x1]
        t = np.linspace(0, 1, x1 - x0 + 2)[1:-1][:, None]
        a[y, x0:x1] = l * (1 - t) + r * t


def wmys_en12(a):
    """第二段第二行开头多一个破折号：删掉并左移对齐。"""
    move_lines(a, [(247, 273)], [(0, 129, 512, -24, 0)], (80, 540))


FIX = {("jqg", 3): jqg03, ("jqg", 11): jqg11, ("jqg", 12): jqg12,
       ("wmzl", 7): wmzl07, ("wmzl", 12): wmzl12,
       ("wmzl_en", 1): wmzl_en01, ("wmzl_en", 4): wmzl_en04, ("wmzl_en", 9): wmzl_en09, ("wmzl_en", 12): wmzl_en12,
       ("wmys_en", 8): wmys_en08, ("wmys_en", 10): wmys_en10, ("wmys_en", 12): wmys_en12}

if __name__ == "__main__":
    want = sys.argv[1:]
    for (code, pg), fn in FIX.items():
        key = "%s%02d" % (code, pg)
        if want and key not in want:
            continue
        a = fresh(code, pg)
        before = a.copy()
        fn(a)
        save(a, code, pg)
        Image.fromarray(np.clip(np.concatenate([before, a], 0), 0, 255).astype(np.uint8)).save(PREV / (key + ".jpg"), quality=88)
        print("✓", key, (fn.__doc__ or "").strip().splitlines()[0] if fn.__doc__ else "")
