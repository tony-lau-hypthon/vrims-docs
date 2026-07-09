---
id: VRIMS-BKG-SCENARIO-CATALOGUE
title: Booking Scenario Catalogue
type: Scenario Catalogue
capability: Booking
version: 0.5R
status: Business Review Draft
---

# Booking Scenario Catalogue

| Scenario ID | Scenario | Stage | Primary Actor | Status |
|---|---|---|---|---|
| BS-BKG-001 | Customer Requests Booking | Initiation | Customer | Business Review Draft |
| BS-BKG-002 | Reception Reviews Booking | Initiation | Reception | Business Review Draft |
| BS-BKG-003 | Validate Package | Initiation | System / Reception | Business Review Draft |
| BS-BKG-004 | Check Resource Availability | Initiation | System / Reception | Business Review Draft |
| BS-BKG-005 | Assign Therapist | Confirmation | Reception | Business Review Draft |
| BS-BKG-006 | Confirm Booking | Confirmation | Reception | Business Review Draft |
| BS-BKG-007 | Send Booking Reminder | Confirmation | System | Business Review Draft |
| BS-BKG-008 | Check-in Client | Execution | Reception | Business Review Draft |
| BS-BKG-009 | Complete Treatment | Execution | Therapist / Reception | Business Review Draft |
| BS-BKG-010 | No-show Handling | Execution | Reception | Business Review Draft |
| BS-BKG-011 | Cancel Booking | Maintenance | Reception | Business Review Draft |
| BS-BKG-012 | Reschedule Booking | Maintenance | Reception | Business Review Draft |
| BS-BKG-013 | Booking Closure | Maintenance | System / Reception | Business Review Draft |

## Scenario Relationship
```text
BS-BKG-001 Customer Requests Booking
        ↓
BS-BKG-002 Reception Reviews Booking
        ↓
BS-BKG-003 Validate Package
        ↓
BS-BKG-004 Check Resource Availability
        ↓
BS-BKG-005 Assign Therapist
        ↓
BS-BKG-006 Confirm Booking
        ↓
BS-BKG-007 Send Booking Reminder
        ↓
BS-BKG-008 Check-in Client
        ↓
BS-BKG-009 Complete Treatment
        ↓
BS-BKG-013 Booking Closure
```

## Alternative Paths
```text
Confirmed Booking → Cancel Booking
Confirmed Booking → Reschedule Booking
Confirmed Booking → No-show Handling
```
