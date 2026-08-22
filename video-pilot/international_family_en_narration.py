# -*- coding: utf-8 -*-
"""
"The International Family" narration (011 English, 12 art slides + 4 documentary photo pages).
Each item = (slide image, [subtitle sentences]). One sentence = one subtitle.
Follows the ACTUAL English deck order (NotebookLM condensed 14->12 and reordered).
Based on the English internal.md; Andrew voice, warm, conversational.
First line = hook. Photo pages have a baked caption + 1 narration line, no spotlight.
"""

NAME = "international_family_en_show"
VOICE = "en-US-AndrewNeural"
FONT = r"C:\Windows\Fonts\georgia.ttf"
RATE = "+0%"
MUSIC = r"F:\百科馆\百科BGM\远空.wav"
WATERMARK = "Lifechanyuan"   # 英文台标（Georgia 无中文字形，必须用英文）

META = [
    {"quote": "You are an Earth citizen"},
    {"quote": "Earth, a village in the cosmos"},
    {"quote": "Every crisis is a crisis of the heart"},
    {"quote": "Embrace the One"},
    {"quote": "Beyond every boundary"},
    {"quote": "One family, every face"},                 # photo_01
    {"quote": "A bud, 2,500 years in the making"},
    {"quote": "Two paths to join"},
    {"quote": "A real branch"},                           # photo_02
    {"quote": "256 havens across the globe"},
    {"quote": "Fortune and hardship, shared"},            # photo_03
    {"quote": "Farewell to hunger and war"},
    {"quote": "Loving one another"},                      # photo_04
    {"quote": "Received into Heaven"},
    {"quote": "Purify the heart, turn danger to safety"},
    {"quote": "A beautiful era is coming"},
]

SLIDES = [
    ("slides_if_en/slide_01.png", [
        "We grow up saying: I'm from this country, you're from that one. But what if that very assumption is what needs to fall away?",
        "This is the International Family — in the Lifechanyuan teaching, what human civilization is meant to become.",
    ]),
    ("slides_if_en/slide_02.png", [
        "The teaching offers an image: the whole Earth is just a small, fragile village in a vast universe.",
        "And every villager is a child of the Greatest Creator.",
        "Only when all the villagers pull together can they dissolve conflict and safeguard this planet.",
    ]),
    ("slides_if_en/slide_03.png", [
        "Look closer at our crises — financial instability, ecological collapse, the wars of regional conflict.",
        "The teaching says these are only surface symptoms, and treating symptoms always fails.",
        "The root is a crisis of the isolated heart-mind — and only its great purification can turn danger into safety.",
    ]),
    ("slides_if_en/slide_04.png", [
        "Behind it all lies an ancient idea — embracing the One.",
        "Heaven holds the One and is clear; Earth holds the One and is still; all things hold the One and live.",
        "Multiplicity breeds disorder; only when all laws return to one source can true peace and harmony flourish.",
    ]),
    ("slides_if_en/slide_05.png", [
        "So what is the International Family? It transcends every boundary of nation, ethnicity, and religion.",
        "It operates with no national distinctions; every life is precious and cherished.",
        "The Earth belongs to its citizens, who have the right to migrate and move freely anywhere in the world.",
    ]),
    ("slides_if_en/photo_01.png", [
        "People of every color and every face, together — here, they truly are one family.",
    ]),
    ("slides_if_en/slide_06.png", [
        "And this idea isn't new.",
        "All laws to one source, all under heaven one family — the necessary path for civilization's leap.",
        "The International Family is its bud — gestating for over 2,500 years, and now, at last, breaking the soil.",
    ]),
    ("slides_if_en/slide_07.png", [
        "So how do you join? There are two paths — one for individuals, one for whole communities.",
        "An individual dedicates their time and talent, follows the 800 Concepts, helps any member in need, and shares fortune and hardship.",
        "And any group — an eco, consensus, or spiritual community — can write, reach consensus, and join as a whole.",
    ]),
    ("slides_if_en/photo_02.png", [
        "This isn't a daydream — at the Thailand branch, family from many nations sit together.",
    ]),
    ("slides_if_en/slide_08.png", [
        "The first phase establishes 256 interconnected havens across the globe.",
        "Every member is freed from the burdens of food, shelter, aging, illness, and death, and shares resources worldwide.",
        "They travel freely among the 256 homes, savoring the joys and sweetness of existence.",
    ]),
    ("slides_if_en/photo_03.png", [
        "Sharing every fortune, facing every hardship together — that is the life of the family.",
    ]),
    ("slides_if_en/slide_09.png", [
        "When these 256 homes are born, humanity bids farewell to hunger, war, misfortune, and fear.",
        "In their place — gentle rains and good seasons, fragrant flowers, singing birds, music, and celebration.",
        "Everyone joyful, happy, free, and blessed; all under heaven as one family, living as if in paradise.",
    ]),
    ("slides_if_en/photo_04.png", [
        "Loving one another, quarreling no more — wherever you go, there is a warm home.",
    ]),
    ("slides_if_en/slide_10.png", [
        "And there's a greater blessing still.",
        "When members leave the human world, they are received one by one into the Kingdom of Heaven —",
        "the Thousand-Year World, the Ten-Thousand-Year World, the Elysium World — to continue in eternal freedom and happiness.",
    ]),
    ("slides_if_en/slide_11.png", [
        "But the whole path rests on one thing — the purification of the heart-mind.",
        "First, release: sacrifice the small interests of nation, party, and self for the good of all humanity.",
        "Then embrace the One as Earth citizens, and ascend — turning danger, at last, into lasting safety.",
    ]),
    ("slides_if_en/slide_12.png", [
        "A beautiful era is coming.",
        "The peoples of the Earth joyfully form one family; wherever you go, there is a warm home and loving family beside you.",
        "People love one another, quarrel no more; all have enough, and fear no more.",
    ]),
]
