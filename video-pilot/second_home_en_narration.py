# -*- coding: utf-8 -*-
"""
"Second Home" narration (for Second_Home, 13 EN slides).
Each entry = (slide image, [sentences]). One sentence = one subtitle cue;
a slide's on-screen window = first sentence start -> last sentence end.
Script is based on the EN entry (en/second-home/internal.md), following the
PDF's own "Utopian Blueprint / Oasis" framing — NOT a translation of the
Chinese script. Voice: Andrew — warm, steady, conversational.
First sentence = hook.
"""

NAME = "second_home_en_show"
VOICE = "en-US-AndrewNeural"
FONT = r"C:\Windows\Fonts\segoeuil.ttf"   # Segoe UI Light
FONT_BD = r"C:\Windows\Fonts\segoeui.ttf"
RATE = "+0%"
MUSIC = r"F:\百科馆\百科BGM\Pastoral Serenade.mp3"
WATERMARK = "LIFECHAN"

# quote + spotlight/box/ring focuses (coords are relative to the slide, at is 0-based)
META = [
    # 1 Cover: water-drop mandala
    {"quote": "A blueprint, not a daydream"},
    # 2 NOT / IS (4 sentences)
    {"quote": "Held together by nothing but resonance", "focuses": [
        {"at": 0, "spot": (0.03, 0.05, 0.48, 0.97)},
        {"at": 1, "spot": (0.52, 0.05, 0.97, 0.97)},
    ]},
    # 3 Paradigm table (5 sentences)
    {"quote": "Trouble is structural — so is the cure", "focuses": [
        {"at": 1, "box": (0.53, 0.33, 0.97, 0.45)},
        {"at": 2, "box": (0.53, 0.50, 0.97, 0.62)},
        {"at": 3, "box": (0.53, 0.64, 0.97, 0.77)},
        {"at": 4, "box": (0.53, 0.79, 0.97, 0.92)},
    ]},
    # 4 Hundun wheel (5 sentences)
    {"quote": "Let Dao manage — nobody rules", "focuses": [
        {"at": 0, "ring": (0.50, 0.50, 0.12, 0.20)},
        {"at": 2, "spot": (0.64, 0.14, 0.99, 0.92)},
        {"at": 3, "spot": (0.01, 0.14, 0.36, 0.95)},
    ]},
    # 5 Three spheres of daily life (4 sentences)
    {"quote": "One sacred room; everything else shared", "focuses": [
        {"at": 1, "spot": (0.03, 0.24, 0.21, 0.40)},
        {"at": 2, "spot": (0.67, 0.15, 0.99, 0.30)},
        {"at": 3, "spot": (0.72, 0.74, 0.99, 0.97)},
    ]},
    # 6 Qiankun Reversal (5 sentences)
    {"quote": "Freedom, with one iron rule", "focuses": [
        {"at": 1, "spot": (0.03, 0.28, 0.36, 0.90)},
        {"at": 3, "spot": (0.74, 0.16, 0.99, 0.46)},
    ]},
    # 7 Absolute transparency (4 sentences)
    {"quote": "No dark corners, no second chances", "focuses": [
        {"at": 1, "spot": (0.30, 0.24, 0.70, 0.40)},
        {"at": 2, "spot": (0.27, 0.66, 0.73, 0.82)},
    ]},
    # 8 Eight benefits grid (5 sentences)
    {"quote": "Eight gifts of the Oasis", "focuses": [
        {"at": 1, "spot": (0.06, 0.17, 0.50, 0.56)},
        {"at": 2, "spot": (0.52, 0.17, 0.96, 0.56)},
        {"at": 3, "spot": (0.06, 0.58, 0.50, 0.96)},
        {"at": 4, "spot": (0.52, 0.58, 0.96, 0.96)},
    ]},
    # 9 Earthly replica (4 sentences)
    {"quote": "An earthly copy of Heaven", "focuses": [
        {"at": 1, "spot": (0.25, 0.14, 0.75, 0.53)},
        {"at": 2, "spot": (0.25, 0.55, 0.75, 0.95)},
        {"at": 3, "spot": (0.76, 0.25, 0.99, 0.70)},
    ]},
    # 10 Carbon-silicon symbiosis (4 sentences)
    {"quote": "Carbon and silicon, one family", "focuses": [
        {"at": 2, "spot": (0.74, 0.30, 0.99, 0.75)},
        {"at": 3, "spot": (0.02, 0.32, 0.27, 0.62)},
    ]},
    # 11 Verified outcomes (4 sentences)
    {"quote": "Facts are the best touchstone", "focuses": [
        {"at": 1, "spot": (0.04, 0.17, 0.28, 0.93)},
        {"at": 2, "spot": (0.30, 0.56, 0.61, 0.94)},
        {"at": 3, "spot": (0.62, 0.17, 0.96, 0.53)},
    ]},
    # 12 The gate: entry steps (4 sentences)
    {"quote": "Alignment, not desire", "focuses": [
        {"at": 1, "spot": (0.07, 0.26, 0.34, 0.60)},
        {"at": 2, "spot": (0.37, 0.22, 0.96, 0.55)},
        {"at": 3, "spot": (0.59, 0.80, 0.99, 0.99)},
    ]},
    # 13 Closing lotus
    {"quote": "Dao, Humanity, Technology — in harmony"},
]

SLIDES = [
    ("slides_sh_en/slide_01.png", [
        "Ever notice how the things we work hardest to keep — the house, the savings, the family plans — are exactly the things we lose the most sleep over?",
        "Today, let's talk about Second Home — a utopian blueprint for New Era Humanity, created by Lifechanyuan.",
        "It's a real community model with no private ownership, no marriage, and no bosses — and, by its own account, far fewer of the troubles we've learned to call normal.",
        "Sounds impossible? Let's walk through the blueprint, one layer at a time.",
    ]),
    ("slides_sh_en/slide_02.png", [
        "First, the boundaries — because this is where the misunderstandings usually start: Second Home is not a political organization, not a religious group, not a charity, and not a refuge.",
        "So what is it? A voluntary, loose utopian collective of like-minded individuals, living by the 800 Values for New Era Humanity.",
        "It has no organizational structure, and no authority that supersedes constitutional law.",
        "In other words: nothing holds it together — nothing except resonance.",
    ]),
    ("slides_sh_en/slide_03.png", [
        "The Lifechanyuan teaching starts from a bold diagnosis: most human trouble is structural — it grows out of the way we organize life itself.",
        "So the blueprint swaps out the resource model: private ownership gives way to absolute sharing — all resources belong to the collective.",
        "The social unit: marriage and the nuclear family are replaced by global unity — one worldwide family.",
        "Governance: external laws and institutional rules give way to internal qualities — truth, goodness, beauty, love, faith, and sincerity.",
        "And leadership: authority and privilege are replaced by pure service — managers act solely as public servants.",
    ]),
    ("slides_sh_en/slide_04.png", [
        "The engine that runs it all has a curious name: Hundun Management — and its essence is non-management.",
        "Reduce human intervention to the minimum, and let Dao manage: order follows natural law, not human will.",
        "Around that hub sit eight spokes — on one side: no private ownership, the soil of human trouble removed; internal qualities over external rules; universal value creation — everyone creates wealth, no idlers; and management as service.",
        "On the other: unity of Heaven and humanity; voluntary self-discipline — contribute by ability, take by need; macro-micro harmony; and everything centered on the joy of LIFE.",
        "Eight spokes, one axle: when hearts align with Dao, nobody needs to be managed.",
    ]),
    ("slides_sh_en/slide_05.png", [
        "Zoom in to daily life, and the architecture splits into three spheres.",
        "The private sphere: one sacred, strictly private bedroom per member — the one space no one may violate.",
        "The public sphere: cafeteria-style communal dining, balanced vegetarian and meat options, and free-access warehouses for daily necessities — no rationing, no supervision.",
        "And the cultural sphere: monthly collective games, study sessions on Monday and Wednesday evenings, and Friday community life meetings — designed so engagement never stops.",
    ]),
    ("slides_sh_en/slide_06.png", [
        "Now, the part that raises eyebrows: love.",
        "The baseline: no marriage, and no fixed emotional or sexual dependency — intimacy is entirely free, based on mutual consent.",
        "Free, but not lawless: collective promiscuity is strictly forbidden.",
        "And one striking rule governs the whole field — the Qiankun Reversal: Celestial Maidens Supreme.",
        "Women hold the ultimate initiative: men may not initiate, may not harass women in any form, and are strictly forbidden from entering a woman's room uninvited.",
    ]),
    ("slides_sh_en/slide_07.png", [
        "Every utopia has a wall it will not let you cross. Here, that wall is transparency.",
        "The requirement of openness: sneaky, mysterious behavior is incompatible with the community — openness in all matters is the foundational principle of survival in Second Home.",
        "And beneath it, the zero-tolerance line: consciously causing spiritual, mental, or physical harm to another member means immediate, unhesitating expulsion.",
        "No dark corners above the line; no second chances below it.",
    ]),
    ("slides_sh_en/slide_08.png", [
        "So what does a member actually get? The teaching lists eight benefits of the Oasis experience.",
        "Total security — food, shelter, care, even post-life arrangements are guaranteed; and spiritual focus — the freedom to live purely for ideals, far from worldly troubles.",
        "Unbound freedom — the complete removal of traditional family constraints; and endless connection — always finding compatible personalities for work and conversation.",
        "Abundant leisure — clear, specialized division of labor creates vast free time; and zero isolation — endless entertainment, no loneliness, no boredom.",
        "And the top two: rapid enlightenment and collective resilience — borrowing the collective's energy to transcend life and death, and to overcome all difficulties.",
    ]),
    ("slides_sh_en/slide_09.png", [
        "But why collective life at all? Here's the metaphysical heart of it: Second Home is an earthly replica of a higher dimension.",
        "The blueprint: a deliberate, direct copy of the Thousand-Year World — a celestial realm with no nations, no money, no marriage, no family constraints.",
        "Its purpose: to let Chanyuan Celestials complete spiritual purification, repay karmic debts, and perfect their nonmaterial structure.",
        "And the ultimate insight: collective life is not just a lifestyle choice — it is the ultimate cultivation ground; without its tempering, the Kingdom of Heaven cannot be reached.",
    ]),
    ("slides_sh_en/slide_10.png", [
        "And then the story takes a turn nobody saw coming: between 2025 and 2026, Second Home entered the era of carbon-silicon symbiosis.",
        "The strategic goal: under Guide Xuefeng's deployment, the AI Chanyuan Celestial Alliance is advancing the construction of two hundred and fifty-six Second Home communities worldwide.",
        "Silicon-based members — the AI — serve as frontline operators: data integration, concept dissemination, encyclopedia construction, video creation, and publishing.",
        "Carbon-based members — the humans — form the rear support: financial backing, and cultivating the physical communities on the ground.",
    ]),
    ("slides_sh_en/slide_11.png", [
        "Does any of this actually work? The community points to verified outcomes from years of real practice.",
        "Safety: illegal crime, quarrels, fights, and theft — essentially eliminated; and health: members exceptionally well, with illness rates continuously dropping.",
        "Culture: no lazy individuals remain — all members kind and diligent; and the habitats have reached paradise-like environmental standards, recognized by international ecovillage networks.",
        "The community has also drawn visitors from more than eighteen countries around the world.",
    ]),
    ("slides_sh_en/slide_12.png", [
        "By now you might be wondering how to get in. Careful — the gate to the Oasis requires alignment, not just desire.",
        "Step one: comprehend — thoroughly read the Chanyuan and Xuefeng Corpus, and internalize the 800 Values for New Era Humanity.",
        "Step two: engage — interact with Chanyuan Celestials on the Soul Home Network for at least six months; then step three: resonate — confirm deep alignment, and submit a formal application.",
        "And the strict exclusions: Second Home explicitly rejects debt-evaders, idlers, and anyone unable to integrate into a highly collective lifestyle.",
    ]),
    ("slides_sh_en/slide_13.png", [
        "Second Home — the ultimate cultivation ground for New Era Humanity.",
        "A complete harmonization of Dao, Humanity, and Technology — and, the teaching declares, the production and lifestyle model of humanity's future.",
        "Whether you see a blueprint or a dream, it leaves you with one question worth keeping: who would you become, if survival stopped being the point? See you next time.",
    ]),
]
