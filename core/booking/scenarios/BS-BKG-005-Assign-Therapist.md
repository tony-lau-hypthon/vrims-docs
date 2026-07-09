---
id: BS-BKG-005
title: Assign Therapist
type: Business Scenario
version: 0.2R
status: Business Review
---

# BS-BKG-005 – Assign Therapist

## Purpose
Assign an appropriate therapist before confirming the booking.

## Business Context
Therapist assignment is performed by authorised VRC staff. Customers cannot choose therapists.

## Actors
- Reception
- Management
- Booking System

## Trigger
Package and resource validation completed.

## Preconditions
- Booking status is Pending
- Required treatment identified

## Main Success Flow
1. Reception opens validated booking.
2. System shows available therapists.
3. Reception selects therapist.
4. System validates availability.
5. Therapist assignment saved.
6. Booking proceeds to confirmation.

## Alternative Flow
- Management changes therapist before confirmation.
- Reception selects another available therapist.

## Exception Flow
- No therapist available.
- Therapist becomes unavailable during assignment.

## Related Business Rules
- BR-BKG-002
- BR-BKG-003
- BR-BKG-004
- BR-BKG-009

## Related Decisions
- D-0002
- D-0003

## Evidence
- VRC Session 5 Workshop
- VRC Session 5 Email
- Session 5 Answered Open Questions
- Tony Review

## Review Questions
- Should management approval be required for reassignment?

## Future Enhancement
Reserved for Functional Version (F).
