# AP1000 Register Validation Contract

## Purpose

The reconstruction database is intentionally allowed to grow from source-discovery tables into strict engineering graphs. CI must therefore distinguish between **research registers** and **strict connected-system registers** while still preventing silent corruption at every stage.

This document defines the validation contract enforced by `scripts/validate_registers.py`.

## Layer 1 — all CSV registers

Every CSV under `data/systems/**` is checked automatically.

Required integrity rules:

- CSV header must exist and may not contain duplicate field names.
- Rows may not contain extra columns beyond the declared header.
- If the first column is an `*_id` field, it is the row primary key and must be nonblank and unique within that file.
- `evidence_state`, where present, must be one of:
  - `VERIFIED_PUBLIC`
  - `CORROBORATED_PUBLIC`
  - `DERIVED`
  - `REPRESENTATIVE`
  - `UNRESOLVED`
  - `WITHHELD_OR_PROPRIETARY`
- `VERIFIED_PUBLIC`, `CORROBORATED_PUBLIC`, and `DERIVED` rows must contain at least one `source_ids` reference.
- Every semicolon-separated `SRC-*` in `source_ids` must exist in `docs/01_SOURCE_REGISTER.md`.
- Malformed or undefined source IDs are CI failures.
- A factual row with a `source_locator` column but no locator generates a warning and must be closed during source audit.

This layer is deliberately schema-agnostic enough to support fabrication ledgers, document maps, material ledgers, valve-tag registers, dimensional overlays and other research tables before they are promoted into a complete object graph.

## Layer 2 — master plant graph

The canonical files in `data/master/` remain strict:

- `objects.csv`
- `systems.csv`
- `ports.csv`
- `connections.csv`

CI rejects:

- duplicate/missing IDs;
- unresolved object parents;
- unresolved object system references;
- ports whose owning object does not exist;
- connections whose `from_port_id` or `to_port_id` does not exist;
- self-connections;
- invalid evidence/source metadata.

The master graph is not allowed to contain a dangling physical interface.

## Layer 3 — strict local system graphs

A system directory is automatically treated as a strict connected graph when it publishes any of the canonical local graph files:

- `major_inventory.csv`
- `ports.csv`
- `connections.csv`

If a system publishes ports or connections, it must provide the complete object → port → connection chain.

For strict system graphs CI rejects:

- `ports.csv` or `connections.csv` without `major_inventory.csv`;
- `connections.csv` without `ports.csv`;
- `ports.csv` without `connections.csv`;
- unresolved local object parents unless the parent exists in the master object register;
- unresolved `system_id` values;
- ports owned by nonexistent local/master objects;
- connections referencing nonexistent ports;
- self-connections;
- ports that participate in no connection unless explicitly dispositioned as a boundary/reference/unresolved/seed/confirmed-absent interface.

This is the first enforcement layer for the project's **zero-orphan** requirement.

## Promotion rule

Research tables are not exempt from eventual normalization.

As a work package matures:

1. source-discovery/fabrication rows identify real equipment and interfaces;
2. those items receive stable canonical object IDs;
3. physical/electrical/control interfaces receive stable port IDs;
4. all interfaces are represented in connection rows;
5. the system is promoted to the strict local graph;
6. after reconciliation, canonical objects/connections may be compiled into the master plant graph.

A work package cannot be declared `PUBLIC_BASELINE_COMPLETE` while important public-source hardware remains only in an unconnected research table.

## Boundary rule

A port may remain intentionally unconnected only when its status makes the disposition explicit, such as:

- `BOUNDARY`
- `UNRESOLVED`
- `REFERENCE`
- `REFERENCE_FOUND`
- `SEED`
- `CONFIRMED_ABSENT`

This is temporary configuration control, not permission to omit the downstream system. A plant boundary remains open until the owning work package closes it or records a named external boundary.

## Future hardening

As more AP1000 systems mature, the validator will be expanded to enforce object-class-specific interface rules. Planned hard failures include:

- pump without suction and discharge;
- motor without electrical supply and mechanical load;
- valve without two process endpoints, except documented vent/drain/relief/end devices;
- instrument without process sensing plus signal/power interfaces as applicable;
- heat exchanger without both hot-side and cold-side connections;
- support without both supported object and supporting structure;
- penetration without both sides;
- cable/conduit/tray segment with no upstream/downstream termination;
- pipe/duct run with an orphaned end;
- relief path without a documented final discharge destination;
- drain/vent/sample branch without a destination;
- factual dimension/material/tag without source or derivation;
- fastener/gasket/seal listed without its mating assembly relationship.

The goal is not merely syntactically valid CSV. The final database must be mechanically and functionally closed enough that a 1:1 digital plant model cannot contain a pipe, cable, support, valve, instrument or auxiliary system that simply terminates without explanation.
