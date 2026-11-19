"""The kinetic chain, measured on a model: a three-link throw seen from above.

    python3 kinetic-chain-model.py            # runs every experiment, prints the tables, writes kinetic-chain-results.json

Links: the trunk turning about the spine, the upper arm, and the forearm with
hand and ball. Each joint has a muscle group that can be switched on once and
stays on until release; its torque falls in a straight line to zero at a top
speed (a straight-line stand-in for Hill's force-velocity curve). Joints have
elastic end stops. There is no gravity: the plane of the throw is horizontal.

Every number the card quotes comes from this file. The assumptions are the
constants below; change one and run it again.
"""
from __future__ import annotations

import itertools
import json
import os
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp
from scipy.optimize import minimize

HERE = Path(__file__).resolve().parent
D = np.pi / 180

# ---- the body: a 70 kg, 1.75 m adult, Winter's segment fractions ---------------
BODY = dict(
    I1=0.40,             # trunk about its long axis: a 35 kg cylinder of radius 0.15 m, 0.5 m r^2
    r1=0.226,            # spine to shoulder joint: 0.129 of height
    m2=1.96, L2=0.33,    # upper arm: 2.8 % of body mass, 0.186 of height
    m3=1.54, L3=0.36,    # forearm and hand: 1.6 % + 0.6 %; elbow to the ball
    mb=0.145,            # a baseball
)
# ---- the muscles: isometric torque (N m) and the speed at which it has fallen to zero (rad/s)
TAU0 = (120.0, 80.0, 40.0)        # trunk rotators, shoulder, elbow extensors
WMAX = (15.0, 30.0, 30.0)
# ---- the posture at the start, the joint ranges, and the release point (degrees)
START = (-120.0, -30.0, -100.0)   # trunk angle; shoulder and elbow measured from the link above
STOPS = ((-40.0, 100.0), (-140.0, 5.0))
KSTOP = 400.0                     # N m per radian past the end of range
RELEASE = -15.0                   # the ball leaves when the elbow is 15 degrees short of straight
TRUNK_LIMIT = 60.0                # the throw must be over before the trunk has turned past this


def build():
    t = sp.symbols("t")
    th = [sp.Function(f"th{i}")(t) for i in (1, 2, 3)]
    I1, r1, m2, L2, m3, L3, mb = sp.symbols("I1 r1 m2 L2 m3 L3 mb", positive=True)
    S = sp.Matrix([r1 * sp.cos(th[0]), r1 * sp.sin(th[0])])
    u2 = sp.Matrix([sp.cos(th[1]), sp.sin(th[1])])
    u3 = sp.Matrix([sp.cos(th[2]), sp.sin(th[2])])
    E = S + L2 * u2
    H = E + L3 * u3
    c2, c3 = S + L2 / 2 * u2, E + L3 / 2 * u3
    v = lambda p: p.diff(t)
    half = sp.Rational(1, 2)
    T1 = half * I1 * th[0].diff(t) ** 2
    T2 = half * m2 * v(c2).dot(v(c2)) + half * (m2 * L2**2 / 12) * th[1].diff(t) ** 2
    T3 = half * m3 * v(c3).dot(v(c3)) + half * (m3 * L3**2 / 12) * th[2].diff(t) ** 2 + half * mb * v(H).dot(v(H))
    T = T1 + T2 + T3
    q, w, a = sp.symbols("q1 q2 q3"), sp.symbols("w1 w2 w3"), sp.symbols("a1 a2 a3")
    sub = {}
    for i in range(3):
        sub[th[i].diff(t, 2)] = a[i]
    for i in range(3):
        sub[th[i].diff(t)] = w[i]
    for i in range(3):
        sub[th[i]] = q[i]
    eqs = [sp.simplify((sp.diff(sp.diff(T, th[i].diff(t)), t) - sp.diff(T, th[i])).subs(sub)) for i in range(3)]
    M = sp.Matrix([[sp.diff(e, ai) for ai in a] for e in eqs])
    b = sp.Matrix([sp.simplify(e - sum(M[i, j] * a[j] for j in range(3))) for i, e in enumerate(eqs)])
    pars = (I1, r1, m2, L2, m3, L3, mb)
    return (sp.lambdify((q, w, pars), M, "numpy"), sp.lambdify((q, w, pars), b, "numpy"),
            sp.lambdify((q, w, pars), [x.subs(sub) for x in (T1, T2, T3)], "numpy"),
            sp.lambdify((q, w, pars), [c.subs(sub) for c in v(H)], "numpy"),
            sp.lambdify((q, pars), [c.subs(sub) for c in (*S, *E, *H)], "numpy"))


fM, fb, fT, fVH, fXY = build()
PARS = tuple(BODY[k] for k in ("I1", "r1", "m2", "L2", "m3", "L3", "mb"))


def passive(q):
    """Ligaments and joint capsule: a stiff spring past the end of range. Elastic, so what goes in comes back."""
    out = np.zeros(3)
    for i, phi in ((1, q[1] - q[0]), (2, q[2] - q[1])):
        lo, hi = STOPS[i - 1]
        if phi < lo * D:
            out[i] = KSTOP * (lo * D - phi)
        if phi > hi * D:
            out[i] = -KSTOP * (phi - hi * D)
    return out


def muscles(t, w, tau0, onset, wmax):
    rel = np.array([w[0], w[1] - w[0], w[2] - w[1]])
    out = np.zeros(3)
    for i in range(3):
        if t >= onset[i]:
            out[i] = tau0[i] * (1.0 if wmax is None else float(np.clip(1 - rel[i] / wmax[i], 0.0, 1.0)))
    return out, rel


def throw(onset=(0.0, 0.0, 0.0), tau0=TAU0, wmax=WMAX, tmax=0.8, dense=False):
    q0 = np.array([START[0], START[0] + START[1], START[0] + START[1] + START[2]]) * D

    def rhs(t, y):
        q, w = y[:3], y[3:6]
        tq, rel = muscles(t, w, tau0, onset, wmax)
        tot = tq + passive(q)
        Q = np.array([tot[0] - tot[1], tot[1] - tot[2], tot[2]])
        a = np.linalg.solve(np.array(fM(q, w, PARS), float), Q - np.array(fb(q, w, PARS), float).ravel())
        return np.concatenate([w, a, tq * rel])            # the last three accumulate each muscle group's work

    def released(t, y):
        return (y[2] - y[1]) - RELEASE * D
    released.terminal, released.direction = True, 1
    sol = solve_ivp(rhs, (0, tmax), np.concatenate([q0, np.zeros(6)]), events=released, max_step=5e-4,
                    rtol=1e-8, atol=1e-10, dense_output=dense)
    y = sol.y[:, -1]
    q, w = y[:3], y[3:6]
    ok = sol.status == 1 and q[0] / D <= TRUNK_LIMIT
    ke = np.array(fT(q, w, PARS), float)
    stored = float((passive(q) ** 2).sum() / (2 * KSTOP))
    return dict(ok=bool(ok), t=float(sol.t[-1]), speed=float(np.hypot(*np.array(fVH(q, w, PARS), float))),
                q=q / D, w=w / D, work=y[6:9].copy(), ke=ke, stored=stored, sol=sol, onset=tuple(onset))


def _try(args):
    onset, tau0, wmax = args
    r = throw(onset, tau0, wmax)
    return (r["speed"] if r["ok"] else 0.0), onset


POOL = None


def best_timing(tau0=TAU0, wmax=WMAX, step=0.01, span=0.40):
    """Search the two onset delays on a grid, then polish the best point."""
    grid = np.arange(0.0, span + 1e-9, step)
    jobs = [((0.0, float(t2), float(t3)), tau0, wmax) for t2, t3 in itertools.product(grid, grid)]
    found = list(POOL.map(_try, jobs, chunksize=16)) if POOL else [_try(j) for j in jobs]
    speed, onset = max(found)
    f = lambda x: -_try(((0.0, max(x[0], 0.0), max(x[1], 0.0)), tau0, wmax))[0]
    o = minimize(f, onset[1:], method="Nelder-Mead", options=dict(xatol=5e-4, fatol=5e-3, maxiter=200))
    r = throw((0.0, max(o.x[0], 0.0), max(o.x[1], 0.0)), tau0, wmax)
    return r if r["ok"] and r["speed"] >= speed else throw(onset, tau0, wmax)


def row(r):
    return dict(onset_ms=[round(x * 1000) for x in r["onset"]], release_ms=round(r["t"] * 1000), hand_speed=round(r["speed"], 2),
                hand_kmh=round(r["speed"] * 3.6, 1), work_J=[round(float(x), 1) for x in r["work"]], ke_J=[round(float(x), 1) for x in r["ke"]],
                omega_deg_s=[round(float(x)) for x in r["w"]], elbow_rel_deg_s=round(float(r["w"][2] - r["w"][1])),
                trunk_deg=round(float(r["q"][0])), shoulder_rel_deg=round(float(r["q"][1] - r["q"][0])),
                energy_check=round(float(r["work"].sum() - r["ke"].sum() - r["stored"]), 3))


if __name__ == "__main__":
    POOL = ProcessPoolExecutor(max_workers=max(1, (os.cpu_count() or 2) - 1))
    dump = lambda: (HERE / "kinetic-chain-results.json").write_text(json.dumps(out, indent=1), encoding="utf-8")
    out = {"assumptions": dict(body=BODY, tau0=TAU0, wmax=WMAX, start=START, stops=STOPS, kstop=KSTOP, release=RELEASE)}

    print("E1  all at once against the best sequence")
    together = throw((0, 0, 0))
    seq = best_timing()
    out["together"], out["sequence"] = row(together), row(seq)
    for k in ("together", "sequence"):
        print("  ", k, out[k])

    print("E2  the same, with muscles that do not weaken with speed (constant torque)")
    out["together_const"] = row(throw((0, 0, 0), wmax=None))
    out["sequence_const"] = row(best_timing(wmax=None))
    for k in ("together_const", "sequence_const"):
        print("  ", k, out[k])

    print("E3  a passive elbow: the elbow muscles never fire")
    out["passive_elbow"] = row(best_timing(tau0=(TAU0[0], TAU0[1], 0.0)))
    print("  ", out["passive_elbow"])

    print("E4  timing: the elbow fires early or late by a few hundredths of a second")
    out["timing"] = []
    for d in (-0.06, -0.04, -0.02, 0.0, 0.02, 0.04):
        r = throw((0.0, seq["onset"][1], max(seq["onset"][2] + d, 0.0)))
        out["timing"].append(dict(shift_ms=round(d * 1000), ok=r["ok"], hand_speed=round(r["speed"], 2)))
        print("  ", out["timing"][-1])

    print("E4b the same for the shoulder, the bigger link")
    out["timing_shoulder"] = []
    for d in (-0.06, -0.04, -0.02, 0.0, 0.02, 0.04, 0.06):
        r = throw((0.0, max(seq["onset"][1] + d, 0.0), seq["onset"][2]))
        out["timing_shoulder"].append(dict(shift_ms=round(d * 1000), ok=r["ok"], hand_speed=round(r["speed"], 2)))
        print("  ", out["timing_shoulder"][-1])
    dump()

    print("E5  a weak link: the trunk gives less, and what the arm must then give to throw as fast")
    out["weak_link"] = []
    for f in (1.0, 0.8, 0.6):
        weak = best_timing(tau0=(TAU0[0] * f, TAU0[1], TAU0[2]), step=0.02)
        lo, hi = 1.0, (1.0 if f == 1.0 else 4.0)
        for _ in range(0 if f == 1.0 else 8):   # the factor on shoulder and elbow that restores the speed, to about 1 %
            mid = (lo + hi) / 2
            r = best_timing(tau0=(TAU0[0] * f, TAU0[1] * mid, TAU0[2] * mid), step=0.02)
            lo, hi = (mid, hi) if r["speed"] < seq["speed"] else (lo, mid)
        fixed = best_timing(tau0=(TAU0[0] * f, TAU0[1] * hi, TAU0[2] * hi), step=0.02)
        out["weak_link"].append(dict(trunk_fraction=f, hand_speed=round(weak["speed"], 2), arm_factor_to_restore=round(hi, 2),
                                     arm_work_J=round(float(fixed["work"][1] + fixed["work"][2]), 1),
                                     arm_work_healthy_J=round(float(seq["work"][1] + seq["work"][2]), 1)))
        print("  ", out["weak_link"][-1], flush=True)
        dump()

    print("E6  the ground: how much grip the trunk torque needs, and a throw on ice")
    weight = 70 * 9.81
    out["ground"] = []
    for stance in (0.4, 0.8, 1.3):
        f_each = TAU0[0] / stance
        out["ground"].append(dict(stance_m=stance, friction_each_foot_N=round(f_each), mu_needed=round(2 * f_each / weight, 2)))
        print("  ", out["ground"][-1])
    mu_ice, stance = 0.05, 1.3
    tau_ice = mu_ice * weight / 2 * stance
    ice = best_timing(tau0=(tau_ice, TAU0[1], TAU0[2]), step=0.02)
    out["ice"] = dict(mu=mu_ice, trunk_torque=round(tau_ice, 1), **row(ice))
    print("  ", out["ice"])

    dump()
    POOL.shutdown()
    print("written kinetic-chain-results.json")
