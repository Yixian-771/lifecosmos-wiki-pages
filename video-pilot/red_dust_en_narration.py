# -*- coding: utf-8 -*-
"""
"Red Dust" narration (for The Anatomy and Transcendence of Red Dust, 12 EN slides).
Each entry = (slide image, [sentences]). One sentence = one subtitle cue;
a slide's on-screen window = first sentence start -> last sentence end.
Tone: Eric — calm, measured, warm but grounded.
"""

NAME = "red_dust_en_show"
VOICE = "en-US-GuyNeural"
FONT = r"C:\Windows\Fonts\segoeuil.ttf"   # Segoe UI Light
FONT_BD = r"C:\Windows\Fonts\segoeui.ttf"
RATE = "+0%"
MUSIC = "F:/音乐/国外经典/安妮的仙境 Anne's Wonderland.MP3"
WATERMARK = "LIFECHAN"

# 金句 + 聚光灯/圈框（坐标为相对幻灯比例；英文版式不同于中文）
META = [
    # 1 封面
    {"quote": "The Red Dust: not a place, but the architecture of entanglement"},
    # 2 结构·同心情感网（4句）
    {"quote": "At the center of the web sits the husband-and-wife bond", "focuses": [
        {"at": 1, "spot": (0.55, 0.12, 0.99, 0.95)},
        {"at": 2, "ring": (0.715, 0.51, 0.075, 0.10)},
        {"at": 3, "spot": (0.07, 0.73, 0.52, 0.93)},
    ]},
    # 3 迷宫 + 大染缸（3句）
    {"quote": "An endless maze, and a great dye vat — none escape the staining", "focuses": [
        {"at": 1, "spot": (0.04, 0.28, 0.48, 0.96)},
        {"at": 2, "spot": (0.50, 0.28, 0.95, 0.96)},
    ]},
    # 4 新窗口·非心如死灰（4句）
    {"quote": "Seeing through is not ashes — it's a new opening", "focuses": [
        {"at": 1, "spot": (0.02, 0.52, 0.31, 0.90)},
        {"at": 2, "spot": (0.60, 0.24, 0.99, 0.74)},
        {"at": 3, "ring": (0.50, 0.30, 0.10, 0.14)},
    ]},
    # 5 在尘修炼·觉悟·应用（5句）
    {"quote": "Powers are useless unless applied within the Red Dust", "focuses": [
        {"at": 1, "ring": (0.30, 0.45, 0.13, 0.11)},
        {"at": 2, "ring": (0.50, 0.31, 0.13, 0.11)},
        {"at": 3, "ring": (0.72, 0.23, 0.13, 0.11)},
        {"at": 4, "spot": (0.66, 0.66, 0.99, 0.96)},
    ]},
    # 6 结构性错配表（5句）
    {"quote": "Environment decides the product — the Red Dust yields ordinary people", "focuses": [
        {"at": 1, "spot": (0.63, 0.20, 0.99, 0.83)},
        {"at": 2, "spot": (0.335, 0.20, 0.625, 0.83)},
        {"at": 4, "box": (0.03, 0.85, 0.98, 0.99)},
    ]},
    # 7 垃圾堆生蝇·第二家园（4句）
    {"quote": "A garbage heap breeds flies, not bees", "focuses": [
        {"at": 1, "spot": (0.05, 0.25, 0.48, 0.86)},
        {"at": 2, "spot": (0.50, 0.25, 0.94, 0.86)},
        {"at": 3, "box": (0.06, 0.88, 0.96, 0.99)},
    ]},
    # 8 四大引力·漏斗（5句）
    {"quote": "Four anchors pull you back into the mundane", "focuses": [
        {"at": 1, "spot": (0.03, 0.34, 0.37, 0.54)},
        {"at": 2, "spot": (0.05, 0.62, 0.41, 0.84)},
        {"at": 3, "spot": (0.62, 0.36, 0.98, 0.56)},
        {"at": 4, "spot": (0.59, 0.64, 0.98, 0.86)},
    ]},
    # 9 人仙·三态（4句）
    {"quote": "No supernatural powers — only the absence of attachment", "focuses": [
        {"at": 1, "spot": (0.07, 0.58, 0.35, 0.96)},
        {"at": 2, "spot": (0.37, 0.58, 0.63, 0.96)},
        {"at": 3, "spot": (0.65, 0.58, 0.93, 0.96)},
    ]},
    # 10 终极轨迹·五站（5句）
    {"quote": "Out of the Red Dust, toward the Celestial Islands", "focuses": [
        {"at": 1, "ring": (0.15, 0.55, 0.10, 0.12)},
        {"at": 2, "ring": (0.38, 0.62, 0.14, 0.13)},
        {"at": 3, "ring": (0.62, 0.45, 0.12, 0.12)},
        {"at": 4, "ring": (0.80, 0.31, 0.11, 0.13)},
    ]},
    # 11 金句·咏雪莲
    {"quote": "I am a rare flower of the Kingdom of Heaven"},
    # 12 框架总览（5句）
    {"quote": "Structure, environment, limitation, liberation", "focuses": [
        {"at": 1, "spot": (0.04, 0.20, 0.47, 0.49)},
        {"at": 2, "spot": (0.50, 0.20, 0.97, 0.49)},
        {"at": 3, "spot": (0.04, 0.53, 0.47, 0.95)},
        {"at": 4, "spot": (0.50, 0.53, 0.97, 0.95)},
    ]},
]

SLIDES = [
    ("slides_rd_en/slide_01.png", [
        "Let's look at one of the most familiar ideas in Eastern thought — the Red Dust.",
        "We usually picture it as the bustling mundane world: cities, crowds, the noise of ordinary life.",
        "But here it's defined far more precisely — not as a place, but as the very architecture of human entanglement. Let's take it apart.",
    ]),
    ("slides_rd_en/slide_02.png", [
        "Start with the structure itself.",
        "The Red Dust isn't a location — it's the Thirty-Six Bagua Formations, an invisible lattice. To live in the mundane world is to live inside these formations.",
        "And at the very center sits the strongest, hardest formation to break: the Emotion Web, with the husband-and-wife bond at its absolute core.",
        "The warning is blunt — if that web is never seen through, we stay adrift, circling the Red Dust forever, and never reach the ideal shore.",
    ]),
    ("slides_rd_en/slide_03.png", [
        "From the inside, this environment behaves in two ways at once.",
        "First, an endless maze. The connections run so deep that untangling them while still living inside is physically impossible — like lifting yourself off the ground by pulling your own hair.",
        "Second, a great dye vat. From emperors to beggars, almost everyone is quietly calculating for their own benefit; stay long enough and you stop noticing the stench — no one inside escapes the staining.",
    ]),
    ("slides_rd_en/slide_04.png", [
        "Now, an important correction.",
        "Seeing through the Red Dust does not mean turning your heart to ashes, or giving up on life — that's the great misconception. Hiding in the city as a bitter hermit only breeds cunning.",
        "The true objective is the opposite: to find a new opening, and step into the realm of the celestial — living out your truest nature, free and unburdened.",
        "Liberation isn't resignation. It's an opening.",
    ]),
    ("slides_rd_en/slide_05.png", [
        "So why not just escape — retreat to a mountain and cultivate in peace? Because spiritual power is useless unless it works inside the Red Dust.",
        "The teaching gives a loop. First, cultivate in the Red Dust — developing concentration and wisdom.",
        "Then awaken in the Red Dust — seeing through the illusions.",
        "And finally, apply it in the Red Dust — testing your non-attachment against the real ordeal.",
        "That's the mandate: buddhahood has to happen right where you stand — flying over the ordeals, not avoiding them.",
    ]),
    ("slides_rd_en/slide_06.png", [
        "Go deeper, and you find a structural mismatch — the reason the Red Dust simply cannot produce celestial beings.",
        "In the reality of the Red Dust, the mind is paralyzed by worry and the fear of survival, burdened by possessions and obligations, bound by laws and family ties, perpetually chasing desire.",
        "Celestial nature is the exact inverse: no dwelling, no obstruction, no self, owning nothing, flowing freely, united with the Tao.",
        "The two simply don't line up.",
        "And the insight is sobering — across thousands of years, the success rate of cultivating to buddhahood inside the Red Dust is very nearly zero.",
    ]),
    ("slides_rd_en/slide_07.png", [
        "Put it plainly: just as a garbage heap produces flies rather than bees, the mundane environment only yields ordinary people.",
        "Marriage and the traditional family structure don't hold the conditions needed to produce Buddhas — they produce ordinary people. That's not a judgment; it's the soil.",
        "To grow a mind of no dwelling and no obstruction, the seed of Buddha-nature needs different ground — the specialized soil of the Second Home.",
        "It's an environmental law: a seed only germinates, flowers, and bears fruit when the soil conditions are exactly right.",
    ]),
    ("slides_rd_en/slide_08.png", [
        "And four distinct gravitational forces keep pulling practitioners back into the mundane matrix.",
        "Anchor one — the Emotion Web, the core barrier binding the heart to earthly attachments.",
        "Anchor two — craving life and fearing death; that primal greed directly blocks the way to the Kingdom of Heaven.",
        "Anchor three — leaving the team; venturing out alone, you're swiftly swallowed and drift backward into mediocrity.",
        "And anchor four — transgression; break the principles of a free environment, and you're cast right back down into the mundane world.",
    ]),
    ("slides_rd_en/slide_09.png", [
        "So what does someone who's made it actually look like? Here's the surprise.",
        "The human-celestial state involves no magical powers at all — their entire strength lies in seeing through the illusions of the world.",
        "Theirs is a weightless mind: country, nationality, family, party, religion no longer weigh on them; they simply act as the moment requires.",
        "And the floating mist — wealth, status, reputation seen as passing clouds; success and failure, winning and losing, all experienced as life's drifting mist.",
    ]),
    ("slides_rd_en/slide_10.png", [
        "Trace the whole arc, and life follows one ultimate trajectory — out of the Red Dust, toward the Celestial Islands.",
        "It begins at the home of heart and spirit — Lifechanyuan.",
        "From there: cross the rolling Red Dust, then return all the way to the Source of life.",
        "Further on, merge completely with the Tao —",
        "and arrive, at last, on the Celestial Islands Continent. As the declaration goes: no trace left in the mundane world, no imprint in the Red Dust — a nightmare finally over; wake up and rejoice.",
    ]),
    ("slides_rd_en/slide_11.png", [
        "And here Guide Xuefeng captures the whole spirit of it in a few lines.",
        "I am a rare flower of the Kingdom of Heaven, untouched by the smoke and blossoms of Red Dust;",
        "alone and beautiful amid a thousand miles of ice, unfolding with celestial grace.",
    ]),
    ("slides_rd_en/slide_12.png", [
        "Pull it all together, and you have one framework for transcending the Red Dust.",
        "Its ontology — the structure — is the Thirty-Six Bagua Formations, anchored by the Husband-Wife Emotion Web at the center.",
        "Its environment is an infinite maze driven by universal selfishness, staining all who remain inside.",
        "Its limitation: this soil is hostile to a mind of no dwelling — marriage and family yield ordinary people, not Buddhas.",
        "And its liberation needs the soil of the Second Home: absolute non-attachment, moving with your original nature, returning to the Source of life.",
    ]),
]
