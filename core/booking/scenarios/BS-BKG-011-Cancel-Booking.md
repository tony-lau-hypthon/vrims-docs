---
id: BS-BKG-011
title: Cancel Booking
version: 0.4R
status: Business Review
---

# BS-BKG-011 – Cancel Booking

## Purpose
Handle cancellation of an existing confirmed booking.

## Business Context
For VRC, customers currently do not cancel bookings directly online. Cancellation is handled by staff.

## Actors
- Reception
- Customer
- Booking System

## Trigger
Customer requests cancellation or staff cancels operationally.

## Preconditions
- Booking exists

## Main Success Flow
1. Reception locates booking.
2. Reviews cancellation request.
3. Cancels booking.
4. Status becomes Cancelled.
5. Notify customer.

## Alternative Flow
- Management overrides cancellation decision.

## Exception Flow
- Booking already completed.
- Booking already cancelled.

## Related Business Rules
- Customer online cancellation not supported.

## Related Decisions
- Staff controls cancellation.

## Evidence
- VRC Session 5 Workshop
- Session 5 Answered Open Questions
- Tony Review

## Review Questions
- Should cancellation reason be mandatory?

## Future Enhancement
Reserved for Functional Version (F).
