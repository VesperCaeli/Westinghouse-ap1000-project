#!/usr/bin/env python3
"""Foundational integrity checks for AP1000 master registers.

This validator intentionally checks structural completeness only. It does not claim
that the design data itself is complete; that is established by source-by-source
audits and the unresolved-item register.
"""

from __future__ import annotations

import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MASTER = ROOT / "data" / "master"


def read_csv(name: str) -> list[dict[str, str]]:
    path = MASTER / name
    with path.open(newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def nonempty(rows, field):
    return {r[field] for r in rows if r.get(field, "").strip()}


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    objects = read_csv("objects.csv")
    systems = read_csv("systems.csv")
    ports = read_csv("ports.csv")
    connections = read_csv("connections.csv")

    object_ids = nonempty(objects, "object_id")
    system_ids = nonempty(systems, "system_id")
    port_ids = nonempty(ports, "port_id")

    # Duplicate IDs.
    for label, rows, field in [
        ("object", objects, "object_id"),
        ("system", systems, "system_id"),
        ("port", ports, "port_id"),
        ("connection", connections, "connection_id"),
    ]:
        seen: set[str] = set()
        for row in rows:
            value = row.get(field, "").strip()
            if not value:
                errors.append(f"{label}: missing {field}")
            elif value in seen:
                errors.append(f"{label}: duplicate {field}={value}")
            seen.add(value)

    # Parent and system references.
    for row in objects:
        oid = row["object_id"]
        parent = row.get("parent_id", "").strip()
        if parent and parent not in object_ids:
            errors.append(f"object {oid}: unresolved parent_id={parent}")
        system = row.get("system_id", "").strip()
        if system and system not in system_ids:
            errors.append(f"object {oid}: unresolved system_id={system}")

    # Port ownership.
    for row in ports:
        pid = row["port_id"]
        oid = row.get("object_id", "").strip()
        if not oid or oid not in object_ids:
            errors.append(f"port {pid}: unresolved object_id={oid or '<blank>'}")

    # Connection endpoints. No dangling connections are allowed.
    for row in connections:
        cid = row["connection_id"]
        a = row.get("from_port_id", "").strip()
        b = row.get("to_port_id", "").strip()
        if not a or a not in port_ids:
            errors.append(f"connection {cid}: unresolved from_port_id={a or '<blank>'}")
        if not b or b not in port_ids:
            errors.append(f"connection {cid}: unresolved to_port_id={b or '<blank>'}")
        if a and b and a == b:
            errors.append(f"connection {cid}: self-connection at port {a}")

    # Evidence-state sanity checks for factual rows.
    allowed_evidence = {
        "VERIFIED_PUBLIC",
        "CORROBORATED_PUBLIC",
        "DERIVED",
        "REPRESENTATIVE",
        "UNRESOLVED",
        "WITHHELD_OR_PROPRIETARY",
    }
    for label, rows in [("object", objects), ("system", systems), ("port", ports), ("connection", connections)]:
        for row in rows:
            ev = row.get("evidence_state", "").strip()
            if ev and ev not in allowed_evidence:
                errors.append(f"{label} {row.get(next(iter(row)), '?')}: invalid evidence_state={ev}")
            if ev in {"VERIFIED_PUBLIC", "CORROBORATED_PUBLIC", "DERIVED"} and not row.get("source_ids", "").strip():
                warnings.append(f"{label} {row.get(next(iter(row)), '?')}: factual evidence state without source_ids")

    print(f"objects={len(objects)} systems={len(systems)} ports={len(ports)} connections={len(connections)}")
    for msg in warnings:
        print(f"WARNING: {msg}")
    for msg in errors:
        print(f"ERROR: {msg}")

    if errors:
        print(f"FAILED with {len(errors)} error(s) and {len(warnings)} warning(s)")
        return 1

    print(f"PASS with {len(warnings)} warning(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
