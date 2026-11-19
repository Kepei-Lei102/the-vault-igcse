# Animation stack: Manim (the bay's standard).
# Every frame is drawn from tendons-model.py: the stance is its integrated
# spring-mass model, the flights are ballistic, the bars are its energies.
# Render:  manim -qk tendons-manim.py SpringRunner
# then copy the MP4 beside the card and delete media/ and __pycache__/.
"""Tendons as Springs - a runner as a mass on a spring leg.

Ch 1  the model: a point mass, a spring leg, a foot on the ground
Ch 2  three strides, slowed ten times: the leg shortens, stores, gives back
Ch 3  the ledger: the leg spring holds ~150 J at mid-stance; the Achilles
      tendon, measured, returns about 10 J of it. The leg is spring-like;
      only part of it is a spring.
"""
import importlib.util
import math
from pathlib import Path

import numpy as np
from manim import *

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("tm", HERE / "tendons-model.py")
tm = importlib.util.module_from_spec(spec); spec.loader.exec_module(tm)
P = tm.P

GREY = ManimColor("#888888"); BLUE = ManimColor("#2563eb"); GREEN = ManimColor("#059669")
AMBER = ManimColor("#f59e0b"); PURPLE = ManimColor("#7c3aed"); RED = ManimColor("#dc2626")
FONT = "Helvetica Neue"
S = 1.55                    # scene units per metre
GROUND_Y = -1.6
X0 = -5.4
SLOW = 15
g = 9.81


def T(text, size, colour):
    return Text(text, font=FONT, font_size=size, color=colour)


def build_run(strides=3, n=240):
    """Time series of the centre of mass over several strides, with foot positions and leg state."""
    st = tm.stance()
    m, k, L0 = P["mass_kg"], P["k_leg_N_per_m"], P["leg_length_m"]
    Tc = st["contact_s"]
    ts = np.linspace(0, Tc, n)
    sol_x, sol_y, sol_vx, sol_vy = st["x"], st["y"], st["vx"], st["vy"]
    tt = st["t"]
    vx_off, vy_off = st["takeoff_v"]
    Tf = 2 * vy_off / g
    frames = []   # (t, comx, comy, footx or None, KE, PEg, PEs, Fy)
    t0, xshift = 0.0, 0.0
    ymin = float(np.min(sol_y))
    # start with half a flight so the first frame is at the top
    for s_ in range(strides):
        # flight before stance: from apex to touchdown
        x_td, y_td = sol_x[0] + xshift, sol_y[0]
        for tau in np.linspace(-Tf / 2, 0, n // 3, endpoint=False):
            x = x_td + vx_off * tau; y = y_td - vy_off * tau - 0.5 * g * tau ** 2
            vy = -vy_off - g * tau
            frames.append((t0 + tau + Tf / 2, x, y, None, 0.5 * m * (vx_off ** 2 + vy ** 2), m * g * (y - ymin), 0.0, 0.0))
        t0 += Tf / 2
        for i in range(len(tt)):
            L = math.hypot(sol_x[i], sol_y[i])
            frames.append((t0 + tt[i], sol_x[i] + xshift, sol_y[i], xshift,
                           0.5 * m * (sol_vx[i] ** 2 + sol_vy[i] ** 2), m * g * (sol_y[i] - ymin),
                           0.5 * k * (L0 - L) ** 2, float(st["Fy"][i])))
        t0 += Tc
        # flight after stance: from takeoff to apex
        x_to, y_to = sol_x[-1] + xshift, sol_y[-1]
        for tau in np.linspace(0, Tf / 2, n // 3, endpoint=False)[1:]:
            x = x_to + vx_off * tau; y = y_to + vy_off * tau - 0.5 * g * tau ** 2
            vy = vy_off - g * tau
            frames.append((t0 + tau, x, y, None, 0.5 * m * (vx_off ** 2 + vy ** 2), m * g * (y - ymin), 0.0, 0.0))
        t0 += Tf / 2
        xshift += (sol_x[-1] - sol_x[0]) + vx_off * Tf
    times = np.array([f[0] for f in frames])
    grid = np.linspace(times[0], times[-1], 900)
    idx = np.clip(np.searchsorted(times, grid), 0, len(frames) - 1)
    return [frames[i] for i in idx], st


def spring_points(a, b, coils=9, width=0.16):
    a, b = np.array(a), np.array(b)
    d = b - a; L = np.linalg.norm(d); u = d / L; nrm = np.array([-u[1], u[0], 0])
    pts = [a, a + u * L * 0.08]
    for i in range(coils * 2):
        f = 0.08 + 0.84 * (i + 0.5) / (coils * 2)
        pts.append(a + u * L * f + nrm * width * (1 if i % 2 == 0 else -1))
    pts += [a + u * L * 0.92, b]
    return pts


class SpringRunner(Scene):
    def construct(self):
        frames, st = build_run()
        self.frames, self.st = frames, st
        self.idx = ValueTracker(0)
        Emax = max(f[4] - min(ff[4] for ff in frames) + f[5] + f[6] for f in frames)
        KEmin = min(f[4] for f in frames)
        L0 = P["leg_length_m"]

        title = T("a runner, modelled as a mass on a spring leg", 30, GREY).to_edge(UP, buff=0.35)
        self.play(FadeIn(title))

        ground = Line([-7, GROUND_Y, 0], [7, GROUND_Y, 0], color=GREY)
        self.add(ground)

        def P2(x, y):
            return np.array([X0 + S * x, GROUND_Y + S * y, 0])

        def cur():
            return frames[int(self.idx.get_value())]

        def runner():
            t, x, y, foot, KE, PEg, PEs, Fy = cur()
            gp = VGroup()
            com = P2(x, y)
            if foot is None:
                th = math.radians(self.st["angle_deg"])
                tip = com + S * L0 * np.array([math.cos(th), -math.sin(th), 0])
                gp.add(VMobject(color=BLUE, stroke_width=4).set_points_as_corners(spring_points(com, tip)))
            else:
                ft = P2(foot, 0)
                gp.add(VMobject(color=AMBER if PEs > 1 else BLUE, stroke_width=4).set_points_as_corners(spring_points(com, ft)))
                gp.add(Dot(ft, radius=0.07, color=GREY))
            gp.add(Circle(radius=0.28, color=BLUE, fill_opacity=0.35).move_to(com))
            return gp

        def bars():
            t, x, y, foot, KE, PEg, PEs, Fy = cur()
            gp = VGroup()
            x0, y0, h = 3.3, -1.2, 2.45
            for i, (val, col, lab) in enumerate(((KE - KEmin, BLUE, "kinetic"), (PEg, GREEN, "height"),
                                                 (PEs, AMBER, "spring"))):
                xx = x0 + 1.15 * i
                hh = max(h * val / Emax, 0.001)
                gp.add(Rectangle(width=0.7, height=hh, color=col, fill_opacity=0.7, stroke_width=1).move_to([xx, y0 + hh / 2, 0]))
                gp.add(T(lab, 18, GREY).move_to([xx, y0 - 0.3, 0]))
                gp.add(T(f"{val:.0f} J", 18, col).move_to([xx, y0 + hh + 0.25, 0]))
            gp.add(T("each bar: energy above its lowest value in the stride", 16, GREY).move_to([4.45, 2.35, 0]))
            gp.add(T(f"ground force {Fy / (P['mass_kg'] * g):.1f} x body weight", 22, PURPLE).move_to([4.45, -2.35, 0]))
            gp.add(T(f"slowed {SLOW} times", 18, GREY).move_to([-5.6, 2.7, 0]))
            return gp

        r = always_redraw(runner); b = always_redraw(bars)
        self.add(r, b)
        note = T("the spring is at its natural length when the foot lands", 24, GREY).to_edge(DOWN, buff=0.35)
        self.play(FadeIn(note)); self.wait(2); self.play(FadeOut(note))

        real = frames[-1][0] - frames[0][0]
        self.play(self.idx.animate.set_value(len(frames) - 1), run_time=real * SLOW, rate_func=linear)
        self.wait(0.5)

        self.play(FadeOut(r), FadeOut(b), FadeOut(ground), FadeOut(title))
        peak = 0.5 * P["k_leg_N_per_m"] * self.st["max_compression_m"] ** 2
        lines = VGroup(
            T(f"at mid-stance the leg spring holds {peak:.0f} J", 30, AMBER),
            T("measured in a living Achilles tendon: about 10 J returned per step", 26, BLUE),
            T("the leg behaves like a spring; only part of it is one", 28, GREY),
            T("tendons store and return, muscles hold them and top them up", 24, GREEN),
        ).arrange(DOWN, buff=0.45)
        for ln in lines:
            self.play(FadeIn(ln), run_time=0.8); self.wait(1.2)
        self.wait(2)
