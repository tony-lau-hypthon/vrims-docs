# GLM Prompt — Implement Repository Delta

You are maintaining the existing VRIMS BA documentation repository.

The attached package is a repository delta. The current GitHub repository is the canonical current state.

## Tasks

1. Review the delta against the current repository.
2. Merge into existing canonical files where possible.
3. Preserve:
   - repository architecture
   - document IDs
   - front matter
   - naming conventions
   - cross references
   - writing style
4. Never silently overwrite existing knowledge.
5. If conflicts exist, report:
   - existing knowledge
   - incoming knowledge
   - recommended resolution
   - impact
6. Preserve classifications:
   - Confirmed Fact
   - Tony Confirmed
   - Design Assumption
   - Pending VR
   - Functional Design Required
7. Update root navigation and release files only where required.
8. Run the knowledge integrity checklist.
9. Commit the repository changes.
10. Stop after commit. Do not generate downstream outputs.

## Required Response

Return only:

1. Merge Summary
2. Added Files
3. Updated Files
4. Conflicts
5. Manual Review Required
6. Integrity Check Result
7. Commit Reference
