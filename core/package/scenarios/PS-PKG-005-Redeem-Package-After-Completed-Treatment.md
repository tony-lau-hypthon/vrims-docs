---
id: PS-PKG-005
title: Redeem Package After Completed Treatment
capability: Package
version: 0.72R
status: Business Review Draft
---

# Redeem Package After Completed Treatment

## Purpose
Consume package entitlement only after the treatment has been successfully completed.

## Trigger
Treatment status changes to Completed.

## Preconditions
- Valid package identified.
- Treatment completed.
- Package has sufficient remaining entitlement.

## Main Success Flow
1. Verify Completed status.
2. Select validated package.
3. Deduct entitlement.
4. Record redemption history.
5. Update remaining balance.
6. Notify downstream billing/reporting if applicable.

## Postconditions
- Package balance reduced.
- Audit history recorded.
- Booking remains linked to redemption record.

## Related Business Rules
- BR-PKG-006
- BR-PKG-008
- BR-PKG-009

## Evidence
- VRC Session 5 workshop
- Answered open questions
- BA consolidation
