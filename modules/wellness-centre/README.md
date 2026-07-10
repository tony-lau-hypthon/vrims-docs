---
id: VRIMS-WC-001
title: Wellness Centre (VRC)
type: Module
module: Wellness Centre
version: 1.2R
status: Domain Foundation Verified
owner: BA
reviewer: Tony
knowledge_confidence: 95%
source_sessions:
  - Session 5
last_updated: 2026-07-10
---

# Wellness Centre (VRC)

This module documents the VRC Wellness Centre business domain.

## Domain Boundary

VRC is a separate commercial rehabilitation and wellness domain from VR Resident care-package operations.

The nine standard and three special care plans belong to VR Resident care packages. They must not be treated as VRC therapy packages.

## Current Customer-Facing Scope

- The Customer Portal is a web application with PWA capability.
- Supported portal user groups include:
  - VR Resident
  - VRC Member
  - VC Member
- VRC Members can request treatment bookings through the Customer Portal.
- Online booking and Customer Portal booking are current scope, not future scope.

## Core Dependencies

- Booking Management
- Package Management
- Assessment Management
- Billing & Finance
- Notification
- Customer Portal

## Module Documents

- `business-scope.md`
- `customer-journey-review.md`
- `business-rules-summary.md`
- `product-catalogue.md`
- `package-and-pricing.md`
- `registration-and-assessment.md`
- `capability-reference-map.md`
- `open-items.md`
- `review-readiness.md`
- `executive-review.md`

## Design Principle

Module documents define VRC-specific business context and reference reusable capability documents instead of duplicating generic capability behaviour.
