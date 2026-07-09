---
id: NTF-BKG-003
title: Booking Cancelled
type: Notification Event
capability: Notification
version: 0.91R
status: Business Review Draft
category: Booking
default_channel: WhatsApp / Email
recipient: Customer / VRC Client
source_capability: Booking
knowledge_confidence: 80%
---

# NTF-BKG-003 — Booking Cancelled

## Purpose
Notify customer that booking has been cancelled.

## Trigger
Booking status changes to Cancelled.

## Recipient
Customer / VRC Client

## Suggested Channel
WhatsApp / Email

## Business Content Summary
Cancellation notice and follow-up instruction.

## Source Capability
Booking

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
