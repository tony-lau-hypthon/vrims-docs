---
id: PS-BIL-002
title: Charge Package Purchase
capability: Billing
version: 0.101R
status: Business Review Draft
knowledge_confidence: 85%
---

# Charge Package Purchase

## Purpose
Generate charge for package purchase.

## Trigger
Package purchase confirmed.

## Preconditions
Package selected.

## Main Success Flow
1. Validate billable event.
2. Determine charge owner.
3. Calculate charge amount.
4. Create billing transaction.
5. Mark ready for invoice generation.

## Postconditions
Package purchase transaction recorded.

## Related Business Rules
- BR-BIL-001 Billing is triggered by billable business events.
- BR-BIL-003 Invoice must have an identifiable owner.
- BR-BIL-004 Billing history must be auditable.

## Open Items
- Tax calculation (future)
- Pricing configuration (functional phase)
