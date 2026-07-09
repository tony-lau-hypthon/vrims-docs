---
id: PS-PKG-003
title: Validate Package Balance
type: Business Scenario
capability: Package
version: 0.71R
status: Business Review Draft
business_value: High
complexity: Medium
knowledge_confidence: 90%
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

# PS-PKG-003 — Validate Package Balance

## 1. Purpose

Confirm whether the package has sufficient remaining entitlement for the requested treatment.

## 2. Business Context

Package-based treatment should only proceed when the customer has enough package balance or session entitlement, unless staff chooses another billing path.

## 3. Primary Actors

- Reception
- Package Management
- Booking Management

## 4. Trigger

An eligible active package is identified.

## 5. Preconditions

- Package is active.
- Package covers requested treatment.
- Remaining balance/session count is available.

## 6. Main Success Flow

1. System checks remaining package balance/session count.
2. System verifies that the requested treatment can be supported.
3. If balance is sufficient, validation passes.
4. Booking may proceed to resource and confirmation handling.
5. Package balance is not deducted during validation.

## 7. Alternative Flow

- If balance is insufficient, staff may propose package renewal or single treatment payment.
- If multiple packages exist, system may evaluate another valid package.

## 8. Exception Flow

- Package balance is missing.
- Package balance is disputed.
- Manual adjustment is required before confirmation.

## 9. Postconditions

- Package balance validation result is known.
- No package redemption has occurred.

## 10. Related Business Rules

- BR-PKG-003 — Redemption occurs after completed treatment
- BR-PKG-005 — Package transaction history must be retained

## 11. Related Decisions

- No-show does not deduct package
- Package redemption happens after completed treatment

## 12. Evidence

- VRC Session 5 Answered Open Questions Q20
- Tony Review

## 13. BA Notes

Balance validation and redemption must remain separate to avoid premature deduction.

## 14. Review Questions

- Should package balance be reserved at booking confirmation?
- Should package balance be deducted only after Completed status?
