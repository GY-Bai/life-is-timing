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

LEGACY_LABELS = [
    "Fastest Adjustable Margin",
    "Slow Stock Persistence",
    "Entry × Re-entry",
    "Leverage Nonlinearity",
    "Optionality Buffers Scarring",
    "Experience ≠ Historical Distribution",
]

errors = []
for term in TERMS:
    if term not in README:
        errors.append(f"README missing canonical term: {term}")
    if term not in CANON:
        errors.append(f"CANONICAL_MODEL missing canonical term: {term}")

for legacy in LEGACY_LABELS:
    if legacy in README:
        errors.append(f"README still contains legacy V1 label: {legacy}")
    if legacy in CANON:
        errors.append(f"CANONICAL_MODEL still contains legacy V1 label: {legacy}")

if "Phase I" not in README or "Phase I" not in CANON:
    errors.append("Phase I freeze language missing from README or CANONICAL_MODEL")

if errors:
    print("Canonical terminology check FAILED")
    for e in errors:
        print(f"- {e}")
    raise SystemExit(1)

print(f"Canonical terminology OK: {len(TERMS)} V2 terms aligned; no legacy labels")
