"""Figures for Tendons as Springs (vault style: #888 text, semantic colours,
transparent background, checked on light and dark).

    python3 tendons-figures.py            # writes the SVGs
    python3 tendons-figures.py --check    # also writes light and dark PNGs to /tmp

Every curve comes from tendons-model.py.
Outputs: tendons-curve.svg, tendons-hysteresis.svg, tendons-stance.svg
"""
import importlib.util
import math
import sys
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("tm", HERE / "tendons-model.py")
tm = importlib.util.module_from_spec(spec); spec.loader.exec_module(tm)
P = tm.P

GREY, BLUE, PURPLE, GREEN, AMBER, RED, TEAL = "#888888", "#2563eb", "#7c3aed", "#059669", "#f59e0b", "#dc2626", "#0891b2"
plt.rcParams.update({
    "text.color": GREY, "axes.edgecolor": GREY, "axes.labelcolor": GREY, "xtick.color": GREY, "ytick.color": GREY,
    "font.size": 11, "axes.titlesize": 12, "svg.fonttype": "none", "svg.hashsalt": "vault",
    "font.family": ["Helvetica Neue", "Arial", "sans-serif"], "axes.spines.top": False, "axes.spines.right": False,
    "axes.facecolor": "none", "legend.frameon": False, "legend.labelcolor": GREY,
})
CHECK = "--check" in sys.argv


def save(fig, name):
    fig.savefig(HERE / name, transparent=True, metadata={"Date": None})
    if CHECK:
        for tag, bg in (("light", "#ffffff"), ("dark", "#1e1e1e")):
            fig.savefig(f"/tmp/{Path(name).stem}-{tag}.png", facecolor=bg, dpi=110)
    plt.close(fig)


def fig_curve():
    fig, (a, b) = plt.subplots(1, 2, figsize=(10, 4.3), gridspec_kw={"width_ratios": [1.55, 1]})
    fig.subplots_adjust(left=0.07, right=0.98, bottom=0.14, top=0.87, wspace=0.28)
    eps = np.linspace(0, 0.09, 181)
    t = P["eps_toe"]
    a.axvspan(0, 100 * t, color=(0.96, 0.62, 0.04, 0.10))
    a.axvspan(100 * P["eps_fail"] - 1.5, 100 * P["eps_fail"], color=(0.86, 0.15, 0.15, 0.10))
    a.plot(100 * eps, tm.sigma_uniform(eps) / 1e6, color=BLUE, lw=2.4, label="derived: quadratic toe, then straight")
    e2 = np.linspace(0, 0.09, 19)
    a.plot(100 * e2, tm.sigma_fibres(e2) / 1e6, "o", color=AMBER, ms=5, label="2000 crimped fibres, added up")
    a.text(1.0, 88, "toe", color=AMBER, ha="center")
    a.text(5.2, 88, "linear: slope = Young modulus", color=BLUE, ha="center")
    a.text(100 * P["eps_fail"] - 0.75, 45, "failure", color=RED, ha="center", rotation=90)
    a.set_xlim(0, 9.2); a.set_ylim(0, 100)
    a.set_xlabel("strain (%)"); a.set_ylabel("stress (MPa)")
    a.set_title("A curve made of fibres going taut one by one")
    a.legend(loc="lower right", fontsize=9.5)

    frac = np.clip(eps / t, 0, 1)
    b.plot(100 * eps, 100 * frac, color=AMBER, lw=2.4)
    b.set_xlim(0, 9.2); b.set_ylim(0, 105)
    b.set_xlabel("strain (%)"); b.set_ylabel("fibres taut (%)")
    b.set_title("Why the toe curves")
    b.text(3.0, 45, "each fibre starts\nwith its own slack;\nby 2 % all are taut", color=GREY, fontsize=10)
    save(fig, "tendons-curve.svg")


def fig_hysteresis():
    fig, ax = plt.subplots(figsize=(10, 4.2))
    fig.subplots_adjust(left=0.07, right=0.98, bottom=0.14, top=0.87)
    eps = np.linspace(0, 0.045, 200)
    load = tm.sigma_uniform(eps) / 1e6
    for loss, col, lab, x0 in ((P["loss_in_vitro"], GREEN, "isolated tendon: 7 % lost", 0),
                               (P["loss_in_vivo"], RED, "measured in a living leg: 19 % (disputed)", 5.2)):
        e = 100 * eps + x0
        ax.fill_between(e, (1 - loss) * load, load, color=col, alpha=0.25)
        ax.plot(e, load, color=BLUE, lw=2.2)
        ax.plot(e, (1 - loss) * load, color=col, lw=2.2, ls="--")
        ax.text(x0 + 2.25, 49, lab, color=col, ha="center", fontsize=10)
        ax.annotate("", xy=(x0 + 3.2, 33), xytext=(x0 + 2.3, 22), arrowprops=dict(arrowstyle="->", color=BLUE))
        ax.annotate("", xy=(x0 + 2.0, 13), xytext=(x0 + 3.0, 25), arrowprops=dict(arrowstyle="->", color=col))
    ax.text(1.15, 26, "stretch", color=BLUE, fontsize=10, ha="right")
    ax.text(3.35, 16, "release", color=GREEN, fontsize=10)
    ax.set_xticks([0, 1, 2, 3, 4, 5.2, 6.2, 7.2, 8.2, 9.2], ["0", "1", "2", "3", "4 %", "0", "1", "2", "3", "4 %"])
    ax.set_ylim(0, 55); ax.set_ylabel("stress (MPa)"); ax.set_xlabel("strain")
    ax.set_title("The loop: energy in along the top, energy back along the bottom, the gap is heat")
    save(fig, "tendons-hysteresis.svg")


def fig_stance():
    s = tm.stance()
    m, k, L0 = P["mass_kg"], P["k_leg_N_per_m"], P["leg_length_m"]
    t = s["t"] * 1000
    fig, (a, b) = plt.subplots(1, 2, figsize=(10, 4.2))
    fig.subplots_adjust(left=0.08, right=0.98, bottom=0.14, top=0.87, wspace=0.28)
    a.plot(t, s["Fy"] / (m * 9.81), color=PURPLE, lw=2.4, label="spring-mass model")
    w = math.sqrt(s["k_vert"] / m)
    a.axhline(1, color=GREY, lw=0.8, ls=":")
    a.text(3, 1.05, "body weight", color=GREY, fontsize=9.5)
    a.annotate("", xy=(1000 * s["contact_s"], 0.15), xytext=(0, 0.15), arrowprops=dict(arrowstyle="<->", color=GREY))
    a.text(500 * s["contact_s"], 0.22, f"contact {1000 * s['contact_s']:.0f} ms (measured 247)", color=GREY, ha="center", fontsize=9.5)
    a.set_xlabel("time on the ground (ms)"); a.set_ylabel("vertical force (body weights)")
    a.set_title(f"One stance at {P['speed_m_s']:.1f} m/s: a peak of {s['peak_Fy_bw']:.1f} body weights")
    a.set_ylim(0, 2.9)

    KE = 0.5 * m * (s["vx"] ** 2 + s["vy"] ** 2)
    PEg = m * 9.81 * (s["y"] - s["y"].min())
    PEs = 0.5 * k * (L0 - s["L"]) ** 2
    base = KE.min()
    b.stackplot(t, KE - base, PEg, PEs, colors=[(0.15, 0.39, 0.92, 0.45), (0.02, 0.59, 0.41, 0.45), (0.96, 0.62, 0.04, 0.6)],
                labels=["kinetic (above its minimum)", "gravitational (above the lowest point)", "stored in the leg spring"])
    b.set_xlabel("time on the ground (ms)"); b.set_ylabel("energy (J)")
    b.set_title("The spring takes the energy in and gives it back")
    b.legend(loc="upper center", fontsize=9, bbox_to_anchor=(0.5, 1.0))
    b.set_ylim(0, 1.45 * max((KE - base + PEg + PEs).max(), 1))
    save(fig, "tendons-stance.svg")


if __name__ == "__main__":
    fig_curve()
    fig_hysteresis()
    fig_stance()
