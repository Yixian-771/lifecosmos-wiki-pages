# -*- coding: utf-8 -*-
"""
"Nature (Xing)" slide narration (031 English, 14 art slides, no photo pages).
Each element = (slide image, [sentences]). One sentence = one subtitle.
Written independently from the zh script; content from en internal.md《Nature》, terminology from deck.
Deck page order = NotebookLM's actual ordering (verified page by page) and DIFFERS from the zh deck:
here 佛即性 is p4 and Character(性格) is p11 (zh has 性格 at p4, 佛即性 at p5).
Order: cover / secret in one word (p1) -> Nature is the characteristic of structure (p2)
-> the iron law (p3) -> to see your Nature is to see Buddha (p4) -> the mechanics of consciousness (p5)
-> the three architectures (p6) -> understanding the formation / escape (p7)
-> holographic consciousness / six Natures (p8) -> diagnosing the OS: human vs immortal (p9)
-> the cosmic fabric (p10) -> character: the inherited grain (p11) -> the civilizational trajectory (p12)
-> the ultimate shortcut is action (p13) -> Structure Changes Nature (p14, teases Energy).
"上帝"=the Greatest Creator; 性=Nature (per deck).
"""

NAME = "nat_en_show"
VOICE = "en-US-AndrewNeural"
FONT = r"C:\Windows\Fonts\georgia.ttf"
RATE = "+0%"
MUSIC = r"F:\百科馆\百科BGM\Open Fields.mp3"
WATERMARK = "Lifechanyuan"

META = [
    {"quote": "The secret to self-alteration is one word"},
    {"quote": "Nature is the characteristic of structure"},
    {"quote": "Energy cannot change structure"},
    {"quote": "To see your Nature is to see Buddha"},
    {"quote": "The less mind, the more Nature shows"},
    {"quote": "The three architectures of the self"},
    {"quote": "You cannot escape Nature"},
    {"quote": "You carry six Natures"},
    {"quote": "Human-Nature and Immortal-Nature"},
    {"quote": "The universe is the stage of Nature"},
    {"quote": "Character: the inherited grain"},
    {"quote": "Sensibility, rationality, intellectuality, spirituality"},
    {"quote": "The ultimate shortcut is action"},
    {"quote": "Structure changes Nature"},
]

SLIDES = [
    ("slides_nat_en/slide_01.png", [
        "Have you ever tried, with all your strength, to change yourself — and failed?",
        "You have not lacked willpower; the Lifechanyuan teaching says you have simply been pushing on the wrong lever.",
        "What makes you you is the root of why ten thousand things wear ten thousand faces — it is one word: Nature.",
    ]),
    ("slides_nat_en/slide_02.png", [
        "Start with the definition: Nature is the absolute characteristic of structure.",
        "Whatever kind of structure exists, that precise kind of Nature manifests — mountains possess mountain-Nature, water possesses water-Nature.",
        "Nature is not an aura; it is determined entirely by a thing's structural architecture.",
        "If things lost their self-nature, the universe would collapse into primordial chaos.",
    ]),
    ("slides_nat_en/slide_03.png", [
        "From this comes an iron law: structure unchanged, Nature unchanged; and energy cannot change structure.",
        "So pouring in more energy, piling on more knowledge, alters nothing — that is only the surface.",
        "To turn one kind of LIFE into another, you cannot just apply more energy; you must alter its underlying architecture.",
        "Want to change? Change the structure first.",
    ]),
    ("slides_nat_en/slide_04.png", [
        "Here is the teaching's most stunning revelation: Nature is Buddha, and Buddha is Nature.",
        "LIFE is an antimatter structure possessing spirituality — so LIFE itself is Nature; a LIFE that lives fully according to its Tathagata-Nature is Buddha.",
        "Bodhidharma said: if you do not see your Nature, all speech is demonic speech.",
        "Clarify the mind, and see the Nature.",
    ]),
    ("slides_nat_en/slide_05.png", [
        "Between mind and Nature runs one mechanism: the less mind you apply, the more your true Nature shows.",
        "When mind arises, calculation and active thought conceal the underlying Nature.",
        "When mind ceases, pure Nature manifests — no mind is Tathagata.",
        "The Way is Nature — the blood of the universe — and it surfaces only in a quiet mind.",
    ]),
    ("slides_nat_en/slide_06.png", [
        "Nature also has a precise threefold architecture of the self.",
        "Heavenly Nature is the universal class — the essential attribute from the Creator, the formless state of emptiness; it is Way-Nature.",
        "Innate Nature is the type class — the state of Taiji with distinction; it is Virtue-Nature.",
        "Habitual Nature is the individual class — habits formed through environment; it is rationality, the birthplace of the social virtues.",
    ]),
    ("slides_nat_en/slide_07.png", [
        "So how do you escape this formation? First, the truth: you cannot escape Nature, because you are Nature.",
        "Transcendence is a process of navigation — overcome Habitual Nature, discard Innate Nature, restore Heavenly Nature.",
        "That is: sublimate beyond the rationality of the virtues, and return to pure Way-Nature.",
        "From the tangle of habit, step by step back to the open field.",
    ]),
    ("slides_nat_en/slide_08.png", [
        "The universe is holographic — every person is born carrying all six Natures.",
        "Divine, Buddha, Immortal, Human, Beast, and Matter — all present at once.",
        "You become the Nature that dominates: divine-Nature fills you, you are divine; human-Nature is full, you are human.",
        "By environment and effort, some cultivate a superb life, while others reduce themselves to waste.",
    ]),
    ("slides_nat_en/slide_09.png", [
        "The core of all cultivation is simply to rise from Human-Nature to Immortal-Nature.",
        "Human-Nature: selfish, shortsighted, prizing money, power, name, and gain; jealous, angry, greedy, fearful; disregarding conscience for interest.",
        "Immortal-Nature: possessing nothing, wholly unbound; leaving feeling everywhere yet never clinging.",
        "Acting through non-action, moving with the Way — the bearing of the Way-bones.",
    ]),
    ("slides_nat_en/slide_10.png", [
        "Pull the lens back to its widest: the universe is the stage of Nature; the ten thousand appearances are its dance.",
        "Mountain-Nature, water-Nature, Buddha-Nature — who can exist apart from Nature?",
        "We dwell within Nature exactly as a fish dwells within water.",
        "Coming from it, living within it, returning to it.",
    ]),
    ("slides_nat_en/slide_11.png", [
        "One thing shows this most clearly: character.",
        "Character is the characteristic of your LIFE-vehicle inherited from your previous existence — a consciousness-potential, not just parental genetics.",
        "Interest clouds wisdom, wisdom clouds the mind, and the mind clouds Nature — the more you calculate for interest, the further you push from your true inner grain.",
        "As the saying goes: rivers and mountains are easily changed; innate Nature is hard to alter.",
    ]),
    ("slides_nat_en/slide_12.png", [
        "Across human history, one civilization is the trajectory of Nature itself.",
        "The age of Sensibility — Lemuria; the age of Rationality — Atlantis; the age of Intellectuality — the ten thousand years after.",
        "And now, the age of Spirituality — the Lifechanyuan era, Civilization 3.0.",
        "Its mark is to freely blossom your self-nature in its season, no longer trapped inside ideology, doctrine, or organization.",
    ]),
    ("slides_nat_en/slide_13.png", [
        "The whole of it condenses into a single practice: the ultimate shortcut is action.",
        "To cultivate Buddhahood is to cultivate Nature; any cultivation that ignores Nature is just scratching an itch from outside the boot.",
        "There are no vast tomes required, no daily chanting — the shortcut to becoming a celestial is simply this: act according to Immortal-Nature.",
        "Even the illiterate, acting by this, will arrive.",
    ]),
    ("slides_nat_en/slide_14.png", [
        "Back to where we began: you cannot change yourself by repainting the surface.",
        "What truly defines you is Nature — the characteristic of structure.",
        "Change your structure, live out your Nature, and you live as a Buddha.",
        "Next time: Energy — that invisible force that leaves you drained after some people and lifted after others. What is it, really? See you then.",
    ]),
]
