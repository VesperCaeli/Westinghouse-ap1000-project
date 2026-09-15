# Public Source Register

This file controls the source universe for the reconstruction. Add individual chapter/section/document entries as research proceeds.

| Source ID | Authority | Configuration | Document | Locator / accession | Use |
|---|---|---|---|---|---|
| SRC-0001 | A | AP1000-DCD-R19-GENERIC | NRC AP1000 issued design certification page | https://www.nrc.gov/reactors/new-reactors/large-lwr/design-cert/ap1000 | Controlling NRC status page; identifies DCD Revision 19 and current Revision 20 renewal/amendment review |
| SRC-0002 | A | AP1000-DCD-R19-GENERIC | AP1000 Design Control Document, Revision 19 | ADAMS ML11171A500; linked from NRC AP1000 design certification page | Primary generic AP1000 design basis |
| SRC-0003 | A | AP1000-DCD-R19-GENERIC | NUREG-1793, Supplement 2, Final Safety Evaluation Report Related to Certification of the AP1000 Standard Design | https://www.nrc.gov/reading-rm/doc-collections/nuregs/staff/sr1793/s2/index | NRC technical evaluation of the certified Revision 19 design |
| SRC-0004 | A | VOGTLE-3-CURRENT-PUBLIC | Vogtle Electric Generating Plant Unit 3, Most Recent UFSAR Submittal | NRC Unit 3 page links current UFSAR; current link observed as ADAMS ML25181A777 | Plant-specific current public licensing/as-built basis |
| SRC-0005 | A | VOGTLE-3/VOGTLE-4 | NUREG-2124, Final Safety Evaluation Report Related to the Combined Licenses for Vogtle Units 3 and 4 | https://www.nrc.gov/reading-rm/doc-collections/nuregs/staff/sr2124/index | Plant-specific NRC evaluation and departures/interfaces |
| SRC-0006 | A | AP1000-GENERIC | NUREG-2103, Knowledge and Abilities Catalog for Nuclear Power Plant Operators: Westinghouse AP1000 PWRs | https://www.nrc.gov/reading-rm/doc-collections/nuregs/staff/sr2103/index | System/component taxonomy and operator-facing functional cross-check |
| SRC-0007 | A | AP1000/VOGTLE | NUREG-2194, Revision 1, Standard Technical Specifications, Westinghouse AP1000 Plants | https://www.nrc.gov/reading-rm/doc-collections/nuregs/staff/sr2194/r1/v1/index | Operability, surveillance, system boundary, instrumentation and limiting-condition cross-check |
| SRC-0008 | A | VOGTLE-3 | NRC Vogtle Unit 3 plant page | https://www.nrc.gov/reactors/new-reactors/large-lwr/col-holder/vog3 | Current licensing links, inspection history, ITAAC and status |
| SRC-0009 | A | VOGTLE-3/VOGTLE-4 | NRC issued combined-license application page | https://www.nrc.gov/reactors/new-reactors/large-lwr/col/vogtle | FSAR history, incorporated DCD basis, public/withheld document boundary |
| SRC-0010 | A | AP1000-DCD-R20-PENDING | Westinghouse AP1000 design certification renewal/amendment application | linked from NRC AP1000 design certification page, submitted 2026-03-27 | Track proposed Revision 20 changes separately; do not merge into R19 baseline until dispositioned |
| SRC-0011 | A | AP1000-GENERIC | NUREG-1793 Initial Report, Chapter 5, Reactor Coolant System and Connected Systems | https://www.nrc.gov/reading-rm/doc-collections/nuregs/staff/sr1793/initial/chapter5.pdf | Detailed NRC evaluation of RCS topology, components, piping, pressure relief, connected systems and DCD section cross-references |
| SRC-0012 | A | AP1000-GENERIC | NUREG-1793 Initial Report, Chapter 3, Design of Structures, Components, Equipment, and Systems | https://www.nrc.gov/reading-rm/doc-collections/nuregs/staff/sr1793/initial/chapter3.pdf | Mechanical/structural qualification, supports, relief/ADS-valve module and loading cross-checks |
| SRC-0013 | A | AP1000-GENERIC | NUREG-1793 Initial Report, Chapter 8, Electric Power Systems | https://www.nrc.gov/sites/default/files/doc_library/cdn/legacy/reading-rm/doc-collections/nuregs/staff/sr1793/initial/chapter8.pdf | Offsite power, onsite AC, standby diesel generators, DC/UPS, transformers, switchgear, buses, distribution, station-blackout design and electrical interfaces |
| SRC-0014 | A | AP1000-GENERIC | NUREG-1793 Initial Report, Chapter 9, Auxiliary Systems | https://www.nrc.gov/sites/default/files/doc_library/cdn/legacy/reading-rm/doc-collections/nuregs/staff/sr1793/initial/chapter9.pdf | Water systems, component/service cooling, demineralized-water treatment/storage, potable/sanitary/wastewater systems, chilled/hot water, fuel handling, ventilation and other plant auxiliaries |
| SRC-0015 | A | AP1000-GENERIC | NUREG-1793 Initial Report, Chapter 10, Steam and Power Conversion System | https://www.nrc.gov/reading-rm/doc-collections/nuregs/staff/sr1793/initial/chapter10.pdf | Main steam/turbine/condenser/feedwater/condensate/circulating-water/heat-rejection systems and balance-of-plant power conversion |

## Authority codes

- `A` - primary regulator/licensee/vendor public licensing basis or regulator inspection evidence.
- `B` - public standards, vendor technical reports, or other authoritative engineering references.
- `C` - peer-reviewed papers, theses, conference proceedings, or credible technical publications.
- `D` - secondary/discovery source; cannot establish an AP1000 fact by itself.

## Research rule

Each factual field in the master registers must cite one or more `Source ID` values plus a precise locator such as chapter, section, figure, table, drawing number, page, ITAAC number, inspection report section, or public vendor-document identifier.

Do not cite only a search-result snippet when the underlying primary document is available.

## Whole-station source rule

The research boundary is the entire generating station and every public-design-basis interface needed to make the unit physically and functionally complete. Chapter 8 electrical systems, Chapter 9 auxiliary systems, and Chapter 10 power-conversion/heat-rejection systems are coequal with the nuclear steam-supply systems; they are not optional balance-of-plant appendices.

Site-specific systems and interfaces that are intentionally left to a COL holder by the generic DCD must be resolved from the selected plant-specific baseline (initially Vogtle Unit 3 current public licensing/as-built evidence) rather than replaced by generic assumptions.

## Known public-record limitation

The Vogtle COL application page explicitly identifies security-plan/safeguards portions as withheld from public availability. Those materials are outside this project's source universe and must not be reconstructed by inference.
