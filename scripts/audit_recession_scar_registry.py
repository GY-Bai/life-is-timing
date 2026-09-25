#!/usr/bin/env python3
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REG = ROOT / "data" / "projects" / "recession_scar_half_life" / "study_registry.csv"

required = {
    "study_id","country","study","publication_year","publication",
    "doi_or_url","sample_or_cohorts","entry_exposure","primary_outcome",
    "author_reported_persistence","design_bucket","raw_data_access","phase2_status"
}
allowed_buckets = {"A","B","C","D"}

rows = list(csv.DictReader(REG.open(newline="", encoding="utf-8")))
errors = []

if not rows:
    errors.append("registry is empty")

ids = [r.get("study_id","") for r in rows]
if len(ids) != len(set(ids)):
    errors.append("duplicate study_id")

missing_cols = required - set(rows[0].keys() if rows else [])
if missing_cols:
    errors.append("missing columns: " + ", ".join(sorted(missing_cols)))

for r in rows:
    sid = r.get("study_id","<unknown>")
    for col in required:
        if not r.get(col,"").strip():
            errors.append(f"{sid}: missing {col}")
    if r.get("design_bucket") not in allowed_buckets:
        errors.append(f"{sid}: invalid design_bucket={r.get('design_bucket')}")
    url = r.get("doi_or_url","")
    if not url.startswith("https://"):
        errors.append(f"{sid}: source must be https URL")

if errors:
    print("Recession scar study registry FAILED")
    for e in errors:
        print("- " + e)
    raise SystemExit(1)

print(f"Recession scar study registry OK: {len(rows)} studies")
