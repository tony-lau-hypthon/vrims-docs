---
id: PS-BIL-013
title: Process Referral Fee Settlement
capability: Billing
version: 0.102R
status: Business Review Draft
knowledge_confidence: 75%
related_capabilities:
  - Package
  - Booking
  - Notification
impacted_modules:
  - Wellness Centre
  - Finance
  - Customer Portal
---

# Process Referral Fee Settlement

## Purpose
Handle referral fee settlement based on agreed referral fee rules.

## Business Context
Referral fee calculation and settlement may impact finance reporting and partner/referrer payment.

## Trigger
Referral fee becomes eligible for review or settlement.

## Preconditions
- Referral relationship exists.
- Referral fee terms are available.
- Related charge/payment condition is satisfied.

## Main Success Flow
1. Finance identifies eligible referral case.
2. Finance checks referral fee terms.
3. Finance calculates referral fee.
4. Finance records referral fee payable/settlement.
5. Settlement status is tracked.

## Alternative Flow
- Referral fee may be calculated periodically.
- Referral fee may require manual verification.

## Exception Flow
- Referral terms missing.
- Referral relationship disputed.
- Payment condition not satisfied.

## Postconditions
- Referral fee record created or marked pending.
- Audit history retained.

## Related Business Rules
- BR-BIL-011 Referral fee must follow approved terms.
- BR-BIL-004 Billing history must be auditable.

## Related Decisions
- D-BIL-007 Referral fee settlement is finance-controlled.

## Evidence
- Invoice / Credit Note sample evidence
- Referral fee terms and calculation reference
- Finance workshop decision evidence
- BA consolidation

## Review Questions
- Is referral fee part of VRC initial scope?
- Is referral fee calculated automatically or manually?
