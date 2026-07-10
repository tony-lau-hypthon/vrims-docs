# GLM Prompt — Generate VRC Review Documents

Use the current canonical `vrims-docs` repository after Release-016R Pack 3 has been merged and validated.

## Required Outputs

1. `deliverables/VRIMS-WC-001-VRC-Executive-Review-v1.2R.md`
2. `deliverables/VRIMS-WC-001-VRC-Business-User-Review-v1.1R.md`

Rendering to DOCX may be performed only after the Markdown outputs pass the Pack 4 checklist.

## Source Priority

1. Explicit decision evidence and user-confirmed decisions represented in canonical files
2. Business rule registers and module canonical documents
3. Review-readiness and open-item records
4. Existing generated deliverables, used only as a presentation reference

Never use an older generated deliverable to override current canonical content.

## Mandatory Content Controls

- State the generation baseline: Release-016R Pack 3.
- Reflect Customer Portal as Web App with PWA capability.
- Reflect three portal user groups: VR Resident, VRC Member and VC Member.
- Reflect VRC Member online treatment booking as current supported scope.
- State that a 45-minute treatment blocks two consecutive 30-minute slots and the remaining 15 minutes is unavailable.
- Preserve the boundary that online booking does not establish online cancellation or rescheduling.
- Keep VR Resident care packages separate from VRC membership and VRC commercial treatment.
- Preserve all pending business validation and Functional Design items as unresolved.

## Required Knowledge Sections

Both documents must visibly separate:

- Confirmed Facts
- Assumptions
- Conflicts
- Open Questions
- Decisions
- Related Modules

Where a section has no content, write `None identified in the canonical baseline` rather than omitting it.

## Prohibited Behaviour

- Do not invent missing rules, data fields, workflows, approvals, calculations or integrations.
- Do not silently resolve contradictions.
- Do not change business rule IDs or classifications.
- Do not describe review output as a Functional or Technical Specification.
- Do not claim business sign-off.

## Completion Report

After generating the documents, provide:

- files created or changed;
- source files used;
- conflicts detected;
- open questions retained;
- checklist result;
- confirmation that no business rule was added or reclassified.
