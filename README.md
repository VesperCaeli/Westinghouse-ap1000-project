# Westinghouse AP1000 1:1 Reconstruction Project

Configuration-controlled reconstruction of a Westinghouse AP1000 nuclear power plant for eventual 1:1-scale simulation in Roblox.

## Project standard

This repository is not a loose reference model. Every modeled object must be traceable through a plant breakdown structure and to public evidence.

The intended hierarchy is:

`plant -> building/structure -> elevation/zone -> system -> subsystem/train -> equipment -> assembly -> component -> part -> fastener`

Every fluid, electrical, mechanical, structural, instrumentation, ventilation, drain, vent, support, access, maintenance, and control interface must terminate at another defined object or an explicitly defined external/site boundary. Dangling pipes, ducts, cables, signal paths, shafts, supports, and unexplained penetrations are validation failures.

## Design basis

Primary baseline:

1. NRC-certified AP1000 Design Control Document (DCD), Revision 19.
2. Current public Vogtle Unit 3 licensing basis/UFSAR and public as-built/inspection evidence where it legitimately refines the generic AP1000 design.
3. NRC safety evaluations, ITAAC, technical specifications, inspection reports, and public Westinghouse technical/topical reports.

Westinghouse submitted AP1000 DCD Revision 20 to the NRC in March 2026. It is tracked as a separate pending design basis and must not be silently mixed into the Revision 19/Vogtle baseline.

## Evidence rule

No value may be presented as an AP1000 fact without a source. If a dimension, material, part number, quantity, route, fastener, internal assembly, or interface cannot be supported from public information, mark it `UNRESOLVED`; do not invent it.

Permitted evidence states:

- `VERIFIED_PUBLIC` - explicitly supported by a public primary source.
- `CORROBORATED_PUBLIC` - supported by multiple public sources.
- `DERIVED` - calculated directly from sourced values; derivation must be recorded.
- `REPRESENTATIVE` - non-AP1000 detail used only for Roblox visualization and clearly segregated from factual AP1000 data.
- `UNRESOLVED` - required detail is known to exist but is not yet publicly resolved.
- `WITHHELD_OR_PROPRIETARY` - public licensing record identifies the information as non-public/proprietary.

## Scope boundary

Use only lawfully public information. Do not ingest or reconstruct safeguards information, security plans, physical-protection layouts, cybersecurity details, access-control vulnerabilities, or non-public proprietary vendor data. Public NRC records themselves identify portions of plant/security documentation that are withheld; those remain out of scope.

## Repository layout

- `docs/` - project rules, source register, plant breakdown structure, research notes.
- `data/master/` - authoritative component, port, connection, source, and unresolved-item registers.
- `schemas/` - machine-readable schemas used to prevent missing fields and orphan objects.
- `scripts/` - validation, import, cross-reference, and reporting tools.
- `sources/` - metadata/manifests for source documents; do not commit copyrighted/non-redistributable documents unless redistribution is permitted.

The source register is the controlling index for research.
