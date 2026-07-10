# Knowledge Integrity Checklist

Use this checklist before merging a repository delta.

## Structure

- [ ] Existing canonical files were updated before creating parallel documents.
- [ ] Module, core, shared, governance, and standards boundaries are respected.
- [ ] File names and IDs follow repository conventions.
- [ ] New files are linked from relevant navigation documents.

## Classification

- [ ] Confirmed facts have supporting evidence.
- [ ] Tony-confirmed items are clearly labelled.
- [ ] Design assumptions remain assumptions.
- [ ] Pending VR decisions remain open.
- [ ] Functional-design items are not mistaken for business decisions.

## Duplication

- [ ] No duplicated rule exists in multiple canonical locations without ownership rationale.
- [ ] Repeated summaries point to a canonical source.
- [ ] Old parallel documents are deprecated or merged.

## Conflict

- [ ] Conflicting knowledge is identified.
- [ ] Existing and new knowledge are both preserved for review.
- [ ] Recommended resolution and impact are documented.
- [ ] No conflict is silently overwritten.

## Traceability

- [ ] Important rules identify source evidence.
- [ ] Superseded rules remain discoverable.
- [ ] Related modules and capabilities are linked.
- [ ] Open questions are traceable to affected knowledge.

## Freshness

- [ ] Deprecated information is labelled.
- [ ] Current-state documents represent the latest verified understanding.
- [ ] Release notes and changelog describe the delta accurately.

## Outcome

- [ ] PASS
- [ ] PASS WITH MANUAL REVIEW
- [ ] FAIL
