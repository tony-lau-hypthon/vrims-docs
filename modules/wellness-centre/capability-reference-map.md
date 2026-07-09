---
id: VRIMS-WC-001-CAPABILITY-MAP
title: Wellness Centre Capability Reference Map
type: Capability Map
module: Wellness Centre
version: 0.6R
status: Business Review Draft
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
  ├── Booking Management
  │     └── Refer to core/booking
  ├── Treatment Management
  ├── Package Management
  ├── Billing & Finance
  ├── Promotion & Membership
  ├── Notification
  └── Reporting
```

## Capability Ownership

| Capability | Source | Status |
|---|---|---|
| Booking Management | `core/booking/` | Review-ready |
| Package Management | Future core capability | Partial |
| Assessment Management | Future core capability | Partial |
| Billing & Finance | Future / Finance session | Partial |
| Notification | Shared capability | Partial |
| Reporting | Module-specific + shared | Partial |

## Design Principle
VRC-specific module documents should reference core capability documents instead of duplicating the full business logic.
