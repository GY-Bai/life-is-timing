#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = (ROOT / "README.md").read_text(encoding="utf-8")
CANON = (ROOT / "CANONICAL_MODEL.md").read_text(encoding="utf-8")

TERMS = [
    "Available-Margin Principle",
    "Binding-Stock Principle",
    "Entry–Re-entry Hysteresis",
    "State-Contingent Leverage Amplification",
    "Exercisable Optionality",
    "Locally Adaptive, Globally Incomplete Experience",
]

errors = []
for term in TERMS:
    if term not in README:
        errors.append(f"README missing canonical term: {term}")
    if term not in CANON:
        errors.append(f"CANONICAL_MODEL missing canonical term: {term}")

if "Phase I" not in README or "Phase I" not in CANON:
    errors.append("Phase I freeze language missing from README or CANONICAL_MODEL")

if errors:
    print("Canonical terminology check FAILED")
    for e in errors:
        print(f"- {e}")
    raise SystemExit(1)

print(f"Canonical terminology OK: {len(TERMS)} V2 terms aligned")
