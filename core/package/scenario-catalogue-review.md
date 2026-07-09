---
id: VRIMS-PKG-SCENARIO-CATALOGUE-R
title: Package Scenario Catalogue Review
type: Scenario Catalogue
capability: Package
version: 1.0R
status: Business Review Draft
---

# Package Scenario Catalogue Review

| Scenario ID | Scenario | Stage | Status |
|---|---|---|---|
| PS-PKG-001 | Validate Active Package | Validation | Business Review Draft |
| PS-PKG-002 | Validate Treatment Eligibility | Validation | Business Review Draft |
| PS-PKG-003 | Validate Package Balance | Validation | Business Review Draft |
| PS-PKG-004 | Handle Multiple Packages | Validation | Business Review Draft |
| PS-PKG-005 | Redeem Package After Completed Treatment | Redemption | Business Review Draft |
| PS-PKG-006 | Handle No-show Without Deduction | Redemption | Business Review Draft |
| PS-PKG-009 | Handle Package Expiry | Lifecycle | Business Review Draft |
| PS-PKG-010 | Freeze Package | Lifecycle | Business Review Draft |
| PS-PKG-011 | Resume Package | Lifecycle | Business Review Draft |
| PS-PKG-012 | Extend Package Validity | Lifecycle | Business Review Draft |
| PS-PKG-013 | Transfer Package Review | Lifecycle | Business Review Draft |

## Scenario Flow Summary

```text
Package Purchase / Ownership
        ↓
Validate Active Package
        ↓
Validate Treatment Eligibility
        ↓
Validate Balance
        ↓
Handle Multiple Packages
        ↓
Booking / Treatment Completion
        ↓
Redeem Package
        ↓
Update Balance + Audit History
```

## Alternative Paths
```text
No-show → No Deduction
Expired Package → Cannot Redeem
Frozen Package → Cannot Consume Until Resumed
Extension Request → Requires Approval
Transfer Request → Requires Policy Confirmation
```
