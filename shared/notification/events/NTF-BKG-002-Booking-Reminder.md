---
id: NTF-BKG-002
title: Booking Reminder
type: Notification Event
capability: Notification
version: 0.91R
status: Business Review Draft
category: Booking
default_channel: WhatsApp
recipient: Customer / VRC Client
source_capability: Booking
knowledge_confidence: 90%
---

# NTF-BKG-002 — Booking Reminder

## Purpose
Remind customer before confirmed appointment.

## Trigger
Configured reminder time before appointment.

## Recipient
Customer / VRC Client

## Suggested Channel
WhatsApp

## Business Content Summary
Appointment reminder, date/time and contact instruction.

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
