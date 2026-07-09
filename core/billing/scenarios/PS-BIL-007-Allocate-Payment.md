---
id: PS-BIL-007
title: Allocate Payment
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

# Allocate Payment

## Purpose
Allocate received payment to one or more invoices or billable transactions.

## Business Context
Finance may need to allocate a customer payment against a specific invoice or multiple outstanding items.

## Trigger
Payment is received or identified for a customer account.

## Preconditions
- Customer / payer is identifiable.
- One or more unpaid invoices or charges exist.

## Main Success Flow
1. Finance identifies payer.
2. Finance identifies outstanding invoice(s).
3. Payment amount is matched against invoice balance.
4. Allocation is saved.
5. Invoice balance is updated.
6. Payment history is retained.

## Alternative Flow
- Partial payment may be allocated to invoice.
- Overpayment may require follow-up or refund handling.

## Exception Flow
- Payment cannot be matched to customer.
- Payment amount conflicts with invoice amount.
- Duplicate payment suspected.

## Postconditions
- Payment allocation record created.
- Invoice outstanding amount updated.

## Related Business Rules
- BR-BIL-004 Billing history must be auditable.
- BR-BIL-006 Payment allocation must reference payer and invoice.

## Related Decisions
- D-BIL-001 Payment allocation must be auditable.

## Evidence
- Invoice / Credit Note sample evidence
- Referral fee terms and calculation reference
- Finance workshop decision evidence
- BA consolidation

## Review Questions
- Should allocation support one payment to multiple invoices?
- How should overpayment be handled in Review Version?
