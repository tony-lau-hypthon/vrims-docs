---
id: BS-BKG-009
title: Complete Treatment
type: Business Scenario
version: 0.3R
status: Business Review
---

# BS-BKG-009 – Complete Treatment

## Purpose
Complete treatment and prepare downstream package/billing.

## Business Context
Therapist finishes treatment and operational completion is recorded.

## Actors
- Therapist
- Reception
- Booking System

## Trigger
Treatment finished.

## Preconditions
- Customer checked in

## Main Success Flow
1. Therapist completes session.
2. Reception records completion.
3. Booking status becomes Completed.
4. Trigger package redemption/billing workflow.

## Alternative Flow
- Completion entered later by reception.

## Exception Flow
- Treatment interrupted.
- Customer leaves early.

## Related Business Rules
- Package redemption occurs after completion.

## Related Decisions
- Completion enables downstream charging.

## Evidence
- VRC Session 5 Workshop
- Session 5 Answered Open Questions
- Tony Review

## Review Questions
- Should therapist remarks be mandatory?

## Future Enhancement
Reserved for Functional Version (F).
