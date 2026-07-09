---
id: PS-PKG-002
title: Validate Treatment Eligibility
type: Business Scenario
capability: Package
version: 0.71R
status: Business Review Draft
business_value: High
complexity: Medium
knowledge_confidence: 85%
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

# PS-PKG-002 — Validate Treatment Eligibility

## 1. Purpose

Confirm whether the selected package can be used for the requested treatment or service.

## 2. Business Context

Not every package may be valid for every treatment type. The package entitlement must align with the requested VRC service before booking confirmation.

## 3. Primary Actors

- Reception
- Booking Management
- Package Management

## 4. Trigger

An active package is found for a customer and treatment/service is selected.

## 5. Preconditions

- Active package exists.
- Requested treatment/service is known.

## 6. Main Success Flow

1. System checks treatment/service category.
2. System compares selected treatment against package entitlement.
3. If package covers the treatment, validation passes.
4. If package does not cover the treatment, validation fails or staff selects another valid package.
5. Reception proceeds based on validation result.

## 7. Alternative Flow

- Customer may purchase another package if current package is not eligible.
- Customer may pay for single treatment if permitted.

## 8. Exception Flow

- Treatment category is not configured.
- Package entitlement is unclear.
- Package contains mixed services not yet defined.

## 9. Postconditions

- Package eligibility result is known.
- Booking may proceed only if entitlement or payment handling is acceptable.

## 10. Related Business Rules

- BR-PKG-002 — Package must be validated before booking confirmation where applicable

## 11. Related Decisions

- Package eligibility rules are treated as package capability rules and should not be duplicated inside Booking.

## 12. Evidence

- VRC Session 5 package / booking discussion
- Tony Review

## 13. BA Notes

Detailed treatment-to-package mapping may require service catalogue confirmation.

## 14. Review Questions

- Are all treatments tied to package entitlement?
- Can staff override package-treatment mismatch?
- Should package entitlement be defined at service category or individual treatment level?
