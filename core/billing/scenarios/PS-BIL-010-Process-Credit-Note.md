---
id: PS-BIL-010
title: Process Credit Note
capability: Billing
version: 0.102R
status: Business Review Draft
knowledge_confidence: 90%
related_capabilities:
  - Package
  - Booking
  - Notification
impacted_modules:
  - Wellness Centre
  - Finance
  - Customer Portal
---

# Process Credit Note

## Purpose
Create a credit note to adjust or reverse a previously issued invoice.

## Business Context
Credit notes are required when invoice adjustment is needed due to correction, cancellation or business-approved reduction.

## Trigger
Finance determines that an issued invoice requires adjustment.

## Preconditions
- Original invoice exists.
- Adjustment reason is known.
- Authorised user performs the action.

## Main Success Flow
1. Finance opens original invoice.
2. Finance selects credit note action.
3. Finance enters reason and amount.
4. Credit note references original invoice.
5. Credit note is issued / recorded.
6. Invoice balance is adjusted.

## Alternative Flow
- Credit note may partially adjust invoice.
- Credit note may fully offset invoice.

## Exception Flow
- Original invoice cannot be found.
- Credit amount exceeds allowable amount.
- Approval missing.

## Postconditions
- Credit note record created.
- Original invoice linkage retained.
- Audit trail recorded.

## Related Business Rules
- BR-BIL-005 Credit notes must reference the original invoice.
- BR-BIL-004 Billing history must be auditable.

## Related Decisions
- D-BIL-004 Credit note must reference original invoice.

## Evidence
- Invoice / Credit Note sample evidence
- Referral fee terms and calculation reference
- Finance workshop decision evidence
- BA consolidation

## Review Questions
- Which roles can approve credit note?
- Should customer receive credit note notification?
