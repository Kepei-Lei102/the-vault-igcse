"""Figure for God Syndrome (vault style: #888 text, semantic colours,
transparent background, checked on light and dark).

    python3 god-syndrome-figures.py            # writes god-syndrome-surprise.svg
    python3 god-syndrome-figures.py --check    # also writes light and dark PNGs to /tmp

Left: a game you win with probability p, win worth 1 and loss worth 0. The
expected value is p, so the surprise (reward prediction error) of a win is
1 - p and of a loss is -p. At p = 1, god mode, a win surprises by nothing.
Right: in Rutledge et al. (PNAS 2014) each past event's pull on momentary
happiness decays by a forgetting factor per trial; the fitted mean was
0.61 (SD 0.30). Weight after k trials = gamma**k, shown for 0.4, 0.61, 0.8.
Every curve is computed here, never typed in.
"""
import sys
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
GREY, BLUE, GREEN, AMBER, RED = "#888888", "#2563eb", "#059669", "#f59e0b", "#dc2626"
plt.rcParams.update({
    "text.color": GREY, "axes.edgecolor": GREY, "axes.labelcolor": GREY, "xtick.color": GREY, "ytick.color": GREY,
    "font.size": 11, "axes.titlesize": 12, "svg.fonttype": "none", "svg.hashsalt": "vault",
    "font.family": ["Helvetica Neue", "Arial", "sans-serif"], "axes.spines.top": False, "axes.spines.right": False,
    "axes.facecolor": "none",
})
CHECK = "--check" in sys.argv

p = np.linspace(0, 1, 201)
win_surprise, loss_surprise = 1 - p, -p
k = np.arange(0, 13)
gammas = {0.4: 0.55, 0.61: 1.0, 0.8: 0.55}
assert abs(0.61 ** 10) < 0.01          # "more than 10 trials ago ... essentially no influence"

fig, (a, b) = plt.subplots(1, 2, figsize=(10, 4.1))
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.15, top=0.86, wspace=0.3)

a.axhline(0, color=GREY, lw=0.8)
a.plot(p, win_surprise, color=GREEN, lw=2.4)
a.plot(p, loss_surprise, color=RED, lw=2.4)
a.text(0.1, 0.95, "surprise when you win", color=GREEN, va="center")
a.text(0.06, -0.62, "surprise when you lose", color=RED, va="center")
a.plot([1], [0], "o", color=AMBER, ms=9, zorder=5)
a.annotate("god mode: you cannot lose,\nso a win surprises by nothing", xy=(1, 0), xytext=(0.47, 0.5),
           color=AMBER, arrowprops=dict(arrowstyle="->", color=AMBER, lw=1.3))
a.set_xlim(0, 1.04); a.set_ylim(-1.08, 1.08)
a.set_xlabel("chance of winning, p")
a.set_ylabel("outcome minus expectation")
a.set_title("A win is worth what you could have lost")

for g, alpha in gammas.items():
    lab = f"γ = {g}" + ("  (fitted mean)" if g == 0.61 else "")
    b.plot(k, g ** k, "o-", color=BLUE, alpha=alpha, lw=2.2 if g == 0.61 else 1.4, ms=4, label=lab)
b.set_xlabel("rounds since the win")
b.set_ylabel("its pull on happiness now")
b.set_ylim(0, 1.05); b.set_xlim(-0.3, 12.3)
b.set_title("And every win fades")
b.legend(frameon=False, labelcolor=GREY)

fig.savefig(HERE / "god-syndrome-surprise.svg", transparent=True, metadata={"Date": None})
if CHECK:
    for tag, bg in (("light", "#ffffff"), ("dark", "#1e1e1e")):
        fig.savefig(f"/tmp/god-syndrome-surprise-{tag}.png", facecolor=bg, dpi=110)
