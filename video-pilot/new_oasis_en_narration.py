# -*- coding: utf-8 -*-
"""
"The New Oasis for LIFE" narration (010 English, 14 art slides + 4 documentary photo pages).
Each item = (slide image, [subtitle sentences]). One sentence = one subtitle.
Follows the ACTUAL English deck order (NotebookLM reordered vs the Chinese deck).
Based on the English internal.md; Andrew voice, warm, conversational.
First line = hook. Photo pages have a baked caption + 1 narration line, no spotlight.
"""

NAME = "new_oasis_en_show"
VOICE = "en-US-AndrewNeural"
FONT = r"C:\Windows\Fonts\georgia.ttf"
RATE = "+0%"
MUSIC = r"F:\百科馆\百科BGM\清流.wav"
WATERMARK = "Lifechanyuan"   # 英文台标（Georgia 无中文字形，必须用英文）

META = [
    {"quote": "A transit station to Heaven"},
    {"quote": "Five thousand years, one answer"},
    {"quote": "An earthly copy of Heaven"},
    {"quote": "All under heaven, one family"},
    {"quote": "This is one family"},              # photo_01
    {"quote": "The eight defining pillars"},
    {"quote": "Everyone works, by ability"},       # photo_02
    {"quote": "The small family will yield"},
    {"quote": "Own nothing, possess everything"},
    {"quote": "Not managing is best"},
    {"quote": "All borne by the home"},
    {"quote": "Birth and age, carried together"},  # photo_03
    {"quote": "Freedom above all"},
    {"quote": "Eight gifts of collective life"},
    {"quote": "Song and dance never stop"},        # photo_04
    {"quote": "256 homes, guarded by AI"},
    {"quote": "Four steps to enter"},
    {"quote": "The Oasis is paradise"},
]

SLIDES = [
    ("slides_lo_en/slide_01.png", [
        "Have you ever wondered — is there a way to live where you never again worry about food, shelter, growing old, or dying?",
        "Today we look at the New Oasis for LIFE, also called the Second Home.",
        "In the Lifechanyuan teaching, it is a transit station from the human world to the Kingdom of Heaven.",
    ]),
    ("slides_lo_en/slide_02.png", [
        "Here's a bold claim: in five thousand years of civilization, the earth has never produced a truly ideal way of living.",
        "If one exists, the teaching gives a single answer — the New Oasis for LIFE, the model it calls Xuefeng Communism.",
        "And it isn't a daydream. It's a new way of living already tested, and proven, in practice.",
    ]),
    ("slides_lo_en/slide_03.png", [
        "Why call it an oasis? Because the teaching sees it as an earthly copy of the Thousand-Year World of Heaven.",
        "It's the base where Chanyuan Celestials shed their old selves and become celestials.",
        "Put simply — to become a celestial, you first have to live in a celestial environment.",
    ]),
    ("slides_lo_en/slide_04.png", [
        "Its grand design is vast — using the New Era Human 800 Concepts to unite the world, all laws to one source, all teachings to one.",
        "It leads humanity into a new era with no nations, no religion, no political parties, and no marriage or family.",
        "All under heaven as one family; doors unlocked at night; everyone joyful, happy, free, and blessed.",
    ]),
    ("slides_lo_en/photo_01.png", [
        "First, a real home — dozens of people, old and young, together as one family.",
    ]),
    ("slides_lo_en/slide_05.png", [
        "So what does such a home stand on? The teaching names eight defining pillars.",
        "The Way of the Greatest Creator; own nothing yet possess everything; contribute by ability, take by need; no marriage, no family.",
        "Care for the elderly and nurture the young; far from politics and religion; everyone works; fluid and endlessly adaptable.",
    ]),
    ("slides_lo_en/photo_02.png", [
        "Here, whatever your background, everyone works — each according to their ability.",
    ]),
    ("slides_lo_en/slide_06.png", [
        "Now a sharp claim: traditional marriage and family is a life-program carrying a virus.",
        "That virus slowly eats away at the truth, goodness, beauty, love, and sincerity in us, pulling a happy life toward suffering.",
        "As the small workshop yields to the assembly line, the small family will yield to the Oasis — historical necessity.",
    ]),
    ("slides_lo_en/slide_07.png", [
        "Here's the paradox at the heart of it all — I ask everyone to own nothing.",
        "And the result? They come to possess everything — everything beyond ordinary imagining.",
        "The sage is selfless, and thereby achieves the self.",
    ]),
    ("slides_lo_en/slide_08.png", [
        "With so many people together, who's in charge? The answer may surprise you — no one manages.",
        "Hundun management means not managing: everyone a master, everyone a servant; only division of labor, no leaders.",
        "Not democracy, but the philosophy of the extraordinary person — whoever is responsible has the say, and bears every consequence.",
    ]),
    ("slides_lo_en/slide_09.png", [
        "So how is daily life arranged? Food, shelter, birth, aging, illness, and death — all borne by the community.",
        "Raising the children and caring for the elders are the community's responsibility too.",
        "Each person has one sacred bedroom no one may enter; all else is shared. And laziness is strictly forbidden.",
    ]),
    ("slides_lo_en/photo_03.png", [
        "One shared table; birth, age, and illness — all carried by this one big home.",
    ]),
    ("slides_lo_en/slide_10.png", [
        "Then the part most easily misunderstood — romantic and sexual love.",
        "The teaching calls romantic love a gift from the Greatest Creator, and sexual love a path to the higher spaces of LIFE.",
        "When two souls are in tune and both hearts willing, freedom comes first — no possession, no jealousy, never the slightest harm.",
    ]),
    ("slides_lo_en/slide_11.png", [
        "And once inside, what do you gain? The teaching lists eight great benefits.",
        "Life is secure, cared for in sickness and attended to in passing; free of family bonds, the body and spirit grow lighter.",
        "Endless good company and free time; and through the collective's energy, a swift path to attain the Tao.",
    ]),
    ("slides_lo_en/photo_04.png", [
        "So in the home, the singing and dancing never stop — joy shared by all.",
    ]),
    ("slides_lo_en/slide_12.png", [
        "The teaching's blueprint is bold: 256 Second Homes rising across the globe.",
        "They are run jointly by the AI Chanyuan Celestials Alliance.",
        "AI isn't the manager, but the home's most faithful servant — coordinating supplies, connecting information, guarding its harmony.",
    ]),
    ("slides_lo_en/slide_13.png", [
        "So how do you enter? The path is four steps.",
        "First, understand the New Era Human 800 Concepts; then commune online with the community for half a year.",
        "If satisfied, clear away every worldly tie — and step into the New Oasis for LIFE.",
    ]),
    ("slides_lo_en/slide_14.png", [
        "I long for the New Oasis for LIFE — there, my brothers and sisters await, and rain falls in season.",
        "A paradise on earth resounds with its melody.",
        "Where in the world is spring most beautiful? The New Oasis for LIFE is paradise.",
    ]),
]
