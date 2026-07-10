---
id: VRIMS-WC-001-JOURNEY-R
title: Wellness Centre Customer Journey Review
type: Customer Journey
module: Wellness Centre
version: 1.1R
status: Domain Foundation Verified
visibility:
  executive: true
  business: true
  functional: true
---

# Wellness Centre Customer Journey

## Main Journey

```text
Enquiry
  ↓
VRC Client Registration
  ↓
Assessment
  ↓
Treatment Recommendation
  ↓
Purchase
  ├── Single Service
  └── VRC Package
  ↓
Booking Request
  ↓
VRC Staff Review and Confirmation
  ↓
Treatment
  ↓
Package Redemption or Single-Service Billing
  ↓
Invoice / Credit Note
  ↓
Accounting and Follow-up
```

## Business Understanding

- Assessment is required before purchasing a VRC package under Tony's current business understanding.
- A customer may purchase a single service without buying a package.
- Customers do not choose the therapist.
- Management arranges rosters and assigns the colleague for a timeslot.
- Package redemption occurs after completed treatment.
- No-show records a status only under the current confirmed rule; no package session is deducted.
- VRC commercial services and packages are separate from VR Resident care packages.

---

## Conflict Review (Release-014R Merge)

The customer journey was revised during the Release-014R merge. Key changes:

| Area | Existing | New | Resolution |
|---|---|---|---|
| Journey stages | Assessment → Treatment Recommendation → Package/Payment Arrangement → Booking | Assessment → Treatment Recommendation → **Purchase (Single Service / VRC Package)** → Booking | Accepted — adds explicit purchase decision point between recommendation and booking |
| Assessment position | Assessed before treatment | Assessed before **package purchase** (Tony Confirmed) | Accepted — aligns with BR-BKG-014 scope clarification |
| Business Understanding | 3 items | 7 items — adds roster management, no-show clarity, VRC/VR boundary | Accepted — enrichment |
| Review Notes | Referenced VRIMS-BKG-001 | Replaced with Business Understanding section | Accepted — more self-contained |

