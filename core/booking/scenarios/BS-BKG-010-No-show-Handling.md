---
id: BS-BKG-010
title: No-show Handling
type: Business Scenario
version: 0.3R
status: Business Review
---

# BS-BKG-010 – No-show Handling

## Purpose
Record non-attendance without deducting package.

## Business Context
Customer fails to attend confirmed appointment.

## Actors
- Reception
- Booking System

## Trigger
Customer absent after operational cut-off.

## Preconditions
- Booking status = Confirmed

## Main Success Flow
1. Reception marks No-show.
2. Booking status becomes No-show.
3. No package deducted.
4. Case available for reporting.

## Alternative Flow
- Customer later contacts reception to rebook.

## Exception Flow
- Attendance dispute requires manager review.

## Related Business Rules
- BR-BKG-013

## Related Decisions
- D-0005

## Evidence
- VRC Session 5 Workshop
- Session 5 Answered Open Questions
- Tony Review

## Review Questions
- Should reminder history be displayed?

## Future Enhancement
Reserved for Functional Version (F).
