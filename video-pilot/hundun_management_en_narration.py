# -*- coding: utf-8 -*-
"""
"Hundun Management" narration script (106 English deck, 14 slides, 1:1 with the source).
Patched pages: p04, p10 and p13 (upside-down mirrored fragments of the body text along the bottom edge, painted out);
p05 (a whole [image] direction leaked onto the slide, with garbled words - replaced with the flower band beside it).
The narration follows the source and the entry text.
Thread: p1 hook (no leaders, yet nothing falls apart) -> p2 Hundun is not Chaos -> p3 the cosmic prototype
-> p4-p6 the eight dimensions -> p7 what it looks like in practice -> p8 each to their own path -> p9 how it runs
(ideas and program) -> p10 the precondition (purification of the heart) -> p11 governance by the Tao
-> p12 the two extremes -> p13 proven in practice -> p14 humanity's way out.
Length: 5:00-10:00 hard, target 8:30-9:30. Andrew +0% is about 15.1 characters/second.
First draft came out 10:44, so the parallel lists were cut back page by page (SOP: trim the English lists first).
Guardrails: stated as the Lifechanyuan teaching's position and practice; no reference to and no comment on any real
   country, government, political party, legal system, institution or person. The two Chinese characters spelled out,
   since the distinction is inaudible in English. All eight dimensions kept, one line each; the third one's marriage,
   family, parties, religions and nations named in a single line as the Second Home's way of living and this teaching's
   picture for humanity, not expanded. "Hardly any punishment" as in the original, never "no punishment". Purification
   of the heart as stated, with the original's judgements of particular people left out - the principle only. The
   comparison with rule of law and rule by persons as this teaching's view. The practice record as the Chanyuan
   Corpus's account; the name of the one at the Thailand Home's information hub not given. The closing line as written.
   The Thousand-Year World line as Xuefeng's own account. No names apart from Guide Xuefeng; every "and so on" list
   flagged as a few examples only.
Separation: 002's core, grouped dimensions and crucible, 004's Thailand Home, 001's "neither rule of law nor rule by
   persons, but rule by the Tao" - kept but re-angled, one page each; 105 (no video), 107, 108, 110, 186, 289 named
   only; 042 and 072 already have videos, one clause each.
Register: attribution on p3 (in the Lifechanyuan teaching) and p14 (Xuefeng says); p11's opening, p12's closing and
   p13's "the Chanyuan Corpus records" are stance clauses.
"""

NAME = "hdgl_en_show"
VOICE = "en-US-AndrewNeural"
FONT = r"C:\Windows\Fonts\msyhl.ttc"
RATE = "+0%"
MUSIC = r"F:\百科馆\百科BGM\Lotus Bloom.mp3"
WATERMARK = "Lifechanyuan"

META = [
    {"quote": "The highest management is no management"},
    {"quote": "Whole and undivided, not confused"},
    {"quote": "Never managed, yet everything in order"},
    {"quote": "One with the Tao, everything left natural"},
    {"quote": "Service in place of management"},
    {"quote": "No one should suffer through life for a goal"},
    {"quote": "No leaders, yet everything in order"},
    {"quote": "Fine rain, not a storm"},
    {"quote": "Living by ideas, running by program"},
    {"quote": "The more perfect the heart, the less management"},
    {"quote": "Not law, not persons, but the Tao"},
    {"quote": "The less managed, the happier and more creative"},
    {"quote": "No orders given, yet a paradise grew"},
    {"quote": "Humanity's way out"},
]

SLIDES = [
    ("slides_hdgl_en/slide_01.png", [
        "Imagine a community living together with no leaders, no rules, no supervision, and no rewards or punishments. How badly would you expect that to fall apart?",
        "It does not. Everything stays in order. This is Hundun Management, the core approach of Lifechanyuan's Second Home, proposed and created by Guide Xuefeng.",
        "Its essence is non-management: strip human intervention to the minimum and let the Tao manage instead, following natural law rather than human will.",
        "In one sentence: service replaces management. The master is the servant, and managing is serving.",
    ]),
    ("slides_hdgl_en/slide_02.png", [
        "First, a word that is easy to mishear. In Chinese, the everyday word for chaos is also pronounced hundun. The two are written with a different first character, and they mean opposite things.",
        "In chaos, hun means muddled, mixed up. Chaos is a disordered state, the state before the universe formed: no heaven, no earth, no edges, no centre, no yin, no yang, no middle way.",
        "In Hundun Management, hun means whole and undivided, and dun means a boundless ocean. Hundun is an ordered state, the state after the universe formed. It has the Taiji, the unified one of opposites, and it has a middle way.",
        "So Hundun Management is orderly. It is the highest form of management, never chaotic disorder. The character of the Tao is exactly this: broad, whole, non-linear understanding.",
    ]),
    ("slides_hdgl_en/slide_03.png", [
        "This approach has a cosmic prototype. In the Lifechanyuan teaching, the way the Greatest Creator runs the universe is Hundun Management.",
        "Nature is in perfect order because every kind of being was given its own nature, and all things simply run by what they were given.",
        "It has never been managed by human hands, yet birds sing, flowers bloom, and wind and rain arrive in their season.",
        "And the universe is holographic: touch one hair and the whole body moves. There are no isolated events; everything is public business. That is why, for all humanity to live happily, Hundun Management has to be global.",
    ]),
    ("slides_hdgl_en/slide_04.png", [
        "Hundun Management has eight dimensions.",
        "One: unity of heaven and humanity, in harmony with the Tao. Follow natural law, and reduce human interference to the minimum.",
        "Two: keep laws, regulations and precepts to a minimum. Awaken the truth, goodness, beauty and love inside people, and let everything be natural.",
        "Three: remove the soil that grows private ownership. One family across the globe, resources shared. In the Second Home that means living without marriage and family; and in this teaching's picture for humanity, without the divisions of parties, religions and nations.",
        "Four: make every member a creator of wealth, of the heart, of the mind or of material things, with as few administrators as possible.",
    ]),
    ("slides_hdgl_en/slide_05.png", [
        "Five: replace management with service. Everyone who manages becomes a servant of all, with no special treatment of any kind.",
        "Six: from each according to ability, to each according to need. No extravagance, no waste, everything done willingly, no administrative orders, and no one may impose their will on another.",
        "Seven: individuality and commonality in harmony. One body at large, distinct individuals up close.",
    ]),
    ("slides_hdgl_en/slide_06.png", [
        "Eight: everything unfolds around people, not around a goal, an ideology, an economic interest or a lofty ideal.",
        "Let people enjoy the journey: children the delights of childhood, the young the interests of youth, the middle-aged the wonders of midlife, and the old the leisure of age.",
        "In a line: no one should suffer through life for the sake of a goal.",
        "Put the eight together and they point one way: take people out of the position of the managed, and let them grow on their own.",
    ]),
    ("slides_hdgl_en/slide_07.png", [
        "So what does it actually look like in the Second Home?",
        "No rules and regulations, no precepts, no leadership bodies or offices, no organization, no discipline, no supervision, no rewards, and hardly any punishment. And yet everything is orderly and harmonious.",
        "Everyone is a master and everyone is a servant. There is only a division of work: no leader and led, no ranks, everyone equal.",
        "Whoever is responsible decides, and bears every consequence. Each person builds a sacred court inside their own conscience.",
    ]),
    ("slides_hdgl_en/slide_08.png", [
        "Day to day it comes down to five lines: each speaks their own words, does their own work, carries their own responsibility, cultivates their own path, and walks their own road.",
        "Do not fret over others, do not run their affairs. If no one asks, I do not step in; if someone asks, I help at once. Whoever proposes it, takes responsibility for it.",
        "Hundun Management works through friendliness, not intimidation; through laughing and joking rather than solemn faces; through ease and freedom rather than strain.",
        "It is fine rain soaking in without a sound, not a violent storm.",
    ]),
    ("slides_hdgl_en/slide_09.png", [
        "So what actually keeps it running? The secret is in the ideas and the program, not in human management.",
        "The Second Home runs by Lifechanyuan concepts and by the Home's program, not by anyone's management. It needs no managing class sitting above everyone else.",
        "Every member follows the 800 Values for New Era Human Beings, and daily life runs by a settled program. The ideas are not moved, and the program is not disturbed.",
        "Put simply, nothing is managed. Put in full, it is the highest form of management. One thing is certain: it is service. Enthusiasm roused by love, hearts moved by sincerity, everything looking entirely natural, without a single track of force left behind.",
    ]),
    ("slides_hdgl_en/slide_10.png", [
        "But there is one precondition that cannot be walked around: people must first go through purification of the heart.",
        "Without it, Hundun Management cannot be implemented. Purifying the heart is hard, intricate work, and where it is not done, Hundun Management is only a mirage.",
        "Heaven practises Hundun Management because the hearts of those living there are pure. Human society requires so much management because people have not been through that purification.",
        "The more perfect a person's heart, the less they need managing. The Second Home's program is itself a crucible, dissolving self-attachment, selfishness, greed and jealousy - to name only a few.",
    ]),
    ("slides_hdgl_en/slide_11.png", [
        "Seen this way, Hundun Management is governance by the Tao. In this teaching's view, that sets it apart from the rule of law and rule by persons.",
        "Rule of law is too cold: the more numerous and detailed the laws, the more problems appear, and the harder human nature is pressed down.",
        "Rule by persons is too complicated: human hearts shift, and it cannot solve anything at the root.",
        "Governance by the Tao follows the way of the Greatest Creator. At its core is harmony between people, between people and society, and between people and the natural world. The sage handles affairs without forcing, and teaches without words.",
    ]),
    ("slides_hdgl_en/slide_12.png", [
        "So the less a place is managed, the closer it is to heaven; the more tightly it is managed, the closer it is to hell.",
        "The highest management is no management. The lowest is managing everything.",
        "The less you manage, the clearer and simpler things get, and the happier and more creative people become. The more you manage, the murkier things get, and the gloomier people become.",
        "This is the Lifechanyuan teaching's judgement about management itself. It points at no real place, institution or system.",
    ]),
    ("slides_hdgl_en/slide_13.png", [
        "None of this stayed on paper. The Second Home has been the proving ground of Hundun Management, over years of living and across several homes.",
        "The Chanyuan Corpus records that in those years there were no quarrels, no fights and no brawls; nothing taken that was not one's own, and no door that needed locking at night.",
        "The Thailand Home is the cleaner example. Guide Xuefeng never visited it, never asked about its affairs, and never issued a single instruction. Everything there was done by Chanyuan Celestials following what their own hearts moved them to do.",
        "The place grew more and more like a paradise, drawing over a hundred visitors from dozens of countries. From this, the existence of the Thousand-Year World can be reasoned out.",
    ]),
    ("slides_hdgl_en/slide_14.png", [
        "Xuefeng says the Thousand-Year World he once lived in was exactly this kind of place: no one managing, still less a managing class, everything in order, everyone living happily, freely and abundantly.",
        "The Second Home exists to test this model. If it works there, it can be spread to the whole world, until Hundun Management is practised globally.",
        "Humanity's way out lies in Hundun Management. Apart from it, humanity has no way out.",
        "As long as the whole of society gives understanding, support and patience, humanity's most beautiful ideal can be realized.",
    ]),
]
