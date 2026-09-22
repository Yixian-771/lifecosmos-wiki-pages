# -*- coding: utf-8 -*-
"""文字行搬移：背景取行上下的空白带逐列插值，字形 alpha 按与背景的差计算。"""
import numpy as np


def line_bg(a, y0, y1, x0, x1, pad=3):
    top = a[y0 - pad:y0, x0:x1].mean(0)
    bot = a[y1:y1 + pad, x0:x1].mean(0)
    k = 31
    ker = np.ones(k) / k
    sm = lambda v: np.stack([np.convolve(np.pad(v[:, c], k // 2, mode="edge"), ker, "valid") for c in range(3)], -1)
    top, bot = sm(top), sm(bot)
    t = np.linspace(0, 1, y1 - y0)[:, None, None]
    return top[None] * (1 - t) + bot[None] * t


def move_lines(a, lines, moves, x_range, lo=3, span=20):
    """lines=[(y0,y1)]：各行带（上下边界应落在行间空白里）；x_range=(X0,X1) 处理的横向范围。
    moves=[(line_idx, x0, x1, dx, dy)]：把该行 [x0,x1) 的字贴到 (x+dx, y+dy)；没列出的字形清掉。"""
    X0, X1 = x_range
    info = []
    for (y0, y1) in lines:
        bg = line_bg(a, y0, y1, X0, X1)
        reg = a[y0:y1, X0:X1].copy()
        al = np.clip((np.abs(reg - bg).max(-1) - lo) / span, 0, 1)
        # 向外扩 1 像素，带上抗锯齿的浅边
        grown = al.copy()
        for dy_, dx_ in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            grown = np.maximum(grown, np.roll(np.roll(al, dy_, 0), dx_, 1) * 0.7)
        al = grown
        info.append((y0, y1, reg, bg, al))
    for y0, y1, reg, bg, al in info:
        a[y0:y1, X0:X1] = reg * (1 - al[..., None]) + bg * al[..., None]
    for li, x0, x1, dx, dy in moves:
        y0, y1, reg, bg, al = info[li]
        lx0, lx1 = x0 - X0, x1 - X0
        seg = reg[:, lx0:lx1]
        sal = al[:, lx0:lx1][..., None]
        ty0, tx0 = y0 + dy, x0 + dx
        h, w = y1 - y0, lx1 - lx0
        tgt = a[ty0:ty0 + h, tx0:tx0 + w]
        a[ty0:ty0 + h, tx0:tx0 + w] = tgt * (1 - sal) + seg * sal
