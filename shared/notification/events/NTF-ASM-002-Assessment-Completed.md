---
id: NTF-ASM-002
title: Assessment Completed
type: Notification Event
capability: Notification
version: 0.91R
status: Business Review Draft
category: Assessment
default_channel: System / Email
recipient: Reception / Customer where applicable
source_capability: Assessment
knowledge_confidence: 75%
---

# NTF-ASM-002 — Assessment Completed

## Purpose
Notify that assessment is completed and recommendation may be available.

## Trigger
Assessment status changes to Completed.

## Recipient
Reception / Customer where applicable

## Suggested Channel
System / Email

## Business Content Summary
Assessment completion and next step recommendation.

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
