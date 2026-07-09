---
id: VRIMS-NTF-001-REVIEW-PACK
title: Notification Capability Review Pack
type: Capability Review Pack
capability: Notification
version: 1.0R
status: Business Review Draft
knowledge_confidence: 85%
source_releases:
  - 009R
  - 009.1R
visibility:
  executive: true
  business: true
  functional: true
  technical: false
---

# Notification Capability Review Pack

## Purpose
This Review Pack consolidates Notification as a reusable shared VRIMS capability.

Notification defines how business events from Booking, Assessment, Package, Billing and Portal modules trigger messages to customers, staff or management users.

## Review Position
This is an **R Version** document.

It confirms business notification events and high-level channel expectations. It does not define technical provider configuration.

## Key Principles
- Notification is triggered by business events.
- Source capabilities own business triggers.
- Notification owns event catalogue, recipient, channel and template governance.
- Final template wording is handled separately.
- Failed notification should be logged.
