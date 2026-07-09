---
id: PS-PKG-004
title: Handle Multiple Packages
type: Business Scenario
capability: Package
version: 0.71R
status: Business Review Draft
business_value: High
complexity: High
knowledge_confidence: 95%
source_sessions:
  - VRC Session 5 Workshop
  - VRC Session 5 Answered Open Questions
  - Tony Review
applies_to:
  - VRC
future_variants:
  - VR Resident
  - Customer Portal
  - Finance
---

# PS-PKG-004 — Handle Multiple Packages

## 1. Purpose

Define how the system determines which package should be used when a customer has multiple valid packages.

## 2. Business Context

VRC confirmed that when multiple active packages exist, the package with the closest expiry date should be used first.

## 3. Primary Actors

- Package Management
- Booking Management
- Reception

## 4. Trigger

Customer has more than one active package eligible for the selected treatment.

## 5. Preconditions

- Multiple active packages exist.
- More than one package is eligible for the requested treatment.
- Package expiry dates are available.

## 6. Main Success Flow

1. System identifies all active and eligible packages.
2. System sorts packages by expiry date.
3. System selects the package with closest expiry date.
4. Reception can view the selected package for validation.
5. Selected package is reserved for future redemption reference, if applicable.
6. Actual redemption occurs after treatment completion.

## 7. Alternative Flow

- If two packages have same expiry date, tie-breaker rule is TBD.
- If staff needs to manually select package, this should be reviewed as future functional rule.

## 8. Exception Flow

- Package expiry date missing.
- Package eligibility conflict.
- Staff disputes system-selected package.

## 9. Postconditions

- A preferred package is identified for future redemption.
- Package balance is not deducted at validation stage.

## 10. Related Business Rules

- BR-PKG-004 — Earliest expiry package is consumed first
- BR-BKG-016 — Package with closest expiry is consumed first

## 11. Related Decisions

- D-0006 — Multiple packages consume closest expiry first

## 12. Evidence

- VRC Session 5 Answered Open Questions Q9
- Tony Review

## 13. BA Notes

This is a confirmed VRC rule and should be treated as a reusable package priority rule unless later sessions define variants.

## 14. Review Questions

- What is the tie-breaker if two valid packages have the same expiry date?
- Should staff be allowed to override closest-expiry selection?
