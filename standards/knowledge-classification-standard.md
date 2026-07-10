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

---

## Knowledge Status Model (Release-016R Pack 1)

The following Knowledge Status model is introduced as a supplementary governance classification layer. It coexists with the existing 5-class knowledge classification above — it does not replace it.

### Knowledge Status Values

| Status | Meaning |
|---|---|
| **Confirmed** | Knowledge is confirmed and locked |
| **Validated** | Knowledge has been reviewed and validated but may await final confirmation |
| **Assumption** | Knowledge is an assumption suitable for drafting but not yet confirmed |
| **Pending Validation** | Knowledge requires validation before it can be promoted |
| **Deprecated** | Knowledge is superseded or no longer current; retained for traceability |

### Relationship to Existing Classifications

The existing 5-class system (Confirmed Fact, Tony Confirmed, Design Assumption, Pending VR, Functional Design Required) remains the **authoritative classification used in business content**. The Knowledge Status model above provides a complementary lifecycle view:

| Existing Classification | Corresponds to Knowledge Status |
|---|---|
| Confirmed Fact | Confirmed |
| Tony Confirmed | Validated |
| Design Assumption | Assumption |
| Pending VR | Pending Validation |
| Functional Design Required | Pending Validation |
| (superseded knowledge) | Deprecated |

Do not change existing classifications without supporting evidence.

---

## Source Type (Release-016R Pack 1)

Every significant knowledge item should identify its source type to support traceability and evidence assessment.

| Source Type | Description |
|---|---|
| **Workshop** | Knowledge captured during a workshop or working session |
| **Email** | Knowledge captured from email correspondence |
| **Document** | Knowledge extracted from a provided document or spreadsheet |
| **Interview** | Knowledge captured from a one-to-one interview or clarification |
| **Inference** | Knowledge derived by analysis (must be classified as Assumption unless validated) |
| **Master Data** | Knowledge from approved master data (price lists, product catalogues) |

---

## Validation Status (Release-016R Pack 1)

Validation Status tracks whether a knowledge item has been through a validation process.

| Validation Status | Meaning |
|---|---|
| **Not Validated** | No validation has been performed |
| **BA Validated** | Business Analyst has reviewed and accepted |
| **Tony Validated** | Tony has reviewed and accepted |
| **Business Validated** | VR business user has confirmed |
| **Failed Validation** | Validation was attempted but the item was rejected or needs correction |


