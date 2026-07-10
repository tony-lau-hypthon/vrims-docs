# Wellness Centre Business Rules Summary

## Knowledge Classification

Rules below use the Release-016R knowledge model:
- **Confirmed** — supported by approved decision evidence or approved business documentation
- **Validated** — confirmed through business clarification but not yet reflected in formal decision evidence
- **Assumption** — BA interpretation awaiting validation
- **Pending Validation** — requires a business decision
- **Functional Design Required** — business intent known, system behaviour still to be designed

## Booking

- **Validated:** The Customer Portal is a web application with PWA capability for VR Resident, VRC Member and VC Member.
- **Validated:** VRC Members can request treatment bookings through the Customer Portal.
- **Validated:** Booking uses consecutive 30-minute calendar slots.
- **Validated:** A 45-minute treatment reserves two consecutive 30-minute slots; the treatment occupies 45 minutes and the remaining 15 minutes stays unavailable within the reserved window.

- **Confirmed:** Booking requires VRC staff confirmation.
- **Confirmed:** Customer cannot choose therapist.
- **Confirmed:** Customer cannot cancel or reschedule online.
- **Confirmed:** Therapist and room cannot be double-booked.
- **Confirmed:** No waiting-list feature is required.
- **Confirmed:** No-show does not deduct package entitlement or apply a penalty.
- **Validated:** Therapist allocation is managed operationally through roster planning.

## Package

- **Confirmed:** A client may hold multiple active VRC packages.
- **Confirmed:** Closest-expiry eligible package is consumed first.
- **Confirmed:** Redemption occurs after completed treatment.
- **Confirmed:** Package transaction history must be retained.
- **Validated:** Add-on items are supported.
- **Validated:** Package upgrade and downgrade are not supported.
- **Assumption:** Premium packages operate on a monthly basis.
- **Assumption:** Package validity begins on the purchase date.
- **Functional Design Required:** Define whether eligible package selection is automatic only or allows controlled staff intervention.

## Assessment

- **Validated:** Assessment is required before purchasing any VRC package.
- **Functional Design Required:** Define assessment type by service/package, validity period, reassessment trigger and fee-waiver authority.

## Product and Pricing

- **Confirmed Master Data:** Single-service purchase is supported.
- **Confirmed Master Data:** Premium Neuro Plan and Premium Exoskeleton Plan have predefined service composition, session quantity, duration, original price and package price.
- **Confirmed:** Promotion and member discount cannot be combined under the current rule.
- **Pending Validation:** Provide the full customer eligibility and discount matrix.

## Billing

- **Confirmed:** Billing is triggered by a single service, package purchase or completed package redemption.
- **Confirmed:** Credit note must reference the original invoice.
- **Confirmed:** Refund handling includes credit-note processing and package inactivation.
- **Pending Validation:** Deposit, partial-payment, instalment and accepted-payment-method rules.
- **Pending Technical Confirmation:** Final eftPay integration approach.

## Notification

- **Confirmed:** WhatsApp notification events include booking confirmation, appointment reminder, package-expiry reminder and final-session reminder.
- **Functional Design Required:** Final templates, languages, recipients and timing configuration.

---

## Conflict Review (Release-014R Merge)

This summary was restructured during the Release-014R merge. Key changes from the previous version:

| Area | Existing | New | Resolution |
|---|---|---|---|
| Knowledge classifications | Rules were unlabelled prose bullets | Rules now carry explicit classifications (Confirmed, Validated, Assumption, Pending Validation, Functional Design Required) | Accepted — enrichment, no knowledge lost |
| Booking rules | 5 rules | 7 rules — added therapist allocation (Validated) and no-waiting-list | Accepted — additive |
| Package rules | 4 rules | 8 rules — added add-on support, no upgrade/downgrade, monthly/validity assumptions | Accepted — additive with assumptions labelled |
| Assessment | "May be mandatory before treatment" | "Required before purchasing any VRC package" (Validated) | Accepted — aligns with BR-BKG-014 scope clarification |
| Product & Pricing | Not present | New section — master data, premium packages, non-combination rule | Accepted — new knowledge |
| Notification | 2 generic rules | 2 rules with WhatsApp-specific events | Accepted — enrichment |
