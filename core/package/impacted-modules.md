---
id: VRIMS-PKG-IMPACT-R
title: Package Impacted Modules
type: Impact Analysis
capability: Package
version: 1.0R
status: Business Review Draft
---

# Package Impacted Modules

| Module / Capability | Impact |
|---|---|
| Wellness Centre (VRC) | Package validation, treatment entitlement, redemption after treatment |
| Booking Management | Requires package validation before confirmation where applicable |
| Billing & Finance | Determines whether to charge package redemption or single-session billing |
| Customer Portal | May show package balance, entitlement and expiry |
| Staff Portal | Staff reviews package during booking and treatment handling |
| Reporting | Package usage, expired package, redemption history |
| Resident Services | May reuse package entitlement logic later |

## Impact Notes
Package Management is a shared core capability. Module documents should reference this capability instead of duplicating package rules.
