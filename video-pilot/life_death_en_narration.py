# -*- coding: utf-8 -*-
"""
"Life and Death" narration (052 English deck, 14 slides).
NotebookLM kept the source order intact, so the deck runs parallel to the Chinese one:
p1 hook -> p2-p6 nature (appearance not substance / boat and passenger / mutually rooted /
the gate / the great womb) -> p7-p9 the present state (three definitions / the Life-and-Death
Formation / the struggle of ignorance) -> p10-p14 the way out.
p14 carries a baked "Next up: Karma, Retribution, and Reincarnation" strap - 053 really is
next, so the closing line says so.
Voice: Andrew, warm and conversational. From the English internal.md; independent.
Sentence 1 = a personal, counter-intuitive hook.
Target run time 6-7 minutes.
"""

NAME = "life_death_en_show"
VOICE = "en-US-AndrewNeural"
FONT = r"C:\Windows\Fonts\georgia.ttf"
RATE = "+0%"
MUSIC = r"F:\百科馆\百科BGM\Quiet Study.mp3"
WATERMARK = "Lifechanyuan"

META = [
    {"quote": "What if dying is just stepping off a boat"},
    {"quote": "Appearance, not substance"},
    {"quote": "The body is the boat; LIFE is the passenger"},
    {"quote": "The living are the root of the dead"},
    {"quote": "One door, two names"},
    {"quote": "Human society is a great womb"},
    {"quote": "Upward, level, or downward"},
    {"quote": "Memories erased, the game replays"},
    {"quote": "The tragedy is not knowing"},
    {"quote": "Nobody judges you; structure decides"},
    {"quote": "Fourteen trajectories, each earned"},
    {"quote": "Five traits stand in the way"},
    {"quote": "Three things that must be done"},
    {"quote": "The boat has reached the shore"},
]

SLIDES = [
    ("slides_lifedeath_en/slide_01.png", [
        "Almost every fear a human being carries, if you follow it far enough down, arrives at the same place.",
        "And the Lifechanyuan teaching makes a claim that sounds impossible on first hearing. LIFE has no death in it at all.",
        "So today we take that claim seriously, and look at how living and dying actually work.",
    ]),
    ("slides_lifedeath_en/slide_02.png", [
        "The starting position is blunt. What we call life and death is a fundamental illusion.",
        "We mistake the survival and demise of LIFE's carrier for the survival and demise of LIFE itself.",
        "The grass on the plain withers and flourishes year by year. Wildfire cannot burn it away, for spring winds bring it back. What burns is the grass, not whatever keeps returning as grass.",
    ]),
    ("slides_lifedeath_en/slide_03.png", [
        "So what is LIFE itself? A person consists of two parts: a material body, and a spirit-body.",
        "Xuefeng's image for this is simple enough to keep. The physical body is a boat. LIFE is the person riding in it.",
        "When the body dies, the boat has reached the bank. The passenger unties the rope, disembarks, and begins a new leg of the journey.",
    ]),
    ("slides_lifedeath_en/slide_04.png", [
        "Go one layer deeper and life and death stop being opposite ends of a line.",
        "They are one of the eight great dialectics of the universe - mutually rooted. Where there is life there must be death, and where there is death there must be life.",
        "Xuefeng reaches for the Mobius strip. Within life there is death; within death there is life. Follow the surface far enough and you are on the other side without ever crossing an edge.",
        "The Huangdi Yinfu Jing said it far earlier and far harder. The living are the root of the dead; the dead are the root of the living.",
    ]),
    ("slides_lifedeath_en/slide_05.png", [
        "If that is true, why do we only ever see the dying half? Because we only ever stand on one side.",
        "LIFE cycles endlessly through transformation. To move from one dimension into another, it passes through a gate.",
        "From this realm's perspective, it has died. From that realm's perspective, it has just been born.",
    ]),
    ("slides_lifedeath_en/slide_06.png", [
        "There is an analogy that makes the whole thing click. Human society is a great womb.",
        "The ultimate goal of a fetus is not to remain inside the womb. It is to arrive in the world. And the ultimate goal of a human life is not to stop here either.",
        "A person must pass through what looks like the channel of death in order to reach that wider world.",
        "So death is not an ending. It is the beginning of the next leg of the journey.",
    ]),
    ("slides_lifedeath_en/slide_07.png", [
        "Xuefeng then redefines the words themselves, and the definitions are unusually precise.",
        "Birth means evolving upward - moving toward the Thousand-Year World, the Ten-Thousand-Year World, the Elysium World, the Celestial Islands. That is what it means to actually be born.",
        "Half-alive means horizontal. Reincarnating back into the human world with the memory wiped. Half of that LIFE is dead, half is alive.",
        "And death means transforming downward - sinking toward the animal and plant layers, the netherworld, the frozen layer, the fire-refining layer.",
        "Which of the three you get is not assigned to you. It is chosen.",
    ]),
    ("slides_lifedeath_en/slide_08.png", [
        "That horizontal loop has a name inside the system. It is one of the thirty-six universal formations - the Life-and-Death Formation.",
        "Former memories are erased. A new self is issued in a specific region of time and space.",
        "The plot unfolds again, hope is renewed, everything flourishes, and the game never ceases to play.",
    ]),
    ("slides_lifedeath_en/slide_09.png", [
        "Which is why Xuefeng locates the tragedy of human life precisely in ignorance - not in suffering, and not in dying.",
        "As long as a person is unclear about what happens after death, their entire life - whether noble or humble - is merely a struggle on the verge of dying.",
        "That is a hard sentence, but the logic holds. If this problem is unresolved, every other problem is illusory.",
        "Death can arrive at any moment, and once it does, regret is always too late. There is nothing left to fix it with.",
    ]),
    ("slides_lifedeath_en/slide_10.png", [
        "So who decides where you go? This is the part that usually surprises people. No verdict is handed down by anyone.",
        "Where you go is determined entirely by the quality of your LIFE's structure.",
        "The more perfect and symmetrical the structure, the higher the quality - and the better the space of existence you can reach, and the greater the freedom in it.",
    ]),
    ("slides_lifedeath_en/slide_11.png", [
        "And the matching is itemised. The teaching lists fourteen trajectories, laid out like a scale.",
        "Upward: supreme love becomes celestial immortals, supreme goodness becomes buddhas, supreme joy becomes divine immortals, supreme health terrestrial immortals, supreme compassion human immortals.",
        "Then perfect loyalty to the noble way, filial piety to the fortunate way, fairness returning to the human way, accumulated virtue to the prosperous way - and unfulfilled wishes bringing a person back to reincarnate here.",
        "Downward: the muddled toward the animal layer, the indifferent toward plants, the malicious to the ghost way, the domineering to the frozen layer, the cruel to the fire-refining layer.",
        "Look closely and none of these are single acts. Every one of them is a disposition, built up over a lifetime.",
    ]),
    ("slides_lifedeath_en/slide_12.png", [
        "If the destination is self-determined, what actually blocks the way? Xuefeng identifies five traits.",
        "Greed - selfishness and the wish to possess. Hatred - anger, resentment, grievance, jealousy.",
        "Delusion - the blind conviction that you are always right. Arrogance - haughtiness and self-conceit.",
        "And doubt - excessive suspicion, refusing facts, hypocrisy toward yourself.",
        "Overcome those five and everything said so far stops being an interesting idea and starts being something you can actually see.",
    ]),
    ("slides_lifedeath_en/slide_13.png", [
        "In practice it comes down to three things that must be done.",
        "One: repay debts and resolve worldly bonds. Two: give and contribute; accumulate merit and virtue. Three: perfect and beautify the antimatter structure of your own LIFE.",
        "And there is a line that refuses to soften any of it. Without killing off the human heart, you cannot attain the nature of an immortal.",
        "Without dying to the human world, you cannot enter the immortal realm. The dying being asked for here was never the body. It is the part of you still committed to the rules of this world.",
    ]),
    ("slides_lifedeath_en/slide_14.png", [
        "Which leaves the practice itself, and it is a daily one. Die to yesterday's self and embrace today's. Die to today's self and embrace tomorrow's.",
        "LIFE's best destination is to enter the Greatest Creator's back garden - to live in the Celestial Islands Continent.",
        "Repay all debts, accumulate sufficient merit, bring the quality of your LIFE up, and death stops being an ending. It becomes an elevation.",
        "The boat has reached the shore. Now step off it.",
        "Next time we look at Karma, Retribution and Reincarnation - the rules that invisible hand is actually running on. See you there.",
    ]),
]
