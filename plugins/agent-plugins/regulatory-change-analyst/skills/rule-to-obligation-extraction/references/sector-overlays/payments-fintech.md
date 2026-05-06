# Payments and fintech sector overlay — rule-to-obligation-extraction

Load this overlay when the rule under extraction is a CFPB rule under the consumer-financial protection statutes (Reg E, Reg Z, Reg DD, Reg P, Reg V, Reg X, Section 1071, Section 1033, UDAAP), a state money-transmitter rule, or a sponsor-bank or partnership-related rule for fintech-bank arrangements. The overlay carries the consumer-protection rule-citation conventions and the cross-jurisdiction obligation-decomposition pattern for state-by-state money-transmitter regimes.

## CFPB Regulation citation conventions

- **Reg E** — Electronic Fund Transfer Act, 12 CFR Part 1005. Provisions: §1005.5 issuance; §1005.6 liability; §1005.7 disclosures; §1005.10 preauthorised transfers; §1005.11 procedures for resolving errors; §1005.18 prepaid accounts; §1005.20 gift cards; §1005.30-37 remittance transfers (the "Remittance Rule" subpart).
- **Reg Z** — Truth in Lending Act, 12 CFR Part 1026. Provisions span open-end and closed-end credit, mortgages, credit cards, ability-to-repay (§1026.43), HOEPA, integrated disclosures (TRID).
- **Reg DD** — Truth in Savings Act, 12 CFR Part 1030. Disclosure requirements for deposit accounts.
- **Reg P** — Privacy of Consumer Financial Information, 12 CFR Part 1016. GLBA privacy notices; opt-out rights; sharing-with-affiliates limitations.
- **Reg V** — Fair Credit Reporting Act, 12 CFR Part 1022. Identity-theft red-flag rules; risk-based-pricing notices; furnisher rules.
- **Reg X** — RESPA, 12 CFR Part 1024. Mortgage-servicer obligations; loss-mitigation procedures.
- **Reg B** — Equal Credit Opportunity Act, 12 CFR Part 1002. Includes Subpart B (Section 1071 small-business-lending data, 12 CFR 1002.101 through 12 CFR 1002.114).
- **Section 1033** — Personal financial-data rights, 12 CFR Part 1033 (final rule 89 FR 90838, November 18 2024 [verify final FR cite]).
- **UDAAP** — 12 USC §5531 (Dodd-Frank Section 1031); not a rule with codified subsections, but the operative supervisory and enforcement standard. UDAAP-anchored extractions pin to CFPB circulars, supervisory highlights, and consent-order articles for the operative standard.

## CFPB Section 1071 — worked pattern

12 CFR 1002.101 through 12 CFR 1002.114 (Subpart B of Reg B), 88 FR 35150 (May 31 2023). Effective date August 29 2023. Tier-based compliance dates [verify post-litigation revised dates, as the rule's compliance dates have been adjusted post-publication]:

- Tier 1 covered FIs (2,500 or more covered originations in each of the two preceding calendar years): originally October 1 2024.
- Tier 2 (500 to 2,499): originally April 1 2025.
- Tier 3 (100 to 499): originally January 1 2026.

Extraction decomposes into atomic obligations:

- **Covered-financial-institution determination** (12 CFR 1002.105(b)). Trigger: each calendar year, the institution determines whether it meets the covered-FI threshold for the preceding two years.
- **Covered-application-data-points obligation** (12 CFR 1002.107(a)). On each covered application: collect 20+ data points enumerated in §1002.107(a). Each data point is an obligation row in the extraction (or a single row with the data-point list as evidence_expected, depending on the granularity required by the consumer).
- **Firewall obligation** (12 CFR 1002.108). The covered FI must maintain procedures to limit the access of the underwriter to demographic data collected under §1002.107(a)(18)-(a)(20) where feasible. The exception (where a firewall is not feasible, the covered FI must provide a notice to the applicant) is its own row.
- **Recordkeeping obligation** (12 CFR 1002.111). Retain covered-application records for at least three years.
- **Reporting obligation** (12 CFR 1002.109). Submit the covered-application data to the CFPB by June 1 of each year covering the preceding calendar year. First-report due dates are tier-staged.
- **Effective-date-and-transition row**. Tier-by-tier compliance dates as the rule provides; capture each tier as its own row in the transition table.

The defined terms section captures: "covered application"; "covered credit transaction"; "covered financial institution"; "covered originations"; "minority-owned business"; "women-owned business"; "LGBTQI+-owned business"; "small business"; "applicant".

## CFPB Section 1033 — worked pattern

12 CFR Part 1033, 89 FR 90838 (November 18 2024) [verify final FR cite]. Tier-based compliance dates by data-provider size [verify post-publication revised dates]. Extraction decomposes into:

- **Data-provider obligations**: make available to consumers and authorised third parties electronic-format data on covered consumer financial accounts.
- **Authorised-third-party obligations**: collect, use, and retain data only for the purposes authorised by the consumer; deletion-on-request obligation.
- **Standard-setter recognition**: CFPB process for recognising industry standard-setting bodies; not a direct obligation on regulated parties.
- **Recordkeeping obligation**: data providers must retain records of data-access requests.

## Reg E error-resolution and remittance-rule patterns

- **Error-resolution procedures** (12 CFR 1005.11). Trigger: receipt of consumer notice of error within 60 days of the periodic statement. Action: investigate and report results within 10 business days; provisional credit if investigation extends beyond 10 business days. Action_type: notice_or_disclosure plus monitoring.
- **Remittance Rule disclosures** (12 CFR 1005.31, 1005.32, 1005.33). Pre-payment disclosure; receipt; error resolution; cancellation. Each is a row.

## State money-transmitter rule structure

State money-transmission rules are state-by-state. The Money Transmission Modernization Act (MTMA) is a model law adopted by the Conference of State Bank Supervisors (CSBS) and adopted by an increasing number of states; the model is not law in any state until adopted. Extraction from a state money-transmitter rule pins to the state code section. Common shared concepts across states: licensing requirement; permissible-investments requirement; net-worth requirement; surety bond; reporting (call reports, BSA filings); notification of material change; consumer disclosures.

The cross-jurisdiction extraction pattern: when the rule under extraction is a model (MTMA, NAIC model, NCCUSL model), the extraction captures model-section obligations and flags state-by-state adoption status as the implementation question. Each state-adopted version is a separate extraction.

## Sponsor-bank and bank-fintech partnership rule structure

The OCC, FRB, and FDIC have issued joint and individual guidance on bank-fintech partnerships and on banking-as-a-service relationships:

- **June 2023 Interagency Guidance on Third-Party Relationships: Risk Management** (88 FR 37920). Operative supervisory expectation; see the banking sector overlay.
- **OCC Bulletin 2023-25** [verify exact bulletin number] on third-party-relationships guidance for community banks.
- **Joint statement on the risks of crypto-asset arrangements** (January 3 2023; February 23 2023; September 7 2023 statements [verify dates]).
- **State-level bank-fintech partnership conditions** in some state DOIs.

Sponsor-bank obligations under partnership arrangements typically decompose into: oversight of the third-party fintech (life-cycle stages from the interagency guidance); BSA/AML programme responsibility for accounts opened through the fintech; consumer-protection programme responsibility; complaint handling; UDAAP oversight. The sponsor bank carries the regulatory obligation; the fintech carries contractual obligations to the sponsor bank that mirror the regulatory obligations. Extraction distinguishes between the regulatory obligation on the bank and the pass-through contractual obligation on the fintech.

## When to escalate

The base SKILL.md is the right tool when the extraction feeds `obligation-mapping` for a fintech, payments firm, or sponsor bank. When the extraction crosses multiple jurisdictions (federal CFPB rule plus state money-transmitter regimes plus state UDAAP analogues), each jurisdiction is a separate extraction; the cross-jurisdiction view is built downstream by `obligation-mapping` running with multiple registers as input.
