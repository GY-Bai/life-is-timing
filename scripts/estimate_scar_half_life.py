#!/usr/bin/env python3
"""Estimate empirical scar half-life from an extracted effect curve.

Input CSV must contain at least:
event_time_years,beta

This script intentionally does NOT use p-values to define persistence.
"""
import argparse
import csv
import math
from pathlib import Path


def load_curve(path: Path):
    rows = list(csv.DictReader(path.open(newline="", encoding="utf-8")))
    pts = []
    for r in rows:
        if not r.get("event_time_years") or not r.get("beta"):
            continue
        pts.append((float(r["event_time_years"]), float(r["beta"])))
    pts.sort()
    if len(pts) < 2:
        raise ValueError("need at least two non-empty event-time beta observations")
    return pts


def empirical_half_life(points):
    t0, b0 = points[0]
    if b0 == 0:
        raise ValueError("reference beta is zero")
    target = 0.5 * abs(b0)

    prev_t, prev_m = t0, abs(b0)
    if prev_m <= target:
        return t0, False

    for t, b in points[1:]:
        m = abs(b)
        if m <= target:
            if m == prev_m:
                return t, False
            # Linear interpolation in absolute effect magnitude.
            frac = (prev_m - target) / (prev_m - m)
            return prev_t + frac * (t - prev_t), True
        prev_t, prev_m = t, m

    return None, False


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("csv", type=Path)
    args = ap.parse_args()

    pts = load_curve(args.csv)
    h, interpolated = empirical_half_life(pts)

    if h is None:
        print(f"RIGHT_CENSORED: half-life > {pts[-1][0]:g} years")
    else:
        tag = "interpolated" if interpolated else "observed"
        print(f"HALF_LIFE={h:.6f} years ({tag})")


if __name__ == "__main__":
    main()
