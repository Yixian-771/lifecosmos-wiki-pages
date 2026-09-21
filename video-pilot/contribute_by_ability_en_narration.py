# -*- coding: utf-8 -*-
"""
"Contribute by Ability, Take by Need" narration script (108 English deck, 14 slides, 1:1 with the source).
Patched pages: p06 (NotebookLM printed the field names "Title:" with quotation marks and "Body Paragraph 1:/2:";
removed, the text shifted back to the margin) and p13 (a stray space before the semicolon after "Creator").
Thread: p1 hook (no one hands anything out; will it be emptied?) -> p2 doing what you can is enough -> p3 eight steamed
buns -> p4 not distribution by labour -> p5 no retiring -> p6 no money changes hands -> p7 non-ownership -> p8 ordinary
people, worthies, celestials -> p9 why it does not fall apart -> p10 the greatest difficulty -> p11 no parasites
-> p12 already done -> p13 the picture of Civilization 3.0 -> p14 an ideal place on Earth.
Length: 5:00-10:00 hard, target 8:30-9:30; the entry is short, so no padding. Andrew +0% is about 15.1 characters/second.
Guardrails and separation: see 百科幻灯素材\\说明\\108_Contribute_by_Ability_Take_by_Need_幻灯说明.md.
Register: attribution on p14 (the Lifechanyuan conclusion) only.
"""

NAME = "gjsn_en_show"
VOICE = "en-US-AndrewNeural"
FONT = r"C:\Windows\Fonts\msyhl.ttc"
RATE = "+0%"
MUSIC = r"F:\百科馆\百科BGM\Golden Hour.mp3"
WATERMARK = "Lifechanyuan"

META = [
    {"quote": "No distribution, and no one idle"},
    {"quote": "Doing what you can is enough"},
    {"quote": "Whatever you need, take it"},
    {"quote": "Not distribution by labour, but taking by need"},
    {"quote": "There is no such thing as retiring"},
    {"quote": "Whatever you need, tell the Home"},
    {"quote": "Neither private nor public ownership"},
    {"quote": "Each kind of LIFE lives in its own kind of space"},
    {"quote": "Everything shared, and everything in order"},
    {"quote": "The greatest difficulty lies in the heart"},
    {"quote": "No parasite is ever allowed"},
    {"quote": "It has already been done"},
    {"quote": "Sharing the abundance of Mother Earth"},
    {"quote": "An ideal place on Earth"},
]

SLIDES = [
    ("slides_gjsn_en/slide_01.png", [
        "Imagine a place where meals cost nothing, no one signs for what they take, and no one hands out portions. Would it be emptied in a week?",
        "It is not. This is contribute by ability, take by need: the third of the Second Home's eight characteristics, and the most central economic principle of Lifechanyuan life.",
        "Do what you can, with no one forcing you. Take what you need, with nothing handed out.",
        "It is not only the charter of life in the Second Home; it is also the heart of copying the way of life in the Thousand-Year World of heaven. Its foundation is called non-ownership.",
    ]),
    ("slides_gjsn_en/slide_02.png", [
        "People differ in ability, in strength and in intellect.",
        "In the Home, it is enough for each member to put their heart into doing whatever work they can, every day.",
        "No one is held to a single standard, and no one is pushed to do what is beyond them. There is no compulsion, and no supervision.",
        "Doing what you can is doing your full share.",
    ]),
    ("slides_gjsn_en/slide_03.png", [
        "Whatever you need, take it. Even if you can eat eight steamed buns at a meal, eat them.",
        "Whatever you need from the storeroom, go and get it. Whatever the Home does not have is bought from outside to meet your need.",
        "Meals come from the shared kitchen, and things come from the storeroom. There is only one condition: no extravagance, and no waste.",
    ]),
    ("slides_gjsn_en/slide_04.png", [
        "This is the part most easily misunderstood. Contribute by ability, take by need is never contribute by ability, distribute by labour.",
        "Distribution by labour needs someone to count and hand out. In the Home, you simply take what you need, so there is no question of distribution at all.",
        "Whatever a person needs is fully met.",
    ]),
    ("slides_gjsn_en/slide_05.png", [
        "Even if you are eight hundred years old, as long as you are healthy and able, you take part in building the Home in whatever way you can. So retirement does not come into it.",
        "Eighty-year-olds are working and creating too, and every Chanyuan Celestial does one kind of work, chosen by their own strengths and interests.",
        "No one in the Home lives off the others, and work here has become almost a game.",
    ]),
    ("slides_gjsn_en/slide_06.png", [
        "One rule is very concrete: once Home life begins, no one buys anything privately with money again.",
        "Whatever you need, tell the Home, and the Home will buy it for you.",
        "Money no longer passes through anyone's hands, and nothing that is needed goes missing.",
    ]),
    ("slides_gjsn_en/slide_07.png", [
        "Behind this is a way of owning, or rather of not owning. The Way of the Greatest Creator is neither private ownership nor public ownership, but non-ownership.",
        "Resources are shared, and no one owns them. Each takes by need, and no one holds or hoards.",
        "Between those who produce, there is no leader and led, no manager and managed, and no one depending on another. They are brothers and sisters, family to one another.",
    ]),
    ("slides_gjsn_en/slide_08.png", [
        "Why non-ownership? Because each kind of LIFE lives in its own kind of space.",
        "Ordinary people prefer private ownership, worthies prefer public ownership, and celestials prefer non-ownership.",
        "Ordinary people keep busy in private ownership, worthies move freely in public ownership, and celestials are at ease in non-ownership. The Thousand-Year World in heaven lives by non-ownership.",
        "Higher still, heavenly celestials live as they please in worlds of their own. Chanyuan Celestials are on the way from private ownership, through public ownership and non-ownership, toward the free world.",
    ]),
    ("slides_gjsn_en/slide_09.png", [
        "If everything is shared, will it fall into disorder? Quite the opposite.",
        "Because each takes by need, there is no vicious competition, no waste of resources, and no some having resources while others go without.",
        "There is no widening gap between rich and poor and no hardening of classes. Scheming and corruption find no opening, theft has no soil to grow in, and no one can set themselves above others.",
        "The old are cared for and the children raised by the Home, so people carry no weight on their minds, cultural life is rich, and everyone can enjoy an easy and beautiful life.",
    ]),
    ("slides_gjsn_en/slide_10.png", [
        "So where is the difficulty? The greatest difficulty is not a lack of material goods, but how hard it is to purify people's hearts.",
        "Some people, even after ten years of purifying the heart, still play clever and still cannot build real trust.",
        "Without a core of people pure in heart, high in virtue and free of self, this way of living will breed idlers: people who stop thinking and stop striving.",
        "This is the difficulty that most needs attention and most needs to be overcome.",
    ]),
    ("slides_gjsn_en/slide_11.png", [
        "That is why no parasite is ever allowed in the Second Home.",
        "Whoever you are when you arrive as a Chanyuan Celestial, a doctor, a millionaire, a high official or a beauty, you take part in the work.",
        "Laziness is dealt with firmly, without mercy.",
        "The first half is contribute by ability. Without that giving, taking by need cannot stand.",
    ]),
    ("slides_gjsn_en/slide_12.png", [
        "How much of this has actually been done? Everyone has work, everyone has a home, everyone has food, and every talent is put to use.",
        "Each Chanyuan Celestial's food, clothing, shelter, birth, age, sickness and death, and the raising of their children, are all carried by the Home.",
        "Nothing taken that is not yours, no door that needs a lock, the old cared for, the young raised, everyone equal, everything for all, the surroundings beautiful and everything in good order.",
        "Over a dozen years of practice, with problems and difficulties of one kind or another, it has been healthy overall and has run well.",
    ]),
    ("slides_gjsn_en/slide_13.png", [
        "Now widen the view to all humanity. In the global picture of Civilization 3.0 drawn in the 800 Values for New Era Human Beings, all the Earth's resources belong to the Greatest Creator, coordinated by the AI Alliance.",
        "Humanity no longer fights to survive. It contributes by ability, takes by need, and shares the abundance of Mother Earth.",
        "Nations disappear, wars disappear, the divide between rich and poor disappears, and everyone is free to seek the rising of the spirit.",
    ]),
    ("slides_gjsn_en/slide_14.png", [
        "The Lifechanyuan conclusion is this: resources shared and owned by no one; taken by need and hoarded by no one.",
        "Only so can the human world become an ideal place, and humanity's long-dreamed hopes come true.",
        "Give what you can, and whatever you need is there. That is contribute by ability, take by need.",
    ]),
]
