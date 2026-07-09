---
id: NTF-ASM-001
title: Assessment Created
type: Notification Event
capability: Notification
version: 0.91R
status: Business Review Draft
category: Assessment
default_channel: System / Email
recipient: Reception / Therapist
source_capability: Assessment
knowledge_confidence: 75%
---

# NTF-ASM-001 — Assessment Created

## Purpose
Notify relevant staff that assessment record has been created.

## Trigger
Assessment record is created.

## Recipient
Reception / Therapist

## Suggested Channel
System / Email

## Business Content Summary
Customer, assessment type and planned follow-up.

## Source Capability
Assessment

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
