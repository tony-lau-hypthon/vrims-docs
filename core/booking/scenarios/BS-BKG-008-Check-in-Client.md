---
id: BS-BKG-008
title: Check-in Client
type: Business Scenario
version: 0.3R
status: Business Review
---

# BS-BKG-008 – Check-in Client

## Purpose
Record client arrival before treatment.

## Business Context
Reception checks in customers with confirmed bookings.

## Actors
- Reception
- Customer
- Booking System

## Trigger
Customer arrives.

## Preconditions
- Booking status = Confirmed

## Main Success Flow
1. Search booking.
2. Verify customer.
3. Mark Checked-in.
4. Notify therapist.

## Alternative Flow
- Walk-in linked to existing booking.

## Exception Flow
- Customer arrives at wrong time.
- Booking not found.

## Related Business Rules
- Booking must be confirmed before check-in.

## Related Decisions
- Checked-in precedes treatment.

## Evidence
- VRC Session 5 Workshop
- Session 5 Answered Open Questions
- Tony Review

## Review Questions
- Should grace period be configurable?

## Future Enhancement
Reserved for Functional Version (F).
