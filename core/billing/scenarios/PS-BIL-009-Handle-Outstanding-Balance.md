---
id: PS-BIL-009
title: Handle Outstanding Balance
capability: Billing
version: 0.102R
status: Business Review Draft
knowledge_confidence: 80%
related_capabilities:
  - Package
  - Booking
  - Notification
impacted_modules:
  - Wellness Centre
  - Finance
  - Customer Portal
---

# Handle Outstanding Balance

## Purpose
Track invoices or charges that remain unpaid or partially paid.

## Business Context
Outstanding balances affect finance follow-up, customer account status and reporting.

## Trigger
Invoice remains unpaid after generation or after partial payment.

## Preconditions
- Invoice exists.
- Payment status is unpaid or partially paid.

## Main Success Flow
1. System identifies unpaid / partially paid invoice.
2. Outstanding amount is calculated.
3. Finance reviews outstanding balance.
4. Follow-up action is recorded.
5. Payment reminder may be triggered.

## Alternative Flow
- Outstanding balance may be settled later.
- Balance may be adjusted by credit note, refund or write-off.

## Exception Flow
- Invoice disputed.
- Customer account cannot be matched.
- Balance calculation discrepancy.

## Postconditions
- Outstanding balance remains visible for Finance review.
- Follow-up history retained.

## Related Business Rules
- BR-BIL-008 Outstanding balance must be visible to Finance.
- BR-NTF-001 Notification is triggered by business events.

## Related Decisions
- D-BIL-003 Outstanding balance requires follow-up visibility.

## Evidence
- Invoice / Credit Note sample evidence
- Referral fee terms and calculation reference
- Finance workshop decision evidence
- BA consolidation

## Review Questions
- Should outstanding balance block future booking?
- Should payment reminder be automatic?
