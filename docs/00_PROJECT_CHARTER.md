# Project Charter and Completeness Standard

## Objective

Create a source-traceable, 1:1-scale digital reconstruction of the Westinghouse AP1000 plant suitable for later conversion into a Roblox implementation.

The reconstruction target is not merely major equipment. The data model is intended to descend, where public information permits, through equipment internals, fittings, supports, actuators, instruments, junctions, ports, removable covers, seals, bearings, fasteners, and other individual parts.

## Controlling principle

**Completeness is demonstrated, not assumed.**

An object is not considered complete merely because its major equipment is present. The project must be able to answer:

- What is it?
- Where is it?
- What contains/supports it?
- What is it connected to?
- What ports/interfaces does it have?
- What passes through those interfaces?
- What material/specification/classification is publicly documented?
- How is it actuated, powered, sensed, drained, vented, isolated, supported, maintained, or removed?
- Which public source proves each factual claim?
- What remains unresolved?

## Plant object hierarchy

1. Plant / unit
2. Site interface
3. Building / civil structure
4. Elevation / room / zone
5. System
6. Subsystem / division / train / loop
7. Equipment item
8. Assembly
9. Component
10. Part
11. Fastener / consumable / local hardware

Objects may have multiple functional relationships, but must have exactly one configuration parent.

## Mandatory object fields

Every registered object must eventually carry, as applicable:

- `object_id`
- `tag_or_mark`
- `name`
- `object_type`
- `parent_id`
- `system_code`
- `plant_variant`
- `building`
- `room_or_zone`
- `elevation`
- `quantity`
- `manufacturer`
- `model_or_drawing_number`
- `material`
- `pressure_class`
- `safety_class`
- `seismic_category`
- `electrical_class`
- `nominal_dimensions`
- `mass`
- `orientation`
- `mounting_or_support`
- `maintenance_access`
- `evidence_state`
- `source_ids`
- `source_locator`
- `notes`

Unknown values remain blank/`UNRESOLVED`; they are never guessed and silently promoted to fact.

## Interface model

Every physical or logical interface is represented explicitly as a port plus a connection.

Port classes include at least:

- process inlet/outlet
- vent
- drain
- relief/discharge
- sample
- chemical addition
- instrument impulse
- pneumatic/hydraulic actuator
- electrical power
- control signal
- data/network
- grounding/bonding
- mechanical drive/shaft
- structural support
- HVAC supply/return/exhaust
- fire protection
- lifting/handling
- maintenance access
- penetration/seal

A pipe, duct, cable, bus, signal path, shaft, linkage, support, or hose is not complete until both ends are resolved to ports or to a formally declared site/external boundary.

## Zero-orphan rules

The validator will ultimately reject:

- objects whose `parent_id` does not resolve;
- connections with a missing endpoint;
- equipment with referenced ports that do not exist;
- pipes/ducts/cables with unexplained dead ends;
- valves without upstream/downstream interfaces;
- instruments without process/electrical/signal interfaces where applicable;
- motors without mechanical load and power interfaces;
- pumps without suction/discharge interfaces;
- supports without supported and supporting objects;
- penetrations without both sides identified;
- source references that do not resolve to the source register;
- factual fields with no source or declared derivation.

## Evidence hierarchy

Priority order:

1. NRC-certified AP1000 DCD / incorporated licensing basis.
2. Current plant-specific Vogtle UFSAR/COL amendments and public licensing basis.
3. NRC ITAAC closure documentation and inspection reports containing as-built or procurement evidence.
4. NRC safety evaluation reports and technical specifications.
5. Public Westinghouse technical/topical reports and manuals.
6. ASME/IEEE/NFPA/ANSI/ASTM or other cited industry codes, where publicly available and applicable.
7. Peer-reviewed papers, theses, conference papers, and credible engineering publications.
8. Secondary references only as discovery aids; they do not override primary sources.

## Variant control

Do not merge different configurations into one fictitious plant.

At minimum the data model distinguishes:

- `AP1000-DCD-R19-GENERIC`
- `VOGTLE-3-CURRENT-PUBLIC`
- `VOGTLE-4-CURRENT-PUBLIC`
- `AP1000-DCD-R20-PENDING`
- other AP1000 sites/configurations when specifically researched

Where plant-specific departures exist, the generic item remains preserved and the departure is stored as a variant/override.

## Public-information boundary

This project uses lawfully public engineering and licensing information only. It does not reconstruct withheld safeguards information, security plans, physical-protection details, cybersecurity implementation, access-control weaknesses, or non-public proprietary fabrication data.

A withheld/proprietary reference may be recorded by title/document number when it appears in a public source, but its inaccessible contents are not inferred.

## Definition of done for an assembly

An assembly reaches `PUBLIC_BASELINE_COMPLETE` only when:

1. all public-source-visible subassemblies/components are registered;
2. all visible ports/interfaces are registered;
3. all connections terminate;
4. all sourceable dimensions/materials/classifications are captured;
5. maintenance/access/support interfaces are represented where documented;
6. unresolved details are itemized rather than hidden;
7. at least one completeness audit has been run against the source set for that assembly.

This status means complete **to the available public design basis**, not that proprietary manufacturing data has somehow been recovered.
