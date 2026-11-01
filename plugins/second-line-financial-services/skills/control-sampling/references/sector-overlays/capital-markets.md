# Capital-markets sector overlay — control-sampling

Loaded when `scope.sector_overlay_set` includes `capital-markets` or when the test addresses FINRA, SEC, MSRB, or CFTC rules for broker-dealers, investment advisers, registered funds, or futures commission merchants. Supplements `references/source-anchors.md` with capital-markets-specific population, stratification, and tolerable-rate conventions.

## Population definition conventions capital-markets examiners expect

FINRA examiners, SEC OCIE/EXAMS reviewers, and adviser internal auditors carry conventions beyond the general sampling baseline:

- **Populations are defined by trading-day, account-day, or transaction-event.** Trades executed during period (broker-dealer best execution, suitability, Reg BI), accounts open during period (KYC, suitability profile freshness), customer communications sent during period (FINRA Rule 2210 communications), supervisory reviews completed during period (FINRA Rule 3110).
- **Recordkeeping populations under SEC 17a-4 / FINRA 4511 are large.** The memo defines the population in items the sample can draw from (records subject to a particular retention requirement) and reconciles to the books-and-records system control totals. WORM-storage populations carry the storage-system extract as the source of truth.
- **Adviser populations under Advisers Act Rule 206(4)-7 follow the firm's annual-review scope.** The annual review's risk-prioritisation drives the populations the sample targets across the year.

## Capital-markets-supervisory anchors (load by reference; do not restate)

- **FINRA Rule 3120 — Supervisory Control System** [verify subsection labels]. The annual-report-on-supervisory-controls testing sits inside this frame. https://www.finra.org/rules-guidance/rulebooks/finra-rules/3120 .
- **FINRA Rule 3130 — Annual Certification of Compliance and Supervisory Processes** [verify subsection labels]. CEO certification supported by CCO testing of supervisory processes; sampling-memo discipline drives the CCO's certification basis. https://www.finra.org/rules-guidance/rulebooks/finra-rules/3130 .
- **FINRA Rule 3110 — Supervision** [verify subsection labels for required tests and verifications]. Supervisory-reviews populations sit here. https://www.finra.org/rules-guidance/rulebooks/finra-rules/3110 .
- **FINRA Rule 2111 — Suitability** and **SEC Regulation Best Interest (17 CFR §240.15l-1)** [verify subsection labels for the Care, Conflict, Disclosure, and Compliance Obligations]. Suitability and Reg BI sampling pulls recommendations and customer profiles. https://www.finra.org/rules-guidance/rulebooks/finra-rules/2111 ; https://www.ecfr.gov/current/title-17/chapter-II/part-240/section-240.15l-1 .
- **SEC Rule 17a-4 (17 CFR §240.17a-4)** and **FINRA Rule 4511 — General Requirements (Books and Records)** [verify subsection labels]. Recordkeeping populations and retention requirements drive the population-completeness basis for capital-markets sampling. https://www.ecfr.gov/current/title-17/chapter-II/part-240/section-240.17a-4 ; https://www.finra.org/rules-guidance/rulebooks/finra-rules/4511 .
- **Investment Advisers Act Rule 206(4)-7** [verify subsection labels for the annual-review documentation expectation and the testing-program component]. https://www.ecfr.gov/current/title-17/chapter-II/part-275/section-275.206(4)-7 .
- **SEC Rule 38a-1 (17 CFR §270.38a-1)** for registered investment companies — fund compliance program rule [verify subsection labels]. https://www.ecfr.gov/current/title-17/chapter-II/part-270/section-270.38a-1 .

## Capital-markets-control-area sampling notes

### Suitability and Reg BI testing

- Sampling conventions: suitability and Reg BI testing samples recommendations made in the period with stratification by product complexity (mutual fund, ETF, structured product, options, alternative, fixed income), customer type (retail, institutional, accredited, high-net-worth), and registered representative experience. Care Obligation testing reads the recommendation against the customer profile; Conflict and Disclosure Obligation testing reads the supervisory documentation. Tolerable rates for high-complexity-with-retail-customer combinations are typically lower than firm baseline because customer-impact framing concentrates risk.

### Trade-execution and best-execution testing

- Sampling conventions: best-execution testing samples trades executed in the period with stratification by venue, order type (market, limit, marketable limit), security type, and trade size. The population is trades subject to best-execution review per the firm's policy; the source of truth is the order-management or execution-management system extract.

### Books-and-records testing

- Sampling conventions: 17a-4 / 4511 testing samples records subject to specific retention requirements with stratification by record category. WORM-storage testing reads the storage-system extract by sample with reperformance against the retention metadata. Tolerable rates for WORM-failure populations are typically zero per firm policy because the regulatory consequence is absolute.

### Supervisory-review testing (3110)

- Sampling conventions: supervisory-review testing samples reviews completed in the period with stratification by review type (electronic communication review, trade exception review, customer-account review), reviewing principal, and reviewed-population subset. The population is reviews-the-firm-was-required-to-perform per the firm's WSPs; missing-review tests use the inverse population.

### Communications-with-public testing (2210)

- Sampling conventions: 2210 testing samples communications sent in the period with stratification by communication type (retail, correspondence, institutional), distribution channel, and pre-use-approval status. Pre-use-approved communications carry a different population from filed-with-FINRA communications.

### Adviser annual-review (206(4)-7) testing

- Sampling conventions: the annual-review scope dictates which control populations are sampled across the year. Custody-rule (Rule 206(4)-2) testing samples client accounts with stratification by custodian, account type, and asset count. Books-and-records testing under Rule 204-2 mirrors the broker-dealer 17a-4 conventions.

### Fund 38a-1 testing

- Sampling conventions: fund compliance-program testing samples board reports, sub-adviser oversight evidence, valuation determinations, and proxy-voting records by sample. The population follows the fund's compliance-program scope under Rule 38a-1 [verify subsection].

## Audience and tone

A sampling memo drafted with an upcoming FINRA examination in mind reads heavier on the FINRA rule citations, the supervisory-control frame (3120/3130), and the WSP-derived population definitions. A memo drafted with an upcoming SEC EXAMS visit in mind reads heavier on the Rule 206(4)-7 annual-review frame, the books-and-records retention matrices, and the customer-impact framing for retail products. A memo drafted for fund-board reporting reads heavier on the 38a-1 compliance-program frame and the custodian-by-custodian breakdown for custody-rule testing.
