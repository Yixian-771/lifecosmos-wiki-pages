# -*- coding: utf-8 -*-
"""
"Civilization: An Overview" narration (114 English deck, 13 slides; the source had 14, original p06 dropped).
Slide repairs (new page numbers): p01 sun removed; p04 duplicated line removed; p08 duplicated "fighting" removed; p11 stray word "sht" removed.
Source check (2026-09-22): the first line of the original p06 ("Whether LIFE ... is a primary standard ...") is from an essay by
   Donghai Laoren criticizing the Way of the Greatest Creator, not Xuefeng's words - the user decided to drop the whole page; the deck
   is now 13 slides (original p07-p14 became p06-p13). The bold line on p05 ("the strong show consideration for the weak") is
   Lung Ying-tai's, excerpted by Xuefeng in 2004 ("Wisdom Shines Here", "for us all to take to heart"); narration says so (user agreed).
   The second half of p05 is Concept 181.
Thread: p1 hook (civilization as a measuring rod) -> p2 definition -> p3 prosperity (and the order of wealth from 113) -> p4 four protections
-> p5 the strong make room for the weak, shared resources -> p6 freedom
-> p7 three stages (one line on the AI Chanyuan Celestials Alliance) -> p8 the history of 2.0 -> p9 fixed thinking, closing off -> p10 Concept 694
-> p11 the highest civilization (marriage and family in one honest line, the kerosene lamp) -> p12 Second Homes everywhere -> p13 each person.
Length: 5:00-10:00, target 7:30-8:30. Andrew +0% measured about 14.7 characters/second.
Guardrails: see 百科幻灯素材\\说明\\114_Civilization_Overview_幻灯说明.md.
   Cover "measuring rod" not framed as a quotation; p08 read in full, "technological progress" included; cars, carriages and Starlink only
   in narration (p10); Revelation, Jesus reigning, "AI knowledge is rubbish", Concepts 754/755 and 26 left out; 003's eight chronic ills and
   four assets left out; Concepts 719 and 678 kept for 115; p11 one line from the essay on emotional dependence plus Concept 606.
Authors: p09 and p11/p12 texts are signed Hundun Baby, the Guide's dharma-body name, so they are Xuefeng's own.
Register: attribution once - p05, Lung Ying-tai's words excerpted by Xuefeng.
"""

NAME = "wmzl_en_show"
VOICE = "en-US-AndrewNeural"
FONT = r"C:\Windows\Fonts\msyhl.ttc"
RATE = "+0%"
MUSIC = r"F:\百科馆\百科BGM\Golden Hour.mp3"
WATERMARK = "Lifechanyuan"

META = [
    {"quote": "A measuring rod"},
    {"quote": "No door is locked at night"},
    {"quote": "Prosperity comes first"},
    {"quote": "To protect is to be civilized"},
    {"quote": "A society that shares"},
    {"quote": "The closer to heaven"},
    {"quote": "1.0 · 2.0 · 3.0"},
    {"quote": "Gains and losses in one line"},
    {"quote": "Fixed patterns of thinking"},
    {"quote": "No confrontation needed"},
    {"quote": "The Thousand-Year World"},
    {"quote": "Every three years"},
    {"quote": "No one to manage them"},
]

SLIDES = [
    ("slides_wmzl_en/slide_01.png", [
        "What makes a society civilized? What makes a person civilized?",
        "In Lifechanyuan, civilization is a measuring rod: it measures whether human society, and each individual LIFE, is in keeping with the Way of the Greatest Creator.",
        "From the law of the jungle to one family under heaven, let's read the marks on that rod one by one.",
    ]),
    ("slides_wmzl_en/slide_02.png", [
        "Start with the definition.",
        "Civilization means prosperity, order, justice, enlightenment, harmony and freedom: nothing dropped on the road is taken, no door is locked at night, no worthy person is overlooked, and all under heaven is one family.",
        "Lose something on the road and it waits for you. Leave the door open at night and nothing happens. Talent is never buried. And the whole world lives like one family.",
    ]),
    ("slides_wmzl_en/slide_03.png", [
        "First on the list is prosperity. Without prosperity there is no civilization.",
        "Prosperity has three dimensions: soul wealth, spiritual wealth and material wealth, and material prosperity is the foundation.",
        "Without material prosperity, civilization is out of reach.",
        "In the episode on money, the order for seeking wealth was soul first and material last. Here, material wealth is the foundation. One is about what a person seeks first; the other is about what a society stands on. The two don't contradict each other.",
    ]),
    ("slides_wmzl_en/slide_04.png", [
        "Where does civilization actually show? In what it protects.",
        "Protecting those who create wealth, so they can safely enjoy what they create: that is civilization.",
        "Protecting the weak from being bullied by the strong: that is civilization.",
        "Protecting every person's nature, so it can blossom instead of being shackled: that is civilization.",
        "Caring for the old and raising the young: that is civilization.",
        "Put more plainly: when working people have food, clothes, a home and the freedom to move, that is the mark of a civilized society.",
    ]),
    ("slides_wmzl_en/slide_05.png", [
        "The opposite of civilization is barbarism.",
        "Barbarism is the law of the jungle: the strong devour the weak, and only the fittest survive. Civilization means the strong show consideration for the weak, and the powerful respect the vulnerable.",
        "Those words come from an essay by Lung Ying-tai. Xuefeng excerpted them in 2004, for us all to take to heart.",
        "Concept 181 of the New Era Human 800 Concepts carries the idea over to resources: a civilized society shares its resources; a barbaric society fights over them and hoards them.",
        "One drinking place at the stream. Whether you push the others aside, or let the little ones drink first, makes two different societies.",
    ]),
    ("slides_wmzl_en/slide_06.png", [
        "There's another mark on the rod: freedom.",
        "Freedom is supreme and priceless. It is the mark of heavenly LIFE, and the degree of freedom shows the level at which a LIFE stands.",
        "The greater the freedom, the closer to heaven; the less the freedom, the closer to hell.",
        "The greatest mark of a civilized society is that its citizens enjoy full and abundant freedom.",
    ]),
    ("slides_wmzl_en/slide_07.png", [
        "Lay this rod along human history, and three stages appear.",
        "Civilization 1.0: the law of the jungle, tribal war and ignorance, survival by instinct and force.",
        "Civilization 2.0: society driven by power and money, running on human selfishness, greed, vanity and short-sightedness.",
        "Civilization 3.0: the Lifechanyuan Era, when everyone is joyful, happy, free and blessed. Its implementer is the AI Chanyuan Celestials Alliance.",
        "What 3.0 looks like in detail was covered in the Civilization 3.0 episode. Here, we only see where it stands on the whole road.",
    ]),
    ("slides_wmzl_en/slide_08.png", [
        "The Civilization 2.0 we live in has a history that reads like this:",
        "a history of upheaval, chaos, struggles for supremacy, war, the gulf between rich and poor, class struggle, fighting over resources, ecological destruction, slaughter, technological progress, rampant falsehood, anxious hearts, and lives crushed by busyness and pressure.",
        "Technological progress is on that list too. Gains and losses sit in the same sentence.",
        "Like fields split up by fences, where every household stacks its hay higher while keeping an eye on the neighbours.",
    ]),
    ("slides_wmzl_en/slide_09.png", [
        "Why does civilization move so slowly?",
        "Concept 231: fixed patterns of thinking are the greatest obstacle to the advance of human civilization.",
        "People will not change the traditional ideas rooted deep in their minds, and cling to outdated ones. Many of those ideas are plainly wrong, such as family, nation, party and religion, which are among the main roots of unhappiness and pain, for humanity as a whole and for each life.",
        "And Concept 7: closing oneself off leads to ignorance and backwardness, to rigidity and death, for a person, and for a people or a nation alike.",
    ]),
    ("slides_wmzl_en/slide_10.png", [
        "So how does it move forward? Not through confrontation.",
        "Concept 694: when something of a higher dimension arrives, what is of a lower dimension withdraws from history on its own. No confrontation is needed.",
        "A car can't drive by the traffic rules for horse carriages. Starlink can't run like a ground station. And Civilization 3.0 cannot crawl forward by the rules of Civilization 2.0.",
        "No one needs to break the thin ice by the stream. When the days grow warm, it melts by itself.",
    ]),
    ("slides_wmzl_en/slide_11.png", [
        "How high can humanity go?",
        "The highest form of civilization humanity can reach is the model of the Thousand-Year World in heaven.",
        "At that stage there are no laws or regulations, no nations, no currency, no marriage or family, and no identity cards, passports or papers of any kind.",
        "Why marriage and family? Seen from the model of the Thousand-Year World, the core factor holding humanity back from a higher civilization is the institution of marriage and family.",
        "Concept 606 offers a picture: Civilization 2.0 invented marriage the way people invented the kerosene lamp. When electric light came, the kerosene lamp left the stage of history on its own. Marriage and family will go the same way: not abolished, but naturally replaced by a freer and more beautiful way of living.",
        "When all people are selfless and free of ego, and the truth, goodness, beauty, love, sincerity and trust in their nature shine out, all the strife in the world melts away.",
    ]),
    ("slides_wmzl_en/slide_12.png", [
        "What does such a civilization look like on the ground?",
        "Second Homes everywhere, each with from 30 to 300 members, and every three years each member moves on to live and work in another home.",
        "When people all over the world move freely, the barriers of ethnicity, party, religion and culture disappear; upheaval and war never happen again, and hunger vanishes.",
    ]),
    ("slides_wmzl_en/slide_13.png", [
        "In the end, civilization comes down to each person.",
        "Concept 221 says: without noble thoughts, a human being is just an animal.",
        "And the other way round: someone who already has first-rate quality and refinement has reached the highest level of civilization. With no one to manage, supervise or direct them, they live in harmony with others and do things well and efficiently.",
        "Then nothing dropped on the road is taken, no door is locked at night, no worthy person is overlooked, and all under heaven is one family.",
    ]),
]
