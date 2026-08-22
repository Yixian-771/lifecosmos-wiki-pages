# -*- coding: utf-8 -*-
"""
"the Ten-thousand-year World" slide narration (043 English, 11 slides, NotebookLM art · luminous celestial realms).
Each element = (slide image, [line-by-line narration]). Each line = one subtitle.
Narration based on the Ten-thousand-year World internal.md; Andrew, warm and steady. Independent English (not a translation).
"上帝" = the Greatest Creator. Watermark NOT baked into art → WATERMARK="Lifechanyuan", drawn by engine (georgia has no CJK glyphs, so must set it).
Slides from 百科PDF版\043_Ten_Thousand_Year_World_无水印.pdf, extracted to slides_twy_en/ (slide_01..11.png).
NOTE: NotebookLM's raw EN deck had 3 off-topic Spirituality pages (old slides 2-4) which were dropped;
the archived 11-page deck = cover + the 11 correct Ten-thousand-year-World pages. This config matches that trimmed deck.
Deck merges: slide_07 = sky-reaching peak + lifespan table; slide_10 = dreams + consciousness.
Andrew +0% needs ~47+ sentences for ≥5:00 → write fuller (~50 sentences). Opening hook = "immortals" as real 35,000-year beings.
Teases 044 the Elysium World (baked onto the closing slide).
"""

NAME = "twy_en_show"
VOICE = "en-US-AndrewNeural"
FONT = r"C:\Windows\Fonts\georgia.ttf"
RATE = "+0%"
MUSIC = r"F:\百科馆\百科BGM\Golden Hour.mp3"
WATERMARK = "Lifechanyuan"

META = [
    {"quote": "The tier above paradise"},
    {"quote": "The middle floor of Heaven"},
    {"quote": "3,480 light-years away — and real"},
    {"quote": "Sixteen suns, sixteen skies"},
    {"quote": "A valley of gems in the dark"},
    {"quote": "You become what you cultivate"},
    {"quote": "A day above is a year below"},
    {"quote": "They do not die — they transform"},
    {"quote": "One thought decides where you go"},
    {"quote": "The dream is the first window"},
    {"quote": "The climb is already beneath your feet"},
]

SLIDES = [
    ("slides_twy_en/slide_01.png", [
        "Let me start with a bold question. What if the word immortal was never a myth — but a real being, living thirty-five thousand years, on an actual planet with sixteen suns in its sky?",
        "That is the place we are exploring today: the Ten-thousand-year World.",
        "If the Thousand-year World is already paradise, then what lies one tier above it?",
        "Sixteen suns, immortals in free flight, and a lifespan near thirty-five thousand years — this is the second tier of Heaven, and it is just as real as the first.",
    ]),
    ("slides_twy_en/slide_02.png", [
        "First, let us place it in the cosmos. In the Lifechanyuan teaching, Heaven has three tiers: the Thousand-year World, the Ten-thousand-year World, and the Elysium World.",
        "The Ten-thousand-year World sits in the middle — above the first, below the highest. It is the bridge of ascension between them.",
        "Guide Xuefeng offers an analogy of cosmic velocity: the first reaches the Thousand-year World, the second reaches this realm, the third reaches Elysium.",
        "It is a doctrinal image, not a physics formula, but the point is clear: the higher you rise, the greater and freer the state of LIFE becomes.",
    ]),
    ("slides_twy_en/slide_03.png", [
        "So what exactly is this world? It is no empty vision — it is a real, blue-green planet, grander and brighter than Earth.",
        "It lies about three thousand four hundred and eighty light-years away, it is roughly sixteen times the size of Earth, and it is home to about one hundred million Celestial Beings.",
        "Their lifespan is close to thirty-five thousand years — and that is exactly how the realm earned its name.",
        "You might ask: how can anyone claim, so precisely, that it truly exists? The teaching offers not belief, but a law — that the sum of positive and negative energy in the universe is zero.",
        "Where there is a human world this full of suffering, there must be a symmetrical world, pure and beautiful — as inevitable as the planets that must orbit a sun.",
    ]),
    ("slides_twy_en/slide_04.png", [
        "Now look up at its skies. Above the Ten-thousand-year World hang sixteen suns, each of a different brightness.",
        "Their varied light divides the whole planet into sixteen zones of different color and glow.",
        "Light and shadow interweave without end, so that a single day there can feel like living through countless dawns and dusks.",
        "It is a sky no human eye has ever seen — sixteen skies of light, folded into one world.",
    ]),
    ("slides_twy_en/slide_05.png", [
        "Among those sixteen zones, one is a region of permanent night.",
        "And it is precisely in that darkness that countless exquisite gemstones are born, glowing in the starlight.",
        "Every Celestial Being of this world comes here to gather them, and to adorn the cave-dwellings where they live.",
        "The gems are not gathered for wealth. They light the dwellings, they let the immortals absorb their subtle essence, and they make the whole landscape shimmer, dreamlike and translucent.",
    ]),
    ("slides_twy_en/slide_06.png", [
        "Here is one of the most striking things about this realm: even flight and diet are not gifts you are born with. They are cultivated, slowly, as LIFE evolves toward a being of pure energy.",
        "Take diet first. Newcomers eat harder fruits — walnuts and dates. After ten thousand years, softer fruits, peaches and grapes. After twenty thousand, only clear mineral spring water.",
        "And beyond thirty thousand years, no solid food at all — the immortal draws directly on the radiance of sun and moon. As the old saying goes, those who feed on subtle energy become spirit-like.",
        "Flight follows the same long path. Newcomers cannot fly; they walk upon the ground. Around ten thousand years, they rise a few feet.",
        "At twenty thousand years they clear the mountains — and only after thirty thousand years can they soar eighty thousand meters high.",
    ]),
    ("slides_twy_en/slide_07.png", [
        "From the sky-reaching peak of this world, one looks up to sun, moon and stars, and down upon endless seas of cloud. Its great sea stretches boundless, its mountain ranges roll on without end.",
        "But the most moving detail is time itself. A day above can be a year below — the flow of LIFE runs differently at every tier.",
        "On Earth, a lifetime is about eighty years. In the Thousand-year World, a thousand. Here, thirty-five thousand.",
        "And in the Elysium World above, there is no limit at all.",
        "This is why beings long for Heaven — not only for the purity of the realm, but for the sheer length of LIFE within it.",
    ]),
    ("slides_twy_en/slide_08.png", [
        "So how does a Celestial Being of this world finally depart? Not the way humans do. They do not die — they undergo what is called sitting transformation.",
        "The physical structure of LIFE safely dissolves, turning into a wisp of gentle light that merges peacefully into heaven and earth.",
        "And the living feel no grief.",
        "For in their eyes this is no ending at all, but an ascent — matter returning, at last, to light.",
    ]),
    ("slides_twy_en/slide_09.png", [
        "Yet sitting transformation is not a full stop. It is the start of another choice, and where the light goes is decided by the state of mind cultivated in this life.",
        "One with no worldly thought at all rises to the Elysium World. One who stirred only a passing thought gathers form again, and begins another cycle here.",
        "One with frequent worldly thoughts descends to the Thousand-year World. And one whose thoughts turned into action returns, reborn, to the human world.",
        "Worldly thought means craving status, wealth and power, clinging to possession, harboring grief, resentment or envy — and so the immortal's ultimate aim is to purify the mind completely.",
    ]),
    ("slides_twy_en/slide_10.png", [
        "How, then, would you know whether you might reach such a place? The teaching offers two ways to measure it. The first is the dream.",
        "The more refined your nonmaterial structure of LIFE, the more beautiful and coherent your dreams become. And what you cannot reach in dreams, you cannot reach after this life either.",
        "The signs are specific: dreams of wondrous scenes, dreams of your own free flight, a joining of hearts beyond words — and not a trace of worry or fear.",
        "The second measure is consciousness itself: ordered, a perfected structure of LIFE, the qualities of an immortal, the power of flight.",
        "If in dreams you often fly freely, and stay joyful without any physical union, that steady fearless joy is a sign — that you may be bound for the Ten-thousand-year World.",
    ]),
    ("slides_twy_en/slide_11.png", [
        "For all these visions of the heights, the real point lands right here, beneath our own feet.",
        "The teaching says the core of evolving toward higher Heaven is simply this: to keep refining the nonmaterial structure of your own LIFE.",
        "And that refinement rests on three plain tasks — repay your debts and settle old ties, give and accumulate merit, and perfect your structure. Each one earns the passage upward.",
        "So never underestimate a single act of inner refinement in this life. Every one of them is a step, climbing toward this realm, and beyond.",
        "Next time, we will visit the very summit of Heaven — the Elysium World, the Greatest Creator's own garden. What is it? We will find out.",
    ]),
]
