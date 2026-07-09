---
id: PS-BIL-005
title: Create Manual Charge
capability: Billing
version: 0.101R
status: Business Review Draft
knowledge_confidence: 85%
---

# Create Manual Charge

## Purpose
Allow authorised staff to create manual charge.

## Trigger
Staff requests manual billing.

## Preconditions
Authorisation available.

## Main Success Flow
1. Validate billable event.
2. Determine charge owner.
3. Calculate charge amount.
4. Create billing transaction.
5. Mark ready for invoice generation.

## Postconditions
Manual charge recorded.

## Related Business Rules
- BR-BIL-001 Billing is triggered by billable business events.
- BR-BIL-003 Invoice must have an identifiable owner.
- BR-BIL-004 Billing history must be auditable.

## Open Items
- Tax calculation (future)
- Pricing configuration (functional phase)
