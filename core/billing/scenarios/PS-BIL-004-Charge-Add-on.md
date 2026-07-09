---
id: PS-BIL-004
title: Charge Add-on
capability: Billing
version: 0.101R
status: Business Review Draft
knowledge_confidence: 85%
---

# Charge Add-on

## Purpose
Generate charge for additional services.

## Trigger
Add-on confirmed.

## Preconditions
Add-on selected.

## Main Success Flow
1. Validate billable event.
2. Determine charge owner.
3. Calculate charge amount.
4. Create billing transaction.
5. Mark ready for invoice generation.

## Postconditions
Add-on charge recorded.

## Related Business Rules
- BR-BIL-001 Billing is triggered by billable business events.
- BR-BIL-003 Invoice must have an identifiable owner.
- BR-BIL-004 Billing history must be auditable.

## Open Items
- Tax calculation (future)
- Pricing configuration (functional phase)
