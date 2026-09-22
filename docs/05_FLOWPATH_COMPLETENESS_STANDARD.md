# AP1000 Flowpath and Auxiliary Hardware Completeness Standard

## Purpose

A plant flow path is not complete merely because its source and destination are known. Before a process, utility, ventilation, electrical, instrumentation, drain, vent, sampling, relief, or maintenance path may be declared `PUBLIC_BASELINE_COMPLETE`, the project must explicitly search for, enumerate, connect, source, or disposition all intermediate and auxiliary hardware supported by the public AP1000 record.

This applies plant-wide: RCS, PXS/ADS/PRHR, CVS, RNS, CCS, SWS, turbine island, water treatment, HVAC, fire protection, diesel fuel and cooling, transformers, electrical distribution, radwaste, compressed air/gases, drains, sumps, sampling, and all later work packages.

## Mandatory flowpath search classes

Every line/run/header/duct/cable/raceway/service path must be checked for the following classes. The absence of a class is not assumed; it is either supported by evidence or remains unresolved.

### Isolation and alignment

- manual isolation valves
- motor-operated valves (MOV)
- air-operated valves (AOV)
- solenoid-operated valves
- squib/pyrotechnic valves
- check/nonreturn valves
- double-isolation arrangements
- lock-open / lock-closed valves
- normally open / normally closed alignment valves
- maintenance isolation valves
- test isolation valves
- containment isolation valves where applicable
- spectacle blinds, blind flanges, caps, plugs, removable spool pieces, or other positive isolation where documented

### Bypass and alternate paths

- equipment bypasses
- valve bypasses
- heat-exchanger bypasses
- filter/strainer bypasses
- pump minimum-flow / recirculation paths
- warmup lines
- startup/shutdown bypasses
- alternate train cross-connects
- emergency/backup cross-connects
- maintenance temporary-connection points where part of the permanent design

### Balancing, restriction, and hydraulic control

The project uses `balancing` as an umbrella search category; the actual hardware name must follow the source.

- balancing valves
- throttling valves
- calibrated/tuning orifices
- restriction orifices
- flow limiters/restrictors
- pressure-equalization/balance lines
- differential-pressure control elements
- flow-control valves
- pressure-reducing/regulating valves
- backpressure regulators
- minimum-flow devices
- fixed resistances/nozzles used to establish branch flow balance

### Protection and pressure control

- safety valves
- relief valves
- vacuum relief / vacuum breaker valves
- rupture disks
- thermal relief valves
- pressure-control valves
- surge suppression devices
- water-hammer mitigation hardware
- accumulators/dampeners where documented

### Vent, drain, fill, sample, chemistry, and test

- high-point vents
- low-point drains
- equipment drains
- leak-off drains
- fill/makeup lines
- flush lines
- purge connections
- sampling connections
- chemical-addition connections
- decontamination connections
- hydrotest/test connections
- temporary hose/quick-connect stations that are permanent plant hardware
- root valves on instrument/sample connections

Every such branch must have a named destination or explicit open-boundary disposition. `drain`, `vent`, `sample`, or `offsite` by itself is not a destination.

### Filtration, separation, conditioning, and treatment

- strainers
- filters
- demineralizers/ion exchangers
- separators
- coalescers
- dryers
- moisture separators
- chemical-treatment equipment
- heaters/coolers
- heat exchangers
- mixers/static mixers
- diffusers/spargers

Each device must carry inlet/outlet interfaces and any required bypass, drain, vent, differential-pressure instrumentation, regeneration/backwash, chemical, or waste interfaces supported by public evidence.

### Instrumentation and actuation attached to the path

- pressure taps/transmitters/switches
- temperature elements/thermowells
- flow elements/transmitters
- level instruments
- valve position switches/transmitters
- differential-pressure instruments
- local gauges/indicators
- instrument root valves/manifolds
- impulse tubing
- pneumatic supply/exhaust
- hydraulic supply/return
- actuator motors/gearboxes
- solenoids
- limit switches
- power feeds
- control/signal/data interfaces
- junction boxes/connectors/cable/conduit/raceway boundaries

### Mechanical construction

- pipe/duct/cable segments
- elbows/bends
- tees/wyes/laterals
- reducers/expanders
- couplings/unions/flanges
- nozzles/safe ends
- branch connections
- expansion joints/bellows where used
- flexible connectors/hoses where permanent
- welds/brazed joints/mechanical joints
- gaskets/O-rings/packing/seals
- supports/hangers/anchors/guides/restraints/snubber interfaces
- insulation and jacketing
- removable insulation sections
- penetrations/seals
- equipment nozzles and mating interfaces

### Maintenance and handling

- removable covers/manways/handholes
- lifting lugs/eyebolts
- monorails/hoists/rails
- maintenance platforms/access clearances
- drain/vent provisions required for maintenance
- disconnects and quick-connects
- local electrical isolation/disconnects where public
- special tooling permanently stored/installed as part of the plant configuration

## Closure rule for each process path

A canonical path may be marked complete only when all of the following are true:

1. source and destination are named;
2. every known intermediate pipe/duct/run segment is represented;
3. every publicly documented isolation/check/control/relief/bypass/balancing device is represented;
4. vents, drains, samples, fills, purge and test branches have destinations;
5. supports and penetrations are assigned or explicitly deferred to their owning package;
6. instrumentation/process taps are assigned or explicitly deferred to I&C;
7. actuator power/control/pneumatic interfaces are assigned or explicitly deferred;
8. materials, pressure/safety/seismic/electrical classifications and dimensions are populated where public;
9. each factual field cites a controlled source and locator;
10. anything not resolved is explicitly `UNRESOLVED` or `WITHHELD_OR_PROPRIETARY` rather than silently omitted.

## Valve completeness rule

A valve object is not complete at the word `valve`. Where public evidence permits, resolve:

- actual plant/vendor tag
- service/function
- valve type and body pattern
- nominal size / pressure class
- body/bonnet/trim/stem/disc/seat materials
- end connection and mating weld/flange identifiers
- normal and fail position
- actuator type
- actuator motor/air/solenoid/gear train as applicable
- local handwheel/manual override
- limit/position switches
- power source and control channel
- pneumatic/hydraulic supply and exhaust/return
- interlocks/permissives
- stroke/opening/closing time where applicable
- leakage/seat requirements where public
- seismic/safety/electrical class
- support/restraint
- maintenance/removal access
- bypass/equalizing/drain/vent connections attached to the valve assembly
- fasteners, packing, gaskets and seals where public

## Pump and heat-exchanger auxiliary rule

Every pump search must include suction/discharge isolation, checks, minimum-flow/recirculation, vent, drain, seal or canned-motor cooling, lube systems, instrument taps, motor/power/control, supports and maintenance interfaces.

Every heat exchanger search must include both fluid sides, all inlet/outlet isolation, bypass if present, vents, drains, reliefs, instrumentation, supports, channel/head or shell access, tubes/tubesheets/plates, gaskets/bolting and connected cooling-water or service-water train down to its ultimate heat sink.

## Electrical-path equivalent

The same zero-orphan principle applies electrically. A load is not complete at `powered by bus`. Trace transformers, switchgear, breakers, disconnects, buses, motor-control centers, distribution panels, cables, penetrations, trays/conduits, junction/termination boxes, grounding/bonding, protective relays, control power, instrumentation power and redundant/backup feeds where public.

## Evidence rule

This checklist is an obligation to search, not permission to invent. Generic industrial practice may identify what to look for, but an AP1000-specific object is created as factual only from controlled public evidence. If public evidence does not resolve it, record the unresolved item and the documents/drawings expected to close it.
