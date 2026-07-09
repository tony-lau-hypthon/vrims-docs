---
id: BS-BKG-004
title: Check Resource Availability
type: Business Scenario
capability: Booking
version: 0.2
status: Business Review Draft
business_value: High
complexity: High
knowledge_confidence: 90%
source_sessions:
  - VRC Session 5 Workshop
  - VRC Session 5 Email
  - VRC Session 5 Answered Open Questions
  - Tony Review
applies_to:
  - VRC
future_variants:
  - VR Resident
  - VC Member
---

# BS-BKG-004 — Check Resource Availability

## 1. Purpose

Define how the booking process checks availability of therapist, room and time slots before confirmation.

## 2. Business Context

VRC booking must prevent double-booking of therapist and room resources. Scheduling is based on 30-minute slots. For VRC, therapist assignment is staff-controlled and will be completed in a later confirmation scenario.

## 3. Primary Actors

- Reception
- Booking System
- Therapist
- Room / Resource

## 4. Trigger

Reception proceeds from package/customer validation to resource availability check.

## 5. Preconditions

- Booking request exists.
- Requested service and preferred time/date are known.
- Therapist roster and room availability are available.
- Required duration or scheduling slot requirement is known.

## 6. Main Success Flow

1. System identifies the requested date and preferred time window.
2. System calculates required scheduling slots based on treatment duration.
3. System checks therapist availability for the required slots.
4. System checks room/resource availability for the required slots.
5. System excludes resources already assigned to overlapping confirmed bookings.
6. System returns available resource/time options to Reception.
7. Reception proceeds to therapist assignment and booking confirmation in Release 003.2.

## 7. Alternative Flow

- If preferred time is unavailable, Reception may propose another slot.
- If first available logic is used, system may search the earliest available slot.
- If the requested treatment is not yet supported online, Reception may handle manually.

## 8. Exception Flow

- If no therapist is available, booking cannot be confirmed at the requested time.
- If no room is available, booking cannot be confirmed at the requested time.
- If home visit booking is requested, VRC currently does not support home visit booking at this moment.

## 9. Postconditions

- Resource availability result is known.
- No therapist is formally assigned in this scenario.
- Booking remains Pending until staff confirms.

## 10. Related Business Rules

- BR-BKG-005 — Calendar uses 30-minute scheduling slots
- BR-BKG-006 — 45-minute treatment reserves two slots on staff calendar
- BR-BKG-007 — 60-minute treatment reserves two slots
- BR-BKG-008 — 90-minute treatment reserves four slots
- BR-BKG-009 — Therapist and room cannot be double-booked
- BR-BKG-015 — Home visit booking not supported at this moment

## 11. Related Decisions

- D-0003 — 45-minute VRC treatment reserves two 30-minute staff-calendar slots

## 12. Acceptance Criteria References

- AC-BKG-004 — Prevent Therapist Double Booking

## 13. Evidence

- VRC booking table sample
- VRC Session 5 Answered Open Questions Q6, Q7, Q8
- Tony clarification on 45-minute booking display

## 14. BA Notes

The current confirmed 45-minute rule applies to Staff Booking Calendar reservation. Customer-side display is not treated as a confirmed business rule unless separately defined later.

## 15. Review Questions

- Should resource availability check happen before or after therapist assignment?
- Are rooms always required for VRC treatment bookings?
- Should public holidays or therapist leave be treated as unavailable resources in this capability?
