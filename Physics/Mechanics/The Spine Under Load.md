---
chinese: 负重的脊柱 (fùzhòng de jǐzhù)
aliases:
  - Spine Under Load
  - Spinal Loading
  - Lumbar Disc Compression
prerequisites:
  - "[[Torque]]"
  - "[[Forces and Equilibrium]]"
  - "[[Centre of Mass]]"
  - "[[Density and Pressure]]"
  - "[[Stress, Strain and Young Modulus]]"
  - "[[The Kinetic Chain]]"
  - "[[The Man Who Weighed a Muscle]]"
leads_to: []
tags:
  - subject/physics
  - domain/mechanics
  - domain/biomechanics
  - level/A-Level
  - level/enrichment
  - type/deep
  - type/application
  - type/cross-domain
  - type/hands-on
  - notation/disc-compression
  - misconception/squatting-always-protects-the-back
  - misconception/weight-matters-more-than-distance
  - misconception/sitting-is-always-worse-than-standing
  - misconception/the-model-is-the-body
  - misconception/a-worn-disc-on-a-scan-means-pain
---

# The Spine Under Load 负重的脊柱

> In 1680 Giovanni Borelli worked out what a porter's back carries. The man bends under 120 pounds on his neck, and the lowest disc of his spine, Borelli calculated, is pressed with 1239 pounds: about 4.1 kN, the weight of 420 kg, on a piece of tissue the size of a biscuit.
>
> Three hundred years later the American workplace guideline for lifting says that above 3.4 kN on that disc, the risk of injury goes up. Borelli's porter was over it. How did a man with a pair of dividers get so close, and what does the same calculation say about the bag on your shoulder, the box you lift and the phone in your hand?

## Try it before you read on

Three experiments, a few minutes each. The sections below explain what you feel.

1. **The bag of books.** Hold a bag of books against your stomach for 30 seconds. Then hold the same bag at arm's length in front of you for 30 seconds. Notice *where* you feel the difference.
2. **Morning and evening.** Stand against a door frame first thing in the morning and have someone mark your height with a pencil on a sticky note. Do it again before bed. Measure the gap.
3. **One bag or two.** Carry a full shopping bag in one hand for a minute, then split the same shopping into two bags, one in each hand. Notice which side of your waist works in the first case.

## Definition

### Formal

The spine is a column of 24 vertebrae separated by **intervertebral discs**. Near its base, the disc between the last lumbar vertebra and the sacrum (**L5/S1**) is where the moments of the whole upper body are balanced. Treated as a static problem in the plane of the body:

1. **The pivot.** The disc is the fulcrum.
2. **The load.** The weight of the head, arms and trunk, and anything held, acts at horizontal distances in front of the disc.
3. **The effort.** The back muscles (erector spinae) act about 5 cm *behind* the disc, roughly parallel to the spine.
4. **Equilibrium.** Moments about the disc balance, so the muscle force is the load's moment divided by 5 cm. Forces along the spine add up to the **compression** on the disc; forces across it add up to the **shear**.
5. **The disc as a vessel.** The compression is carried by a gel-filled core under pressure, held in by rings of fibre: pressure $\approx 1.5\,F/A$ for a disc of area $A$.

### Intuitive

A tower crane can lift a heavy load far out on its long arm only because a massive counterweight sits on the short arm behind the mast. Your spine is a crane built the wrong way round: the load is on the long arm, far in front, and the counterweight, your back muscles, sits on an arm only 5 cm long. So the muscles must pull many times harder than the load weighs, and every newton of that pull presses straight down through the mast, which is your disc.

### 中文锚点

从汽车后备箱里拎出一袋 10 公斤的大米，感觉比把同一袋米抱在怀里重得多，而最先察觉到的，是你的腰。原因是一根杠杆。脊柱最下面的那个关节是支点；米袋拎在手里，探出后备箱的边沿悬在外面，在支点前方大约 40 厘米处往下拽；而要把你撑住的背部肌肉，只在支点后方大约 5 厘米的地方。要平衡 40 厘米外的重量，5 厘米处的肌肉就得用米袋重量八倍的力去拉，而这股拉力全部压在两节椎骨之间的椎间盘上。把米袋贴着肚子抱住，同样一袋米，腰上的负担只剩一小部分。所以，东西离身体多远，比它有多重更要紧；"东西贴身拿"是搬东西的规矩里，唯一真正属于物理的那一条。

### 术语对照

| 中文 | English | Meaning here |
|---|---|---|
| 椎间盘 | intervertebral disc | the pad between two vertebrae; the pivot of the lever |
| 腰椎 | lumbar spine | the five vertebrae of the lower back, L1 to L5 |
| 竖脊肌 | erector spinae | the back muscles; the effort, about 5 cm behind the disc |
| 压力 / 剪切力 | compression / shear | force along the spine / force across it |
| 髓核 / 纤维环 | nucleus / annulus | the gel core / the rings of fibre that hold it |
| 蠕变 | creep | slow deformation of tissue held under a steady load |

## 1. The lever at the base of the spine

Take a 70 kg adult. About 37.5 kg of them, the head, arms and trunk, sits above the base of the spine, with its centre of mass 0.28 m up the trunk from the L5/S1 disc. The trunk leans forward at an angle $\theta$ from upright, and the hands hold a box of mass $m$ at a horizontal distance $d$ in front of the disc. The back muscles pull with force $F_m$ at $e = 0.05$ m behind it.

*Tool: the principle of moments, from [[Forces and Equilibrium]]. Trigger: a body held still, with forces at known distances from one joint.*

$$F_m\, e = W_u\, r \sin\theta + m g\, d \quad\Longrightarrow\quad F_m = \frac{W_u\, r \sin\theta + m g\, d}{e}$$

Resolve along and across the trunk. The muscle pulls along it; the weights have a part along it and a part across it:

$$\boxed{\,C = F_m + (W_u + mg)\cos\theta\,}\qquad \boxed{\,S = (W_u + mg)\sin\theta\,}$$

The single number that runs this whole card is $1/e = 20$ per metre. **Every newton-metre of load costs 20 newtons of muscle, and all of it lands on the disc.** For a 20 kg box, every 10 cm further out adds $20 \times 9.81 \times 0.10 / 0.05 = 392$ N, about 0.4 kN.

![[spine-under-load-lift.svg|760]]
*Left: disc compression against trunk angle for a 20 kg box, from the model `spine-under-load-model.py`. The red stoop curve kinks at 15° where the hanging box finally moves out past 12 cm. Right: at any fixed trunk angle, compression climbs in a straight line with the box's distance. The dashed line is the 3.4 kN workplace guideline.*

![[spine-under-load.mp4]]
*The same model, moving: bend over with straight legs, then squat with the box close, then squat but reach. The bars are the model's muscle force and disc compression for each frame.*

## 2. Stoop, squat, and what actually matters

Everyone is told to "lift with your legs". The model says what that rule gets right and where it is only a proxy.

| Lift, 20 kg box | Trunk | Box distance | Muscle | Compression |
|---|---|---|---|---|
| Stoop: legs straight, box hanging | 90° | 45 cm | 3.8 kN | **3.8 kN** |
| Squat, box held close | 30° | 25 cm | 2.0 kN | **2.5 kN** |
| Squat, but box at arm's length | 30° | 45 cm | 2.8 kN | **3.3 kN** |
| Upright, box hugged | 0° | 10 cm | 0.4 kN | **1.0 kN** |

The third row is the lesson. The same squat, with the box out where the stoop had it, gives almost the stoop's load back. **The knees did not save the back; the distance did.** Bending the knees helps when, and because, it lets you bring the load closer.

The laboratory evidence says the same. A 1999 review of biomechanical studies (van Dieën, Hoozemans and Toussaint) found no significant difference between stooping and squatting in measured disc pressure or in how much the spine shrank, and modelled compression that was equal or *higher* in the squat, lower only when the load could sit between the feet. Its verdict: the literature "does not provide support for advocating the squat technique" as such. What it did find lower in the squat was shear and the bending of the spine itself, which is §4's subject.

## 3. The disc as a pressure vessel

A disc is not a solid pad. At its centre is the **nucleus**, a gel that is mostly water; around it is the **annulus**, many layered rings of tough fibre wound at alternating angles, like the hoops of a barrel. Squeeze the disc and the gel's pressure rises; the rings stretch round it and hold it in. It is a pressure vessel, the same physics as a tyre or a blood vessel from [[Density and Pressure]].

In 1999 Hans-Joachim Wilke and colleagues put a pressure sensor into the L4–L5 disc of one healthy 70 kg volunteer and recorded it through a day of ordinary life. Some of the numbers:

| Posture | Pressure (MPa) |
|---|---|
| Lying on the back | 0.10 |
| Standing, relaxed | 0.50 |
| Sitting, relaxed, no backrest | 0.46 |
| Sitting slouched in a chair | 0.27 |
| Standing, bent forward | 1.10 |
| Holding 20 kg close to the body | 1.10 |
| Holding 20 kg 60 cm out from the chest | 1.80 |
| Lifting 20 kg, knees bent | 1.70 |
| Lifting 20 kg, back rounded | 2.30 |

For comparison, a car tyre runs at about 0.23 MPa. Lifting with a round back, the gel in the middle of your disc is at ten times that.

To turn pressure into force, Alf Nachemson, who first measured it in the 1960s, divided by 1.5 (the gel's pressure is higher than the average stress over the whole disc) and multiplied by the area:

$$F = \frac{P A}{1.5} = \frac{2.30 \times 10^6 \times 18 \times 10^{-4}}{1.5} = 2.76\ \text{kN}$$

That is the round-back lift, measured: under the guideline, but not by much.

**Science that disagrees with itself.** Nachemson's measurements, across more than a hundred people over twenty years, found sitting unsupported loads the disc about 40 % more than standing. That result is why a generation was told sitting is bad for the back. Wilke found relaxed sitting slightly *lower* than standing (0.46 against 0.50 MPa) and blamed the difference on the sensors. A 1999 study of eight people (Sato and colleagues) found sitting higher again. The honest summary: sitting and standing load the disc about the same, and *how* you sit (slouched against a backrest, 0.27; straightened hard, 0.55) matters more than whether you sit.

## 4. Shear and the twist

**Shear.** The weights' component *across* the disc tries to slide one vertebra forward over the next. In the model, the fully stooped lift gives $S = 564$ N. A 2012 review of the spine's tolerance (Gallagher and Marras) recommends keeping shear under 1000 N for occasional lifts and under 700 N for lifts done a hundred times a day or more. But shear is exactly where a one-muscle model fails worst: the deep back muscles run at an angle and can pull backward across the disc when the spine is held in its natural curve, and lose that ability when it is fully rounded. In one classic comparison (McGill and Norman, 1987), replacing the single muscle with a realistic set of fibres flipped the shear from more than 500 N forward to under 200 N backward. The model can tell you shear exists; it cannot tell you its size.

**The twist.** Hold the same 20 kg box at 30° of lean and 25 cm in front, then swing it 25 cm to one side. The moment now has a sideways part, balanced by the muscles on the opposite side of the waist, which also pull down on the disc:

$$C = \frac{M_\text{forward}}{e} + \frac{M_\text{sideways}}{e_\text{side}} + (W_u + mg)\cos\theta = 2.50\ \text{kN} \;\to\; 3.48\ \text{kN}$$

That is before the body's real response. In a twist the muscles on both sides fire together to keep the spine stable (co-contraction), and measurements put the extra load at up to 25 % in side-bending (Marras and Granata, 1997) and twisting while moving at twice the load of the same effort held still (1995). Twisting while bent over, with a load out to the side, stacks every factor in this card at once.

## 5. One bag or two

Walk upright with a 30 kg load. Split into 15 kg in each hand, the two hands' sideways moments cancel and the disc carries only the weights. All in one hand, the load is 22 cm to the side, and the muscles on the *other* side of the waist must balance it from about 5 cm away:

$$F_\text{side} = \frac{30 \times 9.81 \times 0.22}{0.05} = 1.3\ \text{kN}$$

![[spine-under-load-carry-neck.svg|760]]
*Left: 30 kg carried two ways, measured and modelled. Right: the head bowed forward. The moment (blue, left axis) is plain mechanics; the load it causes (right axis) depends on whose model you believe.*

Stuart McGill and colleagues measured this in 2013. With 30 kg in one hand, compression exceeded 2800 N; with 15 kg in each hand it was 1570 N, 44 % less. They also found that 30 kg in *each* hand, twice the total, loaded the spine less than 30 kg in one. The model gets the direction right and underestimates both numbers, because walking is not standing still and the muscles on both sides work at once. A rucksack on both straps is the everyday version of the second bar; the bag slung on one shoulder is the first.

## 6. The neck: a bowed head

The same lever sits at the base of the neck. The head and neck weigh about 8 % of the body, 5.7 kg for a 70 kg adult, with their centre of mass about 16 cm above the lowest neck joint. Bow the head forward by $\phi$ and its moment about that joint is

$$M = m g\, r \sin\phi = 5.7 \times 9.81 \times 0.16 \times \sin\phi$$

zero upright, 4.5 N m at 30°, 6.3 N m at 45°. That part is certain. The neck muscles, a few centimetres behind the joint, must supply it, and the load on the neck rises with it. By how much is where the models disagree:

- A 2014 computer model by Kenneth Hansraj, widely quoted, gives the neck an effective load of 27 lb at 15°, 40 lb at 30°, 49 lb at 45° and 60 lb at 60°: about 4.5 times upright at 45°.
- A 2020 model driven by measured muscle signals (Barrett and colleagues) found compression rose only about 1.6 times at 45°.
- A one-muscle model with an assumed 4 cm arm gives 3.5 times.

What people actually do: in one study of 18 smartphone users the head was held 33° to 45° forward from vertical, most when texting sitting down. The honest conclusion is the certain one: bowing the head multiplies the work the neck muscles do many times over, and they do it for as long as you look down. Nobody has yet shown a simple number for what that does to the discs.

## 7. Creep: the load you hold, not the one you lift

Tissue held under a steady load keeps deforming slowly. This is **creep**, the slow side of [[Stress, Strain and Young Modulus]]: the disc's gel is squeezed and water seeps out through its walls. You measure it with a door frame.

![[spine-under-load-creep.svg|760]]
*Height lost through a day and recovered through a night. Tyrrell, Reilly and Troup (1985) measured the points: 19.3 mm a day, 54 % of it in the first hour after rising, 80 % by three hours, and about 70 % regained in the first half of the night. The curve is two exponentials fitted to those points in `spine-under-load-model.py`.*

The shape is the one from [[Differential Equations]]: the rate of loss is proportional to how far the disc still has to go, $\dfrac{dh}{dt} = \dfrac{h_\infty - h}{\tau}$, so most of the change comes early. Lying down, the load drops to a fifth and the discs drink back overnight; in Wilke's volunteer the pressure rose from 0.10 to 0.24 MPa across seven hours of sleep as the disc swelled. In space, with no load at all, astronauts grow up to 3 % taller.

Two consequences follow.

- **The first hour is different.** A disc full of water after a night is stiffer in bending: one laboratory study (Adams, Dolan and Hutton, 1987) estimated bending stresses on discs about 300 % higher in the early morning. In a randomised trial (Snook and colleagues, 1998), people with chronic low back pain who avoided bending forward in the first hours after rising reported significantly less pain.
- **Posture held is posture loaded.** A slouch held for an hour creeps; changing position lets the tissue recover. The best posture, in the sense that the evidence supports, is the next one.

## 8. What the one-muscle model gets wrong

Every number in this card so far came from one muscle 5 cm behind one joint. Here is that model against the measured disc.

![[spine-under-load-pressure.svg|760]]
*Wilke's measured pressures (grey) against the model with its muscle at 5 cm (purple) and at 7.5 cm (green). Light loads are underestimated, heavy ones overestimated, and the order is right every time.*

- **It underestimates light loads.** Standing relaxed, the model gives 0.31 MPa and the disc reads 0.50. Real muscles are never fully off; front and back work together to hold you upright. Models that ignore this co-contraction can underestimate compression by as much as 45 % (Granata and Marras, 1995).
- **It overestimates heavy ones.** Lifting with a round back, the model gives 3.19 MPa against 2.30 measured. A realistic set of back-muscle fibres gives up to 35 % less compression than the single muscle, as if the one muscle sat 7.5 cm back instead of 5 (McGill and Norman, 1987). The green bars show that change: closer for heavy lifts, worse for light ones.
- **It knows nothing about shear direction, ligaments, pressure in the abdomen, speed or fatigue.**

What survives is the *comparison*. Every ranking in this card (close beats far, two bags beat one, level lifts beat twisted ones) is the same in the model and in the measurements. Use a one-muscle model to compare two ways of doing a job. Do not use it to certify that a job is safe.

## 9. What this means for a body

- **Keep the load close.** It is the one rule every model and measurement agrees on, and the reason is the $1/e$ in §1.
- **Split and centre what you carry.** Two bags, two straps.
- **Don't twist and bend under a load at the same time.** Turn with your feet.
- **Be gentle with your back in the first hour after getting up**, and change position often during a long sitting.
- **Mind the long bowed head.** Raise the screen rather than lower the head.

And the honest part, which matters as much. Training workers in lifting technique has not been shown to prevent back pain (a 2011 Cochrane review of nine trials and over 20,000 employees). Back belts did not reduce injury claims or back pain in a study of 13,873 workers in 160 stores (Wassell and colleagues, 2000). And scans of people with *no* back pain find worn discs in 37 % of 20-year-olds and 96 % of 80-year-olds (Brinjikji and colleagues, 2015): a disc that looks worn on a scan is often not where the pain is coming from, which is [[Where It Hurts Might Not Be Where It Broke]] in its purest form. The physics tells you where the loads go. It does not diagnose a back. Pain that stays, pain down a leg, numbness or weakness needs a doctor.

## Worked examples

### Example 1 — the stooped lift

*Trigger: a body held still with forces at known distances from one joint. Tool: moments about the joint, then resolve along the trunk.* Trunk level ($\theta = 90°$), 20 kg box 0.45 m out:

$$\tau = (37.5 \times 9.81)(0.28) + (20 \times 9.81)(0.45) = 103 + 88 = 191\ \text{N m},\qquad F_m = \frac{191}{0.05} = 3.8\ \text{kN}$$

With $\cos 90° = 0$, compression is the muscle force alone, 3.8 kN, over the 3.4 kN guideline; shear is $(368 + 196) = 564$ N. Pressure $= 1.5 \times 3826 / (18 \times 10^{-4}) = 3.2$ MPa (measured in a real disc for a similar lift: 2.3 MPa; see §8).

### Example 2 — the same box, squatting

*Trigger: the same lever with a new angle and distance. Tool: the same two boxed equations.* $\theta = 30°$, box 0.25 m out:

$$\tau = 368 \times 0.28 \sin 30° + 196 \times 0.25 = 51.5 + 49 = 101\ \text{N m},\quad F_m = 2.0\ \text{kN},\quad C = 2011 + 564 \cos 30° = 2.5\ \text{kN}$$

Push the box out to 0.45 m in the same squat: the load term becomes 88 N m, $F_m = 2.8$ kN, $C = 3.3$ kN. Almost all of the saving came from the 20 cm, not the knees.

### Example 3 — Borelli's porter, checked

*Trigger: a historical claim with numbers and a known unit. Tool: unit conversion, then compare with the guideline.* Borelli gives 1239 pounds on the lowest disc. The Roman pound was about 339 g: $1239 \times 0.339 \times 9.81 = 4.1$ kN. His method (moments about each vertebra, muscles a short distance behind) is §1's; his number is above the modern guideline and in the range a modern single-muscle model gives for a heavy load carried bent over. He could not measure the disc; three centuries later Nachemson and Wilke could, and found his kind of model overestimates heavy loads, exactly as §8 says.

### Example 4 — from pressure to force, and back

*Trigger: a measured pressure and a known area. Tool: $F = PA/1.5$.* Wilke's volunteer standing relaxed: $0.50 \times 10^6 \times 18 \times 10^{-4} / 1.5 = 600$ N on the disc, about 0.86 of his whole body weight, though only about half of it sits above the disc. The rest is the muscles holding him up, the co-contraction that the one-muscle model leaves out and §8 measured.

### Example 5 — the one-handed bag

*Trigger: a load offset to one side of the spine. Tool: moments in the side-to-side plane.* 20 kg in one hand, 0.22 m out: $M = 20 \times 9.81 \times 0.22 = 43$ N m, side muscles $43/0.05 = 863$ N, compression $368 + 196 + 863 = 1.4$ kN. Split into 10 kg each side: the moments cancel and $C = 368 + 196 = 0.56$ kN. Same shopping, less than half the load.

## Common Misconceptions (Teaching Notes)

### 1. "Bend your knees and your back is safe"

The knees help only if they bring the load closer. A squat with the box at arm's length loads the disc almost as much as a stoop.

**Fix:** §2's table, third row, and the last chapter of the video.

### 2. "Heavier is what hurts"

Weight matters; distance matters more, because the muscle multiplies it by $d/e$. A 10 kg bag at 40 cm costs more than a 20 kg bag hugged at 10 cm.

**Fix:** the bag-of-books experiment, then the right panel of the lift figure.

### 3. "Sitting is worse for the back than standing"

The classic measurement said so; the later one did not. Sitting and standing load the disc about the same; slouching against a backrest loads it least.

**Fix:** §3, the disagreement, with the three studies side by side.

### 4. "The model says 3.8 kN, so the disc feels 3.8 kN"

The model is a ranking tool that is wrong by up to 40 % in either direction.

**Fix:** the pressure figure in §8, and the question it teaches: which way is this model biased here, and why?

### 5. "A worn disc on a scan is the cause of the pain"

Worn discs are common in people with no pain at all.

**Fix:** the Brinjikji numbers in §9, and [[Where It Hurts Might Not Be Where It Broke]].

## Exam Notes

No board on file examines the spine. The syllabuses for Cambridge 0625 and 9702, the IB Physics guide and the AP Physics 1, 2 and C: Mechanics course descriptions contain no mention of the spine, discs, posture or lifting; the only mention of muscles in any of them is the eye's lens muscles in AP Physics 2. Every tool used here is examined, and the boards and rows for each are in the Exam Notes of:

| Tool | Exam Notes in |
|---|---|
| Moments, levers, equilibrium of a rigid body | [[Forces and Equilibrium]], [[Torque]] |
| Resolving forces along and across a line | [[Forces and Equilibrium]] |
| Centre of mass of a composite body | [[Centre of Mass]] |
| Pressure as force per area | [[Density and Pressure]] |
| Stress, strain and the behaviour of materials under load | [[Stress, Strain and Young Modulus]] |
| Exponential approach to equilibrium | [[Differential Equations]] |

A body held still with a load is a favourite setting for moment questions on 0625, 9702 and AP Physics 1 (a forearm holding a ball, a person on a plank). The examples here are good practice for those questions, with the added step of asking what the answer means.

## Connections

- **Parents:** [[Torque]] and [[Forces and Equilibrium]], the lever and the resolution; [[Density and Pressure]] for the disc; [[Stress, Strain and Young Modulus]] for creep.
- **The same lever, moving:** [[The Kinetic Chain]], whose Example 4 was the first lift in this card and whose weak-link section shows load passing down a chain.
- **The same lever, 1680:** [[The Man Who Weighed a Muscle]], Borelli's Proposition LXI.
- **Reading pain:** [[Where It Hurts Might Not Be Where It Broke]], for why a scan and a pain need not agree.
- **Springs in the body:** [[Tendons as Springs]].
- **The curve of creep:** [[Differential Equations]].

## Sources

- H.-J. Wilke, P. Neef, M. Caimi, T. Hoogland, L. E. Claes, "New in vivo measurements of pressures in the intervertebral disc in daily life", *Spine* 24 (1999) 755–762, Table 1.
- A. Nachemson, *Acta Orthopaedica Scandinavica* (1965), for the load as pressure divided by 1.5 times area; A. Nachemson, "Disc pressure measurements", *Spine* 6 (1981) 93–97; K. Sato, S. Kikuchi, T. Yonezawa, *Spine* 24 (1999); M. Dreischarf et al. (2013) on the conversion's error, up to 44 %.
- T. R. Waters, V. Putz-Anderson, A. Garg, L. J. Fine, "Revised NIOSH equation for the design and evaluation of manual lifting tasks", *Ergonomics* 36 (1993) 749–776: 3.4 kN, 23 kg.
- S. Gallagher, W. S. Marras, "Tolerance of the lumbar spine to shear: a review and recommended exposure limits", *Clinical Biomechanics* 27 (2012).
- J. H. van Dieën, M. J. M. Hoozemans, H. M. Toussaint, "Stoop or squat: a review of biomechanical studies on lifting technique", *Clinical Biomechanics* 14 (1999) 685–696.
- S. M. McGill, R. W. Norman, "Effects of an anatomically detailed erector spinae model on L4/L5 disc compression and shear", *Journal of Biomechanics* 20 (1987); K. P. Granata, W. S. Marras (1995, 2000); W. S. Marras, K. P. Granata (1995, 1997); W. S. Marras, K. G. Davis (1998).
- S. M. McGill, L. Marshall, J. Andersen, "Low back loads while walking and carrying", *Ergonomics* 56 (2013) 293–302.
- D. A. Winter, *Biomechanics and Motor Control of Human Movement*, Table 4.1: segment mass fractions.
- K. K. Hansraj, "Assessment of stresses in the cervical spine caused by posture and position of the head", *Surgical Technology International* 25 (2014); J. M. Barrett et al. (2020); S. Lee et al. (2015) on smartphone head angles.
- P. Tyrrell, T. Reilly, J. D. G. Troup, "Circadian variation in stature and the effects of spinal loading", *Spine* 10 (1985); M. A. Adams, P. Dolan, W. C. Hutton, *Spine* 12 (1987); S. H. Snook et al., *Spine* 23 (1998); NASA, spinal ultrasound investigation.
- J. H. Verbeek et al., Cochrane review on manual handling advice (2011); J. T. Wassell et al., *JAMA* 284 (2000) on back belts; W. Brinjikji et al., *American Journal of Neuroradiology* 36 (2015) on imaging findings in people without pain.
- G. A. Borelli, *De Motu Animalium* (1680–81), Proposition LXI.
- `spine-under-load-model.py`, `spine-under-load-figures.py`, `spine-under-load-manim.py` — every number, figure and frame, recomputed.

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $F_m e = W r \sin\theta + mgd$ | `F_m e = W r \sin\theta + mgd` | Moments about the disc |
| $C = F_m + W\cos\theta$ | `C = F_m + W\cos\theta` | Compression along the spine |
| $S = W\sin\theta$ | `S = W\sin\theta` | Shear across it |
| $P \approx 1.5\,F/A$ | `P \approx 1.5\,F/A` | Disc pressure from force |
| $\dfrac{dh}{dt} = \dfrac{h_\infty - h}{\tau}$ | `\dfrac{dh}{dt} = \dfrac{h_\infty - h}{\tau}` | Creep toward a new length |
