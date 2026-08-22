# -*- coding: utf-8 -*-
"""
配音 + 字幕生成（可复用流程）
逐句用 edge-tts 合成 -> 句间插停顿 -> ffmpeg 精确拼接 -> 输出对齐 srt

用法:
  python build_audio_srt.py --name awakening --voice zh-CN-YunxiNeural
  python build_audio_srt.py --name awakening_en --voice en-US-EricNeural --src lines_en.txt

句子来源:
  --from-srt xxx.srt  : 复用已有 srt 的每条文本作为分句（默认 awakening_subs.srt）
  --src xxx.txt       : 每行一句的纯文本

输出: {name}_audio.mp3, {name}_subs.srt
"""
import argparse
import asyncio
import os
import re
import subprocess
import tempfile
import time

import edge_tts

SCRATCH = tempfile.mkdtemp(prefix="tts_")


def cues_from_srt(path):
    text = open(path, encoding="utf-8").read()
    out = []
    for b in re.split(r"\n\s*\n", text.strip()):
        lines = b.strip().splitlines()
        ts = next((i for i, l in enumerate(lines) if "-->" in l), None)
        if ts is None:
            continue
        t = " ".join(lines[ts + 1:]).strip()
        if t:
            out.append(t)
    return out


def cues_from_txt(path):
    return [l.strip() for l in open(path, encoding="utf-8") if l.strip()]


def ffprobe_dur(path):
    r = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=nokey=1:noprint_wrappers=1", path],
        capture_output=True, text=True)
    return float(r.stdout.strip())


def srt_ts(sec):
    h = int(sec // 3600); sec -= h * 3600
    m = int(sec // 60); sec -= m * 60
    s = int(sec); ms = int(round((sec - s) * 1000))
    if ms == 1000:
        s += 1; ms = 0
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


async def synth(text, voice, rate, out):
    await edge_tts.Communicate(text, voice, rate=rate).save(out)


def synth_retry(text, voice, rate, out, tries=8):
    # edge-tts 偶发 NoAudioReceived（服务端掉线/限流），整条重跑代价大，逐句重试兜底
    for k in range(tries):
        try:
            asyncio.run(synth(text, voice, rate, out))
            return
        except Exception as e:
            if k == tries - 1:
                raise
            print(f"    重试{k + 1}: {type(e).__name__}", flush=True)
            time.sleep(min(5 * (k + 1), 30))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--name", required=True)
    ap.add_argument("--voice", required=True)
    ap.add_argument("--rate", default="-8%")
    ap.add_argument("--gap", type=float, default=0.30, help="句间停顿秒")
    ap.add_argument("--from-srt", default="awakening_subs.srt")
    ap.add_argument("--src", default=None)
    args = ap.parse_args()

    cues = cues_from_txt(args.src) if args.src else cues_from_srt(args.from_srt)
    print(f"分句 {len(cues)} 条, voice={args.voice}, rate={args.rate}, gap={args.gap}s")

    # 1. 逐句合成
    segs = []
    for i, c in enumerate(cues):
        p = os.path.join(SCRATCH, f"seg_{i:03d}.mp3")
        synth_retry(c, args.voice, args.rate, p)
        segs.append(p)
        print(f"  [{i+1}/{len(cues)}] {c[:18]}...")

    durs = [ffprobe_dur(p) for p in segs]

    # 2. 生成停顿静音
    sil = os.path.join(SCRATCH, "sil.mp3")
    subprocess.run(["ffmpeg", "-y", "-f", "lavfi", "-i",
                    "anullsrc=channel_layout=mono:sample_rate=24000",
                    "-t", str(args.gap), "-q:a", "9", sil],
                   capture_output=True)

    # 3. 拼接（concat 滤镜，重编码保证精确）
    inputs = []
    order = []
    for i, p in enumerate(segs):
        inputs += ["-i", p]
        order.append(i)
    sil_idx = len(segs)
    inputs += ["-i", sil]

    parts = []
    for i in order:
        parts.append(f"[{i}:a]")
        if i != order[-1]:
            parts.append(f"[{sil_idx}:a]")
    filt = "".join(parts) + f"concat=n={len(parts)}:v=0:a=1[out]"
    out_audio = f"{args.name}_audio.mp3"
    subprocess.run(["ffmpeg", "-y", *inputs, "-filter_complex", filt,
                    "-map", "[out]", "-q:a", "2", out_audio],
                   capture_output=True)
    print("音频:", out_audio, f"{ffprobe_dur(out_audio):.1f}s")

    # 4. 生成 srt（含句间停顿偏移）
    lines = []
    t = 0.0
    for i, (c, d) in enumerate(zip(cues, durs), 1):
        start, end = t, t + d
        lines.append(f"{i}\n{srt_ts(start)} --> {srt_ts(end)}\n{c}\n")
        t = end + args.gap
    out_srt = f"{args.name}_subs.srt"
    open(out_srt, "w", encoding="utf-8").write("\n".join(lines))
    print("字幕:", out_srt)


if __name__ == "__main__":
    main()
