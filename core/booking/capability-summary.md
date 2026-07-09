---
id: VRIMS-BKG-001-SUMMARY
title: Booking Management Capability Summary
type: Capability Summary
capability: Booking
version: 0.5R
status: Business Review Draft
knowledge_confidence: 95%
---

# Booking Management Capability Summary

## Business Objective
Booking Management provides a controlled process for creating, reviewing, confirming, executing and maintaining service appointments.

## VRC Booking Principle
VRC booking is staff-controlled.

Customers may request bookings, but VRC staff remain responsible for:
- reviewing the request,
- validating package/resource availability,
- assigning therapist,
- confirming booking,
- handling cancellation/reschedule.

## Confirmed VRC Booking Characteristics
- Customer cannot choose therapist.
- Customer cannot cancel booking online.
- Customer cannot reschedule booking online.
- Booking starts as Pending.
- Reception confirms booking.
- Therapist and room cannot be double-booked.
- No waiting list is supported.
- No-show does not deduct package and does not create penalty.
- Home visit booking is not supported at this moment.

## Booking Lifecycle Summary
```text
Pending
  ├── Confirmed
  │     ├── Checked-in
  │     │     └── Completed
  │     │           └── Closed
  │     ├── Cancelled
  │     └── No-show
  └── Cancelled
```

## Confidence
| Area | Confidence |
|---|---:|
| Booking initiation | 95% |
| Booking confirmation | 95% |
| Booking execution | 90% |
| Booking maintenance | 85% |
| Reporting details | 75% |
| Future module variants | TBD |
