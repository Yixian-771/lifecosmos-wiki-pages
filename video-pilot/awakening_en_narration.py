# -*- coding: utf-8 -*-
"""
"Awakening" narration (for The Architecture of Awakening, 15 EN slides).
Each entry = (slide image, [sentences]). One sentence = one subtitle cue;
a slide's on-screen window = first sentence start -> last sentence end.
Tone: Eric — calm, measured, warm but grounded.
"""

NAME = "awakening_en_show"
VOICE = "en-US-GuyNeural"
FONT = r"C:\Windows\Fonts\segoeuil.ttf"   # Segoe UI Light
FONT_BD = r"C:\Windows\Fonts\segoeui.ttf"
RATE = "+0%"
MUSIC = "F:/音乐/国外经典/安妮的仙境 Anne's Wonderland.MP3"
WATERMARK = "LIFECHAN"

# 金句 + 聚光灯/圈框（坐标为相对幻灯比例；英文版式不同于中文）
META = [
    # 1 封面禅圆
    {"quote": "Awakening: the leap from fog to clarity"},
    # 2 方程式（6句）
    {"quote": "Perception is feeling; understanding is knowing why", "focuses": [
        {"at": 1, "spot": (0.02, 0.30, 0.40, 0.66)},
        {"at": 2, "spot": (0.38, 0.30, 0.72, 0.66)},
        {"at": 3, "ring": (0.86, 0.46, 0.11, 0.09)},
    ]},
    # 3 台阶（6句：2 Survival,3 Direction,4 Cosmic Law,5 Buddhahood）
    {"quote": "Awakening isn't a switch — it's a staircase", "focuses": [
        {"at": 2, "box": (0.10, 0.74, 0.30, 0.92), "ring": (0.42, 0.80, 0.12, 0.07), "line": True},
        {"at": 3, "box": (0.05, 0.47, 0.27, 0.63), "ring": (0.47, 0.64, 0.11, 0.06), "line": True},
        {"at": 4, "box": (0.70, 0.47, 0.97, 0.63), "ring": (0.58, 0.50, 0.11, 0.06), "line": True},
        {"at": 5, "box": (0.70, 0.24, 0.97, 0.40), "ring": (0.66, 0.37, 0.12, 0.07), "line": True},
    ]},
    # 4 对比表（4句）
    {"quote": "The awakened flow like water; the unawakened stay stuck", "focuses": [
        {"at": 1, "spot": (0.03, 0.22, 0.49, 0.96)},
        {"at": 3, "spot": (0.51, 0.22, 0.97, 0.96)},
    ]},
    # 5 孤独检验（氛围图）
    {"quote": "The awakened are never lonely"},
    # 6 八觉·个人维度（6句：3 Life,4 Birth&Death,5 Cause&Effect）
    {"quote": "You are far larger than your body", "focuses": [
        {"at": 3, "spot": (0.04, 0.55, 0.40, 0.93)},
        {"at": 4, "spot": (0.34, 0.40, 0.68, 0.80)},
        {"at": 5, "spot": (0.60, 0.26, 0.98, 0.64)},
    ]},
    # 7 八觉·宇宙维度（4句：1 Space,2 Karmic,3 Heart-Nature）
    {"quote": "Reality is a projection of consciousness", "focuses": [
        {"at": 1, "spot": (0.04, 0.55, 0.40, 0.93)},
        {"at": 2, "spot": (0.34, 0.40, 0.68, 0.80)},
        {"at": 3, "spot": (0.60, 0.26, 0.98, 0.64)},
    ]},
    # 8 八觉·终极维度·源头（5句）
    {"quote": "Know the source, and every gate opens", "focuses": [
        {"at": 2, "ring": (0.80, 0.34, 0.12, 0.11)},
    ]},
    # 9 借力·圣贤（5句）
    {"quote": "One lifetime is too short — learn to borrow", "focuses": [
        {"at": 3, "spot": (0.04, 0.44, 0.98, 0.80)},
    ]},
    # 10 两座山
    {"quote": "Two mountains block the path"},
    # 11 鸟笼（5句）
    {"quote": "Don't let society's labels become a cage", "focuses": [
        {"at": 0, "spot": (0.58, 0.18, 0.99, 0.95)},
        {"at": 3, "ring": (0.80, 0.54, 0.11, 0.16)},
    ]},
    # 12 心之牢笼·情绪（4句）
    {"quote": "Walk out of your inner Egypt", "focuses": [
        {"at": 1, "spot": (0.28, 0.45, 0.99, 0.96)},
    ]},
    # 13 解放的机制（3句）
    {"quote": "Awakening is a predictable process", "focuses": [
        {"at": 1, "spot": (0.02, 0.40, 0.45, 0.95)},
        {"at": 2, "ring": (0.82, 0.46, 0.14, 0.12)},
    ]},
    # 14 终点·喜悦（夕阳）
    {"quote": "One day of joy is one day as a celestial being"},
    # 15 结尾禅圆
    {"quote": "The choice to climb is yours"},
]

SLIDES = [
    ("slides_arch_en/slide_01.png", [
        "Ever notice how the same setback can break one person and barely touch another? The difference usually comes down to one word.",
        "Let's talk about one idea — awakening.",
        "A lot of people picture it as a sudden bolt of lightning, the moment everything clicks.",
        "But it's far more precise than that. Let's take it apart, one layer at a time.",
    ]),
    ("slides_arch_en/slide_02.png", [
        "The word awakening is really two things joined together.",
        "Perception — what your eyes, ears, and intuition take in.",
        "And understanding — thinking it through until you genuinely know why.",
        "Put them together, and you get awakening.",
        "Most people get stuck right here: they perceive, but never follow through to understanding.",
        "A breeze drifts past; you feel it — but how rarely do you ask why you can feel it at all.",
    ]),
    ("slides_arch_en/slide_03.png", [
        "And awakening isn't a switch that's simply on or off.",
        "It's a staircase, climbed one step at a time.",
        "The lowest step is understanding that to live, you need food, shelter, and clothing.",
        "Higher up: telling right from wrong, and finding direction instead of drifting.",
        "Higher still: grasping how the universe works, and moving within the Tao.",
        "And at the very top — buddhahood, total clarity.",
    ]),
    ("slides_arch_en/slide_04.png", [
        "So what separates the awakened from the unawakened?",
        "The awakened move through life with ease, handling things step by step,",
        "and bringing a little light wherever they go.",
        "The unawakened get stuck, tangled in confusion, circling the same ground again and again.",
    ]),
    ("slides_arch_en/slide_05.png", [
        "And here's a strikingly simple test.",
        "A truly awakened person is never lonely.",
        "If you still feel isolated, that's clear proof the awakening isn't complete.",
        "The awakened state feels full and at ease — whether you're entirely alone, or deep within a crowd.",
    ]),
    ("slides_arch_en/slide_06.png", [
        "Go deeper, and awakening becomes a system of eight specific realizations,",
        "carrying you from human to celestial.",
        "The first three loosen the grip of the physical body.",
        "Life: you are far larger than your body.",
        "Birth and death: the body is just a boat, and you are the traveler.",
        "Cause and effect: plant melons, and you harvest melons.",
    ]),
    ("slides_arch_en/slide_07.png", [
        "The next three expand outward, beyond the visible world.",
        "Space: not one world, but twenty parallel ones, across thirty-six dimensions.",
        "Karmic affinity: the invisible coordinates of where you're headed.",
        "And heart-nature — the realization that reality is a projection of your own consciousness.",
    ]),
    ("slides_arch_en/slide_08.png", [
        "And the last two reach all the way to the root.",
        "Everything has a source.",
        "Know the source, and all eighty-four thousand gates of wisdom open.",
        "Miss it, and every path ends at a cliff.",
        "The end of awakening is simply recognizing that original truth.",
    ]),
    ("slides_arch_en/slide_09.png", [
        "But here's the problem: one human lifetime is far too short to figure this out alone.",
        "Time and energy run out.",
        "So the wise approach is to borrow — to draw on the accumulated light of those who came before.",
        "The wisdom of Jesus, of Buddha, of Laozi; the laws uncovered by science.",
        "Absorb them, and add a heart that stays steady and seeks only truth.",
    ]),
    ("slides_arch_en/slide_10.png", [
        "Before that road opens, though, two great mountains stand in the way.",
        "Both are forms of bondage — one imposed from outside, the other built within.",
        "To reach the shore of freedom, both must be dismantled.",
    ]),
    ("slides_arch_en/slide_11.png", [
        "The first mountain is the cage built by society —",
        "family, nation, ethnicity, religion, profession.",
        "None of these are evil in themselves.",
        "But if you let them define you completely, they become a cage you can't step out of.",
        "And heaven has no customs checkpoint for nationality or creed.",
    ]),
    ("slides_arch_en/slide_12.png", [
        "The second mountain is the harder one — the bondage inside the heart.",
        "Jealousy, comparison, complaint, arrogance, anger, greed.",
        "As long as you carry these burdens, you remain enslaved in your own inner Egypt.",
        "Freedom means walking out of it.",
    ]),
    ("slides_arch_en/slide_13.png", [
        "Put it all together, and awakening turns out to be a predictable process.",
        "The right inputs — a cleared heart, and borrowed wisdom — processed through the eight awakenings.",
        "The output is liberation: a permanent departure from the sea of suffering, to the shore of freedom.",
    ]),
    ("slides_arch_en/slide_14.png", [
        "So what is all of this ultimately for?",
        "It comes down to one thing — joy.",
        "The most important thing in life is to be happy, unburdened by cages or a heavy heart.",
        "As the saying goes: one day of joy is one day lived as a celestial being.",
    ]),
    ("slides_arch_en/slide_15.png", [
        "The steps are built. The wisdom is available.",
        "The ultimate expression of life is perpetual clarity —",
        "and the choice to step onto the staircase is entirely yours.",
    ]),
]
