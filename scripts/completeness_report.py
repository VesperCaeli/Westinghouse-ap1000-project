#!/usr/bin/env python3
"""Summarize explicit AP1000 reconstruction completeness audits.

This report is intentionally different from validate_registers.py. A green structural
validation means the database is internally consistent; it does not mean the plant is
complete. This script quantifies the remaining audited work and rejects impossible
completion claims.
"""

from __future__ import annotations

import csv
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SYSTEMS = ROOT / "data" / "systems"

COMPLETE_STATES = {"COMPLETE", "PUBLIC_BASELINE_COMPLETE"}
INCOMPLETE_STATES = {"NOT_STARTED", "SEARCH_REQUIRED", "IN_PROGRESS", "PARTIAL", "UNRESOLVED"}
ALLOWED_AUDIT_STATES = COMPLETE_STATES | INCOMPLETE_STATES


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as f:
        return [{k: (v or "").strip() for k, v in row.items()} for row in csv.DictReader(f)]


def main() -> int:
    errors: list[str] = []
    audit_files = sorted(SYSTEMS.rglob("*completeness_audit.csv")) if SYSTEMS.exists() else []
    discovery_files = sorted(SYSTEMS.rglob("*discovery_queue.csv")) if SYSTEMS.exists() else []

    by_system: dict[str, Counter[str]] = defaultdict(Counter)
    by_domain: Counter[str] = Counter()
    total_rows = 0
    complete_rows = 0

    for path in audit_files:
        system = path.parent.name
        rows = read_rows(path)
        total_rows += len(rows)
        for lineno, row in enumerate(rows, start=2):
            audit_id = row.get("audit_id", f"line-{lineno}")
            state = row.get("audit_state", "").upper()
            status = row.get("status", "").upper()
            evidence = row.get("evidence_state", "").upper()
            domain = row.get("domain", "<unspecified>") or "<unspecified>"

            if state not in ALLOWED_AUDIT_STATES:
                errors.append(f"{path.relative_to(ROOT)}:{lineno}: {audit_id}: invalid audit_state={state or '<blank>'}")
                continue

            by_system[system][state] += 1
            by_domain[domain] += 1
            if state in COMPLETE_STATES:
                complete_rows += 1
                if status in {"SEARCH_REQUIRED", "UNRESOLVED", "IN_PROGRESS"}:
                    errors.append(
                        f"{path.relative_to(ROOT)}:{lineno}: {audit_id}: completion claimed while status={status}"
                    )
                if evidence in {"UNRESOLVED", "WITHHELD_OR_PROPRIETARY"}:
                    errors.append(
                        f"{path.relative_to(ROOT)}:{lineno}: {audit_id}: completion claimed with evidence_state={evidence}"
                    )

    discovery_rows = 0
    discovery_by_system: Counter[str] = Counter()
    for path in discovery_files:
        rows = read_rows(path)
        discovery_rows += len(rows)
        discovery_by_system[path.parent.name] += len(rows)

    print("AP1000 COMPLETENESS REPORT")
    print(f"audit_files={len(audit_files)} audit_rows={total_rows} complete_rows={complete_rows} incomplete_rows={total_rows - complete_rows}")
    for system in sorted(by_system):
        counts = by_system[system]
        details = " ".join(f"{state}={counts[state]}" for state in sorted(counts))
        print(f"system={system} {details}")

    print(f"discovery_files={len(discovery_files)} discovery_candidates={discovery_rows}")
    for system in sorted(discovery_by_system):
        print(f"discovery_system={system} candidates={discovery_by_system[system]}")

    if by_domain:
        print("audit_domains:")
        for domain, count in sorted(by_domain.items()):
            print(f"  {domain}={count}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        print(f"FAILED with {len(errors)} impossible/malformed completion claim(s)")
        return 1

    if total_rows == 0:
        print("WARNING: no component completeness audits have been created yet")
    elif complete_rows == total_rows:
        print("ALL AUDITED DOMAINS CLAIM COMPLETE — perform final unresolved/proprietary/source audit before plant-level closure")
    else:
        print("INCOMPLETE BY DESIGN: green result means progress accounting is internally consistent, not that the plant is finished")

    return 0


if __name__ == "__main__":
    sys.exit(main())
