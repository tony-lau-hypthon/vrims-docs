---
id: BS-BKG-003
title: Validate Package
type: Business Scenario
capability: Booking
version: 0.2
status: Business Review Draft
business_value: High
complexity: High
knowledge_confidence: 95%
source_sessions:
  - VRC Session 5 Workshop
  - VRC Session 5 Email
  - VRC Session 5 Answered Open Questions
  - Tony Review
applies_to:
  - VRC
future_variants:
  - VR Resident
  - VC Member
---

# BS-BKG-003 — Validate Package

## 1. Purpose

Define how the booking process validates whether the customer has valid package entitlement for the selected treatment.

## 2. Business Context

VRC clients may hold multiple active packages. When a booking is related to package entitlement, the system must ensure the booking can be supported by an eligible active package. Package consumption happens after completed treatment, not during booking request.

## 3. Primary Actors

- Reception
- Booking System
- Package Management
- Finance (downstream impact)

## 4. Trigger

Reception reviews a Pending booking request that requires package entitlement validation.

## 5. Preconditions

- Booking request exists.
- Customer / client is identified.
- Service / treatment type is selected.
- Package catalogue and client package balances are available.

## 6. Main Success Flow

1. System retrieves the customer's active packages.
2. System filters packages eligible for the selected treatment/service.
3. System checks remaining balance/session entitlement.
4. If multiple eligible packages exist, system identifies the package with closest expiry date.
5. Reception reviews validation result.
6. Booking may proceed to resource availability check.
7. No package deduction occurs at this stage.

## 7. Alternative Flow

- If service is to be paid as single treatment, package validation may be bypassed and billing will be handled separately.
- If assessment is free of charge, package validation may not be required for that assessment booking.
- If package is missing but customer is allowed to pay per session, Reception may proceed with payment/billing path.

## 8. Exception Flow

- If no valid package exists and payment path is not allowed, booking should not be confirmed.
- If package is expired, it should not be used unless an approved extension exists.
- If package has insufficient balance, booking should not proceed as package-based booking.

## 9. Postconditions

- Eligible package is identified for future redemption.
- Package is not deducted yet.
- Booking can proceed to resource availability validation.

## 10. Related Business Rules

- BR-BKG-016 — Package with closest expiry is consumed first
- BR-BKG-014 — Assessment is mandatory before treatment
- BR-BKG-013 — No-show does not deduct package

## 11. Related Decisions

- D-0006 — Multiple packages consume closest expiry first
- D-0005 — No-show causes no package deduction

## 12. Acceptance Criteria References

- AC-BKG-006 — Closest-expiry Package Consumption

## 13. Evidence

- VRC Session 5 Answered Open Questions Q9, Q17, Q20
- VRC Session 5 Follow-up materials
- Tony Review

## 14. BA Notes

Package validation during booking and package redemption after treatment are separate concepts. This distinction must be preserved to avoid premature revenue or balance deduction.

## 15. Review Questions

- Should booking confirmation be blocked if no package exists but client wants to pay single session?
- Should the closest-expiry rule apply across all package types or only same treatment category?
- Should system reserve package entitlement at booking time, or only deduct after treatment?
