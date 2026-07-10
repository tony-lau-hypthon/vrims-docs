# GLM Import Instructions — Release-016R Pack 4

## Preconditions

1. Finish and commit Release-016R Pack 3.
2. Run `review/release-016R-pack3-review-checklist.md`.
3. Start from a clean working tree.

## Apply

Copy all Pack 4 files into the repository root while preserving paths. Review the diff before committing.

Suggested commit message:

```text
docs(vrc): add VRC review generation handoff (Release-016R Pack4)
```

## Validate

Run `review/release-016R-pack4-review-checklist.md`. Then use `templates/glm-vrc-review-generation-prompt.md` to regenerate the two review documents.

Do not merge generated review wording back into canonical business-rule files. Any newly detected conflict or missing information must be recorded as a separate knowledge delta.
