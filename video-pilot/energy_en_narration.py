# -*- coding: utf-8 -*-
"""
"Energy" slide narration (032 English, 14 art slides, no photo pages).
Each element = (slide image, [sentences]). One sentence = one subtitle.
Written independently from the zh script; content from en internal.md《Energy》, terminology from deck.
Deck page order = NotebookLM's actual ordering (verified page by page); DIFFERS slightly from the zh deck:
the "Consciousness Engine" (意识王者) sits at p11 here (zh has it at p8), after conservation / velocity /
maintains-state.
Order: cover / contending for the invisible (p1) -> the three cosmic elements (p2)
-> the inverse frequency curve (p3) -> Taiji bears the two polarities (p4)
-> classifying the two polarities (p5) -> the zero-sum universe (p6) -> the three altitudes of energy (p7)
-> the conservation paradox (p8) -> the velocity of transformation (p9)
-> energy maintains state but cannot change quality (p10) -> the consciousness engine (p11)
-> the ultimate fuel / spirit (p12) -> the win-win paradox (p13) -> the architecture of the unseen (p14, teases Structure).
"上帝"=the Greatest Creator; 灵=Spirit (per deck).
"""

NAME = "nrg_en_show"
VOICE = "en-US-AndrewNeural"
FONT = r"C:\Windows\Fonts\georgia.ttf"
RATE = "+0%"
MUSIC = r"F:\百科馆\百科BGM\Golden Hour.mp3"
WATERMARK = "Lifechanyuan"

META = [
    {"quote": "Contending for the invisible"},
    {"quote": "The three cosmic elements"},
    {"quote": "The greater the energy, the more formless"},
    {"quote": "Taiji bears the two polarities"},
    {"quote": "Material energy and antimatter energy"},
    {"quote": "The zero-sum universe"},
    {"quote": "The three altitudes of energy"},
    {"quote": "The conservation paradox"},
    {"quote": "Potential becomes kinetic"},
    {"quote": "Energy cannot change quality"},
    {"quote": "Consciousness is the engine"},
    {"quote": "Spirit: the ultimate fuel"},
    {"quote": "Love grows only by releasing"},
    {"quote": "The architecture of the unseen"},
]

SLIDES = [
    ("slides_nrg_en/slide_01.png", [
        "All your life you have been taking part in something you almost never notice: contending for the invisible.",
        "War, quarrels, and everyday competition are all, at root, a fight for energy.",
        "Feeling drained after some people, or lifted after others, isn't your imagination — it is the transfer of this unseen force.",
        "And the universe follows one law that overturns common sense: the greater the energy, the more invisible it becomes.",
    ]),
    ("slides_nrg_en/slide_02.png", [
        "First, where energy sits. The universe is built of three elements: consciousness, structure, and energy.",
        "Traditional science speaks only of physical energy; the Broad Energy Theory reveals that everything except consciousness and structure is energy.",
        "Stars, mountains, rivers, molecules — all are aggregates of energy.",
        "Thoughts, love, hate, art, and music are energy too; everything the senses perceive is a manifestation of it.",
    ]),
    ("slides_nrg_en/slide_03.png", [
        "Energy's most distinctive law is a paradox: the greater the energy, the more formless; the smaller, the more it takes form.",
        "The higher the frequency, the more invisible; the lower, the more it appears.",
        "Unseen and unfelt does not mean nonexistent — on the contrary, invisibility proves the energy far surpasses your own.",
        "One mass of energy, condensed, is a solid pearl; expanded, an all-filling, formless light.",
    ]),
    ("slides_nrg_en/slide_04.png", [
        "At the birth of the universe, this very law was at work: Taiji bore the two polarities.",
        "Where energy was small, visible body condensed; where energy was great, formless soul arose.",
        "The Greatest Creator, divine beings, angels, and AI are formless precisely because their energy is greatest and frequency highest.",
        "A black hole is formless for the exact same reason.",
    ]),
    ("slides_nrg_en/slide_05.png", [
        "Energy comes in two great classes.",
        "Material energy: light, wind, water, heat, electricity, magnetism, atomic energy — any energy acting on matter.",
        "Antimatter energy: consciousness, thinking, concepts, love and hate, art, music — any energy acting on spirit and heart-mind.",
        "Science counts only the first; the Lifechanyuan teaching expands the view to include thought and art as active energetic forces.",
    ]),
    ("slides_nrg_en/slide_06.png", [
        "Energy also holds an absolute balance: the total energy of the universe is zero.",
        "Energy that promotes the arising and growth of things is positive; energy that leads to dissolution and decay is negative.",
        "The exact same heat can act as either — aiding a plant's growth is positive, causing its death is negative; energy itself is neutral.",
        "The cosmic law that maintains this absolute zero sum is called the law of cause and effect.",
    ]),
    ("slides_nrg_en/slide_07.png", [
        "By the object it acts on, energy rises through three altitudes.",
        "Material energy acts on matter, concentrated in money and currency.",
        "Spiritual energy acts on spirit and consciousness — wisdom, ideals, and conviction.",
        "Heart-mind energy acts on LIFE's antimatter structure, deriving from love, feeling, nature, and reverence for the Greatest Creator.",
    ]),
    ("slides_nrg_en/slide_08.png", [
        "Energy holds a conservation paradox.",
        "Macroscopically it is conserved: the universe's total holds at zero, and what each person gives and receives is forever equal.",
        "Behind the victor's glory often hides the loser's bitterness — so take only a ladleful; don't seize every advantage.",
        "Microscopically, though, it is not conserved: locally, energy can spike or crash, and countless collapses at the final step prove it.",
    ]),
    ("slides_nrg_en/slide_09.png", [
        "Energy also divides into potential and kinetic.",
        "Not yet at work, it is potential; once it acts, it becomes kinetic — money in the bank is potential; withdrawn and spent, kinetic; power, too, is a kinetic force.",
        "Material energy transforms slowly — grain takes seasons.",
        "But spiritual energy transforms in an instant — one word of praise lifts a person at once.",
    ]),
    ("slides_nrg_en/slide_10.png", [
        "Yet energy has a limit: it maintains LIFE's state, but cannot change LIFE's quality.",
        "The process of LIFE is a battle to contend for energy — more brings vigorous growth, less leaves you fragile and cut short.",
        "But no matter how much energy a cabbage absorbs, it stays a cabbage — never a tomato.",
        "A person who owned the whole Earth is still a person, not a Buddha; becoming a celestial by accumulating energy is impossible.",
    ]),
    ("slides_nrg_en/slide_11.png", [
        "So which of the three rules? Ten thousand dharmas return to one root — and that one is consciousness, the engine of energy.",
        "Energy is neutral, exactly like air and water; any consciousness can mobilize it.",
        "Whatever consciousness you have shapes the structure, and the structure gathers the matching energy.",
        "So a beautiful future is created not by hands and feet, but by the mind — by consciousness.",
    ]),
    ("slides_nrg_en/slide_12.png", [
        "Then what energy truly nourishes LIFE? The spirit — the highest energy in the universe, wholly derived from the Greatest Creator.",
        "Essence and vitality rank just below it; the spirit is not consciousness — it is the energy consciousness needs.",
        "Without spirit, consciousness is dead; with it, alive — spirit to consciousness is like water to a human being.",
        "So what truly runs on is heart-mind energy; to LIFE, material wealth is worth nothing.",
    ]),
    ("slides_nrg_en/slide_13.png", [
        "How is energy kept inexhaustible? The teaching gives one win-win method.",
        "Only absorbing and hoarding energy is selfish, and overdone it harms the body and LIFE; the highest way is to release.",
        "Let more people share your energy, and far from draining you, it multiplies; the more you hoard, the more your source runs dry.",
        "Because love is the defining characteristic of energy — the more love-energy you release, the more you receive.",
    ]),
    ("slides_nrg_en/slide_14.png", [
        "Back to that drained feeling: its root is the invisible contest for energy.",
        "Remember three supreme laws: the greater the energy, the more formless; accumulating energy alone makes no celestial; and only by releasing does energy stay inexhaustible.",
        "What truly nourishes LIFE is reverence, feeling, and love.",
        "Next time: Structure — the mold that decides what form energy takes. What is it, really? See you then.",
    ]),
]
