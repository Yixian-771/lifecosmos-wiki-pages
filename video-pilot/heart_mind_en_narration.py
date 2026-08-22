# -*- coding: utf-8 -*-
"""
"Heart-Mind" slide narration (027 English, 15 art slides, no photo pages).
Each element = (slide image, [sentences]). One sentence = one subtitle.
Written independently from en internal.md (not a translation of the zh script).
Deck restructured by NotebookLM to 15 pages (verified page by page):
source "behind the mind is Nature / overthinking" EXPANDED into three English pages —
p05 "The Three Operating Systems" (Brain/Heart-Mind/Nature table), p09 "Behind the
Heart-Mind Lies Nature", p10 "The Law of Inverse Visibility".
Order: cover (p1) -> architecture of consciousness (p2) -> the occupant (p3)
-> scope/ladder (p4) -> three operating systems (p5) -> arising & ceasing (p6)
-> the reflection engine (p7) -> the trigram formation (p8) -> behind lies Nature (p9)
-> inverse visibility (p10) -> the release mechanism (p11) -> do not rely on the mirror (p12)
-> expanding the heart, macro (p13) -> anatomy of a no-heart life, micro (p14)
-> live your Nature (p15, teases Affection).
"上帝" is rendered as "the Greatest Creator"; terminology follows the deck (Heart-Mind, Nature, Trigram Formation).
"""

NAME = "hm_en_show"
VOICE = "en-US-AndrewNeural"
FONT = r"C:\Windows\Fonts\georgia.ttf"
RATE = "+0%"
MUSIC = r"F:\百科馆\百科BGM\Open Fields.mp3"
WATERMARK = "Lifechanyuan"

META = [
    {"quote": "The empty room"},
    {"quote": "The architecture of consciousness"},
    {"quote": "Empty — alive only when spirit enters"},
    {"quote": "How large a world can your heart-mind hold"},
    {"quote": "Brain, heart-mind, and Nature"},
    {"quote": "The three heart-minds cannot be grasped"},
    {"quote": "The heart-mind is a mirror"},
    {"quote": "The heart-mind is a trigram maze"},
    {"quote": "Behind the heart-mind lies Nature"},
    {"quote": "When the heart-mind stills, Nature is revealed"},
    {"quote": "Discard the heart-mind"},
    {"quote": "Do not rely on the mirror"},
    {"quote": "Expanding the heart of the cultivator"},
    {"quote": "The anatomy of a no-heart life"},
    {"quote": "Live your Nature"},
]

SLIDES = [
    ("slides_hm_en/slide_01.png", [
        "Have you ever tried, with all your strength, to change yourself — and failed?",
        "The Lifechanyuan teaching says it isn't that you didn't try hard enough — you've been pushing on the wrong place.",
        "Today, one word: heart-mind. Your heart-mind is an empty room — whatever moves in is what you become.",
    ]),
    ("slides_hm_en/slide_02.png", [
        "Four words we constantly confuse — let's set them inside one bedroom.",
        "Heart-mind is the space of thinking — like a bedroom, like a factory's workshop.",
        "Heart-mind-spirit is the information flowing in and out — the furnishings and the occupant; thinking is how that information judges and reasons — the occupant's way of living.",
        "And consciousness is the result — a relatively stable nonmaterial structure, the whole lived atmosphere of the room.",
    ]),
    ("slides_hm_en/slide_03.png", [
        "Here is the key: the heart-mind is fashioned by heaven and earth, yet at its core it is empty.",
        "It comes alive only when spirit enters it; when spirit leaves, the person becomes a vegetable.",
        "The same room blazes with life when the spirit-light enters, and fades to a bare shell when it departs.",
        "And when the spirit that enters is of low level and small energy, the person turns rigid and dull.",
    ]),
    ("slides_hm_en/slide_04.png", [
        "So how large can a heart-mind be? It depends on the energy of the spirit that dwells inside.",
        "When the spirit of the Greatest Creator enters, the heart-mind is the entire universe; a Buddha's spirit fills the whole antimatter world; a celestial's holds all the higher spaces of LIFE.",
        "A king's spirit spans a nation; a sage's holds all of Earth's phenomena; an ordinary person's holds nation, family, and friends.",
        "A worldly person's is occupied by money, power, fame, and resentment; and a muddled person's holds only the instinct to eat and sleep.",
    ]),
    ("slides_hm_en/slide_05.png", [
        "Line up the three operating systems of a human life: the brain, the heart-mind, and Nature.",
        "The brain calculates and reasons — and the more it develops, the further it drifts from Nature.",
        "The heart-mind reflects and reacts — an ungraspable illusion, rising and falling with conditions, actively obscuring Nature when it stirs.",
        "Only Nature is the true, invisible structure of LIFE — still, clear, the ultimate unchanging reality, the essence of a Buddha.",
    ]),
    ("slides_hm_en/slide_06.png", [
        "Shakyamuni Buddha said something strange: the past heart-mind cannot be grasped, the present cannot be grasped, the future cannot be grasped.",
        "Why not? Because the heart-mind arises with conditions, shifts with conditions, ceases with conditions.",
        "Conditions are unreal and illusory — so the heart-mind is unreal and illusory too, never to be held.",
        "This is why the Buddha is without heart-mind: the moment there is heart-mind, it is no longer Buddha.",
    ]),
    ("slides_hm_en/slide_07.png", [
        "So what is this heart-mind, really? It is a mirror.",
        "Ten thousand forms give rise to the heart-mind; the heart-mind gives rise to ten thousand forms — without the outer world, there is no heart-mind.",
        "To be moved by conditions is the ordinary person; to move conditions with the heart-mind is the immortal — yet even that is passive and never final, for conditions never end.",
        "The heart-mind is empty, the heart-mind is nothing — it can never be relied upon.",
    ]),
    ("slides_hm_en/slide_08.png", [
        "Go one layer deeper: in truth, the heart-mind does not exist. By nature, people have no heart-mind — it is only a trigram formation.",
        "People are caught inside the maze without realizing it; they believe they have a heart-mind, and so are bound by its sorrows, partings, and worries.",
        "Without heart-mind, a person becomes an immortal, a Buddha.",
        "Escape this maze, and you step out of every human grief into a bright, boundless spring.",
    ]),
    ("slides_hm_en/slide_09.png", [
        "What is reliable, then? The thing behind the heart-mind — Nature.",
        "Nature is the characteristic of LIFE's structure; whatever structure a LIFE has, such is its Nature.",
        "Nature is non-material and invisible — the heart-mind cannot capture it, and the brain has no access to it.",
        "The more developed the brain, the busier the thinking, the further you stand from Nature.",
    ]),
    ("slides_hm_en/slide_10.png", [
        "The heart-mind and Nature have no direct relationship, but one iron law binds them.",
        "When the heart-mind stirs, Nature is obscured; when the heart-mind stills, Nature is revealed.",
        "Picture a pearl on the bed of a pool: while the water churns it vanishes, and only when the water settles does it shine.",
        "So how do you live out your Nature? By living without relying on heart-mind or brain — that, itself, is living your Nature.",
    ]),
    ("slides_hm_en/slide_11.png", [
        "There is a release mechanism, and it is simple.",
        "Dwell in form, in sound, scent, taste, or touch, and the heart-mind grasps; abide nowhere, and the heart-mind releases.",
        "The World-Honored One taught: give rise to the heart-mind without any fixed abode — in a word, discard the heart-mind, become a person without one.",
        "Laozi said his great trouble was having a self; extend it to the heart-mind — heartbreak exists only because we have a heart-mind, so without one, where could it break?",
    ]),
    ("slides_hm_en/slide_12.png", [
        "The conclusion the teaching repeats: do not rely on the mirror.",
        "Profit blinds wisdom, wisdom blinds the heart-mind, the heart-mind blinds Nature — the more you calculate, the further from your true Nature you drift.",
        "The mirror reflects reality, but it is not reality itself; Bodhidharma said, to seek Buddha you must see your Nature — seeing Nature is Buddha.",
        "So do not chase profit, do not display cleverness, do not rely on the heart-mind — let your original Nature bloom.",
    ]),
    ("slides_hm_en/slide_13.png", [
        "What, then, does the cultivator's heart-mind look like? First, outward — an infinite embrace.",
        "It takes the people's heart as its own: their joy is my joy; it takes all things as its own — trees, insects, and birds all nurture me, and all things live in my heart.",
        "It takes the universe as its own: the universe exists, I exist; my heart dissolves into it.",
        "And it takes the spirit of the divine as its own — clothed in Jesus's armor, holding Shakyamuni's staff.",
    ]),
    ("slides_hm_en/slide_14.png", [
        "Then, inward — an infinite fineness.",
        "It takes mercy as its own, tender as new buds in early spring, gathering all beings into its embrace; it takes the Infinite as its own, beyond glory and disgrace, beyond life and death.",
        "It takes harmony as its own — letting clouds roll, letting flowers bloom and fall.",
        "And it takes no-heart-mind as its own — for heart-mind is the source of every trouble; the Greatest Creator is my spirit, the nature of the Tao is my heart-mind.",
    ]),
    ("slides_hm_en/slide_15.png", [
        "So we return to where we began: the heart-mind is empty, conditions are illusion — then without a heart, how do you live?",
        "You live your Nature. Buddha is Nature, Nature is Buddha — to live your Nature is to live as a Buddha, as an immortal.",
        "Living with neither heart-mind nor brain, yet perfectly at ease — that is the whole secret.",
        "Next time, we turn to Affection — the thing that stirs the moment the heart moves. What is it, really? See you then.",
    ]),
]
