#!/usr/bin/env python3
"""Integrity checks for AP1000 reconstruction registers.

The validator enforces database/research integrity. It does not assert that public
engineering data is complete; unresolved design content remains controlled through
UNRESOLVED/WITHHELD dispositions and source-by-source audits.
"""

from __future__ import annotations

import csv
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MASTER = ROOT / "data" / "master"
SYSTEMS = ROOT / "data" / "systems"
SOURCE_REGISTER = ROOT / "docs" / "01_SOURCE_REGISTER.md"

ALLOWED_EVIDENCE = {
    "VERIFIED_PUBLIC",
    "CORROBORATED_PUBLIC",
    "DERIVED",
    "REPRESENTATIVE",
    "UNRESOLVED",
    "WITHHELD_OR_PROPRIETARY",
}
FACTUAL_EVIDENCE = {"VERIFIED_PUBLIC", "CORROBORATED_PUBLIC", "DERIVED"}
NONCONNECTED_PORT_STATUSES = {
    "BOUNDARY",
    "UNRESOLVED",
    "REFERENCE",
    "REFERENCE_FOUND",
    "CONFIRMED_ABSENT",
    "SEED",
}
PRIMARY_KEY_PRIORITY = (
    "object_id",
    "system_id",
    "port_id",
    "connection_id",
    "item_id",
    "record_id",
    "document_map_id",
    "line_group_id",
    "hx_id",
)


def read_csv_path(path: Path, errors: list[str]) -> tuple[list[str], list[dict[str, str]]]:
    try:
        with path.open(newline="", encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)
            fields = reader.fieldnames or []
            if not fields:
                errors.append(f"{path.relative_to(ROOT)}: missing CSV header")
                return [], []
            duplicates = [name for name, count in Counter(fields).items() if count > 1]
            if duplicates:
                errors.append(
                    f"{path.relative_to(ROOT)}: duplicate header field(s): {', '.join(duplicates)}"
                )
            rows: list[dict[str, str]] = []
            for lineno, raw in enumerate(reader, start=2):
                if None in raw:
                    errors.append(
                        f"{path.relative_to(ROOT)}:{lineno}: extra column(s) beyond header"
                    )
                    raw.pop(None, None)
                row = {str(k): (v or "") for k, v in raw.items()}
                if any(value.strip() for value in row.values()):
                    rows.append(row)
            return fields, rows
    except FileNotFoundError:
        errors.append(f"missing required file: {path.relative_to(ROOT)}")
        return [], []


def read_master(name: str, errors: list[str]) -> tuple[list[str], list[dict[str, str]]]:
    return read_csv_path(MASTER / name, errors)


def nonempty(rows: list[dict[str, str]], field: str) -> set[str]:
    return {r.get(field, "").strip() for r in rows if r.get(field, "").strip()}


def parse_source_ids() -> set[str]:
    if not SOURCE_REGISTER.exists():
        return set()
    text = SOURCE_REGISTER.read_text(encoding="utf-8")
    return set(re.findall(r"\|\s*(SRC-\d+)\s*\|", text))


def split_source_ids(value: str) -> list[str]:
    return [part.strip() for part in value.split(";") if part.strip()]


def choose_primary_key(fields: list[str]) -> str | None:
    # System-local research tables are deliberately designed with their row key
    # as the first column. Respect that first, otherwise a ports table would
    # incorrectly use its repeated owner object_id instead of unique port_id.
    if fields:
        first = fields[0]
        if first.endswith("_id") and first not in {"parent_id", "source_ids"}:
            return first
    for field in PRIMARY_KEY_PRIORITY:
        if field in fields:
            return field
    return None


def validate_common_table(
    path: Path,
    fields: list[str],
    rows: list[dict[str, str]],
    source_ids: set[str],
    errors: list[str],
    warnings: list[str],
) -> None:
    rel = path.relative_to(ROOT)
    key = choose_primary_key(fields)

    if key:
        seen: set[str] = set()
        for lineno, row in enumerate(rows, start=2):
            value = row.get(key, "").strip()
            if not value:
                errors.append(f"{rel}:{lineno}: missing primary key {key}")
            elif value in seen:
                errors.append(f"{rel}:{lineno}: duplicate {key}={value}")
            seen.add(value)

    if "evidence_state" in fields:
        for lineno, row in enumerate(rows, start=2):
            ev = row.get("evidence_state", "").strip()
            identity = row.get(key or fields[0], "?").strip() or "?"
            if ev and ev not in ALLOWED_EVIDENCE:
                errors.append(f"{rel}:{lineno}: {identity}: invalid evidence_state={ev}")
            if ev in FACTUAL_EVIDENCE and not row.get("source_ids", "").strip():
                errors.append(f"{rel}:{lineno}: {identity}: factual evidence state without source_ids")
            if ev in FACTUAL_EVIDENCE and "source_locator" in fields and not row.get("source_locator", "").strip():
                warnings.append(f"{rel}:{lineno}: {identity}: factual row without source_locator")

    if "source_ids" in fields:
        for lineno, row in enumerate(rows, start=2):
            identity = row.get(key or fields[0], "?").strip() or "?"
            for sid in split_source_ids(row.get("source_ids", "")):
                if not re.fullmatch(r"SRC-\d+", sid):
                    errors.append(f"{rel}:{lineno}: {identity}: malformed source id {sid}")
                elif sid not in source_ids:
                    errors.append(f"{rel}:{lineno}: {identity}: undefined source id {sid}")


def validate_master(
    source_ids: set[str], errors: list[str], warnings: list[str]
) -> tuple[set[str], set[str]]:
    object_fields, objects = read_master("objects.csv", errors)
    system_fields, systems = read_master("systems.csv", errors)
    port_fields, ports = read_master("ports.csv", errors)
    connection_fields, connections = read_master("connections.csv", errors)

    for filename, fields, rows in (
        ("objects.csv", object_fields, objects),
        ("systems.csv", system_fields, systems),
        ("ports.csv", port_fields, ports),
        ("connections.csv", connection_fields, connections),
    ):
        validate_common_table(MASTER / filename, fields, rows, source_ids, errors, warnings)

    object_ids = nonempty(objects, "object_id")
    system_ids = nonempty(systems, "system_id")
    port_ids = nonempty(ports, "port_id")

    for row in objects:
        oid = row.get("object_id", "").strip()
        parent = row.get("parent_id", "").strip()
        if parent and parent not in object_ids:
            errors.append(f"data/master/objects.csv: object {oid}: unresolved parent_id={parent}")
        system = row.get("system_id", "").strip()
        if system and system not in system_ids:
            errors.append(f"data/master/objects.csv: object {oid}: unresolved system_id={system}")

    for row in ports:
        pid = row.get("port_id", "").strip()
        oid = row.get("object_id", "").strip()
        if not oid or oid not in object_ids:
            errors.append(f"data/master/ports.csv: port {pid}: unresolved object_id={oid or '<blank>'}")

    for row in connections:
        cid = row.get("connection_id", "").strip()
        a = row.get("from_port_id", "").strip()
        b = row.get("to_port_id", "").strip()
        if not a or a not in port_ids:
            errors.append(f"data/master/connections.csv: connection {cid}: unresolved from_port_id={a or '<blank>'}")
        if not b or b not in port_ids:
            errors.append(f"data/master/connections.csv: connection {cid}: unresolved to_port_id={b or '<blank>'}")
        if a and b and a == b:
            errors.append(f"data/master/connections.csv: connection {cid}: self-connection at port {a}")

    return object_ids, system_ids


def validate_local_graph(
    system_dir: Path,
    master_object_ids: set[str],
    master_system_ids: set[str],
    errors: list[str],
) -> None:
    inventory_path = system_dir / "major_inventory.csv"
    ports_path = system_dir / "ports.csv"
    connections_path = system_dir / "connections.csv"

    if not any(path.exists() for path in (inventory_path, ports_path, connections_path)):
        return

    inventory_fields, inventory = read_csv_path(inventory_path, errors) if inventory_path.exists() else ([], [])
    port_fields, ports = read_csv_path(ports_path, errors) if ports_path.exists() else ([], [])
    connection_fields, connections = (
        read_csv_path(connections_path, errors) if connections_path.exists() else ([], [])
    )

    if ports_path.exists() or connections_path.exists():
        if not inventory_path.exists():
            errors.append(f"{system_dir.relative_to(ROOT)}: strict graph has ports/connections but no major_inventory.csv")
        if not ports_path.exists():
            errors.append(f"{system_dir.relative_to(ROOT)}: strict graph has connections but no ports.csv")
        if ports_path.exists() and not connections_path.exists():
            errors.append(f"{system_dir.relative_to(ROOT)}: strict graph has ports but no connections.csv")

    object_ids = nonempty(inventory, "object_id")
    port_ids = nonempty(ports, "port_id")

    if inventory and "object_id" not in inventory_fields:
        errors.append(f"{inventory_path.relative_to(ROOT)}: strict inventory requires object_id")
    if ports and not {"port_id", "object_id"}.issubset(port_fields):
        errors.append(f"{ports_path.relative_to(ROOT)}: strict ports require port_id and object_id")
    if connections and not {"connection_id", "from_port_id", "to_port_id"}.issubset(connection_fields):
        errors.append(
            f"{connections_path.relative_to(ROOT)}: strict connections require connection_id/from_port_id/to_port_id"
        )

    for row in inventory:
        oid = row.get("object_id", "").strip()
        parent = row.get("parent_id", "").strip()
        if parent and parent not in object_ids and parent not in master_object_ids:
            errors.append(f"{inventory_path.relative_to(ROOT)}: object {oid}: unresolved parent_id={parent}")
        system = row.get("system_id", "").strip()
        if system and system not in master_system_ids:
            errors.append(f"{inventory_path.relative_to(ROOT)}: object {oid}: unresolved system_id={system}")

    connected_ports: set[str] = set()
    for row in ports:
        pid = row.get("port_id", "").strip()
        owner = row.get("object_id", "").strip()
        if not owner or (owner not in object_ids and owner not in master_object_ids):
            errors.append(f"{ports_path.relative_to(ROOT)}: port {pid}: unresolved object_id={owner or '<blank>'}")

    for row in connections:
        cid = row.get("connection_id", "").strip()
        a = row.get("from_port_id", "").strip()
        b = row.get("to_port_id", "").strip()
        if not a or a not in port_ids:
            errors.append(f"{connections_path.relative_to(ROOT)}: connection {cid}: unresolved from_port_id={a or '<blank>'}")
        else:
            connected_ports.add(a)
        if not b or b not in port_ids:
            errors.append(f"{connections_path.relative_to(ROOT)}: connection {cid}: unresolved to_port_id={b or '<blank>'}")
        else:
            connected_ports.add(b)
        if a and b and a == b:
            errors.append(f"{connections_path.relative_to(ROOT)}: connection {cid}: self-connection at port {a}")

    for row in ports:
        pid = row.get("port_id", "").strip()
        status = row.get("status", "").strip().upper()
        if pid and pid not in connected_ports and status not in NONCONNECTED_PORT_STATUSES:
            errors.append(
                f"{ports_path.relative_to(ROOT)}: port {pid}: orphaned (no connection and status={status or '<blank>'})"
            )


def validate_system_tables(
    source_ids: set[str],
    master_object_ids: set[str],
    master_system_ids: set[str],
    errors: list[str],
    warnings: list[str],
) -> tuple[int, int]:
    table_count = 0
    row_count = 0
    if not SYSTEMS.exists():
        warnings.append("data/systems directory does not exist")
        return table_count, row_count

    for path in sorted(SYSTEMS.rglob("*.csv")):
        fields, rows = read_csv_path(path, errors)
        table_count += 1
        row_count += len(rows)
        validate_common_table(path, fields, rows, source_ids, errors, warnings)

    for system_dir in sorted(p for p in SYSTEMS.iterdir() if p.is_dir()):
        validate_local_graph(system_dir, master_object_ids, master_system_ids, errors)

    return table_count, row_count


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    source_ids = parse_source_ids()
    if not source_ids:
        errors.append("docs/01_SOURCE_REGISTER.md: no controlled SRC-* identifiers found")

    master_object_ids, master_system_ids = validate_master(source_ids, errors, warnings)
    table_count, row_count = validate_system_tables(
        source_ids, master_object_ids, master_system_ids, errors, warnings
    )

    print(
        f"controlled_sources={len(source_ids)} master_objects={len(master_object_ids)} "
        f"master_systems={len(master_system_ids)} system_tables={table_count} system_rows={row_count}"
    )
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
