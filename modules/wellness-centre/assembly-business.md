---
id: VRIMS-WC-001-ASSEMBLY-R
title: Wellness Centre Business Review Assembly
type: Module Assembly
module: Wellness Centre
version: 0.6R
status: Business Review Draft
knowledge_confidence: 90%
source_capabilities:
  - VRIMS-BKG-001
source_sessions:
  - VRC Session 5
visibility:
  executive: true
  business: true
  functional: true
  technical: false
---

# Wellness Centre Business Review Assembly

## Purpose
This document assembles the Wellness Centre (VRC) Business Review package from reusable VRIMS capabilities and VRC-specific business knowledge.

## Assembly Principle
The Wellness Centre module should not duplicate core capability logic. Instead, it references reusable capabilities such as Booking Management and adds VRC-specific business context.

## Current Assembly Sources
| Source | Purpose | Status |
|---|---|---|
| `core/booking/` | Booking Management capability | Review-ready |
| `modules/wellness-centre/` | VRC module-specific context | In progress |
| Session 5 Evidence | VRC workshop and follow-up decisions | Ingested |

## Output Documents
This assembly can be rendered by GLM into:

1. Executive Review — short management version
2. Business Review — VR user review / sign-off version
3. Functional Review — Hopkins configuration input, after capability details are expanded

## Current Recommendation
Render the **Business Review** version first for Tony review before preparing VR sign-off version.
