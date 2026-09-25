#!/usr/bin/env python3
import csv
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "data" / "projects" / "recession_scar_half_life" / "effect_curves.csv"
OUTPUT = ROOT / "data" / "projects" / "recession_scar_half_life" / "derived_metrics.csv"


def empirical_half_life(points):
    points = sorted(points)
    t0, b0 = points[0]
    if b0 == 0:
        return None, False, "zero_reference"
    target = 0.5 * abs(b0)
    prev_t, prev_m = t0, abs(b0)
    for t, b in points[1:]:
        m = abs(b)
        if m <= target:
            if m == prev_m:
                return t, False, "observed"
            frac = (prev_m - target) / (prev_m - m)
            return prev_t + frac * (t - prev_t), True, "interpolated"
        prev_t, prev_m = t, m
    return None, False, "right_censored"


rows = list(csv.DictReader(INPUT.open(newline="", encoding="utf-8")))
groups = defaultdict(list)
meta = {}

for r in rows:
    key = (r["study_id"], r["country"], r["outcome"], r["sample_group"], r["specification_id"])
    meta[key] = r
    if r["analysis_eligible"].lower() == "true":
        groups[key].append((float(r["event_time_years"]), float(r["beta"])))

out = []
for key, pts in sorted(groups.items()):
    m = meta[key]
    # Exclude any eligible subset that changes sign; this is intentionally conservative.
    signs = {1 if b > 0 else -1 if b < 0 else 0 for _, b in pts}
    if len(signs - {0}) > 1:
        out.append({
            "study_id": key[0], "country": key[1], "outcome": key[2],
            "sample_group": key[3], "specification_id": key[4],
            "half_life_years": "", "status": "sign_reversal_excluded",
            "interpolated": "", "last_event_time": max(t for t,_ in pts),
            "event_time_basis": m["event_time_basis"],
            "notes": "Half-life not estimated because eligible points reverse sign."
        })
        continue

    h, interp, status = empirical_half_life(pts)
    out.append({
        "study_id": key[0], "country": key[1], "outcome": key[2],
        "sample_group": key[3], "specification_id": key[4],
        "half_life_years": "" if h is None else f"{h:.6f}",
        "status": status,
        "interpolated": "" if h is None else str(interp).lower(),
        "last_event_time": max(t for t,_ in pts),
        "event_time_basis": m["event_time_basis"],
        "notes": "Descriptive within-study metric; bin midpoints are used where source reports grouped experience."
    })

fields = [
    "study_id","country","outcome","sample_group","specification_id",
    "half_life_years","status","interpolated","last_event_time",
    "event_time_basis","notes"
]
with OUTPUT.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fields)
    w.writeheader()
    w.writerows(out)

print(f"Wrote {len(out)} derived scar metrics to {OUTPUT.relative_to(ROOT)}")
