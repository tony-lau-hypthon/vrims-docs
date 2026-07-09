---
id: NTF-BKG-001
title: Booking Confirmed
type: Notification Event
capability: Notification
version: 0.91R
status: Business Review Draft
category: Booking
default_channel: WhatsApp / Email
recipient: Customer / VRC Client
source_capability: Booking
knowledge_confidence: 90%
---

# NTF-BKG-001 — Booking Confirmed

## Purpose
Notify customer that booking has been confirmed.

## Trigger
Booking status changes to Confirmed.

## Recipient
Customer / VRC Client

## Suggested Channel
WhatsApp / Email

## Business Content Summary
Appointment date, time, service, location and reminder of attendance.

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
