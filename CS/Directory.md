# The Vault — Computer Science Directory

> **87 cards across 13 bays.** Last landed: [[Version Control]] (2026-10-01) — the `final2.docx` folder taken apart: content-named snapshots, branches as 41-byte pointers, three-way merge and bisect, all checked against real git.
> One line per card: what it teaches and, where settled, which syllabus rows it closes. Open the card for everything else — its frontmatter and Connections section carry the graph of what to read first.

**Reading the bays.** A bay is a run of cards built in order. *Closed* bays cover their syllabus stretch end to end; *open* bays are still growing, and the italic line under each names what comes next (a link that leads nowhere yet is a card still to be written). 💎 marks enrichment beyond every syllabus. Board codes: 0478 = Cambridge IGCSE, 9618 = Cambridge A Level, AP CSA = AP Computer Science A.

See also: [[Mathematics/Directory|Mathematics]] · [[Physics/Directory|Physics]] · [[Stories/Directory|Stories]] · [[Meta/Directory|Meta]].

---

## Foundations (6)

*The floor everything else stands on: the gates, recursion, information, and the three hard edges of the discipline — Turing, P vs NP, Gödel.*

1. **[[Logic Gates]]** — AND/OR/NOT/NAND/NOR/XOR as circuits that compute with voltage; truth tables and symbols; NAND universality; De Morgan as the licence to swap gates. *0478 §10 · 9618 §3.2*
2. ****Recursion** *(not yet released)*** — base case + recursive case; tracing the call stack; factorial, Fibonacci, list reversal; when recursion is the natural shape and when it costs. *9618 §19.2 · AP CSA §4.16*
3. ****Information Theory** *(not yet released)*** — Shannon's entropy $H=-\sum p\log_2 p$ as surprise measured in bits, and the floor under every lossless compressor. 💎
4. ****The Turing Test** *(not yet released)*** — the Imitation Game as a burden-of-proof flip; Turing's nine pre-answered objections; ELIZA and over-attribution; Searle's Chinese Room. 💎
5. ****P vs NP** *(not yet released)*** — if an answer can be *checked* fast, can it be *found* fast? P, NP, NP-complete, reductions, and why one crack would collapse the whole class. 💎
6. ****Gödel's Incompleteness Theorems** *(not yet released)*** — Gödel numbering makes provability arithmetic, and one self-referential sentence ends Hilbert's program; code-is-data in logical dress. 💎

## Logic Circuits (4 — closed)

*What you do with gates: transform, minimise, wire into arithmetic, bend into memory. 9618 §15.2 end to end.*

1. ****Boolean Algebra** *(not yet released)*** — the identities proved by law-chain, the duality principle, De Morgan, and simplifying an expression without moving a single truth-table row.
2. ****Karnaugh Maps** *(not yet released)*** — the truth table redrawn on a Gray-code grid so minimisation becomes "loop the biggest rectangles of 1s"; the map is a torus.
3. ****Half-Adder and Full-Adder** *(not yet released)*** — a computer does arithmetic by doing logic: Sum = XOR, Carry = the majority function; the ripple-carry chain.
4. ****Flip-Flops** *(not yet released)*** — memory bought with feedback: why one inverter in a loop oscillates and two remember; the SR and JK flip-flops; the SRAM cell.

## Algorithms (11 — core arc closed, plus enrichment, the paradigms, the life cycle and A2 file processing)

*Concrete first, analysis after: searching → sorting → Big-O, with program design and the exam dialect alongside.*

1. ****Program Design** *(not yet released)*** — a flowchart is a causality trace someone already drew for you; the five design notations as five questions about one program; top-down design and the identifier table.
2. ****Cambridge Pseudocode** *(not yet released)*** — the broader exam-dialect reference — keywords, declaration forms, parameter modes and paper-specific built-ins; paired introductory implementations in **Programming Fundamentals** *(not yet released)*.
3. ****Searching** *(not yet released)*** — linear vs binary search; why halving means a million items fall in twenty looks; the sorted precondition that sorting pays for.
4. ****Sorting** *(not yet released)*** — bubble, selection, insertion, merge and quicksort on one shared list, with the $n^2$-vs-$n\log n$ gap made tangible. *0478 §7.16 · 9618 §9.2 · AP CSA §4.15, §4.17*
5. ****Big-O Notation** *(not yet released)*** — how cost grows with $n$: the class ladder from $O(1)$ to $O(n!)$, the $c, n_0$ definition, reading Big-O off code. *9618 §19.1 · AP CSA §2.12*
6. ****Parallel and External Sorting** *(not yet released)*** — what sorting becomes with many cores or data too big for RAM: fork–join merge sort, Amdahl's law, the measured overhead crossover. 💎
7. ****Object-Oriented Programming** *(not yet released)*** — the nine syllabus terms built in real Python: data and behaviour bundled, encapsulation as invariants living next to the data, inheritance as is-a, polymorphism as the loop that never asks, containment as has-a; the June 2025 Animal/Parrot/Wolf and Nov 2025 Station/Train Paper 4 questions worked against their schemes; ECS in Beyond as OOP's deliberate inverse — and the vault's own architecture. *9618 §20.1 · AP CSA Unit 3 · IB CS B3*
8. ****Program Development Life Cycle and Testing** *(not yet released)*** — the cycle from coding onward and the three models (waterfall, iterative, RAD); syntax, run-time and logic errors by who finds them; nine testing methods, the strategy and the plan; normal / abnormal / extreme / boundary data and the six validation checks; trace tables done by hand and by machine; three kinds of maintenance. *0478 §7.1, §7.5–7.8 · 9618 §12.1, §12.3*
9. ****File Processing and Exception Handling** *(not yet released)*** — records out to a file and back; serial, sequential and random organisation with every operation run on a real file and the scan-vs-seek cost measured; the exception as a message that travels up the call stack, `try`/`except`/`finally`/`raise`, when handling is appropriate and the examiners' close-outside-the-try bug. *9618 §20.2*
10. ****Programming Paradigms** *(not yet released)*** — what a paradigm is; low-level, imperative, object-oriented and declarative solving one problem side by side; the five addressing modes executed on a register machine; facts, rules and goals run on a 120-line Prolog engine with backtracking drawn; seven real Paper 3 questions against their schemes. *9618 §20.1*

11. ****Programming Fundamentals** *(not yet released)*** — state and invariants through sixteen 0478-pseudocode/Python pairs: types, I/O, operators, branches, loops, strings, scope and subprograms; real Paper 2 questions and a tested sales stream. *0478 §8.1 · §7.3–7.4, §7.9*

## Data Representation (13 — exam scope closed, plus enrichment)

*How numbers, text, images and sound become bits. 0478 §1 and 9618 §1 complete, plus 9618 §13.1 and §13.3.*

1. **[[Number Bases]]** — place value as the one rule behind binary, denary and hex; conversions both ways; why base 2 and why base 16. *0478 §1.1.1–2 · 9618 §1.1*
2. **[[Two's Complement]]** — signed integers as wraparound turned into a feature: a register is arithmetic mod $2^n$, so subtraction becomes addition on one adder. *0478 §1.1.6*
3. ****Overflow and Underflow** *(not yet released)*** — the same wraparound as the villain: detection by carry bits, and the famous bugs (Pac-Man 256, Gangnam Style, Y2038, Ariane 5). *0478 §1.1.4*
4. **[[Bitwise Operations]]** — AND/OR/XOR/NOT applied bit-parallel; masking to test, set, clear and toggle; logical vs arithmetic shifts. *0478 §1.1.5*
5. ****Gray Code** *(not yet released)*** — the same $n$ bits re-ordered so neighbours differ in one bit, because physical bits don't flip together; the rotary encoder; a walk on the $n$-cube. 💎
6. ****Floating-Point Representation** *(not yet released)*** — binary scientific notation: mantissa for precision, exponent for range, normalisation as the most-tested skill, and the errors that follow. *9618 §13.3*
7. **[[Text Encoding]]** — character set vs encoding as two layers: ASCII's designed tricks, Unicode code points, UTF-8 worked on 你, and the 乱码 gallery read forensically.
8. **[[Image Encoding]]** — bitmaps store samples (pixels, RGB, resolution × colour depth = file size); vectors store intentions (a drawing list).
9. **[[Sound Encoding]]** — sample rate and resolution as the two dials in time; Nyquist–Shannon, aliasing, and why 44,100 Hz.
10. ****Compression** *(not yet released)*** — can you get the original back? RLE with its honest edge, Huffman on MISSISSIPPI, dictionary methods; lossy as a deal with your senses.
11. ****User-Defined Data Types** *(not yet released)*** — a type as allowed values + operations; non-composite (enumerated, pointer) vs composite (set, record, class), each in real Python. *9618 §13.1*
12. **[[Storage Units (Vocab)]]** — kilo/mega/giga vs KiB/MiB/GiB, why $2^{10}\approx10^3$ bred the confusion, and file-size arithmetic for images and sound. *0478 §1.3.1–2*

13. ****Digital Audio Workstation** *(not yet released)*** — samples through a working mixer; EQ, compression, recorded-room reverb, phase vocoder, buffering and export, with audible comparisons. 💎

## Hardware Systems (17 — core closed; enrichment added)

*The whole machine below the software line: Turing → von Neumann → the fetch–execute CPU → pipelining, then memory, storage, I/O, sensors, embedded systems, interrupts, assembly, CISC vs RISC. 0478 §3 (bar network hardware) and 9618 §3.1 + §4.*

1. ****Turing Machine** *(not yet released)*** — tape, head, states and a rule-book as the minimal model of computing; the universal machine; the halting problem proved by diagonal. 💎
2. ****Von Neumann machine** *(not yet released)*** — program and data in one memory, instructions as numbers: reprogram by loading, not rewiring; the bottleneck and the Harvard rival.
3. ****CPU Architecture and the Fetch-Execute Cycle** *(not yet released)*** — CU, ALU, the five exam registers and three buses; the cycle traced register by register on a three-instruction program.
4. ****Pipelining and Simultaneous Multithreading** *(not yet released)*** — overlap the stages so one instruction finishes per cycle; hazards, branch prediction, SMT, and GPU execution groups.
5. ****RAM and the Memory Hierarchy** *(not yet released)*** — DRAM as leaking charge, SRAM as a flip-flop; the cache ladder and why locality pays.
6. ****Clock Domains and Metastability** *(not yet released)*** — one crystal, many clocks: PLLs multiply by dividing, and a signal crossing clock domains can sit undecided. 💎
7. ****Secondary Storage** *(not yet released)*** — nothing in nature is a bit: magnetic, optical and solid-state media each hand you an analogue smear and a decision boundary.
8. ****Input and Output Devices** *(not yet released)*** — every peripheral is a transducer: keyboards, mice, the three touchscreen technologies, screens and printers.
9. ****Sensors and Control Systems** *(not yet released)*** — a sensor is a transducer pointed at the world; the fourteen 0478 sensors, the sensing chain, and the feedback loop with an actuator.
10. ****Embedded Systems** *(not yet released)*** — dedication, not power, is the boundary: the one-question test (can the user change what it does?) and the blurring hardware line.
11. ****Interrupt Handling** *(not yet released)*** — the doorbell and the bookmark: cause families, the service routine, priorities, and why one machine seems to care about everything at once.
12. ****Assembly Language** *(not yet released)*** — machine code with names on; the Cambridge instruction set, addressing modes as hop-counting, traced programs.
13. ****CISC vs RISC** *(not yet released)*** — the ISA is a contract, not a blueprint: why pipelines love RISC, how x86 decodes to micro-ops, and why the ecosystem still decides.

14. ****RAID** *(not yet released)*** — lose a drive and reconstruct its bytes: striping, mirrors, two parity relations, rebuilds and why a mirror has no undo button. 💎

15. ****The GPU — From Triangles to Tensors** *(not yet released)*** — triangles become fragments; SIMT, divergence, memory reuse, tensor cores and CPU–GPU cooperation. *IB A1.1.2–3 · A4.1.2; OCR H446 §1.1.2*
16. ****The Modern CPU vs the Textbook Model** *(not yet released)*** — the fetch–execute model as a contract and the out-of-order core as the engine that honours it; branch prediction, dependency chains and the memory wall measured at ×3, ×8 and ×100 on one laptop; a cycle-level simulator of three machines; renaming and in-order commit; what it means for code. *Enrichment · 9618 §4.1 performance factors · IB A1.1*
17. ****How a Chip Is Made** *(not yet released)*** — the planar process from sand to a stencil eighty layers deep: lithography and its light, the CMOS inverter in cross-section, DRAM and flash cells built the same way, and the Poisson arithmetic of yield that sets what a die costs and why chiplets win.

## Systems Software (4 — open)

*The software that runs the machine itself. 0478 §4, 9618 §5 and §16 complete.*

1. ****Operating Systems** *(not yet released)*** — part government, part illusionist: process states and scheduling, paging vs segmentation, files, drivers, utilities, and virtual machines. *0478 §4.1 · 9618 §5.1, §15.1, §16.1*
2. ****Compilers and Interpreters** *(not yet released)*** — translate the book once or interpret live: the three translators, the four compilation stages, BNF, and RPN on a stack. *0478 §4.2 · 9618 §5.2, §16.2*
3. ****File Systems** *(not yet released)*** — names are not bytes: allocation, links, deletion, SSD discard, formatting, snapshots and sanitisation; an open-file experiment and 4K animation. *0478 §4.1 · 9618 §5.1 · IB A1.3; internals are enrichment.*
4. ****Memory Allocation and the Heap** *(not yet released)*** — where a process's variables live, measured in C (stack down, heap up, 1.5 ns against 19 ns, a 200 MB leak); a first-fit allocator built in forty lines and fragmented on purpose; reference counting and mark and sweep built and run on the cycle only one of them can free (4K Manim); leaks, dangling pointers and pools; 9618 §5.1/§16.1, IB B2.2.1 and AP CSA quoted.

*Next in the bay: [[The Call Stack]].*

## Data Structures (9 — syllabus core closed)

*From the array to the graph, each structure bought by restricting who may connect to whom. 9618 §10 and §19 complete, with §13.2 and the graph half of §18.1.*

1. ****Arrays** *(not yet released)*** — a name made computable: fixed length, one type and consecutive indices all forced by address = base + index × size; 1D and 2D.
2. ****Stacks and Queues** *(not yet released)*** — a stack is an array and one integer; a queue is an array and two; push/pop/enqueue/dequeue with their edge cases. *9618 §10.4, §19.1*
3. ****Linked List** *(not yet released)*** — order separated from location: nodes and pointers, insert in two writes, the free list, and the price paid in access time.
4. ****File Handling** *(not yet released)*** — what survives the process: open/read/write/close, text vs binary, serial, sequential and random-access files. *9618 §13.2*
5. ****Binary Trees** *(not yet released)*** — binary search frozen into pointers: the whole-subtree promise, insert and search, and the three traversals.
6. ****Balanced Trees** *(not yet released)*** — the hope converted into a contract: deletion built properly, the measured price of imbalance, and the rotations that keep $O(\log n)$. 💎
7. ****Hash Tables** *(not yet released)*** — don't store where things are, calculate where they must be; collisions as certainty (the birthday paradox), chaining and probing.
8. ****Graphs** *(not yet released)*** — delete every rule and the graph remains: adjacency matrix vs list, BFS and DFS, Dijkstra and A* worked on real papers. *9618 §18.1*

9. ****Heaps and Priority Queues** *(not yet released)*** — keep the next event ready: sift-up/down, linear-time heap construction, stable ties and rescheduling; Python and a rendered array/tree animation. 💎

## Databases (3 — closed)

*One fact, one place — then what happens when the place is a thousand machines. 0478 §9, 9618 §8 and IB A3 end to end, every worked question a real Paper 1 or Paper 2 against its scheme.*

1. ****Relational Databases** *(not yet released)*** — why files fail, Codd's tables linked by values, keys and E-R diagrams, normalisation to 3NF walked on a real order sheet and on real papers, the DBMS's features, ACID and the trillion SQLite instances in every pocket. *0478 §9.1 · 9618 §8.1–8.2 · IB A3.1–A3.2*
2. ****SQL** *(not yet released)*** — DDL and DML with every paper statement run for real in SQLite (script beside the card); the FROM-first execution order that explains WHERE vs HAVING; joins, GROUP BY, nested queries; the injection attack and the parameterised query. *0478 §9.2 · 9618 §8.3 · IB A3.3*
3. ****NoSQL and Distributed Data** *(not yet released)*** — the four families, sharding and replication, the CAP theorem proved in one paragraph, ACID vs BASE, 12306 and OceanBase, data warehouses and OLAP, and the NewSQL swing back. *IB A3.4 (HL) · 💎 for Cambridge*

## Security (5 — open)

*The threat/defence game, and the mechanism under the word "hacking". 0478 §5.3, 9618 §6, IB A2.4 — one real Paper 1 each against its scheme.*

1. ****Data Security** *(not yet released)*** — security/privacy/integrity; every threat as mechanism → aim → property (malware, phishing vs pharming, brute-force, DDoS, social engineering); the defences with the *how*; validation vs verification (valid ≠ true); a crack-time chart; and Beyond, the buffer overflow with the three walls — canary, NX, ASLR — and why a hack-lab turns ASLR off. *0478 §5.3 · 9618 §6.1–6.2 · IB A2.4*
2. ****Encryption** *(not yet released)*** — symmetric (Caesar → one-time pad → AES, Kerckhoffs) and asymmetric (Diffie–Hellman, RSA with $p=61,\ q=53$ walked and run, Euler's theorem, the factoring trapdoor); the two key directions and the who-holds-which-key table across HTTPS, mail, Signal, SSH, passkeys, updates, U 盾, wallets; hash-then-sign, certificates and CAs, TLS in five lines; key sizes, factoring records, QKD vs Shor and post-quantum; six real 9618 P3 / 0478 P1 questions. *9618 §17.1 · 0478 §2.3 · IB A2.4*

3. ****Ethics and Ownership** *(not yet released)*** — the three layers of obligation (law, code, judgement); the BCS four duties with IEEE and ACM beside them; Horizon, Dieselgate, MCAS as the exam's small scenarios at scale; copyright as a right not a lock; the licence spectrum (FSF, OSI, shareware, commercial, and freeware kept out); AI's applications and impact, with the proxy-variable bias run live. *9618 §7.1 · AP CSA 3.2, 4.1 · IB A4.4*

4. ****Data Protection and Privacy** *(not yet released)*** — personal data as *identifiable*, measured (three ordinary fields make 90 % of a city unique); the linkage attack and why hashing a phone number is not anonymising; lawful bases, principles, rights, controller and processor under GDPR and PIPL side by side; k-anonymity, keyed tokens and differential privacy, each run and priced; three 9618 questions and an AP CSA item against their schemes. *9618 §6.1 · 0478 §5.3 · IB A4.4 · AP CSA 4.1*
5. ****Privacy-Preserving Computation** *(not yet released)*** — input privacy: secret sharing and multi-party computation, Paillier and fully homomorphic encryption, federated learning with its leak and its repair, trusted execution, zero-knowledge proofs; whom each one still asks you to trust. *Enrichment; no school board*

## Artificial Intelligence (4 — open)

*The two ways to build a mind: rules written by people, or rules learned from data — and the calculus that does the learning.*

1. ****Artificial Intelligence** *(not yet released)*** — the IGCSE's four characteristics; expert systems (knowledge base, rule base, inference engine, interface) with a forward-chaining engine run for real; machine learning as parameters adjusted to shrink error — regression, k-means and Q-learning from scratch; the neuron that cannot learn XOR and the layer that can; back propagation as the chain rule, checked numerically; deep beats wide at equal weight budget; nine real 9618 and 0478 questions against their schemes. *9618 §18.1 · 0478 §6.3 · IB-CS A4.1/A4.3 (amber)*

2. ****Automated Systems and Robotics** *(not yet released)*** — sensor → microprocessor → actuator as three roles in one ring with no human in it; what makes a robot a robot (mechanical structure, electrical components, programmable — not autonomy, not intelligence), run forwards on a tractor and backwards on a smart speaker; the seven scenarios and six roles with advantages and disadvantages from the named seat; the exam's robot simulated in a room, one sensor against a vote, and a break-even with its assumptions stated; seven real Paper 1 questions against their schemes. *0478 §6.1–§6.2*
3. ****Affective Computing** *(not yet released)*** — the chain from feeling to display to sensor to label to decision; voice, text, skin and face each tested; Bayes on smiles; bias from a resting face; on-device inference and the EU ban in workplaces and schools. *Enrichment · IB A4.4 case study*

4. ****How a Language Model Works** *(not yet released)*** — next-token prediction as the whole game; counting models that improve and then run out of data; byte-pair tokens; one attention layer built in numpy with a hand-written, gradient-checked backward pass, trained on the Stories until it beats the best counting model; temperature; what scale bought; from completer to assistant; what it is not. *Enrichment · 9618 §18.1 / 0478 §6.3 / IB A4.1 illustration*

*Nothing further is queued in the bay.*

---

## Data Transmission (4 — core closed)

*0478 Sections 2 and 5, with encryption and cyber security in the Security bay; 9618 Sections 2 and 14. The core run is complete.*

1. ****Error Detection and Correction** *(not yet released)*** — validation, verification and correction at three prices: parity and its honest limit, the parity block, checksums, check digits, the echo check. *0478 §2.2*
2. ****Networks** *(not yet released)*** — why a protocol, the four-layer TCP/IP stack with encapsulation counted, packets and packet switching animated, circuit switching weighed, serial/parallel/duplex and USB, latency measured from Chengdu. *9618 §14 closed · 0478 §2.1 · IB A2.1–A2.3*

3. ****The Internet and the Web** *(not yet released)*** — the internet is not the web: URL anatomy, the DNS chain sent by hand and animated, HTTP vs HTTPS with a certificate read live, session and persistent cookies fetched from a real site, MAC/IPv4/IPv6, the router, LAN topologies with a packet's path, client-server vs P2P, cloud, bit streaming. *0478 §3.4 + §5.1 · 9618 §2.1 · IB A2.2*

4. ****Digital Currency and Blockchain** *(not yet released)*** — double spending makes ordering necessary; hashes reveal edits, signatures authorise spending, consensus chooses a history; three real Paper 1 questions and an offline ledger with a separate real-signature experiment. *0478 §5.2 · IB A2.1.2/A2.2.3 applications*

## Java Companions (5 — CLOSED 2026-09-22)

*For exams answered in Java. Each companion keeps the concept in its Python card and shows only what Java does differently; every program was compiled and run. All five delivered; the practice site outside the vault is the next step.*

1. ****Java Values and Expressions** *(not yet released)*** — compile then run, and the three kinds of error; `int`, `double`, `boolean`; int division and `%`; where a cast binds; both rounding idioms; overflow and round-off; compound assignment; the `Math` class and a random integer in a range, derived. *AP CSA 1.1–1.8, 1.11*
2. ****Java Objects, References and Strings** *(not yet released)*** — method signatures, overloading and call by value; class methods against instance methods; `new` and constructors; references, aliases and `null`; what a method can and cannot change; `String` indices read as cuts, immutability, `==` against `equals` against `compareTo`; `Scanner` as a library class at work.
3. ****Java Control Flow** *(not yet released)*** — braces make the block (Apple's `goto fail`); conditions must be `boolean`; one-way, two-way and multiway selection and the dangling `else`; `&&`, `||`, `!`, short-circuit guards; truth tables and De Morgan's laws; `while`, sentinels and the digits of an integer; the order of a `for` header; walking a String; nested loops and statement execution counts.
4. ****Java Classes** *(not yet released)*** — a `BankAccount` written section by section: design as abstraction, `private` fields and `public` methods, constructors and default values (a 4K Manim clip of one `new`), accessors and mutators and where `return` goes, objects as parameters and privacy per class, `this` and the `size = size` trap, `static` and `final`, the three scopes and least scope.
5. ****Java Arrays and ArrayList** *(not yet released)*** — arrays with defaults, `length` and the enhanced for loop's copy; the standard algorithms; reading a text file with `File`, `Scanner` and `split`; wrapper classes and boxing; `ArrayList` and its six methods, the shift after `add` and `remove`, and removing while traversing (a 4K clip of the skipped element); 2D arrays as arrays of rows; the searches and sorts in Java, traced.

## Software Engineering (2 — opened 2026-09-22)

1. ****Anatomy of a Tech Stack** *(not yet released)*** — script versus system: a complete stack in one Python file (page, JSON API, SQLite behind a cache) restarted, timed and loaded; the request's journey with the clock running (4K Manim), the three tiers and the state line that decides what can be copied, the listen backlog that refused half the requests, cloud tiers and deployment; 9618 §2.1, 0478 §3.3/§5.1 and IB A1.1.9/A2.2 quoted.
2. ****Version Control** *(not yet released)*** 💎 — the `final2.docx` folder as a bad version control system; blobs, trees and commits named by SHA-1, written from scratch and accepted by real git; 5000 copies against 349 objects; branches as 41-byte pointers (4K Manim); three-way merge through the merge base, matching `git merge-file` 400 of 400; bisect in $\log_2 n$ tests, measured to 4096 commits; a short history from SCCS to April 2005.

## Enrichment directions

- **Hardware** — **How a Chip Is Made** *(not yet released)*, **The Modern CPU vs the Textbook Model** *(not yet released)*.
- **Software engineering** — **Version Control** *(not yet released)* delivered; APIs and deployment are taught inside **Anatomy of a Tech Stack** *(not yet released)*; [[Concurrency]] next.

---

## How this directory stays honest

- **One line per card.** The hook says what the card teaches; the card carries everything else. If a line wants a second sentence, the second sentence belongs in the card.
- **Counts match the disk.** Each bay's number is the `.md` count in its folder and the total at the top is their sum; the linter checks both, and flags any line that has grown past a paragraph.
- **The landing story lives elsewhere.** What each card closed, and why it was built when it was, is recorded in the maintainer trackers at close-out — never here.
