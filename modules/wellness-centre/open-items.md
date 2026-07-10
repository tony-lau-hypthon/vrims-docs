---
id: VRIMS-WC-001-OPEN-ITEMS
title: Wellness Centre Open Items
type: Open Items
module: Wellness Centre
version: 1.3R
status: Business Review Ready
visibility:
  executive: true
  business: true
  functional: true
---

# Open Items

## Confirmed Facts

| Item | Resolution | Knowledge Status |
|---|---|---|
| Customer Portal scope | Web app with PWA capability for VR Resident, VRC Member and VC Member | Validated |
| VRC online treatment booking | VRC Member can request treatment booking through the Customer Portal | Validated |
| VRC membership timing | VRC Member is an existing user type; future-membership wording is obsolete | Validated |
| 45-minute scheduling | Two consecutive 30-minute slots are reserved; the unused 15 minutes remains unavailable | Validated |
| Online cancellation / rescheduling | Not established by online booking support | Confirmed boundary |

## Assumptions

None. Items below remain unresolved rather than assumed.

## Conflicts

Any source or generated output that presents VRC membership, online treatment booking or Customer Portal as future scope conflicts with the Release-016R Pack 2 canonical baseline.

## Open Questions — Pending Business Validation

| Item | Area | Why Required |
|---|---|---|
| Customer eligibility matrix | Product / Promotion | Define which customer groups may purchase each product or package |
| Discount matrix | Pricing / Promotion | Define resident, member, staff, relative and corporate treatment |
| Accepted payment methods | Billing | Confirm supported payment channels |
| Deposit / partial payment / instalment | Billing | Define settlement and outstanding-balance behaviour |
| Refund calculation and approval | Billing | Define refundable amount and approval authority |
| eftPay integration approach | Integration | Confirm technical method and vendor support |

## Open Questions — Functional Design Required

| Item | Area | Design Need |
|---|---|---|
| Monthly package definition | Package | Confirm exact validity duration and expiry rule |
| Validity start rule | Package | Confirm purchase date versus first-use date |
| Multiple-package selection | Package / Billing | Define automatic selection and controlled staff intervention |
| Assessment matrix | Assessment | Map service or package to required assessment |
| Notification configuration | Notification | Confirm timing, language, recipient and final text |

## Decisions

- Resolved Pack 2 items remain in the confirmed section for regression protection.
- Unresolved items must not be silently promoted to confirmed requirements.
- Deferred supporting evidence does not block business review but may block detailed design or reporting specification.

## Deferred Supporting Evidence

- Detailed report layout and calculations
- Sample transaction and income reports
- Sample invoice layout
- Daily schedule images
- UI screenshots and mockups

## Related Modules

Wellness Centre, Booking, Package, Assessment, Billing, Notification, Customer Portal and Integration.

---

## Decision History

### Release-014R
The open-item structure was enriched into business validation, functional-design and deferred-evidence groups.

### Release-016R Pack 2
Portal scope, current user groups, VRC Member online booking and 45-minute slot handling were validated. Obsolete future-scope questions were removed.

### Release-016R Pack 3
The resolved facts, conflicts, open questions, decisions and related modules were made explicit for business-review traceability. No new business rule was introduced.
