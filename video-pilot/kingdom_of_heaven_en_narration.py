# -*- coding: utf-8 -*-
"""
"the Kingdom of Heaven" slide narration
(041 English, 14 slides, GPT images · luminous blue-green celestial landscape · 台标 baked in, NN/14 baked).
Each element = (slide image, [sentences]). GPT flow: no watermark,
"Lifechanyuan Encyclopedia" baked bottom-left → WATERMARK="".
Source E:\下载\41英 — ★batches badly misaligned with page numbers, resolved per baked NN/14:
  14_06_53(1)=p1, 14_07_13(1)=p2, 14_06_56(2)=p3, 14_06_57(3)=p4, 14_06_58(4)=p5, 14_06_58(5)=p6,
  14_06_59(6)=p7, 14_07_00(7)=p8, 14_07_03(8)=p9, 14_07_03(9)=p10,
  14_07_13(2)=p11, 14_07_14(3)=p12, 14_07_15(4)=p13, 14_07_16(5)=p14.
★p10 originally showed a hammer-and-sickle on the red flag; Claude inpainted the emblem out
  (flag shape/folds preserved); original backed up in 41英\_原版备份\.
★p10's baked subtitle says the two mountains "must be understood — and not crossed", which
  contradicts point 03 and the entry; user chose to leave the image, so the narration states it correctly.
Archived slides_koh_en/ + 百科图片版\041_..._无水印_图片\.
GPT slides carry short text → write fuller (~56 sentences) for ≥5:00.
"上帝"=the Greatest Creator. Independent English narration (not a translation). Teases 042 the Thousand-year World.
"""

NAME = "koh_en_show"
VOICE = "en-US-AndrewNeural"
FONT = r"C:\Windows\Fonts\georgia.ttf"
RATE = "+0%"
MUSIC = r"F:\百科馆\百科BGM\Open Fields.mp3"
WATERMARK = ""  # baked into GPT image

META = [
    {"quote": "A feeling, or a place?"},
    {"quote": "What Heaven is"},
    {"quote": "Only half true"},
    {"quote": "A structural necessity"},
    {"quote": "Layer one · the Thousand-year World"},
    {"quote": "Layer two · the Ten-thousand-year World"},
    {"quote": "Layer three · the Elysium World"},
    {"quote": "What LIFE is like there"},
    {"quote": "Three conditions"},
    {"quote": "Two mountains"},
    {"quote": "The threshold, and the signs"},
    {"quote": "Eight awakenings"},
    {"quote": "Treasure, and the nearest road"},
    {"quote": "The heart can live there first"},
]

SLIDES = [
    ("slides_koh_en/slide_01.png", [
        "Many people say Heaven and Hell exist only within the human heart — feel good, and you are in Heaven; feel wretched, and you are in Hell.",
        "The Lifechanyuan teaching answers: that is only half true.",
        "Because Heaven is not merely a mood. It has coordinates, thresholds, and a route — it is real.",
        "Today we work through it all: what Heaven is, where it is, what it is like, and how one actually gets there.",
    ]),
    ("slides_koh_en/slide_02.png", [
        "Start with the definition. Heaven, also called the Kingdom of Heaven, is the collective name for three layers: the Thousand-year World, the Ten-thousand-year World, and the Elysium World.",
        "It is the living space for LIFE whose nonmaterial structure is finer than ordinary human structure.",
        "So it is not that good people are rewarded with a nice location after death; rather, when the quality of a life reaches a level, it naturally belongs to that space.",
        "Heaven's three marks: great freedom, no anxiety about food or shelter, and no disease, war, or sudden catastrophe.",
    ]),
    ("slides_koh_en/slide_03.png", [
        "So why is the popular saying only half right?",
        "The half that is right: the mind does shape its realm. What your inner state is, the world you experience becomes.",
        "The half that is wrong: Heaven exists whether or not you hold it in your mind.",
        "Distant relatives do not cease to exist because you stopped thinking of them. Inner purity does not create Heaven — it opens the way to it.",
    ]),
    ("slides_koh_en/slide_04.png", [
        "But what grounds the claim that Heaven must exist? Not belief — a law.",
        "The sum of positive and negative energy is zero. Where there is a positive, there must be a negative; where there are higher realms, there must be corresponding lower ones.",
        "As the solar system must have its planets, as a body must have limbs and organs — it is a structural necessity.",
        "So Heaven and Hell exist much as rich and poor exist: not imagination, but a consequence of how the universe is built.",
    ]),
    ("slides_koh_en/slide_05.png", [
        "Now the three layers in turn. Layer one: the Thousand-year World.",
        "It is an actual world about 960 light-years from Earth, roughly ten times Earth's size, currently home to some 200 million inhabitants.",
        "Life there has a baseline span near one thousand years — hence the name.",
        "It is purely a world of truth, goodness, beauty, love, and peace — human nature raised to its finest. Anyone who has attained complete human character may go, and there is no quota.",
    ]),
    ("slides_koh_en/slide_06.png", [
        "Layer two: the Ten-thousand-year World — a clear step higher.",
        "It lies about 3,480 light-years away, sixteen times Earth's size, with sixteen suns arranged at equal distance across its sky.",
        "Around one hundred million celestial beings live there.",
        "Their lifespans, measured against human time, run to roughly thirty-five thousand years — hence its name.",
    ]),
    ("slides_koh_en/slide_07.png", [
        "Layer three: the Elysium World — and this layer differs in kind from the two below it.",
        "Elysium belongs to the negative universe; it is the nonmaterial world. If the world we live in is the front of a sheet of paper, Elysium is its back.",
        "Elysium contains ten continents, and the one Lifechanyuan guides Chanyuan Celestials toward is the Celestial Islands Continent — the Greatest Creator's back garden.",
        "It holds eighty billion isles, each about the size of Earth. Thirty billion are already home to Super Celestials; fifty billion still wait for those who cultivate their way there.",
    ]),
    ("slides_koh_en/slide_08.png", [
        "So what is daily life actually like for LIFE in Heaven?",
        "First, freedom is the core trait. The degree of freedom reveals the level of a life — the greater the freedom, the nearer to Heaven; the smaller, the nearer to Hell.",
        "Second, it is a world of joy and play. There are no police, lawyers, judges, or officials there. If you cannot play and do not wish to play, what would you be cultivating toward?",
        "Third, there is no oppression and no exploitation, and no imposing your will on another. And selflessness is the pass that lets you in.",
    ]),
    ("slides_koh_en/slide_09.png", [
        "Having seen what it is like, we come to the real question: how does one get there? First, three conditions.",
        "One: all debts repaid, and worldly entanglements concluded.",
        "Two: sufficient merit accumulated, and character genuinely elevated.",
        "Three: the inner being purified, and the quality of LIFE refined. All three are required, and the order is hard to skip.",
    ]),
    ("slides_koh_en/slide_10.png", [
        "Beyond those three conditions, two mountains lie across the road — and both of them must be crossed.",
        "The first is the set of programs humanity built: family, ethnicity, nation, religion, political party, and the whole existing social order.",
        "The second is the inner land of Egypt: envy, comparison, resentment, arrogance, anger, possessiveness, hatred, greed, and sloth.",
        "Fail the first, and you stay bound by outer identity; fail the second, and you stay weighed down from within. Cross neither, and Heaven cannot be reached.",
    ]),
    ("slides_koh_en/slide_11.png", [
        "Is there anything measurable? Yes — and it is quite specific.",
        "By the Lifechanyuan account of LIFE, the minimum threshold is a vibration level of five hundred. Below that, entry is simply not possible.",
        "Besides the threshold there are signs, and they show up in your dreams. Dreaming often of green mountains and clear water, of gentle weather and pervading peace that leaves you glad — that points toward the Thousand-year World.",
        "Dreaming often of flying freely while remaining in steady joy points to the Ten-thousand-year World; and dreams of invisibility, of shifting shape, of scenery changing with your consciousness, point to Elysium.",
    ]),
    ("slides_koh_en/slide_12.png", [
        "From human to celestial, understanding must pass through eight gates — the eight awakenings.",
        "Awaken to LIFE — a nonmaterial structure with spirit, endlessly transforming, never extinguished. Awaken to life and death — form, not essence. Awaken to cause and effect. Awaken to space — the state of a life determines the space it inhabits.",
        "Awaken to affinity — bind with ghosts and you go below, bind with celestials and you arrive above. Awaken to mind-nature — reality is the projection of consciousness. Awaken to the cosmic matrix — power, money, fame, and desire are each a game one gets trapped in. Awaken to origin-truth — consciousness, structure, and energy are the three elements, and the Greatest Creator is their source.",
        "Pass those eight, know the Greatest Creator and walk the Way, and every one of the countless gates becomes a road. Without that, every road ends at a cliff.",
    ]),
    ("slides_koh_en/slide_13.png", [
        "Understanding settled, one still has to build up the capital. How is treasure stored in Heaven?",
        "Revering the Greatest Creator, revering LIFE and nature, and walking the Way — that stores treasure. Giving selflessly, without seeking return — that stores treasure.",
        "Reconciling old grievances, bringing calm and warmth to others, holding good thoughts and doing good deeds, easing another's anxiety and fear — all of it stores treasure in Heaven.",
        "Many roads lead to Heaven, but a lifetime is short, so choose the best one — the Second Home, an earthly copy of the Thousand-year World, and a transfer station from here to there.",
    ]),
    ("slides_koh_en/slide_14.png", [
        "And at the end, one line matters most: you do not have to wait until after death to begin living a heavenly life.",
        "A pure heart lives a heaven-like life; a cluttered heart lives an ordinary human one; a poisoned heart drifts toward the lower realms.",
        "Where consciousness is, there we are — if consciousness dwells in Heaven, then so do we.",
        "The body may still be bound to this world, yet the heart can move in first. Next time: the Thousand-year World — what does that world, 960 light-years away, actually look like? See you then.",
    ]),
]
