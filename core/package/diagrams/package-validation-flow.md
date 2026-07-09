---
id: VRIMS-PKG-FLOW-0071
title: Package Validation Flow
type: Flow
capability: Package
version: 0.71R
status: Business Review Draft
---

# Package Validation Flow

```text
Booking / Treatment Request
        |
        v
Identify Customer
        |
        v
Retrieve Customer Packages
        |
        v
Filter Active Packages
        |
        v
Check Treatment Eligibility
        |
        v
Check Remaining Balance
        |
        v
Multiple Valid Packages?
        |
        +-- Yes --> Select Closest Expiry Package
        |
        +-- No  --> Use Eligible Package
        |
        v
Validation Result Returned
        |
        v
Proceed to Booking Confirmation / Payment Handling
```

## Important Note
Package validation does not equal package redemption.  
Redemption occurs after completed treatment.
