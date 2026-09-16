# Unit 3 RNS B-Train Suction Assembly — Controlled Reconstruction Note

## Scope

This note expands the Unit-3 RNS reconstruction around `RNS-PL-V002B` from an isolated MOV object into the controlled B-train suction assembly. It is intentionally **not** a declaration that every local line transition, spool, support, instrument or electrical termination is already known.

The governing machine-readable registers are:

- `data/systems/PXS/unit3_rns_b_train_suction_assembly.csv`
- `data/systems/PXS/unit3_rns_b_train_suction_final_configuration_overlay.csv`
- `data/systems/PXS/unit3_rns_b_train_suction_closure_gates.csv`
- `data/systems/PXS/unit3_rns_b_train_containment_ltop_retrieval.csv`
- `data/systems/PXS/unit3_rns_dual_ltop_relief_decomposition.csv`
- `data/systems/PXS/unit3_rns_p19_penetration_decomposition.csv`
- the existing V002B electromechanical, EQRR, diagnostic, design-model and isometric recovery registers.

Where the final-configuration overlay conflicts with an older row in the base suction-assembly register, the overlay controls. This allows configuration corrections to remain explicit rather than silently rewriting the evidence history.

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
                                           +--> V020  1-in LTOP relief
                                           |      lower-capacity / lower-setpoint branch
                                           |
                                           +--> V021  3-in LTOP relief
                                           |      larger-capacity branch; PV16 Z0D-105 route
                                           |
                                           |  exact post-LAR takeoffs/outlet routing OPEN
                                           v
                                  SV3-RNS-PY-C01 / P19
                                  RCS to RHR Pump Out
                                  common suction mechanical penetration
                                           |
                                           |  outside-containment common suction header
                                           |  single normally closed MOV in U.S. design;
                                           |  V022 is the leading Unit-3 tag bridge
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

The diagram does **not** assert a locally exact `L004B -> L005B -> L006B -> L007B -> L009B` spool sequence. The generic Westinghouse construction-verification tables establish the downstream line family and the `L006B` convergence relationships; direct Unit-3 construction evidence independently fixes `L009B` at the MP-01B suction nozzle. The local line-number transitions around V002B, the common-header line number through P19, the exact V022 placement, V020/V021 takeoffs/outlets, and exact V005B placement still require current Unit-3 P&ID/isometric/line-designation records.

## P19 common suction containment penetration

The suction penetration itself is substantially resolved at the Unit-3 hardware-identity level.

- NRC construction records identify **`SV3-RNS-PY-C01` as P19, `RCS to RHR Pump Out`** (`SRC-0730`).
- This is the **common RNS suction penetration** after the two V001/V002 parallel RCS-pressure-boundary branches recombine, not a dedicated B-train or V002B-only penetration (`SRC-0733`).
- The public 2017 construction inventory identifies installation work package **`SV3-RNS-MLW-860363`**, *ASME Section III - Installation of Containment Vessel Penetration SV3-RNS-PY-C01 (P19)* (`SRC-0732`).
- The three named P19 pressure-boundary welds are:
  - `SV3-RNS-PY-C01-1` — sleeve extension to penetration sleeve;
  - `SV3-RNS-PY-C01-2` — guard pipe to penetration sleeve;
  - `SV3-RNS-PY-C01-3` — flued head to guard pipe (`SRC-0730`).
- NRC identifies final radiography review for weld `-1` on the inside-containment side and `-2` on the outside-containment side, and separately lists the P19 RT report family including `V-16-RT-301-0242`, `-0246`, and `-0254` (`SRC-0730`, `SRC-0731`).
- Controlled geometry routes include `SV3-RNS-MLK-881065` P19 weld map, `SV3-ML10-V6-003` P19 flued-head detail, `SV3-1100-P0-906` mechanical-penetration details, `SV3-MV50-V2-062` sleeve extensions, `SV3-MV50-V1-015` penetration list, `SV3-MV50-V1-016` penetration location, and the sleeve/ring drawings (`SRC-0731`, `SRC-0734`, `SRC-0715`).

Still unresolved are the public numeric P19 shell azimuth/elevation, sleeve/guard/flued-head dimensions and material heats, process-pipe line number through the assembly, exact common-header spool geometry, supports/restraints, and final installation/turnover details. NRC records establish that location/as-built verification occurred, but the public inspection prose does not print the required coordinates.

## B-side V001B/V002B relationship to P19

The design basis supports a precise functional sequence while leaving local geometry open:

- `RNS-PL-V001B` is the inner series hot-leg suction RCS-pressure-boundary MOV.
- `RNS-PL-V002B` is the outer B-side series hot-leg suction MOV, ASME Class 1 / IST Category A, and the containment-isolation member of its two-valve branch (`SRC-0702`).
- Westinghouse describes the V002 member as the valve in each pair closest to the containment penetration (`SRC-0714`).
- U.S. NRC design text establishes that the two parallel V001/V002 paths then connect to a **common suction header before the containment crossing** (`SRC-0733`).
- Therefore `V002B -> P19` is not a direct exclusive B-train pipe segment. The unresolved B-side geometry is `V002B outlet -> B-branch spool/junction -> common suction header -> P19`.

The exact V002B outlet line number, branch-combining fitting, header line number, spool lengths, fittings, welds, supports and distance to P19 remain open. PLW-015/L005 remains a candidate drawing route rather than proof of the V002B outlet line.

## Relief systems — thermal relief is not LTOP

Two fundamentally different relief functions remain separate graph families.

### RCS pressure-boundary thermal relief

`RNS-PL-V003B` is the B-side thermal-relief check valve and is directly present in the Unit-3 RNS EQ population; `RNS-PL-V004B` is the separately identified thermal-relief isolation valve. The exact branch takeoff, local line number, restrictor/orifice hardware, sequence/spacing and downstream routing remain to be recovered (`SRC-0701`, `SRC-0704`). This branch is **not** part of the V020/V021 LTOP relief subsystem.

### Final Vogtle LTOP configuration — V020 + V021

The original AP1000/single-relief picture is **not the final Vogtle configuration**. Unit-3 Amendment 104, issued December 20, 2017 under LAR 17-022, added `RNS-PL-V020` in parallel with existing `RNS-PL-V021`, with associated piping changes (`SRC-0735`). The post-amendment UFSAR lists both tags as `RNS Hot Leg Suction Relief`, and current Unit-3 licensing correspondence describes the applicable TS 3.4.14 condition as requiring **two RNS suction relief valves operable** unless the alternative depressurized-RCS/vent condition is met (`SRC-0737`, `SRC-0738`).

The two valves intentionally have different hydraulic roles:

- **`RNS-PL-V020`** — added **1-inch** relief valve. Licensing evidence states it has lower flow capacity and a lower setpoint than V021 and was added to reduce chatter of the larger valve during low-flow LTOP scenarios (`SRC-0736`). Its exact vendor/commodity family, datasheet, model, serial, numeric setpoint, capacity and internal construction remain unresolved. It must **not** inherit V021's PV16/Z0D-105 identity.
- **`RNS-PL-V021`** — existing **3-inch** relief valve retained in the final dual-relief configuration. NRC directly maps it to `APP-PV16-Z0D-105` and the associated QME-1/PV16 qualification family (`SRC-0716`, `SRC-0739`). Exact installed model/serial and post-amendment numeric setpoint/capacity remain open.

The original `APP-RNS-M3C-002` single-relief basis exposed 850-gpm minimum capacity, 500-psig nominal set pressure and 550-psig full-open pressure at 10% accumulation. Those values are now carried as **pre-amendment/configuration-history values**, not final Unit-3 V020/V021 operating values. NRC later identifies `LDCR-2017-114`, *Change to RNS Suction Relief Valve Design Parameters*, which must be recovered before any final numerical LTOP model is frozen (`SRC-0717`, `SRC-0740`).

Unit-3 ITAAC Index 372 (`ML18120A270`) and Index 373 (`ML18117A424`) closed the LTOP capacity and set-pressure criteria after Amendment 104. Those final completion packages are therefore the preferred route to actual installed performance. Public status indexes confirm the completion records but do not expose the underlying measured V020/V021 values.

The final outlet routing also remains open. Pre-amendment Chapter-5 text conflicts between an IRWST destination and a containment-sump destination, and Amendment 104 added additional relief piping. A post-amendment Unit-3 P&ID/isometric must establish whether V020/V021 outlets remain separate or combine and where they terminate.

## Outside-containment common suction header

U.S. NRC design text states that once the common RNS suction header is outside containment it contains a **single normally closed motor-operated isolation valve**; downstream of that valve the header branches to the two RNS pumps, with a normally open manual isolation valve upstream of each pump (`SRC-0733`).

The Vogtle UFSAR identifies `RNS-PL-V022` as the **RNS Suction Header Containment Isolation** valve and `RNS-PL-V005A/B` as the pump suction isolation valves (`SRC-0704`). V022 is therefore the leading tag bridge for the single common-header MOV, but the exact physical sequence/line assignment remains subject to current P&ID closure. V005B remains a known B-pump suction-isolation object whose exact line segment still requires the site drawing.

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

1. `LDCR-2017-114` plus the post-Amendment-104 revision of `APP-RNS-M3C-002`, to close V020/V021 design setpoints, capacities and current LTOP analytical assumptions.
2. Unit-3 ITAAC ICNs `ML18120A270` / `ML18117A424` and their referenced NV-1/code-data/test records, to recover final installed relief capacity and set-pressure evidence.
3. The exact **V020 datasheet/vendor/QME-1/code-data package**. No tag-specific public data-sheet bridge has yet been recovered; V021's PV16 Z0D-105 must not be reused.
4. Post-LAR `SV3-RNS-M6-003` / current RNS P&ID plus affected isometrics, to place V020/V021 inlet and outlet branches and resolve their final destination(s).
5. `SV3-MV50-V1-016` + `SV3-MV50-V1-015` + `SV3-RNS-MLK-881065` + `SV3-ML10-V6-003`, specifically querying P19, to close its azimuth/elevation, hardware dimensions and weld locations.
6. `SV3-RNS-MLW-860363`, to close P19 material traceability, installation details, NDE bridges and final turnover.
7. Current Unit-3 RNS P&ID / `SV3-RNS-M6K-FA201` / `SV3-RNS-M6X-004`, to identify the V002A/B branch-combining point, common-header line number, V022 physical placement and downstream pump split.
8. PLW-015, to resolve L005/L029/L080 geometry and determine whether it contains the V002/common-header region.
9. Final RNS Index-361 EQRR/PCD and V002B row, followed by the V002B setup VDR, V2 assembly drawing and diagnostic package.
10. MP-01B post-disassembly reassembly/alignment/turnover records, V033B instrument endpoint, V036B drain destination and remaining electrical/control closure.

Until those records are recovered, unresolved interfaces remain explicit graph boundaries rather than being filled by symmetry, line-number patterns or generic-family assumptions.
