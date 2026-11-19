"""Where It Hurts Might Not Be Where It Broke: the code lab.

    python3 where-it-hurts-lab.py

A three-stage pipeline (parse -> load -> report) with one defect in the
first stage. Part 1 runs it and prints the traceback: the program dies in
the last stage. Part 2 walks the chain upstream by checking what each stage
hands to the next, and finds the first stage whose output is wrong. Part 3
fixes the defect where it is, and adds a fail-fast check so that the next
bad record hurts exactly where it breaks.
Every output quoted in the card comes from running this file.
"""
import traceback

RECORDS = ["Ana,78", "Ben,85", "Chen,absent", "Dara,91"]


# ---- the pipeline, with one defect -------------------------------------
def parse(line):
    name, mark = line.split(",")
    if mark.isdigit():
        return name, int(mark)
    # the defect: any other mark falls off the end and returns None


def load(lines):
    return [parse(line) for line in lines]


def top_student(rows):
    return max(rows, key=lambda row: row[1])


# ---- part 1: where it hurts --------------------------------------------
print("PART 1  run the pipeline")
try:
    print(top_student(load(RECORDS)))
except Exception:
    tb = traceback.format_exc().strip().splitlines()
    print("\n".join(tb[-4:]))       # the last frames: where it died


# ---- part 2: walk the chain upstream ------------------------------------
print("\nPART 2  check what each stage hands on")
rows = load(RECORDS)
print("load() returned:", rows)
for line, row in zip(RECORDS, rows):
    ok = isinstance(row, tuple) and isinstance(row[1], int)
    print(f"  parse({line!r:15}) -> {row!r:15} {'ok' if ok else '<- first bad output'}")


# ---- part 3: fix it where it broke, and make the next break hurt there ---
print("\nPART 3  fix the defect; fail fast on anything unexpected")


def parse_fixed(line):
    name, mark = line.split(",")
    if mark.isdigit():
        return name, int(mark)
    if mark == "absent":
        return name, None
    raise ValueError(f"{name}: mark {mark!r} is neither a number nor 'absent'")


def top_student_fixed(rows):
    sat = [row for row in rows if row[1] is not None]
    return max(sat, key=lambda row: row[1])


print(top_student_fixed([parse_fixed(line) for line in RECORDS]))
try:
    parse_fixed("Eve,8O")                   # letter O typed for a zero
except ValueError as err:
    print("ValueError:", err)
