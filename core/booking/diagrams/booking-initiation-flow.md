---
id: VRIMS-BKG-FLOW-0031
title: Booking Initiation Flow
type: Flow
capability: Booking
version: 0.2
status: Business Review Draft
---

# Booking Initiation Flow

```text
Customer / VRC Client
        |
        v
Submit Booking Request
        |
        v
Booking Status = Pending
        |
        v
Reception Reviews Request
        |
        v
Validate Customer / Assessment Requirement
        |
        v
Validate Package Entitlement
        |
        v
Check Therapist / Room Availability
        |
        v
Ready for Release 003.2:
Therapist Assignment and Booking Confirmation
```

## Notes

- Booking confirmation is intentionally excluded from this release.
- Therapist assignment is intentionally excluded from this release.
- Package deduction does not occur during booking initiation.
