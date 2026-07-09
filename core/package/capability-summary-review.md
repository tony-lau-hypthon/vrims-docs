---
id: VRIMS-PKG-001-SUMMARY-R
title: Package Management Capability Summary Review
type: Capability Summary
capability: Package
version: 1.0R
status: Business Review Draft
visibility:
  executive: true
  business: true
  functional: true
---

# Package Management Capability Summary

## Business Objective
Package Management ensures that prepaid service entitlement is correctly validated, consumed, tracked and governed across VRIMS modules.

## Core Responsibilities
- Maintain customer package entitlement.
- Validate package usability before service confirmation.
- Select appropriate package when multiple valid packages exist.
- Redeem package entitlement after service completion.
- Prevent deduction on no-show.
- Maintain auditable package transaction history.
- Support lifecycle governance such as expiry, freeze, resume and extension.

## Relationship with Booking
Booking uses Package Management to:
- validate entitlement before confirmation;
- identify eligible package;
- trigger redemption after treatment completion.

Booking does not own package rules. Package rules remain under Package Management.

## Relationship with Billing
Billing may depend on Package Management to determine whether:
- package entitlement should be consumed;
- single-session billing is needed;
- refund / credit note handling is required.

Detailed finance configuration remains out of scope for Review Version.
