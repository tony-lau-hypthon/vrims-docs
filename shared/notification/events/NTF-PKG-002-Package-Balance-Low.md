---
id: NTF-PKG-002
title: Package Balance Low
type: Notification Event
capability: Notification
version: 0.91R
status: Business Review Draft
category: Package
default_channel: System / Email
recipient: Customer / Staff
source_capability: Package
knowledge_confidence: 70%
---

# NTF-PKG-002 — Package Balance Low

## Purpose
Notify when package balance is low.

## Trigger
Remaining entitlement falls below business-defined threshold.

## Recipient
Customer / Staff

## Suggested Channel
System / Email

## Business Content Summary
Remaining balance and renewal suggestion.

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
