# Banking sector overlay — section1071-readiness

When the engagement scope flags banking, load this overlay alongside `references/source-anchors.md`. This is the heaviest sector overlay for §1071 readiness because depository institutions are the predominant covered-financial-institution population.

## Covered-financial-institution determination for depository institutions

- **Origination-volume counting at depositories**. The 12 CFR 1002.105 threshold under the May 2026 revised rule is **1,000 covered originations to small businesses in each of the two preceding calendar years**. Depositories typically have the operational data to count cleanly, but the count's correctness depends on the per-product covered-transaction mapping (1002.106). Common mistakes: counting all SBA originations regardless of small-business definition; counting renewals as new originations where the rule treats them differently; counting business-credit-card originations on a per-account basis where the rule's treatment of business credit cards needs careful reading [verify the credit-card treatment under the current rule text].
- **Threshold-proximity sensitivity**. A depository sitting near the 1,000-transaction line in either of the two preceding calendar years can flip CFI / not-CFI year-over-year. Run the count under both years and surface the proximity in the memo; near-threshold firms still build to the same compliance date as far-above-threshold firms because the binary determination triggers it.
- **Affiliate aggregation question**. Where the firm operates through multiple affiliated depository entities, each entity's CFI determination is its own. The rule does not aggregate at the holding-company level for the threshold count [verify under current rule]; surface this as an open question for legal where the firm's structure makes the answer non-trivial.

## Per-product covered-transaction mapping at depositories

Depositories have the broadest small-business product range. Each product needs `in / out / edge` classification with rule-cited rationale:

- **Term loans for business purposes** — typically `in` under 1002.106.
- **Lines of credit for business purposes** — typically `in`; capture the line-establishment vs. draw treatment.
- **Business credit cards** — `in` per the rule's express coverage; the data-point capture for business credit cards differs operationally from term-loan capture (no formal "application date" in the same shape; verify the application-method and application-recipient capture for the credit-card flow).
- **SBA 7(a) and SBA 504 loans** — `in` where the borrower meets the small-business definition; the data already collected for SBA reporting overlaps with §1071 but does not satisfy §1071 (different schema, different demographic-collection requirements, different firewall posture). Map; do not assume SBA capture is §1071 capture.
- **Commercial real-estate loans for small-business borrowers** — `in` where the borrower is a small business under the rule's definition; HMDA-reportable transactions are excluded under 1002.106(b)(1) and the boundary between HMDA-reportable and §1071-reportable for owner-occupied commercial real estate needs careful per-loan classification.
- **Equipment finance and equipment leases** — `in` where the lease meets the credit-extension definition; capital-lease vs. operating-lease treatment is the operative distinction [verify].
- **Letters of credit and trade finance** — `edge`; surface as an open question for legal. The boundary between letter-of-credit issuance and a covered credit transaction is non-trivial.
- **Demand-deposit-account-secured lines** — `in` where the secured line is a covered credit transaction.
- **Floor-plan financing** — `in` for dealer floor plans where the dealer meets the small-business definition.
- **Agricultural credit** — `in` where the borrower meets the small-business definition; the agricultural-credit population overlaps with the rule but agricultural-specific exemptions in other regimes do not extend to §1071.
- **Intra-group lending and shareholder loans** — `edge`; surface for legal.

## Firewall design at depositories

The firewall under 1002.108 reads against the depository's role-based access controls in the LOS, the customer-360 / relationship-management view, and any data warehouse that aggregates lending and deposit data. The most material 1002.108 gap at depositories is rarely in the LOS itself; the LOS vendor builds the firewall capability into the product. The gap is usually in the customer-360 view where:

- **Self-reported demographics from the deposit side** (race, ethnicity, sex captured at account opening for HMDA cross-product or other firm-internal purposes) are aggregated into the customer-360 record and exposed to underwriters who pull the customer-360 record during credit decisioning. The §1071 firewall is breached if the underwriter sees the demographic from the deposit-side feed even though the LOS-side firewall is intact.
- **Cross-product reporting** that pulls demographic data into a firm-internal dashboard accessible to underwriters.
- **Manager / executive overrides** that grant temporary access for case review without a documented exception process.

Depositories also need to pin the firewall-trained-personnel design: who is trained, what training, what cadence, what attestation. The rule's notice provision for permitted-exception cases needs a documented procedure (script, log, attestation per case).

## Recordkeeping and the broader records-retention schedule

Depositories typically have an enterprise records-retention schedule managed by records management or general counsel. The §1071 three-year retention from the date of submission needs to be reflected explicitly in the schedule, with the records identified and the disposition policy named. A depository running on a generic "lending records — seven years" rubric needs the §1071-specific retention added to the schedule.

## FIG conformance, validation engine, and submission channel

Depositories typically have an existing regulatory-reporting pipeline (HMDA LAR submission, Call Report, FFIEC reporting). The §1071 submission flows through the CFPB's filing channel [verify current channel and authentication mechanics]; the validation-engine choice (CFPB-provided, vendor-built, or in-house) and the test-submission plan should land before the compliance-date go-live. A depository assuming the HMDA pipeline serves §1071 misses the schema differences and the firewall implications for the analytics environment.

## Output-template additions for banking

- CFI determination section carries the per-affiliate count where the firm operates through multiple affiliated depositories.
- Product mapping table includes the SBA / HMDA boundary rows explicitly.
- Firewall section calls out the customer-360 / relationship-management view as a standing review row.
- Recordkeeping section calls out the integration with the enterprise records-retention schedule.
- FIG-readiness section names the existing regulatory-reporting pipeline and the analytics-environment firewall posture.

## Common pitfalls in banking §1071 readiness

- Treating SBA reporting as §1071 readiness. Different schema, different demographic-collection design, different firewall posture.
- Assuming the LOS vendor's firewall capability is the firm's firewall control. The vendor builds the capability; the firm operates the control across the customer-360 and analytics environments.
- Counting business-credit-card originations using a per-transaction definition where the rule expects per-account [verify under current rule text].
- Missing the HMDA / §1071 boundary for owner-occupied commercial real estate.
- Pinning the compliance date from a stale source (the original 2023 final-rule dates, or an outdated CFPB compliance-date-table snapshot). The dates have moved; pin from the current CFPB compliance-resources page at the time of drafting.
- Relying on the existing enterprise records-retention schedule without an explicit §1071 row; "covered by the lending-records retention rule" is not the same as named retention.
