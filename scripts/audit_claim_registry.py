#!/usr/bin/env python3
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "evidence" / "P0_CLAIMS_REGISTRY.csv"

ALLOWED = {
    "L1_primary_exact_value",
    "L1_primary_plus_derived",
    "L1_primary_abstract",
    "L1_primary_exact_statement",
    "L1_authoritative_exact_statement",
    "L2_design_verified",
}

rows = list(csv.DictReader(REGISTRY.open(newline="", encoding="utf-8")))
ids = [r["claim_id"] for r in rows]

errors = []
if len(ids) != len(set(ids)):
    errors.append("duplicate claim_id detected")

for r in rows:
    if r["verification_level"] not in ALLOWED:
        errors.append(f'{r["claim_id"]}: unknown verification level {r["verification_level"]}')
    if not r["source_url"].startswith("https://"):
        errors.append(f'{r["claim_id"]}: missing https source URL')
    if not r["source_title"].strip():
        errors.append(f'{r["claim_id"]}: missing source title')
    artifact = r["derived_artifact"].strip()
    if artifact and artifact.startswith("/"):
        errors.append(f'{r["claim_id"]}: derived artifact must be repo-relative')

if errors:
    print("P0 claim registry FAILED")
    for e in errors:
        print(f"- {e}")
    raise SystemExit(1)

print(f"P0 claim registry OK: {len(rows)} unique verified claims")
