---
id: PS-PKG-001
title: Validate Active Package
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

# PS-PKG-001 — Validate Active Package

## 1. Purpose

Confirm whether a customer has an active package that can be considered for booking or treatment entitlement.

## 2. Business Context

VRC customers may hold one or more packages. Before confirming a package-based booking, staff and system must verify that the package is active and usable.

## 3. Primary Actors

- Reception
- Package Management
- Booking Management
- Customer / VRC Client

## 4. Trigger

A booking or treatment request requires package entitlement validation.

## 5. Preconditions

- Customer / VRC client is identified.
- Service or treatment type is selected.
- Package records are available.

## 6. Main Success Flow

1. System retrieves customer packages.
2. System filters packages with Active status.
3. System excludes expired or inactive packages.
4. System returns active package candidates for further validation.
5. Reception reviews package validation result before booking confirmation.

## 7. Alternative Flow

- If no active package exists, staff may check whether single-session payment is allowed.
- If assessment is free of charge, package validation may not be required for that assessment.

## 8. Exception Flow

- Package record cannot be found.
- Package status is inconsistent.
- Customer identity is duplicated or unclear.

## 9. Postconditions

- Active package candidates are identified, or booking proceeds through non-package handling if allowed.
- No package is redeemed at this stage.

## 10. Related Business Rules

- BR-PKG-001 — Customer may own multiple packages
- BR-PKG-002 — Package must be validated before booking confirmation where applicable

## 11. Related Decisions

- D-0006 — Multiple packages consume closest expiry first

## 12. Evidence

- VRC Session 5 Answered Open Questions
- Booking package validation discussion
- Tony Review

## 13. BA Notes

This scenario validates package availability only. Package redemption is handled after treatment completion and will be covered in Release-007.2R.

## 14. Review Questions

- Should inactive package be visible to Reception during validation?
- Should staff be allowed to override inactive package validation?
