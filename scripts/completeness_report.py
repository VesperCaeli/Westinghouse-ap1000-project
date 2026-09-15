#!/usr/bin/env python3
"""Summarize explicit AP1000 reconstruction completeness audits.

A green structural validation means the database is internally consistent; it does not
mean the plant is complete. This script quantifies explicit remaining work and rejects
impossible completion claims for component-domain, flowpath, and whole-station work-package
controls.
"""

from __future__ import annotations

import csv
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SYSTEMS = ROOT / "data" / "systems"
WORK_PACKAGES = ROOT / "data" / "master" / "work_package_completeness.csv"

COMPLETE_STATES = {"COMPLETE", "PUBLIC_BASELINE_COMPLETE"}
COMPONENT_STATES = COMPLETE_STATES | {"NOT_STARTED", "SEARCH_REQUIRED", "IN_PROGRESS", "PARTIAL", "UNRESOLVED"}
FLOW_COMPLETE_STATES = {"COMPLETE", "PUBLIC_BASELINE_COMPLETE"}
FLOW_INCOMPLETE_STATES = {"INCOMPLETE", "IN_PROGRESS", "PARTIAL", "SEARCH_REQUIRED", "UNRESOLVED", "NOT_STARTED"}
FLOW_CATEGORY_COLUMNS = (
    "isolation_and_alignment",
    "bypass_and_alternate",
    "balancing_restriction_equalization",
    "pressure_vacuum_protection",
    "vents_drains_fill_sample_test",
    "instrumentation_and_actuation",
    "mechanical_construction",
    "maintenance_handling",
)


def read_table(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        fields = reader.fieldnames or []
        rows = [{k: (v or "").strip() for k, v in row.items()} for row in reader]
    return fields, rows


def unresolved_category(value: str) -> bool:
    normalized = value.strip().upper()
    return normalized.startswith(("SEARCH_REQUIRED", "PARTIAL", "UNRESOLVED", "NOT_STARTED", "IN_PROGRESS"))


def main() -> int:
    errors: list[str] = []
    audit_files = sorted(SYSTEMS.rglob("*completeness_audit.csv")) if SYSTEMS.exists() else []
    discovery_files = sorted(SYSTEMS.rglob("*discovery_queue.csv")) if SYSTEMS.exists() else []

    component_by_system: dict[str, Counter[str]] = defaultdict(Counter)
    flow_by_system: dict[str, Counter[str]] = defaultdict(Counter)
    by_domain: Counter[str] = Counter()
    flow_category_status: Counter[str] = Counter()

    component_rows = 0
    component_complete = 0
    flow_rows = 0
    flow_complete = 0

    for path in audit_files:
        system = path.parent.name
        fields, rows = read_table(path)

        if "audit_state" in fields:
            component_rows += len(rows)
            for lineno, row in enumerate(rows, start=2):
                audit_id = row.get("audit_id", f"line-{lineno}")
                state = row.get("audit_state", "").upper()
                status = row.get("status", "").upper()
                evidence = row.get("evidence_state", "").upper()
                domain = row.get("domain", "<unspecified>") or "<unspecified>"

                if state not in COMPONENT_STATES:
                    errors.append(
                        f"{path.relative_to(ROOT)}:{lineno}: {audit_id}: invalid audit_state={state or '<blank>'}"
                    )
                    continue

                component_by_system[system][state] += 1
                by_domain[domain] += 1
                if state in COMPLETE_STATES:
                    component_complete += 1
                    if status in {"SEARCH_REQUIRED", "UNRESOLVED", "IN_PROGRESS"}:
                        errors.append(
                            f"{path.relative_to(ROOT)}:{lineno}: {audit_id}: completion claimed while status={status}"
                        )
                    if evidence in {"UNRESOLVED", "WITHHELD_OR_PROPRIETARY"}:
                        errors.append(
                            f"{path.relative_to(ROOT)}:{lineno}: {audit_id}: completion claimed with evidence_state={evidence}"
                        )

        elif "completion_state" in fields:
            flow_rows += len(rows)
            for lineno, row in enumerate(rows, start=2):
                audit_id = row.get("audit_id", f"line-{lineno}")
                state = row.get("completion_state", "").upper()
                if state not in FLOW_COMPLETE_STATES | FLOW_INCOMPLETE_STATES:
                    errors.append(
                        f"{path.relative_to(ROOT)}:{lineno}: {audit_id}: invalid completion_state={state or '<blank>'}"
                    )
                    continue
                flow_by_system[system][state] += 1
                unresolved = []
                for column in FLOW_CATEGORY_COLUMNS:
                    value = row.get(column, "")
                    if value:
                        prefix = value.split(":", 1)[0].strip().upper()
                        flow_category_status[f"{column}:{prefix}"] += 1
                    if unresolved_category(value):
                        unresolved.append(column)
                if state in FLOW_COMPLETE_STATES:
                    flow_complete += 1
                    if unresolved:
                        errors.append(
                            f"{path.relative_to(ROOT)}:{lineno}: {audit_id}: completion claimed with unresolved categories="
                            + ",".join(unresolved)
                        )
        else:
            errors.append(
                f"{path.relative_to(ROOT)}: completeness audit must contain audit_state or completion_state"
            )

    discovery_rows = 0
    discovery_by_system: Counter[str] = Counter()
    for path in discovery_files:
        _, rows = read_table(path)
        discovery_rows += len(rows)
        discovery_by_system[path.parent.name] += len(rows)

    wp_rows: list[dict[str, str]] = []
    wp_lifecycle: Counter[str] = Counter()
    wp_baseline: Counter[str] = Counter()
    if WORK_PACKAGES.exists():
        _, wp_rows = read_table(WORK_PACKAGES)
        seen: set[str] = set()
        for lineno, row in enumerate(wp_rows, start=2):
            wid = row.get("work_package_id", "")
            if not wid:
                errors.append(f"{WORK_PACKAGES.relative_to(ROOT)}:{lineno}: missing work_package_id")
            elif wid in seen:
                errors.append(f"{WORK_PACKAGES.relative_to(ROOT)}:{lineno}: duplicate work_package_id={wid}")
            seen.add(wid)
            wp_lifecycle[row.get("lifecycle_state", "<blank>") or "<blank>"] += 1
            baseline = row.get("public_baseline_state", "<blank>") or "<blank>"
            wp_baseline[baseline] += 1
            if baseline == "PUBLIC_BASELINE_COMPLETE":
                unresolved_fields = [
                    name for name in (
                        "decomposition_state",
                        "component_audit_state",
                        "cross_system_closure_state",
                    ) if row.get(name, "").upper() not in {"COMPLETE", "PUBLIC_BASELINE_COMPLETE", "NOT_APPLICABLE"}
                ]
                if unresolved_fields:
                    errors.append(
                        f"{WORK_PACKAGES.relative_to(ROOT)}:{lineno}: {wid}: PUBLIC_BASELINE_COMPLETE claimed with unresolved fields="
                        + ",".join(unresolved_fields)
                    )

    print("AP1000 COMPLETENESS REPORT")
    print(
        f"work_packages={len(wp_rows)} audit_files={len(audit_files)} component_audit_rows={component_rows} "
        f"component_complete={component_complete} component_incomplete={component_rows - component_complete} "
        f"flowpath_audit_rows={flow_rows} flowpath_complete={flow_complete} flowpath_incomplete={flow_rows - flow_complete}"
    )

    if wp_rows:
        print("work_package_lifecycle: " + " ".join(f"{k}={wp_lifecycle[k]}" for k in sorted(wp_lifecycle)))
        print("work_package_public_baseline: " + " ".join(f"{k}={wp_baseline[k]}" for k in sorted(wp_baseline)))

    for system in sorted(component_by_system):
        counts = component_by_system[system]
        details = " ".join(f"{state}={counts[state]}" for state in sorted(counts))
        print(f"component_system={system} {details}")
    for system in sorted(flow_by_system):
        counts = flow_by_system[system]
        details = " ".join(f"{state}={counts[state]}" for state in sorted(counts))
        print(f"flowpath_system={system} {details}")

    print(f"discovery_files={len(discovery_files)} discovery_candidates={discovery_rows}")
    for system in sorted(discovery_by_system):
        print(f"discovery_system={system} candidates={discovery_by_system[system]}")

    if by_domain:
        print("component_audit_domains:")
        for domain, count in sorted(by_domain.items()):
            print(f"  {domain}={count}")

    if flow_category_status:
        print("flowpath_category_statuses:")
        for key, count in sorted(flow_category_status.items()):
            print(f"  {key}={count}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        print(f"FAILED with {len(errors)} impossible/malformed completion claim(s)")
        return 1

    audited_total = component_rows + flow_rows
    complete_total = component_complete + flow_complete
    if audited_total == 0:
        print("WARNING: no component/flowpath completeness audits have been created yet")
    elif complete_total == audited_total and all(k == "PUBLIC_BASELINE_COMPLETE" for k in wp_baseline):
        print("ALL AUDITED ITEMS AND WORK PACKAGES CLAIM COMPLETE — perform final unresolved/proprietary/source audit before plant-level closure")
    else:
        print("INCOMPLETE BY DESIGN: green result means progress accounting is internally consistent, not that the plant is finished")

    return 0


if __name__ == "__main__":
    sys.exit(main())
