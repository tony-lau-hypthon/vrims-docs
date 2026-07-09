# GLM Import Instructions

## Goal

Apply this release package into the `vrims-docs` repository and push to GitHub.

## Steps

1. Clone or open the local `vrims-docs` repository.
2. Extract this zip into a temporary folder.
3. Copy the `core/booking/*.md` files into the repo root, preserving paths.
4. Review changed files.
5. Commit using the content of `commit-message.txt`.

## Suggested Commands

```bash
cd /path/to/vrims-docs
unzip /path/to/release-002-core-booking.zip -d /tmp/release-002
rsync -av /tmp/release-002/core/ ./core/
git status
git add core/booking CHANGELOG.md
git commit -F /tmp/release-002/commit-message.txt
git push
```

## Notes

- Do not overwrite `standards/` unless explicitly included in a future release.
- This release does not include Word/PDF generation.
- Markdown remains the source of truth.
