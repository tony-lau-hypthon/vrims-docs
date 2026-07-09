# Billing Adjustment & Settlement Flow

```text
Invoice Generated
        |
        v
Payment Pending
        |
        +--> Payment Received
        |         |
        |         v
        |   Allocate Payment
        |         |
        |         v
        |   Invoice Paid / Partially Paid
        |
        +--> Outstanding Balance
        |         |
        |         +--> Payment Reminder
        |         +--> Write-off
        |
        +--> Credit Note
        |         |
        |         v
        |   Adjust Invoice Balance
        |
        +--> Refund
                  |
                  v
            Refund Record Created
```
