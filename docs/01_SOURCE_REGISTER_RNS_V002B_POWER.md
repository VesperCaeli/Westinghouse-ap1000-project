# Public Source Register Supplement — RNS V002B Class-1E DC Power

This supplement shares the global controlled `SRC-*` namespace with the other `01_SOURCE_REGISTER*.md` files.

| Source ID | Authority | Configuration | Document | Locator / accession | Use |
|---|---|---|---|---|---|
| SRC-0467 | A | AP1000-DESIGN-CHANGE-TO-R19 | U.S. NRC, NUREG-1793 Supplement 2, *Final Safety Evaluation Report Related to Certification of the AP1000 Standard Design* | September 2011; Volume 2, Chapter 17 §17.6.2, p.17-9; NRC NUREG-1793 Supplement 2 publication page / ADAMS package ML112061231 | NRC explicitly records that the nominal voltage of the AP1000 24-hour batteries was changed from **125 Vdc to 250 Vdc**, states that the staff review of the modification is in §8.3.2 of the safety evaluation, and notes that the applicant subsequently incorporated the change into the DCD. This is the controlling configuration-history bridge explaining why older AP1000/RNS material can mention 125-Vdc safety-related MOV supply while Revision 19 and Vogtle Unit 3 use the Class-1E 250-Vdc IDS architecture. It resolves the current V002B **source/distribution nominal voltage family** as 250 Vdc when combined with SRC-0449 and SRC-0452, but does not establish the V002B motor nameplate voltage, exact terminal voltage under load, MCC cubicle, fuse size, or actuator model. |
