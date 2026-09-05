# -*- coding: utf-8 -*-
"""比对 wiki 里的幻灯图集 vs 百科图片版的当前无水印图：内容是否同一版。"""
import json, re, os
from pathlib import Path
from PIL import Image, ImageChops
import numpy as np

W = Path(r'F:\百科馆\lifecosmos-wiki-pages')
IMG = Path(r'F:\百科馆\百科图片版')
SC = Path(r'E:\CodexData\temp\claude\F-----\119a44a8-4965-4117-adff-776ab2c516be\scratchpad\wiki_scan.json')
d = json.loads(SC.read_text(encoding='utf-8'))
s2e = {k: v for k, v in d['slug2ep'].items()}

# 百科图片版 目录按序号归类
dirs = {}
for p in IMG.iterdir():
    if not p.is_dir(): continue
    m = re.match(r'^(\d{3})_', p.name)
    if not m: continue
    ep = int(m.group(1))
    lang = 'zh' if '（' in p.name else 'en'
    dirs.setdefault(ep, {})[lang] = p

def diff(a, b):
    ia = Image.open(a).convert('RGB'); ib = Image.open(b).convert('RGB')
    ia = ia.resize((320, 180)); ib = ib.resize((320, 180))
    return float(np.abs(np.asarray(ia, float) - np.asarray(ib, float)).mean())

rows = []
for slug, info in d['pages'].items():
    if slug not in s2e: continue
    ep = s2e[slug][0]
    for lang in ('zh', 'en'):
        sd = W / lang / slug / 'slides'
        if not sd.is_dir(): continue
        wf = sorted(sd.glob('*.jpg'))
        src = dirs.get(ep, {}).get(lang)
        if not src:
            rows.append((ep, slug, lang, len(wf), -1, None, '无源目录')); continue
        sf = sorted(src.glob('*.jpg')) or sorted(src.glob('*.png'))
        note = ''
        if len(wf) != len(sf): note = f'页数 {len(wf)}≠{len(sf)}'
        n = min(len(wf), len(sf))
        ds = [diff(wf[i], sf[i]) for i in range(n)]
        mx = max(ds) if ds else 0
        rows.append((ep, slug, lang, len(wf), len(sf), mx, note))

print(f'{"ep":>4} {"lang":<4} {"wiki":>4} {"src":>4} {"maxdiff":>8}  note')
bad = 0
for r in sorted(rows):
    ep, slug, lang, nw, ns, mx, note = r
    flag = ''
    if note: flag = '✗'
    elif mx is not None and mx > 6: flag = '✗'
    if flag: bad += 1
    print(f'{ep:>4} {lang:<4} {nw:>4} {ns:>4} {("%.2f"%mx) if mx is not None else "-":>8}  {flag}{note} {slug if flag else ""}')
print(f'\n可疑 {bad} 项')
