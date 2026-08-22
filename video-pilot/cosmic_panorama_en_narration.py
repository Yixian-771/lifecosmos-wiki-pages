# -*- coding: utf-8 -*-
"""
"Cosmic Panorama" slide narration (034 English, 14 art slides, no photo pages).
Each element = (slide image, [sentences]). One sentence = one subtitle.
Written independently from the zh script; content from internal.md《宇宙全景图》, terminology from deck.
Deck page order = NotebookLM's actual ordering, 1:1 with the zh deck (verified page by page).
Order: cover (p1) -> cosmogenesis, not a big bang (p2) -> chaos vs. Hundun (p3)
-> architecture of the Earth-universe (p4) -> consciousness decides existence / 36 dimensions (p5)
-> the three tiers of space (p6) -> the supreme mathematician's grid / 20 worlds (p7)
-> the 16 levels of LIFE (p8) -> the system of Heaven (p9) -> mapping the heavens (p10)
-> the ultimate destination: Elysium (p11) -> the 36 gates of the lower realms (p12)
-> the standard of ascent and descent (p13) -> the purpose of the panorama (p14, teases LIFE Origin).
"上帝"=the Greatest Creator; 清凉界=Clear-Cool World, 法旋系=Faxuan System, 千年界/万年界=Thousand-/Ten-Thousand-Year World.
"""

NAME = "cp_en_show"
VOICE = "en-US-AndrewNeural"
FONT = r"C:\Windows\Fonts\georgia.ttf"
RATE = "+0%"
MUSIC = r"F:\百科馆\百科BGM\远空.wav"
WATERMARK = "Lifechanyuan"

META = [
    {"quote": "Where do we go after death? A complete map"},
    {"quote": "Not a Big Bang, but a Blooming"},
    {"quote": "Chaos vs. Hundun"},
    {"quote": "The architecture of the Earth-Universe"},
    {"quote": "Consciousness decides existence"},
    {"quote": "The three tiers of space"},
    {"quote": "The supreme mathematician's grid"},
    {"quote": "The 16 levels of LIFE"},
    {"quote": "The system of Heaven"},
    {"quote": "Mapping the heavens"},
    {"quote": "The ultimate destination: Elysium"},
    {"quote": "The 36 gates of the lower realms"},
    {"quote": "The standard of ascent and descent"},
    {"quote": "The universe exists for LIFE"},
]

SLIDES = [
    ("slides_cp_en/slide_01.png", [
        "Where do we actually go after death? Are Heaven and hell real? What does the universe truly look like?",
        "The Lifechanyuan teaching lays out an unprecedented, complete map — 36 dimensions of space, 20 parallel worlds, 16 levels of LIFE.",
        "Today, a bird's-eye view of the whole cosmic panorama.",
    ]),
    ("slides_cp_en/slide_02.png", [
        "First, the origin. The universe did not begin with a Big Bang, but with a blooming — Wuji gives birth to Taiji, disordered chaos becomes ordered Hundun.",
        "Before birth there was Wuji: boundless, timeless, at once all being and all nothingness.",
        "This vast universe is built of three elements — consciousness, structure, energy — and moved by eight cosmic forces.",
    ]),
    ("slides_cp_en/slide_03.png", [
        "Two states, one character apart, yet worlds apart: chaos, and Hundun.",
        "Chaos is the disordered state — turbulent, without boundary — the way things were before the universe formed.",
        "Hundun is the ordered state — a seamless whole, the unified One of opposites — the way things are after.",
    ]),
    ("slides_cp_en/slide_04.png", [
        "The universe we live in is the Earth-universe, a precise system nested layer within layer.",
        "The outermost is the Faxuan System; within it, spiral-river systems; within those, galaxies; within those, solar systems.",
        "And this blue Earth, a member of the solar system, was set up and serves specifically for humankind's experience and evolution.",
    ]),
    ("slides_cp_en/slide_05.png", [
        "One line, two cosmologies.",
        "If existence decides consciousness, we have only one Earth; if consciousness decides existence, we have 36 dimensions of space.",
        "And the passages connecting these 36 dimensions are called space tunnels.",
    ]),
    ("slides_cp_en/slide_06.png", [
        "The 36 dimensions fall into three tiers, plus one waystation.",
        "Six higher worlds — the Clear-Cool World, the Celestial World, the Elysium World and more, spaces of the highest, purest frequency; six lower worlds — the netherworld, the freezing layer, the fire-refining layer.",
        "And six neutral worlds between.",
        "Our own human world is the one waystation — the crossing-point where higher and lower LIFE come and go.",
    ]),
    ("slides_cp_en/slide_07.png", [
        "The Greatest Creator is the supreme mathematician.",
        "From the three axes of a coordinate system arise exactly 20 quadrants — that is, 20 parallel worlds, and no others.",
        "At the very center, point O, is the Clear-Cool World, where the substance of the Greatest Creator dwells.",
        "All 20 worlds connect to it; without this center, not one of them could exist.",
    ]),
    ("slides_cp_en/slide_08.png", [
        "In terms of the antimatter structure that has spirituality, LIFE divides into 16 levels — a ladder of spirituality.",
        "From the pure light at the summit — the Greatest Creator, gods, immortals and Buddhas — down to humankind, standing at the point of choice,",
        "and on down through birds, flowers, livestock, animals, trees, and insects, to the netherworld, freezing layer, and fire-refining layer.",
        "Which level you stand on depends entirely on the quality and frequency of your antimatter structure.",
    ]),
    ("slides_cp_en/slide_09.png", [
        "At the top of this ladder is the system of Heaven — the highest destination of LIFE.",
        "Heaven is no vague myth, but a precise collective name: the Thousand-Year World, the Ten-Thousand-Year World, the Elysium World, and its Celestial Islands Continent.",
        "These are real spaces, with locations, sizes, populations, and lifespans.",
    ]),
    ("slides_cp_en/slide_10.png", [
        "Consider Heaven's first two stations, side by side.",
        "The Thousand-Year World: about 960 light-years away, ten times Earth's size, home to some 200 million immortals, lifespan about 1,000 years — no sun, yet lovelier than Earth.",
        "The Ten-Thousand-Year World: about 3,480 light-years away, with 16 evenly spaced suns, lifespan about 35,000 years.",
        "Those bound for the first dream of green hills and clear waters; those bound for the second, of flying free.",
    ]),
    ("slides_cp_en/slide_11.png", [
        "The Elysium World holds ten great continents, from the Lotus Continent up to the Continent of Supreme Enlightenment.",
        "The most radiant of all is the Celestial Islands Continent — the back garden of the Greatest Creator.",
        "It has 80 billion islands, each home to a single Heavenly Celestial, each its own complete world.",
        "This is the highest destination of LIFE.",
    ]),
    ("slides_cp_en/slide_12.png", [
        "At the bottom of the map is the system of hell — reached through the 36 gates of the Continent of the Three Realms' Passage.",
        "The fire-refining layer, for those who slaughtered LIFE; the freezing layer, for those who crushed the good; the netherworld, for those who drove others to ruin.",
        "Above them, the plant world, animal world, and livestock world — up to the human waystation.",
        "The human world is the divide: the awake cultivate and rise, while the confused keep sinking, turning in the wheel.",
    ]),
    ("slides_cp_en/slide_13.png", [
        "So who decides where you go? The universe is a perfect sorting machine of consciousness.",
        "It is not drawn by lot, but decided by the quality of your LIFE right now.",
        "The most loving rise as Heavenly Celestials, the most good as Buddhas, the most joyful as celestial immortals.",
        "The muddled turn toward the animal world, the cold toward the plant world, the cruel down into the fire-refining layer — missing nothing.",
    ]),
    ("slides_cp_en/slide_14.png", [
        "This whole cosmic panorama says, at bottom, one thing: the universe exists for LIFE, and LIFE exists for the universe.",
        "Death is never LIFE's final stop — it only sheds one shell, passing from one coordinate to another.",
        "Your structure and quality, right now, are the ticket to your next station.",
        "Next: the Panorama of LIFE's Origin and Evolution — where, finally, does LIFE come from, and where is it going? See you then.",
    ]),
]
