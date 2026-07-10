---
id: VRIMS-WC-001-PACKAGE-PRICING
title: Wellness Centre Package and Pricing
type: Master Data Summary
module: Wellness Centre
version: 1.0R
status: Domain Foundation Verified
source_sessions:
  - Session 5
---

# Package and Pricing

## Pricing Structures

### Single Service

A customer may purchase and be invoiced for an individual VRC service without buying a package.

### Package

A VRC package may define:

- included service items
- number of sessions
- session duration
- original price
- package price
- discount condition
- validity / expiry

## Premium Neuro Plan

Current master-data interpretation:

| Item | Entitlement |
|---|---|
| Home-based PT / OT | 1 × 60 minutes |
| Home-based Rehabilitation Trainer | 3 × 60 minutes |
| Centre-based Comprehensive Rehabilitation | 8 × 90 minutes |
| Original Price | HK$25,880 |
| Package Price | HK$20,704 |
| Stated Discount | 20% |
| Combination Rule | Cannot combine with other benefits |

## Premium Exoskeleton Plan

Current master-data interpretation:

| Item | Entitlement |
|---|---|
| Centre-based PT / OT Comprehensive Rehabilitation | 8 × 90 minutes |
| Exoskeleton Training | 8 × 90 minutes |
| Original Price | HK$43,040 |
| Package Price | HK$34,432 |
| Stated Discount | 20% |
| Combination Rule | Cannot combine with other benefits |

## Example Single Service

| Service | Duration | Listed Price |
|---|---:|---:|
| Exoskeleton Training | 90 minutes | From HK$3,300 |

## Current Business Interpretation

- Add-on items are supported.
- Upgrade and downgrade are not supported.
- Premium packages are expected to be monthly.
- Validity is expected to begin at purchase.
- Expired entitlement cannot be used.

## Status Warning

Monthly duration and validity-start rules remain design assumptions pending Functional Design or VR confirmation.
