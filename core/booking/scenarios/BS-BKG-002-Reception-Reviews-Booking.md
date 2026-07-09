---
id: BS-BKG-002
title: Reception Reviews Booking
type: Business Scenario
capability: Booking
version: 0.2
status: Business Review Draft
business_value: High
complexity: Medium
knowledge_confidence: 95%
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

# BS-BKG-002 — Reception Reviews Booking

## 1. Purpose

Define how Reception reviews a Pending booking request before package and resource validation.

## 2. Business Context

VRC booking is staff-controlled. Reception acts as the operational gatekeeper to ensure booking details are valid before assigning therapist and confirming the appointment.

## 3. Primary Actors

- Reception
- Customer / VRC Client
- Booking System

## 4. Trigger

A Pending booking request is created by customer or by staff.

## 5. Preconditions

- Booking request exists with status `Pending`.
- Customer / client record is identifiable.
- Requested service type is known.

## 6. Main Success Flow

1. Reception opens the Pending booking queue.
2. Reception selects a booking request.
3. Reception verifies customer identity and contact information.
4. Reception reviews requested service, preferred date/time and remarks.
5. Reception checks whether assessment is required or already completed.
6. Reception proceeds to package validation if the booking is package-based.
7. Reception proceeds to resource availability check.
8. Reception prepares the booking for therapist assignment and confirmation.

## 7. Alternative Flow

- If customer details are incomplete, Reception updates or requests missing information.
- If assessment is mandatory but missing, Reception redirects the booking to assessment handling.
- If the customer request is unclear, Reception contacts customer before proceeding.

## 8. Exception Flow

- If customer is not eligible for the selected service, the booking should not be confirmed.
- If the requested service is not available, Reception should cancel or revise the request.
- If customer cannot be contacted, booking remains Pending or is cancelled according to operation policy.

## 9. Postconditions

- Booking remains Pending until all required validation is completed.
- Reception has enough information to proceed to package/resource validation.
- No therapist assignment occurs in this scenario.

## 10. Related Business Rules

- BR-BKG-001 — Booking requires staff confirmation
- BR-BKG-003 — Staff assigns therapist
- BR-BKG-014 — Assessment is mandatory before treatment

## 11. Related Decisions

- D-0001 — VRC staff confirms booking

## 12. Acceptance Criteria References

- AC-BKG-002 — Staff Confirms Booking (later stage)
- Additional acceptance criteria to be expanded in Release 004

## 13. Evidence

- VRC Session 5 Workshop
- VRC Session 5 Answered Open Questions Q17
- Tony Review

## 14. BA Notes

This scenario represents operational review, not final confirmation. Therapist assignment is deliberately kept in Release 003.2.

## 15. Review Questions

- Should Reception be the only role that reviews Pending bookings?
- Should Pending bookings have ageing / follow-up alerts?
- Should assessment missing condition automatically block confirmation?
