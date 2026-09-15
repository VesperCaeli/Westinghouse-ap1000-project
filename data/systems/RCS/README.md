# Reactor Coolant System (RCS) — decomposition pilot

This is the first detailed system package used to test the project completeness model.

**Important:** IDs in this directory beginning with `RCS-` are project configuration IDs, not claimed Westinghouse equipment tags unless a source later provides the actual tag/mark.

## Verified public topology

NUREG-1793 Chapter 5 states that the AP1000 RCS consists of two heat-transfer circuits/loops. Each loop contains:

- one U-tube steam generator;
- two reactor coolant pumps;
- one hot-leg pipe;
- two cold-leg pipes.

The RCS additionally includes the reactor vessel, pressurizer, interconnecting piping, valves, fittings and instrumentation. All RCS equipment is located in reactor containment.

The NRC evaluation further identifies:

- four hermetically sealed canned-motor RCPs total, two integrated with each SG channel head;
- each RCP as a vertical single-stage centrifugal pump;
- an impeller attached to the electric-induction-motor rotor shaft;
- corrosion-resistant pressure-retaining cans around stator and rotor;
- no shaft seal because of the canned design;
- a uranium-alloy flywheel attached to the pump shaft for coastdown inertia;
- a variable-frequency drive used for the documented startup/heatup/cooldown function;
- one 31-inch (78.34 cm) inside-diameter hot leg in each main coolant loop;
- two 22-inch (55.88 cm) inside-diameter cold legs per loop, one per RCP;
- RCP suction nozzles welded directly to outlets on the bottom of each SG channel head, eliminating the crossover leg;
- a pressurizer connected by a surge line to one hot leg;
- pressurizer electrical heaters and water-spray pressure-control interfaces;
- spring-loaded pressurizer safety valves;
- automatic depressurization system interfaces;
- reactor-vessel-head vent isolation-valve interfaces;
- piping/fittings/valves leading to auxiliary and support systems.

Source: `SRC-0011`, NUREG-1793 Initial Report, Chapter 5, especially Sections 5.1–5.1.3.4 and later component sections. Revision-19 DCD/Vogtle sources must still be used to confirm configuration before an item is declared current-baseline complete.

## Ownership rule

The RCS package owns the reactor coolant pressure-boundary equipment and main-loop configuration assigned to RCS. Connected hardware owned by PXS/ADS, CVS, RNS, SGS, sampling, WLS, CCS, electrical, I&C, or other systems is represented here first as a boundary/interface and decomposed in its owning system package later.

This prevents duplicate equipment and lets validation prove that every interface has exactly one owner.

## Decomposition order

1. Freeze top-level equipment and loop topology from primary public sources.
2. Resolve every equipment nozzle/port.
3. Resolve main-loop pipe geometry, fittings, welds and supports.
4. Decompose reactor vessel and head interfaces.
5. Decompose SG primary-side pressure boundary and channel-head interfaces.
6. Decompose each RCP into pressure boundary, hydraulic assembly, rotor/shaft/impeller/flywheel, motor/stator/rotor cans, bearings and electrical/VFD interfaces to the level supported publicly.
7. Decompose pressurizer vessel, heaters, spray, surge line, relief interfaces, insulation/supports and instrumentation.
8. Close all auxiliary-system boundaries.
9. Add all publicly documented local instruments, impulse lines, electrical feeds, signal paths, junctions, supports, drains, vents and maintenance interfaces.
10. Audit the source set for missing parts and record non-public gaps in the unresolved register.

## Current status

`FOUNDATION / NOT COMPLETE`.

The major topology is source-backed. Detailed nozzles, fittings, weld counts, supports, instrument taps, local hardware, manufacturing BOM and plant-specific routing remain to be extracted and verified.
