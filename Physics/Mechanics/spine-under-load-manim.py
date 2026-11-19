# Animation stack: Manim (the bay's standard).
# Every number on screen is computed by spine-under-load-model.py: the bars are
# its muscle force and disc compression for the pose being drawn.
# Render:  manim -qk spine-under-load-manim.py SpineUnderLoad
# then copy the MP4 beside the card and delete media/ and __pycache__/.
"""The Spine Under Load - one box, four ways to pick it up.

Ch 1  the lever: a joint, the upper body in front, the back muscles 5 cm behind
Ch 2  bend over, box hanging from straight arms: the bars cross the guideline
Ch 3  squat with the box close: under it
Ch 4  squat but reach: back over it. The knees did not save you; the distance did.
"""
import importlib.util
from pathlib import Path

import numpy as np
from manim import *

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("sm", HERE / "spine-under-load-model.py")
sm = importlib.util.module_from_spec(spec); spec.loader.exec_module(sm)

GREY = ManimColor("#888888")
BLUE = ManimColor("#2563eb")
PURPLE = ManimColor("#7c3aed")
GREEN = ManimColor("#059669")
AMBER = ManimColor("#f59e0b")
RED = ManimColor("#dc2626")
TEAL = ManimColor("#0891b2")
S = 3.2                              # scene units per metre
HIP_STAND = np.array([-2.3, 0.05, 0.0])
FLOOR_Y = HIP_STAND[1] - 0.92 * S
SHOULDER = 0.45                      # metres along the trunk
ARM = 0.62
KN = 0.95                            # scene units per kN on the bars
NIOSH = sm.P["niosh_N"] / 1000
D = np.pi / 180
FONT = "Helvetica Neue"


def T(text, size, colour):
    return Text(text, font=FONT, font_size=size, color=colour)


class SpineUnderLoad(Scene):
    def construct(self):
        self.theta = ValueTracker(0.0)      # trunk angle from vertical, degrees
        self.squat = ValueTracker(0.0)      # 0 straight legs, 1 deep squat
        self.hang = ValueTracker(1.0)       # 1 box hangs under the shoulders, 0 held at `reach`
        self.reach = ValueTracker(0.25)     # box distance in front of L5/S1 when held, metres
        self.box = ValueTracker(0.0)        # box mass on/off (0..1 of 20 kg)

        self.lever()
        self.bend()
        self.squat_close()
        self.squat_far()
        self.close()

    # ---------- geometry ----------
    def hip(self):
        return HIP_STAND + np.array([-0.05 * S * self.squat.get_value(), -0.32 * S * self.squat.get_value(), 0])

    def box_dist(self):
        th = self.theta.get_value() * D
        hanging = max(0.12, SHOULDER * np.sin(th))
        h = self.hang.get_value()
        return h * hanging + (1 - h) * self.reach.get_value()

    def pose(self):
        th = self.theta.get_value() * D
        hip = self.hip()
        u = np.array([np.sin(th), np.cos(th), 0])
        shoulder = hip + S * SHOULDER * u
        head = hip + S * (SHOULDER + 0.14) * u
        com = hip + S * sm.P["upper_body_com_m"] * u
        d = self.box_dist()
        h = self.hang.get_value()
        held_y = hip[1] - S * 0.08 if self.theta.get_value() > 5 else shoulder[1] - S * 0.15
        box_c = np.array([hip[0] + S * d, max(FLOOR_Y + 0.22, h * (shoulder[1] - S * ARM) + (1 - h) * held_y), 0])
        q = self.squat.get_value()
        knee = hip + np.array([S * (0.05 + 0.33 * q), -S * (0.46 - 0.12 * q), 0])
        foot = np.array([hip[0] + S * 0.02 * (1 - q) + S * 0.02, FLOOR_Y, 0])
        return hip, shoulder, head, com, box_c, knee, foot

    def loads(self):
        r = sm.lift(self.theta.get_value(), 20 * self.box.get_value(), self.box_dist())
        return r["muscle_N"] / 1000, r["compression_N"] / 1000

    # ---------- drawing ----------
    def figure(self):
        def draw():
            hip, shoulder, head, com, box_c, knee, foot = self.pose()
            g = VGroup()
            g.add(Line([-6.6, FLOOR_Y, 0], [0.4, FLOOR_Y, 0], color=GREY, stroke_width=2))
            g.add(Line(hip, knee, color=GREY, stroke_width=7), Line(knee, foot, color=GREY, stroke_width=7))
            g.add(Line(hip, shoulder, color=BLUE, stroke_width=10))
            g.add(Circle(radius=0.26, color=BLUE, fill_opacity=0.25).move_to(head))
            # back muscles: a band 5 cm behind the trunk line, drawn wider so it can be seen
            th = self.theta.get_value() * D
            back = np.array([-np.cos(th), np.sin(th), 0]) * 0.22
            g.add(Line(hip + back, hip + back + (shoulder - hip) * 0.55, color=RED, stroke_width=6))
            g.add(Dot(hip, radius=0.09, color=AMBER))
            if self.box.get_value() > 0.01:
                g.add(Line(shoulder, box_c + UP * 0.2, color=GREY, stroke_width=5))
                g.add(Square(0.42, color=GREEN, fill_opacity=0.35 * self.box.get_value()).move_to(box_c))
            # lever arms on the floor
            yl = FLOOR_Y - 0.28
            g.add(Line([hip[0], yl, 0], [com[0], yl, 0], color=BLUE, stroke_width=5))
            if self.box.get_value() > 0.01:
                g.add(Line([hip[0], yl - 0.16, 0], [box_c[0], yl - 0.16, 0], color=GREEN, stroke_width=5))
            g.add(DashedLine([hip[0], hip[1], 0], [hip[0], yl - 0.25, 0], color=AMBER, stroke_width=1.5))
            return g
        return always_redraw(draw)

    def bars(self):
        x0, y0 = 1.9, -2.55

        def draw():
            m, c = self.loads()
            g = VGroup()
            g.add(DashedLine([x0 - 0.6, y0 + NIOSH * KN, 0], [x0 + 2.9, y0 + NIOSH * KN, 0], color=AMBER))
            for i, (val, col, lab) in enumerate(((m, RED, "back muscles"), (c, PURPLE, "disc compression"))):
                x = x0 + 2.3 * i
                g.add(Rectangle(width=0.9, height=max(val * KN, 0.001), color=col, fill_opacity=0.8,
                                stroke_width=1).move_to([x, y0 + val * KN / 2, 0]))
                top = y0 + val * KN
                g.add(T(f"{val:.1f} kN", 24, GREY if val * KN > 1.4 else col).move_to([x, top - 0.75 if val * KN > 1.4 else top + 0.3, 0]))
                g.add(T(lab, 19, GREY).move_to([x, y0 - 0.3, 0]))
            g.add(T("3.4 kN\nguideline", 20, AMBER).next_to([x0 + 2.9, y0 + NIOSH * KN, 0], RIGHT, buff=0.15))
            over = c > NIOSH
            g.add(T("over the guideline" if over else "under the guideline", 22, RED if over else GREEN)
                  .move_to([x0 + 1.15, 2.85, 0]))
            return g
        return always_redraw(draw)

    def say(self, text, colour=GREY, size=28):
        t = T(text, size, colour).to_edge(UP, buff=0.4)
        return t

    # ---------- chapters ----------
    def lever(self):
        title = self.say("one joint, one lever")
        self.add(self.figure(), self.bars())
        self.play(FadeIn(title))
        hip = self.hip()
        notes = VGroup(
            T("the disc at the base of the spine: the pivot", 20, AMBER).next_to(hip, RIGHT, buff=0.3).shift(DOWN * 0.3),
            T("back muscles, 5 cm behind it", 20, RED).next_to(hip + UP * 0.8, LEFT, buff=0.4),
            T("upper body, 37.5 kg", 20, BLUE).next_to(hip + UP * 1.4, RIGHT, buff=0.35),
        )
        self.play(FadeIn(notes), run_time=1.2)
        self.wait(2.5)
        self.play(FadeOut(notes))
        t2 = self.say("pick up a 20 kg box, held against you")
        self.play(ReplacementTransform(title, t2))
        self.hang.set_value(0); self.reach.set_value(0.10)
        self.play(self.box.animate.set_value(1), run_time=1.5)
        self.wait(1.5)
        self.title = t2

    def bend(self):
        t = self.say("bend over, legs straight: the box hangs from your arms")
        self.play(ReplacementTransform(self.title, t))
        self.play(self.hang.animate.set_value(1), run_time=0.8)
        self.play(self.theta.animate.set_value(90), run_time=5, rate_func=smooth)
        floor = T("lines under the floor: how far in front of the joint each weight acts", 20, GREY).to_edge(DOWN, buff=0.15)
        self.play(FadeIn(floor))
        self.wait(3)
        self.play(FadeOut(floor))
        self.title = t

    def squat_close(self):
        t = self.say("squat, trunk 30 degrees, box close: 25 cm")
        self.play(ReplacementTransform(self.title, t))
        self.reach.set_value(0.25)
        self.play(self.theta.animate.set_value(30), self.squat.animate.set_value(1), self.hang.animate.set_value(0),
                  run_time=4, rate_func=smooth)
        self.wait(3)
        self.title = t

    def squat_far(self):
        t = self.say("same squat, but the box at arm's length: 45 cm")
        self.play(ReplacementTransform(self.title, t))
        self.play(self.reach.animate.set_value(0.45), run_time=3, rate_func=smooth)
        self.wait(2)
        t2 = self.say("the knees did not save the back. the distance did.", AMBER, 30)
        self.play(ReplacementTransform(t, t2))
        self.wait(3)
        self.title = t2

    def close(self):
        self.play(self.reach.animate.set_value(0.25), run_time=2)
        end = T("the box never changed. the distances did.", 28, GREY).to_edge(DOWN, buff=0.15)
        self.play(FadeIn(end))
        self.wait(3)
