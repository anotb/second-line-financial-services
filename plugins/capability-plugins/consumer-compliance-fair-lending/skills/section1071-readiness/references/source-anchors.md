# Source anchors — section1071-readiness

The named, dated regulatory and supervisory sources this skill anchors to. SKILL.md cites this file by path and does not restate excerpts. Sector-specific and cross-cutting anchors live in the corresponding overlay files. Firm-specific anchors belong in plugin-level `references/firm-overlay.md` (consumed when present).

`[verify ...]` markers are deliberate, not omissions. The Section 1071 compliance-date schedule has been moved by court order and the CFPB's response; pin the currently effective date before drafting and re-pin if it moves again.

## Statutory frame

- **Equal Credit Opportunity Act, Section 1071 (15 U.S.C. §1691c-2)**, added by §1071 of the Dodd-Frank Wall Street Reform and Consumer Protection Act (Pub. L. 111-203). The statutory authority for the small-business-lending data-collection and reporting obligation. Source: https://www.law.cornell.edu/uscode/text/15/1691c-2 .

## Primary frame — CFPB Section 1071 final rule

- **Small Business Lending under the Equal Credit Opportunity Act (Regulation B)**. CFPB final rule, published 88 Fed. Reg. 35150 (May 31, 2023), with adoption date March 30, 2023; codified as Subpart B of Regulation B at **12 CFR 1002.101 through 12 CFR 1002.114**. Rule landing page: https://www.consumerfinance.gov/rules-policy/final-rules/small-business-lending-under-the-equal-credit-opportunity-act-regulation-b/ .

- **12 CFR 1002.103 — Definitions**. Sets the operative definitions for *covered financial institution*, *covered application*, *covered credit transaction*, *covered originations*, *small business*, and the related terms the rest of Subpart B reads from. Read 1002.103 first; the rest of the rule cascades from these definitions.

- **12 CFR 1002.104 — Covered applications**. Defines what counts as a covered application, including the treatment of inquiries, prequalifications, withdrawn applications, incomplete applications, and reevaluations of existing accounts. Source: https://www.ecfr.gov/current/title-12/chapter-X/part-1002/subpart-B/section-1002.104 .

- **12 CFR 1002.105 — Covered financial institutions**. Sets the **origination thresholds** for covered-financial-institution determination: a financial institution that originated at least the threshold number of *covered originations* to small businesses in each of the two preceding calendar years. The threshold and tier mechanics drive the compliance-date assignment under 1002.114. Methodology for counting (covered-transaction definition under 1002.106 applied per product) is the engagement's first analytic step. Source: https://www.ecfr.gov/current/title-12/chapter-X/part-1002/subpart-B/section-1002.105 .

- **12 CFR 1002.106 — Covered credit transactions**. Defines the in-scope credit transactions: term loans, lines of credit, business credit cards, merchant cash advances and other sales-based financing, and similar products extended to a small business for business purposes. Specifies the exclusions (consumer-purpose credit, HMDA-reportable transactions, securities transactions, and similar). Per-product covered-transaction mapping reads against this section. Source: https://www.ecfr.gov/current/title-12/chapter-X/part-1002/subpart-B/section-1002.106 .

- **12 CFR 1002.107 — Compilation of reportable data**. The canonical data-point list. The skill's readiness matrix has one row per data point in this section. The data points include unique identifier, application date, application method, application recipient, credit type (product type, guarantee, loan term), credit purpose, amount applied for, amount approved or originated, action taken, action taken date, denial reasons, pricing information (interest rate; total origination charges; broker fees; initial annual charges; additional cost for merchant cash advance and other sales-based financing; prepayment penalty), census tract (principal address), gross annual revenue, NAICS code, number of workers, time in business, number of principal owners, minority-owned business status, women-owned business status, LGBTQI+-owned business status, and ethnicity / race / sex of principal owners. Verify the complete list and the exact subsection labels (`1002.107(a)(1)` through the trailing subsections) against the current rule text at each engagement; the CFPB has published technical amendments and the structured output's `data_points[].rule_ref` must match. Source: https://www.consumerfinance.gov/rules-policy/regulations/1002/107/ .

- **12 CFR 1002.108 — Limitations on the use and access of certain information** (the **firewall**). Restricts access by underwriters and others involved in determining whether to extend credit from accessing the applicant-demographic information collected under 1002.107, with limited exceptions where the firm cannot reasonably avoid such access (and with a notice provision in those cases). The firewall design is the operative privacy-adjacent control for §1071 data; the firm's role-based access controls, exception process, attestation map, and firewall-trained personnel design read against this section. Source: https://www.ecfr.gov/current/title-12/chapter-X/part-1002/subpart-B/section-1002.108 .

- **12 CFR 1002.109 — Reporting of data to the Bureau**. Annual reporting; modified version of submitted data is published by the Bureau. The modified-data publication has re-identification implications for low-volume small-business lending in identifiable geographies; surface in the privacy overlay. Source: https://www.ecfr.gov/current/title-12/chapter-X/part-1002/subpart-B/section-1002.109 .

- **12 CFR 1002.110 — Recordkeeping**. **Three-year retention** from the date of submission. The retention obligation reads against the firm's broader records-retention schedule. Source: https://www.ecfr.gov/current/title-12/chapter-X/part-1002/subpart-B/section-1002.110 .

- **12 CFR 1002.111 — Enforcement**. ECOA enforcement provisions apply. The skill carries this as a pointer for the readiness memo's escalation section, not as a primary anchor.

- **12 CFR 1002.112 — Bona fide errors and safe harbors**. The firm's documented bona-fide-error policy and procedure for amending submitted data should sit in place before go-live. The safe-harbor mechanics are narrow; the practitioner's reading of the section is itself an open legal question worth flagging for counsel. Source: https://www.ecfr.gov/current/title-12/chapter-X/part-1002/subpart-B/section-1002.112 .

- **12 CFR 1002.114 — Compliance dates**. Sets the **tier-based compliance schedule** with three tiers keyed to the firm's covered-origination volume:
  - **Tier 1** — high-volume covered originators.
  - **Tier 2** — moderate-volume covered originators.
  - **Tier 3** — lower-volume covered originators (above the 1002.105 threshold).
  
  The compliance dates have been **moved by court order and bureau response** following the CTA-style litigation history. The original final-rule dates were superseded by the CFPB's revised compliance dates published in 2024 in response to the *Texas Bankers Association v. CFPB* litigation and subsequent court orders [verify current effectiveness and tier dates against the most recent CFPB compliance-date table]. The CFPB's compliance-date table is the operative source: https://www.consumerfinance.gov/compliance/compliance-resources/small-business-lending-resources/small-business-lending-collection-and-reporting-requirements/ . Pin the current Tier 1, Tier 2, and Tier 3 effective dates from that page at the time of drafting and re-pin if they move again. The structured output's `cfi_determination.compliance_date` field carries the date as a sourced citation, not a bare value.

## CFPB Filing Instructions Guide and submission mechanics

- **CFPB Filing Instructions Guide (FIG) for small business lending data**, the operative companion to 12 CFR 1002.107 and 1002.109 [verify current edition and version number at the time of drafting]. The FIG sets the file-format specification, data-validation rules, and submission-channel mechanics for the annual filing. The matrix's `reporting_readiness.fig_edition` field records which edition the firm is building against; FIG version changes between cycles trigger a mapping refresh. CFPB filing-resources page: https://www.consumerfinance.gov/data-research/small-business-lending/filing-instructions-guide/ [verify URL].

- **CFPB Section 1071 Sample Data Collection Form** [verify CFPB-published version and date]. The CFPB-published sample form for applicant-demographic data collection. Firms that adopt the sample form's structure get implementation-aid value; firms that build their own form must still meet the rule's required disclosures and refusal-handling. Surface a row in `demographic_collection_mechanics` that names which form is in use.

- **CFPB Section 1071 small-business-lending compliance resources page** — https://www.consumerfinance.gov/compliance/compliance-resources/small-business-lending-resources/ — the operative landing page for the CFPB's compliance materials. The compliance-date table on this page is the source of truth for the currently effective dates and is updated when the dates move.

## Litigation status and current-state caveat

- **Texas Bankers Association v. CFPB**, S.D. Tex. (2023–2024), and related cases. The CTA-style litigation cluster has produced injunctions and partial stays affecting the §1071 final rule's compliance dates. The CFPB has issued revised compliance dates in response. The current state has changed multiple times since the rule's March 2023 adoption [verify current effectiveness and tier dates and any active injunctions at the time of drafting]. The structured output marks every date-bearing field with the sourced citation; the readiness memo's executive summary leads with the current-state caveat where the date is material to the firm's go-live planning.

- **Subsequent CFPB amendments and statements** — the CFPB has issued procedural and substantive amendments since adoption. Verify the consolidated rule text at https://www.consumerfinance.gov/rules-policy/regulations/1002/ and any open Federal Register notices at https://www.federalregister.gov/agencies/consumer-financial-protection-bureau before drafting; do not assume the rule text is static.

## Fair-lending intersection

- **Interagency Fair Lending Examination Procedures** (FFIEC, current edition) [verify edition]. Sets the supervisory expectation for fair-lending testing on lending data. The §1071 dataset becomes the canonical small-business-lending fair-lending dataset once it exists, and is read by `fair-lending-test-plan` for the testing design. The readiness skill's responsibility is to confirm the dataset is fit for that downstream use; the test-design responsibility lives with `fair-lending-test-plan`. Source: https://www.ffiec.gov/exam/ .

- **CFPB Fair Lending Reports** (annual) [verify current edition]. The CFPB's annual fair-lending posture; the small-business-lending sub-section gains weight once §1071 reporting is in flight.

## Cross-skill anchors inside this plugin

- `fair-lending-test-plan` — downstream consumer of the §1071 dataset; this skill's data-point matrix is the readiness contract for the fair-lending testing pipeline.
- `adverse-action-review` — adjacent obligation; small-business adverse-action notices remain governed by Reg B 1002.9 and FCRA §615 (where applicable). §1071 does not change adverse-action obligations; this skill's scope is data collection and reporting, not adverse-action notification.
- `complaint-theme-analysis`, `udaap-risk-review`, `marketing-claim-review` — separate but adjacent surfaces; the firm's small-business complaint themes, UDAAP exposure on small-business products, and small-business marketing reads are independent of §1071 readiness.

## Plugin-level shared references

Also consult, when present in the plugin:

- `references/source-map.md` — plugin-wide named-source map.
- `references/policy-control-library.md` — plugin-wide policy-and-control library, including the data-collection control, the firewall control, and the regulatory-reporting control.
- `references/review-gates.md` — named human-review gates and confidence-label definitions.

## Firm overlays

A firm using this skill in production adds firm-specific detail in plugin-level `references/firm-overlay.md`: the firm's own product-to-1002.106 mapping table, the named owners per data point, the LOS vendor, the firewall system, the FIG-validation engine, and the compliance committee that signs off on submission readiness. The skill consumes that file when present. Firm overlays do not modify the public anchors above.

## Verification posture summary

The skill marks four classes of citation with `[verify]`:

- **`[verify current effectiveness and tier dates]`** — the 12 CFR 1002.114 compliance-date schedule. Court-revised; pin from the CFPB compliance-date table at the time of drafting.
- **`[verify current edition]`** — the FIG edition, the Sample Data Collection Form version, the FFIEC Interagency Fair Lending Examination Procedures edition, the CFPB Fair Lending Report edition.
- **`[verify state-specific scope]`** — state privacy-law applicability to the demographic-data collection (lives primarily in `references/cross-cutting/privacy.md`).
- **`[verify subsection]`** — exact 1002.107 subsection labels for individual data points where the rule has been amended; the skill's structured output carries the current label or `[verify subsection]` if uncertain, never an invented label.
