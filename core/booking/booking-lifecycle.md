---
id: VRIMS-BKG-LIFECYCLE-001
title: Booking Lifecycle
type: Lifecycle
capability: Booking
version: 0.1
status: Business Review Draft
knowledge_confidence: 95%
source_sessions:
  - VRC Session 5
---

# Booking Lifecycle

## Confirmed Booking Statuses

| Status | Description |
|---|---|
| Pending | Booking request created and awaiting staff confirmation |
| Confirmed | Booking confirmed by authorised staff |
| Checked-in | Client has arrived for the booking |
| Completed | Treatment/service completed |
| Cancelled | Booking cancelled |
| No-show | Client did not attend |

## VRC Lifecycle

```text
Pending
  ├── Confirmed
  │     ├── Checked-in
  │     │     └── Completed
  │     ├── Cancelled
  │     └── No-show
  └── Cancelled
```

## Status Rules

- VRC booking request starts as Pending.
- Staff confirmation is required before booking becomes Confirmed.
- No-show is a status only; it does not deduct package balance and does not create penalty.
- Cancelled bookings do not proceed to treatment completion.
- Completed bookings may trigger package redemption or payment settlement.

## Open Design Notes

- Whether a separate "Closed" status is needed is not confirmed.
- Whether backend audit status is required is not confirmed.
