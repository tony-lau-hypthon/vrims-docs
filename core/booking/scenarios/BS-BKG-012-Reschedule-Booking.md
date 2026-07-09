---
id: BS-BKG-012
title: Reschedule Booking
version: 0.4R
status: Business Review
---

# BS-BKG-012 – Reschedule Booking

## Purpose
Move an existing booking to another available slot.

## Business Context
Rescheduling is performed by staff after validating new availability.

## Actors
- Reception
- Booking System

## Trigger
Customer requests a new appointment time.

## Preconditions
- Booking exists
- New slot available

## Main Success Flow
1. Open booking.
2. Search new slot.
3. Validate therapist and room.
4. Save new appointment.
5. Notify customer.

## Alternative Flow
- Customer accepts first available slot.

## Exception Flow
- No suitable slot available.

## Related Business Rules
- Customer online reschedule not supported.

## Related Decisions
- Staff approves reschedule.

## Evidence
- VRC Session 5 Workshop
- Session 5 Answered Open Questions
- Tony Review

## Review Questions
- Should original booking history be retained?

## Future Enhancement
Reserved for Functional Version (F).
