---
id: BS-BKG-006
title: Confirm Booking
type: Business Scenario
version: 0.2R
status: Business Review
---

# BS-BKG-006 – Confirm Booking

## Purpose
Confirm a validated booking and notify the customer.

## Business Context
Only authorised staff can confirm a booking after all validations succeed.

## Actors
- Reception
- Booking System

## Trigger
Therapist assigned.

## Preconditions
- Pending booking
- Package validated
- Resources available

## Main Success Flow
1. Reception reviews booking.
2. Reception confirms booking.
3. Status changes to Confirmed.
4. Confirmation timestamp recorded.
5. Reminder event created.

## Alternative Flow
- Reception adjusts booking before confirmation.

## Exception Flow
- Validation fails.
- Resource conflict detected before save.

## Related Business Rules
- BR-BKG-001

## Related Decisions
- D-0001

## Evidence
- VRC Session 5 Workshop
- VRC Session 5 Email
- Session 5 Answered Open Questions
- Tony Review

## Review Questions
- Should confirmation require mandatory remarks?

## Future Enhancement
Reserved for Functional Version (F).
