#!/usr/bin/env python3
import csv
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "derived" / "china_house_price_drawdown.csv"

rows = list(csv.DictReader(DATA.open(newline="", encoding="utf-8")))
raw = {r["note"]: float(r["value"]) for r in rows if r["claim_id"] == "C009"}
stored = next(float(r["value"]) for r in rows if r["claim_id"] == "C009_DERIVED")

start = raw["2021Q3"]
end = raw["2026Q1"]
computed = (end / start - 1.0) * 100.0

tol = 1e-9
if not math.isclose(computed, stored, rel_tol=0.0, abs_tol=tol):
    raise SystemExit(
        f"C009 mismatch: computed={computed:.12f}, stored={stored:.12f}"
    )

print(f"C009 OK: {start} -> {end} = {computed:.6f}%")
