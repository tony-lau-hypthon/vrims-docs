---
id: VRIMS-ASM-001-REVIEW-PACK
title: Assessment Management Review Pack
type: Capability Review Pack
capability: Assessment
version: 1.0R
status: Business Review Draft
knowledge_confidence: 85%
source_releases:
  - 008.1R
  - 008.2R
visibility:
  executive: true
  business: true
  functional: true
  technical: false
---

# Assessment Management Review Pack

## Purpose
This Review Pack consolidates the Assessment Management capability for business review.

Assessment Management defines how VRC assessments are created, assigned, conducted, completed, and used to generate treatment recommendations.

## Capability Coverage
The Assessment Management capability currently covers:

1. Assessment execution
2. Assessment completion
3. Assessment outcome handling
4. Treatment recommendation
5. Assessment-to-booking dependency
6. Assessment-to-package dependency

## Review Position
This is an **R Version** document.

It confirms the business behaviour and dependencies of Assessment Management. It is not yet a clinical form design, scoring model, or Odoo configuration specification.

## Related Modules
- Wellness Centre (VRC)
- Booking Management
- Package Management
- Treatment Management
- Reporting

## Key Business Principles
- Assessment may be required before selected treatments.
- Assessment record must be retained.
- Completed assessment may generate treatment recommendation.
- Treatment booking should align with assessment recommendation where assessment is mandatory.
- Recommendation may influence package selection.

## Next Step
This capability can now be referenced by `VRIMS-WC-001 — Wellness Centre (VRC)` in the module-level Business Functional Design.
