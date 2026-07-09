---
id: PS-BIL-008
title: Record Payment Received
capability: Billing
version: 0.102R
status: Business Review Draft
knowledge_confidence: 85%
related_capabilities:
  - Package
  - Booking
  - Notification
impacted_modules:
  - Wellness Centre
  - Finance
  - Customer Portal
---

# Record Payment Received

## Purpose
Record that payment has been received for an invoice or billable item.

## Business Context
Payment received is a key settlement event and may trigger receipt, invoice status update and reporting.

## Trigger
Customer payment is confirmed by Finance or payment channel.

## Preconditions
- Invoice exists.
- Payment amount and method are known.

## Main Success Flow
1. Finance opens invoice.
2. Finance records payment method and amount.
3. System updates payment status.
4. Receipt / payment record is retained.
5. Notification event may be raised where applicable.

## Alternative Flow
- Payment may be received before invoice generation in special cases.
- Payment may be split across methods.

## Exception Flow
- Payment amount is invalid.
- Payment method is unsupported.
- Invoice already fully paid.

## Postconditions
- Payment record exists.
- Invoice status updated.

## Related Business Rules
- BR-BIL-004 Billing history must be auditable.
- BR-BIL-007 Payment received must update invoice/payment status.

## Related Decisions
- D-BIL-002 Payment received changes billing status.

## Evidence
- Invoice / Credit Note sample evidence
- Referral fee terms and calculation reference
- Finance workshop decision evidence
- BA consolidation

## Review Questions
- Should receipt generation be part of Review Version?
- Which payment methods are accepted for VRC?
