---
id: VRIMS-NTF-EVENT-LIBRARY-R
title: Notification Event Library
type: Event Library
capability: Notification
version: 0.91R
status: Business Review Draft
knowledge_confidence: 85%
visibility:
  executive: false
  business: true
  functional: true
  technical: false
---

# Notification Event Library

## Purpose
The Notification Event Library defines reusable business notification events across VRIMS.

Business modules should reference notification event IDs instead of defining channels and templates separately.

## Event Categories

| Category | Prefix | Example |
|---|---|---|
| Booking | NTF-BKG | Booking confirmation / reminder |
| Assessment | NTF-ASM | Assessment created / completed |
| Package | NTF-PKG | Package expiry / balance |
| Billing | NTF-BIL | Invoice / payment |
| Portal | NTF-PORTAL | Account / login |
| Staff Task | NTF-TASK | Internal operational task |

## Design Principle
Notification is a shared capability. Source modules trigger notification events; Notification capability manages event definition, channel, recipient and template ownership.

## Current Review Position
This is Review Version. It confirms event requirements, not final provider configuration.

## VRC Event Set

| Event | Business Trigger | Current Channel |
|---|---|---|
| NTF-BKG-001 | VRC booking confirmed | WhatsApp |
| NTF-BKG-002 | Appointment reminder | WhatsApp |
| NTF-PKG-001 | Package expiry approaching | WhatsApp |
| NTF-PKG-003 | Final package session | WhatsApp |

Separate VR and VRC WhatsApp Business Accounts are technically possible. Final account ownership, approved templates, languages, recipients and timing require Functional Design confirmation.
