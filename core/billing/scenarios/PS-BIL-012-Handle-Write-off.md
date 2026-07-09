---
id: PS-BIL-012
title: Handle Write-off
capability: Billing
version: 0.102R
status: Business Review Draft
knowledge_confidence: 70%
related_capabilities:
  - Package
  - Booking
  - Notification
impacted_modules:
  - Wellness Centre
  - Finance
  - Customer Portal
---

# Handle Write-off

## Purpose
Handle approved write-off of outstanding balance.

## Business Context
Write-off may be required for finance adjustment, unrecoverable balance or approved business decision.

## Trigger
Finance determines that an outstanding balance should be written off.

## Preconditions
- Outstanding invoice/balance exists.
- Write-off reason is known.
- Approval obtained where required.

## Main Success Flow
1. Finance opens outstanding balance.
2. Finance selects write-off action.
3. Finance records reason.
4. System adjusts outstanding balance.
5. Write-off history is retained.

## Alternative Flow
- Write-off may be partial or full.
- Write-off may require management approval.

## Exception Flow
- Approval missing.
- Balance already settled.
- Write-off reason missing.

## Postconditions
- Outstanding balance reduced or closed.
- Write-off record retained.

## Related Business Rules
- BR-BIL-010 Write-off must be approved and auditable.

## Related Decisions
- D-BIL-006 Write-off requires approval and reason.

## Evidence
- Invoice / Credit Note sample evidence
- Referral fee terms and calculation reference
- Finance workshop decision evidence
- BA consolidation

## Review Questions
- Is write-off required for VRC initial launch?
- Who can approve write-off?
