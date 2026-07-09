# Notification Event Flow

```text
Source Business Capability
        |
        v
Business Event Occurs
        |
        v
Notification Event ID Raised
        |
        v
Recipient Determined
        |
        v
Template Selected
        |
        v
Channel Selected
        |
        v
Notification Sent
        |
        v
Delivery Logged
```

## Notes
- Source capability owns the business trigger.
- Notification capability owns event definition, channel and template governance.
- Technical provider integration is out of scope for Review Version.
