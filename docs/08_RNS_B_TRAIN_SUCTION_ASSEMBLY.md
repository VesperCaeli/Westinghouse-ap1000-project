# Unit 3 RNS B-Train Suction Assembly — Controlled Reconstruction Note

## Scope

This note expands the Unit-3 RNS reconstruction around `RNS-PL-V002B` from an isolated MOV object into the controlled B-train suction assembly. It is intentionally **not** a declaration that every local line transition, spool, support, instrument or electrical termination is already known.

The governing machine-readable registers are:

- `data/systems/PXS/unit3_rns_b_train_suction_assembly.csv`
- `data/systems/PXS/unit3_rns_b_train_suction_closure_gates.csv`
- `data/systems/PXS/unit3_rns_b_train_containment_ltop_retrieval.csv`
- `data/systems/PXS/unit3_rns_p19_penetration_decomposition.csv`
- the existing V002B electromechanical, EQRR, diagnostic, design-model and isometric recovery registers.

## Evidence-controlled topology

The earlier simplified picture of `V001B -> V002B -> containment penetration -> B pump` is superseded. U.S. AP1000 design evidence shows that the A/B hot-leg RCS-pressure-boundary branches recombine into a **common suction header before the containment crossing**.

```text
RCS hot leg / single RNS step-nozzle connection
  |
  |  generic AP1000 connection basis: 20-in Sch 140
  v
inside-containment parallel RCS-pressure-boundary suction paths
  |
  +--> A branch: V001A -> V002A --+
  |                                 |
  +--> B branch: V001B -> V002B --+----> common RNS suction header
                                           |
                                           |  V021 LTOP relief branch is located
                                           |  off the suction header inside containment;
                                           |  exact Unit-3 takeoff remains open
                                           v
                                  SV3-RNS-PY-C01 / P19
                                  RCS to RHR Pump Out
                                  common suction mechanical penetration
                                           |
                                           |  outside-containment common suction header
                                           |  single normally closed MOV in U.S. design;
                                           |  exact tag-to-sequence bridge still to be closed
                                           v
                                    downstream branch split
                                      /              \
                               pump-A path        pump-B path
                                                     |
                                                     | V005B pump-B suction isolation exists;
                                                     | exact local line remains open
                                                     v
                                      B-train downstream suction family
                                      L004B/L005B/L006B/L007B/L009B
                                                     |
                                     L006B convergence at design level
                                         ^                    ^
                                         |                    |
                                      L065B                L052B
                                   common suction       HX-bypass return
                                                     |
                                      V033B suction-pressure branch
                                      V036B suction-drain branch
                                                     v
                                                RNS-L009B
                                                     |
                                   SV3-RNS-PLW-09B-15
                                  10-in Sch-80 CJP to pump
                                                     v
                                                RNS-MP-01B
```

The diagram does **not** assert a locally exact `L004B -> L005B -> L006B -> L007B -> L009B` spool sequence. The generic Westinghouse construction-verification tables establish the downstream line family and the `L006B` convergence relationships; direct Unit-3 construction evidence independently fixes `L009B` at the MP-01B suction nozzle. The local line-number transitions around V002B, the common-header line number through P19, the outside-containment isolation valve placement, and exact V005B placement still require the current Unit-3 P&ID/isometric/line-designation records.

## P19 common suction containment penetration

The suction penetration itself is now substantially resolved at the Unit-3 hardware-identity level.

- NRC construction records identify **`SV3-RNS-PY-C01` as P19, `RCS to RHR Pump Out`** (`SRC-0730`).
- This is the **common RNS suction penetration** after the two V001/V002 parallel RCS-pressure-boundary branches recombine, not a dedicated B-train or V002B-only penetration (`SRC-0733`).
- The public 2017 construction inventory identifies installation work package **`SV3-RNS-MLW-860363`**, *ASME Section III - Installation of Containment Vessel Penetration SV3-RNS-PY-C01 (P19)* (`SRC-0732`).
- The three named P19 pressure-boundary welds are:
  - `SV3-RNS-PY-C01-1` — sleeve extension to penetration sleeve;
  - `SV3-RNS-PY-C01-2` — guard pipe to penetration sleeve;
  - `SV3-RNS-PY-C01-3` — flued head to guard pipe (`SRC-0730`).
- NRC identifies final radiography review for weld `-1` on the inside-containment side and `-2` on the outside-containment side, and separately lists the P19 RT report family including `V-16-RT-301-0242`, `-0246`, and `-0254` (`SRC-0730`, `SRC-0731`).
- Controlled geometry routes now include `SV3-RNS-MLK-881065` P19 weld map, `SV3-ML10-V6-003` P19 flued-head detail, `SV3-1100-P0-906` mechanical-penetration details, `SV3-MV50-V2-062` sleeve extensions, `SV3-MV50-V1-015` penetration list, `SV3-MV50-V1-016` penetration location, and the sleeve/ring drawings (`SRC-0731`, `SRC-0734`, `SRC-0715`).

Still unresolved are the actual P19 shell azimuth/elevation, sleeve/guard/flued-head dimensions and materials, process-pipe line number through the assembly, exact common-header spool geometry, supports/restraints, and final installation/turnover details. Those values must come from the recovered drawings/work package rather than from another AP1000 penetration.

## B-side V001B/V002B relationship to P19

The design basis now supports a more precise description of the B-side boundary:

- `RNS-PL-V001B` is the inner series hot-leg suction RCS-pressure-boundary MOV.
- `RNS-PL-V002B` is the outer B-side series hot-leg suction MOV, ASME Class 1 / IST Category A, and the containment-isolation member of its two-valve branch (`SRC-0702`).
- Westinghouse describes the V002 member as the valve in each pair closest to the containment penetration (`SRC-0714`).
- U.S. NRC design text establishes that the two parallel V001/V002 paths then connect to a **common suction header before the containment crossing** (`SRC-0733`).
- Therefore `V002B -> P19` is not to be represented as a direct exclusive B-train pipe segment. The unresolved B-side geometry is `V002B outlet -> B-branch spool/junction -> common suction header -> P19`.

The exact V002B outlet line number, branch-combining fitting, header line number, spool lengths, fittings, welds, supports and distance to P19 remain open. This also means PLW-015/L005 remains a candidate drawing route rather than proof of the V002B outlet line.

## Separate pressure-relief branches

Two different relief functions remain separate graph branches.

1. **RCS pressure-boundary thermal relief:** `RNS-PL-V003B` is the B-side thermal-relief check valve and is directly present in the Unit-3 RNS EQ population; `RNS-PL-V004B` is the separately identified thermal-relief isolation valve. The exact branch takeoff, local line number, restrictor/orifice hardware, sequence/spacing and downstream routing remain to be recovered (`SRC-0701`, `SRC-0704`).
2. **Low-temperature overpressure protection:** `RNS-PL-V021` is the Unit-3 RNS hot-leg suction pressure relief valve and is directly bridged to PV16 Datasheet 105 / its QME-1 qualification family (`SRC-0711`, `SRC-0716`). U.S. AP1000 system-description evidence places the LTOP relief branch **off the RNS suction header inside containment** (`SRC-0733`). AP1000 LTOP design evidence establishes a minimum required relief capacity of 850 gpm, 500-psig nominal set pressure and 550-psig full-open pressure at 10% accumulation (`SRC-0717`). Those are design requirements, not the final Unit-3 production-test results. NUREG-1793 remains internally inconsistent on the final discharge destination: the RNS system description says IRWST while the detailed LTOP evaluation says containment sump. The Unit-3 P&ID/isometric and Index 372/373 completion records must resolve that conflict.

These branches must not be merged into one generic “relief branch.”

## Outside-containment common suction header

U.S. NRC design text states that once the common RNS suction header is outside containment it contains a **single normally closed motor-operated isolation valve**; downstream of that valve the header branches to the two RNS pumps, with a normally open manual isolation valve upstream of each pump (`SRC-0733`).

The Vogtle UFSAR separately identifies `RNS-PL-V022` as the **RNS Suction Header Containment Isolation** valve and `RNS-PL-V005A/B` as the pump suction isolation valves (`SRC-0704`). That makes V022 the leading tag candidate for the single common-header MOV described by the U.S. FSER, but this project will not promote the exact tag-to-sequence bridge until the current Unit-3 P&ID or functional-requirement record explicitly closes it. V005B remains a known B-pump suction-isolation object whose exact line segment still requires the site drawing.

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

`RNS-MP-01B` retains three evidence layers that must remain separate:

- **Direct Unit-3 physical anchor:** `RNS-L009B` to `RNS-MP-01B` weld `SV3-RNS-PLW-09B-15`, 10-inch Schedule-80 CJP, plus independently inspected suction slope (`SRC-0706`).
- **Design/qualification family:** MP08 qualification records identify a Flowserve Flow Solutions Group 6X19WD coupled-pump family and `APP-MP08-VDR-001` is explicitly mapped to MP-01B in the RNS completion-plan route (`SRC-0701`, `SRC-0709`).
- **Installation history:** public work-package inventory includes both `SV3-RNS-MPW-ME0753` (*RNS-MP-01B Set & Anchor*) and a later `SV3-RNS-MPW-ME1743` (*Disassembly of Residual Heat Removal Pump B*) (`SRC-0708`).

Therefore the initial set-and-anchor condition is not to be promoted to the final as-built pump state until reassembly/alignment/turnover records are recovered.

## Support, instrumentation and electrical boundaries

The assembly register carries these boundaries explicitly:

- `SV3-RNS-PH-12Y2060` as a Unit-3 RNS support/snubber candidate requiring exact L006/site placement reconciliation (`SRC-0612`).
- `SV3-RNS-PHW-861876` as the support work-package route associated with `SV3-RNS-PLW-015`, requiring package-index recovery before individual supports are assigned (`SRC-0608`).
- `RNS-PL-V033B` plus a separate unresolved downstream pressure-instrument endpoint (`SRC-0704`).
- `RNS-PL-V036B` plus a separate unresolved downstream drain destination (`SRC-0704`).
- `IDSB-DK-1` / Division-B 250-Vdc source boundary for V002B, the installed `SV3-RNS-EW-PLV002BBXB` / P31Y cable interface, and the still-open P31Y ORC/feedthrough/pin/raceway/local-pigtail details.
- `ZOS-MG-02B` as the documented Unit-3 standby source for RNS Pump 1B; normal feeder, switchgear/breaker/starter, protection, motor/cable details and transfer implementation remain open (`SRC-0710`).

## Next retrieval priorities

The highest-value next records are now:

1. `SV3-MV50-V1-016` + `SV3-MV50-V1-015` + `SV3-RNS-MLK-881065` + `SV3-ML10-V6-003`, specifically querying **P19**, to close its azimuth/elevation, hardware dimensions and weld locations.
2. `SV3-RNS-MLW-860363`, to close P19 material traceability, installation details, NDE bridges and final turnover.
3. Current Unit-3 RNS P&ID / `SV3-RNS-M6K-FA201` / `SV3-RNS-M6X-004`, to identify the V002A/B branch-combining point, common-header line number, outside common-header MOV tag, V021 takeoff, and downstream pump split.
4. PLW-015, to resolve L005/L029/L080 geometry and determine whether it actually contains the V002/common-header region.
5. Unit-3 LTOP ICNs `ML18120A270` / `ML18117A424`, to close V021 actual capacity/set pressure and help resolve its discharge path.
6. Final RNS Index-361 EQRR/PCD and V002B row.
7. `SV3-PV01-VDR-000002` V002B row and exact referenced PV01-V2 assembly drawing.
8. `SV3-RNS-T0W-1237493` diagnostic result package.
9. MP-01B post-disassembly reassembly/alignment/turnover records and pump-support drawings.
10. V033B instrument endpoint, V036B drain destination, V002B DK01/P31Y circuit closure and MP-01B normal feeder/control circuit.

Until those records are recovered, unresolved interfaces remain explicit graph boundaries rather than being filled by symmetry, line-number patterns or generic-family assumptions.
