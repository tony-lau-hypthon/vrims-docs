---
id: VRIMS-BKG-001
title: Booking Management
type: Core Capability
capability: Booking
version: 0.1
status: Business Review Draft
owner: BA
reviewer: Tony
knowledge_confidence: 95%
source_sessions:
  - VRC Session 5
related_modules:
  - Wellness Centre (VRC)
  - Customer Portal
  - Staff Portal
  - Resident Services
  - Ventria Club
last_updated: 2026-07-09
---

# Booking Management

## Purpose

Booking Management is a core VRIMS capability used to manage service appointment requests, confirmation, resource allocation, attendance, completion, cancellation and reporting.

This capability is shared across multiple VRIMS business areas, including:

- Wellness Centre (VRC)
- VR Resident services
- Ventria Club member services
- Customer Portal
- Staff Portal

## Design Principle

Booking Management owns common booking concepts such as booking status, availability, confirmation, resource allocation and scheduling conflict detection.

Module-specific rules, such as VRC therapist assignment rules, should be defined as variants under this capability instead of duplicated in module documents.

## Current Scope

The first version is based primarily on VRC Session 5 evidence and covers:

- Booking request creation
- Staff confirmation
- Therapist assignment
- Room and therapist availability control
- Booking status lifecycle
- No-show handling
- Cancellation / reschedule restrictions for VRC
- Appointment reminders
- Package validation integration
- Reporting impact

## Out of Scope for Current Version

- Resident-specific booking rules
- Ventria Club class or activity booking rules
- Full payment gateway integration
- Online reschedule
- Online cancellation
- Waiting list
- Recurring bookings

These may be added after related workshops are confirmed.

## Knowledge Confidence

| Area | Confidence |
|---|---:|
| VRC Booking Flow | 95% |
| VRC Booking Rules | 95% |
| Therapist Assignment | 95% |
| Slot Scheduling | 90% |
| Notification Triggers | 90% |
| Reporting Details | 75% |
| Payment Gateway | 20% |
