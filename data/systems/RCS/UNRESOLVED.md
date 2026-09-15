# RCS unresolved-detail ledger

This file is intentionally long-lived. A gap disappears only when a cited public source resolves it or when it is formally classified as non-public/proprietary.

## System topology and plant-specific configuration

- Actual Westinghouse/Vogtle equipment tags for the reactor vessel, two SGs, four RCPs, pressurizer and main-loop piping.
- Exact plant coordinate/elevation/orientation data for each RCS major component.
- Exact hot-leg assignment of the pressurizer surge line in the current Revision-19/Vogtle baseline.
- Complete list and ownership of every RCS-to-auxiliary-system connection, including CVS, PXS, RNS, primary sampling, WLS, CCS and SGS boundaries.
- Complete RCS instrumentation list: sensing locations, process taps, thermowells, RTDs, pressure/level/temperature/flow channels, impulse tubing, junction boxes, cabling and signal destinations.

## Reactor vessel

- Full nozzle schedule and dimensions.
- Flange/stud/nut/washer schedule for vessel head closure.
- Vessel shell/head course geometry and individual welds.
- Materials/forgings/cladding by course/nozzle/flange.
- Internals interfaces, guide structures, hold-down structures and attachment hardware.
- CRDM housing details and each pressure-boundary weld/attachment.
- Head vent connection geometry, isolation valves and downstream path.
- Vessel supports, keys/restraints, insulation package, access hardware, lifting/handling features and local instrumentation.

## Steam generators — RCS/primary-side scope

- Complete channel-head geometry and primary nozzle schedule.
- Exact RCP suction/outlet nozzle geometry and weld details.
- Tube count, tube dimensions, tube pitch, tube-support geometry and tube-to-tubesheet joints.
- Tubesheet geometry/materials and cladding.
- Primary manways/covers, studs/nuts/gaskets and maintenance tooling interfaces.
- Internal primary-side dividers and attachment hardware.
- SG supports, lateral restraints, snubbers/restraints if any, insulation, platforms and maintenance-access interfaces.

## Reactor coolant pumps

Public NRC evidence currently resolves the overall canned-motor topology, impeller, shaft, induction motor, rotor/stator pressure cans, uranium-alloy flywheel and VFD function. Still unresolved:

- Complete pressure-casing and nozzle geometry/materials.
- Internal diffuser/flow passages.
- Exact impeller geometry/material.
- Shaft geometry/material and all shaft interfaces.
- Radial/thrust bearing count, type, materials, locations and lubrication/cooling mechanism.
- Rotor/stator lamination, winding, insulation and terminal details.
- Rotor/stator can thickness/material specification and joining method.
- Flywheel alloy specification, dimensions, attachment/keying/retention hardware and containment features.
- Internal cooling/thermal management paths.
- Electrical penetration/terminal construction, cables/connectors and local junction hardware.
- VFD cabinet internals and power/control connections.
- Every bolt/stud/nut/washer/pin/key/retaining ring/gasket/seal and its specification.
- Installation/removal tooling, lifting points and maintenance supports.

## Main-loop piping

Verified public basis currently establishes one 31-in-ID hot leg per loop and two 22-in-ID cold legs per loop. Still unresolved:

- Exact centerline coordinates and lengths.
- Wall thicknesses/schedules and exact material specification in current Revision-19/Vogtle basis.
- Every elbow/bend/reducer/tee/branch/nozzle fitting and its geometry.
- Every field/shop weld and weld identifier.
- Every branch connection, instrument tap, vent, drain and sample connection.
- Every hanger/support/anchor/guide/restraint and local structural attachment.
- Insulation thickness/material/jacketing and removable sections.
- NDE/ISI boundaries and inspection-access hardware.

## Pressurizer and connected RCS-owned hardware

- Vessel dimensions/course geometry/materials/cladding.
- Heater count, type, wattage, individual penetrations, power feeds and mounting details.
- Spray-nozzle geometry, spray-line sizes/materials/routes/valves and source connections.
- Surge-line size/material/route/fittings/welds/supports and exact hot-leg connection.
- Safety-valve inlet/discharge piping geometry and all rupture-disk/leak-detection details.
- Water-level/pressure/temperature instrumentation and exact taps.
- Vessel support/skirt/restraints, insulation, maintenance platforms and access.
- Manways/covers/gaskets/studs/nuts and internal hardware.

## Relief, ADS and vent interfaces

These interfaces cross ownership with PXS/ADS and reactor-vessel-head-vent functions. Do not duplicate ownership.

- Confirm Revision-19/Vogtle valve quantities/configuration for every ADS stage before creating final individual-valve objects.
- Resolve every series/parallel path, inlet branch, isolation element, discharge line, sparger, rupture disk and containment discharge point.
- Resolve PSARV module steel/support members and all valve/piping restraints from public structural sources.
- Resolve reactor vessel head vent isolation valves, piping, supports and IRWST/containment destination as applicable.

## Common hardware completeness

For every RCS assembly, eventually account for all publicly documentable:

- bolts, studs, nuts, washers, screws, pins, keys, dowels, clips and retainers;
- gaskets, O-rings, packing, seals and seal retainers;
- welds/brazes and pressure-boundary joints;
- brackets, baseplates, shims, grout, embeds, anchors and structural attachments;
- nameplates, tags, identification plates and local markings;
- insulation, jacketing and removable insulation covers;
- lifting lugs, eyebolts, handling fixtures and maintenance covers;
- electrical terminals, connectors, glands, conduit, cable trays and grounding/bonding hardware;
- tubing, fittings, manifolds and instrument/root valves.

If AP1000-specific public evidence cannot resolve one of these items, leave it unresolved. A generic commercial equivalent may later be used for the Roblox visualization only under the separate `REPRESENTATIVE` evidence state.
