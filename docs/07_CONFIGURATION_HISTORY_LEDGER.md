# AP1000 Public Configuration History Ledger

## Purpose

The AP1000 public record contains preliminary, superseded, licensing-change, construction, and final/as-built descriptions. This ledger prevents obsolete public details from being blended into the current Revision-19 generic baseline or the Vogtle Unit 3 current-public model.

A historical feature remains useful evidence, but it must not be instantiated as current hardware unless the controlling configuration confirms it.

## Status vocabulary

- `CURRENT_BASELINE` — accepted for the stated current configuration.
- `PLANT_SPECIFIC_CURRENT` — current for the named plant/unit only.
- `SUPERSEDED` — publicly documented older design replaced before/current certification or construction.
- `CONFIRMED_ABSENT` — feature explicitly removed from the current modeled configuration.
- `HISTORY_ONLY` — retained only to understand the design evolution.
- `UNRESOLVED_CONFIG` — competing public records exist and the current controlling configuration has not yet been proven.

## CHG-001 — CMT outlet check-valve design

**Older public description:** Early AP1000 safety-evaluation text describes two series tilt-disc check valves in each CMT injection line.

**Change:** DCP 864 changed the CMT outlet check valves from tilting-disk to in-line/nozzle check valves. The NRC design-change inspection states that the change was incorporated into the AP1000 DCD. The same change added six safety-related 1-inch manual valves used for flow testing the CMT outlet check valves and removed remote position indication for those CMT check valves.

**Current evidence:** Vogtle Unit 3 public inspection records identify an AP1000 8-inch Class-1707 nozzle-check assembly and specifically identify PXS-PL-V016A as the ERV-Z/nozzle-check commodity family. Vogtle construction evidence distinguishes the CMT nozzle-check design from the accumulator 8-inch Class-1530 swing-check design.

**Disposition:**
- CMT tilt-disc check description: `SUPERSEDED` / history only.
- CMT in-line/nozzle checks V016A/B and V017A/B: `CURRENT_BASELINE` subject to final R19 P&ID/datasheet dimensional closure.
- Six 1-inch CMT-check test valves: function/quantity/size confirmed; individual tag-to-branch mapping remains `UNRESOLVED_CONFIG` until current P&ID/isometric confirmation.

**Controlled sources:** SRC-0424; SRC-0404; SRC-0417.

## CHG-002 — AP1000 reactor coolant pump cooling arrangement

**Older public description:** Preliminary AP1000 RCP descriptions included a thermal-barrier heat-exchanger arrangement and an earlier motor heat-exchanger configuration.

**Change/current configuration:** Later certified generic-pump changes eliminated the preliminary thermal-barrier heat exchanger and replaced the older wraparound motor exchanger arrangement with an externally mounted conventional shell-and-tube RCP heat exchanger. The pump still retains the pressure-boundary thermal-barrier component/function where documented; the obsolete auxiliary heat-exchanger implementation is not modeled as current hardware.

**Disposition:**
- preliminary thermal-barrier heat exchanger: `CONFIRMED_ABSENT` in current baseline.
- obsolete wraparound motor heat-exchanger arrangement: `SUPERSEDED`.
- current external RCP heat exchanger: `CURRENT_BASELINE`; detailed nozzle/support/CCS-side geometry remains unresolved.

**Controlled sources:** RCS source/document trail already maintained under WP-02; preserve exact DCD/licensing-change locator in the RCS configuration register.

## CHG-003 — Integrated Head Package cooling/cable/lifting arrangement

**Older public description:** Early AP1000 IHP depictions included fans mounted as part of the IHP and referred to a cable bridge.

**Change/current configuration:** The later certified IHP configuration relocates CRDM cooling fans to adjacent/support structure, replaces the obsolete cable-bridge concept with removable cable guides/support structure, adds stud-hoist rail support and revises the IHP lifting arrangement/load path.

**Disposition:**
- IHP-mounted CRDM cooling fans: `CONFIRMED_ABSENT` from current IHP assembly; fans remain plant hardware on adjacent support structure.
- old cable bridge: `CONFIRMED_ABSENT` / history only.
- removable cable guides/support structure: `CURRENT_BASELINE`.
- revised lift legs/sling block/clevis/sling-rod load path: `CURRENT_BASELINE` with member/fastener details still unresolved.

**Controlled sources:** SRC-0302 plus current R19/UFSAR IHP sources.

## CHG-004 — IRWST valve-tag discrepancy around V121

**Conflicting public evidence:** One 2017 inspection narrative refers to associated IRWST injection check valves V121A/B and V124A/B, while later Unit-3 preoperational testing, the COL risk-significant component list, and DCD-family tables consistently identify the IRWST injection check valves as V122A/B and V124A/B. Separate older/public design material identifies V121A/B as IRWST line isolation valves.

**Disposition:** `UNRESOLVED_CONFIG` for V121A/B function in the current Unit-3 model. Do not instantiate V121A/B as check valves from the isolated wording. V122A/B and V124A/B remain the confirmed IRWST injection check-valve families. Resolve V121A/B against current Unit-3 P&ID `SV3-PXS-M6-002` / controlling R19 P&ID before promotion.

**Controlled sources:** SRC-0415; SRC-0412; SRC-0420; SRC-0004.

## CHG-005 — PXS valve leak-test panel removal

**Older public/training description:** Older AP1000 material may describe the PXS valve leak-test subsystem as including a dedicated valve test panel.

**Change:** AP1000 design change `APP-GW-GEE-3449`, titled **Removal of PXS Valve Test Panel**, was approved for implementation. A later public Westinghouse AP1000 plant description still identifies the valve leak-test subsystem and permanent test connections for four PXS accumulator isolation check valves and eight RNS RCS-pressure-boundary valves, but does not describe the removed panel.

**Current disposition:**
- dedicated PXS valve test panel: `CONFIRMED_ABSENT` from current modeled configuration.
- permanent valve leak-test subsystem/test connections: `CURRENT_BASELINE`.
- exact piping/tubing, root/test valves, pressure-source routing, drains/vents and local connection hardware: `UNRESOLVED_CONFIG` until current R19/Unit-3 P&ID/isometric closure.

**Controlled sources:** SRC-0407 (`APP-GW-GEE-3449`); SRC-0414 Sec.6.6.1.2.4.

## CHG-006 — PXS valve leak-test subsystem design-pressure change

**Change:** AP1000 DCP `APP-GW-GEE-4560`, **PXS Valve Leak Test Subsystem Design Pressure Increase and Related Changes**, was approved after the earlier panel-removal change.

**Disposition:** `CURRENT_BASELINE` design-change history. Do not retain preliminary leak-test-line pressure classes/material selections merely because they occur in older public drawings. Exact revised design pressure, affected line classes, component ratings and support-analysis consequences must be resolved from the DCP/current R19 construction documents before geometry/specification freeze.

**Controlled source:** SRC-0407.

## Rule for future changes

Every newly discovered public design change that alters component type, quantity, tag, location, routing, material, actuation, support, electrical interface, or installed/removed status gets a ledger entry before the newer detail is allowed to overwrite an existing canonical object. The canonical database should reference the current feature; the historical feature remains queryable here or in a dedicated system-level configuration register.
