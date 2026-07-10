---
id: VRIMS-REL-016R-P3
title: Release-016R Pack 3 — VRC Review Readiness and Traceability Closure
type: Release Summary
version: 1.0
status: Ready for Merge
owner: BA
---

# Release-016R Pack 3 — VRC Review Readiness and Traceability Closure

## Objective

Close the Release-016R VRC regression cycle after Pack 2 by aligning review readiness, open-item classification, release navigation and merge controls with the canonical validated scope.

## Confirmed Facts Carried Forward

- Customer Portal is a web application with PWA capability.
- Current portal user groups are VR Resident, VRC Member and VC Member.
- VRC Members can submit treatment booking requests through the Customer Portal.
- Booking uses 30-minute calendar slots.
- A 45-minute treatment reserves two consecutive 30-minute slots.
- The unused 15 minutes remains unavailable within the reserved booking window.
- Online booking does not establish online cancellation or online rescheduling.
- VRC commercial services and packages remain separate from VR Resident care packages.

## Assumptions

None added by this pack.

## Conflicts

No new conflict is introduced. Any document that describes VRC membership, online booking or Customer Portal as future scope conflicts with Pack 2 and must not be restored.

## Open Questions

The following remain unresolved and must stay visible:

- Customer eligibility matrix
- Discount matrix
- Accepted payment methods
- Deposit, partial payment and instalment behaviour
- Refund calculation and approval
- eftPay integration approach
- Monthly package validity definition
- Package validity start rule
- Multiple-package selection behaviour
- Assessment matrix
- Notification configuration

## Decisions

- Pack 3 is a traceability and readiness closure pack only.
- No new business rule ID is created.
- Review deliverables may be generated only after the Pack 3 merge gate passes.

## Related Modules

- Wellness Centre (VRC)
- Booking
- Package
- Assessment
- Billing
- Notification
- Customer Portal

## Business Impact

No new business behaviour. This pack improves repository integrity and establishes a controlled hand-off for business-review document generation.

## Regression Risk

Low, provided the merge preserves Pack 2 business rules and does not convert unresolved items into confirmed requirements.
