# Animation stack: Manim (the bay's standard).
# Every frame is drawn from kinetic-chain-model.py: the links move as the model
# says they move, and the bars are its angular velocities, not an illustration.
# Render:  manim -qk kinetic-chain-see-it-throw.py KineticChainThrow
# then copy the MP4 beside the card and delete media/ and __pycache__/.
"""The kinetic chain - one throw, seen from above, twice.

Ch 1  the cast: trunk, upper arm, forearm with the ball
Ch 2  everything fires at once: the elbow is straight before the trunk has moved
Ch 3  in order: each link peaks later than the last, and hands its motion on
Ch 4  the ledger: who did the work, and who left with the energy
"""
import importlib.util
import json
from pathlib import Path

import numpy as np
from manim import *

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("kc", HERE / "kinetic-chain-model.py")
kc = importlib.util.module_from_spec(spec); spec.loader.exec_module(kc)
R = json.loads((HERE / "kinetic-chain-results.json").read_text())

GREY = ManimColor("#888888")
BLUE = ManimColor("#2563eb")
PURPLE = ManimColor("#7c3aed")
GREEN = ManimColor("#059669")
AMBER = ManimColor("#f59e0b")
RED = ManimColor("#dc2626")
SEG = (BLUE, PURPLE, GREEN)
NAMES = ("trunk", "upper arm", "forearm")
D = np.pi / 180
SCALE = 4.6                      # scene units per metre
ORIGIN_XY = np.array([-2.6, 1.75, 0.0])
SLOW = 40                        # the throw is shown this many times slower than life


def run(key, n=600):
    on = tuple(x / 1000 for x in R[key]["onset_ms"])
    r = kc.throw(on, dense=True)
    t = np.linspace(0, r["t"], n)
    y = r["sol"].sol(t)
    q, w = y[:3], y[3:6]
    xy = np.array([kc.fXY(q[:, i], kc.PARS) for i in range(n)], float)
    vh = np.array([np.hypot(*np.array(kc.fVH(q[:, i], w[:, i], kc.PARS), float)) for i in range(n)])
    vdir = np.array(kc.fVH(q[:, -1], w[:, -1], kc.PARS), float)
    return dict(t=t, w=w / D, xy=xy, vh=vh, T=r["t"], on=on, speed=r["speed"], vdir=vdir / np.hypot(*vdir))


def P(x, y):
    return ORIGIN_XY + SCALE * np.array([x, y, 0.0])


class KineticChainThrow(Scene):
    def construct(self):
        self.together, self.sequence = run("together"), run("sequence")
        self.wtop = 1.08 * max(self.sequence["w"].max(), self.together["w"].max())
        self.cast()
        a = self.throw(self.together, "everything fires at once", first=True)
        b = self.throw(self.sequence, "now in order: trunk, shoulder, elbow", first=False)
        self.compare(a, b)
        self.ledger()

    # ------------------------------------------------------------------ helpers
    def chain(self, data, tr):
        def at(i):
            k = int(np.clip(round(tr.get_value()), 0, len(data["t"]) - 1))
            return data["xy"][k]
        trunk = always_redraw(lambda: Line(P(0, 0), P(*at(0)[0:2]), color=BLUE, stroke_width=14))
        upper = always_redraw(lambda: Line(P(*at(0)[0:2]), P(*at(0)[2:4]), color=PURPLE, stroke_width=10))
        fore = always_redraw(lambda: Line(P(*at(0)[2:4]), P(*at(0)[4:6]), color=GREEN, stroke_width=7))
        ball = always_redraw(lambda: Dot(P(*at(0)[4:6]), radius=0.11, color=AMBER))
        spine = Dot(P(0, 0), radius=0.09, color=GREY)
        self.ball = ball
        return VGroup(trunk, upper, fore, ball, spine)

    def meters(self, data, tr):
        x0, y0, h, wd = 3.0, -1.35, 3.3, 0.55
        group = VGroup()
        base = Line([x0 - 0.3, y0, 0], [x0 + 3 * 1.05 + 0.1, y0, 0], color=GREY, stroke_width=2)
        group.add(base)
        for i in range(3):
            x = x0 + i * 1.05
            def bar(i=i, x=x):
                k = int(np.clip(round(tr.get_value()), 0, len(data["t"]) - 1))
                v = max(data["w"][i][k], 0.0)
                hh = max(h * v / self.wtop, 0.01)
                return Rectangle(width=wd, height=hh, color=SEG[i], fill_opacity=0.45, stroke_width=3).move_to([x, y0 + hh / 2, 0])
            group.add(always_redraw(bar))
            group.add(Text(NAMES[i], font_size=20, color=SEG[i]).move_to([x, y0 - 0.32, 0]))
        group.add(Text("how fast each link is turning", font_size=22, color=GREY).move_to([x0 + 1.05, y0 + h + 0.45, 0]))
        speed = always_redraw(lambda: Text(
            f"ball  {data['vh'][int(np.clip(round(tr.get_value()), 0, len(data['t']) - 1))]:4.1f} m/s",
            font_size=30, color=AMBER).move_to([x0 + 1.05, y0 - 0.9, 0]))
        clock = always_redraw(lambda: Text(
            f"{1000 * data['t'][int(np.clip(round(tr.get_value()), 0, len(data['t']) - 1))]:3.0f} ms",
            font_size=24, color=GREY).move_to([-5.9, 2.35, 0]))
        group.add(speed, clock)
        return group

    # ------------------------------------------------------------------ Ch 1
    def cast(self):
        title = Text("one throw, seen from above", font_size=34, color=GREY).to_edge(UP, buff=0.4)
        self.play(FadeIn(title), run_time=0.8)
        tr = ValueTracker(0)
        ch = self.chain(self.sequence, tr)
        self.play(FadeIn(ch), run_time=0.8)
        xy = self.sequence["xy"][0]
        labels = VGroup(
            Text("trunk, 35 kg, turning about the spine", font_size=24, color=BLUE).next_to(P(*(xy[0:2] / 2)), RIGHT, buff=0.45),
            Text("upper arm, 2.0 kg", font_size=24, color=PURPLE).next_to(P(*((xy[0:2] + xy[2:4]) / 2)), DOWN + RIGHT, buff=0.3),
            Text("forearm and hand, 1.5 kg, and the ball", font_size=24, color=GREEN).next_to(P(*xy[4:6]), UP, buff=0.3).shift(RIGHT * 0.6),
        )
        for lab in labels:
            self.play(FadeIn(lab), run_time=0.6)
        note = Text("each link is lighter than the one it hangs from", font_size=28, color=GREY).to_edge(DOWN, buff=0.5)
        self.play(FadeIn(note), run_time=0.8)
        self.wait(1.6)
        self.play(FadeOut(VGroup(title, labels, note, ch)), run_time=0.7)

    # ------------------------------------------------------------------ Ch 2 and 3
    def throw(self, data, heading, first):
        title = Text(heading, font_size=32, color=GREY).to_edge(UP, buff=0.4)
        slow = Text(f"slowed {SLOW} times", font_size=22, color=GREY).move_to([-5.7, 2.8, 0])
        tr = ValueTracker(0)
        ch, mt = self.chain(data, tr), self.meters(data, tr)
        self.play(FadeIn(title), FadeIn(slow), FadeIn(ch), FadeIn(mt), run_time=0.8)
        self.wait(0.6)
        n = len(data["t"]) - 1
        marks = [0.0] + [o for o in data["on"][1:] if 0 < o < data["T"]] + [data["T"]]
        flags = {data["on"][1]: "shoulder fires", data["on"][2]: "elbow fires"}
        note = None
        for a, b in zip(marks[:-1], marks[1:]):
            if not first and a in flags:
                new = Text(flags[a], font_size=26, color=RED).move_to([-5.5, 1.85, 0])
                self.play(FadeIn(new), *( [FadeOut(note)] if note else [] ), run_time=0.3)
                note = new
            self.play(tr.animate.set_value(n * b / data["T"]), run_time=max(SLOW * (b - a), 0.3), rate_func=linear)
        if note:
            self.play(FadeOut(note), run_time=0.2)
        end = data["xy"][-1][4:6]
        fly = Dot(P(*end), radius=0.11, color=AMBER)
        ch.remove(self.ball); self.remove(self.ball)          # the ball has left the hand
        self.add(fly)
        reach = 0.22 + 0.012 * data["speed"]
        self.play(fly.animate.move_to(P(*end) + np.array([*(reach * SCALE * data["vdir"]), 0.0])), run_time=0.9, rate_func=linear)
        result = Text(f"{data['speed']:.1f} m/s  =  {3.6 * data['speed']:.0f} km/h,  released after {1000 * data['T']:.0f} ms",
                      font_size=28, color=AMBER).move_to([0, -3.55, 0])
        why = Text("the elbow is straight before the trunk has turned" if first else
                   "each link peaks after the one before, which then slows", font_size=26, color=GREY).move_to([0, -3.05, 0])
        self.play(FadeIn(result), FadeIn(why), run_time=0.7)
        self.wait(2.2)
        self.play(FadeOut(VGroup(title, slow, ch, mt, fly, result, why)), run_time=0.7)
        return data["speed"]

    # ------------------------------------------------------------------ compare
    def compare(self, a, b):
        t1 = Text("same body, same muscles", font_size=34, color=GREY).shift(UP * 1.4)
        t2 = Text(f"at once: {a:.1f} m/s", font_size=34, color=GREY).shift(UP * 0.3)
        t3 = Text(f"in order: {b:.1f} m/s", font_size=34, color=AMBER).shift(DOWN * 0.5)
        t4 = Text(f"{b / a:.2f} times the speed, {(b / a) ** 2:.1f} times the energy", font_size=30, color=GREY).shift(DOWN * 1.6)
        for x in (t1, t2, t3, t4):
            self.play(FadeIn(x), run_time=0.6)
        self.wait(2.0)
        self.play(FadeOut(VGroup(t1, t2, t3, t4)), run_time=0.7)

    # ------------------------------------------------------------------ Ch 4
    def ledger(self):
        work, ke = R["sequence"]["work_J"], R["sequence"]["ke_J"]
        total = sum(work)
        title = Text("the ledger of the throw made in order", font_size=32, color=GREY).to_edge(UP, buff=0.4)
        self.play(FadeIn(title), run_time=0.7)
        width = 10.0
        rows = []
        for y, vals, label in ((1.0, work, "work done by the muscles of each joint"), (-1.2, ke, "kinetic energy of each link at release")):
            x = -width / 2
            lab = Text(label, font_size=24, color=GREY).move_to([0, y + 0.75, 0])
            row = VGroup(lab)
            for i, v in enumerate(vals):
                wd = max(width * v / total, 0.02)
                rect = Rectangle(width=wd, height=0.8, color=SEG[i], fill_opacity=0.45, stroke_width=3).move_to([x + wd / 2, y, 0])
                row.add(rect)
                if wd > 0.9:
                    row.add(Text(f"{v:.0f} J", font_size=22, color=GREY).move_to(rect))
                x += wd
            rows.append(row)
        self.play(FadeIn(rows[0]), run_time=1.0)
        self.wait(1.0)
        self.play(FadeIn(rows[1]), run_time=1.0)
        key = VGroup(*[Text(n, font_size=22, color=c) for n, c in zip(("trunk", "shoulder and upper arm", "elbow, forearm and ball"), SEG)]).arrange(RIGHT, buff=0.7).move_to([0, -2.4, 0])
        self.play(FadeIn(key), run_time=0.6)
        end = Text(f"the elbow's muscles gave {work[2]:.0f} J; the forearm and ball left with {ke[2]:.0f} J",
                   font_size=26, color=AMBER).to_edge(DOWN, buff=0.35)
        self.play(FadeIn(end), run_time=0.8)
        self.wait(3.0)
        self.play(FadeOut(VGroup(title, rows[0], rows[1], key, end)), run_time=0.8)
