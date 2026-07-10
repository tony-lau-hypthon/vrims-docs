# Repository Design Principles

## 1. Repository First

The repository is the canonical current state. AI memory, chat history, and release packages are not authoritative.

## 2. Current State over Release Replay

Consumers should read current canonical files instead of replaying all historical releases.

## 3. Git Preserves History

The repository stores current knowledge. Git stores evolution and historical versions.

## 4. Modules Own Domain-Specific Knowledge

Business-domain rules belong under `modules/`.

## 5. Core Owns Reusable Capabilities

Reusable lifecycle and capability rules belong under `core/`.

## 6. Shared Owns Cross-Cutting Capabilities

Notifications, shared controls, and reusable cross-domain concerns belong under `shared/`.

## 7. Governance Owns Operating Rules

Repository rules, evidence hierarchy, integrity, traceability, and release governance belong under `governance/` and `standards/`.

## 8. Update Before Create

Existing canonical files should be updated before new parallel documents are created.

## 9. Evidence Before Inference

Inference may create an assumption or open question, but not a confirmed rule.

## 10. No Silent Overwrite

Every supersession must preserve the previous knowledge, reason, source, and impact through Git history and repository notes where necessary.

## 11. Release as Delta

A release contains only the repository changes required to move from one canonical state to the next.

## 12. Healthier After Every Release

Every release should improve consistency, traceability, clarity, coverage, or maintainability.
