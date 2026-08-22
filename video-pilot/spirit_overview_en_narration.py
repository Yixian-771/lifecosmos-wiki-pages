# -*- coding: utf-8 -*-
"""
"Spirit (Overview)" slide narration (026 English, 13 art slides, no photo pages).
Each element = (slide image, [sentences]). One sentence = one subtitle.
Written independently from en internal.md (not a translation of the zh script).
Deck is 13 pages (source draft was 14): NotebookLM merged draft S8+S9
(Six Gauges part one / part two) into a single six-token wheel page p8.
Verified page order: cover (p1) -> Jing & Shen (p2) -> structural pillar (p3)
-> cosmic hierarchy Ling/Shen/Jing (p4) -> three worlds table (p5)
-> census 98%/2%/0.01% (p6) -> three treasures flower (p7) -> Six Gauges (p8)
-> visible signifiers (p9) -> faith navigator (p10) -> self-rescue veils (p11)
-> spiritual aristocrat (p12) -> final ascent (p13, deck itself teases Heart-Mind).
Terms follow the en deck: spirit world / soul world (心灵世界 = soul world here).
"上帝" is rendered as "the Greatest Creator" throughout.
"""

NAME = "sp_en_show"
VOICE = "en-US-AndrewNeural"
FONT = r"C:\Windows\Fonts\georgia.ttf"
RATE = "+0%"
MUSIC = r"F:\百科馆\百科BGM\Golden Hour.mp3"
WATERMARK = "Lifechanyuan"

META = [
    {"quote": "Exhausting, or light?"},
    {"quote": "What works on you unseen is shen"},
    {"quote": "The pillar between two universes"},
    {"quote": "Energy flows downward in ranks"},
    {"quote": "Heavy, light, weightless"},
    {"quote": "98%, 2%, one in ten thousand"},
    {"quote": "Without spirit, a dead man walking"},
    {"quote": "The six gauges"},
    {"quote": "A lighter life shows"},
    {"quote": "Faith is the navigator"},
    {"quote": "Spirit can only be self-rescued"},
    {"quote": "The spiritual aristocrat"},
    {"quote": "From spirit to soul"},
]

SLIDES = [
    ("slides_sp_en/slide_01.png", [
        "If you had to sum up your life right now in one word, what would it be? For most people, the honest answer is: exhausting.",
        "The Lifechanyuan teaching draws the line simply: living in the material world is exhausting; living in the spirit world is light.",
        "Today: the Spirit — and how to move from the heavy world into the light one.",
    ]),
    ("slides_sp_en/slide_02.png", [
        "Take the word apart and you find two primitives of life energy: jing and shen.",
        "Jing, the vital essence, is the refined energy a LIFE-body draws from food, and the subtle substance stored within for later use.",
        "Shen, the animating power, is the invisible coordinating force that keeps every organ working in concert — the same force that unfolds a fertilized cell into a complete human being.",
        "Whatever you cannot see, name, or touch, yet works on you unmistakably — that is shen.",
    ]),
    ("slides_sp_en/slide_03.png", [
        "Together they form Spirit: the composite of jing and shen, the structural pillar of the LIFE-body.",
        "Spirit is the bridge and junction where matter and antimatter connect and interact.",
        "One end is anchored in the body that food sustains; the other reaches into the negative universe.",
    ]),
    ("slides_sp_en/slide_04.png", [
        "Seen through the universe's three elements, energy flows downward in ranks.",
        "Ling, the Spirit-Force, is the highest energy in the universe, flowing entirely from the Greatest Creator.",
        "Shen draws its energy from the level of consciousness — a structural, programmatic, faith-based energy; jing draws its energy mainly from the vital breath of heaven and earth.",
        "Jing and shen rank immediately below ling.",
    ]),
    ("slides_sp_en/slide_05.png", [
        "LIFE divides into three distinct worlds of experience.",
        "Toiling for food, housing, fame, and status — the material world, heavy and exhausting.",
        "Working gladly for joy, happiness, and freedom — the spirit world, light and relaxed; giving selflessly for bliss — the soul world, weightless and radiant.",
        "Animals live in the material world; humans live in the spirit world; celestials, Buddhas, and angels live in the soul world.",
    ]),
    ("slides_sp_en/slide_06.png", [
        "Now take the census: where does humanity actually reside?",
        "Ninety-eight percent live in the material world — draining body, mind, and soul.",
        "Fewer than two percent live in the relaxed spirit world.",
        "And perhaps one in ten thousand lives in the weightless, formless soul world — the realm Shakyamuni spoke of.",
    ]),
    ("slides_sp_en/slide_07.png", [
        "Among life's three treasures — soul wealth, spirit wealth, material wealth — none can be missing.",
        "The soul is the root; spirit is the vitality growing from that root; material wealth supports the spirit.",
        "Without spirit wealth, a person turns lonely, bored, and hollow — repressed, irritable, prone to extremes.",
        "The teaching states it without softening: without spiritual faith and a spiritual life, a person is effectively a dead man walking.",
    ]),
    ("slides_sp_en/slide_08.png", [
        "Are you living in the spirit world? Six gauges tell you; when all six align, you are there.",
        "One: unshakable certainty that someone will reach out whenever you fall — so hardship no longer frightens you.",
        "Two: trust that cause and effect never miss by a hair — so your heart stays calm in calamity. Three: seeing life as a single journey — unowned by houses, cars, money, or family roles.",
        "Four: seeing the rise and fall of civilizations as a passing drama — living free and at ease. Five: knowing the mysteries of spacetime and setting your aim on Heaven.",
        "Six: unshakable faith in the Greatest Creator.",
    ]),
    ("slides_sp_en/slide_09.png", [
        "You can also see it from the outside — a lighter life has visible signifiers.",
        "No hoarding of gold, luxuries, or brand names; treating every person as an equal; preferring solitude to going along with the crowd; fond of reading the wordless book of heaven.",
        "And here is the secret: those living in the spirit world actually enjoy finer material lives than those who live for matter.",
        "That is exactly why a celestial's quality of life surpasses a human's.",
    ]),
    ("slides_sp_en/slide_10.png", [
        "What steers the spirit? Faith.",
        "As the faith, so the state of spirit and the movements of the mind; as the mind, so the words and deeds; as the words and deeds, so the outcome and the road of a life.",
        "Faith is the navigator of the spirit; different faiths steer different lives.",
        "And the spirit reaches its absolute peak when the heart is in joy.",
    ]),
    ("slides_sp_en/slide_11.png", [
        "When the spirit runs low, no one can lend you theirs: spirit cannot be borrowed or stolen — it can only be rescued by your own effort.",
        "The old verses tend it: speak less to nourish the inner breath; renounce anger to nourish the lungs; eat with restraint to nourish the stomach; think less to nourish the liver; want less to nourish the heart.",
        "Restrain thinking, and shen is complete; restrain speech, and qi is complete; restrain desire, and jing is complete.",
        "Heart unstirred, body unstirred — three circles complete, and one naturally becomes an immortal.",
    ]),
    ("slides_sp_en/slide_12.png", [
        "Cultivated to its height, the spirit produces a human archetype: the spiritual aristocrat.",
        "Noble in spirit, rich in soul, unmoved by power, capital, custom, or fashion — independent, upright, gracefully free.",
        "The opposite of an aristocrat is not a commoner but a beggar — whoever tramples their own dignity and freedom to beg the world for favor.",
        "Millennia of history testify: aristocrats of wealth and power never brought humanity happiness; only spiritual aristocrats are the hope of humankind.",
    ]),
    ("slides_sp_en/slide_13.png", [
        "One final clarity: the spirit world is the human goal, but the soul world is the final direction of LIFE's ascent.",
        "Freed first from the bondage of matter, and eventually freed from the bondage of spirit, one lives in the soul world — as a Heavenly Celestial or a Buddha.",
        "And when the material world turns grim, simply switch the scenery at will: that inner world is yours to roam without limit.",
        "Next episode: the Heart-Mind — the mirror that reflects all things; what is the mirror itself? See you there.",
    ]),
]
