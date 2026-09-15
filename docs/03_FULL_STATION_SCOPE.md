# Full-Station Scope Boundary

## Governing scope rule

The reconstruction boundary is the **entire AP1000 generating station and every publicly resolvable system physically or functionally connected to it**, not only the nuclear steam supply system.

A system is in scope if it does any of the following:

- supplies the plant with power, water, fuel, air, gas, chemicals, cooling, heating, ventilation or communications;
- removes heat, water, steam, waste, sewage, gases, effluent or electrical power from the plant;
- conditions or treats any fluid used by the plant;
- transforms, distributes, converts, stores or backs up electrical energy;
- supports operation, startup, shutdown, refueling, maintenance, fire protection or emergency response;
- provides a heat sink or heat source for another plant system;
- supports equipment through lubrication, seal fluid, cooling, heating, control fluid, starting air or ventilation;
- crosses a building, yard, site or utility boundary associated with the selected plant baseline.

Nothing is excluded merely because it is "balance of plant," "non-safety," "conventional," "site utility," or outside containment.

## Electrical generation, transformation and grid interface

The model must include all publicly resolvable equipment from generator terminals to the defined utility-grid/site boundary, including as applicable:

- main generator and excitation interfaces;
- generator isolated-phase bus / bus duct and associated supports;
- generator circuit breaker if present in the selected baseline;
- generator step-up transformer(s);
- unit auxiliary / station service transformer(s);
- reserve / startup / offsite source transformer(s);
- auxiliary transformers and distribution transformers;
- switchyard or switchyard interface equipment within the public plant scope;
- transmission-line termination/interface points;
- surge arresters, disconnects, grounding switches, instrument transformers, bushings and neutral-grounding equipment where public;
- transformer cooling hardware: radiators/coolers, fans, pumps, oil circuits, conservators or equivalent expansion arrangements, nitrogen systems where applicable, temperature/level/pressure instrumentation, fire protection and containment/drainage;
- switchgear, buses, breakers, motor-control centers, panels and local disconnects;
- protective relaying and metering interfaces where publicly resolvable;
- AC distribution at all voltage levels;
- DC distribution, batteries, racks, chargers, inverters and UPS equipment;
- raceways, cable trays, conduits, penetrations, junction/terminal boxes, grounding grids, bonding and lightning protection where within public scope.

Every transformer is an equipment assembly with explicit high-voltage, low-voltage, tertiary/auxiliary if applicable, grounding, cooling, monitoring, protection, structural, oil-containment and fire-protection interfaces rather than a single decorative object.

## Onsite standby and emergency/defense-in-depth power

All publicly documented onsite standby generators are decomposed to the same standard as reactor equipment. A generator set is not one object.

For each diesel-generator installation, resolve where applicable and publicly available:

- diesel engine block/crankcase/cylinders/heads;
- crankshaft, connecting rods, pistons, cam/valve gear and flywheel where public;
- starting system, including starting-air receivers/compressors or electric starters as applicable;
- generator/alternator, excitation, AVR and output breaker;
- local and remote control/protection panels;
- day tank(s);
- bulk fuel-oil storage tank(s);
- fuel-oil transfer pumps, strainers/filters, heaters if present, supply/return piping, vents, drains and overflow paths;
- tank level/temperature/leak instrumentation;
- fuel unloading/fill connections and transfer route;
- lube-oil reservoir/sump, pumps, filters, coolers and piping;
- engine jacket-water cooling loop, pumps, heat exchangers/radiators and expansion/surge tank;
- combustion-air intake, filters, silencers and ducting;
- exhaust manifolds, piping, flexible connections, silencers/stacks and supports;
- room ventilation and heat removal;
- engine/generator foundation, skid, vibration isolation, anchors and maintenance access;
- batteries/chargers or other starting/control-power supplies;
- fire detection/suppression and drainage/containment around fuel systems;
- all control, alarm, trip and status signals.

If an AP1000 safety function is passive and therefore does not require a conventional safety-related emergency diesel generator, that does **not** remove the documented non-safety onsite standby generators or their auxiliaries from scope.

## Water-source, treatment and chemistry systems

The model includes all public plant water sources, treatment processes, storage, transfer and discharge paths. This includes, as applicable to the selected plant baseline:

- raw-water source/intake/interface;
- intake screens, strainers, pumps and associated structures;
- pretreatment equipment;
- clarifiers/settling equipment where present;
- filtration systems;
- multimedia/cartridge filters where present;
- reverse osmosis, electrodialysis or other membrane systems where present;
- demineralizers/ion exchangers;
- regeneration chemical systems;
- acid/caustic/chemical storage, day tanks, metering pumps and transfer piping;
- degasification/decarbonation equipment where present;
- demineralized-water treatment system;
- demineralized-water storage and transfer system;
- condensate cleanup/polishing where used;
- potable-water treatment/storage/distribution;
- sanitary-water and sanitary-drainage interfaces;
- wastewater collection, treatment, neutralization and discharge;
- oily-water collection/separation where present;
- storm-water/site drainage interfaces;
- cooling-tower makeup and blowdown treatment;
- chemistry sampling, analyzers, chemical-injection skids, sample coolers and drains;
- tank vents, overflows, drains, recirculation paths and freeze/heat-trace systems where documented.

Every treatment train is represented stage by stage. "Water treatment plant" is not an acceptable terminal node.

## Heat exchangers and cooling hierarchy

Every heat exchanger in the public plant design is cataloged individually and assigned both a hot-side and cold-side owning system. No heat exchanger is represented without resolving both sides.

Heat-exchanger classes to capture include, wherever present:

- steam generators;
- passive residual heat removal heat exchanger;
- component cooling water heat exchangers;
- turbine-building closed-cooling-water heat exchangers;
- chilled-water chillers/evaporators/condensers;
- lube-oil coolers;
- seal-oil or seal-water coolers;
- generator coolers;
- transformer oil coolers/radiators;
- diesel-generator jacket-water coolers/radiators;
- diesel-generator lube-oil coolers;
- sample coolers;
- feedwater heaters;
- moisture-separator reheaters;
- gland-steam condensers or equivalent auxiliary condensers where present;
- main condenser;
- condenser vacuum-pump seal-water heat exchangers;
- HVAC heating/cooling coils;
- miscellaneous equipment coolers identified by DCD/UFSAR/as-built sources.

For each unit, record at minimum:

- equipment ID/tag;
- exchanger type;
- quantity;
- hot-side system, inlet and outlet;
- cold-side system, inlet and outlet;
- bypass/recirculation paths;
- isolation, control, balancing, drain and vent valves;
- relief devices where applicable;
- shell/channel/head/tubes/plates/coil internals to public-source fidelity;
- materials, dimensions, pressure/temperature ratings and heat duty where public;
- supports, anchors, insulation and maintenance/removal clearances;
- fouling/cleaning interfaces and removable heads/manways where present;
- instrumentation and control loops.

A global `heat_exchangers` register will cross-reference every exchanger so an omitted cooling dependency can be detected automatically.

## Heat rejection and circulating-water systems

The station model extends through the ultimate/site heat-rejection equipment represented by the chosen plant-specific baseline. Include as applicable:

- main condenser;
- circulating-water pumps;
- intake/discharge structures;
- circulating-water piping, valves and expansion joints;
- cooling tower(s), basins, fill, distribution headers/nozzles and bypasses where used;
- cooling-tower makeup and blowdown;
- turbine-building closed cooling;
- service water and component cooling interfaces;
- condenser water boxes and associated vents/drains;
- condenser air-removal/vacuum systems;
- chemical treatment, corrosion/fouling control and monitoring;
- site-specific heat sink interfaces.

Generic DCD conceptual/site-specific equipment must be replaced or overlaid with actual public Vogtle configuration when the project reaches plant-specific reconciliation.

## Plant HVAC, chilled water and heating

Every building and equipment area must have its publicly documented environmental-support chain represented, including:

- supply, return, recirculation and exhaust fans;
- air-handling units;
- filters and high-efficiency filtration where applicable;
- dampers, isolation dampers and backdraft dampers;
- heating and cooling coils;
- chillers and associated refrigerant/cooling-water interfaces;
- chilled-water pumps, headers, expansion tanks and makeup;
- hot-water heating pumps, heat exchangers/heaters, expansion tanks and makeup;
- ducts, plenums, louvers and penetrations;
- room thermostats/sensors, differential-pressure instrumentation and controls;
- condensate drains;
- smoke/fire-damper interfaces;
- emergency habitability systems where documented.

## Fire protection and fire water

Include complete public fire-protection infrastructure, including as applicable:

- water source/reservoir/interface;
- fire pumps and jockey pumps;
- diesel/electric fire-pump auxiliaries where present;
- headers/ring mains;
- sectional isolation valves;
- hydrants/hose stations;
- sprinklers/deluge/preaction systems;
- transformer spray/deluge systems;
- diesel-generator-room protection;
- fire detection/alarm panels and field devices;
- gaseous/clean-agent systems where documented;
- drains and containment of fire-water discharge.

## Compressed gases, service gases and breathing/utility air

Include, where present:

- service air;
- instrument air;
- compressors and aftercoolers;
- intercoolers;
- dryers;
- receivers;
- filters/separators;
- condensate traps/drains;
- distribution headers and local drops;
- nitrogen/hydrogen/carbon-dioxide or other plant gases used by generator, tanks, maintenance or process systems;
- gas bottle/manifold or bulk storage systems where public;
- pressure regulation, relief and monitoring.

## Turbine-generator and conventional island auxiliaries

The turbine island receives the same fidelity as the nuclear island, including:

- HP/LP turbine sections;
- stop/control/intercept valves;
- bearings and bearing-oil systems;
- turning gear;
- turbine lube/control oil;
- generator stator/rotor/cooling interfaces;
- hydrogen seal-oil/gas systems if used by the selected generator design;
- gland sealing/extraction;
- moisture separation/reheat;
- condenser and hotwell;
- condensate pumps;
- condensate polishing/cleanup where present;
- low/high-pressure feedwater heaters;
- deaeration functions if applicable;
- feedwater booster/main feed pumps and drives;
- heater drains;
- startup feedwater;
- main steam and turbine bypass/dump;
- drains, vents, warmup lines and extraction-steam interfaces.

## Waste, drainage and environmental discharge

Include all publicly documented radioactive and non-radioactive waste/effluent paths:

- liquid radwaste;
- gaseous radwaste;
- solid radwaste interfaces;
- radioactive drains;
- nonradioactive equipment/floor drains;
- oily wastewater;
- chemical drains;
- sanitary waste;
- storm drainage;
- cooling-water blowdown;
- monitored release points and associated instrumentation where public;
- tanks, sumps, pumps, filters, separators, evaporative/processing equipment and treatment stages.

## Site and maintenance infrastructure

Where part of the selected public plant design, also include:

- warehouses and maintenance shops;
- chemistry laboratories;
- hot machine shop/controlled maintenance facilities;
- cranes, hoists, monorails and elevators;
- refueling/fuel-handling support areas;
- laydown and equipment-removal paths;
- road/rail/heavy-haul interfaces needed for major equipment;
- auxiliary boilers/heaters or temporary/startup services where installed;
- lighting and receptacle distribution;
- normal building services;
- site communications/public-address interfaces where public;
- cathodic protection where used;
- freeze protection/heat tracing;
- sump pumps, groundwater/dewatering systems and building drainage where documented.

## External-boundary rule

The model may stop only at a named, auditable external boundary such as:

- transmission/grid interconnection;
- raw-water source/intake boundary;
- treated municipal-water boundary;
- sanitary-sewer boundary;
- stormwater/outfall boundary;
- natural-gas/fuel-delivery boundary;
- chemical-delivery/unloading connection;
- rail/road receiving boundary;
- shared multi-unit/site-service boundary.

The final internal component must connect to that boundary explicitly. "Goes offsite" or "connects to utility" is not a valid endpoint.

## Site-specificity rule

Some AP1000 balance-of-plant systems are intentionally site-specific or conceptual in the generic DCD. Those items remain in the generic model with their evidence state and COL-action/site-specific status, then receive a `VOGTLE-3-CURRENT-PUBLIC` overlay using the current public licensing/as-built record.

Do not silently combine the reference cooling tower, generic switchyard, generic water supply or other conceptual DCD feature with the actual Vogtle configuration.

## Completeness consequence

A reactor-system work package cannot be considered globally closed merely because its own equipment is complete. If it depends on another system, that dependency becomes a tracked boundary and remains open until the other system is modeled.

Examples:

- an RCP is not globally complete until its component-cooling, electrical/VFD, instrumentation, structural and maintenance interfaces close;
- a diesel generator is not complete until fuel, cooling, lubrication, starting, air/exhaust, ventilation, electrical and fire-protection interfaces close;
- a transformer is not complete until electrical, grounding, cooling, protection, oil containment/drainage, structural and fire-protection interfaces close;
- a heat exchanger is not complete until **both** process sides and all bypass/drain/vent/control paths close.
