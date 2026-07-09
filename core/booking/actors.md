---
id: VRIMS-BKG-ACTORS-001
title: Booking Actors
type: Actor Catalogue
capability: Booking
version: 0.1
status: Business Review Draft
knowledge_confidence: 95%
source_sessions:
  - VRC Session 5
---

# Booking Actors

| Actor ID | Actor | Role in Booking |
|---|---|---|
| ACT-BKG-001 | Customer / Client | Requests or attends booking |
| ACT-BKG-002 | VRC Client | VRC service recipient |
| ACT-BKG-003 | Reception / Clinic Staff | Confirms booking and assigns therapist |
| ACT-BKG-004 | Therapist | Provides treatment and views assigned bookings |
| ACT-BKG-005 | Management Role | Can assign or change therapist after confirmation |
| ACT-BKG-006 | Finance | Handles billing, package redemption and credit note impact |
| ACT-BKG-007 | System | Validates availability, status and notification triggers |
| ACT-BKG-008 | Customer Portal | Allows customer-facing booking request and status view |
| ACT-BKG-009 | Staff Portal | Allows operational booking management |

## VRC Actor Rules

- VRC client cannot choose therapist.
- VRC client cannot reschedule online.
- VRC client cannot cancel online.
- VRC staff manage booking confirmation.
- Management role or above can assign/change therapist after confirmation.
