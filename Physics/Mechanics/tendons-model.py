"""Tendons as Springs: the models behind every number in the card.

    python3 tendons-model.py          # prints the numbers the card quotes, writes tendons-results.json

1. Fibre recruitment. A tendon is many parallel collagen fibres, each crimped
   (wavy) with its own slack. A fibre carries load only once its slack is
   taken up, then obeys sigma = E_f * (strain - slack). With slack spread
   evenly from 0 to eps_toe, the tendon's curve is quadratic up to eps_toe
   (the toe) and straight after it (the linear region): derived, then checked
   by adding up 2000 individual fibres.
2. Energy. Energy stored in a stretched tendon, and what hysteresis costs.
3. The Achilles tendon in running: stress, strain and energy from force,
   area, length and modulus.
4. The spring-mass runner: a point mass on a massless spring leg (the
   spring-loaded inverted pendulum), integrated through one stance; contact
   time, peak force, and the comparison with half a period of simple
   harmonic motion.
5. Power amplification: slow in, fast out.
Every parameter is in P with its source.
"""
import json
import math
from pathlib import Path

import numpy as np
from scipy.integrate import solve_ivp

HERE = Path(__file__).resolve().parent
g = 9.81

P = {
    # material
    "E_Pa": 1.2e9,          # linear-region modulus: 1.22 GPa across 18 species (Pollock & Shadwick 1994); 1.2 GPa TA in vivo
                            # (Maganaris & Paul 1999). Living human Achilles measures lower, 0.38-0.82 GPa (Obst 2020).
    "eps_toe": 0.02,        # end of the toe region: textbook ~2 %; up to ~4 % in vivo (Maganaris & Paul 1999)
    "eps_fail": 0.09,       # failure strain 7.5-9.9 %, excised Achilles (Wren 2001)
    "sigma_fail_Pa": 86e6,  # failure stress 71-86 MPa (Wren 2001); "at least 100 MPa" across species (Bennett 1986)
    "loss_in_vitro": 0.07,  # "dissipates about 7%" (Ker 1981); 8.9 % across species (Pollock & Shadwick 1994)
    "loss_in_vivo": 0.19,   # 18-19 % in vivo (Maganaris & Paul 2000, 2002); contested on method (Finni 2013)
    # Achilles in running at 3.5 m/s (Kharazi et al. 2021): 3.2-3.5 body weights, strain 4.0-4.9 %, recoil 11.2 J
    "achilles_force_N": 2400.0,
    "achilles_area_m2": 65e-6,   # ESTIMATE: 55 mm2 by ultrasound (unconfirmed) to 81 mm2 (implied by Komi 1990)
    "achilles_length_m": 0.20,   # rest length about 200 mm (Kharazi 2021)
    # runner: Moore et al. 2019, 65 kg at 12.7 km/h, contact 0.247 s, leg stiffness 8.38 kN/m
    "mass_kg": 65.0,
    "leg_length_m": 0.90,        # ESTIMATE for a 65 kg adult (hip height)
    "k_leg_N_per_m": 8.38e3,
    "speed_m_s": 12.7 / 3.6,
    "contact_target_s": 0.247,
    "vy_touchdown_m_s": -0.7,    # ASSUMED landing speed, about 0.14 s of flight; contact time is insensitive to it
}


# ---------- 1. fibre recruitment ----------
def sigma_uniform(eps, E=None, eps_toe=None):
    """Closed form for slack uniform on [0, eps_toe]: quadratic toe, then linear."""
    E = P["E_Pa"] if E is None else E
    t = P["eps_toe"] if eps_toe is None else eps_toe
    eps = np.asarray(eps, float)
    return np.where(eps < t, E * eps ** 2 / (2 * t), E * (eps - t / 2))


def sigma_fibres(eps, n=2000, seed=1):
    """Add up n fibres with slack drawn uniformly on [0, eps_toe]; each carries E*(eps - slack) when taut."""
    rng = np.random.default_rng(seed)
    slack = rng.uniform(0, P["eps_toe"], n)
    eps = np.asarray(eps, float)[:, None]
    return (P["E_Pa"] * np.clip(eps - slack, 0, None)).mean(axis=1)


def energy_density(eps):
    """J per m^3 stored up to strain eps: integral of sigma."""
    E, t = P["E_Pa"], P["eps_toe"]
    if eps < t:
        return E * eps ** 3 / (6 * t)
    return E * t ** 2 / 6 + E * ((eps - t / 2) ** 2 - (t / 2) ** 2) / 2


# ---------- 3. Achilles ----------
def achilles(F=None, A=None, L=None):
    F = P["achilles_force_N"] if F is None else F
    A = P["achilles_area_m2"] if A is None else A
    L = P["achilles_length_m"] if L is None else L
    stress = F / A
    # invert the curve for strain
    E, t = P["E_Pa"], P["eps_toe"]
    eps = math.sqrt(2 * t * stress / E) if stress < E * t / 2 else stress / E + t / 2
    U = energy_density(eps) * A * L
    U_linear = F ** 2 * L / (2 * E * A)
    return {"force_N": F, "stress_MPa": stress / 1e6, "strain": eps, "stretch_mm": eps * L * 1000,
            "energy_J": U, "energy_linear_J": U_linear, "safety_factor": P["sigma_fail_Pa"] / stress}


# ---------- 4. spring-mass runner ----------
def stance(k=None, m=None, L0=None, v=None, angle_deg=None, vy0=None):
    """Integrate one stance of the spring-loaded inverted pendulum. Foot at the origin.

    With no angle given, the touchdown angle is solved for a symmetric stance (take-off mirrors touchdown),
    which is what a steady stride needs.
    """
    k = P["k_leg_N_per_m"] if k is None else k
    m = P["mass_kg"] if m is None else m
    L0 = P["leg_length_m"] if L0 is None else L0
    v = P["speed_m_s"] if v is None else v
    vy0 = P["vy_touchdown_m_s"] if vy0 is None else vy0
    if angle_deg is None:
        from scipy.optimize import brentq
        angle_deg = brentq(lambda d: _stance(k, m, L0, v, d, vy0)["takeoff_v"][1] + vy0, 55, 85, xtol=1e-6)
    r = _stance(k, m, L0, v, angle_deg, vy0)
    r["angle_deg"] = angle_deg
    return r


def _stance(k, m, L0, v, angle_deg, vy0):
    a = math.radians(angle_deg)
    x0, y0 = -L0 * math.cos(a), L0 * math.sin(a)

    def f(t, s):
        x, y, vx, vy = s
        L = math.hypot(x, y)
        F = k * max(L0 - L, 0.0)
        return [vx, vy, F * x / L / m, F * y / L / m - g]

    def takeoff(t, s):
        return math.hypot(s[0], s[1]) - L0
    takeoff.terminal, takeoff.direction = True, 1

    sol = solve_ivp(f, (0, 1.0), [x0, y0, v, vy0], events=takeoff, max_step=1e-4, dense_output=True,
                    rtol=1e-9, atol=1e-12)
    T = sol.t_events[0][0]
    t = np.linspace(0, T, 400)
    x, y, vx, vy = sol.sol(t)
    L = np.hypot(x, y)
    Fleg = k * np.clip(L0 - L, 0, None)
    Fy = Fleg * y / L
    return {"contact_s": T, "t": t, "Fy": Fy, "y": y, "L": L, "vx": vx, "vy": vy, "x": x,
            "peak_Fy_N": float(Fy.max()), "peak_Fy_bw": float(Fy.max() / (m * g)),
            "max_compression_m": float((L0 - L).max()), "com_drop_m": float(y[0] - y.min()),
            "takeoff_v": (float(vx[-1]), float(vy[-1])), "k_vert": float(Fy.max() / (y[0] - y.min())),
            "half_period_vert_s": math.pi * math.sqrt(m / (Fy.max() / (y[0] - y.min())))}


def calibrate():
    """Choose the landing speed so that the symmetric stance lasts the measured contact time."""
    from scipy.optimize import brentq
    return brentq(lambda vy: stance(vy0=vy)["contact_s"] - P["contact_target_s"], -1.5, -0.05, xtol=1e-5)


def shm_contact(m, k, v0):
    """Vertical bounce on a spring from natural length: contact = (pi + 2 arcsin(z0/A)) / omega."""
    w = math.sqrt(k / m); z0 = m * g / k; A = math.hypot(z0, v0 / w)
    return (math.pi + 2 * math.asin(z0 / A)) / w, math.pi / w, A


if __name__ == "__main__":
    R = {"params": P}
    eps = np.linspace(0, 0.08, 81)
    R["curve"] = {"eps": eps.tolist(), "closed": sigma_uniform(eps).tolist(), "fibres": sigma_fibres(eps).tolist()}
    err = np.max(np.abs(np.array(R["curve"]["closed"]) - np.array(R["curve"]["fibres"]))) / 1e6
    R["achilles"] = achilles()
    s = stance()
    R["stance"] = {k: v for k, v in s.items() if not isinstance(v, np.ndarray)}
    R["stance_trace"] = {"t": s["t"].tolist(), "Fy": s["Fy"].tolist()}
    R["shm"] = {"contact_s": shm_contact(P["mass_kg"], st_k := R["stance"]["k_vert"], abs(P["vy_touchdown_m_s"]))[0],
                "half_period_s": shm_contact(P["mass_kg"], st_k, abs(P["vy_touchdown_m_s"]))[1]}
    E_in = energy_density(0.045)
    R["loop"] = {"stored_J_per_m3_at_4.5pc": E_in, "lost_in_vitro": P["loss_in_vitro"], "lost_in_vivo": P["loss_in_vivo"]}
    # 5. power amplification, flea (Bennet-Clark & Lucey 1967): 2.25e-7 J in 0.75-1.0 ms
    R["flea"] = {"energy_J": 2.25e-7, "release_s": (0.75e-3, 1.0e-3), "power_W": (2.25e-7 / 1.0e-3, 2.25e-7 / 0.75e-3)}
    (HERE / "tendons-results.json").write_text(json.dumps(R, indent=1))

    print(f"toe region: closed form vs 2000 fibres, max difference {err:.2f} MPa")
    print(f"stress at 2 % (end of toe): {sigma_uniform(0.02) / 1e6:.1f} MPa; at 4 %: {sigma_uniform(0.04) / 1e6:.1f} MPa; "
          f"at 8 %: {sigma_uniform(0.08) / 1e6:.1f} MPa")
    a = R["achilles"]
    print(f"Achilles: {a['force_N']:.0f} N over {P['achilles_area_m2'] * 1e6:.0f} mm2 = {a['stress_MPa']:.0f} MPa, "
          f"strain {100 * a['strain']:.1f} %, stretch {a['stretch_mm']:.1f} mm, energy {a['energy_J']:.1f} J "
          f"(linear spring {a['energy_linear_J']:.1f} J), safety factor {a['safety_factor']:.1f}")
    st = R["stance"]
    print(f"landing speed {P['vy_touchdown_m_s']} m/s; measured contact {P['contact_target_s']} s")
    print(f"stance: contact {1000 * st['contact_s']:.0f} ms, peak vertical force {st['peak_Fy_N']:.0f} N = "
          f"{st['peak_Fy_bw']:.2f} body weights, leg compression {100 * st['max_compression_m']:.1f} cm, "
          f"centre of mass drop {100 * st['com_drop_m']:.1f} cm, k_vert {st['k_vert'] / 1000:.1f} kN/m, "
          f"half period pi*sqrt(m/k_vert) {1000 * st['half_period_vert_s']:.0f} ms, touchdown angle {st['angle_deg']:.1f} deg, "
          f"takeoff v ({st['takeoff_v'][0]:.2f}, {st['takeoff_v'][1]:.2f})")
    print(f"vertical-spring check at k_vert: contact {1000 * R['shm']['contact_s']:.0f} ms vs half period "
          f"{1000 * R['shm']['half_period_s']:.0f} ms")
    print(f"energy density at 4.5 % strain: {R['loop']['stored_J_per_m3_at_4.5pc'] / 1e6:.2f} MJ/m3")
    print("flea power (W):", [f"{x * 1000:.2f} mW" for x in R["flea"]["power_W"]])
