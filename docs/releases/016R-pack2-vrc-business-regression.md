---
id: VRIMS-REL-016R-P2
title: Release-016R Pack 2 — VRC Business Regression
type: Release Summary
version: 1.0
status: Ready for Merge
owner: BA
---

# Release-016R Pack 2 — VRC Business Regression

## Objective

Synchronise the canonical repository with validated VRC business clarifications identified during Brain Regression.

## Knowledge Changes

- Customer Portal is a web application with PWA capability.
- Current portal user groups are VR Resident, VRC Member and VC Member.
- VRC Member can submit treatment booking requests through Customer Portal.
- Online booking and Customer Portal booking are current scope.
- VRC Member is an existing user type; future-membership questions are obsolete.
- Booking calendar uses 30-minute slots.
- A 45-minute treatment reserves two consecutive 30-minute slots.
- The remaining 15 minutes stays unavailable within the reserved window.
- Add-on support, no upgrade/downgrade, operational therapist assignment and package-purchase assessment prerequisite use `Validated` status where touched.

## Business Impact

Clarifies current portal and booking scope. No technical design is introduced.

## Regression Risk

Medium-low. Existing restrictions on online cancellation and online rescheduling are preserved and must not be inferred from online booking support.
