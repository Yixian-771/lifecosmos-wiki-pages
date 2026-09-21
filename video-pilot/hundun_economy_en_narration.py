# -*- coding: utf-8 -*-
"""
"Hundun Economy - Market Economy - Planned Economy" narration (110 English deck, 14 slides, 1:1 with the source).
The English deck passed the page-by-page check: one consistent style, blue sky and clear water throughout, no garbled text.
(The Chinese deck p02-p06 came back in a cartoon style with speech bubbles, and p03 lost text at the right edge;
the user is regenerating those, so only the English render runs now.)
Thread: p1 hook (two models, neither civilized) -> p2 strengths, and which side of human nature each calls on
-> p3 five of the eight flaws of planning -> p4 planning against nature -> p5-p6 flaws of the market
-> p7 a heavenly economy -> p8 resources belong to the Greatest Creator -> p9 international big family and AI
-> p10 money gone, F Coin -> p11 no planning and no market -> p12 crime, armies, suicide lose their soil
-> p13 everyone free; the sages, not government -> p14 where humanity's future hope lies.
Length: 5:00-10:00, target 7:00-7:45. Andrew +0% is about 15.1 characters/second.
Guardrails and separation: see 百科幻灯素材\\说明\\110_Hundun_Economy_幻灯说明.md.
   Country names are spoken as the source has them (user's call, 2026-09-19); no flags, maps or borders in the pictures.
   Say plainly that lists are only part of the whole: eight flaws of planning (five given), eighteen principles (a few given).
   Courts handled by intelligent robots (principle 4) and no need for defence spending (principle 15) are both said.
   108 already covered the heavenly economic model and the difficulty of purifying the heart: one line only here.
   013 F Coin, 111 Heavenly Bank and 112 the view of money are separate entries: one page on money, no more.
Register: attribution twice (p1 Lifechanyuan's verdict, p7 Lifechanyuan's answer), plus the Greatest Creator's viewpoint on p7.
"""

NAME = "hdjj_en_show"
VOICE = "en-US-AndrewNeural"
FONT = r"C:\Windows\Fonts\msyhl.ttc"
RATE = "+0%"
MUSIC = r"F:\百科馆\百科BGM\Golden Sunset.mp3"
WATERMARK = "Lifechanyuan"

META = [
    {"quote": "Neither economy is a civilized economy"},
    {"quote": "Each has strengths, and each has flaws"},
    {"quote": "Plans made in an office"},
    {"quote": "Planning goes against the way of nature"},
    {"quote": "The rich get richer, the poor get poorer"},
    {"quote": "The jungle economy of the animal world"},
    {"quote": "A copy, on Earth, of heaven's economy"},
    {"quote": "Resources belong to no nation"},
    {"quote": "The international big family"},
    {"quote": "Money disappears, F Coin circulates"},
    {"quote": "No planning, and no market either"},
    {"quote": "No soil left to grow in"},
    {"quote": "Everyone free, everyone willing"},
    {"quote": "Where humanity's future hope lies"},
]

SLIDES = [
    ("slides_hdjj_en/slide_01.png", [
        "Today most people on Earth live inside one of two economic models. One or the other.",
        "The capitalist countries led by the United States run a market economy.",
        "The socialist countries led by China run a planned economy.",
        "The argument has gone on for more than a century, each side with its reasons and its believers.",
        "Almost every economic debate we grow up hearing stays inside those two options.",
        "Lifechanyuan's verdict is blunt: neither of them is a civilized economy.",
        "A planned economy will surely lead to poverty and backwardness; a market economy will surely lead to the collapse of Earth's ecology.",
    ]),
    ("slides_hdjj_en/slide_02.png", [
        "Start with what each one genuinely does well, because the strengths are real.",
        "A market economy fully rouses people's drive to pursue gain, but it leaves them permanently inside a tense competition.",
        "A planned economy can gather resources and accomplish great things, but everything is steered by human will, and attending to one thing means neglecting another.",
        "Look one layer deeper: which side of human nature does each one call on?",
        "A market economy calls on the evil side of human nature; a planned economy calls on the cunning side.",
        "One runs on grabbing, the other on scheming. Neither is the best choice.",
        "Note that this is not saying one side's people are bad. It is saying what each machinery naturally pulls out of us.",
    ]),
    ("slides_hdjj_en/slide_03.png", [
        "Take the planned economy first. The source lists eight flaws; here are five of them.",
        "One: plans made in an office cannot keep up with a changing world.",
        "Two: whoever holds the power to hand out resources is easily corrupted.",
        "Three: it crushes initiative and creativity, so talents and things are never put to their best use.",
        "Four: costs climb, waste grows, and goods become fewer and fewer.",
        "Five: citizens are kept from going abroad and outside information is shut out, driving society toward extremism and ignorance, and toward confrontation with the outside world.",
    ]),
    ("slides_hdjj_en/slide_04.png", [
        "Behind all five lies one thing: planning goes against the way of nature.",
        "If the day you are born, the day you marry and the day you die were all planned, what would there be to live for? Where would the surprises be?",
        "Plan how many factories a country builds, how big every house is, what everyone eats for breakfast, and the result is a mess.",
        "Water finds its own way. Drive in stakes to force it into a straight channel and it spills through the gaps and goes on along its own path.",
        "A human life is water too. The tighter the plan, the more places it runs over the edge.",
    ]),
    ("slides_hdjj_en/slide_05.png", [
        "Now the market economy. Its flaws are just as clear, and again these are only a few of them.",
        "The rich get richer and the poor get poorer.",
        "Savage competition exploits resources with no thought for future generations, and Earth's ecology decays ever faster.",
        "Money above all: people's ties become naked interest, and warmth is gone.",
    ]),
    ("slides_hdjj_en/slide_06.png", [
        "And demand keeps swelling like a balloon being pumped without end. A great slump every so often is bound to come.",
        "Where you eat only by your own ability, those born weaker are pushed to the margins, their dignity gone.",
        "In truth, the market is the jungle economy of the animal world.",
        "A jungle has its abundance too. It just grows on top of the weak.",
        "If neither road goes through, what is the third one?",
    ]),
    ("slides_hdjj_en/slide_07.png", [
        "Lifechanyuan's answer is called the Hundun Economy.",
        "The Hundun Economy belongs to the economic model of heaven: a copy, on Earth, of heaven's early economic model.",
        "Its aim is for every person on Earth to enjoy the beauty of life.",
        "Free of worry about food, clothing, shelter, birth, age, sickness and death, living out the finest qualities of LIFE: truth, goodness, beauty, love, faith and sincerity.",
        "One thing to keep in mind as we go on: all of this is set out from the viewpoint of the Greatest Creator, from where the celestials and the buddhas stand. It is a picture drawn by a higher form of civilization looking down.",
        "Eighteen principles are laid out for how such an economy runs. We will take a few of them.",
    ]),
    ("slides_hdjj_en/slide_08.png", [
        "The whole model rests on one premise, and once that premise shifts, everything after it shifts too.",
        "All of Earth's natural resources belong to the Greatest Creator and to all humanity, not to any nation, people, group or individual.",
        "Earth is humanity's common home, and every person has the God-given right to move and settle freely across it.",
        "If resources belong to no one, owning them loses its ground, and everything built on top of owning goes slack.",
        "Borders, property, monopoly: these are not overthrown. They simply lose the ground they stood on.",
    ]),
    ("slides_hdjj_en/slide_09.png", [
        "So how do people live? The institution of marriage and the small family disappear.",
        "People live, work and make their lives in international big families, which care for the old and raise the young.",
        "Education and medical care are free; the running of the whole society is set by AI.",
        "Courts, too, are handled by intelligent robots.",
    ]),
    ("slides_hdjj_en/slide_10.png", [
        "And money? Money, the symbol of material wealth, disappears; F Coin, the symbol of spiritual wealth and wealth of the heart, circulates.",
        "The more F Coin a person has, the more they have given to humanity.",
        "People will find that the richer the heart and spirit, the more abundant material wealth becomes.",
        "Money measures how much you have taken in. F Coin measures how much you have given out.",
    ]),
    ("slides_hdjj_en/slide_11.png", [
        "Then how is production organized? Here is the decisive step: no planning is needed, and no market either.",
        "What each person needs and uses is worked out precisely by AI, so no factory makes a single surplus product.",
        "Work is shared out across the globe: each place offers its own climate, land and talent to serve all humanity.",
        "And everything it needs is met by others in turn.",
        "Nobody decides it in an office, and nobody fights for it. It flows from what is actually needed.",
    ]),
    ("slides_hdjj_en/slide_12.png", [
        "Once that structure stands, many old problems are not suppressed. They have no soil left.",
        "Theft, robbery, corruption and drug trafficking disappear, with no soil left to grow in.",
        "With people moving freely across the globe, armies and weapons are no longer needed, and there is no need for defence spending at all.",
        "The depression, anxiety and pressure that lead to suicide all disappear.",
        "That distinction matters: the behavior is not being policed. It simply has nothing to grow from.",
    ]),
    ("slides_hdjj_en/slide_13.png", [
        "At this point someone will ask: what about people who do not want to live this way?",
        "For those who do not want to live in an international big family, a place is left.",
        "Suppose, for example, Australia were left to them to live their own way.",
        "And those who wish to live in the big family are brought over from Australia.",
        "Everyone free, everyone by their own choice.",
        "Only a symbolic global government remains.",
        "What actually makes the Hundun Economy run is not government, but the sages among humanity.",
        "That line is the floor the whole model stands on: it rests not on control, but on the quality of the people.",
    ]),
    ("slides_hdjj_en/slide_14.png", [
        "And this is not only a proposal. Over a dozen years of heavenly economic practice in the Second Home have gone beyond both the market economy and the planned economy.",
        "It is where humanity's future hope lies.",
        "And it is the surest guarantee that humanity can survive in the age of strong artificial intelligence.",
    ]),
]
