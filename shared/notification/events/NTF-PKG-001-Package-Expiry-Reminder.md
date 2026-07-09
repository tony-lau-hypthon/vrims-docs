---
id: NTF-PKG-001
title: Package Expiry Reminder
type: Notification Event
capability: Notification
version: 0.91R
status: Business Review Draft
category: Package
default_channel: Email / WhatsApp
recipient: Customer
source_capability: Package
knowledge_confidence: 70%
---

# NTF-PKG-001 — Package Expiry Reminder

## Purpose
Remind customer before package expiry.

## Trigger
Package is approaching expiry threshold.

## Recipient
Customer

## Suggested Channel
Email / WhatsApp

## Business Content Summary
Package name, expiry date and suggested action.

## Source Capability
Package

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
