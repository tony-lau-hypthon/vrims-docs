---
id: VRIMS-WC-001-SCOPE
title: Wellness Centre Business Scope
type: Scope
module: Wellness Centre
version: 1.1R
status: Domain Foundation Verified
visibility:
  executive: true
  business: true
  functional: true
---

# Business Scope

## In Scope

| Area | Description | Status |
|---|---|---|
| Customer Registration | VRC client identity, contact, emergency contact, insurance, source and consent handling | Foundation verified |
| Assessment | Assessment before VRC package purchase; detailed matrix pending | Foundation verified |
| Product Catalogue | Rehab, speech, assessment, home service, gym, outreach and related products | Foundation verified |
| Package & Pricing | Single service, premium packages, add-ons, session entitlement and price structure | Foundation verified |
| Booking | Booking request, staff confirmation, resource assignment and treatment execution | Review-ready |
| Treatment | Treatment completion and package usage linkage | Review-ready |
| Billing | Single-service charge, package redemption, invoice and credit-note handling | Foundation verified |
| Notification | Booking and package lifecycle WhatsApp events | Foundation verified |
| Promotion | Non-combination rule and future eligibility/discount matrix | Partial |
| Reporting | Mandatory reports acknowledged; detailed layouts deferred | Deferred |

## Explicitly Out of Scope for This Foundation Release

- Odoo object design
- API design
- Database schema
- Final payment-gateway implementation
- Detailed report field layouts
- Dashboard design
- Daily staff roster interpretation
- UI mockups and screenshots
- Detailed clinical scoring rules

## Business Boundary

Management determines staff rosters and which colleague serves a timeslot. The system records the assigned resource and booking status but does not determine clinical staffing policy.
