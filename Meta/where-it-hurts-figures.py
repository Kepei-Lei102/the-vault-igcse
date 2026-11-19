"""Figure for Where It Hurts Might Not Be Where It Broke (vault style: #888
text, semantic colours, transparent background, checked on light and dark).

    python3 where-it-hurts-figures.py            # writes where-it-hurts-chains.svg
    python3 where-it-hurts-figures.py --check    # also writes light and dark PNGs to /tmp

Five chains, each drawn the same way: links in order, the first bad link
in amber ("broke"), the place the trouble shows in red ("hurts"), and a
dashed arrow back along the chain. The examples are the card's own.
"""
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

HERE = Path(__file__).resolve().parent
GREY, AMBER, RED = "#888888", "#f59e0b", "#dc2626"
plt.rcParams.update({"text.color": GREY, "font.size": 10.5, "svg.fonttype": "none", "svg.hashsalt": "vault",
                     "font.family": ["Helvetica Neue", "Arial", "sans-serif"]})
CHECK = "--check" in sys.argv

CHAINS = [  # (row label, links, index of the break, index of the hurt)
    ("a flat", ["pipe upstairs", "along the beam", "your ceiling drips"], 0, 2),
    ("a child's leg", ["hip joint", "shared nerve", "knee aches"], 0, 2),
    ("a throw", ["trunk does less", "shoulder", "elbow overloaded"], 0, 2),
    ("a program", ["parse() returns None", "load()", "top_student() crashes"], 0, 2),
    ("a derivation", ["step 2: sign slip", "step 3", "step 4", "step 5: √ of −167"], 0, 3),
]

fig, ax = plt.subplots(figsize=(10, 6.0))
ax.set_xlim(0, 10); ax.set_ylim(-0.75, len(CHAINS) + 0.1); ax.axis("off")
fig.subplots_adjust(left=0.01, right=0.99, top=0.97, bottom=0.02)

X0, X1 = 1.9, 9.6
for r, (label, links, broke, hurt) in enumerate(CHAINS):
    y = len(CHAINS) - 1 - r + 0.35
    ax.text(0.05, y, label, va="center", ha="left", fontsize=11, fontweight="bold")
    n = len(links)
    xs = [X0 + (X1 - X0) * (i + 0.5) / n for i in range(n)]
    w = (X1 - X0) / n * 0.84
    for i, (x, text) in enumerate(zip(xs, links)):
        colour = AMBER if i == broke else RED if i == hurt else GREY
        fill = (0.96, 0.62, 0.04, 0.12) if i == broke else (0.86, 0.15, 0.15, 0.09) if i == hurt else (0.53, 0.53, 0.53, 0.08)
        ax.add_patch(FancyBboxPatch((x - w / 2, y - 0.2), w, 0.4, boxstyle="round,pad=0.02,rounding_size=0.08",
                                    fc=fill, ec=colour, lw=1.4))
        ax.text(x, y, text, ha="center", va="center", color=colour if i in (broke, hurt) else GREY, fontsize=10)
        if i < n - 1:
            ax.add_patch(FancyArrowPatch((x + w / 2, y), (xs[i + 1] - w / 2, y), arrowstyle="-|>",
                                         mutation_scale=11, color=GREY, lw=1.1))
    ax.add_patch(FancyArrowPatch((xs[hurt], y - 0.23), (xs[broke], y - 0.23), arrowstyle="-|>", mutation_scale=11,
                                 color=AMBER, lw=1.2, ls=(0, (4, 3)), connectionstyle="arc3,rad=-0.12"))

ax.text(X0, -0.6, "broke", color=AMBER, fontsize=10.5, fontweight="bold", va="center")
ax.text(X0 + 0.75, -0.6, "hurts", color=RED, fontsize=10.5, fontweight="bold", va="center")
ax.text(X0 + 1.5, -0.6, "dashed: trace back along the chain", color=AMBER, fontsize=10.5, va="center")

fig.savefig(HERE / "where-it-hurts-chains.svg", transparent=True, metadata={"Date": None})
if CHECK:
    for tag, bg in (("light", "#ffffff"), ("dark", "#1e1e1e")):
        fig.savefig(f"/tmp/where-it-hurts-chains-{tag}.png", facecolor=bg, dpi=110)
