# AP1000 Plant-Object Completeness Standard

## Purpose

The reconstruction target is the complete public-design-basis generating station, not a collection of major systems and not merely complete piping. Every physical and functional plant object is decomposed until public evidence is exhausted. Nothing is silently omitted because it is small, auxiliary, embedded, normally inactive, maintenance-only, or outside the nuclear steam supply system.

This standard applies to every work package and every plant variant.

## Fundamental rule

An object is not complete merely because its name, outer envelope, or two process connections are known. Before an object may be dispositioned `PUBLIC_BASELINE_COMPLETE`, the project must search for, enumerate, connect, source, or explicitly disposition all applicable subassemblies, auxiliaries, interfaces, construction hardware, maintenance provisions, and dependencies listed below.

Absence is never inferred from ordinary industry practice. Generic practice defines what must be searched for; AP1000-specific factual objects require controlled public evidence. Unresolved public detail remains `UNRESOLVED`; known nonpublic/proprietary detail remains `WITHHELD_OR_PROPRIETARY`.

## Universal decomposition hierarchy

The default physical hierarchy is:

`plant -> site/building -> room/zone/elevation -> system -> subsystem/train -> equipment -> assembly -> component -> part -> fastener/joint`

The lowest modeled level is whichever level public evidence supports. If a drawing exposes individual bolts, clips, welds, connectors, cartridges, plates, bearings, seals, or terminals, those items enter the database rather than being hidden inside a parent object.

## Loop / area scope rule

For this project, a named **loop**, **train**, **system area**, or similar reconstruction scope means the complete physical plant volume and all infrastructure required to build, operate, monitor, protect, access, inspect, maintain and remove the equipment in that scope. It does **not** mean only the process-fluid path.

Accordingly, loop/area closure must include or explicitly disposition, as applicable:

- exact room/zone/elevation boundaries and floor-plan geometry;
- adjacent rooms, corridors, doors, hatches, stairs, ladders, platforms and egress paths;
- equipment footprints, orientation, elevations, laydown zones and maintenance/removal clearances;
- all process piping/ducting, fittings, valves, supports, restraints, insulation, penetrations and weld/joint populations;
- HVAC/ventilation supply, return and exhaust paths, local unit coolers, coils, dampers, filters, drains and environmental controls;
- electrical power distribution, starters/breakers/disconnects, panels/MCCs, cable, conduit, tray, junction boxes, grounding and room-service electrical loads;
- instrumentation, probes, process taps, sample points, analyzers, radiation monitoring, local indicators, cabinets and control/signal paths;
- fire detection, suppression, barriers, penetration seals and combustible-control interfaces;
- floor/equipment/condensate drains, sumps, leak collection, vents, fills, flushes, test connections and waste destinations;
- permanent maintenance hardware including hatches, padeyes, monorails, hoists, cranes, removable panels, special fixtures/tooling and rigging routes;
- civil/structural boundaries, wall/floor/ceiling modules, embeds, foundations and load paths;
- all system-specific internals and functional hardware within the area, including reactor-vessel internals, fuel/core objects, control rods/drive mechanisms, vessel-head assemblies and in-core/ex-core monitoring where the scope is the primary reactor loop/area.

A loop/area completeness percentage must therefore be based on this full scope. Process-topology, licensing-evidence, piping-geometry, electrical, HVAC, spatial/architectural, maintenance, I&C, civil/structural and equipment-internal progress may be reported separately, but none of those partial metrics may be presented as the completion percentage of the full loop.

## Mandatory completeness domains

Every equipment object must be audited against all applicable domains.

### 1. Primary function and internal working parts

- pressure boundary or enclosure
- shells, heads, covers, doors, hatches and access panels
- internal chambers, plenums, baffles, partitions, diffusers and distributors
- rotors, impellers, shafts, gears, bearings, couplings and flywheels
- tubes, plates, bundles, coils, elements, cores, windings and buswork
- filters, strainers, cartridges, media, screens and separators
- heaters, coolers, trace heat and anti-condensation heaters
- internal liners, cladding, coatings and wear surfaces
- internal restraints, guides, spacers and supports

### 2. Process and utility interfaces

- every inlet and outlet
- every branch, cross-connect and tie-in
- isolation, check, control, bypass, balancing and relief hardware
- vents, drains, fills, samples, flushes, purges and test connections
- seal water, cooling water, heating water/steam, lube oil, instrument air, service air, nitrogen or other gas interfaces
- chemical-addition, regeneration, backwash and waste interfaces
- ultimate upstream source and downstream destination

The detailed requirements of `docs/05_FLOWPATH_COMPLETENESS_STANDARD.md` apply to every process or utility path.

### 3. Instrumentation and control

- sensing points and process taps
- local gauges and indicators
- transmitters, switches and analyzers
- thermowells, RTDs, thermocouples and level elements
- flow/pressure/level/temperature elements and manifolds
- valve position indication and limit switches
- actuator solenoids, relays, contactors and local controls
- local control panels, cabinets and junction boxes
- control/signal/data cabling and termination points
- trip, interlock, permissive and alarm interfaces where public
- calibration/test connections and instrument isolation/root valves

### 4. Electrical power

- normal and alternate power feeds
- voltage, phase, frequency and load where public
- breakers, fuses, disconnects and isolation devices
- motor starters, VFDs, soft starters and contactors
- MCC/switchgear/panel source
- transformers and control-power transformers
- cables, connectors, glands, conduit, tray and penetrations
- grounding and bonding
- protective relays and monitoring
- space/anti-condensation heaters and panel cooling where applicable
- batteries, chargers, UPS or DC interfaces where applicable

### 5. Mechanical support and structural load path

- baseplates, skirts, saddles, columns, lugs and brackets
- embeds, anchors, anchor bolts, grout and shims
- pipe/duct/cable supports, hangers, guides, restraints and snubbers
- seismic restraints and impact/missile protection
- support steel and supporting building structure
- thermal-expansion provisions and sliding/guided interfaces
- vibration isolation where applicable
- exact supported/supporting-object relationship

### 6. Joints, seals and fastening hardware

Where public evidence permits, model:

- welds and weld categories
- brazed/soldered joints
- flanges and flange classes
- studs, bolts, nuts, washers and screws
- pins, dowels, keys, clips, retainers and locking devices
- gaskets, O-rings, packing, mechanical seals and canned boundaries
- threaded fittings, couplings and unions
- retaining rings, snap rings and lockwire
- torque/tensioning requirements and locking method where public

A fastener or seal is linked to the mating parts it joins; free-floating BOM entries are not accepted.

### 7. Thermal protection and environmental conditioning

- insulation type, thickness and jacketing where public
- removable insulation blankets/covers
- heat tracing
- freeze protection
- equipment-room cooling/heating dependencies
- ventilation supply/return/exhaust connections
- local fans, blowers and duct interfaces
- environmental/seismic qualification boundaries
- drainage/flood protection
- fire barriers and fire-protection interfaces

### 8. Maintenance, inspection and handling

- manways, handholes and removable covers
- inspection ports and NDE/ISI access
- maintenance clearances and removal paths
- lifting lugs, padeyes, eyebolts and certified lift points
- monorails, cranes, hoists, trolleys and rails
- jacking points and temporary-support interfaces
- local disconnects and quick-disconnects
- special permanent fixtures/tooling
- laydown/staging provisions where part of permanent plant design
- drain/vent/depressurization provisions required before maintenance

### 9. Identification and configuration hardware

- equipment tags and nameplates
- valve/line labels where public
- flow arrows and identification plates
- calibration plates and setpoint labels
- locking/administrative-position devices
- local operating placards where public

### 10. Materials, classifications and fabrication evidence

For every part where public:

- material specification/grade/heat number
- cladding/coating/liner material
- pressure class/design pressure/design temperature
- ASME class / safety class
- seismic category
- electrical class / environmental qualification
- dimensions, tolerances and mass
- fabrication drawing/specification
- CMTR/data report identifiers
- weld map, NDE and inspection records
- hydro/pneumatic/leak test requirements
- installation/as-built/ITAAC evidence

## Equipment-class-specific search requirements

### Tanks and pressure vessels

Search for shell/head courses, nozzles, manways, internals, supports, insulation, heaters, mixers, vents, drains, reliefs, level/pressure/temperature instrumentation, fill/sample/chemical interfaces, ladders/platforms, lifting lugs, anchor hardware, coatings/cladding, weld maps and NDE.

### Heaters

Search for heater elements/banks, sheaths, penetrations, terminal boxes, power feeds, breakers/contactors, control logic, temperature sensors, overtemperature protection, mounting hardware, removable elements, local disconnects and associated cooling/flow permissives.

### Pumps

Search for casing, cover, impeller, shaft, bearings, wear rings, diffuser/volute, seal/canned-motor boundary, motor, coupling, flywheel if any, cooling/lube systems, suction/discharge nozzles, checks/isolation/minimum-flow, vents/drains, instrumentation, baseplate, anchors, electrical supply/control and lifting/maintenance provisions.

### Motors and generators

Search for stator, rotor, shaft, bearings, cooling/ventilation, space heaters, terminal boxes, excitation where applicable, lubrication, grounding, instrumentation, protection, coupling, enclosure, foundation and power/control connections.

### Heat exchangers

Search both fluid sides plus shell/channel heads/tubes/tubesheets/plates, baffles/supports, inlet/outlet isolation, bypass, vents, drains, reliefs, instrumentation, bolting/gaskets, fouling/cleaning access, supports, insulation and the complete upstream/downstream heat-rejection chain.

### Valves and actuators

Use the valve completeness rule in `docs/05_FLOWPATH_COMPLETENESS_STANDARD.md`, including body/bonnet/trim/stem/disc/seat, actuator, gearbox, handwheel/manual override, position switches, power/air interfaces, packing/gaskets, supports and attached bypass/equalizing/drain/vent hardware where public.

### Filters, strainers and treatment equipment

Search housings, baskets/cartridges/media, covers, bolting/gaskets, differential-pressure instrumentation, isolation/bypass, drains/vents, backwash/regeneration paths, chemical supplies, waste destinations, lifting/removal hardware and support frames.

### HVAC equipment

Search fan/blower internals, motors, dampers, filters, heating/cooling coils, humidification/dehumidification if used, drains, instrumentation, fire/smoke dampers, duct transitions, silencers, flexible connectors, supports, power/control and room/zone boundaries.

### Electrical equipment

Search internal buses, breakers/contactors, CTs/PTs, relays, meters, control power, heaters, ventilation/cooling, enclosures, doors/interlocks, cable terminations, grounding, structural supports, fire protection and incoming/outgoing circuits.

### Transformers

Search core/windings, tank, insulating medium, bushings, tap changer, radiators/coolers, pumps/fans, conservator or equivalent oil-management hardware if used, pressure/temperature/level protection, sudden-pressure/Buchholz-type protection if applicable, fire protection, oil containment/drainage, grounding, surge arresters, neutral equipment, controls and foundations. Only AP1000/site-specific hardware supported by sources is instantiated.

### Diesel generators and engines

Search engine block/heads, crankshaft/pistons/valvetrain, turbocharging/aftercooling, fuel injection, starting system, day/bulk fuel tanks and transfer, filters/strainers, lube oil, jacket-water and auxiliary cooling loops, radiator/heat rejection, combustion air, exhaust/silencer, alternator/excitation, batteries/air start as applicable, control/protection, ventilation, drainage, fire protection, foundations and electrical output path.

### Water-treatment systems

Search raw-water pretreatment, strainers/filters, demineralizers/RO/ion exchange where applicable, chemical storage/feed, pumps, tanks, heaters/coolers, sample/analyzer panels, regeneration/backwash/rinse paths, neutralization/waste systems, drains, vents, instrumentation and distribution headers.

### Civil/structural objects

Search concrete/steel members, liners, embeds, anchors, penetrations, sleeves, seals, doors/hatches, curbs, sumps, coatings, drains, platforms, stairs/ladders, handrails, equipment foundations and interfaces to supported equipment.

## Completion-state rule

The database may use research and partial states while work proceeds, but a work package is not `PUBLIC_BASELINE_COMPLETE` until:

1. every applicable completeness domain above has been audited;
2. every publicly documented child object has a stable ID and parent;
3. every interface is connected or explicitly dispositioned;
4. every support has a supported and supporting object;
5. every electrical/control interface has an owning downstream package or named boundary;
6. maintenance/handling hardware is accounted for where public;
7. construction hardware and joints are represented to the public-evidence limit;
8. source citations and locators exist for factual fields;
9. unresolved and proprietary gaps are explicitly recorded;
10. no major fact remains solely in prose if it can be represented structurally in the database.

## Whole-plant closure

The final reconstruction is complete only when all work packages compile into a single connected plant graph with named external boundaries. A subsystem may not be considered complete merely because it stops at another system name. The downstream system, electrical source, utility source, heat sink, waste destination, building support, or site interface must itself be modeled and connected.
