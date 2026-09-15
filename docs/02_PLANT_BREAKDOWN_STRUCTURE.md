# Plant Breakdown Structure (PBS) — Foundation

This is the configuration hierarchy for the 1:1 reconstruction. It is intentionally broader than the operator-system taxonomy in NUREG-2103; operator catalogs omit many civil, structural, maintenance, local utility, and balance-of-plant details that still have to exist in the model.

## PBS-00 Plant and configuration control

- AP1000 unit root
- generic DCD Revision 19 configuration
- plant-specific variant overlays
- site and external interface boundaries
- coordinate system, survey datum, elevations, grids, room/zone identifiers

## PBS-10 Site, yard, and external interfaces

- site civil works
- yard piping and duct banks
- external electrical interfaces
- switchyard boundary/interface
- water intake/discharge interfaces
- site drainage interfaces
- roads/laydown/maintenance interfaces where part of public design scope

## PBS-20 Buildings, civil structures, and architectural fabric

- nuclear island civil structure
- containment vessel and shield building civil interfaces
- auxiliary building
- turbine building
- annex/administrative/support structures represented in the public design basis
- radwaste building
- diesel-generator/standby-power structures where applicable
- foundations, slabs, walls, floors, roofs, embeds, liners, doors/hatches, penetrations, stairs, ladders, platforms, gratings, rails, local structural steel

## PBS-30 Reactor and reactor internals

- reactor vessel
- vessel head and integrated head-package interfaces
- core support structures
- core barrel/baffles/formers and other public-source-visible internals
- fuel assemblies and control components at the fidelity supported by public sources
- control rod drive mechanisms and position indication interfaces
- incore instrumentation interfaces
- vessel supports, insulation, access and handling interfaces

## PBS-40 Reactor coolant and connected systems

- reactor coolant system (RCS)
- reactor coolant pumps
- steam generators — primary-side boundary
- pressurizer and associated pressure/level-control hardware
- chemical and volume control system
- normal residual heat removal system
- connected vents, drains, sampling, purification, charging/makeup/letdown interfaces
- pressure-boundary supports, snubbers/restraints where applicable and publicly documented

## PBS-50 Passive safety and engineered safety features

- passive core cooling system
- core makeup tanks
- accumulators
- in-containment refueling water storage tank interfaces
- automatic depressurization functions and associated public-source-visible hardware
- passive residual heat removal system/heat exchanger
- containment isolation functions
- passive containment cooling system
- containment hydrogen-control equipment
- associated actuation, instrumentation, valves, piping, vents, drains and supports

## PBS-60 Instrumentation, control, and protection

- reactor trip system
- engineered safeguards actuation system
- diverse actuation system
- nuclear instrumentation system
- incore instrumentation system
- post-accident monitoring
- plant control systems
- local instrumentation, transmitters, switches, analyzers, cabinets, panels, junction boxes and public-source-visible signal interfaces

## PBS-70 Electrical power and distribution

- main generation interfaces
- main AC distribution
- Class 1E and non-Class 1E DC/UPS systems
- batteries/chargers/inverters
- onsite standby power
- transformers, switchgear, buses, breakers, motor-control centers, distribution panels
- grounding/bonding and raceway/cable-tray hierarchy where public sources support it

## PBS-80 Plant auxiliary and service systems

- compressed/instrument/service air
- component cooling water
- service water
- circulating water
- demineralized/water-storage systems
- plant gas systems
- sampling systems
- heating/chilled-water systems
- drains and sumps
- fire protection
- miscellaneous plant utility systems revealed by DCD/UFSAR source extraction

## PBS-90 Fuel handling and spent-fuel systems

- new-fuel receipt/handling interfaces
- refueling equipment
- fuel handling machines and cranes where public
- spent-fuel pool structures and cooling/cleanup
- fuel-transfer interfaces
- tools, racks, lifting and handling interfaces supported by public documentation

## PBS-100 HVAC and environmental control

- containment ventilation/filtration interfaces
- radiologically controlled area ventilation
- main control room HVAC/emergency habitability
- turbine building ventilation
- radwaste building HVAC
- auxiliary/annex building ventilation
- health physics/hot-machine-shop HVAC
- chilled-water/hot-water interfaces
- ducts, dampers, filters, coils, fans, plenums, louvers, drains, controls and supports

## PBS-110 Steam, turbine, feedwater, condensate, and heat rejection

- steam generator secondary side
- main steam
- main/startup feedwater
- steam dump/bypass
- turbine-generator
- moisture separation/reheat where applicable
- condenser and air-removal
- condensate/feedwater-heating train
- heater drains
- circulating-water/heat-rejection interfaces
- lube/seal/control-oil and generator gas auxiliaries

## PBS-120 Radioactive waste, sampling, and radiation monitoring

- liquid radwaste
- gaseous radwaste
- radioactive drains
- solid waste handling where within public AP1000 design basis
- process sampling
- radiation monitoring interfaces
- tanks, pumps, filters, demineralizers, evaporative/processing equipment where applicable and documented

## PBS-130 Mechanical handling, maintenance, and access

- polar/bridge/jib cranes and hoists
- monorails
- lifting fixtures
- removable shielding/access covers
- maintenance platforms
- equipment removal paths and service clearances when documented
- special tools when publicly documented

## PBS-140 Piping, valves, fittings, and supports

This PBS is cross-cutting and does not replace system ownership.

- line segments
- reducers/expanders
- elbows/bends
- tees/crosses/branches
- flanges/unions/couplings
- manual and actuated valves
- check valves
- relief/safety devices
- orifices/restrictors
- strainers/filters
- drains/vents/sample connections
- pipe supports, hangers, anchors, guides, restraints and penetration seals

Every item remains linked to its owning process system and physical route.

## PBS-150 Electrical/instrument raceways and local hardware

- cable trays
- conduit
- penetrations
- junction boxes
- terminal boxes
- local disconnects
- instrument tubing/impulse lines
- mounting brackets
- grounding jumpers
- cable/support hardware

## PBS-160 Equipment internals and common hardware

- shafts
- bearings
- seals/packing
- couplings
- impellers/rotors
- stators/windings where public
- diaphragms/pistons/springs
- actuator internals
- gaskets/O-rings
- bolts/studs/nuts/washers/pins/keys/retaining rings
- nameplates/tags

These are only populated as AP1000 facts when public evidence supports them. Generic stand-ins must be isolated as `REPRESENTATIVE`, never mixed into the verified AP1000 bill of material.

## Functional-system seed

NUREG-2103 provides a useful operator-facing AP1000 system taxonomy, including RCS, CVS, PXS, ADS, PRHR, RNS, SGS, feedwater/main-steam/condensate systems, containment/PCS, AC/DC/UPS/standby power, DAS/IIS/NIS/RMS/RTS, compressed air, CCS, circulating water, fuel handling, fire protection, spent-fuel cooling, HVAC/filtration, and gaseous/liquid radwaste.

That list is a **cross-check**, not a claim that those are all plant systems. DCD/UFSAR chapter-by-chapter extraction controls the eventual complete system register.
