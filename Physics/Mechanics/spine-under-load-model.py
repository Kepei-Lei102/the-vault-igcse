"""The Spine Under Load: a static model of the base of the spine and the neck.

    python3 spine-under-load-model.py          # prints every number the card quotes, writes the JSON

Everything is moments about one joint, the disc between the last lumbar
vertebra and the sacrum (L5/S1), with the back muscles as one force a
fixed distance behind it. It is the model of The Kinetic Chain, Example 4,
taken further: trunk angle, load distance, the disc as a pressure vessel,
one-sided carrying, a twist, the neck and creep. Every parameter is in P
with its source; the card quotes only numbers printed here.

Outputs: spine-under-load-results.json
"""
import json
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
g = 9.81

P = {
    # the person and the lever (The Kinetic Chain, Example 4)
    "body_kg": 70.0,
    "upper_body_kg": 37.5,       # 0.536 of body mass above L4/L5: Winter Table 4.1, HAT 0.678 less pelvis 0.142
    "upper_body_com_m": 0.28,    # from L5/S1 along the trunk (The Kinetic Chain, Example 4; an estimate)
    "extensor_arm_m": 0.05,      # the textbook single muscle, "5 cm posterior" (McGill & Norman 1987; Chaffin 5.3 cm)
    "lateral_arm_m": 0.05,       # side-bending muscles beside the joint (assumed equal; an estimate)
    "box_kg": 20.0,
    # the disc
    "disc_area_cm2": 18.0,       # L4-L5 disc area, Wilke et al. 1999
    "pressure_factor": 1.5,      # Nachemson 1965: load = pressure / 1.5 x area
    # carrying
    "hand_lateral_m": 0.22,      # a hand at the side, from the midline of the spine
    # the neck
    "head_kg": 5.7,              # head and neck, 0.081 of body mass (Winter)
    "head_com_m": 0.16,          # "16cm above C7" (Hansraj 2014)
    "neck_extensor_arm_m": 0.04, # ASSUMED: no open source found; Hansraj's 60 degree figures imply about 4 cm
    # guideline
    "niosh_N": 3400.0,           # Waters et al. 1993: "defines an increased risk of low-back injury"
}


def lift(theta_deg, box_kg, box_dist_m, trunk_com_frac=1.0):
    """Stoop or squat: trunk at theta from vertical, box held box_dist_m in front of L5/S1 (horizontally).

    Returns the moment, muscle force and the compression and shear on the disc, taking the disc
    plane perpendicular to the trunk. Shear is the part of the weights across the disc; the
    single-muscle model has no muscle pulling across it.
    """
    th = math.radians(theta_deg)
    Wu, Wb = P["upper_body_kg"] * g, box_kg * g
    r = P["upper_body_com_m"] * trunk_com_frac
    moment = Wu * r * math.sin(th) + Wb * box_dist_m
    muscle = moment / P["extensor_arm_m"]
    compression = muscle + (Wu + Wb) * math.cos(th)
    shear = (Wu + Wb) * math.sin(th)
    return {"theta": theta_deg, "box_kg": box_kg, "box_dist_m": box_dist_m, "moment_Nm": moment,
            "muscle_N": muscle, "compression_N": compression, "shear_N": shear,
            "pressure_MPa": pressure(compression)}


def pressure(force_N):
    return P["pressure_factor"] * force_N / (P["disc_area_cm2"] * 1e-4) / 1e6


def carry(masses_kg):
    """Walking upright with a load in each hand, (left, right). Side-bending moment about L5/S1."""
    Wu = P["upper_body_kg"] * g
    left, right = masses_kg
    lateral_moment = abs(left - right) * g * P["hand_lateral_m"]
    muscle = lateral_moment / P["lateral_arm_m"]
    compression = Wu + (left + right) * g + muscle
    return {"left_kg": left, "right_kg": right, "lateral_moment_Nm": lateral_moment, "muscle_N": muscle,
            "compression_N": compression}


def twist(theta_deg, box_kg, forward_m, side_m):
    """Box held forward and to one side with the trunk flexed: the moment has a forward and a sideways part.

    Each part is balanced by its own muscles (extensors, side-benders), and both pull down along the spine.
    """
    th = math.radians(theta_deg)
    Wu, Wb = P["upper_body_kg"] * g, box_kg * g
    m_sag = Wu * P["upper_body_com_m"] * math.sin(th) + Wb * forward_m
    m_lat = Wb * side_m
    compression = m_sag / P["extensor_arm_m"] + m_lat / P["lateral_arm_m"] + (Wu + Wb) * math.cos(th)
    return {"theta": theta_deg, "forward_m": forward_m, "side_m": side_m, "sagittal_Nm": m_sag,
            "lateral_Nm": m_lat, "compression_N": compression}


def neck(phi_deg):
    """Head bowed phi from upright. Extensor force and compression at the lower neck; 'effective weight' in kg."""
    ph = math.radians(phi_deg)
    W = P["head_kg"] * g
    moment = W * P["head_com_m"] * math.sin(ph)
    muscle = moment / P["neck_extensor_arm_m"]
    compression = muscle + W * math.cos(ph)
    return {"phi": phi_deg, "muscle_N": muscle, "compression_N": compression, "effective_kg": compression / g}


CREEP = {"loss_mm": 19.3, "fast": 0.6, "tau_fast_h": 0.6, "tau_slow_h": 4.0, "tau_night_h": 3.3, "day_h": 16.0}
# Tyrrell, Reilly & Troup 1985: 19.3 mm a day, 54 % of it in the first hour, 80 % by three hours,
# about 70 % regained in the first half of the night. Two exponentials fitted by hand to those points.


def creep_day(t):
    c = CREEP
    return c["loss_mm"] * (c["fast"] * (1 - math.exp(-t / c["tau_fast_h"]))
                           + (1 - c["fast"]) * (1 - math.exp(-t / c["tau_slow_h"])))


def creep(hours):
    c = CREEP
    end = creep_day(c["day_h"])
    return [creep_day(t % 24) if t % 24 <= c["day_h"] else end * math.exp(-((t % 24) - c["day_h"]) / c["tau_night_h"])
            for t in hours]


if __name__ == "__main__":
    R = {"params": P}

    # 1. stoop against squat, the Kinetic Chain pair and a range of angles
    R["stoop_level"] = lift(90, 20, 0.45)
    R["squat_close"] = lift(30, 20, 0.25)
    # stooping, the box hangs below the shoulders: 0.45 m out when the trunk is level, never closer than 0.12 m
    R["stoop_curve"] = [lift(t, 20, max(0.12, 0.45 * math.sin(math.radians(t)))) for t in range(0, 91, 5)]
    R["squat_close_curve"] = [lift(t, 20, 0.25) for t in range(0, 91, 5)]
    R["squat_far"] = lift(30, 20, 0.45)          # squatting but the box still at arm's length
    R["upright_close"] = lift(0, 20, 0.10)
    R["standing"] = lift(0, 0, 0.0)
    R["bent_no_load"] = lift(90, 0, 0.0)
    R["box_distance_sweep"] = [lift(30, 20, d / 100) for d in range(10, 61, 5)]

    # 2. the disc as a pressure vessel
    R["pressure_table"] = {k: round(R[k]["pressure_MPa"], 2) for k in
                           ("standing", "upright_close", "squat_close", "stoop_level", "bent_no_load")}

    # 3. carrying: McGill, Marshall & Andersen 2013 measured > 2800 N (30 kg in one hand), 1570 N (15 + 15)
    R["carry"] = [carry((30, 0)), carry((15, 15)), carry((20, 0)), carry((10, 10)), carry((0, 0))]
    R["carry_measured_N"] = {"30+0": 2800, "15+15": 1570}

    # 2b. the model against Wilke et al. 1999 (one man, 70 kg, L4-L5), pressures in MPa
    R["wilke"] = [
        ("standing, relaxed", 0.50, lift(0, 0, 0)["pressure_MPa"]),
        ("holding 20 kg close", 1.10, lift(0, 20, 0.10)["pressure_MPa"]),
        ("lifting 20 kg, knees bent", 1.70, lift(30, 20, 0.25)["pressure_MPa"]),
        ("holding 20 kg 60 cm out", 1.80, lift(0, 20, 0.60)["pressure_MPa"]),
        ("lifting 20 kg, round back", 2.30, lift(90, 20, 0.45)["pressure_MPa"]),
    ]
    R["wilke_round_back_force_N"] = 2.30e6 * 18e-4 / 1.5

    # 4. twist
    R["twist"] = [twist(30, 20, 0.25, 0.0), twist(30, 20, 0.25, 0.25)]

    # 5. neck
    R["neck"] = [neck(p) for p in (0, 15, 30, 45, 60)]

    # 6. creep
    hours = [h / 4 for h in range(0, 24 * 4 + 1)]
    R["creep"] = {"hours": hours, "loss_mm": creep(hours)}

    # 7. Borelli's porter, Proposition LXI: 1239 Roman pounds in the disc, the libbra at 339 g
    R["borelli_disc_N"] = 1239 * 0.339 * g

    (HERE / "spine-under-load-results.json").write_text(json.dumps(R, indent=1))

    f = lambda x: f"{x:,.0f}"
    print("STOOP (trunk level, box 0.45 m):", {k: f(v) for k, v in R["stoop_level"].items() if k.endswith("N") or k.endswith("Nm")},
          f"p = {R['stoop_level']['pressure_MPa']:.2f} MPa")
    print("SQUAT (30 deg, box 0.25 m):     ", {k: f(v) for k, v in R["squat_close"].items() if k.endswith("N") or k.endswith("Nm")},
          f"p = {R['squat_close']['pressure_MPa']:.2f} MPa")
    print("SQUAT but box far (0.45 m):     ", f(R["squat_far"]["compression_N"]), "N")
    print("upright, box hugged (0.10 m):   ", f(R["upright_close"]["compression_N"]), "N")
    print("bent level, no box:             ", f(R["bent_no_load"]["compression_N"]), "N")
    print("standing, nothing:              ", f(R["standing"]["compression_N"]), "N")
    print("box distance sweep at 30 deg:   ", [(r["box_dist_m"], f(r["compression_N"])) for r in R["box_distance_sweep"]])
    print("pressures (MPa):                ", R["pressure_table"])
    for c in R["carry"]:
        print("carry", c["left_kg"], "+", c["right_kg"], "kg:", f(c["compression_N"]), "N  (side muscles", f(c["muscle_N"]), "N)")
    for t in R["twist"]:
        print(f"twist side {t['side_m']} m:", f(t["compression_N"]), "N")
    for n in R["neck"]:
        print(f"neck {n['phi']:>2} deg: muscle {f(n['muscle_N'])} N, compression {f(n['compression_N'])} N = {n['effective_kg']:.1f} kg")
    cl = R["creep"]["loss_mm"]
    print("creep: fraction of 19.3 mm at 1 h, 3 h:", round(cl[4] / 19.3, 2), round(cl[12] / 19.3, 2),
          "| at 16 h", round(cl[64], 1), "mm | regained by 20 h (half the night):", round(1 - cl[80] / cl[64], 2))
    for name, meas, model in R["wilke"]:
        print(f"Wilke {name:28} measured {meas:.2f} MPa  model {model:.2f} MPa  ratio {model / meas:.2f}")
    print("Wilke round back as force:", f(R["wilke_round_back_force_N"]), "N")
    print("Borelli's disc:", f(R["borelli_disc_N"]), "N")
