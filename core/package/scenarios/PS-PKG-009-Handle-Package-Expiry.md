---
id: PS-PKG-009
title: Handle Package Expiry
capability: Package
version: 0.73R
status: Business Review Draft
---

# Handle Package Expiry

## Purpose
Automatically expire eligible packages after their validity period.

## Trigger
Business event requiring lifecycle management.

## Preconditions
- Package exists.
- Customer identified.
- Staff has appropriate authority where required.

## Main Flow
1. Identify package.
2. Validate current lifecycle status.
3. Apply lifecycle action.
4. Record audit history.
5. Notify affected users if required.

## Business Rules
- Lifecycle actions must be auditable.
- Expired packages cannot be redeemed.
- Freeze prevents redemption until resumed.

## Open Questions
- Confirm approval matrix.
- Confirm customer notification method.
