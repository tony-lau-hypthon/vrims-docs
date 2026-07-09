---
id: VRIMS-BIL-001-REVIEW-PACK
title: Billing Management Review Pack
type: Capability Review Pack
capability: Billing
version: 1.0R
status: Business Review Draft
knowledge_confidence: 80%
---

# Billing Management Review Pack

## Purpose
Billing Management defines how billable events create charges, invoices, payment records, adjustments and settlement records.

## Review Position
This is an R Version document. It confirms business behaviour and finance-facing concepts. It is not yet an accounting configuration, tax configuration, or payment gateway technical design.

## Capability Coverage
1. Billing foundation
2. Charge processing
3. Invoice generation
4. Payment allocation
5. Payment received
6. Outstanding balance
7. Credit note
8. Refund
9. Write-off
10. Referral fee settlement

## Key Business Principles
- Billing is triggered by billable business events.
- Invoice must have an identifiable owner.
- Billing history must be auditable.
- Credit note must reference original invoice.
- Payment allocation must reference payer and invoice.
- Referral fee settlement is finance-controlled.
