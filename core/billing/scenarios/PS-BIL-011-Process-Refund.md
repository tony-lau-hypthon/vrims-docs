---
id: PS-BIL-011
title: Process Refund
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

# Process Refund

## Purpose
Handle refund to customer when business-approved refund is required.

## Business Context
Refund may occur after overpayment, cancellation, credit note or other approved finance adjustment.

## Trigger
Refund request or finance-approved refund event occurs.

## Preconditions
- Customer / payer is identifiable.
- Refund amount is approved.
- Refund reason is recorded.

## Main Success Flow
1. Finance reviews refund request.
2. Finance validates original payment / invoice.
3. Finance records refund reason and amount.
4. Refund transaction is created.
5. Invoice/payment status is updated where applicable.

## Alternative Flow
- Refund may be full or partial.
- Refund may be handled manually outside system in Review Version.

## Exception Flow
- Refund amount exceeds original payment.
- Approval missing.
- Original payment cannot be verified.

## Postconditions
- Refund record created.
- Audit trail retained.

## Related Business Rules
- BR-BIL-009 Refund must reference original payment or invoice where applicable.
- BR-BIL-004 Billing history must be auditable.

## Related Decisions
- D-BIL-005 Refund requires approved reason and audit trail.

## Evidence
- Invoice / Credit Note sample evidence
- Referral fee terms and calculation reference
- Finance workshop decision evidence
- BA consolidation

## Review Questions
- Is refund in initial scope for VRC?
- Which refund methods are supported?
