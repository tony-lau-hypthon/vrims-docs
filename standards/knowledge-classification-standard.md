# Knowledge Classification Standard

Every significant knowledge item shall be classified as one of:

- Confirmed Fact
- Tony Confirmed
- Design Assumption
- Pending VR
- Functional Design Required

Do not change classification without supporting evidence.

---

## Conflict Review (Release-015R Pack 3 Merge)

This standard codifies the 5 knowledge classifications as binding. It overlaps with existing documents.

| | |
|---|---|
| **Existing knowledge** | `standards/metadata-standard.md` defines a `status` field with values: Draft / Internal Review / Business Review / VR Review / Approved / Baseline / Superseded. `standards/writing-style-guide.md` defines confidence levels: Confirmed / Partial / Assumption / TBD. `standards/review-workflow.md` defines a review lifecycle. |
| **New knowledge** | This document defines 5 knowledge classifications: Confirmed Fact, Tony Confirmed, Design Assumption, Pending VR, Functional Design Required — used throughout business rule registers and scenario specifications. |
| **Recommended resolution** | **Complementary, different axes.** The metadata `status` field tracks document lifecycle stage (Draft → Approved). Knowledge classification tracks evidence strength of individual rules/facts. Both are needed. The writing-style-guide confidence levels (Confirmed/Partial/Assumption/TBD) are a lighter-weight version; the 5-class system here is the authoritative taxonomy used in business content. |
| **Impact** | None — no contradiction. Recommend future reconciliation of writing-style-guide confidence levels to align with these 5 classifications. |

