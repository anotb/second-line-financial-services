# Source anchors — open-banking-data-controls

Named, dated regulatory sources this skill anchors to. SKILL.md cites this file by path and does not restate excerpts in narrative. Sector flavour for payments-fintech sits in `sector-overlays/payments-fintech.md`; cross-cutting flavour sits in `cross-cutting/<topic>.md`.

The CFPB Personal Financial Data Rights Final Rule is the central anchor. Its docket has been active since finalisation; the `s1033_status_note` field in the artifact carries the verification date for the firm's tier and the current docket posture as of each engagement. The FDX API specification is industry, not regulator; alignment is supervisory expectation, not a legal obligation by itself. Network and card-network rulebooks are paywalled where they appear in adjacent overlays; this skill does not cite them directly.

## Personal Financial Data Rights Final Rule (central anchor)

- **CFPB Personal Financial Data Rights Final Rule under §1033 of the Dodd-Frank Act**, codifying 12 CFR Part 1033 [verify exact part number against the published final rule], finalised October 22, 2024 [verify Federal Register publication date and exact citation]. Key elements (treat as current as of the rule text published October 22, 2024; verify effective dates for the firm's tier on each engagement):
  - **Covered data** — transaction data, account balance, configuration data, and payment-initiation information for accounts in scope (consumer asset accounts under the consumer-EFT regime, credit cards under the credit-card regime, and certain payment products) [verify exact covered-data list and account scope on the analysis date].
  - **Developer interface** — the data provider's obligation to maintain a covered-data interface meeting performance, security, and access standards; prohibition on charging consumers or authorised third parties for access [verify exact section reference and wording].
  - **Authorisation, scope, duration, revocation** — consumer authorisation, one-year reauthorisation cadence, scope limited to what is reasonably necessary, revocation handling end-to-end [verify exact timing rules and section reference].
  - **Authorised third party / data recipient duties** — limits on collection, use, retention; secondary-use restrictions; data-deletion duties on revocation; certifications [verify section reference].
  - **Implementation tiers** — staggered compliance dates by data-provider asset size [verify the dates and tiers operative on the date of analysis; the rule has been subject to litigation and dates may have shifted].
  - **Litigation status** — the final rule has been challenged in court [verify current docket status, any stays, and any compliance-date relief on the analysis date]. CFPB final-rule landing page: https://www.consumerfinance.gov/rules-policy/final-rules/required-rulemaking-on-personal-financial-data-rights/ .

The artifact's `s1033_status_note` block carries the firm-specific application of the bullets above and date-stamps each engagement's verification.

## Federal Safeguards and Privacy frame

- **GLBA Safeguards Rule, 16 CFR Part 314** as amended (FTC, December 2021 amendments effective 2023). **§314.4** the written information security programme requirements (qualified individual, risk assessment, access controls, encryption, MFA, change management, monitoring, incident-response plan, vendor oversight); **§314.4(f)** service-provider obligations; **§314.4(h)** incident-response posture. Where the firm is FTC-supervised, the affected-customer notification threshold applies [verify current threshold]. https://www.ecfr.gov/current/title-16/chapter-I/subchapter-C/part-314 .

- **GLBA Privacy Rule / Reg P, 12 CFR Part 1016**. Initial and annual privacy notices; sharing rules; opt-out mechanics. Where the data flow includes "nonpublic personal information," Reg P frames the customer-facing notice and the sharing scope. https://www.ecfr.gov/current/title-12/chapter-X/part-1016 .

- **FTC GLBA Privacy Rule, 16 CFR Part 313** — applies where the firm is FTC-supervised rather than CFPB-supervised under the prudential framework. https://www.ecfr.gov/current/title-16/chapter-I/subchapter-C/part-313 .

## Authentication and tokenised access frame

- **FFIEC Authentication and Access to Financial Institution Services and Systems Guidance** (August 11, 2021). Sets the supervisory expectation for authentication posture, including for high-risk transactions and for customer-permissioned data sharing. Risk-based authentication, layered controls, account-takeover monitoring. https://www.ffiec.gov/press/pr081121.htm .

- **NIST SP 800-63B, Digital Identity Guidelines, Authentication and Lifecycle Management** [verify current revision]. Authentication assurance levels (AAL1, AAL2, AAL3) and the lifecycle controls that hold each level. https://pages.nist.gov/800-63-3/sp800-63b.html .

- **OAuth 2.0 (RFC 6749)** — the underlying authorisation-server pattern for tokenised access. https://datatracker.ietf.org/doc/html/rfc6749 .

- **OpenID FAPI 1.0 — Financial-grade API Security Profile** [verify whether the firm cites FAPI 1.0 Final, FAPI 2.0, or a later profile on the analysis date]. Security profile for financial-data API access. https://openid.net/specs/openid-financial-api-part-1-1_0.html .

- **Financial Data Exchange (FDX) API specification (current major version)** [verify version number and release date on the analysis date]. The de facto US industry standard for tokenised open-banking data exchange. Conceptual citation; FDX is industry, not regulator. https://financialdataexchange.org/ .

## Consumer-EFT error-resolution overlay (data-recipient incidents)

- **Reg E — Electronic Fund Transfers Act and Regulation E, 12 CFR Part 1005**.
  - **§1005.11** procedures for resolving errors. Where a data-recipient flow surfaces an unauthorised electronic fund transfer (e.g., a PFM-initiated transfer, a payroll-on-demand disbursement), the consumer-EFT error-resolution clocks apply. The clock runs from the consumer's notice, not from the firm's incident detection. https://www.ecfr.gov/current/title-12/chapter-X/part-1005/section-1005.11 .
  - **§1005.6** consumer liability for unauthorised electronic fund transfers. https://www.ecfr.gov/current/title-12/chapter-X/part-1005/section-1005.6 .

## State privacy frame

- **California Consumer Privacy Act / California Privacy Rights Act, Cal. Civ. Code §1798.100 et seq.** Consumer rights to know, delete, correct, opt-out of sale and sharing; sensitive-personal-information limits; data-breach private right of action under specific conditions. https://oag.ca.gov/privacy/ccpa .

- **Rolling state-privacy-law landscape** — active comprehensive privacy laws as of analysis include (incomplete; verify currency on the analysis date) Virginia (VCDPA), Colorado (CPA), Connecticut (CTDPA), Utah (UCPA), Texas (TDPSA), Oregon (OCPA), Montana (MTCDPA), and others. Each carries its own consumer-rights set, sensitive-data category, opt-out mechanics, and enforcement posture. https://iapp.org/resources/article/us-state-privacy-legislation-tracker/ [verify currency].

- **State breach-notification statutes** — state-by-state; verify per state in the firm's resident footprint. Each carries its own notification trigger (acquisition standard vs access standard), timing window, AG-notification thresholds, and content requirements.

## CFPB direct supervision and supervisory signal

- **CFPB final rule defining larger participants of a market for general-use digital consumer payment applications** (December 2024) [verify Federal Register citation and current state including any litigation, congressional review, or compliance-date relief on the analysis date]. Brings designated non-bank larger participants under direct CFPB supervision; a designated firm faces direct CFPB EXAMS posture rather than sponsor-bank-mediated supervision. https://www.consumerfinance.gov/rules-policy/final-rules/ [verify exact link to the final rule].

- **CFPB Circular series** [verify section and which circulars in the 2024-26 series directly address §1033 implementation, data-recipient duties, or screen-scraping migration on the analysis date]. https://www.consumerfinance.gov/compliance/circulars/ .

- **CFPB Supervisory Highlights (current cycles)** [verify section and which issues are current on the analysis date]. Recurring open-banking themes: authorisation-flow disclosure; revocation-path failures; data-recipient secondary-use; aggregator credential-storage. https://www.consumerfinance.gov/data-research/research-reports/supervisory-highlights/ .

- **CFPB and FTC enforcement actions in the aggregator and credential-storage space, 2023-26** [verify section and which actions are current and finalised on the analysis date]. Use only public defendants in finalised actions for fact-pattern citation. The credential-storage and unauthorised-retention actions establish the conceptual fact pattern that several scenarios in this skill turn on. https://www.consumerfinance.gov/enforcement/actions/ ; https://www.ftc.gov/legal-library/browse/cases-proceedings .

## Sponsor-bank and TPRM frame

- **Interagency Guidance on Third-Party Relationships: Risk Management** (OCC Bulletin 2023-17 / FRB SR 23-4 / FDIC FIL-29-2023, June 6, 2023) [verify exact section structure across the released bulletin]. Risk-based lifecycle: planning, due diligence and third-party selection, contract negotiation, ongoing monitoring, termination. The aggregator and the developer-portal vendor are TPRM targets. https://www.occ.gov/news-issuances/news-releases/2023/nr-ia-2023-53.html ; https://www.federalreserve.gov/newsevents/pressreleases/bcreg20230606a.htm ; https://www.fdic.gov/news/press-releases/2023/pr23047.html .

- **Joint Statement on Banks' Arrangements with Third Parties to Deliver Bank Deposit Products and Services** (FDIC / OCC / FRB, July 25, 2024) [verify exact title and date — this is the operative statement, not the 2023 RFI]. Sponsor-bank end-customer reconciliation expectation; the statement frames the sponsor-bank-side oversight of the data-rights programme. https://www.fdic.gov/news/financial-institution-letters/2024/ [verify exact FIL number].

## Cyber overlay (cross-cutting carries the detail)

- **NYDFS 23 NYCRR Part 500** including **§500.17(a)** cybersecurity-event notification clock (72 hours from determination that a cybersecurity event has occurred). Applies to firms that are NYDFS Covered Entities; many fintechs are by virtue of NY footprint. https://www.dfs.ny.gov/industry_guidance/cybersecurity .

- **FFIEC IT Examination Handbook — Information Security booklet** [verify current edition and section]. Sets the supervisory expectation for the firm's information-security programme. https://ithandbook.ffiec.gov/ .

## Plugin-level shared references

Also consult, when present in the plugin:

- `references/source-map.md` — plugin-wide named-source map for payments-fintech.
- `references/policy-control-library.md` — plugin-wide control library for cross-skill payments-fintech controls.
- `references/public-regulatory-scenarios.md` — canonical scenario library reused across the four sector skills.

## Firm overlays

A firm using this skill in production adds firm-specific detail in `references/firm-overlay.md` — the firm's data-provider tier date, the named aggregators integrated, the developer-portal vendor, the firm's sponsor-bank programme-agreement clause-set on data-rights compliance, the named runbooks for authorisation, revocation, and deletion, and the named human-review gates. The skill consumes that file when present. Firm overlays do not modify the public anchors above.
