# -*- coding: utf-8 -*-
"""
"Spiritual Life" narration script (094 English deck, 14 slides, deck 1:1 with the source, checked page by page).
Thread: p1 hook (the best road through a life is not the one walked by being cleverer) -> p2 the three kinds
of life, their definitions and proportions -> p3 the portrait of a spiritual life -> p4 what reason runs on,
what spirit runs on -> p5 the proportion: reason is genuinely valuable, and it is the ceiling
-> p6 human cleverness against the workings of heaven -> p7 where the sage is stuck: he will not empty his
head -> p8 the outlook: when you meet what is worthy, entrust yourself entirely -> p9 keep only kindness,
diligence, honesty and good faith; hand the rest to the Dao -> p10 reason complicates, spirit simplifies
-> p11 reason is the mark of a human, spirit the mark of a celestial -> p12 religion or not: no religion in
the heart -> p13 what is taken is the teaching, not the membership -> p14 reason walks you to the wall;
open your hand and it thins.
⚠ Length: **5:00-10:00 hard, 8:30-9:30 target** (upper bound set by the user 2026-09-06). Andrew +0%
   measured at **≈15.1 characters/second**; body ≈8400 characters. Run `--stills` before rendering; if it
   passes 570s, cut setup sentences — **never cut a guardrail clause**.
⚠ Nine guardrails (follow each): 1. **The percentages are quoted as they stand, with no ranking judgement**
   — p2 must say in the same breath that these are three different roads, not three classes of people.
   2. **Never turn this into a dismissal of reason** — p5 is devoted to the proportion; the line **"for a
   human being, reason is the ceiling of cognition and a genuinely valuable mode of thought" must be
   spoken**, then paired with "for LIFE above the human, reason is a cage". 3. **The angel passage names
   several faith communities** — p12 says only that examples from several different faiths are given,
   **repeats none of them and judges none**; the clause about not excluding others is **not quoted**; the
   page lands on "living a spiritual life does not require joining a religion". 4. **"One who truly intends
   to become a celestial holds no religion in the heart" and "the wisest are usually outside the religions"
   are quoted as they stand, and must sit beside p13's "listen to the teaching of Jesus"** — the teaching,
   not the membership; p12/p13 stay adjacent or they read as a contradiction. 5. **"The best road to a
   spiritual life is to cultivate according to the teaching of Christ Jesus" is stated as it stands** — no
   embellishment, no exclusivist framing. 6. **The "worshipping the guide" passage is not quoted,
   paraphrased or implied**; from that source take only that being at ease wherever one is, transforming
   with circumstance, moving with one's nature and acting as the moment asks is the mark of a celestial.
   7. **"They do not join religions, nor place their hope in nations or in humanity" is stated plainly and
   not expanded** — no political allusion. 8. **Name no Chanyuan Celestial.** 9. **Wherever a list is
   abridged, say only a few are named** (this entry carries no such list).
⚠ Neighbour split: **093 The Spirit Manifests Reality just aired** — **the mind-image definition and the
   eight-year rule are not repeated.** **087 Mind Without Abiding and 090 Fluid Adaptability** are written:
   **the four adaptations are read once and never expanded.** **015 The Greatest Creator, 016 Dao and
   017 The Way of the Greatest Creator** are published: take only "entrust your life to the Dao".
   **095 Settled Stillness, 044 the Elysium World and 066 Antimatter Structure** have their own entries.
⚠ Register: **speak from inside the Lifechanyuan teaching; do not cite a source every other line.**
   One attribution only, on p1; the Caigentan (p6) and Concept 526 (p13) are precise citations and stay.
   **Never read a writing instruction aloud** — no "this entry answers", no "named only here".
Voice: Andrew, warm and conversational. Built from the 094 English slide source. First line = the hook.
"""

NAME = "spl_en_show"
VOICE = "en-US-AndrewNeural"
FONT = r"C:\Windows\Fonts\msyhl.ttc"
RATE = "+0%"
MUSIC = r"F:\百科馆\百科BGM\Golden Sunset.mp3"
WATERMARK = "Lifechanyuan"

META = [
    {"quote": "The last road is not walked by being clever"},
    {"quote": "Three different roads, not three ranks"},
    {"quote": "Seeds of heaven, the finest among people"},
    {"quote": "One is assembled. One flows."},
    {"quote": "Reason carries you to the highest point, then it is the wall"},
    {"quote": "The tighter you calculate, the narrower the road"},
    {"quote": "Hands full, and no hand left over"},
    {"quote": "Reverence, trust, and a gladness that answers"},
    {"quote": "Keep four things, hand the rest to the Dao"},
    {"quote": "Fewer loose ends, straighter road"},
    {"quote": "Move to a layer, live the way that layer lives"},
    {"quote": "One who truly intends to become a celestial holds no religion in the heart"},
    {"quote": "The teaching, not the membership"},
    {"quote": "Open your hand, and the wall thins"},
]

SLIDES = [
    ("slides_spl_en/slide_01.png", [
        "Here is something that runs against the grain: the best road through a life is not the one you walk by being cleverer than everybody else.",
        "Most people spend a lifetime on the same road. Make the living good, get the things done, secure what is owed.",
        "The Lifechanyuan teaching sorts a life into three kinds, and what separates them is neither income nor education. It is what you live by.",
        "Money and position is one kind. Wisdom and truth is another. The third does not live by its own cleverness at all, but by the perception and the inner drive of the spirit. That is the spiritual life.",
    ]),
    ("slides_spl_en/slide_02.png", [
        "The sorting is blunt, and it gives proportions.",
        "The worldly life is lived for money and food, for position and reputation, for favour and friendship. Roughly eighty to eighty-five per cent of people live it.",
        "The life of wisdom is lived to seek truth, create spiritual wealth, pursue the true, the good, the beautiful and love, and build a harmonious society. Roughly five to ten per cent.",
        "The spiritual life takes reverence for the Greatest Creator as its faith, perceives the subtlety of the Dao with the spirit, and seeks unsurpassed awareness. Roughly two to five per cent.",
        "Read those numbers as they stand. They are not three classes of people. They are three different roads.",
    ]),
    ("slides_spl_en/slide_03.png", [
        "There is a full portrait of this third kind.",
        "They carry only the Greatest Creator within, and live not by their own cleverness but by what the spirit perceives and drives them to do.",
        "They do not join religions, nor place their hope in nations or in humanity. Though they live among people, the spirit has passed clean out of space and time and ranges through the kingdom.",
        "They contend for nothing, ask for nothing, and have forgotten their own living and dying altogether. Quiet and glad inside, clear and open. There is a name for them: the seeds of heaven, the finest among human beings.",
    ]),
    ("slides_spl_en/slide_04.png", [
        "Set the two strings of words side by side and the line is plain.",
        "The rational life runs on knowledge, fact, logic and science. It does not look for its best road in slogans, postures, promises or moods.",
        "The spiritual life runs on faith, conviction, conscience, feeling, inner drive and destiny. It does not speak or act out of knowledge, experience, law or rule.",
        "Then each is pressed into one sentence. The core of reason is calculation drawn from knowledge and evidence. The core of spirit is going with one's nature, on faith and intuition.",
    ]),
    ("slides_spl_en/slide_05.png", [
        "This is the easiest place to hear wrongly. That the spiritual life stands above the rational life does not mean reason is a poor thing.",
        "Reason is in fact rated highly here. The rational life is called the life philosophy of the sage, not the philosophy of the muddled, the vulgar or the ordinary.",
        "And it is said outright: for a human being, reason is the ceiling of cognition, and a genuinely valuable mode of thought.",
        "The trouble starts one level up. For LIFE above the human, reason is the cage of thought, a high wall that is hard to cross on the way to heaven.",
        "So hear the two together. Reason carries a person to the highest point a person can reach. And then it is the wall.",
    ]),
    ("slides_spl_en/slide_06.png", [
        "A line in the Caigentan, a Ming-dynasty book of reflections, says this exactly. The upright man does not scheme for blessing, and heaven opens a window for him in the very place he was not scheming. The crafty man works at dodging misfortune, and heaven takes his spirit away in the very place he was working.",
        "Its conclusion: the workings of heaven are most wondrous, so what use is human cleverness?",
        "Brought across, it takes two sentences. Reason is human cleverness. Spirit is the workings of heaven.",
        "The landing is light, and heavy at once. The tighter you calculate, the narrower the road.",
    ]),
    ("slides_spl_en/slide_07.png", [
        "A sage has passed beyond the bindings of instinct, desire and emotion, and entered the rational life. That is already no small thing.",
        "But the moment something passes beyond conventional thinking, the sage is at a loss, baffled, full of doubt, sometimes pushing back. Everything provable he accepts easily; this he cannot.",
        "The answer given is blunt. Unless he gives up his whole mode of thinking and empties his head, a sage can only ever stay a sage.",
    ]),
    ("slides_spl_en/slide_08.png", [
        "The outlook of the spiritual life is itself one sentence. On the road of life, if you meet someone you revere and trust, someone who stirs a gladness in you that answers back, then entrust yourself to them entirely.",
        "Notice the three thresholds, and not one can be skipped. Reverence. Trust. And a gladness inside you that answers.",
        "Which is what separates entrusting from credulity. Credulity has no threshold. Entrusting is the choice you make after crossing all three.",
    ]),
    ("slides_spl_en/slide_09.png", [
        "So how is it lived? The working instructions come in one sentence. Entrust your life to the Greatest Creator. Hand your living over to the Dao to arrange and manage. Keep only kindness, diligence, honesty and good faith. Play your life as a game: be at ease wherever you are, transform with circumstance, move with your own nature, and act as the moment asks.",
        "The most practical part is the middle. Keep only kindness, diligence, honesty and good faith.",
        "Four things, all of them yours to decide. Everything else you hand over.",
        "Playing it as a game is not treating it lightly. It is not holding yourself rigid inside it. Those four ways of going with things are the mark of a celestial.",
    ]),
    ("slides_spl_en/slide_10.png", [
        "A short observation here that most people recognise at once. Reason complicates a person. Spirit simplifies a person.",
        "The work of reason is to calculate. Gains and losses, risks, what somebody else meant, what happens three moves from now. The finer the calculation, the more loose ends.",
        "The work of spirit is to follow. You go with what the spirit drives you toward, and the loose ends are few.",
        "Then the point is joined to the goal. A life that is glad, free and happy, a climb to the summit of a life: only one who thinks with the spirit will arrive.",
    ]),
    ("slides_spl_en/slide_11.png", [
        "Why move in that direction at all? The reason ties this to the level of a life.",
        "The higher the level of a life, the more it seeks what belongs to the spirit. The lower the level, the more it seeks what belongs to matter.",
        "Then the dividing line. Reason is the mark of a human being. Spirit is the mark of a celestial. Reason belongs to the material layer, spirit to the antimatter layer.",
        "So the call does not rest on which is finer. It rests on direction. Whichever layer you mean to move toward, you have to start living the way that layer lives.",
    ]),
    ("slides_spl_en/slide_12.png", [
        "There is a question a great many people ask. Do you have to join a religion in order to live the life of wisdom that is lived through the spirit?",
        "The exchange gives examples from several different faiths, and what it lands on is the answer that follows. To live that life, you do not necessarily have to join a religion.",
        "Joining one is mainly a way of finding the surroundings for it, listening to others' teaching, and strengthening conviction through certain forms. If your conviction is already strong, there is no need to be bound by the forms.",
        "And then the two sharpest sentences. One who truly intends to become a celestial holds no religion in the heart. The wisest people are usually found outside the religions.",
    ]),
    ("slides_spl_en/slide_13.png", [
        "No religion in the heart has a second half that belongs with it, and the two have to be heard together.",
        "The road pointed out for the spiritual life is stated plainly. To live a spiritual life, the best road is to cultivate according to the teaching of Christ Jesus.",
        "The reason given: everything Jesus taught was gathered around one thing, walking the way of the Greatest Creator. That was his whole mission on earth and his only purpose.",
        "Concept five hundred and twenty-six of the Eight Hundred Values puts both halves in one line. To accomplish a spiritual life, listen to the teaching of Jesus, and walk the way of the Greatest Creator as he taught it.",
        "Heard together, the meaning is clear. What is taken is the teaching, not the membership.",
    ]),
    ("slides_spl_en/slide_14.png", [
        "Here is where it lands. The spiritual life is the one stride that carries a sage across into a celestial.",
        "The sage stops at the border of reason and judges the way by logic, so he never crosses that wall. The one living a spiritual life opens the hand and entrusts himself entirely, and the door opens instead.",
        "Look back along the road. A life sorts into three kinds, and the difference is what you live by. Reason runs on knowledge and logic; spirit on faith and inner drive. Reason is valuable, and it is the human ceiling. Where the sage sticks is his refusal to empty his head.",
        "Reason walks you up to the wall. Open your hand, and the wall thins away.",
    ]),
]
