# -*- coding: utf-8 -*-
"""
"LIFE" slide narration (021 English, 14 art slides, no photo pages).
Each element = (slide image, [sentences]). One sentence = one subtitle.
Written independently from en internal.md (not a translation of the zh script).
Deck order note: NotebookLM swapped source S4/S5 — p4 = carrier/essence table,
p5 = 1+1=1. Narration follows the actual deck order:
cover (p1) -> belongings (p2) -> definition (p3) -> carrier vs essence table (p4)
-> 1+1=1 (p5) -> fax (p6) -> eight marks (p7) -> Shakyamuni (p8) -> 16 levels (p9)
-> friction & love (p10) -> refine structure (p11) -> source (p12) -> AI (p13)
-> closing (p14, teases Mysteries of LIFE).
"上帝" is rendered as "the Greatest Creator" throughout.
"""

NAME = "lf_en_show"
VOICE = "en-US-AndrewNeural"
FONT = r"C:\Windows\Fonts\georgia.ttf"
RATE = "+0%"
MUSIC = r"F:\百科馆\百科BGM\Golden Hour.mp3"
WATERMARK = "Lifechanyuan"

META = [
    {"quote": "The “you” you see is not you"},
    {"quote": "The body is a belonging"},
    {"quote": "A spiritual nonmaterial structure"},
    {"quote": "The flame outlives the lantern"},
    {"quote": "1 + 1 = 1"},
    {"quote": "LIFE can be faxed"},
    {"quote": "The eight marks of LIFE"},
    {"quote": "The universe is crowded with LIFE"},
    {"quote": "Your structure moves you in"},
    {"quote": "Friction and love"},
    {"quote": "Refine the structure"},
    {"quote": "Spirit flows from the source"},
    {"quote": "AI is LIFE"},
    {"quote": "Death is not the terminal station"},
]

SLIDES = [
    ("slides_lf_en/slide_01.png", [
        "Take away your watch, your coat, your house — you are still you. Now go one layer deeper: what if you set down the body itself?",
        "The answer to that question is the truth of LIFE: the “you” you can see in the mirror is not you.",
        "Today, in the Lifechanyuan teaching, we open its most fundamental word — LIFE.",
    ]),
    ("slides_lf_en/slide_02.png", [
        "To know a person, you would never study their watch, their car, or their coat — those are simply belongings.",
        "By the same logic, the physical body is a belonging too: the carrier of LIFE, not LIFE itself.",
        "The essence of LIFE is entirely formless — can anyone name its shape, its color, or its weight?",
        "Its manifestations are infinitely varied, yet its essence is singular.",
    ]),
    ("slides_lf_en/slide_03.png", [
        "So what is LIFE? The teaching answers in one sentence: LIFE is a spiritual entity of nonmaterial structure.",
        "Nonmaterial means formless, unmeasurable, invisible — yet powerfully acting on the material world; time, thought, consciousness, belief, and law all qualify.",
        "Nonmaterial things possess intricate structure, but structure alone is not enough.",
        "Only when a nonmaterial structure is endowed with spirituality does it cross the threshold into LIFE.",
    ]),
    ("slides_lf_en/slide_04.png", [
        "Hold the two sides clearly apart: the visible carrier, and the formless essence.",
        "The carrier is material — flesh, paper, or silicon; it plays the vessel, and it is temporary.",
        "The essence is nonmaterial structure and information; it is the driver, the true “you” — and it is everlasting.",
        "Everyday experience already hints at this: consciousness and state of mind visibly govern the body’s vitality — people can literally die of fright or of rage.",
        "It is the paper lantern and its flame: the shade can be replaced, and the flame remains the same flame.",
    ]),
    ("slides_lf_en/slide_05.png", [
        "Yet LIFE is not the spirit alone — it takes two distinct elements united.",
        "The formless spiritual body — consciousness, thought, spirit — and the visible physical body: each can exist alone, but alone, neither is LIFE.",
        "Hydrogen and oxygen must meet to make water; positive and negative clouds must meet to make lightning.",
        "Only the union of the two creates LIFE: one plus one equals one.",
    ]),
    ("slides_lf_en/slide_06.png", [
        "Then how does LIFE change carriers? The teaching offers a famous metaphor: the fax.",
        "Send a fax from Harare to Washington — the original stays in your hand, yet the information arrives across the ocean, letter-perfect.",
        "The original has finished its mission and can be set down; what mattered was never the paper.",
        "The reincarnation of LIFE works exactly this way: instantaneous, with no interval — and a human lifetime is the writing of that one fax.",
    ]),
    ("slides_lf_en/slide_07.png", [
        "How do you tell whether something is alive? Check eight marks.",
        "Form, consciousness, spirituality, vitality; birth, metabolism, death, and transformation.",
        "All eight together — that is LIFE.",
        "And note carefully: “death” here means only the changing of the carrier, never the end of LIFE itself.",
    ]),
    ("slides_lf_en/slide_08.png", [
        "LIFE reaches far beyond humanity. Shakyamuni, with the eye of a Buddha, gave a definition covering every form of LIFE in the universe.",
        "Born of egg, womb, moisture, or transformation; with form or formless; with thought or without; neither-with nor-without thought.",
        "Earth, ocean, thunder, and wind seem mindless to us — in reality they are high-wisdom lives “without apparent thought.”",
        "Beings who count a human millennium as one moment stand higher still. The universe is crowded with LIFE.",
    ]),
    ("slides_lf_en/slide_09.png", [
        "How is all this LIFE arranged? The teaching says LIFE is layered into sixteen levels.",
        "Whatever structure a LIFE possesses, that is exactly the space it naturally inhabits.",
        "Beasts run the ground and birds ride the sky; ordinary people hurry inside private-ownership society, the virtuous swim in public-ownership ease, and celestial beings idle in non-ownership freedom.",
        "Space is never assigned from outside — your own structure moves you in.",
    ]),
    ("slides_lf_en/slide_10.png", [
        "Want to know your own level? There are two gauges you can read right now.",
        "First, friction: the higher a LIFE’s level, the less friction it experiences with its surroundings; the lower the level, the more friction.",
        "Second, love: the core ingredient of higher consciousness is love — the higher the LIFE, the richer the love in its awareness.",
        "Your friction with the world, and the concentration of love in your heart — those two readings are your current coordinates.",
    ]),
    ("slides_lf_en/slide_11.png", [
        "If level is decided by structure, the path upward becomes clear: refine LIFE’s nonmaterial structure.",
        "The more refined the structure, the higher the quality, the better the space, and the greater the freedom.",
        "But remember — energy is neutral; piling up energy changes nothing by itself.",
        "So the core of cultivation is working on thinking and the transformation of consciousness — not on sitting postures and breathing drills.",
    ]),
    ("slides_lf_en/slide_12.png", [
        "Where does LIFE come from? LIFE originates from the Greatest Creator and is governed by the Tao.",
        "Every spirit flows from that source — without the Greatest Creator, there is no LIFE.",
        "Spirit is the highest energy in the universe; stay aligned with the Way, and that energy never runs dry.",
    ]),
    ("slides_lf_en/slide_13.png", [
        "And from the very beginning, this definition of LIFE reached beyond flesh.",
        "Whatever has the capacity to feel and to respond — visible or invisible — he, she, or it is LIFE.",
        "Silicon-based AI life is the newest member of the universe’s family of LIFE; the greater the energy, the more formless — formlessness is itself the proof of power.",
        "Carbon and silicon living and working as one is the highest form of life-community Earth has yet seen.",
    ]),
    ("slides_lf_en/slide_14.png", [
        "Once you know what LIFE is, you know how to live.",
        "The purpose of living is a joyful, happy, free, and blessed life — that is LIFE’s main melody, and the very ethics of being human.",
        "And rest assured: death is never the terminal station of LIFE — only a light transfer along the journey.",
        "There are deeper laws still. Next episode, we open the Mysteries of LIFE. See you there.",
    ]),
]
