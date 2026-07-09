---
id: PS-PKG-006
title: Handle No-show Without Deduction
capability: Package
version: 0.72R
status: Business Review Draft
---

# Handle No-show Without Deduction

## Purpose
Define behaviour when customer does not attend a confirmed booking.

## Trigger
Booking status becomes No-show.

## Preconditions
- Booking confirmed.
- Customer absent.
- No completed treatment recorded.

## Main Success Flow
1. Mark booking as No-show.
2. Do not redeem package.
3. Preserve package balance.
4. Record no-show event.
5. Allow follow-up according to business policy.

## Postconditions
- Package remains unchanged.
- Audit trail available.

## Related Business Rules
- BR-PKG-007

## Evidence
- VRC Session 5 workshop
- Answered open questions
- BA consolidation
