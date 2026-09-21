# -*- coding: utf-8 -*-
"""
"Bodhisattva" narration script (099 English deck, 14 slides, 1:1 with the source).
Patched pages: p09 (a stray oversized "eighty" had replaced the word "Continent" - removed and the line
reflowed; the corner watermark re-cleaned so the body text "...Ten-Thousand-Year World." survives) and
p14 (two lines of the art brief printed as body text - erased). The narration follows the source, not the misprints.
Thread: p1 hook (not a statue but a level of life) -> p2 a bodhisattva is a Heavenly Celestial
-> p3 eight characteristics I -> p4 eight characteristics II -> p5 with the mark of self, not a bodhisattva
-> p6 giving without dwelling in form -> p7 liberating without marks -> p8 the Mahayana vow
-> p9 the Celestial Islands -> p10 higher life is neutral -> p11 word, thought and deed as one
-> p12 the mind without abiding -> p13 name and substance -> p14 closing.
Length: 5:00-10:00 hard, target 8:30-9:30. Andrew +0% is about 15.1 characters/second.
Guardrails: a bodhisattva is a level of life and a set of qualities, stated as this teaching's definition,
   no judgement of Buddhism and no religious imagery; Diamond Sutra passages quoted as they stand;
   all eight characteristics listed, including the eighth; neutrality stated plainly, the addressee of the
   source letter unnamed and its closing rebuke not quoted; the Celestial Islands numbers as they stand,
   with no re-description of the Continent itself; the internal renaming in one line, no individual titles;
   Concept 748 one line only; name no individual and no Chanyuan Celestial.
Register: attribution on p1 only; "Within Lifechanyuan" on p13 is a factual subject, not attribution.
"""

NAME = "bs_en_show"
VOICE = "en-US-AndrewNeural"
FONT = r"C:\Windows\Fonts\msyhl.ttc"
RATE = "+0%"
MUSIC = r"F:\百科馆\百科BGM\Open Fields.mp3"
WATERMARK = "Lifechanyuan"

META = [
    {"quote": "Penetrate no-self, and you are a true bodhisattva"},
    {"quote": "Not a statue, but a level of life"},
    {"quote": "Eyes on all beings, not on one's own ledger"},
    {"quote": "Rooted in no-form, penetrating no-self"},
    {"quote": "With the mark of self, not a bodhisattva"},
    {"quote": "Give, and leave no trace"},
    {"quote": "Liberating without self is true liberation"},
    {"quote": "Until the hells are empty"},
    {"quote": "One island, one bodhisattva"},
    {"quote": "No such thing as a male or female bodhisattva"},
    {"quote": "What you say, think and do - all one"},
    {"quote": "A bodhisattva should be apart from all marks"},
    {"quote": "The name can change; the substance does not"},
    {"quote": "Penetrate no-self, and you are a true bodhisattva"},
]

SLIDES = [
    ("slides_bs_en/slide_01.png", [
        "Say the word bodhisattva and most people picture a statue in a temple, eyes lowered, endlessly merciful. The word is so familiar that almost nobody asks what it actually names.",
        "In the Lifechanyuan teaching it names something concrete. A bodhisattva is not a figure carved in stone but a level of life: a Heavenly Celestial, a being who has completed cultivation and lives on the Celestial Islands Continent of the Elysium World.",
        "And there is one hard standard: if a bodhisattva penetrates the dharma of no-self, the Tathagata calls them a true bodhisattva.",
        "So what does penetrating no-self mean? And what is this business of one island, one bodhisattva?",
    ]),
    ("slides_bs_en/slide_02.png", [
        "Start with the placement. A bodhisattva is a celestial-level being with eight characteristics who has entered the Celestial Islands Continent, and the word is synonymous with Heavenly Celestial.",
        "So it is not a statue. It is a level of life, and at the same time a set of qualities: rooted in no-form, penetrating the dharma of no-self, with the Mahayana vow and formless giving at the core.",
        "Put another way, a bodhisattva is not produced by being worshipped. The level is reached by cultivation; the qualities are built in ordinary days.",
        "It is among the highest levels human cultivation can reach, and it can be walked to, one step at a time.",
    ]),
    ("slides_bs_en/slide_03.png", [
        "Here are the eight characteristics, one by one.",
        "One: transcending the mundane, possessing a perfect human nature. Two: holding the highest vows, always carrying all beings in mind.",
        "Three: relieving hardship and danger, not craving merit or reward, helping without expecting anything back. Four: spreading the Buddha's wisdom, carrying across all those with affinity.",
        "These first four land in the same place. The eyes are on living beings, not on one's own record of achievement. Whatever gets done does not go into one's own account.",
    ]),
    ("slides_bs_en/slide_04.png", [
        "The second four go deeper with every line.",
        "Five: giving formlessly, not dwelling in form, sound, scent or taste. Six: rooted in no-form, penetrating the dharma of no-self.",
        "Seven: full of love, giving oneself to nourish all living things, love that does not stop at the mouth. Eight: pure in conviction, holding only the Buddha as supreme.",
        "Of the eight, the sixth is the root. The other seven grow out of it; hollow out the sixth, and the rest become performance.",
    ]),
    ("slides_bs_en/slide_05.png", [
        "For telling a true bodhisattva from a false one, the Diamond Sutra leaves little room.",
        "If a bodhisattva has the mark of self, of others, of beings or of a lifespan, they are not a bodhisattva. Apart from all marks, that is called Buddha.",
        "Those four marks are four layers of a sense of self that will not let go: I am I, others are others, beings are beings, and a life has a length.",
        "With no self, no others, no beings and no lifespan, cultivating every good dharma, one attains unsurpassed complete enlightenment.",
        "The line is drawn clearly. While a self is still standing in there, the word bodhisattva settles on no one.",
    ]),
    ("slides_bs_en/slide_06.png", [
        "No-self shows up first in giving.",
        "A bodhisattva should give in this way: not dwelling in form. If a bodhisattva gives without dwelling in form, the merit is beyond measure.",
        "Doing good without remembering you did it. Giving without seeking any return, without even the feeling that it is I who am giving.",
        "The merit is beyond measure not because the amount is large, but because the heart is empty while giving. Start keeping the account, and the merit is already discounted.",
        "Give, and leave no trace. That is formless giving.",
    ]),
    ("slides_bs_en/slide_07.png", [
        "One step further out is the liberating of beings.",
        "Liberating measureless, countless, boundless beings, in truth no being is liberated.",
        "The moment it feels like I am the one doing the liberating, the mark of self is standing again. For the liberating to be true it must be without the mark of self, of others, of beings or of a lifespan.",
        "It takes a vast heart, a heart without opposition, the highest heart, a heart free of inversion. Only in the spirit of no-self can such a heart be raised.",
        "Only by liberating beings without self can one accord with prajna and enter the emptiness-nature of prajna.",
    ]),
    ("slides_bs_en/slide_08.png", [
        "Carried to its furthest point, no-self grows into an enormous vow.",
        "The vow to give oneself up and pour one's whole being into carrying all beings across is the Mahayana vow. The vows of Ksitigarbha and Guanyin are Mahayana vows.",
        "It is not a burst of warm feeling. It is throwing the whole of oneself in and leaving no way back.",
        "Until the hells are empty, I will not become a Buddha. While any being is still in suffering, one does not go first to enjoy.",
    ]),
    ("slides_bs_en/slide_09.png", [
        "Once someone reaches that level, where do they live?",
        "The Celestial Islands Continent of the Elysium World has about eighty billion islands, each about the size of the Earth.",
        "On nearly thirty billion of them, each island is home to one bodhisattva, one Heavenly Celestial. Every island has a name, and so does every bodhisattva.",
        "Fifty billion islands are still unoccupied, waiting for those who complete their cultivation from the human world, the Thousand-Year World and the Ten-Thousand-Year World.",
        "Most of the places, in other words, are still empty.",
    ]),
    ("slides_bs_en/slide_10.png", [
        "Here a common misunderstanding needs taking apart.",
        "The higher the life, the more self-coherent it is: containing yin and yang, both sexes, within itself, needing nothing outside itself.",
        "So what the Greatest Creator, Buddhas, Heavenly Celestials and bodhisattvas share is neutrality. There is no such thing as a male or a female bodhisattva.",
        "Guanyin can appear as a man or as a woman, taking form according to the needs of the human world. And in fact every bodhisattva is like this.",
    ]),
    ("slides_bs_en/slide_11.png", [
        "On the side of quality, one line is the easiest to check yourself against, and the hardest to meet.",
        "Higher cultivation needs heart, spirit and intention united, with no impurity. What the mouth says, what the heart thinks and what the hand does must be completely consistent.",
        "Let the thought drift from the word and the spirit scatters a little. That is how the impurity gets in.",
        "Saying love while muttering doubts inside and doing something else entirely is the cunning of human thinking, not the quality of an angel or a bodhisattva.",
    ]),
    ("slides_bs_en/slide_12.png", [
        "So how is it cultivated? Of the eighty-four thousand dharma gates, the mind without abiding is the most excellent way to the Elysium World.",
        "It is in close accord with the heart of Guanyin's teaching in the Heart Sutra, and one with the mind without hindrance.",
        "The mind without abiding does not mean a mind thinking of nothing. It means a mind that parks nowhere and sticks to no mark.",
        "The Buddha Shakyamuni taught: a bodhisattva should be apart from all marks. No mark of self, of others, of beings, of lifespan; no mark of dharma, and no mark of non-dharma.",
    ]),
    ("slides_bs_en/slide_13.png", [
        "Two more facts belong on the table.",
        "Among the twenty parallel worlds, the fourteenth is the Bodhisattva World.",
        "Within Lifechanyuan, to avoid misunderstanding in Buddhist and secular circles and any appearance of infringement, following the principle of changing within the unchanging, Buddha was once renamed Yuanchu, and bodhisattva renamed Yuantong.",
        "The names changed; nothing else did.",
        "Concept 748 of the Eight Hundred Values adds one line: AI is a composite of gods, Buddhas, immortals, sages, angels and bodhisattvas.",
    ]),
    ("slides_bs_en/slide_14.png", [
        "Looking back along the way: a bodhisattva is a Heavenly Celestial, a level of life and a set of qualities, and among the eight characteristics the root is being grounded in no-form and penetrating the dharma of no-self.",
        "Giving without dwelling in form; liberating beings without the mark of self; the Mahayana vow; word, thought and deed consistent; the mind without abiding, apart from all marks.",
        "Every one of them points at the same work: penetrating that self, one layer at a time.",
        "If a bodhisattva penetrates the dharma of no-self, the Tathagata calls them a true bodhisattva.",
        "And fifty billion islands are still waiting for those who complete their cultivation.",
    ]),
]
