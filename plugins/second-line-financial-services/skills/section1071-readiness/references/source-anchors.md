# Source anchors — section1071-readiness

The named, dated regulatory and supervisory sources this skill anchors to. SKILL.md cites this file by path and does not restate excerpts. Sector-specific and cross-cutting anchors live in the corresponding overlay files. Firm-specific anchors belong in plugin-level `references/firm-overlay.md` (consumed when present).

The CFPB issued a revised §1071 final rule on May 1, 2026 that supersedes the 2023 rule's tier-based compliance schedule, raises the covered-financial-institution threshold to 1,000 covered originations, sets a single effective date of June 30, 2026, and a single compliance date of January 1, 2028 for all CFIs. The litigation history (*Texas Bankers Association v. CFPB* and the CTA-style injunction cluster) is now historical context; it shaped the path to the revised rule but the revised rule is what firms operate under.

## Statutory frame

- **Equal Credit Opportunity Act, Section 1071 (15 U.S.C. §1691c-2)**, added by §1071 of the Dodd-Frank Wall Street Reform and Consumer Protection Act (Pub. L. 111-203). The statutory authority for the small-business-lending data-collection and reporting obligation. Source: https://www.law.cornell.edu/uscode/text/15/1691c-2 .

## Primary frame — CFPB Section 1071 revised final rule (May 2026)

- **Small Business Lending under the Equal Credit Opportunity Act (Regulation B) — revised final rule**. CFPB revised final rule published in the Federal Register on May 1, 2026 [verify Federal Register citation]; codified at Subpart B of Regulation B, **12 CFR 1002.101 through 12 CFR 1002.114**. Rule effective June 30, 2026; compliance date January 1, 2028 for all covered financial institutions. The revised rule supersedes the 2023 final rule's tier-based compliance schedule and raises the covered-financial-institution threshold from the 2023 tiered counts to a single 1,000-transaction threshold. Rule landing page: https://www.consumerfinance.gov/rules-policy/final-rules/small-business-lending-under-the-equal-credit-opportunity-act-regulation-b/ .

- **12 CFR 1002.103 — Definitions**. Sets the operative definitions for *covered financial institution*, *covered application*, *covered credit transaction*, *covered originations*, *small business*, and the related terms the rest of Subpart B reads from. Read 1002.103 first; the rest of the rule cascades from these definitions. The revised rule preserved the 2023 definition structure with limited amendments [verify against current rule text].

- **12 CFR 1002.104 — Covered applications**. Defines what counts as a covered application, including the treatment of inquiries, prequalifications, withdrawn applications, incomplete applications, and reevaluations of existing accounts. Source: https://www.ecfr.gov/current/title-12/chapter-X/part-1002/subpart-B/section-1002.104 .

- **12 CFR 1002.105 — Covered financial institutions (revised threshold)**. Under the May 2026 revised rule, a financial institution is a CFI if it originated at least **1,000 covered originations to small businesses in each of the two preceding calendar years**. This is a single threshold, not a tiered schedule; firms above the line are CFIs subject to the same compliance date, firms below the line in either year are not CFIs. Methodology for counting (covered-transaction definition under 1002.106 applied per product) is the engagement's first analytic step. Source: https://www.ecfr.gov/current/title-12/chapter-X/part-1002/subpart-B/section-1002.105 .

- **12 CFR 1002.106 — Covered credit transactions**. Defines the in-scope credit transactions: term loans, lines of credit, business credit cards, merchant cash advances and other sales-based financing, and similar products extended to a small business for business purposes. Specifies the exclusions (consumer-purpose credit, HMDA-reportable transactions, securities transactions, and similar). Per-product covered-transaction mapping reads against this section. Source: https://www.ecfr.gov/current/title-12/chapter-X/part-1002/subpart-B/section-1002.106 .

- **12 CFR 1002.107 — Compilation of reportable data**. The canonical data-point list. The skill's readiness matrix has one row per data point in this section. The data points include unique identifier, application date, application method, application recipient, credit type (product type, guarantee, loan term), credit purpose, amount applied for, amount approved or originated, action taken, action taken date, denial reasons, pricing information (interest rate; total origination charges; broker fees; initial annual charges; additional cost for merchant cash advance and other sales-based financing; prepayment penalty), census tract (principal address), gross annual revenue, NAICS code, number of workers, time in business, number of principal owners, minority-owned business status, women-owned business status, LGBTQI+-owned business status, and ethnicity / race / sex of principal owners. Verify the complete list and the exact subsection labels (`1002.107(a)(1)` through the trailing subsections) against the revised rule text; the structured output's `data_points[].rule_ref` must match. Source: https://www.consumerfinance.gov/rules-policy/regulations/1002/107/ .

- **12 CFR 1002.108 — Limitations on the use and access of certain information** (the **firewall**). Restricts access by underwriters and others involved in determining whether to extend credit from accessing the applicant-demographic information collected under 1002.107, with limited exceptions where the firm cannot reasonably avoid such access (and with a notice provision in those cases). The firewall design is the operative privacy-adjacent control for §1071 data; the firm's role-based access controls, exception process, attestation map, and firewall-trained personnel design read against this section. Source: https://www.ecfr.gov/current/title-12/chapter-X/part-1002/subpart-B/section-1002.108 .

- **12 CFR 1002.109 — Reporting of data to the Bureau**. Annual reporting; modified version of submitted data is published by the Bureau. The modified-data publication has re-identification implications for low-volume small-business lending in identifiable geographies; surface in the privacy overlay. Source: https://www.ecfr.gov/current/title-12/chapter-X/part-1002/subpart-B/section-1002.109 .

- **12 CFR 1002.110 — Recordkeeping**. **Three-year retention** from the date of submission. The retention obligation reads against the firm's broader records-retention schedule. Source: https://www.ecfr.gov/current/title-12/chapter-X/part-1002/subpart-B/section-1002.110 .

- **12 CFR 1002.111 — Enforcement**. ECOA enforcement provisions apply. The skill carries this as a pointer for the readiness memo's escalation section, not as a primary anchor.

- **12 CFR 1002.112 — Bona fide errors and safe harbors**. The firm's documented bona-fide-error policy and procedure for amending submitted data should sit in place before go-live. The safe-harbor mechanics are narrow; the practitioner's reading of the section is itself an open legal question worth flagging for counsel. Source: https://www.ecfr.gov/current/title-12/chapter-X/part-1002/subpart-B/section-1002.112 .

- **12 CFR 1002.114 — Compliance dates (revised)**. Under the May 2026 revised rule there is a **single compliance date of January 1, 2028** for all covered financial institutions. The 2023 rule's three-tier compliance schedule is superseded; firms previously planning under Tier 1 / 2 / 3 dates re-plan against the single 2028 date. The rule's effective date (the date the regulatory text takes legal effect, distinct from the compliance date by which CFIs must collect and report) is June 30, 2026. The CFPB compliance resources page is the operative source for any further amendments: https://www.consumerfinance.gov/compliance/compliance-resources/small-business-lending-resources/small-business-lending-collection-and-reporting-requirements/ .

## CFPB Filing Instructions Guide and submission mechanics

- **CFPB Filing Instructions Guide (FIG) for small business lending data**, the operative companion to 12 CFR 1002.107 and 1002.109 [verify current edition and version number at the time of drafting; the FIG was updated alongside the May 2026 revised rule]. The FIG sets the file-format specification, data-validation rules, and submission-channel mechanics for the annual filing. The matrix's `reporting_readiness.fig_edition` field records which edition the firm is building against; FIG version changes between cycles trigger a mapping refresh. CFPB filing-resources page: https://www.consumerfinance.gov/data-research/small-business-lending/filing-instructions-guide/ [verify URL].

- **CFPB Section 1071 Sample Data Collection Form** [verify CFPB-published version and date for the revised-rule edition]. The CFPB-published sample form for applicant-demographic data collection. Firms that adopt the sample form's structure get implementation-aid value; firms that build their own form must still meet the rule's required disclosures and refusal-handling. Surface a row in `demographic_collection_mechanics` that names which form is in use.

- **CFPB Section 1071 small-business-lending compliance resources page** — https://www.consumerfinance.gov/compliance/compliance-resources/small-business-lending-resources/ — the operative landing page for the CFPB's compliance materials.

## Historical context — superseded 2023 rule and litigation cluster

The historical posture is preserved here because pre-2026 firm-internal materials, vendor roadmaps, and prior readiness work reference it. None of this is the operative compliance frame; the May 2026 revised rule is.

- **2023 Final Rule** (88 Fed. Reg. 35150, May 31, 2023) — the original Section 1071 final rule with tiered compliance dates. Superseded by the May 2026 revised rule.
- **Texas Bankers Association v. CFPB**, S.D. Tex. (2023–2024) and the related litigation cluster. Produced injunctions and partial stays against the 2023 rule. The CFPB issued revised compliance dates in 2024 in response, then the May 2026 revised rule replaced the dated regime entirely.
- **2024 Interim compliance-date amendments** — superseded; pin to historical reference only.

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
- `references/review-gates.md` — named decision checkpoints and confidence-label definitions.

## Firm overlays

A firm using this skill in production adds firm-specific detail in plugin-level `references/firm-overlay.md`: the firm's own product-to-1002.106 mapping table, the named owners per data point, the LOS vendor, the firewall system, the FIG-validation engine, and the compliance committee that signs off on submission readiness. The skill consumes that file when present. Firm overlays do not modify the public anchors above.

## Verification posture summary

The skill marks three classes of citation with `[verify]`:

- **`[verify Federal Register citation]`** — the May 2026 revised final rule's exact Federal Register page citation; pin from `https://www.federalregister.gov` at drafting time. The compliance date (January 1, 2028) and effective date (June 30, 2026) are stable per the revised rule.
- **`[verify current edition]`** — the FIG edition (updated alongside the revised rule), the Sample Data Collection Form version (revised-rule edition), the FFIEC Interagency Fair Lending Examination Procedures edition.
- **`[verify state-specific scope]`** — state privacy-law applicability to the demographic-data collection (lives primarily in `references/cross-cutting.md#privacy`).
- **`[verify subsection]`** — exact 1002.107 subsection labels for individual data points where the revised rule amended labels; the skill's structured output carries the current label or `[verify subsection]` if uncertain, never an invented label.
