# RCS unresolved-detail ledger

This file is intentionally long-lived. A gap disappears only when a cited public source resolves it or when it is formally classified as non-public/proprietary.

## System topology and plant-specific configuration

- Actual Vogtle tags for the reactor vessel, two steam generators, four RCPs, pressurizer, pressurizer safety valves and main-loop piping remain to be resolved. ADS/head-vent tags are now seeded separately from public Unit 3 ITAAC evidence.
- Exact plant coordinate/elevation/orientation data for each RCS major component.
- Confirm final current Vogtle Unit 3 pressurizer surge-line hot-leg assignment from plant P&ID/isometric. Public AP1000 test/design material indicates connection to Hot Leg 2, but this is not yet promoted to the plant overlay.
- Complete list and ownership of every RCS-to-auxiliary-system connection, including CVS, PXS, RNS, primary sampling, WLS, CCS and SGS boundaries.
- Complete RCS instrumentation list: sensing locations, process taps, thermowells, RTDs, pressure/level/temperature/flow channels, impulse tubing, junction boxes, cabling and signal destinations.
- Retrieve or otherwise publicly resolve the cited Vogtle RCS P&IDs/isometrics/work packages cataloged in `public_document_map.csv` before extracting unverified line geometry from document titles alone.

## Reactor vessel

Now resolved at major Revision-19 pressure-boundary level: upper/lower shell forgings, transition ring, lower head, one-piece closure head/flange, 4 × 22-in inlets, 2 × 31-in outlets, 2 × 6.81-in DVI nozzles, 45 × 7-in closure studs, dual metal O-rings, 69 CRDM penetrations, 8 Quickloc instrumentation penetrations, major vessel envelope dimensions, and the four support-box/leg arrangement.

Still unresolved:

- Exact safe-end dimensions/material mapping for each individual inlet/outlet/DVI nozzle and every associated dissimilar/similar-metal weld.
- Full shell/head course axial dimensions and individual weld identifiers.
- Closure-stud length/thread geometry, individual nut/washer quantities/materials and preload/torque requirements.
- Detailed CRDM head-adapter/housing assemblies and every pressure-boundary weld/attachment; decomposed under reactor/IHP work package.
- Detailed Quickloc plug/nozzle/thimble part BOM, seals, retainers and fasteners.
- Reactor vessel head-vent pressure-boundary nozzle/fitting geometry and mapping of Unit 3 tags `RCS-PL-V150A` through `V150D` to exact line segments.
- Support-pad/base-pad/side-stop dimensions, sliding-surface material/finish, support-box plates/welds/anchors/embedments and shield-wall reinforcement interfaces.
- Vessel reflective-insulation panel BOM, attachments, flow paths for external vessel cooling, access hardware and removal sequence.
- Closure-head lifting lug count/geometry/material/weld details.
- Complete vessel instrumentation taps and local hardware.

## Steam generators — RCS/primary-side scope

Resolved at current public level: primary channel head, tubesheet, Alloy 690 TT U-tube bundle concept, broached support plates, antivibration bars, primary manways and identified inspection/access openings.

Still unresolved:

- Exact tube count, tube OD/wall thickness, bend radii and complete tube-layout map.
- Tubesheet geometry/materials/cladding and individual tube-to-tubesheet joint construction.
- Complete channel-head geometry/divider plate and primary nozzle schedule.
- Exact RCP suction/outlet nozzle geometry and all SG-to-RCP pressure-boundary weld details.
- Primary manway covers, hinges/handling features, studs/nuts/washers/gaskets and seal details.
- SG supports, lateral restraints, insulation, platforms and maintenance-access interfaces.

## Reactor coolant pumps

Now resolved beyond the initial generic pump description:

- single-stage canned-motor architecture;
- pump casing, thermal barrier, stator shell/cap, impeller and common shaft;
- metallic rotor/stator cans;
- water-lubricated bearing architecture;
- final Revision-19 externally mounted conventional shell-and-tube motor-cavity heat exchanger and Class 1 internal-circulation supply/return piping;
- stator cooling jacket / CCS heat-sink interface;
- upper/lower thrust-bearing arrangement integrated around lower flywheel;
- final upper/lower bimetallic flywheel construction using heavy-alloy segments, Type 403 stainless hubs, 18Ni maraging-steel retaining cylinders and Alloy 690 sealing components;
- obsolete preliminary depleted-uranium/wraparound-HX concepts explicitly rejected from the Revision-19 model.

Still unresolved:

- Complete pump casing/nozzle/diffuser/flow-passage geometry and material/weld map.
- Exact impeller geometry/material.
- Shaft geometry/material and detailed couplings/interfaces.
- Water-lubricated radial-bearing count, locations, pad geometry/material and exact internal coolant paths.
- Thrust-bearing shoe/pad count, geometry/material and adjustment/retention hardware.
- Motor rotor/stator lamination, winding, insulation, terminal and internal electrical details.
- Metallic can thickness/material specification and joining method.
- Heavy-alloy flywheel exact alloy, segment count/dimensions, endplate count/dimensions, interference-fit values and weld map.
- External RCP heat-exchanger primary/secondary nozzle sizes, internals, materials, supports, relief protection, valves and instrumentation.
- CCS branch tags/sizes/routes/isolation/relief instrumentation.
- Electrical penetrations/terminals, VFD cabinet internals, cables/connectors and local junction hardware.
- Every RCP bolt/stud/nut/washer/pin/key/retaining ring/gasket/seal and installation/removal fixture.

## Pressurizer

Now resolved at major Revision-19 level:

- vertical cylindrical vessel with hemispherical top/bottom heads;
- design pressure 2485 psig, design temperature 680 F, internal volume 2100 ft3;
- 18-in surge nozzle, 4-in spray nozzle and 14-in safety-valve-nozzle design basis;
- one top spray nozzle and two top safety/depressurization header connections;
- bottom surge connection and removable electrical heaters;
- 480 Vac / 60 Hz heater grouping: 370-kW control group; 245-kW backup A/B; 370-kW backup C/D;
- 18-in SA-312 TP316LN surge-line design basis and public spool-document references;
- pressurizer safety valve internal component BOM from Baker Hughes 3707S public manual.

Still unresolved:

- Certified Revision-19 shell inside diameter/overall vessel height: older public summaries provide values, but they remain intentionally unpromoted until directly reconciled with the certified R19 table/figure.
- Shell/head course dimensions, materials/cladding and circumferential/longitudinal weld map.
- Individual immersion-heater count, element wattage, heater wells/penetrations, seals/flanges/connectors and exact power-feed grouping.
- Spray-line source branches, scoop geometry, valves, control logic, common line geometry and CVS auxiliary-spray hardware.
- Surge-line exact as-built route, bend geometry, spool/weld map and supports from `APP-RCS-PLW-041/-042/-043` and associated support drawings.
- Safety/ADS header nozzle assignment and detailed header branch topology.
- Vessel support/skirt/pads/restraints, insulation panels, manway/access and lifting hardware.
- Complete pressure/level/temperature tap, transmitter and cable-channel inventory.
- Detailed internal baffle/diffuser/screen geometry; do not import non-US design details without R19 verification.

## Pressurizer safety valves and discharge trains

Now resolved:

- two AP1000 3707S spring-loaded safety valves;
- per-valve inlet/discharge path, terminal rupture disk, RCDT leakage-drain boundary, position indication and discharge-temperature monitoring;
- public vendor nomenclature/BOM down to base, nozzle, bonnet, spindle, disc/collar/holder/guide, upper/lower adjusting rings and pins, spring and washers, compression screw/locknut, plunger, cap, studs/nuts, limit-switch assembly, bracket kit, drain plug, lift stop, cotter pins, inlet/outlet studs and nuts, gag hardware, nameplates/tag plates, seal wire/seal, screws and inlet/outlet gaskets;
- exact vendor-listed quantities are captured in `psv_3707s_component_bom.csv`.

Still unresolved:

- Exact valve GA dimensions and AP1000 as-built material callouts for every listed part.
- Thread sizes/pitches, bolting preload/torque, gasket specification and seal details.
- Exact inlet/discharge line sizes/materials/routes/supports and rupture-disk holder/flange/bolting.
- Drain branch size/slope/root valves/supports and exact RCDT endpoint.
- Limit-switch internal part BOM, wiring, junction-box/channel routing and calibration details.
- PSARV/ADS support-module steel and restraint details where the safety-valve/discharge hardware interfaces with support structures.

## ADS and reactor-vessel-head vent plant overlay

Public Vogtle Unit 3 ITAAC now resolves these tags at the equipment-name/function level:

- ADS Stage 1: `RCS-PL-V001A/B`; isolation `RCS-PL-V011A/B`.
- ADS Stage 2: `RCS-PL-V002A/B`; isolation `RCS-PL-V012A/B`.
- ADS Stage 3: `RCS-PL-V003A/B`; isolation `RCS-PL-V013A/B`.
- ADS Stage 4 squib valves: `RCS-PL-V004A/B/C/D`; associated MOVs `RCS-PL-V014A/B`.
- Reactor vessel head vent: `RCS-PL-V150A/B/C/D`.

Still unresolved:

- Exact line-by-line topology, pair groupings, sizes, manufacturers/models, pressure classes and actuator details from plant P&IDs/equipment records.
- Exact valve-to-isometric mapping and supports/restraints.
- ADS sparger/discharge geometry and IRWST interfaces; detailed ADS ownership belongs primarily to WP-04.
- Head-vent destination, fittings and precise A/B/C/D series/parallel arrangement from Unit 3 P&IDs/isometrics.

## Main-loop piping

Verified public basis currently establishes one 31-in-ID hot leg per loop and two 22-in-ID cold legs per loop. Still unresolved:

- Exact centerline coordinates and lengths.
- Wall thicknesses/schedules and final as-built material heat/lot data.
- Every elbow/bend/reducer/tee/branch/nozzle fitting and its geometry.
- Every field/shop weld and weld identifier.
- Every branch connection, instrument tap, vent, drain and sample connection.
- Every hanger/support/anchor/guide/restraint and local structural attachment.
- Insulation thickness/material/jacketing and removable sections.
- NDE/ISI boundaries and inspection-access hardware.

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
