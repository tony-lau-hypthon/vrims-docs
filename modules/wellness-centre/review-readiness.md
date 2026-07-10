---
id: VRIMS-WC-001-READINESS-R
title: Wellness Centre Review Readiness
type: Readiness Assessment
module: Wellness Centre
version: 1.2R
status: Business Review Ready
visibility:
  executive: true
  business: true
  functional: true
---

# Wellness Centre Review Readiness

| Area | Readiness | Notes |
|---|---|---|
| Customer Journey | High | Main VRC journey consolidated; current portal user groups and VRC Member booking scope validated |
| Product Catalogue | High | Core service and product lines understood |
| Package & Pricing | Medium-High | Core package model captured; monthly validity, start rule and multiple-package selection remain open |
| Booking | High | Staff-controlled confirmation and fixed-slot behaviour consolidated; online cancellation/rescheduling are not established |
| Customer Portal | High | Web App + PWA scope and supported user groups validated |
| Assessment | Medium-High | Package-purchase prerequisite understood; detailed matrix pending |
| Billing | Medium | Main lifecycle understood; payment, instalment and refund policies pending |
| Promotion / Eligibility | Medium | Non-combination rule known; eligibility and discount matrices pending |
| Notification | Medium-High | Trigger capability known; timing, language, recipients and final text pending |
| Reporting | Deferred | Supporting report evidence intentionally postponed |

## Confirmed Facts

- VRC Members can submit treatment booking requests through the Customer Portal.
- Customer Portal supports VR Resident, VRC Member and VC Member user groups.
- Customer Portal is a web application with PWA capability.
- A 45-minute treatment blocks two consecutive 30-minute slots, including the unavailable 15-minute remainder.
- VRC package/service operations are separate from VR Resident care packages.

## Assumptions

None introduced by this readiness assessment.

## Conflicts

Future-scope descriptions of VRC membership, Customer Portal or online treatment booking are obsolete and must not be used.

## Open Questions

See `modules/wellness-centre/open-items.md`. Open questions must remain visible in generated business-review outputs and must not be presented as confirmed requirements.

## Decisions

The VRC domain is ready for Executive and Business User Review. Controlled Functional Design drafting may start only for areas with sufficient confirmed knowledge and must preserve all pending decisions.

## Related Modules

Booking, Package, Assessment, Billing, Notification and Customer Portal.

## Overall Assessment

The VRC Domain Foundation is business-review ready after Release-016R Pack 2 regression clarification and Pack 3 traceability closure.

It is not a final Odoo configuration, Functional Design or Technical Specification. Design assumptions and pending VR decisions must remain visibly labelled.
