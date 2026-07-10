# Decision Hierarchy

1. Decision Evidence
2. Business Confirmation
3. Tony Confirmation
4. Approved Master Data
5. Functional Design
6. Raw Requirements
7. Supporting Evidence
8. Inference

---

## Conflict Review (Release-015R Merge)

This document defines the evidence/decision priority hierarchy. It interacts with two existing standards that have a **pre-existing inconsistency** in decision ID format.

### 1. Hierarchy alignment with writing-style-guide.md

| | |
|---|---|
| **Existing knowledge** | `standards/writing-style-guide.md` defines confidence levels: Confirmed / Partial / Assumption / TBD. |
| **New knowledge** | This document defines an 8-level decision hierarchy: Decision Evidence → Business Confirmation → Tony Confirmation → Approved Master Data → Functional Design → Raw Requirements → Supporting Evidence → Inference. |
| **Recommended resolution** | **Complementary.** The hierarchy here is more granular and maps to the knowledge classifications (Confirmed Fact, Tony Confirmed, Design Assumption, Pending VR, Functional Design Required). Both are retained. |
| **Impact** | None — the hierarchy enriches, not contradicts. |

### 2. Pre-existing decision ID format inconsistency (flagged, not resolved by this release)

| | |
|---|---|
| **Existing knowledge** | `standards/decision-standard.md` uses `D-NNNN` format (e.g. `D-0001`). `governance/naming-standard.md` uses `D-<CAP>-001` format (e.g. `D-BKG-001`). These are inconsistent. |
| **New knowledge** | This document does not address ID format — it only defines the evidence hierarchy. |
| **Recommended resolution** | **Manual review required.** The ID format inconsistency between `standards/decision-standard.md` (`D-0001`) and `governance/naming-standard.md` (`D-<CAP>-001`) predates this release and is not resolved here. The repository currently uses `D-NNNN` in practice (Booking decisions D-0001..D-0006, Package decisions D-PKG-001..007, etc.). Recommend standardising on the capability-prefixed format (`D-<CAP>-NNN`) in a future governance pack to align with BR/AC/BS naming. |
| **Impact** | Low — current documents use `D-NNNN` or `D-<CAP>-NNN` consistently within each capability. The inconsistency is between the two standard documents, not within the business content. |

