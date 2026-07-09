---
id: VRIMS-BKG-DECISIONS-001
title: Booking Decision Register
type: Decision Register
capability: Booking
version: 0.1
status: Business Review Draft
knowledge_confidence: 95%
source_sessions:
  - VRC Session 5
---

# Booking Decision Register

## D-0001 — VRC staff confirms booking

**Status:** Confirmed  
**Decision:** VRC booking requests require staff confirmation before becoming confirmed appointments.  
**Rationale:** Operational staff must validate availability and assign therapist.  
**Impacted Areas:** Booking Status, Staff Portal, Customer Portal.

## D-0002 — VRC client cannot choose therapist

**Status:** Confirmed  
**Decision:** Therapist assignment is controlled by VRC staff, not customer.  
**Rationale:** Ensures operational control and avoids incorrect therapist selection.  
**Impacted Areas:** Customer Portal, Staff Portal, Therapist Schedule.

## D-0003 — 45-minute VRC treatment reserves two 30-minute staff-calendar slots

**Status:** Confirmed  
**Decision:** A 45-minute VRC treatment reserves two consecutive 30-minute slots on the Staff Booking Calendar.  
**Rationale:** Staff scheduling calendar uses fixed 30-minute slots.  
**Impacted Areas:** Scheduling, Staff Calendar, Resource Allocation.

## D-0004 — VRC has no waiting list

**Status:** Confirmed  
**Decision:** Waiting list is not required for VRC booking.  
**Impacted Areas:** Booking Engine, Customer Portal.

## D-0005 — No-show causes no package deduction

**Status:** Confirmed  
**Decision:** No-show is recorded as a booking status only. No penalty and no package deduction applies.  
**Impacted Areas:** Package Management, Finance, Reporting.

## D-0006 — Multiple packages consume closest expiry first

**Status:** Confirmed  
**Decision:** When multiple active packages exist, consume the one with closest expiry date first.  
**Impacted Areas:** Package Management, Booking Validation, Billing.
