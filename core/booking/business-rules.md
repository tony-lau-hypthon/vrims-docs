---
id: VRIMS-BKG-RULES-001
title: Booking Business Rules
type: Business Rule Catalogue
capability: Booking
version: 0.1
status: Business Review Draft
knowledge_confidence: 95%
source_sessions:
  - VRC Session 5
---

# Booking Business Rule Catalogue

## VRC Booking Rules

### BR-BKG-001 — Booking requires staff confirmation

**Status:** Confirmed  
**Applies To:** VRC  
**Description:** VRC booking requests must be confirmed by VRC staff before they become confirmed appointments.  
**Evidence:** VRC Session 5 materials and answered open questions.  
**Impact:** Customer Portal, Staff Portal, Booking Status.

### BR-BKG-002 — Customer cannot choose therapist

**Status:** Confirmed  
**Applies To:** VRC  
**Description:** VRC client cannot choose a preferred therapist. Therapist allocation is managed by VRC staff.  
**Evidence:** Answered open question Q4.  
**Impact:** Customer Portal, Staff Portal, Therapist Scheduling.

### BR-BKG-003 — Staff assignment follows the operational roster

**Status:** Tony Confirmed  
**Applies To:** VRC  
**Description:** VRC management arranges the operational roster and determines which colleague serves a timeslot. The system records the assigned staff resource but does not determine clinical staffing policy.  
**Evidence:** Tony clarification following Session 5 review.  
**Impact:** Staff Portal, Therapist Calendar, Role Boundary.

### BR-BKG-004 — Management role can change therapist after confirmation

**Status:** Confirmed  
**Applies To:** VRC  
**Description:** Management role or above can assign or change therapist after booking confirmation.  
**Evidence:** Answered open question Q15.  
**Impact:** Security, Staff Portal, Audit.

### BR-BKG-005 — Calendar uses 30-minute scheduling slots

**Status:** Confirmed  
**Applies To:** VRC initially; candidate general booking rule  
**Description:** Booking calendar is based on 30-minute scheduling slots.  
**Evidence:** VRC booking table sample and answered open question Q6.  
**Impact:** Availability, Therapist Schedule, Room Schedule.

### BR-BKG-006 — 45-minute treatment reserves two slots on staff calendar

**Status:** Confirmed with Tony clarification  
**Applies To:** VRC  
**Description:** A 45-minute treatment reserves two consecutive 30-minute slots on the Staff Booking Calendar.  
**Rationale:** Staff scheduling uses fixed 30-minute slots.  
**Evidence:** Session 5 email and Tony confirmation.  
**Impact:** Staff Calendar, Therapist Availability, Room Availability.

### BR-BKG-007 — 60-minute treatment reserves two slots

**Status:** Confirmed  
**Applies To:** VRC  
**Description:** A 60-minute treatment reserves two consecutive 30-minute slots.  
**Evidence:** Answered open question Q6.  
**Impact:** Scheduling.

### BR-BKG-008 — 90-minute treatment reserves four slots

**Status:** Confirmed  
**Applies To:** VRC  
**Description:** A 90-minute treatment reserves four consecutive 30-minute slots.  
**Evidence:** Answered open question Q6.  
**Impact:** Scheduling.

### BR-BKG-009 — Therapist and room cannot be double-booked

**Status:** Confirmed  
**Applies To:** VRC  
**Description:** Therapist and room resources must not be double-booked.  
**Evidence:** Answered open question Q7.  
**Impact:** Resource Allocation, Availability Engine.

### BR-BKG-010 — No online reschedule for VRC client

**Status:** Confirmed  
**Applies To:** VRC  
**Description:** VRC clients cannot reschedule bookings online.  
**Evidence:** Answered open question Q1.  
**Impact:** Customer Portal, Staff Portal.

### BR-BKG-011 — No online cancellation for VRC client

**Status:** Confirmed  
**Applies To:** VRC  
**Description:** VRC clients cannot cancel bookings online.  
**Evidence:** Answered open question Q2.  
**Impact:** Customer Portal, Staff Portal.

### BR-BKG-012 — No waiting list

**Status:** Confirmed  
**Applies To:** VRC  
**Description:** VRC does not support waiting list feature.  
**Evidence:** Answered open question Q19.  
**Impact:** Booking Engine, Customer Portal.

### BR-BKG-013 — No-show does not deduct package

**Status:** Confirmed  
**Applies To:** VRC  
**Description:** A no-show booking records No-show status only; no package deduction and no penalty applies.  
**Evidence:** Answered open question Q20.  
**Impact:** Package Management, Finance, Reporting.

### BR-BKG-014 — Assessment prerequisite for package purchase

**Status:** Tony Confirmed; detailed matrix pending  
**Applies To:** VRC  
**Description:** Assessment is required before purchasing any VRC package. The required assessment type, validity and fee-waiver rules require Functional Design confirmation.  
**Evidence:** Tony clarification and Session 5 evidence.  
**Impact:** Booking, Assessment, Package, Billing.

### BR-BKG-015 — Home visit booking not supported at this moment

**Status:** Confirmed  
**Applies To:** VRC  
**Description:** Home visit booking is not supported at this moment.  
**Evidence:** Answered open question Q8.  
**Impact:** Booking Scope, Scheduling.

### BR-BKG-016 — Package with closest expiry is consumed first

**Status:** Confirmed  
**Applies To:** VRC  
**Description:** If a customer has multiple active packages, the package with the closest expiry date is consumed first.  
**Evidence:** Answered open question Q9.  
**Impact:** Booking Validation, Package Management, Billing.

---

## Conflict Review (Release-014R Merge)

The following rules were revised during the Release-014R VRC Domain Foundation merge. Existing knowledge was not silently overwritten — the changes are documented below for traceability.

### BR-BKG-003 — Therapist assignment

| | |
|---|---|
| **Existing knowledge** | "Staff assigns therapist" — Reception or authorised staff assigns therapist during booking confirmation. Status: Confirmed. |
| **New knowledge** | "Staff assignment follows the operational roster" — VRC management arranges the operational roster and determines which colleague serves a timeslot. The system records the assigned staff resource but does not determine clinical staffing policy. Status: Tony Confirmed. |
| **Recommended resolution** | Accept new version. This is a refinement, not a contradiction — it clarifies that therapist allocation is an operational roster decision by management, not a system-determined assignment. |
| **Impact** | Staff Portal, Therapist Calendar, Role Boundary. Status changes from Confirmed to Tony Confirmed. |

### BR-BKG-014 — Assessment prerequisite

| | |
|---|---|
| **Existing knowledge** | "Assessment is mandatory before treatment" — Assessment is mandatory before each treatment type. Assessment may sometimes be free of charge. Status: Confirmed. |
| **New knowledge** | "Assessment prerequisite for package purchase" — Assessment is required before purchasing any VRC package. The required assessment type, validity and fee-waiver rules require Functional Design confirmation. Status: Tony Confirmed; detailed matrix pending. |
| **Recommended resolution** | Accept new version. This is a **scope clarification**: the assessment prerequisite applies to *package purchase*, not to every individual *treatment*. The existing rule was overly broad. |
| **Impact** | Booking, Assessment, Package, Billing. Status changes from Confirmed to Tony Confirmed (detailed matrix pending). |

