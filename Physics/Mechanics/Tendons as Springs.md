---
chinese: 肌腱是弹簧 (jījiàn shì tánhuáng)
aliases:
  - Tendons as Springs
  - Elastic Energy in Tendons
  - Spring-Mass Model of Running
prerequisites:
  - "[[Stress, Strain and Young Modulus]]"
  - "[[Hooke's Law for Springs]]"
  - "[[Simple Harmonic Motion]]"
  - "[[Work, Energy and Power]]"
  - "[[The Kinetic Chain]]"
leads_to: []
tags:
  - subject/physics
  - domain/mechanics
  - domain/biomechanics
  - domain/materials
  - level/A-Level
  - level/enrichment
  - type/deep
  - type/application
  - type/cross-domain
  - type/derivation
  - type/hands-on
  - notation/leg-stiffness
  - misconception/tendons-are-just-ropes
  - misconception/a-stiffer-tendon-stores-more-energy
  - misconception/the-leg-spring-is-all-tendon
  - misconception/tendons-strengthen-as-fast-as-muscles
---

# Tendons as Springs 肌腱是弹簧

> In 1973 two physiologists put kangaroos on a treadmill and measured how much oxygen they used. Hopping at 7 km/h, then 10, then 15, then 22, the kangaroos went faster and faster, and their oxygen use did not go up. It went slightly down.
>
> Every other animal on a treadmill pays more to go faster. The kangaroo had found a way round it, and so, to a smaller degree, have you. The trick is a material in your legs that stretches like a spring and hands back almost all the energy you put into it.

## Try it before you read on

1. **Balls of the feet or heels.** Skip with a rope for thirty seconds on the balls of your feet, then thirty seconds landing on your heels. Which is harder, and where do you feel it?
2. **Your own resonance.** Hop in place on both feet as easily as you can for ten seconds and count the hops. Then try to hop much faster or much slower. Notice that one rhythm feels effortless and the others do not.
3. **The rubber band.** Stretch a thick rubber band hard, hold it against your lip, and let it relax. It feels warm when stretched. Some of the energy you put in comes back as heat, not motion: that is §3.

## Definition

### Formal

A **tendon** connects muscle to bone. It is made of parallel fibres of **collagen**, each gently crimped (wavy) when unloaded. As a material under tension:

1. **The toe region.** At small strains, up to about 2 % (up to 4 % in some tendons measured in living people), the stress–strain curve bends upward: stiffness rises as more fibres straighten and take load.
2. **The linear region.** Beyond it, stress is proportional to strain. The slope, the **Young modulus**, is about 1.2 GPa for tendon fibres across many species; the whole living human Achilles tendon measures lower, 0.4 to 0.8 GPa.
3. **Failure.** Excised human Achilles tendon fails at about 70 to 90 MPa and 7.5 to 10 % strain.
4. **Hysteresis.** Unloading follows a lower curve than loading. The area between them is energy turned into heat: about 7 to 9 % for an isolated tendon.
5. **As a spring.** A tendon of area $A$ and length $L$ in the linear region has spring constant $k = EA/L$ and stores $U = \tfrac12 F^2/k$.

A runner's whole leg, in turn, behaves like a spring: the **spring-mass model** treats the body as a point mass bouncing on a massless spring leg.

### Intuitive

A rope made of a thousand threads, each tied in with a slightly different amount of slack. Pull gently and only the tightest threads take the load, so the rope feels soft. Pull further and more threads go taut, so it stiffens. Once every thread is taut, it stretches in a straight line, like any spring. Let go, and it springs back with nearly everything you put in.

### 中文锚点

一分钟跳绳测试里，跳得好的同学都用前脚掌一下一下地弹，而且能坚持的时间，远远超过光靠小腿肌肉能撑住的。秘诀在跟腱，就是脚踝后面那根粗粗的"筋"。每次落地，你的体重把它拉长大约一厘米，就像把弹簧跳跳杆往下一压；紧接着它弹回来，又把你送上去。小腿肌肉主要只是绷紧，好让跟腱去完成拉长和回弹；而单是一根跟腱，就能把存进去的能量还回来九成以上。换成用脚后跟落地，就没有弹簧可以拉了：每一跳都得由肌肉从头出力，所以用脚后跟跳绳会觉得又沉又震。肌腱不只是把肌肉拴在骨头上的一根绳子，它是长在你腿里的一根弹簧。

### 术语对照

| 中文 | English | Meaning here |
|---|---|---|
| 肌腱 / 跟腱 | tendon / Achilles tendon | the collagen cord joining muscle to bone / the one at the heel |
| 胶原纤维 | collagen fibre | the strands a tendon is made of, crimped when relaxed |
| 趾区 | toe region | the curved start of the stress–strain graph |
| 弹性滞后 | hysteresis | loading and unloading follow different curves; the gap is heat |
| 腿刚度 | leg stiffness | peak leg force ÷ how much the leg shortens |
| 触地时间 | contact time | how long the foot is on the ground in one step |

## 1. Where the toe comes from

Why does tendon's stress–strain graph curve upward before it goes straight? The crimp gives an answer that can be derived, not just described.

*Tool: add up the fibres. Trigger: a material made of many parallel strands that do not all start taut.*

**Step 1.** Model the tendon as many identical parallel fibres. Each has its own slack $s$: it carries nothing until the tendon's strain $\varepsilon$ exceeds $s$, then obeys Hooke's law, carrying stress $E(\varepsilon - s)$.

**Step 2.** Suppose the slacks are spread evenly between $0$ and $\varepsilon_t$. The tendon's stress is the average over all fibres:
$$\sigma(\varepsilon) = \frac{1}{\varepsilon_t}\int_0^{\varepsilon_t} E\,\max(\varepsilon - s,\, 0)\,ds.$$

**Step 3.** If $\varepsilon < \varepsilon_t$, only fibres with $s < \varepsilon$ are taut:
$$\sigma = \frac{E}{\varepsilon_t}\int_0^{\varepsilon}(\varepsilon - s)\,ds = \frac{E\varepsilon^2}{2\varepsilon_t}.$$

**Step 4.** If $\varepsilon \ge \varepsilon_t$, every fibre is taut:
$$\sigma = \frac{E}{\varepsilon_t}\int_0^{\varepsilon_t}(\varepsilon - s)\,ds = E\left(\varepsilon - \frac{\varepsilon_t}{2}\right).$$

$$\boxed{\;\sigma(\varepsilon) = \begin{cases} \dfrac{E\varepsilon^2}{2\varepsilon_t}, & \varepsilon < \varepsilon_t \quad\text{(toe: a parabola)}\\[2ex] E\left(\varepsilon - \dfrac{\varepsilon_t}{2}\right), & \varepsilon \ge \varepsilon_t \quad\text{(linear, slope } E)\end{cases}}$$

At $\varepsilon = \varepsilon_t$ both pieces give $E\varepsilon_t/2$ and both have slope $E$, so the curve joins smoothly. The toe is a parabola, and it is a parabola *because* fibres are being recruited at a steady rate.

![[tendons-curve.svg|760]]
*Left: the derived curve (line) against 2000 individual fibres with random slack, added up in `tendons-model.py` (dots): they agree to 0.04 MPa. Right: the fraction of fibres taut. The crimp is real: in mouse tendon, the waviness of the fibres was seen to fall as the toe region was loaded (Miller and colleagues, 2012).*

## 2. Stiff and nearly perfect

With $E = 1.2$ GPa, a tendon at 4 % strain is under $1.2 \times 10^9 \times (0.04 - 0.01) = 36$ MPa. That is stiff: a steel wire is about 170 times stiffer, a rubber band ten to a hundred times softer. Tendon sits where a spring in a leg needs to be: stiff enough to transmit a muscle's force without flopping, stretchy enough to store energy in a centimetre of give.

**As a spring.** Treat the Achilles tendon in its linear region as a spring with $A \approx 65$ mm² and $L \approx 0.20$ m:

$$k = \frac{EA}{L} = \frac{1.2\times10^9 \times 65\times10^{-6}}{0.20} = 3.9\times10^5\ \text{N m}^{-1}.$$

That is from the fibre modulus. Measured whole, a living Achilles tendon has the lower modulus of 0.4 to 0.8 GPa, so its $k$ is two to three times smaller.

**Stiffer does not mean more energy.** At a given force $F$, a spring stores $U = F^2/2k$: the *softer* spring stores more, because it stretches further. A very stiff tendon would hand the muscle's force on crisply but store little; a very soft one would store a lot but make the joint feel loose. Real tendons sit between.

## 3. The loop: where the rest goes

Stretch a tendon and release it, and the unloading curve runs slightly below the loading curve. The work done on the way up is the area under the top curve; the work returned on the way down is the area under the bottom one. The gap between them is **hysteresis**, and it is heat.

![[tendons-hysteresis.svg|760]]
*Left: an isolated tendon loses about 7 % per cycle (Ker, 1981: sheep, measured with the heat checked against a thermometer); across 18 mammal species the figure is about 9 % (Pollock and Shadwick, 1994). Right: measurements inside living human legs give 18 to 35 %, but the method is disputed and the true value is probably lower. The shape of each loop is illustrative; the losses are the measured ones.*

Ker's 1981 measurement is a lovely piece of physics: he stretched a tendon repeatedly and measured its temperature rise, and the heat matched the area of the loop. Energy the tendon did not give back had gone exactly where the first law of thermodynamics said it must. The same loop shape appears in [[Magnetism and Magnetic Materials]], where the lost energy heats a transformer core.

## 4. The Achilles tendon at work

A 2021 study (Kharazi and colleagues) measured the Achilles tendon directly in people running at 2.5 and 3.5 m/s: peak force 3.2 to 3.5 body weights, about 2.0 to 2.6 kN, and strain 4.0 to 4.9 %.

*Tool: stress = force ÷ area, then the derived curve of §1, then energy = area under it. Trigger: a measured force on a known cross-section.*

$$\sigma = \frac{2400}{65 \times 10^{-6}} = 37\ \text{MPa},\qquad \varepsilon = \frac{\sigma}{E} + \frac{\varepsilon_t}{2} = 0.031 + 0.010 = 4.1\ \%.$$

The model's 4.1 % sits inside the measured 4.0 to 4.9 %. The stretch is $0.041 \times 200 = 8$ mm, and the energy stored is about 7.6 J. The same study measured the tendon's recoil directly: **9.2 J per step at 2.5 m/s and 11.2 J at 3.5 m/s.**

Two honest details.

- **The older estimates were three times higher.** Models before direct measurement put the Achilles tendon's return at 28 to 39 J a step, and the classic 1987 study by Robert Ker and colleagues estimated that at 4.5 m/s the Achilles stored about 35 % of the energy lost and regained in each step, and the arch of the foot 17 %. Direct measurement at slower speeds gives about a third of the modelled joules. The spring is real; its size was overestimated.
- **The safety margin is thin.** Running stresses of 37 MPa against a failure stress of about 86 MPa give a safety factor of about 2.3, small next to the factor of 3 or more common in engineering. Paavo Komi measured forces as high as 9 kN in a living Achilles tendon in 1990, about 111 MPa, higher than the failure stress of excised tendon. Either living tendon is stronger than dead tendon, or the loading rate matters, or the measurement overestimates; the question is open.

## 5. A runner is a mass on a spring

Watch a runner from the side and ignore the details. The body lands, the leg shortens, the body is pushed back up. The **spring-mass model** takes that literally: a point mass on a massless spring leg of stiffness $k$, natural length $L_0$, with the foot pinned to the ground during contact.

Take a measured runner (Moore and colleagues, 2019): 65 kg at 12.7 km/h, leg stiffness 8.38 kN/m, contact time 0.247 s. `tendons-model.py` integrates the model through one symmetric stance, with a 0.90 m leg and an assumed landing speed of 0.7 m/s:

![[tendons-stance.svg|760]]
*Left: the vertical ground force, a smooth hump peaking at 2.5 body weights, with contact lasting 259 ms (measured: 247). Right: the energy ledger. Kinetic and gravitational energy flow into the leg spring as it shortens, peak at mid-stance, and flow back out.*

![[tendons-spring-runner.mp4]]
*The model, moving: three strides slowed fifteen times, with the leg drawn as a spring and the energy bars exchanging.*

**Why contact lasts longer than half a period.** It is tempting to say a bounce is half a cycle of [[Simple Harmonic Motion]], lasting $\pi\sqrt{m/k}$. It lasts longer, and SHM says by how much. Treat the vertical motion alone, with vertical stiffness $k_v$ (19.6 kN/m here, from peak force ÷ how far the body sinks).

*Tool: SHM about the equilibrium point, not about the landing point. Trigger: a spring that is at its natural length at the moment of contact.*

1. The spring's equilibrium, where it holds the body's weight, is $z_0 = mg/k_v = 65 \times 9.81 / 19\,600 = 3.25$ cm *below* the landing point.
2. So the landing happens 3.25 cm above the centre of oscillation, moving down at $v_0 = 0.7$ m/s. With $\omega = \sqrt{k_v/m} = 17.4$ rad s⁻¹, the amplitude is $A = \sqrt{z_0^2 + (v_0/\omega)^2} = \sqrt{3.25^2 + 4.03^2} = 5.18$ cm.
3. The foot is on the ground while the body is below the landing height: half a cycle below the centre, plus the two arcs between the landing height and the centre, each of angle $\arcsin(z_0/A)$:
$$t_c = \frac{\pi + 2\arcsin(z_0/A)}{\omega} = \frac{3.142 + 2(0.679)}{17.4} = 0.259\ \text{s}.$$

Half a period would be only 0.181 s. The formula gives exactly the 259 ms that the full two-dimensional model does. The contact is 43 % longer than half a cycle because the landing is a long way above the centre.

**Stiffness is something runners choose.** Asked to run at different stride frequencies at 2.5 m/s, runners changed their leg stiffness 2.3-fold, from 7.0 to 16.3 kN/m (Farley and González, 1996); on softer surfaces they stiffen their legs so that the body moves the same way (Ferris and colleagues, 1998). Experiment 2's effortless hopping rhythm is you choosing the stiffness that suits your legs.

**The leg spring is not all tendon.** At mid-stance the model's leg spring holds $\tfrac12 k (\Delta L)^2 = \tfrac12 \times 8380 \times 0.191^2 = 153$ J. The Achilles tendon, measured, returns about 10 J of it. The rest is muscles doing work, other tendons and ligaments, and the arch of the foot. When the arch was prevented from compressing in one experiment (Stearne and colleagues, 2016), running at 2.7 m/s cost 6.0 % more metabolic energy. The leg *behaves* like a spring; only part of it *is* one.

## 6. Slow in, fast out: springs amplify power

A muscle is limited in how fast it can do work. The most powerful muscles measured, a quail's flight muscles in a burst, produce about 400 W per kilogram of muscle. A spring has no such limit: stretch it slowly, release it suddenly, and $P = E/t$ can be huge because $t$ is tiny.

- **The flea.** A flea's jump needs $2.25 \times 10^{-7}$ J, delivered in 0.75 to 1.0 ms (Bennet-Clark and Lucey, 1967): $P = 2.25 \times 10^{-7} / 0.75 \times 10^{-3} = 0.30$ mW, from an animal weighing well under a milligram. No muscle could do that. The flea's muscles slowly compress a pad of **resilin**, a rubbery protein, which a catch holds; release the catch and the pad throws the flea off at about 1.3 m/s with an acceleration near 150 $g$ (Sutton and Burrows, 2011). Species that jump better have larger resilin pads.
- **Your jump.** In a squat jump, the muscle fibres of the calf shortened while the tendon stretched 6 % and stored 4.9 J, then released it with a higher peak power than the fibres could produce themselves (Kurokawa and colleagues, 2001). The dip before a jump in [[The Kinetic Chain]] §4 is the same catapult.
- **Landing, in reverse.** A spring can also *take in* energy faster than a muscle can absorb it, then let the muscle absorb it slowly: power attenuation. Landing from a jump, your tendons buy your muscles time.

## 7. The kangaroo

Terence Dawson and Richard Taylor's 1973 treadmill result, the one this card began with: from 7 to 22 km/h, a hopping kangaroo's oxygen use fell slightly as its speed rose, and above 18 km/h hopping was cheaper than running on four legs. The hop frequency hardly changed; the kangaroos went faster by taking longer hops. Two years later Robert McNeill Alexander and A. Vernon measured the forces (about 6 body weights) and estimated that elastic storage in the tendons saved about 40 % of the cost for a wallaby at moderate speed, and more at higher speeds. A kangaroo is a spring-mass model with a large, efficient spring.

## 8. Training a spring

Tendons adapt to load, but slowly and only to heavy load.

- A 2015 review of 27 studies (Bohm, Mersmann and Arampatzis) found training increased tendon stiffness mainly by changing the *material*, not by thickening it. Loads above 70 % of a maximal contraction worked (standardised effect 0.90); lighter ones did almost nothing (0.04). Fourteen weeks of training that stretched the tendon to 4.55 % strain increased its stiffness; the same training at 2.85 % did not (Arampatzis and colleagues, 2007).
- The core of an adult tendon is hardly renewed at all. Nuclear bomb tests in the 1950s and 60s left a spike of carbon-14 in everything alive; measured in adults' Achilles tendons, it showed that the tendon core is essentially not replaced after about the age of 17 (Heinemeier and colleagues, 2013). The surface adapts; the core you built as a teenager is the one you keep.
- Muscles strengthen faster than tendons stiffen. In adolescent volleyball players, tendon force was 33 % above that of untrained peers but tendon stiffness only 22 % higher, so their tendons were stretched further at maximum effort (8.0 % against 6.4 % strain) (Mersmann and colleagues, 2017).

## 9. Why tendons tear

A tendon working with a safety factor of 2 lives close to its limit, and it accumulates damage. Loaded repeatedly in the laboratory, tendon fails by **fatigue**: small damage builds up until it breaks, at stresses well below its one-pull strength (Ker, Wang and Pike, 2000). In a living body, repair normally keeps pace with routine damage. The trouble comes when load outruns repair, or muscle outruns tendon.

That is the pattern of Achilles ruptures. In Sweden they rose from 47 to 55 per 100,000 men a year between 2001 and 2012 (Huttunen and colleagues, 2014), with the authors pointing to older adults in demanding sports. In United States emergency departments, 82 % of ruptures happened during sport, the largest rise was in people aged 40 to 59, and basketball led the list (Lemme and colleagues, 2018). A strong muscle, a tendon whose core was built decades ago, and a sudden explosive push: the spring is asked for more than it has.

The physics suggests the direction: build load gradually, heavily enough to make the tendon adapt, and give it time. It does not examine a leg. Pain in a tendon that lasts, swelling, or a sudden snap and weakness needs a doctor or a physiotherapist.

## Worked examples

### Example 1 — stress at 3 % strain

*Trigger: a strain past the toe. Tool: the linear branch of §1.* $\sigma = 1.2 \times 10^9\,(0.03 - 0.01) = 24$ MPa. A straight line through the origin with the same slope would give 36 MPa: the toe "costs" half the toe strain, $\varepsilon_t/2 = 1$ %, for good.

### Example 2 — the Achilles as a spring

*Trigger: force, area and length of a tendon in its linear region. Tool: $k = EA/L$, then $U = F^2/2k$.* $k = 3.9 \times 10^5$ N m⁻¹; at 2400 N, $U = 2400^2 / (2 \times 3.9 \times 10^5) = 7.4$ J. With the living modulus of 0.6 GPa, $k$ halves and $U$ doubles to 15 J. The measured 9 to 11 J lies between.

### Example 3 — contact time from SHM

*Trigger: a spring meeting the ground at its natural length. Tool: SHM about the equilibrium point.* §5: $z_0 = 3.25$ cm, $A = 5.18$ cm, $\omega = 17.4$ rad s⁻¹, $t_c = 0.259$ s, not the half-period 0.181 s. Faster landing (larger $v_0$) makes $A \gg z_0$, $\arcsin(z_0/A) \to 0$, and $t_c \to \pi/\omega$: a hard landing is closer to half a cycle.

### Example 4 — the flea's power

*Trigger: an energy and a very short time. Tool: $P = E/t$.* $2.25 \times 10^{-7}\ \text{J} / 0.75 \times 10^{-3}\ \text{s} = 3.0 \times 10^{-4}$ W. The muscles supply the energy over a much longer time; the resilin pad and its catch squeeze the delivery into under a millisecond.

### Example 5 — why the kangaroo's cost stays flat

*Trigger: a cost that does not rise with speed. Tool: work per step, with most of it recycled.* If each hop's energy is mostly stored and returned by tendons, the muscles pay only for the loss, a few to a few tens of per cent of each hop. Going faster by taking longer hops at the same frequency keeps the number of expensive muscle contractions per second the same, and a larger stored fraction at higher speed can more than cover the rest.

## Common Misconceptions (Teaching Notes)

### 1. "A tendon is a rope that joins muscle to bone"

It is a spring, and part of the engine.

**Fix:** the skipping experiment; then §4's 9 to 11 J returned per step.

### 2. "A stiffer tendon stores more energy"

At a given force, the softer one stores more: $U = F^2/2k$.

**Fix:** Example 2, with the modulus halved.

### 3. "The leg's spring is the Achilles tendon"

The leg behaves like a 153 J spring at mid-stance; the Achilles tendon returns about 10 J of it.

**Fix:** §5's last paragraph and the end of the video.

### 4. "Tendons get stronger as fast as muscles"

Tendons adapt slowly, only to heavy load, and their core is hardly renewed after the teens.

**Fix:** §8, and the adolescent volleyball numbers.

## Exam Notes

No board on file examines tendons, hysteresis in materials, or the spring-mass model of running. The syllabuses for Cambridge 0625 and 9702, the IB Physics guide and the AP Physics 1, 2 and C: Mechanics course descriptions contain none of them; AP Physics 1 mentions a spring-mass oscillator only in a classroom activity. Every tool used here is examined:

| Tool | Exam Notes in |
|---|---|
| Stress, strain, Young modulus; elastic potential energy as the area under a force–extension graph (9702 §6) | [[Stress, Strain and Young Modulus]] |
| Hooke's law, $k$, and energy $\tfrac12 kx^2$ | [[Hooke's Law for Springs]], [[Elastic Strings and Springs]] |
| Simple harmonic motion, $\omega = \sqrt{k/m}$, amplitude and phase | [[Simple Harmonic Motion]] |
| Work, energy and power | [[Work, Energy and Power]] |

The SHM contact-time derivation in §5 is a good extended problem at A-Level: it needs the equilibrium point, amplitude from position and velocity, and an inverse sine, all in one setting.

## Connections

- **Parents:** [[Stress, Strain and Young Modulus]] (the material), [[Hooke's Law for Springs]] (the spring), [[Simple Harmonic Motion]] (the bounce), [[Work, Energy and Power]] (slow in, fast out).
- **The body thread:** [[The Kinetic Chain]], whose §4 first named these springs; [[The Spine Under Load]], the same honesty about models against measurement.
- **The same loop elsewhere:** [[Magnetism and Magnetic Materials]], hysteresis in iron.
- **Tension in general:** [[Elastic Strings and Springs]].

## Sources

- T. J. Dawson, C. R. Taylor, "Energetic cost of locomotion in kangaroos", *Nature* 246 (1973) 313–314; R. McN. Alexander, A. Vernon, "The mechanics of hopping by kangaroos", *Journal of Zoology* 177 (1975).
- C. N. Maganaris, J. P. Paul, *Journal of Physiology* 521 (1999) and *Journal of Biomechanics* (2000, 2002); T. A. L. Wren et al., *Clinical Biomechanics* 16 (2001); S. Obst et al., *Frontiers in Physiology* (2020); T. Pollock, R. E. Shadwick, *American Journal of Physiology* (1994); M. B. Bennett, R. F. Ker, N. J. Dimery, R. McN. Alexander, *Journal of Zoology* 209 (1986); K. S. Miller et al., *Journal of Biomechanics* 45 (2012).
- R. F. Ker, "Dynamic tensile properties of the plantaris tendon of sheep", *Journal of Experimental Biology* 93 (1981); T. Finni et al., *Journal of Applied Physiology* (2013) on in vivo hysteresis.
- A. A. Kharazi et al., *Scientific Reports* 11 (2021), Achilles tendon force, strain and recoil measured in running; P. V. Komi, *Journal of Biomechanics* 23 (1990); R. F. Ker, M. B. Bennett, S. R. Bibby, R. C. Kester, R. McN. Alexander, "The spring in the arch of the human foot", *Nature* 325 (1987) 147–149, as reported by Alexander, *Journal of Experimental Biology* 160 (1991); L. A. Stearne et al., *Scientific Reports* 6 (2016).
- R. Blickhan, *Journal of Biomechanics* 22 (1989); T. A. McMahon, G. C. Cheng, *Journal of Biomechanics* 23 (1990); C. T. Farley, O. González, *Journal of Biomechanics* 29 (1996); D. P. Ferris, M. Louie, C. T. Farley, *Proceedings of the Royal Society B* 265 (1998); I. S. Moore et al., *Frontiers in Sports and Active Living* (2019).
- H. C. Bennet-Clark, E. C. A. Lucey, "The jump of the flea", *Journal of Experimental Biology* 47 (1967); G. P. Sutton, M. Burrows, *Journal of Experimental Biology* 214 (2011); G. N. Askew, R. L. Marsh, *Journal of Experimental Biology* (2002); T. J. Roberts, E. Azizi, *Journal of Experimental Biology* 214 (2011); S. Kurokawa et al., *Journal of Applied Physiology* 90 (2001).
- S. Bohm, F. Mersmann, A. Arampatzis, *Sports Medicine – Open* 1 (2015); A. Arampatzis et al., *Journal of Experimental Biology* 210 (2007); K. M. Heinemeier et al., *FASEB Journal* 27 (2013); F. Mersmann et al. (2017), adolescent volleyball players.
- R. F. Ker, X. T. Wang, A. V. L. Pike, *Journal of Experimental Biology* 203 (2000); V. Huttunen et al., *American Journal of Sports Medicine* 42 (2014); N. J. Lemme et al., *Orthopaedic Journal of Sports Medicine* 6 (2018).
- `tendons-model.py`, `tendons-figures.py`, `tendons-manim.py` — every number, curve and frame, recomputed.

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\sigma = E\varepsilon^2/2\varepsilon_t$ | `\sigma = E\varepsilon^2/2\varepsilon_t` | Toe region from fibre recruitment |
| $\sigma = E(\varepsilon - \varepsilon_t/2)$ | `\sigma = E(\varepsilon - \varepsilon_t/2)` | Linear region |
| $k = EA/L$ | `k = EA/L` | Spring constant of a tendon |
| $U = F^2/2k$ | `U = F^2/2k` | Energy stored at force $F$ |
| $t_c = (\pi + 2\arcsin(z_0/A))/\omega$ | `t_c = (\pi + 2\arcsin(z_0/A))/\omega` | Contact time of a spring landing at natural length |
