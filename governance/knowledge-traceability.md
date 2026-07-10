# Knowledge Traceability

## Objective

Ensure important business knowledge can be traced from source evidence through design and implementation.

## Traceability Chain

```text
Evidence
→ Decision / Clarification
→ Repository Knowledge Item
→ Executive Review
→ Functional Design
→ GitHub Issue
→ Implementation
→ Test Evidence
```

## Minimum Traceability Fields

Important knowledge should identify, where available:

- Knowledge ID
- Classification
- Source document or session
- Decision owner
- Decision date
- Related module
- Related capability
- Supersedes / superseded by
- Open question reference
- Functional-design reference
- GitHub issue reference

## Traceability Rules

1. A confirmed rule should have identifiable supporting evidence.
2. Tony-confirmed knowledge must remain labelled until business confirmation is available.
3. Design assumptions must not be presented as confirmed requirements.
4. Superseded knowledge must retain a discoverable history.
5. Cross-module impacts must be recorded.
6. Missing traceability must be reported as an integrity issue.

## Traceability Quality Levels

- **Complete** — source, classification, ownership, and downstream links available.
- **Partial** — source or downstream links incomplete.
- **Untraceable** — no reliable source or ownership reference.

---

## Conflict Review (Release-015R Pack 4 Merge)

This document defines the knowledge traceability framework. It overlaps thematically with existing traceability documents.

| | |
|---|---|
| **Existing knowledge** | `governance/cross-capability-traceability.md` — maps inter-capability dependencies (Assessment → Booking → Package, etc.). `standards/traceability-standard.md` — defines the evidence-to-acceptance-criteria chain (Evidence → Decision → Rule → Scenario → Acceptance). |
| **New knowledge** | This document defines the full traceability chain from Evidence through to Implementation + Test Evidence, minimum traceability fields (12 fields), 6 traceability rules, and 3 quality levels (Complete / Partial / Untraceable). |
| **Recommended resolution** | **Complementary — different scopes.** `cross-capability-traceability.md` maps which capabilities depend on which. `traceability-standard.md` defines the BA-level evidence chain. This document extends traceability end-to-end (through Functional Design → GitHub Issue → Implementation → Test) and adds the field/rule/quality-level framework. All three retained. |
| **Impact** | None — consistent and non-contradictory. This document is the most comprehensive of the three. |

