---
chinese: 神明综合症 (shénmíng zōnghézhèng) — 不会受伤的人，也很难找到快乐
prerequisites:
  - "[[The Gift of the Gradient]]"
  - "[[You Are a Reinforcement Learner]]"
  - "[[Fun Is the Brachistochrone]]"
leads_to:
  - "[[Where It Hurts Might Not Be Where It Broke]]"
tags:
  - subject/methodology
  - subject/philosophy
  - subject/psychology
  - domain/cognition
  - domain/emotion
  - level/life
  - type/methodology
  - type/cross-domain
  - misconception/pain-is-only-an-enemy
  - misconception/protecting-means-removing-every-hurt
  - misconception/suffering-is-good-for-you
---

# God Syndrome 神明综合症

> *A god who cannot be hurt has nothing at stake, and a life with nothing at stake has nothing to celebrate. The hurt was never the price of the joy by accident. It is what the joy is measured against.*

Every player knows the cheat code. Type it in and nothing can touch you: no damage, no death, infinite everything. The first ten minutes are glorious. Then the game goes flat. You walk through the boss fight you once spent a week on, win, and feel nothing at all, because you knew you would win before you started.

This card takes that flat feeling seriously. Its claim is simple and, stated carefully, true: **someone who cannot be hurt, in the body or in the heart, will struggle to find what it means to be happy.** Not because suffering is good; it is not. Because joy is a *difference*: the distance between what happened and what could have happened instead. Take away the chance of loss and there is no distance left to feel.

The name is a warning, not a diagnosis. In English a "god complex" means arrogance, someone who thinks they are always right; that is a different thing. God Syndrome here means the condition of the invulnerable: the god in the story who cannot bleed, and so, slowly, cannot feel.

## 中文锚点

玩过游戏的人都知道"无敌模式"：什么都伤不到你，你也死不了。头十分钟特别爽，然后就没意思了。你打赢了大Boss，心里却一点波澜都没有，因为你早就知道自己会赢。赢的快乐从来不在"赢"本身，而在"赢"和"本来可能会输"之间的那段距离里。把输的可能关掉，这段距离就缩成了零，快乐也跟着没了。人生也是这样。受伤——身体上的，还有心里的——是"有东西可以失去"的代价：一个永远不可能失去朋友的人，也没法真正感受到有朋友的温暖。所以，当你想给自己、或者给你爱的人打开无敌模式，躲开每一次可能的失败、拒绝和失去时，要想清楚你在拿什么交换。你拿掉的不只是痛，还有让好日子显得美好的那些东西。

---

## 1. Baldur: the gift that took everything

In *God of War* (2018) the goddess Freya loved her son Baldur so much that she could not bear the thought of him being hurt. So she cast a spell on him. Nothing could wound him any more, with a single exception she kept secret: mistletoe.

The spell worked. It also took everything else. It could not remove pain alone, because a body does not keep pain and pleasure in separate drawers; it stopped him feeling pain *or pleasure*, down to the cold of the snow. He lived like that for about a hundred years, and in those hundred years the love he had for his mother curdled into hatred. When he finally meets Kratos, a warrior strong enough to hit him properly, what he hopes for is not to win. He hopes, in his own words, that a real fight would "finally make me feel something". It does not. Nothing can.

Then, in a scuffle, Baldur strikes the boy Atreus, and his fist closes on an arrowhead of mistletoe tied to the boy's quiver. The spell breaks, and for the first time in a century he can feel. The first thing he feels is pain. At the end he turns on Freya, who pleads that she was only trying to protect him, and Kratos kills him to save her. His last word, as a flake settles on his face, is "Snow…". The first gentle thing he has felt in a hundred years is the last thing he feels.

Freya's intentions were perfect and her spell did exactly what she asked. That is what makes the story frightening. She asked for the wrong thing: she asked for a son who could not be hurt, and she got a son who could not be reached.

## 2. William: the park where nothing can hurt you

*Westworld* (HBO, 2016) is a theme park full of lifelike robot "hosts", built so that paying guests can do anything, win every fight and suffer no consequence. The hosts are programmed never to harm a guest. It is god mode, sold by the day.

The Man in Black has been coming for thirty years. He is rich, powerful and bored beyond words, and what he wants from the park, the one thing money cannot buy there, is a fight he could lose. In the first episode he tells a host he did not pay all that money to have it easy; he wants it to fight back. In the last he says it plainly: the game is not worth playing if your opponent is programmed to lose.

The darkest scene explains why. After his wife died he came to the park to find out who he really was, and to test whether he had real evil in him he killed a host and her daughter. His verdict on himself afterwards is that he felt nothing. What he did see was the mother's grief as she held her child, and he says that for a moment she was truly alive. The one moment of real life he found in his invulnerable world belonged to someone who had just lost everything.

In the finale the hosts are given the power to fight back for real. A bullet hits the Man in Black in the arm, and he smiles. It is the first thing in thirty years that could actually cost him.

Two very different stories, one shape. Freya tried to give invulnerability to someone she loved; William bought it for himself. Both got the same thing: a life with the colour drained out.

## 3. Why: a win is worth what you could have lost

Fiction can make a point vivid, but it proves nothing. Here is the mechanism, and the measurement.

[[You Are a Reinforcement Learner]] showed that a brain learning from reward runs on a **prediction error**: what happened, minus what you expected. Call the chance of winning $p$, value a win at 1 and a loss at 0. Your expectation before the outcome is $p$, so

$$\text{surprise of a win} = 1 - p, \qquad \text{surprise of a loss} = 0 - p = -p .$$

A win you had a 10 % chance of is a surprise of 0.9. A win you had a 90 % chance of is 0.1. A win in god mode, where $p = 1$, is a surprise of exactly zero. The left panel below is those two lines, nothing more.

![[god-syndrome-surprise.svg|720]]
*Left: the surprise of a win shrinks to zero as the chance of losing does; god mode sits at the amber dot. Right: in the 2014 happiness study, each outcome's pull on how happy people felt decayed by a factor $\gamma$ every round; with the fitted average $\gamma = 0.61$, a win ten rounds ago has under 1 % of its original pull. Both panels are computed in `god-syndrome-figures.py`.*

Is happiness really tied to surprise, or is that just a neat piece of algebra? Robb Rutledge and colleagues at University College London tested it in 2014. People made a string of choices between a sure amount of money and a gamble, and every few choices they were asked one question: *how happy are you right now?* Their momentary happiness was explained **not by how much they had won so far**, but by their recent expectations and the prediction errors that followed. The result held in a smartphone version played by 18,420 people who were paid nothing, and an independent preregistered replication in 2021 mostly confirmed it. A follow-up by Blain and Rutledge in 2020, in a task built to pull the two apart, sharpened it: happiness followed surprise about *how likely* things were, that is, what people were learning about the game, rather than the size of the rewards. God mode offers neither kind of surprise. When the outcome is certain there is nothing left to learn.

Two honest details keep this from being oversold. First, sure rewards counted too: in the model a certain gain did lift happiness, so a guaranteed win is not worth *nothing*. Second, every reward faded fast, sure or not. With the average forgetting factor, anything more than about ten rounds old had essentially no influence (right panel). So a life of sure wins is a life of small lifts that vanish in minutes, with no surprise to renew them. That is the flat feeling of god mode, in numbers.

## 4. The numbing does not choose

Freya's spell took pleasure along with pain. Is that just a story, or does feeling really come as one piece?

The evidence is suggestive and should be held loosely.

- **A painkiller that dulls both ends.** In 2015 Geoffrey Durso, Andrew Luttrell and Baldwin Way gave people either 1,000 mg of paracetamol (acetaminophen) or a placebo and showed them pictures ranging from very unpleasant to very pleasant. The paracetamol group rated the pictures less extremely *in both directions*: less upset by the grim ones, less delighted by the lovely ones. Colour judgements were unaffected. A related study in 2016 found the same drug reduced people's distress at *other people's* pain, and a 2019 study found it reduced their pleasure at others' good news.
- **But hold it loosely.** These were small samples (80 to 120 people). A 2021 study found no effect of the drug on the brain's response to emotional pictures, reviewers call the field young, and none of these results has had a direct preregistered replication. They are a hint that feeling is dimmed as a whole, not a proof.
- **Relief is a pleasure, and it grows with the pain.** Siri Leknes and colleagues (2008) measured it directly: when pain stops, people rate the relief as pleasant, and the stronger the pain, the stronger the relief. The oldest version of the idea, Solomon and Corbit's opponent-process theory (1974), says every strong feeling is followed by its opposite. The glow after a hard race, the laugh after the scare on a roller coaster, the hot shower after a freezing walk: those joys exist only on the far side of something that hurt.
- **Shared hurt binds.** A 2014 review by Brock Bastian and colleagues gathered evidence that pain sharpens later pleasure and brings people together. In a related 2014 experiment, strangers who went through something painful together cooperated more afterwards; a 2020 re-examination found the effect only when the pain was *shared*: suffering alone did not bind anyone. The heart's version of this is familiar: the friends you keep for life are often the ones you went through something hard with.

## 5. Two kinds of hurt, both teachers

**The body's hurt.** Some people are born unable to feel physical pain, a rare condition called congenital insensitivity to pain. It sounds like a superpower and it is a danger. Children with it bite their tongues and lips, walk on broken bones without knowing, and burn themselves, because nothing tells them to stop; the medical literature warns that they may have shorter lives. Pain is the body's alarm and its teacher. A child learns that the stove is hot once, and remembers.

**The heart's hurt.** Being left out hurts, and not only as a figure of speech. In 2003 Naomi Eisenberger and colleagues scanned people playing *Cyberball*, a ball-tossing game in which two computer players quietly stop throwing to them, and found activity in a brain region also involved in the unpleasantness of physical pain. The strong version of that claim, that rejection *is* pain in the same circuit, did not survive: a 2014 study by Choong-Wan Woo and colleagues showed the brain's patterns for a burn and for a rejection can be told apart reliably. So the heart's hurt is not borrowed from the body. It is its own alarm, with its own lesson: *this matters to you.* The pang when a friend walks away is the same fact as the warmth when they come back.

A person who could never be rejected could never be chosen. A person who could never lose could never win. That is the whole syndrome in two sentences.

## 6. Jo Cameron: the miracle we do not try to copy

There is one real person who seems to break the rule, and the card owes her an honest look.

Jo Cameron lives in Scotland. At 66 she came into hospital in Inverness for an operation on her hand that is known to be painful, and needed nothing stronger than paracetamol afterwards. Her anaesthetist, Devjit Srivastava, referred her to pain geneticists at University College London and Oxford, and in 2019 the team around James Cox published why: a small deletion in a gene they named *FAAH-OUT* turns down an enzyme that normally breaks up the body's own pain-dampening chemistry. Her case report records burns she noticed only by the smell, cuts that healed fast, a broken wrist with no pain relief, and scores of zero on standard tests for anxiety and depression. She described childbirth as a tickle. The 2023 follow-up paper describes her as having "a happy, non-anxious disposition".

At first sight she is the counterexample. She feels almost no physical pain and she is happy. Look closer, and she is something rarer.

- **She is not unhurtable in the heart.** In Ariel Levy's 2020 profile in *The New Yorker* she cries easily at sad stories and calls herself a softie; she feels indignation at injustice. What she lacks is the far end: Levy reports she has never known the extremes of rage, dread or grief, and that her mind looks for a fix rather than dwelling on unhappiness.
- **She cares for people without feeling their pain as her own.** Levy reports that she does not feel other people's pain the way most of us do, and yet she is warm and affectionate to the people in her life. The ordinary route to kindness runs through our own hurt: we know what it is like, so we flinch when it happens to someone else. Somehow she found her way to caring without that teacher.

That is not a hole in the argument. It is a miracle, and the right response to a miracle is to honour it, not to reverse-engineer it. Her gift came from one small deletion in her genes, plus a life and a temperament nobody chose for her. Levy's profile raises exactly this card's question, whether pain is what makes joy precious, and leaves it open. This card's claim survives her because it was always a *might*: most of us learn what matters by what it costs us, and she is the exception who got there another way.

## 7. Why trying to copy it fails

Everyone who tries to manufacture invulnerability gets the wrong half.

- **Freya** tried to give it to someone she loved. She removed the hurt and the feeling came out with it, and the love went next.
- **William** bought it for himself. He removed the stakes and found that the only living thing in his world was someone else's grief.
- **The everyday version** needs no magic. A parent who clears every obstacle from a child's path, who argues every low mark up and fixes every falling-out, is casting Freya's spell in small doses. A student who never answers in class so as never to be wrong, never enters a competition so as never to lose, never tells a friend they matter so as never to be let down, has switched on god mode for themselves. And reaching for anything that numbs, from endless scrolling to a substance, dims the good along with the bad, which is what the paracetamol studies hint at and what [[You Are a Reinforcement Learner]] says about addiction: a loop that gets its reward without an act to credit stops being able to feel the real ones.

The mistake is always the same one. It treats pain as a defect in an otherwise good system and tries to delete it. Pain is not a defect. It is the signal that tells you something is at stake. Delete the signal and the stakes do not disappear; you just stop being able to feel them, the good ones included.

## 8. What to do instead

This is not an argument for seeking pain. Nobody should go looking for hurt, and nobody should inflict it for someone's "own good". The decision the card is about is smaller and harder: **when you could switch on god mode, for yourself or for someone you love, don't.**

- **Keep the chance of loss in the game.** Enter the competition you might lose. Answer the question you might get wrong. Tell the friend they matter. The possibility of a bad outcome is what gives the good one its weight.
- **Let people you love meet small hurts while you are near.** A scraped knee with a hug is a lesson; a childhood with no scraped knees is Freya's spell.
- **Share the hurt.** Suffering alone does not bind anyone; suffering together does, and it is the ground most lasting friendships are built on.
- **Read it rather than silence it.** Pain is information. It says *something here matters*, and often *something here is wrong*. The next step, [[Where It Hurts Might Not Be Where It Broke]], is learning to read where the signal is really coming from.

## Honest edges

- **This is not "suffering is good".** Some pain teaches nothing. Chronic pain, depression, and grief that does not lift are alarms that have gone wrong or will not switch off; they call for a doctor, a counsellor or a trusted adult, not for endurance. The card is about *the possibility* of hurt, not about collecting it.
- **The evidence comes in tiers.** The link between happiness and surprise (Rutledge and colleagues) is measured, replicated and fairly solid. The paracetamol studies are small, partly contradicted, and a hint at best. The two stories are fiction: they make the idea vivid and prove nothing.
- **Jo Cameron is not a case against pain, and not a case for it.** She is one person with a rare gene and a warm heart. Her life shows that caring *can* grow without the usual teacher. It does not show that anyone could get there by numbing themselves, and nothing here should be read as a claim about her inner life beyond what she and her doctors have said.
- **"Might", not "must".** The claim is that someone who cannot be hurt will *struggle* to find what happiness means, not that they cannot. Most of us learn it through what things cost; a few, like her, do not.

---

## Connections

- **Builds on:** [[The Gift of the Gradient]] — nothing runs on the amount of anything, only on a difference; this card is the same idea for a human heart: joy runs on the gap between what happened and what might have. [[You Are a Reinforcement Learner]] — the prediction error behind §3, and the addiction warning behind §7. [[Fun Is the Brachistochrone]] — fun needs a target you chose and could miss.
- **Leads to:** [[Where It Hurts Might Not Be Where It Broke]] — once hurt is a signal worth keeping, the next skill is reading where it comes from.
- **Sibling:** [[The Love of Wisdom]] — meaning lives in the lack that reaches; a being that lacked nothing and risked nothing would have nothing to reach for. [[Credit Is the Currency]] — a promise is worth something only because it could have been broken.

## Sources

- R. B. Rutledge, N. Skandali, P. Dayan and R. J. Dolan, "A computational and neural model of momentary subjective well-being", *PNAS* 111 (2014) 12252–12257 — happiness from expectations and prediction errors; the 18,420-person smartphone replication; forgetting factor 0.61 ± 0.30.
- N. Vanhasbroeck et al., "Testing a computational model of subjective well-being: a preregistered replication of Rutledge et al. (2014)", *Cognition and Emotion* 35 (2021) 822–835.
- B. Blain and R. B. Rutledge, "Momentary subjective well-being depends on learning and not reward", *eLife* 9 (2020) e57977.
- G. R. O. Durso, A. Luttrell and B. M. Way, "Over-the-counter relief from pains and pleasures alike", *Psychological Science* 26 (2015); D. Mischkowski, J. Crocker and B. M. Way, "From painkiller to empathy killer", *Social Cognitive and Affective Neuroscience* 11 (2016) 1345; D. Mischkowski et al., "A social analgesic? Acetaminophen reduces positive empathy", *Frontiers in Psychology* 10 (2019) 538; and, against, Garrison et al., *Cognitive, Affective, & Behavioral Neuroscience* (2021).
- S. Leknes, J. C. W. Brooks, K. Wiech and I. Tracey, "Pain relief as an opponent process: a psychophysical investigation", *European Journal of Neuroscience* 28 (2008) 794–801; R. L. Solomon and J. D. Corbit, "An opponent-process theory of motivation", *Psychological Review* 81 (1974) 119–145.
- B. Bastian, J. Jetten, M. J. Hornsey and S. Leknes, "The positive consequences of pain: a biopsychosocial approach", *Personality and Social Psychology Review* 18 (2014); and the 2020 re-examination of the shared-pain finding in the *Journal of Pacific Rim Psychology*.
- N. I. Eisenberger, M. D. Lieberman and K. D. Williams, "Does rejection hurt? An fMRI study of social exclusion", *Science* 302 (2003) 290–292; C.-W. Woo et al., "Separate neural representations for physical pain and social rejection", *Nature Communications* 5 (2014) 5380.
- MedlinePlus Genetics, "Congenital insensitivity to pain" and "Congenital insensitivity to pain with anhidrosis".
- A. M. Habib et al., "Microdeletion in a FAAH pseudogene identified in a patient with high anandamide concentrations and pain insensitivity", *British Journal of Anaesthesia* 123 (2019) e249–e253; H. Mikaeili et al., "Molecular basis of FAAH-OUT-associated human pain insensitivity", *Brain* 146 (2023) 3851–3865; A. Levy, "A world without pain", *The New Yorker* (13 January 2020); H. Murphy, *The New York Times* (March 2019).
- *God of War* (Santa Monica Studio, 2018); *Westworld*, season 1 (HBO, 2016), episodes 1, 8 and 10.
- `god-syndrome-figures.py` — the figure, computed.
