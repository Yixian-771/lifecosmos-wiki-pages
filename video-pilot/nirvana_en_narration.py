# -*- coding: utf-8 -*-
"""
"Nirvana" narration script (098 English deck, 14 slides, 1:1 with the source, unpatched).
Note: NotebookLM titled slide 5 "Strip away the mythology to see the historical reality" — sharper than the
source's "No need to make them untouchable"; flagged to the user, narration keeps the source's register.
Thread: p1 hook (nirvana is not an ending but an arrival) -> p2 the wondrous mind -> p3 lively, not merely tranquil
-> p4 Buddha and celestial -> p5 the Buddha's nirvana in history -> p6 turn around and reach the shore
-> p7 without hindrance -> p8 four ways to leave the body; Phoenix Nirvana is transformation -> p9 breaking the cocoon
-> p10 letting go of fixed views -> p11 the state of nirvana -> p12 the raft -> p13 the joy -> p14 closing.
⚠ Length: 5:00-10:00 hard. Andrew ≈ 15.5 characters/second.
⚠ Guardrails: nirvana is not death; "turning around is death" is transformation, not ending life, and the chain's answer
   to "why die?" is not used; the four ways listed, Phoenix Nirvana clarified, natural death and soul separation named only;
   "no intimate friends" one line tied to the mind without hindrance; the Buddha's nirvana as this teaching's view of
   history, no judgement of any religion; "nirvana is lively" as an argument, no mockery; "same in nature, different in
   method"; name no individual; "only some of them" for the abridged list.
⚠ Register: attribution on p1 and p5; Concept 693 is a precise citation.
"""

NAME = "nv_en_show"
VOICE = "en-US-AndrewNeural"
FONT = r"C:\Windows\Fonts\msyhl.ttc"
RATE = "+0%"
MUSIC = r"F:\百科馆\百科BGM\Quiet Study.mp3"
WATERMARK = "Lifechanyuan"

META = [
    {"quote": "Nirvana is not an ending, but an arrival"},
    {"quote": "Pointing directly to the human heart"},
    {"quote": "Nirvana is lively, not merely tranquil"},
    {"quote": "For a celestial, everything becomes play"},
    {"quote": "No need to make them untouchable"},
    {"quote": "Turn around, and there is the shore"},
    {"quote": "The mind without hindrance reaches nirvana"},
    {"quote": "The same in nature, different in method"},
    {"quote": "Without breaking the cocoon, no taking wing"},
    {"quote": "Let go of the self to see things as they are"},
    {"quote": "Eyes closed, stillness, another world"},
    {"quote": "On the far shore, set down the raft"},
    {"quote": "Leaving the six paths of rebirth"},
    {"quote": "Nirvana is not an ending, but an arrival"},
]

SLIDES = [
    ("slides_nv_en/slide_01.png", [
        "Hear the word nirvana, and many people think of death, or of an empty stillness with no life left in it.",
        "In the Lifechanyuan teaching it is the opposite: nirvana is life's ultimate transcendence and its homecoming. Not a cold void, but life entering its purest joy and freedom once every affliction and suffering has been taken away.",
        "Ultimate nirvana means you have already arrived at the Elysium World.",
        "So what state is nirvana, how does one get there, and what is it like on arrival?",
    ]),
    ("slides_nv_en/slide_02.png", [
        "The source of Zen heart-teaching is a saying of the World-Honoured One: I possess the Treasury of the True Dharma Eye, the wondrous mind of nirvana, the true form that is formless, the subtle dharma gate; not founded on words, transmitted outside the teachings, pointing directly to the human heart; see your nature and become a Buddha.",
        "Here nirvana is not a final station. It is a wondrous mind.",
        "It is not passed on through words or scriptures. It points straight to the heart, and seeing one's nature is becoming a Buddha.",
    ]),
    ("slides_nv_en/slide_03.png", [
        "Buddhism has three dharma seals: all conditioned things are impermanent, all phenomena are without self, nirvana is tranquil.",
        "This teaching offers an argument. Every phenomenon can be falsified within limited space-time, but none can be falsified within infinite space-time.",
        "Because the universe is a unity of opposites, countless examples can be found to prove any phenomenon true, and countless more to prove it false.",
        "So one can equally show: all conditioned things have constancy, all phenomena have self, and nirvana is lively. Nirvana is not cold and quiet; it is full of life.",
    ]),
    ("slides_nv_en/slide_04.png", [
        "So after nirvana, is there simply nothing left to do?",
        "Having nothing left to do does not mean lying motionless, or turning into stone or wood. It means being flexible and whole, going with nature: at ease wherever you are, transforming with circumstance, moving with your nature, acting as the moment asks.",
        "Without striving, without desire, without clinging, without resentment, without fear, to name only some, and in the end, without self.",
        "As a Buddha, one has entered nirvana's stillness. As a celestial, everything has become play.",
    ]),
    ("slides_nv_en/slide_05.png", [
        "On the Buddha's own nirvana, this teaching takes a very direct view.",
        "The Buddha passed into nirvana after accidentally eating poisonous mushrooms, not, as The Buddha's Final Testament describes, after calmly answering many questions and departing without a trace of fatigue. That does not accord with history.",
        "And it holds that the greatest person in human history was Christ Jesus, and the one of highest wisdom was the Buddha Shakyamuni.",
        "But later generations covered over the history and sanctified them so far that it made them harder for people to draw near to.",
    ]),
    ("slides_nv_en/slide_06.png", [
        "So how does one reach nirvana? Take it one question at a time.",
        "The sea of suffering is boundless; turn around, and there is the shore. Turn around? What does it mean to turn around? Turning around is dying. And the dying here is not ending one's life; it is leaving behind the sea of suffering and old habits and attachments, the old self transformed from the bone.",
        "How does one die? Nirvana. How does one reach nirvana? Cultivation. How does one cultivate? Raise awakening, grow wisdom.",
        "And what is wisdom? A supreme, thorough understanding of life and death. That is wisdom.",
    ]),
    ("slides_nv_en/slide_07.png", [
        "Within cultivation there is one core gate: a mind without hindrance.",
        "Concept six hundred and ninety-three of the Eight Hundred Values: through prajnaparamita the mind is without hindrance; without hindrance there is no fear; far from inverted illusions, one reaches ultimate nirvana.",
        "Put more bluntly: to cultivate into a celestial, one must come to have no intimate friends.",
        "As the Heart Sutra says, with the mind without hindrance there are no inverted illusions, and one can reach ultimate nirvana and go straight to the heavenly kingdom.",
        "While the heart still holds worry, clinging, fear or resentment, nirvana stays out of reach; the heart of cultivation is letting go, step by step.",
    ]),
    ("slides_nv_en/slide_08.png", [
        "There are four ways to leave the physical body: first, natural death; second, transmutation; third, Phoenix Nirvana; fourth, soul separation.",
        "The one Lifechanyuan emphasises is the Phoenix Nirvana method.",
        "To be clear, this Phoenix Nirvana is transformation through cultivation. It is not ending one's life.",
        "It shares something with the historical, and especially the Buddhist, Phoenix Nirvana, and differs from it too: the same in nature, different in method. Please do not conflate them, or read meaning into the name.",
    ]),
    ("slides_nv_en/slide_09.png", [
        "Phoenix Nirvana has a vivid image behind it.",
        "The silkworm's cocoon protects the pupa, and the pupa transforms inside it. Once the transformation is complete, it must break through the cocoon to reach Phoenix Nirvana and transmute into a celestial, just as the pupa has to break out of its case to become a butterfly.",
        "There are thirty-six Bagua Formations in the universe, each like a cave strung thick with webs.",
        "Without finding the way out, the ascent is never completed, and another realm is never entered. The cocoon is protection, and it is also the layer that has to break.",
    ]),
    ("slides_nv_en/slide_10.png", [
        "What is it that has to break? First of all, attachment to self.",
        "The Buddha taught no self-form to lead us, first, to let go of clinging to the self.",
        "Only when the fixed views, biases and narrow views of I are thrown away can one see things as they truly are, and see the Tathagata of one's own nature; only then can one roam freely through the thirty-six dimensions, released from every fence and shackle.",
        "And so one reaches nirvana and supreme enlightenment, and all of it, in the end, serves the I. Letting go of the small self is how the true self is fulfilled.",
    ]),
    ("slides_nv_en/slide_11.png", [
        "What is the state of nirvana like? It can be described very concretely.",
        "Close the eyes. Be still. Clear the mind entirely of material-world consciousness, and be in the state of nirvana.",
        "One then enters a space tunnel at once, not a time tunnel, and according to the state of one's own antimatter life structure, can arrive instantly in another world.",
        "What one sees there is a single scenic spot of the antimatter world, a realm trillions of times more complex and immense than the Earth we see.",
    ]),
    ("slides_nv_en/slide_12.png", [
        "And once there, does one still need the method? There is a beautiful parable.",
        "The Tathagata often said: monks, know that my teaching is like a raft; even the dharma should be let go of, how much more what is not dharma?",
        "Once you have seen your own nature and known the joy of nirvana, you may let go of this method, just as a bamboo raft built to cross a river is not needed once you reach the far shore.",
        "If even the true dharma is to be set down, why hold on so tightly to the ways of the world?",
        "The method of cultivation is the raft. On the far shore, with the joy of nirvana known, the raft can be set down too. That is not clinging even to the method.",
    ]),
    ("slides_nv_en/slide_13.png", [
        "So what is the joy of nirvana?",
        "Having seen the Tathagata and become a Buddha, one can leave the six paths of rebirth, pass into nirvana in the Western Elysium World, and live an eternal life of supreme joy.",
        "Ultimate nirvana is having arrived at the Elysium World: great freedom, great completeness, joy without end.",
        "For a Buddha it is nirvana's stillness; for a celestial everything becomes play, living freely among the Celestial Islands of the Elysium World.",
    ]),
    ("slides_nv_en/slide_14.png", [
        "Looking back along the way: the wondrous mind of nirvana is the source of Zen heart-teaching; nirvana is not only tranquil but lively, full of life; for a Buddha it is stillness, for a celestial everything becomes play.",
        "The road to nirvana is cultivation, a mind without hindrance, and letting go of the self; Phoenix Nirvana is breaking out of the cocoon, transformation from the bone.",
        "Once the joy of nirvana is known, even the raft that carried you across can be set down.",
        "Nirvana is not an ending. It is an arrival: from the sea of suffering, through cultivation, to the Elysium World.",
    ]),
]
