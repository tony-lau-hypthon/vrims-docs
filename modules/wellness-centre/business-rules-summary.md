# Wellness Centre Business Rules Summary

## Knowledge Classification

Rules below are labelled as:
- **Confirmed** — supported by decision evidence or explicit user confirmation
- **Tony Confirmed** — accepted as current BA understanding
- **Design Assumption** — suitable for drafting but not yet business-confirmed
- **Pending VR** — requires VR decision
- **Functional Design Required** — business intent known, system behaviour still to be designed

## Booking

- **Confirmed:** Booking requires VRC staff confirmation.
- **Confirmed:** Customer cannot choose therapist.
- **Confirmed:** Customer cannot cancel or reschedule online.
- **Confirmed:** Therapist and room cannot be double-booked.
- **Confirmed:** No waiting-list feature is required.
- **Confirmed:** No-show does not deduct package entitlement or apply a penalty.
- **Tony Confirmed:** Therapist allocation is managed operationally through roster planning.

## Package

- **Confirmed:** A client may hold multiple active VRC packages.
- **Confirmed:** Closest-expiry eligible package is consumed first.
- **Confirmed:** Redemption occurs after completed treatment.
- **Confirmed:** Package transaction history must be retained.
- **Tony Confirmed:** Add-on items are supported.
- **Tony Confirmed:** Package upgrade and downgrade are not supported.
- **Design Assumption:** Premium packages operate on a monthly basis.
- **Design Assumption:** Package validity begins on the purchase date.
- **Functional Design Required:** Define whether eligible package selection is automatic only or allows controlled staff intervention.

## Assessment

- **Tony Confirmed:** Assessment is required before purchasing any VRC package.
- **Functional Design Required:** Define assessment type by service/package, validity period, reassessment trigger and fee-waiver authority.

## Product and Pricing

- **Confirmed Master Data:** Single-service purchase is supported.
- **Confirmed Master Data:** Premium Neuro Plan and Premium Exoskeleton Plan have predefined service composition, session quantity, duration, original price and package price.
- **Confirmed:** Promotion and member discount cannot be combined under the current rule.
- **Pending VR:** Provide the full customer eligibility and discount matrix.

## Billing

- **Confirmed:** Billing is triggered by a single service, package purchase or completed package redemption.
- **Confirmed:** Credit note must reference the original invoice.
- **Confirmed:** Refund handling includes credit-note processing and package inactivation.
- **Pending VR:** Deposit, partial-payment, instalment and accepted-payment-method rules.
- **Pending Technical Confirmation:** Final eftPay integration approach.

## Notification

- **Confirmed:** WhatsApp notification events include booking confirmation, appointment reminder, package-expiry reminder and final-session reminder.
- **Functional Design Required:** Final templates, languages, recipients and timing configuration.

---

## Conflict Review (Release-014R Merge)

This summary was restructured during the Release-014R merge. Key changes from the previous version:

| Area | Existing | New | Resolution |
|---|---|---|---|
| Knowledge classifications | Rules were unlabelled prose bullets | Rules now carry explicit classifications (Confirmed, Tony Confirmed, Design Assumption, Pending VR, Functional Design Required) | Accepted — enrichment, no knowledge lost |
| Booking rules | 5 rules | 7 rules — added therapist allocation (Tony Confirmed) and no-waiting-list | Accepted — additive |
| Package rules | 4 rules | 8 rules — added add-on support, no upgrade/downgrade, monthly/validity assumptions | Accepted — additive with assumptions labelled |
| Assessment | "May be mandatory before treatment" | "Required before purchasing any VRC package" (Tony Confirmed) | Accepted — aligns with BR-BKG-014 scope clarification |
| Product & Pricing | Not present | New section — master data, premium packages, non-combination rule | Accepted — new knowledge |
| Notification | 2 generic rules | 2 rules with WhatsApp-specific events | Accepted — enrichment |

