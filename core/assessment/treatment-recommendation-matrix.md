---
id: VRIMS-ASM-TREATMENT-RECOMMENDATION-R
title: Treatment Recommendation Matrix
capability: Assessment
version: 0.82R
status: Business Review Draft
knowledge_confidence: 85%
---

# Treatment Recommendation Matrix

| Assessment Result | Recommendation Output | Impact |
|---|---|---|
| Treatment suitable | Recommended treatment type | Booking may proceed |
| Package suitable | Recommended package / session count | Package sales or validation may proceed |
| Assessment only | No immediate treatment | Booking blocked until recommendation exists |
| Follow-up required | Follow-up assessment | Treatment booking deferred |

## Business Principle
Treatment booking should be aligned with completed assessment and recommendation where assessment is mandatory.

## Review Questions
- Are recommendation outputs always required before treatment booking?
- Can Reception override recommendation for operational reasons?
- Are recommendations linked to package selection?
