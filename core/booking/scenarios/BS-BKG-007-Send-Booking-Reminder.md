---
id: BS-BKG-007
title: Send Booking Reminder
type: Business Scenario
version: 0.2R
status: Business Review
---

# BS-BKG-007 – Send Booking Reminder

## Purpose
Remind customers of confirmed appointments.

## Business Context
Reminder messages improve attendance and reduce no-show.

## Actors
- Scheduler
- Booking System
- Customer

## Trigger
Configured reminder time reached.

## Preconditions
- Booking status is Confirmed

## Main Success Flow
1. System identifies eligible bookings.
2. Reminder generated.
3. WhatsApp reminder sent.
4. Delivery logged.

## Alternative Flow
- Reception sends reminder manually.

## Exception Flow
- Invalid phone number.
- Messaging service unavailable.

## Related Business Rules
- Uses approved VRC reminder templates

## Related Decisions
- Reminder only applies to confirmed bookings.

## Evidence
- VRC Session 5 Workshop
- VRC Session 5 Email
- Session 5 Answered Open Questions
- Tony Review

## Review Questions
- Is one reminder sufficient?

## Future Enhancement
Reserved for Functional Version (F).
