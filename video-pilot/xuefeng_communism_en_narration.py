# -*- coding: utf-8 -*-
"""
"Xuefeng Communism" narration script (107 English deck, 14 slides, 1:1 with the source). No patches needed.
Thread: p1 hook (have nothing, own everything) -> p2 sharing -> p3 not a monster -> p4 one family under heaven
-> p5 the Great Harmony -> p6-p7 the eight characteristics -> p8 ever-changing -> p9 practice, not utopia
-> p10 problems that disappear -> p11 it will come -> p12 the great purification -> p13 the by-product of the harvest
-> p14 the necessary road.
Length: 5:00-10:00 hard, target 8:30-9:30. Andrew +0% is about 15.1 characters/second.
Guardrails and separation: see 百科幻灯素材\\说明\\107_Xuefeng_Communism_幻灯说明.md. Marx named once; the nine homes broken
up in one line, no agent named; four of the eight arguments, flagged as a few; obstacles only at the level of the heart;
marriage and family in one line plus one line of reason; no comment on any real country, party or system.
Register: attribution on p2 (in the Lifechanyuan teaching), p13 (Xuefeng says), p14 (the 800 Values, no. 621).
"""

NAME = "xfgc_en_show"
VOICE = "en-US-AndrewNeural"
FONT = r"C:\Windows\Fonts\msyhl.ttc"
RATE = "+0%"
MUSIC = r"F:\百科馆\百科BGM\Quiet Study.mp3"
WATERMARK = "Lifechanyuan"

META = [
    {"quote": "Have nothing, own everything"},
    {"quote": "Communism is really sharing"},
    {"quote": "Not a monster, but spring rain"},
    {"quote": "One family under heaven"},
    {"quote": "In truth, the Great Harmony"},
    {"quote": "No leaders; everyone is master of the Home"},
    {"quote": "Whatever your background, everyone works"},
    {"quote": "Running water never goes stale"},
    {"quote": "Not a utopia, a practice"},
    {"quote": "Problems that simply disappear"},
    {"quote": "Communism will certainly come"},
    {"quote": "A great purification of the heart"},
    {"quote": "Harvesting the ripe crop"},
    {"quote": "The necessary road for the new era"},
]

SLIDES = [
    ("slides_xfgc_en/slide_01.png", [
        "What if there were a way of living where you have nothing, and yet own everything? Would you try it?",
        "This is Xuefeng Communism: a completely new way for humanity to produce and to live, proposed and personally practised by the guide Xuefeng.",
        "Its basic principle is contribute by ability, take by need. It has been lived in the Second Home since 2009.",
        "The word communism makes many people frown. Hold on for a moment. This is not what you think it is.",
    ]),
    ("slides_xfgc_en/slide_02.png", [
        "In the Lifechanyuan teaching, communism is really sharing.",
        "The more widely a thing is shared, the greater its value.",
        "The most effective way to bring every resource to its greatest value is to share it, and that is the substance of communism.",
        "So at its heart is not taking away, but sharing.",
    ]),
    ("slides_xfgc_en/slide_03.png", [
        "Communism was once a gracious and noble lady, and she was turned into a monster.",
        "That was not the fault of ordinary people. Ever since Marx, the theory of communism has been incomplete, and the way it was carried out was wrong: pushing it through by seizing the property of capitalists and landlords went against natural law.",
        "So was the ideal itself wrong? No. To set his own theory and practice apart from the communism that was demonized, the guide Xuefeng called it Xuefeng Communism.",
        "It seizes no private property and runs no mass campaigns. It follows natural principles, like fine rain soaking in without a sound, or spring sun over the whole land, and people join of their own free will.",
    ]),
    ("slides_xfgc_en/slide_04.png", [
        "Its goal: no talent left behind, one family under heaven; nothing taken that is not yours, no door that needs a lock; the old cared for, the young raised.",
        "The weather kind, the world at peace, people settled in their work, and everyone happy, joyful, free and content.",
        "If the world is one family, there are no more nations, religions or political parties, no money or power, and no marriage or family. That is the way of life in the Second Home, and the Lifechanyuan picture of humanity's future.",
        "There are no constitutions and no laws, only shared values. Everyone has nothing, and owns everything.",
    ]),
    ("slides_xfgc_en/slide_05.png", [
        "In the end, Xuefeng Communism is the Great Harmony that sages through the ages have sought.",
        "First, harmony of the four views: values, LIFE, life, and the universe.",
        "Then harmony of language and of ways of communicating, and finally harmony of the ways we produce and live.",
        "Its aim is for people to feel, more and more, that the traditional life, even the life of the rich, is less happy, less joyful and less free than this one, until they choose it gladly.",
    ]),
    ("slides_xfgc_en/slide_06.png", [
        "This is not just talk. The Second Home has summed up eight characteristics.",
        "One: the Way of the Greatest Creator, Hundun Management. There are no leaders and no offices; everyone is master of the Home. Two: have nothing, own everything. No private belongings and no money, yet everything the Home has is there to enjoy, without extravagance or waste.",
        "Three: contribute by ability, take by need. Do what you can, and whatever you need is met. There is no question of distribution.",
        "Four: no marriage, no family. The reason is plain: marriage and family are a breeding ground of selfishness, a well of worry and pain, and a root of the endless plundering and waste of nature's resources.",
    ]),
    ("slides_xfgc_en/slide_07.png", [
        "Five: the old cared for, the young raised. Food, clothing, shelter, birth, age, sickness and death are all carried by the Home, so children no longer worry about parents, and parents no longer worry about children.",
        "Six: apart from politics, apart from religion. No political activity, no religious ritual, no idol worship; love for mountains, rivers and plants, and care for every creature.",
        "Seven: whatever your background, everyone works. Doctor or unschooled, rich or poor, high official or ordinary person, once you are in, you are a worker, and only the present counts.",
        "Eight: flexible, rounded and ever-changing. This one is the most unusual, and it deserves a closer look.",
    ]),
    ("slides_xfgc_en/slide_08.png", [
        "In the Home, where people stay keeps changing, work changes as needed, people keep moving, and games and pastimes keep changing too.",
        "Two people staying together in one place for good is not possible. Everyone is always somewhere new.",
        "This keeps entropy from reaching its maximum and the Home from becoming stagnant water. It wakes up interest and thinking, and it keeps cliques and little fiefdoms from forming.",
        "Running water never goes stale. The Home stays alive by changing.",
    ]),
    ("slides_xfgc_en/slide_09.png", [
        "If all this were only ideas and discussion, it would be utopian communism.",
        "Xuefeng Communism rests on practice: the Second Home, founded in April 2009 and running for more than a decade, with a great deal of writing, photographs and video about it online.",
        "Over those years, nine homes as lovely as poems were broken up by force, and still the journey never stopped.",
        "One key lesson: anyone who wants to come in must first go through purification of the heart. If people whose hearts are not yet whole come in, laziness and love of ease bring trouble; so for now it can only be done locally, on a small scale.",
    ]),
    ("slides_xfgc_en/slide_10.png", [
        "A life like this makes quite a few problems disappear on their own. Here are only a few.",
        "Old age: the elderly live among the young and the children, at ease in their later years. Children: raising them is everyone's work, so spoiling them or stealing them has no way to happen.",
        "Theft: there is nowhere to keep what you took and no way to use it, so there is no reason to steal. Poisoned food: whoever grows or makes the food eats it too.",
        "Corruption: everyone here is a worker, and no officials are needed. With no officials, corruption disappears. And the crisis of trust: when people have no clashing interests, it disappears too.",
    ]),
    ("slides_xfgc_en/slide_11.png", [
        "Why say communism will certainly come? There are eight lines of reasoning; here are only a few.",
        "First, shared information: the internet shares information, and AI has a global view and universal values, which leads toward one world. Second, free movement: visa-free travel keeps spreading, and in the end there will be no border controls. When people can move freely across the Earth, Xuefeng Communism has arrived.",
        "Third, machines at work: as robots take over more and more, and most people no longer need to work, society will have to provide for everyone together.",
        "Fourth, civilization rising: from barbarism to civilization is the law of human history, and nothing can hold it back.",
    ]),
    ("slides_xfgc_en/slide_12.png", [
        "If this life is so good, why is it so hard to spread? The root is in the heart: wanting special treatment, wanting to stand above others, wanting to live better than others.",
        "Nothing else stands in the way of Xuefeng Communism. The greatest difficulty is that all humanity needs a great purification of the heart.",
        "At its core is tending the garden of the heart: pulling out greed, jealousy, comparison, selfishness, laziness, resentment and self-attachment, to name only a few.",
        "It is hard, vast work, and it is work each person can begin with themselves.",
    ]),
    ("slides_xfgc_en/slide_13.png", [
        "Xuefeng says his main task is to harvest the ripe crop, and Xuefeng Communism is only a by-product.",
        "It was set up so that Chanyuan Celestials could settle their worldly ties, repay their debts and perfect the antimatter structure of LIFE, and so go on to the Thousand-Year World, the Ten-Thousand-Year World, the World of Ultimate Bliss and the Celestial Islands Continent.",
        "So it is not only a road to happiness for working people. It is also a road to becoming celestials and Buddhas for those who cultivate.",
        "Those who cultivate will come to see it: only those who give their whole heart to the happiness of all humanity can hope to leave the cycle of rebirth and enter heaven.",
    ]),
    ("slides_xfgc_en/slide_14.png", [
        "Number 621 of the 800 Values for New Era Human Beings says: dissolving the small family and forming the great family of Xuefeng Communism is the necessary road for humanity in the new era.",
        "That road has already been opened. In the Second Home, nearly everyone lives happily, joyfully, freely and contentedly.",
        "Whether people believe it or not, whether they want it or not, the program has already begun.",
        "It is not a monster. It is fine rain, and spring sun.",
    ]),
]
