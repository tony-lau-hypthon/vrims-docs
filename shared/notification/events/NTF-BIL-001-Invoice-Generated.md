---
id: NTF-BIL-001
title: Invoice Generated
type: Notification Event
capability: Notification
version: 0.91R
status: Business Review Draft
category: Billing
default_channel: Email
recipient: Customer / Finance
source_capability: Billing
knowledge_confidence: 70%
---

# NTF-BIL-001 — Invoice Generated

## Purpose
Notify customer or finance when invoice is generated.

## Trigger
Invoice is created.

## Recipient
Customer / Finance

## Suggested Channel
Email

## Business Content Summary
Invoice number, amount, due date and payment instruction.

## Source Capability
Billing

## Related Modules
- Wellness Centre
- Customer Portal
- Staff Portal

## Business Rules
- BR-NTF-001 — Notification is triggered by business events.
- BR-NTF-004 — Notification templates are centrally managed.

## Open Items
- Final template wording TBD.
- Language requirement TBD.
- Retry / failure handling TBD.
