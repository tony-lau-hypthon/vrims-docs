---
id: VRIMS-BKG-NOTIFICATIONS-001
title: Booking Notifications
type: Notification Matrix
capability: Booking
version: 0.1
status: Business Review Draft
knowledge_confidence: 90%
source_sessions:
  - VRC Session 5
---

# Booking Notifications

## VRC Notification Triggers

| Notification ID | Trigger | Recipient | Channel | Timing | Status |
|---|---|---|---|---|---|
| NTF-BKG-001 | Booking made and confirmed | Client | WhatsApp | Upon confirmation | Confirmed |
| NTF-BKG-002 | Appointment reminder | Client | WhatsApp | One day before booking | Confirmed |

## Template Source

WhatsApp templates are referenced from:

- `whatsapp-messages-sample-1.png`
- `whatsapp-messages-sample-2.png`

Located in VRC Session 5 Email attachment folder.

## Notes

- Exact message wording should be controlled by approved WhatsApp templates.
- Notification failure handling is not yet defined.
