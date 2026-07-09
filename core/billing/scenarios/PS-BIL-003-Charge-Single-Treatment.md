---
id: PS-BIL-003
title: Charge Single Treatment
capability: Billing
version: 0.101R
status: Business Review Draft
knowledge_confidence: 85%
---

# Charge Single Treatment

## Purpose
Generate charge for non-package treatment.

## Trigger
Treatment completed without package.

## Preconditions
Treatment billable.

## Main Success Flow
1. Validate billable event.
2. Determine charge owner.
3. Calculate charge amount.
4. Create billing transaction.
5. Mark ready for invoice generation.

## Postconditions
Treatment charge recorded.

## Related Business Rules
- BR-BIL-001 Billing is triggered by billable business events.
- BR-BIL-003 Invoice must have an identifiable owner.
- BR-BIL-004 Billing history must be auditable.

## Open Items
- Tax calculation (future)
- Pricing configuration (functional phase)
