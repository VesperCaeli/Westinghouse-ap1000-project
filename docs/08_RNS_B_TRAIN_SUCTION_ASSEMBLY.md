# Unit 3 RNS B-Train Suction Assembly — Controlled Reconstruction Note

## Scope

This note expands the Unit-3 RNS reconstruction around `RNS-PL-V002B` from an isolated MOV object into the controlled B-train suction assembly. It is intentionally **not** a declaration that every local line transition, spool, support, instrument or electrical termination is already known.

The governing machine-readable registers are:

- `data/systems/PXS/unit3_rns_b_train_suction_assembly.csv`
- `data/systems/PXS/unit3_rns_b_train_suction_closure_gates.csv`
- `data/systems/PXS/unit3_rns_b_train_containment_ltop_retrieval.csv`
- the existing V002B electromechanical, EQRR, diagnostic, design-model and isometric recovery registers.

## Evidence-controlled topology

```text
RCS hot leg
  |
  |  generic AP1000 connection basis: 20-in Sch 140
  v
RNS-L001 / RNS-L002B family
  |
  v
RNS-PL-V001B  inner hot-leg suction MOV
  |  + V001B-M motor-operator child boundary
  |  + V001B-L limit/position-switch child boundary
  |
  |  exact Unit-3 pressure-boundary spool / containment-transition geometry OPEN
  v
RNS-PL-V002B  outer hot-leg suction / containment-isolation MOV
  |  + design-level spatial constraint: containment-isolation member closest to suction penetration
  |  + Unit-3 penetration number / shell coordinates / exact valve-to-shell distance OPEN
  v
RNS downstream suction family
  L004B / L005B / L006B / L007B / L009B
  |
  +--------------------------+
  |                          |
  |                L006B convergence is controlled at design level
  |                    ^                 ^
  |                    |                 |
  |                 L065B             L052B
  |              common suction    HX-bypass return
  |                          |
  |          exact Unit-3 fitting/coordinates OPEN
  |
  |  V005B pump-B suction isolation exists; exact local segment/valve details OPEN
  |  V033B pump-B suction-pressure instrument isolation exists;
  |        downstream pressure instrument/loop OPEN
  |  V036B pump-B suction-piping drain isolation exists;
  |        receiving drain system/path OPEN
  v
RNS-L009B
  |
  |  SV3-RNS-PLW-09B-15
  |  direct Unit-3 evidence: 10-in Sch-80 CJP L009B -> MP-01B
  v
RNS-MP-01B
  |
  + anchor/support drawing routes: APP-1215-CE-003, APP-MZ12-V1-001/-002
  + installation-history gate: SV3-RNS-MPW-ME0753 Set & Anchor
  + later configuration-history gate: SV3-RNS-MPW-ME1743 Disassembly
  + standby-source boundary: ZOS-MG-02B
  + generic MCR Start / run-status interface
```

The diagram above **does not** assert a locally exact `L004B -> L005B -> L006B -> L007B -> L009B` spool sequence. The generic Westinghouse construction-verification tables establish the downstream line family and the `L006B` convergence relationships; direct Unit-3 construction evidence independently fixes `L009B` at the MP-01B suction nozzle. The local line-number transitions around V002B and the exact placement of V005B still require the current site P&ID/isometric/line-designation records (`SRC-0613`, `SRC-0607`, `SRC-0608`, `SRC-0705`, `SRC-0706`).

## Separate pressure-relief branches

Two different relief functions are retained as separate graph branches.

1. **RCS pressure-boundary thermal relief:** `RNS-PL-V003B` is the B-side thermal-relief check valve and is directly present in the Unit-3 RNS EQ population; `RNS-PL-V004B` is the separately identified thermal-relief isolation valve. The exact branch takeoff, local line number, restrictor/orifice hardware, sequence/spacing and downstream routing remain to be recovered (`SRC-0701`, `SRC-0704`).
2. **Low-temperature overpressure protection:** `RNS-PL-V021` is the Unit-3 RNS hot-leg suction pressure relief valve and is directly bridged to PV16 Datasheet 105 / its QME-1 qualification family (`SRC-0711`, `SRC-0716`). AP1000 LTOP design evidence establishes a minimum required relief capacity of 850 gpm, 500-psig nominal set pressure and 550-psig full-open pressure at 10% accumulation (`SRC-0717`). Those are design requirements, not the final Unit-3 production-test results. NUREG-1793 Chapter 5 is internally inconsistent on the discharge destination: its RNS design description says the relief valve discharges to the **IRWST**, while its detailed LTOP evaluation says it discharges to the **containment sump**. The destination is therefore an explicit unresolved conflict, not a resolved graph endpoint (`SRC-0712`). Unit-3 `SV3-RNS-M6-003`, the applicable isometric and ITAAC Index 372/373 records are the closure route.

These branches must not be merged into one generic “relief branch.” The earlier project phrase `containment sump/containment atmosphere` for V021 is superseded; containment atmosphere was not supported by the controlled Chapter-5 passages.

## Containment and pressure-boundary transition

The design basis resolves more of the sequence than the earlier register carried, while exact site geometry remains open:

- `RNS-PL-V001B` is the **inner** series hot-leg suction RCS-pressure-boundary MOV.
- `RNS-PL-V002B` is the **outer** series hot-leg suction MOV, an ASME Class-1 / IST Category-A RCS-pressure-boundary and containment-isolation valve (`SRC-0702`).
- Westinghouse describes the containment-isolation member of each two-valve suction pair as the valve **closest to the containment penetration** (`SRC-0714`). This fixes the V001-inner → V002-outer-nearest-penetration ordering, but does not supply a valve-to-shell distance or prove zero intervening spool length.
- The certified RCS-to-RHR-pump containment-isolation table assigns the penetration isolation function to `RNS-PL-V002A/B`, with safety-related closure signals and the documented leak-rate-test boundary behavior (`SRC-0703`).
- NRC's Unit-3 containment functional-arrangement inspection reviewed `SV3-RNS-M6-003` Rev.4 together with `SV3-MV50-V1-016` Rev.1, *Containment Vessel Penetration Location*. These are now the preferred retrieval pair for the exact Unit-3 mechanical penetration identifier and shell location (`SRC-0715`).
- The exact penetration number, liner/sleeve/embedment, spool through the shell, welds, coordinates, room/elevation, restraints/supports and V001B/V002B centerline relationship remain open.

No penetration number or shell geometry is to be fabricated from the functional tables or generic spatial language.

## V002B remains gated at exact-hardware level

Expanding the surrounding train does **not** relax the V002B evidence standard. The following remain explicit open closure gates:

| Gate | Controlled target | What it closes |
|---|---|---|
| Setup/VDR | `SV3-PV01-VDR-000002 Rev.2` | Exact V002B setup-table row, datasheet/configuration, stem/travel/gearing, switches and linked assembly/calculation records |
| Sizing | `APP-PV01-VDR-000001 Rev.2 / WCAP-18549` | Required thrust/torque, friction/packing/gearing inputs, degraded-voltage capability and margin |
| Final EQRR | Final RNS Index-361 EQRR / PCD, exact identifier still unresolved | Installed make/model/serial, orientation, anchorage, clearances, interfaces and as-built references |
| Diagnostics | `SV3-RNS-T0W-1237493 / CWA 3-21-0403` | V002B thrust/torque/travel/current/voltage/switch traces, calibration and as-found/as-left results |
| Assembly | Exact V002B/applicable-datasheet PV01-V2 assembly drawing, identifier unresolved | Valve/yoke/operator geometry, bolting/mounting, spring-pack and local physical interfaces |
| Manufacturing | Applicable `SV3-PV01-VQQ-*` / Flowserve final-data package | Production serial/order, material/heat traceability, code data and shop-test records |

The qualification-family result—Flowserve flex-wedge gate valve with Limitorque operator—remains a design/EQ-family result until the final V002B row establishes the installed unit details.

## MP-01B configuration control

`RNS-MP-01B` now has three different evidence layers that must remain separate:

- **Direct Unit-3 physical anchor:** `RNS-L009B` to `RNS-MP-01B` weld `SV3-RNS-PLW-09B-15`, 10-inch Schedule-80 CJP, plus independently inspected suction slope (`SRC-0706`).
- **Design/qualification family:** MP08 qualification records identify a Flowserve Flow Solutions Group 6X19WD coupled-pump family and `APP-MP08-VDR-001` is explicitly mapped to MP-01B in the RNS completion-plan route (`SRC-0701`, `SRC-0709`).
- **Installation history:** public work-package inventory includes both `SV3-RNS-MPW-ME0753` (*RNS-MP-01B Set & Anchor*) and a later `SV3-RNS-MPW-ME1743` (*Disassembly of Residual Heat Removal Pump B*) (`SRC-0708`).

Therefore the initial set-and-anchor condition is **not** to be promoted to the final as-built pump state until reassembly/alignment/turnover records are recovered.

## Support, instrumentation and electrical boundaries

The assembly register carries the following boundaries explicitly rather than leaving them implicit:

- `SV3-RNS-PH-12Y2060` as a Unit-3 RNS support/snubber candidate requiring exact L006/site placement reconciliation (`SRC-0612`).
- `SV3-RNS-PHW-861876` as the support work-package route associated with `SV3-RNS-PLW-015`, requiring package-index recovery before individual supports are assigned (`SRC-0608`).
- `RNS-PL-V033B` plus a separate unresolved downstream pressure-instrument endpoint (`SRC-0704`).
- `RNS-PL-V036B` plus a separate unresolved downstream drain destination (`SRC-0704`).
- `IDSB-DK-1` / Division-B 250-Vdc source boundary for V002B, the installed `SV3-RNS-EW-PLV002BBXB` / P31Y cable interface, and the still-open P31Y ORC/feedthrough/pin/raceway/local-pigtail details.
- `ZOS-MG-02B` as the documented Unit-3 **standby** source for RNS Pump 1B; normal feeder, switchgear/breaker/starter, protection, motor/cable details and transfer implementation remain open (`SRC-0710`).

## Next retrieval priorities

The highest-value next records are those that collapse multiple open fields at once:

1. `SV3-RNS-M6-003 Rev.4` + `SV3-MV50-V1-016 Rev.1`, to identify the exact RNS suction containment penetration and shell location, then bridge that result into the suction isometric.
2. Current Unit-3 RNS P&ID / `SV3-RNS-M6K-FA201` / line-designation contents and the relevant suction isometrics, to place V001B/V002B, V003B/V004B, V021, V005B, V033B and V036B on exact lines and spools.
3. Unit-3 LTOP ICNs `ML18120A270` / `ML18117A424` and their referenced code-data/test records, to close V021 actual capacity/set pressure and help resolve its discharge path.
4. Final RNS Index-361 EQRR/PCD and V002B row.
5. `SV3-PV01-VDR-000002` V002B row and exact referenced PV01-V2 assembly drawing.
6. `SV3-RNS-T0W-1237493` diagnostic result package.
7. MP-01B post-disassembly reassembly/alignment/turnover work packages and the contents of the pump anchor/support drawings.
8. V033B instrument endpoint/loop and V036B drain destination.
9. V002B DK01 branch + P31Y ORC/feedthrough/raceway/pigtail closure and MP-01B normal feeder/control circuit.

Until those records are recovered, the model should represent the unresolved interfaces as explicit graph boundaries rather than filling them with symmetry, sibling or generic-family assumptions.
