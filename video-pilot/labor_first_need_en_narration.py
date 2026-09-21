# -*- coding: utf-8 -*-
"""
"Labor as the First Need of Life" narration (109 English deck, 14 slides, 1:1 with the source).
Second English deck (user regenerated 2026-09-20): the navy solid text bar across p02-p14 and the
coloured-pencil texture on p02-p05 are gone; all 14 pages now match the locked style, no garbled text.
Page-for-page mirror of the Chinese config labor_first_need_narration.py: same 14 pages, same
line distribution (7,5,5,7,6,5,7,4,6,5,5,5,5,5), so the two languages stay in step.
Thread: p1 hook (asking to rest feels like punishment) + the first need -> p2 everyone works
-> p3 it means physical work -> p4 the two steps of the labor threshold -> p5 no high and no low
-> p6 two thousand years of an old habit -> p7 what labor gives -> p8 good with books and with hands
-> p9 laziness -> p10 the Home is not for easy living -> p11 the most beautiful hearts
-> p12 the source of joy -> p13 art and work side by side -> p14 to love labor is to love LIFE.
Length: 5:00-10:00, target 6:30-7:30. Andrew +0% is about 15.1 characters/second.
Guardrails and separation: see 百科幻灯素材\\说明\\109_Labor_as_the_First_Need_of_Life_幻灯说明.md.
   Confucius and Fan Chi are not named (only "for more than two thousand years");
   Jesus, Shakyamuni and Laozi are not named (only "the sages").
   "Half crippled" is quoted once in the narration and never printed on a slide.
   The list of physical work and the list of benefits are both marked as only a few of the whole.
   107 covered the eight characteristics and 108 the eighty-year-old and the parasites: not repeated here.
   Soul garden is an existing entry: named once, in passing. No money talk (112 covers that).
Register: attribution once, on p4 (Lifechanyuan calls it tending your own soul garden).
"""

NAME = "ldxy_en_show"
VOICE = "en-US-AndrewNeural"
FONT = r"C:\Windows\Fonts\msyhl.ttc"
RATE = "+0%"
MUSIC = r"F:\百科馆\百科BGM\Open Fields.mp3"
WATERMARK = "Lifechanyuan"

META = [
    {"quote": "What the world looks down on, we value"},
    {"quote": "Everyone works, no exceptions"},
    {"quote": "It means physical work"},
    {"quote": "No labor threshold, no perfect soul garden"},
    {"quote": "No high and no low"},
    {"quote": "Two thousand years of an old habit"},
    {"quote": "What labor actually gives"},
    {"quote": "Good with books, and good with your hands"},
    {"quote": "Laziness is the great enemy"},
    {"quote": "The Home is not a place for easy living"},
    {"quote": "Laborers have the most beautiful hearts"},
    {"quote": "Labor and creation are the source of joy"},
    {"quote": "The farmer can also be a painter"},
    {"quote": "To love labor is to love LIFE"},
]

SLIDES = [
    ("slides_ldxy_en/slide_01.png", [
        "There is a place where, if you ask to rest, the others feel you are being punished.",
        "That is not a joke. It is ordinary life in Lifechanyuan's Second Home, also called the Life Oasis.",
        "There is a rule there that sounds badly out of step with the times: labor is the first need of every member's life.",
        "Notice the wording. Not a way to earn a living, not a chore you cannot avoid. The first need.",
        "We usually save that phrase for eating, sleeping and breathing; putting labor in that row is a heavy claim.",
        "Because the whole world outside is busy doing the opposite: finding every way to escape physical work. We study so we will not have to work the land; we get promoted so we will not have to use our hands. One mark of success is never having to do the work again.",
        "The Oasis goes the other way: what the world dislikes, we love; what the world looks down on, we value.",
    ]),
    ("slides_ldxy_en/slide_02.png", [
        "So how does that actually work? Start with the hardest rule.",
        "Everyone works. No exceptions.",
        "Whoever you are, however great your merit or your wisdom, you take part in the work.",
        "In the Home there cannot be one person who does not work, no one who stands above the rest giving orders, and no one who lives by their talk alone.",
        "There is no exemption, and no seniority that buys you out of it.",
    ]),
    ("slides_ldxy_en/slide_03.png", [
        "The second thing to make clear is what labor means here.",
        "It means physical work.",
        "Cooking, washing, growing vegetables, watering, pruning fruit trees, building, harvesting, feeding the chickens and ducks, planting flowers and trees — and those are only a few of them; the list in the source goes on.",
        "Online work and administrative work do not count as physical labor.",
        "That definition sounds unforgiving, but what it tests is not the body. It is the heart.",
    ]),
    ("slides_ldxy_en/slide_04.png", [
        "Lifechanyuan calls the work of the heart tending your own soul garden.",
        "And without passing the labor threshold, the soul garden cannot be perfect.",
        "How do you pass it? In two steps, and the order matters.",
        "First, love labor in your mind, respect those who labor, and hold that laborers are the most beautiful.",
        "Then, take part in the work willingly and joyfully.",
        "Notice the sequence: the heart agrees first, and only then do the hands follow.",
        "If the body is working while the heart refuses, the threshold has not been crossed. Digging, and thinking all the while how did someone like me end up doing this — that is still outside the gate.",
    ]),
    ("slides_ldxy_en/slide_05.png", [
        "Why insist on this threshold at all?",
        "Because there can be no divide between physical and mental work, and no class of managers over a class of the managed.",
        "Leave that divide in place, and people sort themselves into layers automatically.",
        "Without passing the labor threshold, we never learn how hard laborers work, and we start to think ourselves above others.",
        "Once that sets in, a person is standing on a platform, cut off from the ground underfoot and from the people nearby.",
        "The higher the platform, the less you can see.",
    ]),
    ("slides_ldxy_en/slide_06.png", [
        "This is not a new problem, and not one person's fault.",
        "For more than two thousand years, looking down on physical work has been deeply rooted.",
        "Always wanting an office job, always feeling that those who do simple, repetitive work are beneath them.",
        "Carry that attitude into the Home and life becomes painful, and it troubles everyone around you.",
        "What hurts is not the work. It is what the heart cannot get past.",
    ]),
    ("slides_ldxy_en/slide_07.png", [
        "So turn it around and ask: what does labor actually give a person? Here too, only a few of them.",
        "First, skilled hands and a nimble mind, and a stronger body against illness.",
        "Second, more confidence, and the ability to live on your own.",
        "Third, feet on the ground, a finer character, and a consciousness brought toward perfection.",
        "Those three sound plain, but in a real person they are solid.",
        "Someone who can keep vegetables alive, cook a meal and mend a house carries a steadiness into everything else.",
        "That steadiness cannot be argued into you. It comes out of the hands.",
    ]),
    ("slides_ldxy_en/slide_08.png", [
        "The other way round, many people finish university unable to do even simple, basic tasks.",
        "Badly lacking the ability to manage themselves and to live on their own — the source puts it harder still, and calls such a person half crippled.",
        "Good with books, and good with your hands — this deserves our serious attention.",
        "Books give a person range; hands give a person ground. Missing either one, we are thin.",
    ]),
    ("slides_ldxy_en/slide_09.png", [
        "At the far end from labor stands laziness.",
        "Diligence stands for beauty; laziness stands for ugliness.",
        "Laziness eats away at will, spirit, heart and body.",
        "And it spreads like a virus through the spirit of a whole community.",
        "One person's laziness is never only that person's business.",
        "Where life is shared, one person stepping back means everyone else must step forward.",
    ]),
    ("slides_ldxy_en/slide_10.png", [
        "So one thing has to be said plainly: the Home is not a place for easy living.",
        "It is not a place where you enjoy life without giving and without working.",
        "It is a place to repay the debts of many lives, to store up treasure in heaven, and to cultivate toward higher realms of LIFE.",
        "Enduring hardships and toil we have never known before.",
        "That is put bluntly on purpose, so no one arrives carrying the wrong expectation.",
    ]),
    ("slides_ldxy_en/slide_11.png", [
        "But if the words are that heavy, what are the people who actually do the work like?",
        "They may not write brilliant essays or quote the classics, and they may seem plain and ordinary.",
        "But their hearts are the most beautiful, and their lives themselves keep the teachings of the sages.",
        "They may not be able to explain the principle, yet their days are lived by it.",
        "That is the line most easily missed in all of this: the finest hearts are rarely found in the people best at talking.",
    ]),
    ("slides_ldxy_en/slide_12.png", [
        "And the work itself is not bitter there.",
        "True joy is found in the very process of selfless labor and creation.",
        "In the Home, work has become almost a game.",
        "Keeping someone from the work would be a punishment.",
        "That first sentence, the one we opened with, means exactly this.",
    ]),
    ("slides_ldxy_en/slide_13.png", [
        "Nor does labor keep anyone from blooming.",
        "Art and work side by side are the fullest way for a person to bloom.",
        "The one who farms can be a painter, the one who cooks can be a poet, the one who sweeps the courtyard can be a dancer.",
        "The hoe goes down, the brush comes up, and it is the same person, the same pair of hands.",
        "No one has to leave the work behind before they are allowed to speak of beauty.",
    ]),
    ("slides_ldxy_en/slide_14.png", [
        "So in the end this rule is not asking people to suffer.",
        "It is resting your hopes for living on your own labor and creation.",
        "Not on someone's charity, not on luck, not on a hollow position.",
        "Do honest work, and live an upright life.",
        "To love labor is to love LIFE.",
    ]),
]
