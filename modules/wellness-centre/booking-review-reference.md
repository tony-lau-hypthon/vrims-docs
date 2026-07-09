---
id: VRIMS-WC-001-BOOKING-REF
title: Wellness Centre Booking Reference
type: Capability Reference
module: Wellness Centre
capability: Booking
version: 0.6R
status: Business Review Draft
visibility:
  executive: false
  business: true
  functional: true
---

# Booking Reference

The Wellness Centre module uses the core Booking Management capability:

`VRIMS-BKG-001 — Booking Management`

## VRC Booking Characteristics

- Booking starts as Pending.
- Reception reviews booking requests.
- Package validation is performed before confirmation where applicable.
- Therapist and room availability must be checked.
- Reception assigns therapist.
- Customer cannot choose therapist.
- Customer cannot cancel online.
- Customer cannot reschedule online.
- Booking can be Confirmed, Checked-in, Completed, Cancelled or No-show.
- No-show does not deduct package and does not create penalty.
- No waiting list is supported for VRC.

## Related Booking Review Pack Files

- `core/booking/review-pack.md`
- `core/booking/capability-summary.md`
- `core/booking/scenario-catalogue.md`
- `core/booking/business-rule-register-review.md`
- `core/booking/decision-register-review.md`
- `core/booking/traceability-matrix-review.md`

## Review Note
This section should be used as a reference, not a duplicate of Booking Management.
