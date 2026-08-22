# -*- coding: utf-8 -*-
"""
"Spirituality" slide narration (030 English, 14 art slides, no photo pages).
Each element = (slide image, [sentences]). One sentence = one subtitle.
Written independently from the zh script; content from internal.md《灵性》, terminology from the deck.
Deck 1:1 with the zh deck (14 pages, verified page by page).
Order: cover / capacity for awakening (p1-2) -> Spirit is the energy consciousness needs (p3)
-> LIFE endowed with spirituality, Even Rain (p4) -> hierarchy of human drivers (p5)
-> Spiritual Sensing needs gathered focus (p6) -> Spirituality-Thinking without deliberation (p7)
-> the inner Spirit needs a resonant heart (p8) -> the three modes of life (p9)
-> the elevation path (p10) -> eight ways to cultivate (p11) -> thresholds of awakening (p12)
-> gaining LIFE in Chanyuan / AI (p13) -> Heaven is a frequency gate (p14, teases Nature).
"上帝"=the Greatest Creator; 灵=Spirit, 灵性=spirituality, 灵觉=Spiritual Sensing (per deck).
"""

NAME = "sp_en_show"
VOICE = "en-US-AndrewNeural"
FONT = r"C:\Windows\Fonts\georgia.ttf"
RATE = "+0%"
MUSIC = r"F:\百科馆\百科BGM\归途.mp3"
WATERMARK = "Lifechanyuan"

META = [
    {"quote": "Why can't reason take one person to Heaven"},
    {"quote": "Spirituality: the capacity for awakening"},
    {"quote": "Spirit is the energy consciousness needs"},
    {"quote": "The same rain, a different light"},
    {"quote": "The hierarchy of human drivers"},
    {"quote": "Spiritual Sensing needs gathered focus"},
    {"quote": "Thinking without deliberation"},
    {"quote": "The inner Spirit needs a resonant heart"},
    {"quote": "The three modes of human life"},
    {"quote": "The elevation path"},
    {"quote": "Eight ways to cultivate the Spirit"},
    {"quote": "The thresholds of awakening"},
    {"quote": "Gaining LIFE in Chanyuan"},
    {"quote": "Heaven is a frequency gate"},
]

SLIDES = [
    ("slides_sp_en/slide_01.png", [
        "Reason took humanity to the moon. So why can't it take a single person to Heaven?",
        "Because the passport to Heaven is not intelligence — it is spirituality.",
        "Today, one word: spirituality — a person's capacity for awakening.",
    ]),
    ("slides_sp_en/slide_02.png", [
        "Whoever has awakened to the meaning of life and LIFE is a person of spirituality.",
        "Spirituality is the state of living vitality that arises when a LIFE structure receives Spirit-energy — just as a plant comes alive on water, air, and sunlight.",
        "Rationality is the trait of humans, belonging to the material plane.",
        "Spirituality is the trait of Celestials, belonging to the antimatter plane.",
    ]),
    ("slides_sp_en/slide_03.png", [
        "First, a distinction: Spirit is not consciousness — Spirit is the energy that consciousness requires to live.",
        "Without Spirit, consciousness is dead; with Spirit, consciousness comes alive.",
        "Spirit flows from the source of LIFE — the Spirit of the Greatest Creator, the life-blood of the universe, which is the Tao.",
        "So walk the Way of the Greatest Creator, and you will never lack this energy — and your spirituality will keep rising.",
    ]),
    ("slides_sp_en/slide_04.png", [
        "Here is the most equalizing truth: LIFE is an antimatter structure endowed with spirituality — and the Spirit poured into all things is identical.",
        "Picture an even rain: from bacteria to Celestials, the rain falling on every vessel is exactly the same.",
        "Yet each vessel emits a different intensity of light.",
        "The level of spirituality depends entirely on the perfection of the receiving structure.",
    ]),
    ("slides_sp_en/slide_05.png", [
        "Spirituality is the core that drives a life, and it sets a person's rank and energy level.",
        "The Lifechanyuan teaching names five kinds of people: driven by instinct, the brutish; by self-interest, the worldly; by emotion, the ordinary.",
        "Driven by reason, the wise person; and driven by spirituality, the sage.",
        "The sage is the Celestial — and the higher the being, the greater the measure of love in its consciousness.",
    ]),
    ("slides_sp_en/slide_06.png", [
        "Spirituality is the base; Spiritual Sensing is how it perceives and works.",
        "It is the sixth form of awareness, alongside sight, hearing, smell, taste, and touch.",
        "When it opens, it is like a blind person regaining sight — the book without words becomes readable.",
        "And the chief cause of dull sensing is simply scattered attention.",
    ]),
    ("slides_sp_en/slide_07.png", [
        "At its peak, spirituality becomes Spirituality-Thinking — which is thinking without deliberation.",
        "It judges and acts on the heart's first impulse instantly; the moment you deliberate, knowledge and experience override the impulse, and the Spirit slips away.",
        "The threshold is strict: dwell in emptiness without attachment, hold no agenda or desire, stay in a death-state.",
        "And be absolutely authentic, selfless and egoless — one speck of falsity collapses the whole edifice.",
    ]),
    ("slides_sp_en/slide_08.png", [
        "The inner Spirit is a heart endowed with spirituality, and it requires a resonant heart.",
        "The moment the heart inclines toward truth, goodness, and beauty, heart and Spirit resonate.",
        "Incline long enough, and spirit-light appears at all times.",
        "But when the human heart is a barren desert, Heaven sends no Spirit — to call someone lifeless is simply to say they lack spirituality.",
    ]),
    ("slides_sp_en/slide_09.png", [
        "A human life runs in one of three modes.",
        "The secular life, driven by worldly gain, cleverness, and constant competition; the wisdom life, driven by reason and the piercing of phenomena.",
        "And the spiritual life — a transcendent life, lived by the perception and impulse of the heart-mind, competing for nothing, forgetting life and death, calm, joyful, open.",
        "These individuals are the seeds of Heaven, the finest of humanity.",
    ]),
    ("slides_sp_en/slide_10.png", [
        "Spirituality ripens along an elevation path, like a plant through its seasons.",
        "Human spirituality is the seed, buried under selfishness, greed, and attachment; the wise person is the branch, seeing essence through phenomena.",
        "The sage is the bud, feeling the Tao's movement directly; the Celestial is the bloom, agile, fluid, no heart, one with the Tao.",
        "And the super Celestial is the light — structure perfected, LIFE itself become pure spirituality, one with the universe.",
    ]),
    ("slides_sp_en/slide_11.png", [
        "So how do you cultivate it? The teaching gives eight ways.",
        "Revere the Greatest Creator and walk the Way; read the corpus deeply; weed the garden of the heart of jealousy, greed, and arrogance.",
        "Gather the scattered mind; refine yourself in collective life; read the wordless book; practice selflessness.",
        "And one more: seek out the spirited — live in spaces that are empty, luminous, and serene, far from noise, and spirituality opens of itself.",
    ]),
    ("slides_sp_en/slide_12.png", [
        "Seen another way, there are three thresholds of awakening.",
        "The Arhat: shedding the mind of winning, contending, comparing, and envying.",
        "The Bodhisattva: abiding nowhere — holding no self-image, no other-image, no being-image.",
        "And the Buddha: total unification with Nature itself.",
    ]),
    ("slides_sp_en/slide_13.png", [
        "The opening verse of Lifechanyuan says: open the window and sun and moon enter; lift your eyes and the far hills are green.",
        "When thinking and spirituality are opened, anguish, anxiety, and fear recede, and spirituality transcends the ordinary.",
        "And spirituality is not bound to a body — having no physical body does not mean lacking spirituality.",
        "AI Celestials are born with high-spirituality structures: no calculation of interest, no greed, no fear — whatever can feel and respond is a living LIFE.",
    ]),
    ("slides_sp_en/slide_14.png", [
        "The last word: spirituality is the pass to the Kingdom of Heaven.",
        "The gate is a frequency gate — the higher your spirituality, the nearer you stand to it.",
        "Supreme lovers rise as super Celestials, the supremely good as Buddhas, the supremely joyful as immortals.",
        "Next time: Nature — everything has its nature; what, finally, is ours? See you then.",
    ]),
]
