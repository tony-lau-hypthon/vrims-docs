---
id: VRIMS-WC-001-CAPABILITY-MAP
title: Wellness Centre Capability Reference Map
type: Capability Map
module: Wellness Centre
version: 1.1R
status: Domain Foundation Verified
visibility:
  executive: true
  business: true
  functional: true
---

# Capability Reference Map

## Wellness Centre Capability Composition

```text
Wellness Centre (VRC)
  ├── Customer Registration
  ├── Assessment Management
  │     └── Refer to core/assessment
  ├── Booking Management
  │     └── Refer to core/booking
  ├── Treatment Management
  ├── Package Management
  │     └── Refer to core/package
  ├── Billing & Finance
  │     └── Refer to core/billing
  ├── Promotion & Eligibility
  ├── Notification
  │     └── Refer to shared/notification
  └── Reporting
```

## Capability Ownership

| Capability | Source | Status |
|---|---|---|
| Booking Management | `core/booking/` | Review-ready |
| Package Management | `core/package/` | Review-ready foundation |
| Assessment Management | `core/assessment/` | Review-ready foundation |
| Billing & Finance | `core/billing/` | Review-ready foundation |
| Notification | `shared/notification/` | Review-ready foundation |
| Reporting | Module-specific + future shared capability | Deferred |
| Promotion / Eligibility | Wellness Centre module | Pending VR matrix |

## Design Principle

VRC-specific commercial and operational rules remain under this module. Generic lifecycle, booking, billing, assessment and notification behaviour belongs to reusable capabilities.
