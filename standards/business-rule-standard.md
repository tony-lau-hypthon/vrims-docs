# Business Rule Standard

## Business Rule ID Format

```text
BR-<CAPABILITY>-NNN
```

Example:

```text
BR-BKG-001
```

## Business Rule Template

```markdown
## BR-BKG-001 — Rule Title

**Status:** Confirmed / Partial / TBD  
**Capability:** Booking  
**Applies To:** VRC / Resident / VC / All  
**Description:**  
Business rule statement.

**Rationale:**  
Why this rule exists.

**Evidence:**  
Source evidence.

**Impacted Areas:**  
Related modules and capabilities.

**Acceptance Reference:**  
Related acceptance criteria.
```

## Rule Writing Principles

- Write business rules, not UI behaviour.
- Do not include technical implementation unless required.
- Do not mark assumptions as confirmed.
- Every confirmed rule must have evidence.
