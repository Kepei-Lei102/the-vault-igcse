"""Figures for The Spine Under Load (vault style: #888 text, semantic colours,
transparent background, checked on light and dark).

Run from this folder, after spine-under-load-model.py has written its results:

    python3 spine-under-load-figures.py            # writes the SVGs
    python3 spine-under-load-figures.py --check    # also writes light and dark PNGs to /tmp

Model curves come from the model's own functions; measured values are typed in
once, here, with their sources, and never adjusted to fit.
Outputs: spine-under-load-lift.svg, spine-under-load-pressure.svg,
spine-under-load-carry-neck.svg, spine-under-load-creep.svg
"""
import importlib.util
import json
import math
import sys
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("sm", HERE / "spine-under-load-model.py")
sm = importlib.util.module_from_spec(spec); spec.loader.exec_module(sm)
R = json.loads((HERE / "spine-under-load-results.json").read_text())

GREY, BLUE, PURPLE, GREEN, AMBER, RED, TEAL = "#888888", "#2563eb", "#7c3aed", "#059669", "#f59e0b", "#dc2626", "#0891b2"
plt.rcParams.update({
    "text.color": GREY, "axes.edgecolor": GREY, "axes.labelcolor": GREY, "xtick.color": GREY, "ytick.color": GREY,
    "font.size": 11, "axes.titlesize": 12, "svg.fonttype": "none", "svg.hashsalt": "vault",
    "font.family": ["Helvetica Neue", "Arial", "sans-serif"], "axes.spines.top": False, "axes.spines.right": False,
    "axes.facecolor": "none", "legend.frameon": False, "legend.labelcolor": GREY,
})
CHECK = "--check" in sys.argv
NIOSH = sm.P["niosh_N"] / 1000


def save(fig, name):
    fig.savefig(HERE / name, transparent=True, metadata={"Date": None})
    if CHECK:
        for tag, bg in (("light", "#ffffff"), ("dark", "#1e1e1e")):
            fig.savefig(f"/tmp/{Path(name).stem}-{tag}.png", facecolor=bg, dpi=110)
    plt.close(fig)


def niosh(ax, x):
    ax.axhline(NIOSH, color=AMBER, lw=1.3, ls=(0, (5, 3)))
    ax.text(x, NIOSH + 0.08, "3.4 kN guideline", color=AMBER, ha="left", va="bottom", fontsize=10)


# ---- 1. the lift: angle and distance ------------------------------------------------
def fig_lift():
    fig, (a, b) = plt.subplots(1, 2, figsize=(10, 4.9))
    fig.subplots_adjust(left=0.07, right=0.98, bottom=0.27, top=0.9, wspace=0.28)
    th = np.arange(0, 91, 1)
    stoop = [sm.lift(t, 20, max(0.12, 0.45 * math.sin(math.radians(t))))["compression_N"] / 1000 for t in th]
    close = [sm.lift(t, 20, 0.25)["compression_N"] / 1000 for t in th]
    far = [sm.lift(t, 20, 0.45)["compression_N"] / 1000 for t in th]
    empty = [sm.lift(t, 0, 0)["compression_N"] / 1000 for t in th]
    a.plot(th, stoop, color=RED, lw=2.3, label="stoop: box hangs from the shoulders")
    a.plot(th, far, color=PURPLE, lw=2.0, ls="--", label="box held 45 cm out")
    a.plot(th, close, color=GREEN, lw=2.3, label="box held 25 cm out")
    a.plot(th, empty, color=GREY, lw=1.6, ls=":", label="no box")
    niosh(a, 1.5)
    for key, col in (("stoop_level", RED), ("squat_close", GREEN)):
        r = R[key]
        a.plot([r["theta"]], [r["compression_N"] / 1000], "o", color=col, ms=7, zorder=5)
    a.annotate("Example 1\n3.8 kN", (90, R["stoop_level"]["compression_N"] / 1000), xytext=(66, 4.25), color=RED, fontsize=10,
               arrowprops=dict(arrowstyle="->", color=RED, lw=1))
    a.annotate("Example 2\n2.5 kN", (30, R["squat_close"]["compression_N"] / 1000), xytext=(42, 0.55), color=GREEN, fontsize=10,
               arrowprops=dict(arrowstyle="->", color=GREEN, lw=1))
    a.set_xlim(0, 92); a.set_ylim(0, 4.8)
    a.set_xlabel("trunk angle from upright (degrees)"); a.set_ylabel("disc compression (kN)")
    a.set_title("20 kg box: bending adds, distance adds more")
    a.legend(loc="upper center", bbox_to_anchor=(0.5, -0.17), ncol=2, fontsize=9.5)

    d = np.linspace(0.05, 0.60, 56)
    for t, col in ((0, BLUE), (30, GREEN), (60, PURPLE)):
        b.plot(d * 100, [sm.lift(t, 20, x)["compression_N"] / 1000 for x in d], color=col, lw=2.2, label=f"trunk at {t}°")
    niosh(b, 6)
    b.set_xlim(5, 60); b.set_ylim(0, 4.6)
    b.set_xlabel("box distance in front of the joint (cm)"); b.set_ylabel("disc compression (kN)")
    b.set_title("Every 10 cm of reach adds 0.4 kN")
    b.legend(loc="lower right", fontsize=9.5)
    save(fig, "spine-under-load-lift.svg")


# ---- 2. the model against the measured disc (Wilke et al. 1999) --------------------------
def fig_pressure():
    cases = [("standing,\nrelaxed", 0.50, (0, 0, 0)), ("holding 20 kg\nclose", 1.10, (0, 20, 0.10)),
             ("lifting 20 kg,\nknees bent", 1.70, (30, 20, 0.25)), ("holding 20 kg\n60 cm out", 1.80, (0, 20, 0.60)),
             ("lifting 20 kg,\nround back", 2.30, (90, 20, 0.45))]
    arm = sm.P["extensor_arm_m"]
    m5 = [sm.lift(*c[2])["pressure_MPa"] for c in cases]
    sm.P["extensor_arm_m"] = 0.075
    m75 = [sm.lift(*c[2])["pressure_MPa"] for c in cases]
    sm.P["extensor_arm_m"] = arm
    x = np.arange(len(cases)); w = 0.26
    fig, ax = plt.subplots(figsize=(10, 4.3))
    fig.subplots_adjust(left=0.07, right=0.98, bottom=0.2, top=0.87)
    ax.bar(x - w, [c[1] for c in cases], w, color=(0.55, 0.55, 0.55, 0.55), edgecolor=GREY, label="measured in a living disc (Wilke 1999)")
    ax.bar(x, m5, w, color=(0.49, 0.23, 0.93, 0.35), edgecolor=PURPLE, label="model, one muscle 5 cm behind")
    ax.bar(x + w, m75, w, color=(0.05, 0.59, 0.41, 0.35), edgecolor=GREEN, label="model, one muscle 7.5 cm behind")
    for i, c in enumerate(cases):
        ax.text(x[i] - w, c[1] + 0.05, f"{c[1]:.2f}", ha="center", fontsize=9)
        ax.text(x[i], m5[i] + 0.05, f"{m5[i]:.2f}", ha="center", fontsize=9, color=PURPLE)
        ax.text(x[i] + w, m75[i] + 0.05, f"{m75[i]:.2f}", ha="center", fontsize=9, color=GREEN)
    ax.set_xticks(x, [c[0] for c in cases])
    ax.set_ylabel("pressure in the disc (MPa)")
    ax.set_ylim(0, 3.6)
    ax.set_title("A one-muscle model gets the order right and the sizes wrong by up to 40 %")
    ax.legend(loc="upper left", fontsize=9.5)
    save(fig, "spine-under-load-pressure.svg")


# ---- 3. carrying and the neck ---------------------------------------------------------------
def fig_carry_neck():
    fig, (a, b) = plt.subplots(1, 2, figsize=(10, 4.3))
    fig.subplots_adjust(left=0.08, right=0.93, bottom=0.2, top=0.86, wspace=0.34)
    one, two = sm.carry((30, 0)), sm.carry((15, 15))
    labels = ["30 kg\nin one hand", "15 kg\nin each hand"]
    x = np.arange(2); w = 0.34
    model = [one["compression_N"] / 1000, two["compression_N"] / 1000]
    meas = [2.8, 1.57]
    a.bar(x - w / 2, meas, w, color=(0.55, 0.55, 0.55, 0.55), edgecolor=GREY, label="measured (McGill 2013)")
    a.bar(x + w / 2, model, w, color=(0.49, 0.23, 0.93, 0.35), edgecolor=PURPLE, label="one-muscle model")
    for i in range(2):
        a.text(x[i] - w / 2, meas[i] + 0.05, (">" if i == 0 else "") + f"{meas[i]:.2f}", ha="center", fontsize=9.5)
        a.text(x[i] + w / 2, model[i] + 0.05, f"{model[i]:.2f}", ha="center", fontsize=9.5, color=PURPLE)
    a.set_xticks(x, labels); a.set_ylim(0, 3.4)
    a.set_ylabel("compression at the base of the spine (kN)")
    a.set_title("Same 30 kg, split or not")
    a.legend(loc="upper right", fontsize=9.5)

    phi = np.arange(0, 61, 1)
    W = sm.P["head_kg"] * 9.81
    base = sm.neck(0)["compression_N"]
    b.plot(phi, [W * sm.P["head_com_m"] * math.sin(math.radians(p_)) for p_ in phi], color=BLUE, lw=2.3,
           label="moment of the head about the lower neck (N m)")
    b2 = b.twinx()
    b2.spines["right"].set_visible(True); b2.spines["top"].set_visible(False)
    b2.plot(phi, [sm.neck(p_)["compression_N"] / base for p_ in phi], color=PURPLE, lw=2, ls="--",
            label="one-muscle model, 4 cm arm (assumed)")
    b2.plot([0, 15, 30, 45, 60], [1, 27 / 11, 40 / 11, 49 / 11, 60 / 11], "s", color=RED, ms=6, label="Hansraj 2014, computer model")
    b2.plot([45], [1.6], "D", color=GREEN, ms=7, label="Barrett 2020, from muscle signals")
    b2.set_ylabel("load on the neck, times upright", color=GREY)
    b2.set_ylim(0, 6); b.set_ylim(0, 9)
    b.set_xlabel("head bowed forward (degrees)"); b.set_ylabel("moment (N m)", color=BLUE)
    b.set_title("A bowed head: the moment is sure, the load is not")
    h1, l1 = b.get_legend_handles_labels(); h2, l2 = b2.get_legend_handles_labels()
    b.legend(h1 + h2, l1 + l2, loc="upper left", fontsize=8.8)
    save(fig, "spine-under-load-carry-neck.svg")


# ---- 4. creep: a day and a night ----------------------------------------------------------
def fig_creep():
    t = np.linspace(0, 23.95, 480)
    loss = sm.creep(t)
    fig, ax = plt.subplots(figsize=(10, 3.6))
    fig.subplots_adjust(left=0.08, right=0.98, bottom=0.17, top=0.86)
    ax.axvspan(sm.CREEP["day_h"], 24, color=(0.03, 0.57, 0.7, 0.08))
    ax.plot(t, loss, color=TEAL, lw=2.4)
    L = sm.CREEP["loss_mm"]
    ax.plot([1, 3], [0.54 * L, 0.80 * L], "o", color=AMBER, ms=7, zorder=5)
    ax.annotate("54 % gone in the first hour", (1, 0.54 * L), xytext=(2.2, 6.5), color=AMBER, fontsize=10,
                arrowprops=dict(arrowstyle="->", color=AMBER, lw=1))
    ax.annotate("80 % by three hours", (3, 0.80 * L), xytext=(5, 12.5), color=AMBER, fontsize=10,
                arrowprops=dict(arrowstyle="->", color=AMBER, lw=1))
    ax.text(20, 16.5, "lying down: the discs\ndrink back", color=TEAL, ha="center", fontsize=10)
    ax.text(9.5, 20.3, f"{L} mm, about 1 % of your height", color=GREY, ha="center", fontsize=10)
    ax.set_xlim(0, 24); ax.set_ylim(0, 22)
    ax.set_xticks(range(0, 25, 4), ["rise", "4 h", "8 h", "12 h", "16 h: bed", "20 h", "24 h"])
    ax.set_ylabel("height lost (mm)")
    ax.set_title("You are shorter every evening: creep, and recovery")
    save(fig, "spine-under-load-creep.svg")


if __name__ == "__main__":
    fig_lift()
    fig_pressure()
    fig_carry_neck()
    fig_creep()
