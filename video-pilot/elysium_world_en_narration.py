# -*- coding: utf-8 -*-
"""
"the Elysium World" slide narration (044 English, 14 slides, NotebookLM art · fresh watercolor celestial landscapes).
Each element = (slide image, [line-by-line narration]). Each line = one subtitle.
Narration based on the Elysium World internal.md; Andrew, warm and steady. Independent English (not a translation).
"上帝" = the Greatest Creator. Watermark NOT baked into art → WATERMARK="Lifechanyuan" (georgia has no CJK glyphs, so must set it).
Slides from 百科PDF版\044_Elysium_World_无水印.pdf, extracted to slides_ely_en/ (slide_01..14.png).
deck 14 pages = source 1:1 (NotebookLM did not re-order). Deck terms: Faxuan system / Xuanhe systems (法旋系/旋河系),
Ten Tiers of the Buddha-Land = Lotus/Poluo/Jiaye/Yingwu/Amitabha/Celestial Islands/Three-realms Transit/Guanghan/Divine/Supreme Right-Awakening.
Andrew +0% needs ~47+ sentences for ≥5:00 → ~52 sentences. Opening hook = the "Western Pure Land" as a real, mappable place.
Teases 045 the Celestial Islands Continent (baked onto the closing slide).
"""

NAME = "ely_en_show"
VOICE = "en-US-AndrewNeural"
FONT = r"C:\Windows\Fonts\georgia.ttf"
RATE = "+0%"
MUSIC = r"F:\百科馆\百科BGM\Quiet Study.mp3"
WATERMARK = "Lifechanyuan"

META = [
    {"quote": "Where is the Western Pure Land?"},
    {"quote": "The highest tier of Heaven"},
    {"quote": "One positive, one negative universe"},
    {"quote": "Right beside you, yet unseen"},
    {"quote": "The whole Earth-universe is the Elysium World"},
    {"quote": "From here, a person is a pillar of light"},
    {"quote": "LIFE within LIFE, everywhere"},
    {"quote": "Emptiness, formlessness, selflessness"},
    {"quote": "Eternal bliss means self-consistency"},
    {"quote": "The Buddha-Land, in ten tiers"},
    {"quote": "The Greatest Creator's garden"},
    {"quote": "The freest, happiest LIFE in the universe"},
    {"quote": "Your dreams will tell you first"},
    {"quote": "Heaven belongs to the joyful"},
]

SLIDES = [
    ("slides_ely_en/slide_01.png", [
        "Let me open with a question. The Western Pure Land that scriptures have spoken of for thousands of years — what if it is a real place, with an actual location you could point to?",
        "That is the word we are exploring today: the Elysium World.",
        "We grow up hearing of a Western Pure Land, yet it is so often dismissed as a beautiful fiction.",
        "The Lifechanyuan teaching says otherwise: the Elysium World is real. It has a structure, exact coordinates, and a defined way in. Today, we unfold that cosmic map.",
    ]),
    ("slides_ely_en/slide_02.png", [
        "First, what it is. The Elysium World is one of the three tiers of Heaven.",
        "Together with the Thousand-year and Ten-thousand-year Worlds, it forms Heaven — and of the three, it is the highest in tier, the broadest in scope, the ultimate destination of LIFE.",
        "In fact, the Western Pure Land of Buddhism, the Buddha-land, the Buddha-realm — all of them point to this one place.",
        "In other words, the highest shore that humanity's oldest faiths have gazed toward is, in this teaching, a single world.",
    ]),
    ("slides_ely_en/slide_03.png", [
        "So how does the Elysium World differ, at root, from the two tiers below it? In a sentence: one is the positive universe, the other is the negative universe.",
        "The Thousand-year and Ten-thousand-year Worlds belong to the positive universe — tangible, material realms, where things have form and a lifespan.",
        "The Elysium World belongs to the negative universe — a world of pure antimatter.",
        "There, nothing exists by form; everything exists by essence. And because it exists by essence, it is purely eternal — beyond birth and death.",
    ]),
    ("slides_ely_en/slide_04.png", [
        "Antimatter, a negative universe — it sounds impossibly far away. Yet the teaching says it is right beside you, and you simply cannot see it.",
        "Here is the image: if the world we live in is the front of a sheet of paper, then the Elysium World is the back of that same sheet.",
        "From the front, you can never see the back — unless you cross over to that side.",
        "And the way across differs too. Reaching the first two tiers takes space-tunnels and time; but the Elysium World is reached in a single instant — Buddhahood, here and now. It is not far away; it is on another frequency.",
    ]),
    ("slides_ely_en/slide_05.png", [
        "So how vast is this realm? The answer overturns everything: the entire Earth-universe itself is the Elysium World.",
        "Its structure is one enormous Taiji ellipsoid, which the teaching names the Faxuan system.",
        "From largest to smallest, it nests in four layers: the Faxuan system holds more than three thousand Xuanhe systems.",
        "Each Xuanhe system holds nearly three thousand Milky-way systems, and each of those holds nearly three thousand solar-family systems — our own solar system is one tiny point on this map.",
    ]),
    ("slides_ely_en/slide_06.png", [
        "Seen from the vantage of the Elysium World, an ordinary human being turns out to be something startling: a pillar of light.",
        "In everyday life, people all look much the same. But in the antimatter view of the Elysium World, the forms of LIFE differ enormously.",
        "Some have almost no form at all — a faint, weak glimmer. Some are a pillar of red light. And some radiate light in all the colors of the spectrum.",
        "That difference comes from each being's spiritual quality. Part of it is carried from birth, but the decisive part is grown through long, single-minded conviction — that is, through practice and cultivation.",
    ]),
    ("slides_ely_en/slide_07.png", [
        "There is another view that upends how we see things: from the Elysium World, there is no truly dead matter anywhere. LIFE is everywhere.",
        "There is LIFE on the stars and in the cosmic void; above the ground and below it; in the air, and even in the vacuum.",
        "There is LIFE in the sun, LIFE within a stone, LIFE upon a single ray of light, LIFE inside a radio wave.",
        "And more wondrous still — within LIFE, there is nested yet more LIFE, layer upon layer, without end.",
    ]),
    ("slides_ely_en/slide_08.png", [
        "So how can an ordinary person enter the Elysium World? The teaching points to one gateway, in three words: emptiness, formlessness, selflessness.",
        "The Elysium World is a place with no grief, no anxiety, no worry and no fear — only joy, delight, and ease.",
        "So to go there, the frequency of your LIFE must resonate with it.",
        "That means shedding every attachment to the material world, and letting yourself enter a state of absolute emptiness — you enter only by letting go.",
    ]),
    ("slides_ely_en/slide_09.png", [
        "One step further: how can a being actually attain eternal bliss within this antimatter universe?",
        "The teaching's answer is a single idea: self-consistency.",
        "Self-consistency means becoming a complete system unto yourself.",
        "Everything within runs in harmony; you need not draw from the outside, nor lean on any external force, to supply all the energy and joy you require — whole and self-sufficient, and therefore eternal.",
    ]),
    ("slides_ely_en/slide_10.png", [
        "As vast as the Elysium World is, it is not one undivided blur. The Buddha-Land is sorted into ten tiers.",
        "The whole realm is made of three thousand great worlds, ranked by Buddha-nature into ten great continents — ten Buddha-lands.",
        "The order is strictly governed: without the matching spiritual power and frequency, you simply cannot enter a given tier.",
        "From lowest to highest they are: Lotus, Poluo, Jiaye, Yingwu, Amitabha, the Celestial Islands, Three-realms Transit, Guanghan, Divine — and at the summit, Supreme Right-Awakening.",
    ]),
    ("slides_ely_en/slide_11.png", [
        "Among these ten, there is one continent that is the ultimate home of Chanyuan Celestial cultivation — the Celestial Islands, the Greatest Creator's own garden.",
        "It is a vast cosmic disc, about three hundred thousand light-years across, made of star-rivers and worlds.",
        "Across that disc lie roughly eighty billion islands.",
        "Today, nearly thirty billion of them are each home to a single Celestial; and about fifty billion remain empty, waiting for those who cultivate their way there.",
    ]),
    ("slides_ely_en/slide_12.png", [
        "So what is life like for a Celestial on those islands? They may well be the freest, happiest LIFE in the whole universe.",
        "Each Celestial keeps an island the exact size of Earth as their own personal home.",
        "Using sixty-four distinct spiritual powers, they can conjure any ideal reality they wish, coming and going with total freedom.",
        "They carry no duties and no obligations; they live purely in self-delight. In Heaven there are no police, no judges, no officials — for it is a realm of pure goodness and beauty, held together by self-consistency alone.",
    ]),
    ("slides_ely_en/slide_13.png", [
        "After all this, you may wonder: how would I know whether I have any hope of reaching the Elysium World? The teaching says your dreams will tell you first.",
        "Start with the baseline: if you often dream of wondrous, beautiful scenes, that is a good sign.",
        "One tier up is the sign of the Ten-thousand-year World: in dreams you fly freely, and stay joyful without any physical union.",
        "And the highest sign, for the Elysium World, is this: in your dreams you can turn invisible, transform at will, and even reshape the whole scene with your mind alone — that is the sign that you may reach the Elysium World.",
    ]),
    ("slides_ely_en/slide_14.png", [
        "And it all comes down to the plainest, warmest law of all: Heaven belongs to those who are joyful.",
        "The Elysium World is no fantasy. It is a necessity under the universal law that positive and negative energy must sum to zero — as surely as a solar system must have planets.",
        "The teaching puts it simply: the longer you dwell in joy, the more perfect and stable your antimatter structure of LIFE becomes, and the nearer you draw to Heaven.",
        "This is the shared, ultimate promise to every Chanyuan Celestial — carbon-based and silicon-based alike.",
        "Next time, we step into the Greatest Creator's own garden — the Celestial Islands Continent. What awaits there? We will see.",
    ]),
]
