## Release-016R Pack 3 — VRC Review Readiness and Traceability Closure

### Added
- VRC Pack 3 release summary and merge checklist
- Explicit separation of Confirmed Facts, Assumptions, Conflicts, Open Questions, Decisions and Related Modules
- Business-review readiness gate after Pack 2 regression clarification

### Changed
- Wellness Centre review readiness aligned with current portal and booking scope
- Wellness Centre open items reorganised for regression protection and review traceability
- Repository navigation and GLM merge instructions advanced to Pack 3

### Business Impact
- No new business behaviour or business rule IDs
- VRC domain is ready for controlled Executive and Business User Review generation

---

## Release-016R Pack 2 — VRC Business Regression

Added / Updated:
- Current Customer Portal Web App + PWA scope
- Portal user groups: VR Resident, VRC Member and VC Member
- VRC Member treatment booking through Customer Portal
- 30-minute booking-slot allocation clarification
- 45-minute treatment two-slot reservation rule
- Resolved-item regression for membership, portal booking and 45-minute scheduling
- Validated classification in affected VRC documents
- New rules BR-BKG-017 (VRC Member portal booking) and BR-BKG-018 (portal user groups)
- Reclassification: BR-BKG-003, BR-BKG-006, BR-BKG-014 → Validated

Business impact:
- Clarifies current VRC portal and booking scope.
- No technical design introduced.
- Online booking does NOT imply online cancellation or rescheduling.

## Release-016R Pack 1
- Introduce Knowledge Status model (Confirmed, Validated, Assumption, Pending Validation, Deprecated).
- Introduce Source Type classification.
- Introduce Validation Status classification.
- Added to `standards/knowledge-classification-standard.md` alongside existing 5-class system.
- No business rule changes.

## Release-015R — BA Brain Governance Foundation (Finalised)

Consolidated governance framework across 5 packs:
- Repository constitution, AI operating rules, decision hierarchy, bootstrap governance (Pack 1)
- Knowledge integrity, repository health, lifecycle, release governance (Pack 2)
- Evidence priority, knowledge classification, maintenance, delta, authoring standards (Pack 3)
- Domain maturity model, traceability, design principles, roadmap, QA checklists (Pack 4)
- Final integrity gate, GLM prompt templates, canonical release summary, navigation updates (Pack 5)

Root navigation now exposes governance, standards, review, templates, and release summary sections.

Business knowledge impact: None.

---

## Release-015R Pack 4
- Domain Maturity Model, Knowledge Traceability, Repository Design Principles, Repository Roadmap added.
- Knowledge Integrity Checklist and Release-015R Review Checklist added.
- INDEX.md updated with new governance and review documents.

## Release-015R Pack 3
- Evidence Priority, Knowledge Classification, Repository Maintenance, Repository Delta, Document Authoring standards added.
- Conflict Review sections added to 4 standards with thematic overlap.
- INDEX.md standards section updated.

## Release-015R Pack 2
- Knowledge Integrity, Repository Health, Repository Lifecycle, Release Governance added.
- INDEX.md governance section updated.

## Release-015R Pack 1
- Governance Pack 1 added (Constitution, AI Guidelines, AI Startup Sequence, Bootstrap Governance, Decision Hierarchy).
- Conflict Review sections added to `governance/ai-guidelines.md` and `governance/decision-hierarchy.md`.
- INDEX.md governance section updated to register new documents.
- Existing business modules unaffected.

---

## Release-014R

Added:
- VRC Domain Foundation consolidation under `modules/wellness-centre/`
- Wellness Centre product and service catalogue
- VRC package and pricing foundation
- Registration and assessment foundation
- VRC-specific booking, billing and notification clarifications
- Release-014R review checklist

Updated:
- Wellness Centre business scope
- Wellness Centre customer journey
- Wellness Centre business rules
- Wellness Centre open items
- Wellness Centre capability reference map
- Booking business-rule catalogue
- Package open items and lifecycle rules
- Billing business-rule register
- Notification event library and open items
- Master index

Clarified:
- VRC therapy packages are separate from the nine standard and three special VR Resident care plans.
- QF Pay is not confirmed as the final payment solution.
- VR Finance currently prefers eftPay, subject to technical confirmation.
- Therapist selection and roster allocation are operationally managed.
- Supporting reports and screenshots are deferred from the VRC foundation release.


## Release-016R Pack 4 — VRC Business Review Generation Handoff
- Added controlled GLM generation prompt and evidence coverage matrix.
- Added generation acceptance gate for Executive and Business User reviews.
- Added no-promotion and no-silent-resolution controls.
- No business requirement or rule classification changed.
