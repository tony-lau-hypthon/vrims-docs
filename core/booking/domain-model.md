---
id: VRIMS-BKG-DOMAIN-001
title: Booking Domain Model
type: Domain Model
capability: Booking
version: 0.1
status: Business Review Draft
knowledge_confidence: 90%
source_sessions:
  - VRC Session 5
---

# Booking Domain Model

This document defines the business-level entities involved in Booking Management. It is not a database schema.

## Core Entities

| Entity ID | Entity | Description |
|---|---|---|
| ENT-BKG-001 | Booking | A request or confirmed appointment for a service |
| ENT-BKG-002 | Booking Item | The service item booked within a booking |
| ENT-BKG-003 | Booking Status | Current lifecycle state of a booking |
| ENT-BKG-004 | Time Slot | Scheduling unit used by the booking calendar |
| ENT-BKG-005 | Resource | Person, room or asset required to fulfil a booking |
| ENT-BKG-006 | Therapist | Treatment provider assigned to a VRC booking |
| ENT-BKG-007 | Room | Physical treatment location |
| ENT-BKG-008 | Package Entitlement | Client's available prepaid service balance |
| ENT-BKG-009 | Treatment | The delivered service resulting from a completed booking |
| ENT-BKG-010 | Notification | Reminder or confirmation sent to customer or staff |

## Key Relationships

```text
Customer / Client
    └── Booking
          ├── Booking Item
          ├── Booking Status
          ├── Assigned Therapist
          ├── Room / Resource
          ├── Package Entitlement
          └── Notification
```

## Business Notes

- A booking may require one or more resources.
- A VRC treatment booking requires therapist allocation by staff.
- A completed booking may trigger package redemption or payment settlement.
- Package validation is related to Booking but owned by Package Management.
