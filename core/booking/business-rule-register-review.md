---
id: VRIMS-BKG-BR-REGISTER-R
title: Booking Business Rule Register Review
type: Business Rule Register
capability: Booking
version: 0.6R
status: Business Review Draft
---

# Booking Business Rule Register Review

| Rule ID | Rule | Status | Applies To |
|---|---|---|---|
| BR-BKG-001 | Booking requires staff confirmation | Confirmed | VRC |
| BR-BKG-002 | Customer cannot choose therapist | Confirmed | VRC |
| BR-BKG-003 | Staff assignment follows the operational roster | Validated | VRC |
| BR-BKG-004 | Management role can change therapist after confirmation | Confirmed | VRC |
| BR-BKG-005 | Calendar uses 30-minute scheduling slots | Confirmed | VRC initially |
| BR-BKG-006 | 45-minute treatment reserves two 30-minute slots; 45-minute treatment plus 15-minute unavailable remainder | Validated | VRC |
| BR-BKG-007 | 60-minute treatment reserves two slots | Confirmed | VRC |
| BR-BKG-008 | 90-minute treatment reserves four slots | Confirmed | VRC |
| BR-BKG-009 | Therapist and room cannot be double-booked | Confirmed | VRC |
| BR-BKG-010 | Customer cannot reschedule online | Confirmed | VRC |
| BR-BKG-011 | Customer cannot cancel online | Confirmed | VRC |
| BR-BKG-012 | No waiting list | Confirmed | VRC |
| BR-BKG-013 | No-show does not deduct package | Confirmed | VRC |
| BR-BKG-014 | Assessment is required before purchasing a VRC package | Validated | VRC |
| BR-BKG-015 | Home visit booking not supported at this moment | Confirmed | VRC |
| BR-BKG-016 | Package with closest expiry is consumed first | Confirmed | VRC |
| BR-BKG-017 | VRC Member can request treatment booking through Customer Portal | Validated | VRC |
| BR-BKG-018 | Customer Portal supports VR Resident, VRC Member and VC Member | Validated | Cross-domain |

## Review Notes
This register is business-facing and intentionally avoids Odoo field design, permission configuration and implementation logic.
