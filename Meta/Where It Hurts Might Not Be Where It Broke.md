---
chinese: 疼的地方，未必是坏的地方 (téng de dìfang, wèibì shì huài de dìfang)
prerequisites:
  - "[[God Syndrome]]"
  - "[[The Kinetic Chain]]"
  - "[[Forward Reading and Problem Discovery]]"
leads_to: []
tags:
  - subject/methodology
  - subject/computer-science
  - subject/physics
  - domain/debugging
  - domain/cognition
  - domain/biomechanics
  - level/life
  - type/methodology
  - type/cross-domain
  - type/hands-on
  - misconception/the-fault-is-where-it-hurts
  - misconception/the-crash-line-is-the-bug
  - misconception/always-look-upstream
---

# Where It Hurts Might Not Be Where It Broke 疼的地方，未必是坏的地方

> *Pain is a message, and messages travel. It is reported where it arrives, not where it was written. Most of the time the two are the same place. The skill is noticing when they are not.*

A heart in trouble can make itself felt as an ache down the left arm. A program can crash on line 30 because of a mistake on line 20. An exam answer can come out as the square root of a negative number because of a sign written three steps earlier. In each case the place that hurts is the end of a chain, and the place that broke is further up it.

[[God Syndrome]] argued that hurt is worth keeping, because it is the signal that something is at stake. This card is about reading that signal: **where it hurts might not be where it broke.** The word that matters is *might*. A cut finger hurts where it is cut, and a student who treats every pain as a clue to somewhere else is as lost as one who never looks past the obvious. What the card teaches is when to trace back, how to do it, and when to stop.

## 中文锚点

天花板角落开始滴水。你擦干了，第二天早上它又来了。水在落下来之前，会先顺着梁、顺着管子流一段路，所以滴水的地方只是水"出得来"的地方，不一定是管子破的地方——破口可能在楼上邻居家，位置还错开了两个房间。身上的疼、程序的报错、算错的答案，常常也是这样：一个信号顺着一条链传下来，最后在看得见的地方冒出来。所以，擦了又滴、擦了又滴的时候，就别再擦了，上楼去：顺着水可能走过的路，一路找回它开始的地方。但要记住"未必"这两个字：有时候破的就是你头顶那根管子。所以先看头顶，看一眼不费事；等擦干了水又回来，再上楼。

---

## 1. Why hurt travels

Every example in this card has the same shape. Something goes wrong at one link of a chain. The chain carries the consequence along. The consequence becomes visible at the first place that is able to show it, which is usually near the end.

![[where-it-hurts-chains.svg|760]]
*Five chains from this card. Amber is where it broke, red is where it hurts, and the dashed arrow is the trace back. In every row the red box is the one you notice first, and the amber box is the one you have to fix.*

Why near the end? Because the end is where the chain meets you. Water becomes visible where it can drip. A program's mistake becomes visible when some later line tries to use the bad value. A wrong sign becomes visible when the arithmetic finally refuses to work. A body's trouble becomes visible where the nerves that carry it happen to be mapped. The chain does not hide the break on purpose; it just carries it quietly until something downstream cannot cope.

The debugging researcher Andreas Zeller gave the software version names that fit every row: a **defect** (the broken link) causes an **infection** (a bad state that spreads) which finally causes a **failure** (something you can see). Not every defect infects anything, and not every infection shows. But when a failure does show, it is the end of that chain, not its start.

## 2. The body: pain that arrives somewhere else

**Referred pain.** Nerves from the internal organs and nerves from the skin and muscles meet on the same neurons in the spinal cord. The brain has a detailed map of the skin and only a blurry one of the organs, so when a signal arrives on a shared line, it tends to be read as coming from the body surface that shares it. Physiologists call this convergence; one review likens it to crossed telephone lines. The pattern is consistent enough that doctors learn it as a map:

- **The heart.** Angina and heart attacks are often felt in the chest, and also in the left arm and hand, the neck, the jaw or the back. In a study of 434,877 heart attacks in the United States (Canto and colleagues, 2000), **a third of patients arrived at hospital with no chest pain at all**. They arrived hours later, were far less often recognised as having a heart attack on admission (22 % against 50 %), and died in hospital more often (23 % against 9 %). The hurt in the unexpected place was the more dangerous one, because nobody traced it back.
- **The diaphragm.** Blood or irritation under the diaphragm, from a ruptured spleen for instance, can be felt at the tip of the shoulder: the diaphragm's own sensory nerve, the phrenic, enters the spinal cord in the neck (C3 to C5), near the nerves that serve the shoulder. Doctors call it Kehr's sign.
- **The appendix.** Appendicitis usually starts as a vague ache around the navel, carried by the gut's own nerves, and only later settles in the lower right of the abdomen, once the inflamed appendix irritates the lining of the belly wall, whose nerves are precise. Here the hurt *moves toward* where it broke. That is itself a clue.
- **A child's hip.** In a condition where the top of the thigh bone slips at its growth plate (slipped capital femoral epiphysis), about a quarter of children feel it mainly in the knee, through a nerve the hip and knee share. In a study of every child with the condition in 650 UK family-doctor practices over 23 years, those who complained of knee pain waited a median of **161 days** for a diagnosis, against 20 days for those who complained of the hip. Medical teaching now says: in a child with knee pain, examine the hip.

**Load that moves down a chain.** [[The Kinetic Chain]] §5 measured a second way for the body to hurt in the wrong place. Weaken the trunk in a throw and leave the arm alone: to keep the ball's speed, the shoulder and elbow must produce 22 % more torque at 80 % trunk strength and 47 % more at 60 %. The elbow is where it hurts; the trunk is where it broke.

> [!warning] This card never diagnoses
> Maps of referred pain describe what is common, not what is happening to you. **Chest pain, or pain spreading to the arm, neck or jaw, or sudden breathlessness, is an emergency: call for help at once (120 in mainland China).** A pain that stays, swelling, a limp or a joint that gives way needs a doctor or a physiotherapist. The only thing this card gives you is the right question to bring: not only "what hurts?" but "what else could be sending this?"

## 3. Code: the crash line is not the bug

Run `where-it-hurts-lab.py` beside this card. It is a three-stage pipeline: `parse` turns a line like `"Ben,85"` into a name and a mark, `load` parses a whole list, and `top_student` finds the highest mark. One record reads `"Chen,absent"`, and `parse` has a defect: for anything that is not digits it forgets to return anything, so Python quietly hands back `None`.

**Part 1, where it hurts.** The program dies in the last stage:

```text
  File "where-it-hurts-lab.py", line 31, in <lambda>
    return max(rows, key=lambda row: row[1])
TypeError: 'NoneType' object is not subscriptable
```

The traceback points at `top_student`, and `top_student` is correct. Change it however you like and the crash just moves. Jim Shore put it exactly, writing about this pattern in 2004: the stack trace leads to a dead end.

**Part 2, walk the chain upstream.** Check what each stage *hands on*, starting from the one that failed and moving back, and stop at the first bad output:

```text
load() returned: [('Ana', 78), ('Ben', 85), None, ('Dara', 91)]
  parse('Chen,absent'  ) -> None            <- first bad output
```

The infection is visible in `load`'s output, and it entered at `parse`. That is where it broke.

**Part 3, fix it where it broke, and make the next break hurt there.** The fixed `parse` handles `"absent"` on purpose and *refuses* anything else it does not understand, loudly, at once:

```text
('Dara', 91)
ValueError: Eve: mark '8O' is neither a number nor 'absent'
```

A letter O typed for a zero now fails inside `parse`, naming the record, instead of three functions later. This is the design lesson Shore called **fail fast**: a program should complain as close as possible to the original problem. You cannot always stop things breaking. You can arrange for them to hurt where they broke.

When the chain is long (a thousand commits, not three functions), you do not walk it one link at a time. You check the middle, keep whichever half still contains the break, and repeat. That is binary search aimed at history, and **Searching** *(not yet released)* shows `git bisect` doing it: about twenty checks find the guilty change among a million.

## 4. Maths: the answer hurts at step 5, the sign broke at step 2

A ball is thrown straight up at 15 m s⁻¹ from the edge of a cliff 20 m high. How long until it hits the ground below?

A student takes up as positive, writes the displacement to the ground as $+20$ m, and solves $s = ut + \tfrac12 at^2$ with $a = -9.8$:

$$20 = 15t - 4.9t^2 \quad\Longrightarrow\quad 4.9t^2 - 15t + 20 = 0, \qquad \Delta = 15^2 - 4(4.9)(20) = -167.$$

The square root of $-167$ is where it hurts. The quadratic formula is fine. The break is the sign at step 2: with up as positive, the ground is 20 m *below* the start, so $s = -20$:

$$-20 = 15t - 4.9t^2 \quad\Longrightarrow\quad 4.9t^2 - 15t - 20 = 0, \qquad t = \frac{15 + \sqrt{617}}{9.8} = 4.07\ \text{s}.$$

And the negative discriminant was telling the truth all along, about the question the student had actually asked. The ball rises only $15^2 / (2 \times 9.8) = 11.5$ m, so it never *is* 20 m above the cliff top. A symptom is often a correct answer to a question you did not mean to ask. Reading it that way is the fastest route back to the break: *what question would make this answer right?*

## 5. Engineering: 226 km planned, 57 km flown

On 23 September 1999 NASA's Mars Climate Orbiter fired its engine to go into orbit around Mars and was never heard from again. Its first pass was planned at 226 km above the surface; 80 km was the lowest it could survive. Reconstruction afterwards put it at about **57 km**, deep enough in the atmosphere to destroy it.

The break was far from Mars. One ground software file reported the small thruster firings used to trim the spacecraft's path in pound-force seconds, while the navigation software that read it expected newton seconds. Every firing was underestimated **by a factor of 4.45**, and over nine months of cruise the small errors added up.

The hurt had shown itself early. The investigation board found that navigators saw odd results within a week of the file coming into use, and raised concerns through the spring and summer, but the discrepancies were only reported informally, by e-mail, and never pushed back up the chain to the file that caused them. The signal existed. Nobody traced it. The board's lesson is the one from §3 at the scale of an organisation: make small hurts loud, and make someone responsible for following them upstream.

## 6. The heart: the snap is not about the sibling

Hurt in the heart travels too. A student gets a bad mark, says nothing, goes home, and snaps at a younger brother over the television. The brother is where it hurts. The mark is where it broke. Psychologists call this **displacement**: a feeling transferred from where it started to a safer target, like the employee who cannot shout at the boss and criticises their spouse instead. A 2000 review pooling the experiments (Marcus-Newhall and colleagues) found the effect is robust: people who have been provoked and cannot answer back take it out on someone else, more so when that someone resembles the provoker.

This cuts both ways. When you catch yourself snapping, ask what happened earlier. When someone snaps at you out of nowhere, it *might* not be about you. It might be about something upstream you cannot see, and a quiet "bad day?" can reach the break faster than an argument about the television.

## 7. The other side of "might"

Tracing back is a tool, and like every tool it can be used where it does not belong.

**Sometimes it is exactly where it broke.** You cut your finger; it hurts where it is cut. The ceiling drips directly under a bathroom with a cracked pipe. The crash really is in `top_student` because `top_student` has a typo. Most hurts, most of the time, are local. Look there first, because looking is cheap.

**Sometimes the arrow points the other way.** People with long-term knee pain at the front of the knee are often found to have weaker hip muscles, and for years the natural reading was that weak hips cause the knee pain: a hurt far from the break. When researchers followed people *forwards* (Rathleff and colleagues, 2014, pooling the studies), weak hips did not predict who would later develop the knee pain. The weakness may be a *result* of the pain, not its cause. Tracing upstream found a real link and read its direction wrong. The test that settled it was about time: which came first?

**Sometimes everything seems connected.** Once you have learned that pain can travel, it is tempting to see a distant cause behind every symptom, and to go on hunting long after the answer was in front of you. A good tracer carries a stopping rule.

So here is the decision, written as a test.

| Evidence | Points to |
|---|---|
| A clear local cause (you know what hit it) | here |
| The local fix works and stays fixed | here |
| The symptom comes back after every local fix | upstream |
| Nothing local explains it | upstream |
| It sits at the end of a chain (last joint, last function, last step, lowest ceiling) | look upstream |
| It matches a known map (heart → arm, hip → knee, diaphragm → shoulder) | look upstream, urgently if it is the heart |
| Several symptoms share one upstream link | upstream, at that link |
| A candidate cause was found only *after* the symptom began | check which came first |

## 8. The method: walk the chain upstream

1. **Say exactly where it hurts.** The line number, the step, the joint, the drip. Precision here is what makes the rest possible.
2. **Draw the chain that delivers to that spot.** Which functions feed this one, which steps produced this line, which links hand force to this joint, which pipes run above this ceiling.
3. **Check the handovers, not the insides.** At each link ask only: *was what arrived here already wrong?* The first link that receives good input and sends out bad output is the break.
4. **Halve long chains.** Check the middle and keep the half that still contains the break; twenty checks cover a million links.
5. **Fix at the break.** Treating the symptom is sometimes right (painkillers while you wait, a `try` while you debug), but know that it is a bucket under the drip, not a plumber.
6. **Confirm the hurt goes away, and stays away.** If it comes back, you fixed a link, not *the* link. Go back to step 3.
7. **Make the next break hurt closer to where it happens.** An assertion at the handover, a check of units at the interface, a question to a friend before the snap. That is fail fast, for code and for people.

## Worked examples

### Example 1 — the pipeline

*Trigger: a crash inside a function whose own code looks right. Tool: check each handover, from the failure backwards.* §3: `top_student` fails on `row[1]`; the value it received was `None`; `load` passed on a `None`; `parse` produced it from `"Chen,absent"`. Fixed at `parse`, and made to refuse anything unexpected.

### Example 2 — the cliff

*Trigger: an impossible result (a negative discriminant) from a formula applied correctly. Tool: ask what question the result answers.* §4: $\Delta = -167$ says the ball is never 20 m *above* the start, which is true. The question should have placed the ground 20 m below: $s = -20$ gives $t = 4.07$ s.

### Example 3 — the ache that keeps coming back

A student's elbow aches after every basketball session. Rest helps for a week; then it returns.

*Trigger: a symptom that returns after every local fix, at the end of a chain. Tool: the decision table in §7, then the handovers of [[The Kinetic Chain]].* The local fix (rest) works only while the elbow is not used, so the load is still arriving from somewhere. The elbow is the last big link before the ball: ask what feeds it. Does the student shoot flat-footed, with legs straight and trunk still, so the arm does all the work? That is the question to take to a physiotherapist, who can examine what this card cannot. Note what the table does *not* license: guessing a diagnosis.

## Common Misconceptions (Teaching Notes)

### 1. "The fault is where the pain is"

Sometimes; not reliably. A third of heart attacks arrive without chest pain.

**Fix:** the five rows of the chain figure. In each, name the red box and the amber box.

### 2. "The line in the error message is the bug"

It is where the program noticed. `top_student` was correct.

**Fix:** run the lab and change `top_student`: the crash only moves. Then check the handovers.

### 3. "Always look upstream"

Most hurts are local, and some upstream links run backwards (the hip and the knee).

**Fix:** the decision table, and the question "which came first?"

### 4. "Treating the symptom is wrong"

It is often necessary; it is just not the repair. A bucket under the drip is sensible while you find the plumber.

**Fix:** step 5 of the method: know which you are doing.

## Honest edges

- **Not medical advice.** Referred-pain patterns are common, not universal, and the list here is teaching, not a checklist for self-diagnosis. Emergencies first; the questions afterwards, with a professional.
- **The kinetic-chain numbers are a model.** The 22 % and 47 % come from a simulated three-link arm in [[The Kinetic Chain]], not from measuring an athlete. The sports-medicine literature makes the same argument; its own often-quoted figure (a 20 % loss from hip and trunk needing a 34 % faster shoulder) is itself a calculation passed between reviews, not a measurement.
- **Displacement is an average.** The 2000 review shows the effect across many studies; it does not mean every sharp word is displaced, and it is no excuse for taking a bad day out on someone.
- **Chains are drawn by us.** Real systems are webs, and a break can have two causes. The chain is the simplest map that makes the trace possible; redraw it when the trace fails.

---

## Connections

- **Builds on:** [[God Syndrome]] — hurt is a signal worth keeping; this card reads it. [[The Kinetic Chain]] — the weak-link experiment in §5 is where this card's body half was measured. [[Forward Reading and Problem Discovery]] — a hunter traces causality; this card is tracing it backwards from a symptom.
- **Sibling:** [[When a Model Breaks]] — when a prediction fails, find which ingredient is missing with a test that tells the candidates apart; §7's "which came first?" is one such test. **Searching** *(not yet released)* — binary search, and `git bisect` for long chains of history. [[Learning as Verification]] — checking each handover is cheaper than redoing the work. [[Physical Quantities and Units]] — the Mars Climate Orbiter, a unit check that would have hurt on the ground instead of at Mars.

## Sources

- D. Purves et al., *Neuroscience*, 2nd ed. (2001), Box A "Referred pain" (NCBI Bookshelf NBK10967); X. Jin et al., "Referred pain: characteristics, possible mechanisms, and clinical management", *Frontiers in Neurology* 14 (2023) 1104817.
- J. G. Canto et al., "Prevalence, clinical characteristics, and mortality among patients with myocardial infarction presenting without chest pain", *JAMA* 283 (2000) 3223–3229; NHS, "Heart attack: symptoms".
- StatPearls: "Anatomy, thorax, phrenic nerves" (Kehr's sign); "Appendicitis"; "Slipped capital femoral epiphysis" (pain sites: knee 26 %).
- D. C. Perry, D. Metcalfe, M. L. Costa and T. Van Staa, "A nationwide cohort study of slipped capital femoral epiphysis", *Archives of Disease in Childhood* 102 (2017) 1132–1136 — median delay 161 days with knee pain, 20 with hip pain; M. J. Matava et al., *Journal of Pediatric Orthopaedics* 19 (1999); M. S. Kocher et al., *Pediatrics* 113 (2004).
- M. S. Rathleff et al., "Is hip strength a risk factor for patellofemoral pain? A systematic review and meta-analysis", *British Journal of Sports Medicine* 48 (2014); C. M. Powers, *JOSPT* 40 (2010) 42–51, for the upstream hypothesis it tested.
- Mars Climate Orbiter Mishap Investigation Board, *Phase I Report* (NASA, 10 November 1999).
- A. Zeller, "Causes and effects in computer programs" (AADEBUG 2003), and *Why Programs Fail*; J. Shore, "Fail fast", *IEEE Software* 21(5) (2004) 21–25.
- APA Dictionary of Psychology, "displacement"; A. Marcus-Newhall, W. C. Pedersen, M. Carlson and N. Miller, "Displaced aggression is alive and well: a meta-analytic review", *Journal of Personality and Social Psychology* 78 (2000) 670–689.
- `where-it-hurts-lab.py` — every line of program output quoted, run as printed; `where-it-hurts-figures.py` — the chain figure.
