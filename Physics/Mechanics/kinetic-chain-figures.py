"""Figures for The Kinetic Chain (vault style: #888 text, semantic colours,
transparent background, checked on light and dark).

Run from this folder, after kinetic-chain-model.py has written its results:

    python3 kinetic-chain-figures.py            # writes the four SVGs
    python3 kinetic-chain-figures.py --check    # also writes light and dark PNGs to /tmp for a look

Every curve and bar is drawn from the model's own output, never typed in.
Outputs: kinetic-chain-strobe.svg, kinetic-chain-sequence.svg,
kinetic-chain-energy.svg, kinetic-chain-weak-link.svg, kinetic-chain-levers.svg
"""
import importlib.util
import json
import sys
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, Rectangle

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("kc", HERE / "kinetic-chain-model.py")
kc = importlib.util.module_from_spec(spec); spec.loader.exec_module(kc)
R = json.loads((HERE / "kinetic-chain-results.json").read_text())

GREY, BLUE, PURPLE, GREEN, AMBER, RED, TEAL = "#888888", "#2563eb", "#7c3aed", "#059669", "#f59e0b", "#dc2626", "#0891b2"
SEG = (BLUE, PURPLE, GREEN)                      # trunk, upper arm, forearm and hand
NAMES = ("trunk", "upper arm", "forearm and hand")
plt.rcParams.update({
    "text.color": GREY, "axes.edgecolor": GREY, "axes.labelcolor": GREY, "xtick.color": GREY, "ytick.color": GREY,
    "font.size": 11, "axes.titlesize": 12, "svg.fonttype": "none", "svg.hashsalt": "vault",
    "font.family": ["Helvetica Neue", "Arial", "sans-serif"], "axes.spines.top": False, "axes.spines.right": False, "axes.facecolor": "none",
})
CHECK = "--check" in sys.argv
D = np.pi / 180


def rgba(c, a):
    return tuple(int(c[i:i + 2], 16) / 255 for i in (1, 3, 5)) + (a,)


def save(fig, name):
    fig.savefig(HERE / name, transparent=True, metadata={"Date": None})
    if CHECK:
        for tag, bg in (("light", "#ffffff"), ("dark", "#1e1e1e")):
            fig.savefig(f"/tmp/{Path(name).stem}-{tag}.png", facecolor=bg, dpi=110)
    plt.close(fig)


def run(key):
    on = [x / 1000 for x in R[key]["onset_ms"]]
    r = kc.throw(tuple(on), dense=True)
    assert abs(r["speed"] - R[key]["hand_speed"]) < 0.05, (key, r["speed"], R[key]["hand_speed"])
    return r


def series(r, n=400):
    t = np.linspace(0, r["t"], n)
    y = r["sol"].sol(t)
    q, w = y[:3], y[3:6]
    xy = np.array([kc.fXY(q[:, i], kc.PARS) for i in range(n)], float)      # Sx Sy Ex Ey Hx Hy
    vh = np.array([np.hypot(*np.array(kc.fVH(q[:, i], w[:, i], kc.PARS), float)) for i in range(n)])
    return t, q, w, xy, vh


together, sequence = run("together"), run("sequence")

# ============================ Fig 1: the two throws, frame by frame ============================
fig, axes = plt.subplots(1, 2, figsize=(10.6, 5.0))
for ax, r, title in ((axes[0], together, "everything fires at once"), (axes[1], sequence, "trunk, then shoulder, then elbow")):
    t, q, w, xy, vh = series(r)
    frames = np.linspace(0, len(t) - 1, 9).astype(int)
    for k, i in enumerate(frames):
        a = 0.18 + 0.82 * k / (len(frames) - 1)
        S, E, H = xy[i, 0:2], xy[i, 2:4], xy[i, 4:6]
        ax.plot([0, S[0]], [0, S[1]], color=rgba(BLUE, a), lw=5, solid_capstyle="round")
        ax.plot([S[0], E[0]], [S[1], E[1]], color=rgba(PURPLE, a), lw=3.6, solid_capstyle="round")
        ax.plot([E[0], H[0]], [E[1], H[1]], color=rgba(GREEN, a), lw=2.6, solid_capstyle="round")
        ax.add_patch(Circle(H, 0.022, facecolor=rgba(AMBER, a), edgecolor="none"))
    ax.plot(xy[:, 4], xy[:, 5], color=AMBER, lw=1.0, ls=(0, (3, 3)))
    ax.add_patch(Circle((0, 0), 0.03, facecolor=rgba(GREY, 0.5), edgecolor=GREY))
    ax.text(0.05, 0.02, "spine", color=GREY, fontsize=9.5)
    H = xy[-1, 4:6]
    ax.text(0.5, -0.115, f"ball leaves at {r['speed']:.1f} m/s  ({r['speed'] * 3.6:.0f} km/h)\n{r['t'] * 1000:.0f} ms after the trunk starts",
            transform=ax.transAxes, ha="center", va="top", color=GREY, fontsize=10.5)
    ax.set_title(title, color=GREY, pad=8)
    ax.set_aspect("equal"); ax.axis("off")
    ax.set_xlim(-0.80, 0.55); ax.set_ylim(-0.80, 0.16)
handles = [plt.Line2D([], [], color=c, lw=4) for c in SEG] + [plt.Line2D([], [], color=AMBER, marker="o", lw=0)]
fig.legend(handles, list(NAMES) + ["ball"], loc="upper center", ncol=4, frameon=False, labelcolor=GREY, bbox_to_anchor=(0.5, 0.93))
fig.suptitle("the same muscles, seen from above: nine frames at equal time steps, faint to solid", color=GREY, fontsize=12.5, y=0.99)
fig.tight_layout(rect=(0, 0.06, 1, 0.90))
save(fig, "kinetic-chain-strobe.svg")

# ============================ Fig 2: who is fastest, and when ============================
fig, (a1, a2) = plt.subplots(2, 1, figsize=(10.0, 7.2), sharex=True, height_ratios=[1.25, 1])
t, q, w, xy, vh = series(sequence)
ms = t * 1000
for i in range(3):
    a1.plot(ms, w[i] / D, color=SEG[i], lw=2.2, label=NAMES[i])
    k = int(np.argmax(w[i]))
    a1.plot(ms[k], w[i][k] / D, "o", color=SEG[i], ms=6)
for i, name in ((1, "shoulder fires"), (2, "elbow fires")):
    for ax in (a1, a2):
        ax.axvline(sequence["onset"][i] * 1000, color=GREY, lw=0.9, ls=(0, (4, 4)))
    a1.text(sequence["onset"][i] * 1000 + 1.5, a1.get_ylim()[1] * 0.93, name, color=GREY, fontsize=9.5, va="top")
a1.axhline(0, color=GREY, lw=0.6)
a1.set_ylabel("angular velocity of each link (degrees per second)")
a1.legend(frameon=False, labelcolor=GREY, loc="center left")
a1.set_title("each link peaks later than the one before it, and the earlier one slows as it hands over", color=GREY, pad=8)
a2.plot(ms, vh, color=AMBER, lw=2.4)
a2.set_ylabel("speed of the ball (m/s)"); a2.set_xlabel("time since the trunk started (ms)")
a2.text(ms[-1], vh[-1], f"  {vh[-1]:.1f} m/s", color=AMBER, va="center", fontsize=10.5)
a2.set_xlim(0, ms[-1] * 1.09)
fig.tight_layout()
save(fig, "kinetic-chain-sequence.svg")

# ============================ Fig 3: the energy ledger ============================
fig, ax = plt.subplots(figsize=(10.0, 4.2))
fig.subplots_adjust(left=0.24, right=0.97, top=0.80, bottom=0.30)
work, ke = np.array(R["sequence"]["work_J"]), np.array(R["sequence"]["ke_J"])
for y, vals in ((1, work), (0, ke)):
    left = 0
    for i in range(3):
        ax.barh(y, vals[i], left=left, height=0.62, color=rgba(SEG[i], 0.30), edgecolor=SEG[i], lw=1.6)
        if vals[i] > 6:
            ax.text(left + vals[i] / 2, y, f"{vals[i]:.0f} J", ha="center", va="center", color=GREY, fontsize=10.5)
        left += vals[i]
ax.set_yticks([1, 0], ["work done by the muscles\nof each joint", "kinetic energy of each link\nat release"])
ax.set_xlabel("energy (J)")
ax.set_ylim(-0.55, 1.55)
fig.legend([Rectangle((0, 0), 1, 1, facecolor=rgba(c, 0.30), edgecolor=c) for c in SEG],
           ["trunk", "shoulder and upper arm", "elbow, forearm, hand and ball"], frameon=False, labelcolor=GREY, ncol=3,
           loc="upper center", bbox_to_anchor=(0.58, 0.97))
fig.text(0.58, 0.06, f"the elbow's own muscles did {work[2]:.0f} J; the forearm, hand and ball left with {ke[2]:.0f} J. The rest came down the chain.",
         ha="center", color=GREY, fontsize=10.5)
save(fig, "kinetic-chain-energy.svg")

# ============================ Fig 4: the weak link ============================
fig, (a1, a2) = plt.subplots(1, 2, figsize=(10.4, 4.4))
wl = R["weak_link"]
f = [100 * x["trunk_fraction"] for x in wl]
a1.plot(f, [x["hand_speed"] for x in wl], "o-", color=AMBER, lw=2.2)
for x in wl:
    a1.text(100 * x["trunk_fraction"], x["hand_speed"] + 0.35, f"{x['hand_speed']:.1f}", ha="center", color=GREY, fontsize=10)
a1.set_xlabel("what the trunk can give (% of full torque)"); a1.set_ylabel("speed of the ball (m/s)")
a1.set_title("the arm unchanged: the throw gets slower", color=GREY, pad=8)
a1.invert_xaxis(); a1.set_ylim(0, max(x["hand_speed"] for x in wl) * 1.18)
a2.bar([str(int(round(v))) for v in f], [100 * (x["arm_factor_to_restore"] - 1) for x in wl], color=rgba(RED, 0.28), edgecolor=RED, lw=1.6)
for i, x in enumerate(wl):
    a2.text(i, 100 * (x["arm_factor_to_restore"] - 1) + 2, f"+{100 * (x['arm_factor_to_restore'] - 1):.0f}%", ha="center", color=GREY, fontsize=10.5)
a2.set_xlabel("what the trunk can give (% of full torque)"); a2.set_ylabel("extra torque the shoulder and elbow need (%)")
a2.set_ylim(0, 100 * (max(x["arm_factor_to_restore"] for x in wl) - 1) * 1.2)
a2.set_title("to throw as fast as before: the arm pays", color=GREY, pad=8)
fig.tight_layout()
save(fig, "kinetic-chain-weak-link.svg")

# ============================ Fig 5: two levers, drawn to scale ============================
fig, (a1, a2) = plt.subplots(1, 2, figsize=(10.8, 4.9))


def arrow(ax, a, b, c, lw=2.0):
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle="-|>", color=c, lw=lw, mutation_scale=13, zorder=6))


ax = a1                                          # the forearm, elbow at the origin, lengths in metres
ax.plot([0, 0.35], [0, 0], color=GREEN, lw=6, solid_capstyle="round")
ax.plot([0, 0], [0, 0.30], color=PURPLE, lw=6, solid_capstyle="round")
ax.add_patch(Circle((0, 0), 0.012, facecolor=rgba(GREY, 0.6), edgecolor=GREY, zorder=7))
ax.plot([0.04, 0.012], [0, 0.27], color=rgba(RED, 0.45), lw=5, solid_capstyle="round")
arrow(ax, (0.075, 0.0), (0.075, 0.17), RED)
arrow(ax, (0.35, 0.0), (0.35, -0.10), BLUE)
arrow(ax, (0.174, 0.0), (0.174, -0.055), TEAL)
ax.text(0.09, 0.13, "the biceps pulls\nwith 495 N", color=RED, fontsize=10.5, va="center")
ax.text(0.35, -0.125, "5 kg held\n49 N", color=BLUE, fontsize=10.5, ha="center", va="top")
ax.text(0.174, -0.075, "forearm and hand\n15 N", color=TEAL, fontsize=10, ha="center", va="top")
ax.text(0.04, -0.018, "4 cm", color=RED, fontsize=9.5, ha="center", va="top")
ax.text(0.30, 0.022, "35 cm from the elbow", color=GREY, fontsize=9.5, ha="center")
ax.text(-0.015, -0.02, "elbow", color=GREY, fontsize=9.5, ha="right", va="top")
ax.set_title("the forearm: ten times the force, a ninth of the travel", color=GREY, pad=8)
ax.set_xlim(-0.12, 0.47); ax.set_ylim(-0.22, 0.33); ax.set_aspect("equal"); ax.axis("off")

ax = a2                                          # the bent back, lumbar joint at the origin
ax.plot([0, 0.45], [0, 0], color=BLUE, lw=7, solid_capstyle="round")
ax.plot([0, -0.02], [0, -0.42], color=GREY, lw=6, solid_capstyle="round", alpha=0.7)
ax.plot([0.45, 0.45], [0, -0.33], color=PURPLE, lw=4, solid_capstyle="round")
ax.add_patch(Rectangle((0.37, -0.47), 0.16, 0.14, facecolor=rgba(AMBER, 0.25), edgecolor=AMBER, lw=1.6))
ax.add_patch(Circle((0, 0), 0.014, facecolor=rgba(GREY, 0.6), edgecolor=GREY, zorder=7))
ax.plot([-0.05, 0.40], [0.05, 0.05], color=RED, lw=2.2)
arrow(ax, (0.10, 0.05), (-0.06, 0.05), RED)
arrow(ax, (0.28, 0.0), (0.28, -0.12), TEAL)
arrow(ax, (0.45, -0.47), (0.45, -0.58), AMBER)
ax.text(0.17, 0.085, "back muscles, 5 cm above the joint: 3800 N", color=RED, fontsize=10.5, ha="center")
ax.text(0.265, -0.06, "upper body\n368 N at 28 cm", color=TEAL, fontsize=10, ha="right", va="center")
ax.text(0.45, -0.60, "20 kg box, 196 N at 45 cm", color=AMBER, fontsize=10, ha="center", va="top")
ax.text(-0.02, 0.02, "lumbar joint", color=GREY, fontsize=9.5, ha="right")
ax.set_title("the bent back: a 20 kg box costs the spine 3.8 kN", color=GREY, pad=8)
ax.set_xlim(-0.30, 0.75); ax.set_ylim(-0.70, 0.22); ax.set_aspect("equal"); ax.axis("off")
fig.tight_layout()
save(fig, "kinetic-chain-levers.svg")
print("five SVGs written from the model's own numbers")
