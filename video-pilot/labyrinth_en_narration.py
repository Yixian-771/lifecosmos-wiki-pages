# -*- coding: utf-8 -*-
"""
"The Cosmic Labyrinth" narration (Taxonomy of the 36 Bagua Formations, 13 EN slides).
Each entry = (slide image, [sentences]). One sentence = one subtitle cue;
a slide's on-screen window = first sentence start -> last sentence end.
Tone: Eric — calm, measured, warm but grounded. Longer and unhurried: explain clearly.
"""

NAME = "labyrinth_en_show"
VOICE = "en-US-GuyNeural"
FONT = r"C:\Windows\Fonts\segoeuil.ttf"   # Segoe UI Light
FONT_BD = r"C:\Windows\Fonts\segoeui.ttf"
RATE = "+0%"
MUSIC = "F:/音乐/国外经典/安妮的仙境 Anne's Wonderland.MP3"
WATERMARK = "LIFECHAN"

# 金句 + 聚光灯/圈框（坐标为相对幻灯比例）
META = [
    # 1 封面
    {"quote": "The universe lays down thirty-six formations — see through them, and you are free"},
    # 2 Architecture of the Illusion（4句）
    {"quote": "Not mere obstacles — the systemic programs of the cosmos", "focuses": [
        {"at": 1, "spot": (0.02, 0.06, 0.62, 0.96)},
        {"at": 2, "box": (0.665, 0.43, 0.985, 0.82)},
        {"at": 3, "spot": (0.665, 0.84, 0.985, 0.99)},
    ]},
    # 3 Taxonomy of Confinement — 三球（5句，浅底）
    {"quote": "Three spheres of entanglement: cosmic, social, internal", "focuses": [
        {"at": 1, "spot": (0.04, 0.20, 0.46, 0.62)},
        {"at": 2, "ring": (0.625, 0.30, 0.105, 0.135)},
        {"at": 3, "ring": (0.525, 0.55, 0.105, 0.135)},
        {"at": 4, "ring": (0.725, 0.55, 0.105, 0.135)},
    ]},
    # 4 Sphere I · Gravity of Fate（5句）
    {"quote": "Cosmic law is the ultimate fixed number — resisting only breeds suffering", "focuses": [
        {"at": 1, "spot": (0.30, 0.18, 0.70, 0.92)},
        {"at": 2, "box": (0.71, 0.13, 0.985, 0.42)},
        {"at": 3, "box": (0.04, 0.40, 0.31, 0.73)},
        {"at": 4, "box": (0.71, 0.60, 0.985, 0.90)},
    ]},
    # 5 Time Formation — 逃脱三步（5句）
    {"quote": "Time only records the script — the True Self stands outside it", "focuses": [
        {"at": 1, "spot": (0.02, 0.50, 0.50, 0.92)},
        {"at": 2, "box": (0.71, 0.15, 0.985, 0.38)},
        {"at": 3, "box": (0.71, 0.42, 0.985, 0.64)},
        {"at": 4, "box": (0.71, 0.68, 0.985, 0.93)},
    ]},
    # 6 Sphere II · Webs of Affiliation（5句）
    {"quote": "Become a Citizen of Earth — serve all, belong to no faction", "focuses": [
        {"at": 1, "spot": (0.05, 0.18, 0.95, 0.66)},
        {"at": 2, "box": (0.055, 0.70, 0.49, 0.99)},
        {"at": 3, "box": (0.51, 0.70, 0.95, 0.99)},
    ]},
    # 7 Emotion Formation — 三组转化（5句，浅底）
    {"quote": "Of all formations, Emotion is the hardest to escape", "focuses": [
        {"at": 1, "ring": (0.18, 0.45, 0.13, 0.17)},
        {"at": 2, "box": (0.055, 0.78, 0.345, 0.93)},
        {"at": 3, "box": (0.355, 0.78, 0.645, 0.93)},
        {"at": 4, "box": (0.655, 0.78, 0.945, 0.93)},
    ]},
    # 8 Sphere III · Prison of the Psyche（5句）
    {"quote": "The mind itself does not exist — it is purely a formation", "focuses": [
        {"at": 1, "box": (0.05, 0.16, 0.32, 0.40)},
        {"at": 2, "spot": (0.34, 0.22, 0.70, 0.78)},
        {"at": 3, "box": (0.04, 0.72, 0.32, 0.96)},
        {"at": 4, "box": (0.745, 0.66, 0.985, 0.96)},
    ]},
    # 9 Wisdom Paradox（5句）
    {"quote": "Abandon cleverness, return to the uncarved simplicity", "focuses": [
        {"at": 1, "spot": (0.03, 0.16, 0.50, 0.80)},
        {"at": 2, "spot": (0.03, 0.82, 0.49, 0.99)},
        {"at": 3, "ring": (0.755, 0.42, 0.155, 0.21)},
        {"at": 4, "box": (0.515, 0.82, 0.985, 0.99)},
    ]},
    # 10 Dimensional Shift 表（5句，浅底）
    {"quote": "From the entangled human to the liberated celestial", "focuses": [
        {"at": 1, "box": (0.06, 0.25, 0.97, 0.38)},
        {"at": 2, "box": (0.06, 0.38, 0.97, 0.51)},
        {"at": 3, "box": (0.06, 0.51, 0.97, 0.65)},
        {"at": 4, "box": (0.06, 0.65, 0.97, 0.80)},
    ]},
    # 11 Synthesis（5句）
    {"quote": "You do not need thirty-six keys for thirty-six rooms", "focuses": [
        {"at": 1, "spot": (0.06, 0.28, 0.32, 0.74)},
        {"at": 2, "spot": (0.39, 0.28, 0.66, 0.74)},
        {"at": 3, "ring": (0.835, 0.50, 0.115, 0.16)},
        {"at": 4, "box": (0.515, 0.83, 0.985, 0.99)},
    ]},
    # 12 Master Key（5句）
    {"quote": "One master key: a clear, independent consciousness", "focuses": [
        {"at": 1, "ring": (0.265, 0.59, 0.075, 0.10)},
        {"at": 2, "box": (0.535, 0.40, 0.965, 0.55)},
        {"at": 3, "box": (0.535, 0.59, 0.965, 0.74)},
        {"at": 4, "box": (0.535, 0.78, 0.965, 0.97)},
    ]},
    # 13 收束
    {"quote": "The net is always open on one side — sail toward the ideal shore"},
]

SLIDES = [
    ("slides_lb_en/slide_01.png", [
        "Let's explore one of the most striking maps in the Lifechanyuan teaching — the Cosmic Labyrinth.",
        "The universe, it says, is laid out as thirty-six Bagua Formations — a taxonomy of confinement, and a path to liberation.",
        "It sounds elaborate, but the heart of it is simple: see through the formations, and you walk free. Let's take it apart, step by step.",
    ]),
    ("slides_lb_en/slide_02.png", [
        "Start with the architecture itself.",
        "These thirty-six formations are not mere obstacles in your way — they are the systemic programs of the cosmos, a heaven-spanning net designed to keep everything in orderly harmony.",
        "Think of it as a spider's web: it keeps each layer of life thriving in its assigned space, and it's the source of the whole cosmic game — power, fame, attraction, and emotion.",
        "But here is the mercy in it — the net is absolute, yet always left open on one side, for anyone who genuinely seeks the way out.",
    ]),
    ("slides_lb_en/slide_03.png", [
        "So where exactly do these formations catch us? They appear across three spheres of entanglement.",
        "The first sphere is cosmic — the physical and the destined: fate, time, space, gravity, structure, nature, fixed number, and life and death.",
        "The second is social — the relational webs of ethics, belonging, and emotion.",
        "And the third is internal — the psychological traps: desire, mind, intelligence, thinking, instinct, sloth, and wisdom.",
        "To transcend, you have to learn to walk through all three — the physical cosmos, the social fabric, and the inner psyche.",
    ]),
    ("slides_lb_en/slide_04.png", [
        "Let's enter the first sphere — the gravity of fate.",
        "The Fate Formation is a final accounting of past karmic information — a program of fixed numbers assigned to you at birth; complaining is futile, so accept it calmly while working toward the next elevation.",
        "The Gravity Formation is subtler: an antimatter gravity pulls souls together in proportion to mutual debt, and wherever that gravity is strongest, life reincarnates toward it.",
        "And the Structure and Space Formations confine us to the human environment — to escape, you must format out the human consciousness and install a celestial one.",
        "The lesson of this whole sphere: cosmic law is the ultimate fixed number, and resisting it only breeds needless suffering.",
    ]),
    ("slides_lb_en/slide_05.png", [
        "The most haunting of the cosmic traps is time.",
        "Time, the teaching says, is not a causal force — it's merely a recorder of material motion, and the human script of arising, abiding, and passing is already pre-written: birth, aging, illness, death.",
        "So how do you escape a script that's already written? First, shift the anchor — mentally place yourself in the Celestial Islands of the Elysium World, not in the human realm.",
        "Second, separate the observer from the actor — watch your human self as if watching a character in a film.",
        "And third, realize the True Self — the character in the drama is transient, but the observer is Buddha, is Nature, is celestial.",
    ]),
    ("slides_lb_en/slide_06.png", [
        "Now the second sphere — the webs of affiliation, the ties that bind us to the crowd.",
        "These are real bonds dissolving into open space, and there are two great formations here.",
        "The Belonging Formation feeds the human need not to feel like an aimless cloud — so consciousness attaches to nations, races, religions, parties, and clans; the escape is to become a Citizen of Earth, serving all humanity rather than drifting inside one isolated circle.",
        "The Ethics Formation, called Lun, traps us in generational rank, seniority, and social roles that keep us sleepwalking through reincarnations; the escape is to cultivate a complete, independent personality governed only by the Greatest Creator — while still repaying every necessary earthly debt.",
    ]),
    ("slides_lb_en/slide_07.png", [
        "And then the hardest formation of all to escape — emotion, or Qing.",
        "Every layer of life has its own emotion, and as long as your heart clings to one specific individual, you remain caught in the web.",
        "The way out is not to kill feeling, but to transmute it — dilute the parent-child bond, and deepen it into devotion to the Dao.",
        "Dilute the pull of sibling and friend, and deepen it into love for all things in the universe; dilute exclusive romantic attachment, and let it open into a free-flowing, celestial affection.",
        "The day will come when your heart has nothing left to cling to — and that is the day you've escaped the Emotion Formation.",
    ]),
    ("slides_lb_en/slide_08.png", [
        "The third sphere is the prison of the psyche — the traps we build inside our own minds.",
        "At the center is desire: humans carry eight great desires — food, sex, possessions, pleasure, life, fame, superiority, control — and desire works like a nose-ring on a bull, ensuring a lifetime of exhaustion and endless dissatisfaction.",
        "There's also the Sloth-and-Pleasure Formation — the cyclical gravity of ease, where the pursuit of comfort leads to decay, cycling endlessly from lowly to noble and back to lowly.",
        "And the deepest illusion of all is the Mind Formation, called Xin — the Buddha taught that past, present, and future mind cannot be grasped; the mind itself does not exist — it is purely a Bagua formation.",
    ]),
    ("slides_lb_en/slide_09.png", [
        "That leads straight into the wisdom paradox — and here intelligence itself becomes a trap.",
        "In the human world, the clever are flowers, not fruit — dazzling, yet the chase after cleverness only keeps people wandering deeper inside the formation, lost to vanity.",
        "Even wisdom is a trap: it's a golden treasure, yet a devourer of life's precious time, and a lifetime spent chasing knowledge is an unnatural detour.",
        "So what's the escape? The teaching calls it Hundun wisdom — abandon sageliness, discard cleverness, as Laozi said.",
        "Keep consciousness in a state of clear emptiness, and respond with equanimity — moving with nature, acting only as the moment calls.",
    ]),
    ("slides_lb_en/slide_10.png", [
        "Let's lay the two states side by side — the dimensional shift from human nature to celestial nature.",
        "In identity and belonging, the human is bound to nation, family, or faction; the celestial is a Citizen of Earth and the universe, unattached to any earthly side.",
        "In affection, the human is exclusive, clinging, possessive; the celestial is free-flowing and universal, anchored in the Dao and all living things.",
        "In state of mind, the human is fixed and grasping, endlessly pursuing cleverness; the celestial abides nowhere, format-cleared, resting in clear emptiness.",
        "And in action and instinct, the human is driven by survival programs and fixed patterns; the celestial flows with natural freedom, responding to affinities as they come.",
    ]),
    ("slides_lb_en/slide_11.png", [
        "Here's the synthesis — and it's a relief.",
        "You do not need thirty-six different keys to escape thirty-six different rooms.",
        "Watch the whole structure: the formations dissolve, and what remains is emptiness — the single root.",
        "Because every formation, cosmic, social, or internal, relies on one thing: a point of attachment.",
        "The moment attachment is severed, the complex knot of the universe dissolves — for the labyrinth was never built of stone; it was built of consciousness. The trap is the mind, and the escape is the mind.",
    ]),
    ("slides_lb_en/slide_12.png", [
        "Which gives us the master key — a clear, independent consciousness.",
        "To escape any formation, you keep a clear head amid confusing appearances, and grasp the absolute essence of things.",
        "First, establish a clear internal standard of consciousness — a fixed point of your own.",
        "Second, judge every phenomenon independently, completely unswayed by immediate interest, emotion, or earthly authority.",
        "And the ultimate test: let nothing — not wealth, not beauty, not scriptures, not masters, not gods, not even the Jade Emperor himself — move your soul from its direct alignment with the Greatest Creator.",
    ]),
    ("slides_lb_en/slide_13.png", [
        "So we return to the source.",
        "The net is always open on one side — there is always a way out for those who seek it.",
        "The thirty-six formations are the beautiful, complex game of the cosmos; treat everything as a game to be played, but hold fast to the hand of the Dao.",
        "Shed the heavy gravity of human nature, realize the clear emptiness of the celestial mind, and sail toward the ideal shore of life.",
    ]),
]
