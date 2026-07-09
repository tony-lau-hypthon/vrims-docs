---
id: BS-BKG-001
title: Customer Requests Booking
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

# BS-BKG-001 — Customer Requests Booking

## 1. Purpose

Define how a customer or VRC client initiates a booking request before staff review and confirmation.

## 2. Business Context

For VRC, the customer-facing booking flow is request-based rather than self-confirmation. The customer may provide preferred booking information, but final confirmation and therapist assignment remain under VRC staff control.

## 3. Primary Actors

- Customer / VRC Client
- Customer Portal
- Booking System
- Reception

## 4. Trigger

Customer intends to book a VRC treatment, assessment or service appointment.

## 5. Preconditions

- Customer has sufficient basic profile information to identify the client.
- Required service/treatment is available for booking.
- If the service requires prior assessment, assessment requirement must be handled before treatment booking confirmation.
- Customer Portal must not expose therapist selection for VRC booking.

## 6. Main Success Flow

1. Customer opens the booking request function.
2. Customer selects service or treatment type.
3. Customer provides preferred date and preferred time, or selects first available option if presented.
4. Customer may provide remarks or special needs.
5. Customer submits the booking request.
6. System creates a booking request with status `Pending`.
7. Booking request becomes available for Reception review.
8. Customer is informed that the booking is pending staff confirmation.

## 7. Alternative Flow

- If customer is not yet a VRC client, the flow may require registration before booking request can proceed.
- If the selected service requires assessment, the system or staff should guide the customer to assessment booking first.
- If no preferred slot is entered, staff may follow up manually.

## 8. Exception Flow

- If required customer identity cannot be matched, booking request should not be confirmed until staff resolves the client record.
- If service is inactive, booking request should not proceed.
- If online booking is unavailable, reception may create booking manually on behalf of customer.

## 9. Postconditions

- A Pending booking request exists.
- No therapist has been assigned by customer.
- No package deduction has occurred.
- No booking confirmation has been issued yet.

## 10. Related Business Rules

- BR-BKG-001 — Booking requires staff confirmation
- BR-BKG-002 — Customer cannot choose therapist
- BR-BKG-010 — No online reschedule for VRC client
- BR-BKG-011 — No online cancellation for VRC client

## 11. Related Decisions

- D-0001 — VRC staff confirms booking
- D-0002 — VRC client cannot choose therapist

## 12. Acceptance Criteria References

- AC-BKG-001 — Create Pending Booking
- AC-BKG-003 — Customer Cannot Choose Therapist

## 13. Evidence

- VRC Session 5 Workshop
- VRC Session 5 Email
- VRC Session 5 Answered Open Questions Q1, Q2, Q4
- Tony Review confirmation

## 14. BA Notes

This scenario only covers request creation. Staff confirmation, therapist assignment and reminder notification are covered in later scenarios/releases.

## 15. Review Questions

- Is `Pending` the correct initial status for customer-created booking requests?
- Should registration be mandatory before customer can submit booking request?
- Should customer see first available slots, or only submit preferred date/time?
