---
id: VRIMS-WC-001-OPEN-ITEMS
title: Wellness Centre Open Items
type: Open Items
module: Wellness Centre
version: 1.2R
status: Domain Foundation Verified
visibility:
  executive: true
  business: true
  functional: true
---

# Open Items

## Pending Validation

| Item | Area | Why Required |
|---|---|---|
| Customer eligibility matrix | Product / Promotion | Define which customer groups may purchase each product/package |
| Discount matrix | Pricing / Promotion | Define resident, member, staff, relative and corporate treatment |
| Accepted payment methods | Billing | Confirm supported payment channels |
| Deposit / partial payment / instalment | Billing | Define settlement and outstanding-balance behaviour |
| Refund calculation and approval | Billing | Define refundable amount and authority |
| eftPay integration approach | Integration | Confirm technical method and vendor support |

## Functional Design Required

| Item | Area | Design Need |
|---|---|---|
| Monthly package definition | Package | Confirm exact validity duration and expiry |
| Validity start rule | Package | Confirm purchase date vs first-use date |
| Multiple-package selection | Package / Billing | Define automatic selection and whether controlled staff intervention exists |
| Assessment matrix | Assessment | Map service/package to required assessment |
| Notification configuration | Notification | Confirm timing, language, recipient and final text |


## Resolved by Business Clarification

| Item | Resolution | Knowledge Status |
|---|---|---|
| Customer Portal scope | Web app with PWA capability for VR Resident, VRC Member and VC Member | Validated |
| VRC online treatment booking | VRC Member can request treatment booking through the Customer Portal | Validated |
| Future membership question | Removed; VRC Member is an existing user type | Validated |
| 45-minute scheduling | Reserves two consecutive 30-minute slots; 45 minutes treatment plus 15 minutes unavailable remainder | Validated |

## Deferred Supporting Evidence

- Detailed report layout and calculations
- Sample transaction and income reports
- Sample invoice layout
- Daily schedule images
- UI screenshots and mockups

---

## Conflict Review (Release-014R Merge)

The open items list was restructured during the Release-014R merge. Key changes:

| Area | Existing | New | Resolution |
|---|---|---|---|
| Structure | Two sections: VRC Functional Design (6 items) + Future Capability Releases (5 items) | Three sections: Pending VR Confirmation (6-item table) + Functional Design Required (6-item table) + Deferred Supporting Evidence (5 items) | Accepted — richer structure with status classification |
| Payment items | Generic "Payment gateway provider" | Specific: eftPay integration approach, deposit/partial payment, accepted payment methods | Accepted — more precise |
| Assessment items | "Detailed form fields / clinical scoring" | "Assessment matrix: service/package to required assessment" | Accepted — aligns with BR-BKG-014 |
| Package items | "Same-expiry tie-breaker" | "Monthly package definition + validity start rule + multiple-package selection" | Accepted — richer |
