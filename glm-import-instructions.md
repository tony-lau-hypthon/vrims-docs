# GLM Import Instructions — Release-016R Pack 3

## Expected Baseline

The target repository must already include Release-016R Pack 1 and Pack 2. Expected latest Pack 2 commit: `617b476`.

## Required Actions

1. Confirm the target repository and inspect `git status`.
2. Do not overwrite unrelated uncommitted work.
3. Review every supplied full-file replacement against the current canonical file.
4. Merge the supplied files into the same repository-relative paths.
5. Preserve any newer, evidence-backed changes that do not conflict with Pack 2.
6. Do not create parallel VRC documents.
7. Run `review/release-016R-pack3-review-checklist.md`.
8. Review the final diff for business-rule regression.
9. Commit as a documentation-only release.
10. Stop after commit; do not generate or modify application code.

## Required Regression Protections

- Customer Portal remains Web App + PWA.
- Supported portal groups remain VR Resident, VRC Member and VC Member.
- VRC Member treatment booking remains current scope.
- A 45-minute treatment continues to reserve two 30-minute slots.
- The unused 15 minutes remains unavailable.
- Online booking must not be expanded into online cancellation or rescheduling.
- VRC packages must not be merged with VR Resident care packages.
- Open questions must remain unresolved until evidence is supplied.

## Do Not

- Introduce new business rules.
- Write Functional Design or Technical Specification content.
- Infer UI, API, database, Odoo or Firebase implementation.
- Promote assumptions or open questions to confirmed facts.
- Restore obsolete future membership, future online booking or future Customer Portal questions.

## Suggested Commit Message

`docs(vrc): close review readiness and traceability (Release-016R Pack3)`

## Post-merge Output

After the Pack 3 checklist passes and the merge is committed, GLM may generate the VRC Executive Review or Business User Review from the canonical repository. Generated outputs must keep open questions and design limitations visible.
