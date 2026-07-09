---
id: VRIMS-BKG-ACCEPTANCE-001
title: Booking Acceptance Criteria
type: Acceptance Criteria
capability: Booking
version: 0.1
status: Draft
knowledge_confidence: 85%
source_sessions:
  - VRC Session 5
---

# Booking Acceptance Criteria

## AC-BKG-001 — Create Pending Booking

**Related Rules:** BR-BKG-001  
Given a VRC client submits a booking request  
When the request is recorded  
Then the booking status shall be Pending.

## AC-BKG-002 — Staff Confirms Booking

**Related Rules:** BR-BKG-001, BR-BKG-003  
Given a booking is Pending  
When authorised VRC staff validates and confirms the booking  
Then the booking status shall become Confirmed.

## AC-BKG-003 — Customer Cannot Choose Therapist

**Related Rules:** BR-BKG-002  
Given a VRC client creates a booking request  
When the client provides booking preference  
Then therapist selection shall not be available to the client.

## AC-BKG-004 — Prevent Therapist Double Booking

**Related Rules:** BR-BKG-009  
Given a therapist is already assigned to a confirmed booking  
When staff attempts to assign the same therapist to another booking at overlapping time  
Then the system shall prevent double booking.

## AC-BKG-005 — No-show Handling

**Related Rules:** BR-BKG-013  
Given a confirmed booking is marked as No-show  
When the status is saved  
Then no package deduction shall be created.

## AC-BKG-006 — Closest-expiry Package Consumption

**Related Rules:** BR-BKG-016  
Given a client has multiple active packages for the selected treatment  
When treatment is completed and redemption is required  
Then the package with the closest expiry date shall be consumed first.
