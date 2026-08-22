# -*- coding: utf-8 -*-
"""
正式引擎（配置驱动）：4:3 框版式 + 每张金句 + 聚光灯/圈框/连线指引 + 背景音乐
用法: python make_show.py --config awakening_narration [--stills] [--slide N]

配置模块需提供：
  SLIDES = [(img, [句子...]), ...]
  NAME, VOICE, FONT, RATE
  可选 MUSIC = 背景音乐路径
  可选 META = [ {quote:str, focuses:[ {at:int, spot/box/ring/line ...} ]}, ... ]  与 SLIDES 等长
focus 字段（坐标均为相对幻灯的比例）：
  at   : 该聚焦从本张第几句开始(0基)
  box  : (x0,y0,x1,y1) 左侧说明框/要框的文字
  ring : (cx,cy,rx,ry) 要画圈的图元
  spot : (x0,y0,x1,y1) 额外要打亮的区域（默认用 box∪ring）
  line : True 则从 box 连线带箭头到 ring
无 focuses 的张：整图常亮，只有金句+字幕。
"""
import re, sys, importlib, subprocess, math
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from moviepy import AudioFileClip, VideoClip, CompositeVideoClip, CompositeAudioClip, afx

W, H = 1440, 1080
TOP_H, BOT_H = 120, 156
GOLD = (255, 186, 70)
OUTRO, GAP, TAIL = 3.0, 0.28, 0.3


def load_cfg():
    name = "awakening_narration"
    if "--config" in sys.argv:
        name = sys.argv[sys.argv.index("--config")+1]
    return importlib.import_module(name)

CFG = load_cfg()
SLIDES = CFG.SLIDES
NAME = getattr(CFG, "NAME", "show")
VOICE = getattr(CFG, "VOICE", "zh-CN-YunxiNeural")
FONT = getattr(CFG, "FONT", r"C:\Windows\Fonts\msyhl.ttc")
FONT_BD = getattr(CFG, "FONT_BD", r"C:\Windows\Fonts\msyhbd.ttc")
RATE = getattr(CFG, "RATE", "+0%")
MUSIC = getattr(CFG, "MUSIC", None)
WATERMARK = getattr(CFG, "WATERMARK", "生命禅院百科")
META = getattr(CFG, "META", [{} for _ in SLIDES])

_ff = {}
def font(path, sz):
    if (path, sz) not in _ff:
        _ff[(path, sz)] = ImageFont.truetype(path, sz)
    return _ff[(path, sz)]


def parse_srt(path):
    out = []
    for b in re.split(r"\n\s*\n", open(path, encoding="utf-8").read().strip()):
        ls = b.strip().splitlines()
        ts = next((l for l in ls if "-->" in l), None)
        if not ts:
            continue
        m = re.match(r"(\d+):(\d+):(\d+)[,.](\d+)\s*-->\s*(\d+):(\d+):(\d+)[,.](\d+)", ts)
        h1, m1, s1, ms1, h2, m2, s2, ms2 = map(int, m.groups())
        out.append((h1*3600+m1*60+s1+ms1/1000, h2*3600+m2*60+s2+ms2/1000,
                    " ".join(ls[ls.index(ts)+1:]).strip()))
    return out


def smooth(p):
    p = min(max(p, 0), 1)
    return p*p*(3-2*p)


def build_audio(force=False):
    if not force and __import__("os").path.exists(f"{NAME}_audio.mp3") and \
       __import__("os").path.exists(f"{NAME}_subs.srt"):
        print("配音已存在，跳过"); return
    lines = [s for _, sents in SLIDES for s in sents]
    src = f"{NAME}_lines.txt"
    open(src, "w", encoding="utf-8").write("\n".join(lines))
    subprocess.run([sys.executable, "build_audio_srt.py", "--name", NAME,
                    "--voice", VOICE, f"--rate={RATE}", "--gap", str(GAP),
                    "--src", src], check=True)


# ---------- 每张幻灯的底图（框版式 + 金句 + 台标）----------
def build_base(img_path, quote):
    top = np.array([0, 0, 0]); bot = np.array([0, 0, 0])   # 底纹=纯黑（2026-07-05 由深棕改；用户觉得棕色不舒服）
    grad = np.linspace(0, 1, H)[:, None, None]
    canvas = Image.fromarray(np.repeat((top*(1-grad)+bot*grad).astype(np.uint8), W, axis=1))
    im = Image.open(img_path).convert("RGB")
    sw, sh = im.size
    nw, nh = W, round(sh*W/sw)
    im = im.resize((nw, nh), Image.LANCZOS)
    ox, oy = 0, TOP_H
    canvas.paste(im, (ox, oy))
    d = ImageDraw.Draw(canvas, "RGBA")
    # 台标（细体）；WATERMARK="" 则不画（用于图里已烤好台标的 GPT 图，2026-07-20）
    chip = WATERMARK
    if chip:
        f = font(FONT, 26)
        tw = d.textbbox((0, 0), chip, font=f)[2]; pad = 16
        bx1, by1 = ox+nw-12, oy+nh-12; bx0, by0 = bx1-tw-pad*2, by1-44
        d.rounded_rectangle([bx0, by0, bx1, by1], radius=10, fill=(0, 0, 0, 230))
        d.text((bx0+pad, (by0+by1)//2), chip, font=f, fill=(255, 205, 120, 255), anchor="lm")   # 台标文字垂直居中（2026-07-05）
    # 金句（细体）
    if quote:
        fq = font(FONT, 42); qw = d.textbbox((0, 0), quote, font=fq)[2]
        d.text(((W-qw)//2, (TOP_H-42)//2-2), quote, font=fq, fill=(255, 210, 140, 240))
    return np.asarray(canvas).astype(np.float32), (ox, oy, nw, nh)


def shape_mask(rect, foc):
    ox, oy, nw, nh = rect
    m = Image.new("L", (W, H), 0); dd = ImageDraw.Draw(m)
    drew = False
    if foc.get("spot"):
        x0, y0, x1, y1 = foc["spot"]
        dd.rounded_rectangle([ox+x0*nw, oy+y0*nh, ox+x1*nw, oy+y1*nh], radius=24, fill=255); drew = True
    if foc.get("box"):
        x0, y0, x1, y1 = foc["box"]
        dd.rounded_rectangle([ox+x0*nw-12, oy+y0*nh-8, ox+x1*nw+12, oy+y1*nh+8], radius=18, fill=255); drew = True
    if foc.get("ring"):
        cx, cy, rx, ry = foc["ring"]
        dd.ellipse([ox+cx*nw-rx*nw, oy+cy*nh-ry*nh, ox+cx*nw+rx*nw, oy+cy*nh+ry*nh], fill=255); drew = True
    if not drew:
        return np.ones((H, W, 1), np.float32)
    return (np.asarray(m.filter(ImageFilter.GaussianBlur(24))).astype(np.float32)/255)[:, :, None]


def annotate(img, rect, foc, la):
    ox, oy, nw, nh = rect
    a = smooth(la/0.5); pulse = 1.0+0.04*math.sin(2*math.pi*la/1.6)
    ov = Image.fromarray(img.astype(np.uint8)).convert("RGBA")
    d = ImageDraw.Draw(ov, "RGBA")
    col = GOLD+(int(235*a),); lw = max(2, int(5*a))
    bx = ring_c = None
    if foc.get("box"):
        x0, y0, x1, y1 = foc["box"]
        bx = [ox+x0*nw-12, oy+y0*nh-8, ox+x1*nw+12, oy+y1*nh+8]
        d.rounded_rectangle(bx, radius=18, outline=col, width=lw)
    if foc.get("ring"):
        cx, cy, rx, ry = foc["ring"]
        rxx, ryy = rx*nw*pulse, ry*nh*pulse
        cxp, cyp = ox+cx*nw, oy+cy*nh
        d.ellipse([cxp-rxx, cyp-ryy, cxp+rxx, cyp+ryy], outline=col, width=lw+1)
        ring_c = (cxp, cyp, rxx)
    if foc.get("line") and bx and ring_c:
        cxp, cyp, rxx = ring_c
        sx = bx[2] if cxp >= bx[2] else (bx[0] if cxp <= bx[0] else (bx[0]+bx[2])/2)
        sy = (bx[1]+bx[3])/2
        ex = cxp-rxx if cxp >= sx else cxp+rxx
        ey = cyp
        axp, ayp = sx+(ex-sx)*a, sy+(ey-sy)*a
        d.line([sx, sy, axp, ayp], fill=col, width=lw)
        if a > 0.6:
            ang = math.atan2(ayp-sy, axp-sx)
            for da in (2.5, -2.5):
                d.line([axp, ayp, axp-18*math.cos(ang+da), ayp-18*math.sin(ang+da)], fill=col, width=lw)
    return np.asarray(ov.convert("RGB")).astype(np.float32)


def main(stills=False, only=None):
    import os
    build_audio()
    cues = parse_srt(f"{NAME}_subs.srt")
    # 切片：每张幻灯的全局句子范围
    spans = []; idx = 0
    for _, sents in SLIDES:
        spans.append((idx, idx+len(sents))); idx += len(sents)

    bases, rects, foclists, masks = [], [], [], []
    for si, (img, sents) in enumerate(SLIDES):
        meta = META[si] if si < len(META) else {}
        base, rect = build_base(img, meta.get("quote", ""))
        bases.append(base); rects.append(rect)
        a, b = spans[si]
        focs = meta.get("focuses", [])
        # 为每个 focus 算起止时间
        items = []
        for fi, foc in enumerate(focs):
            g_start = a + foc["at"]
            t0 = cues[g_start][0]
            t1 = cues[(a+focs[fi+1]["at"])][0] if fi+1 < len(focs) else cues[b-1][1]
            items.append((t0, t1, foc))
        foclists.append(items)
        masks.append([shape_mask(rect, foc) for _, _, foc in items])

    win = [(cues[a][0], cues[b-1][1]) for a, b in spans]   # 每张显示窗口
    a_dur = cues[-1][1]; total = a_dur + OUTRO

    def render_slide(si, t):
        base = bases[si]; items = foclists[si]
        if not items:
            return base
        # 找当前 focus
        cur = -1
        for k, (t0, t1, _) in enumerate(items):
            if t >= t0: cur = k
        if cur < 0:
            return base
        t0, t1, foc = items[cur]
        dim = base.copy()
        ox, oy, nw, nh = rects[si]
        dim[oy:oy+nh, ox:ox+nw] *= 0.5
        m = masks[si][cur]
        comp = dim*(1-m) + base*m
        return annotate(comp, rects[si], foc, t-t0)

    def frame(t):
        if t >= win[-1][1]:
            return bases[-1].astype(np.uint8)
        # 当前张 / 间隙
        si = 0
        for k, (s, e) in enumerate(win):
            if t < e or k == len(win)-1:
                si = k; break
        s, e = win[si]
        if si > 0 and t < s:   # 间隙：上一张->本张 交叉淡入
            ps, pe = win[si-1]
            a = min(max((t-pe)/max(s-pe, 1e-3), 0), 1)
            return (bases[si-1]*(1-a) + bases[si]*a).astype(np.uint8)
        return np.clip(render_slide(si, min(t, e)), 0, 255).astype(np.uint8)

    if stills:
        for si in range(len(SLIDES)):
            if only is not None and si != only:
                continue
            tmid = (win[si][0]+win[si][1])/2
            items = foclists[si]
            ts = [ (it[0]+it[1])/2 for it in items ] or [tmid]
            for j, tt in enumerate(ts):
                Image.fromarray(frame(tt)).save(f"_frames/show_{NAME}_s{si+1:02d}_{j}.png")
        print("stills saved"); return

    # 字幕（下边栏）
    fnt = font(FONT, 46); cache = {}
    def sub_wrap(txt):
        img = Image.new("RGBA", (4, 4)); d = ImageDraw.Draw(img)
        maxw = W-180; lines, cur = [], ""
        if " " in txt:
            for w in txt.split(" "):
                t = (cur+" "+w).strip()
                if d.textbbox((0, 0), t, font=fnt)[2] > maxw and cur: lines.append(cur); cur = w
                else: cur = t
        else:
            for ch in txt:
                if d.textbbox((0, 0), cur+ch, font=fnt)[2] > maxw and cur: lines.append(cur); cur = ch
                else: cur += ch
        if cur: lines.append(cur)
        return lines

    # 长句分页：超过2行的字幕按各页字数占时长比例切成多页，跟读翻页，不丢字
    pcues = []
    for s, e, txt in cues:
        if not txt: continue
        pl = sub_wrap(txt)
        pages = [pl[i:i+2] for i in range(0, len(pl), 2)]
        if len(pages) == 1:
            pcues.append((s, e, "\n".join(pages[0])))
        else:
            wts = [len("".join(p)) for p in pages]; wsum = sum(wts); t0 = s
            for pi, (p, wgt) in enumerate(zip(pages, wts)):
                t1 = e if pi == len(pages)-1 else t0 + (e-s)*wgt/wsum
                pcues.append((t0, t1, "\n".join(p))); t0 = t1

    def sub_render(txt):
        img = Image.new("RGBA", (W, BOT_H), (0, 0, 0, 0)); d = ImageDraw.Draw(img)
        lines = txt.split("\n")
        lh = 46+10; tot = lh*len(lines); y = (BOT_H-tot)//2
        for l in lines:
            w = d.textbbox((0, 0), l, font=fnt)[2]
            d.text(((W-w)//2, y), l, font=fnt, fill=(255, 248, 235, 255)); y += lh
        return np.array(img)
    def sub_frame(t):
        for s, e, txt in pcues:
            if s <= t < e and txt:
                if txt not in cache: cache[txt] = sub_render(txt)
                return cache[txt]
        return np.zeros((BOT_H, W, 4), np.uint8)

    # 音频：响度归一化（解说 -16 / 音乐 -28 / 整体 -14 LUFS），而非固定百分比
    padded = f"_{NAME}_padded.mp3"
    subprocess.run(["ffmpeg", "-y", "-i", f"{NAME}_audio.mp3", "-af",
                    f"apad=pad_dur={OUTRO}", "-q:a", "2", padded], capture_output=True)
    mixwav = f"_{NAME}_mix.wav"
    fout = max(total-2.5, 0)
    if MUSIC and os.path.exists(MUSIC):
        fc = (f"[0:a]loudnorm=I=-16:TP=-1.5:LRA=11[n];"
              f"[1:a]loudnorm=I=-35:TP=-2:LRA=11,apad,atrim=0:{total:.3f},"
              f"afade=t=in:st=0:d=1.5,afade=t=out:st={fout:.3f}:d=2.5[m];"
              f"[n][m]amix=inputs=2:duration=first:normalize=0[mx];"
              f"[mx]acompressor=threshold=-18dB:ratio=3:attack=15:release=250,"
              f"loudnorm=I=-14:TP=-1.0:LRA=11[out]")
        subprocess.run(["ffmpeg", "-y", "-i", padded, "-stream_loop", "-1", "-i", MUSIC,
                        "-filter_complex", fc, "-map", "[out]", "-ar", "44100",
                        mixwav], capture_output=True)
    else:
        subprocess.run(["ffmpeg", "-y", "-i", padded, "-af",
                        "acompressor=threshold=-18dB:ratio=3:attack=15:release=250,"
                        "loudnorm=I=-14:TP=-1.0:LRA=11", "-ar", "44100", mixwav],
                       capture_output=True)
    audio = AudioFileClip(mixwav).with_duration(total)

    sclip = VideoClip(frame, duration=total)
    subclip = VideoClip(sub_frame, duration=a_dur).with_position(("center", H-BOT_H))
    final = CompositeVideoClip([sclip, subclip], size=(W, H)).with_audio(audio).with_duration(total)
    final.write_videofile(f"{NAME}.mp4", fps=24, codec="libx264", audio_codec="aac",
                          threads=4, preset="medium")
    print("done:", f"{NAME}.mp4", f"{total:.1f}s")


if __name__ == "__main__":
    only = int(sys.argv[sys.argv.index("--slide")+1])-1 if "--slide" in sys.argv else None
    main(stills="--stills" in sys.argv, only=only)
