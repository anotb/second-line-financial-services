# Spec sheet: open-banking-data-controls

Plugin: `sector-plugins/payments-fintech-compliance`
Status: v1 retained skill (sector-unique under strict overlay rule).
Phase: 1 (spec only; no SKILL.md content here).

## Why this is a sector-only skill

Open banking and consumer-permissioned data access is a payments-fintech-native problem. The capability primitives (`third-party-operational-resilience/vendor-diligence`, `consumer-compliance-fair-lending/marketing-claim-review`) do not produce the artifact this work needs: a controls inventory mapped to §1033 / open-finance duties, FDX-style data-sharing posture, secure-tunnel / token / API-vs-screen-scraping decisions, and the data-recipient-side accountability the rule places on the fintech consuming the data. The audience is a data-provider fintech, a data-recipient fintech, or a sponsor-bank program acting as either, plus the second-line / advisory team supporting them.

The other sector overlays do not own this. Banking touches it through deposit accounts but is not the natural audience. Capital markets and asset management touch it only at the edges (investment-account aggregation). Insurance does not run on this rule.

## Activation-tuned description

```
Drafts a controls inventory and self-evidence pack for consumer-permissioned data sharing under the CFPB Personal Financial Data Rights Final Rule (October 2024, Section 1033 of the Consumer Financial Protection Act), covering data-provider duties (covered data scope, developer-interface availability, authorization, revocation, third-party screening) and data-recipient duties (consumer authorization, scope and duration limits, accuracy, retention, reauthorization). Aligns the artifact to FDX-style data-sharing patterns and to the migration away from credential-based screen scraping.

Best for:
- A data-provider fintech (or its sponsor bank's program) is preparing for a §1033 implementation milestone, an examiner data request, or a sponsor-bank-led review of the developer interface and authorization stack.
- A data-recipient fintech (account aggregator, PFM, lending, BNPL, payroll-on-demand) is preparing its consumer-authorization, scope, retention, and reauthorization controls for second-line review.
- A program is migrating an aggregator integration from screen scraping (credential-based) to API-tokenized access and needs a side-by-side controls comparison and gap close-out plan.
- An incoming due diligence or contract-cycle review involves an aggregator or developer-interface partner and the team needs the §1033-aligned controls and evidence list.

Not the right tool when:
- The work is a generic vendor due-diligence pack (use third-party-operational-resilience/vendor-diligence with the payments-fintech overlay).
- The work is a fintech-side controls inventory across all rails (use fintech-partner-controls).
- The work is an incident review where data was disclosed without authorization (use payment-operations-incident-review).
- The work is GLBA-Safeguards-only without §1033 in scope (use the Safeguards-side capability skills).

Anchored to: CFPB Personal Financial Data Rights Final Rule under §1033 of the Consumer Financial Protection Act (October 2024) [verify Federal Register citation, effective date, implementation tiers, and current litigation status]; 12 CFR Part 1033 (final rule codification) [verify exact part number]; GLBA Safeguards Rule (16 CFR Part 314) where data security obligations of the data provider and recipient are anchored; FDX (Financial Data Exchange) API specification (current major version) [verify version] as the de facto US standard; NIST SP 800-63B for authentication assurance levels; OAuth 2.0 / FAPI as the common authorization-server pattern [verify whether the firm cites the FAPI 1.0 Final or a newer profile].
```

## Source anchors (skill-specific)

Named US sources, with section references where stable.

- **CFPB Personal Financial Data Rights Final Rule, October 2024** [verify Federal Register publication date and citation], codifying 12 CFR Part 1033 [verify exact part number]. Key elements (treat as current as of the rule text published October 2024; verify effective dates for the firm's tier):
  - **Covered data** — transaction data, account balance, configuration data, payment-initiation information for accounts in scope (Reg E accounts, Reg Z credit cards, and certain payment products) [verify exact covered data list and account scope].
  - **Developer interface** — the data provider's obligation to maintain a covered data interface meeting performance, security, and access standards; prohibition on charging consumers or authorized third parties for access [verify exact wording].
  - **Authorization, scope, duration, revocation** — consumer authorization, one-year reauthorization, scope limited to what is reasonably necessary, revocation handling [verify exact timing rules].
  - **Authorized third party / data recipient duties** — limits on collection, use, retention; secondary-use restrictions; data-deletion duties on revocation; certifications [verify].
  - **Implementation tiers** — staggered compliance dates by data-provider asset size [verify the dates and tiers operative on the date of analysis; the rule has been subject to litigation, and dates may have shifted].
  - **Litigation status** — the final rule has been challenged in court [verify current docket status, any stays, or any compliance-date relief, as of the date of analysis].
- **GLBA Safeguards Rule (16 CFR Part 314)** — written information security program, qualified individual, risk assessment, access controls, encryption, MFA, vendor oversight, incident-response plan; service-provider oversight at §314.4(f).
- **GLBA Privacy Rule (16 CFR Part 313 / Reg P at 12 CFR Part 1016)** — initial and annual privacy notices, opt-out, sharing rules; relevant where the data flow includes "nonpublic personal information."
- **FDX API specification, current major version** [verify version number and release date] — the de facto US standard for tokenized open-banking data exchange. Conceptual citation; FDX is industry, not regulator.
- **NIST SP 800-63B, Digital Identity Guidelines, Authentication and Lifecycle Management** — AAL2 / AAL3 reasoning where the authorization stack is being designed.
- **OAuth 2.0 (RFC 6749) and FAPI 1.0 Final / current profile** [verify which profile the firm cites] — the underlying authorization-server pattern.
- **FFIEC Authentication and Access to Financial Institution Services and Systems guidance, August 2021** — supervisory expectations for authentication, including for high-risk transactions and customer-permissioned data sharing.
- **CFPB Circular 2024-XX series** [verify whether any circulars in 2024-26 directly address §1033 implementation; do not assert without verification] — supervisory expectations and enforcement signaling on §1033.
- **State privacy laws** — CCPA / CPRA, and the rolling state-privacy-law landscape (CT / CO / VA / UT / TX / OR and others); relevant where the data flow includes California or other in-scope residents.
- **Applicable consent orders** in the fintech-aggregator space [verify which are current as of the date of analysis] — public source for fact patterns on credential storage, secondary use, and unauthorized retention.

Treat every external source as an anchor, not a substitute for legal interpretation. Date every citation in the output. The §1033 final rule is the central anchor; its dates and litigation posture must be re-verified at the time of each engagement and noted in the artifact.

## Sector overlays needed

Only `payments-fintech` (this is the sector skill).

## Cross-cutting overlays

- `cross-cutting/cyber.md` — required. NYDFS Part 500 (where applicable), FFIEC IT booklets, GLBA Safeguards Rule §314.4 controls (encryption, access management, MFA, change management, monitoring), token / key management for the developer interface, authentication assurance level reasoning.
- `cross-cutting/privacy.md` — required. GLBA Privacy Rule / Reg P notices, CCPA / CPRA, state privacy laws, secondary-use limits, retention and deletion duties, consumer access and revocation under §1033.
- `cross-cutting/conduct.md` — recommended. UDAAP exposure when consumer authorization flows are misleading, when revocation does not work end-to-end, or when scope creep occurs after authorization. Cross-references `consumer-compliance-fair-lending/udaap-risk-review`.

## Output template named sections

Practitioner headings on the default-output template:

1. Program summary (provider role: data provider / data recipient / both; products; consumer base; partner aggregators / developers in scope).
2. **Current-state regulatory frame** — §1033 final rule as of October 2024, the firm's implementation tier with date, current litigation status as of the date of analysis, and any active CFPB or state guidance overlays. (This section is a "stop and date this" section; do not soft-state.)
3. Data-provider scope (covered data inventory, in-scope accounts, in-scope products; out-of-scope items with rationale).
4. Developer interface posture (availability, performance, security; uptime SLOs; documentation, sandbox, conformance testing; reliance on a third-party developer-portal vendor if applicable; prohibition on consumer / authorized-party fees for access).
5. Authorization, scope, duration, revocation controls (consumer-facing flows, scope-narrowing, one-year reauthorization, revocation propagation, audit trail).
6. Data-recipient screening and onboarding (third-party authorization conditions, certifications collected, ongoing monitoring; tie-back to TPRM lifecycle).
7. Data-recipient duties (where the firm is a data recipient): collection limits, use limits, secondary-use posture, retention schedule, deletion-on-revocation, reauthorization, downstream sharing and notice.
8. Screen-scraping migration plan (where applicable): credential-storage inventory, deprecation roadmap, fallback posture, customer-impact assessment, sponsor-bank coordination.
9. Cyber controls on the data flow (encryption in transit and at rest, key management, token lifecycle, MFA / FAPI assurance level, monitoring and incident detection, breach-response chain to consumer and sponsor bank).
10. Privacy controls (GLBA / Reg P notices, state-privacy-law obligations, dual-purpose consent stack, do-not-sell / share signals where in scope).
11. Vendor and fourth-party register (aggregators, developer-portal vendor, consent-management vendor, identity-vendor, fraud-decision vendor) with criticality flag.
12. Self-evidence index (artifact list mapped to each control section).
13. Gaps, issues, recommended remediation.
14. Open items and named follow-ups with owners.
15. Source citations with date (and §1033 status note repeated here).

## Structured output fields

| Field | Type | Purpose |
|---|---|---|
| `program_id` | string | Internal identifier for the data-sharing program under review. |
| `firm_role` | enum (`data_provider`, `data_recipient`, `both`) | Drives which §1033 obligations apply. |
| `s1033_status_note` | object | `effective_date` (string, with `[verify]` flag), `firm_implementation_tier` (string), `litigation_status_as_of` (date), `notes` (string). Required field; cannot be blank. |
| `covered_data_inventory` | array of object | Each: data element, in-scope flag (yes / no / `[verify]`), source system, owner. |
| `accounts_in_scope` | array of enum (`Reg_E_consumer_asset_account`, `Reg_Z_credit_card`, `prepaid_account`, `payment_product`, `other`) | Maps to the rule's covered-account scope [verify]. |
| `developer_interface_findings` | array of finding | Availability, performance, security, free-access, sandbox, conformance. |
| `authorization_findings` | array of finding | Consent flow, scope, duration, revocation propagation, reauthorization timing. |
| `data_recipient_screening_findings` | array of finding | Third-party authorization conditions, certifications, monitoring. |
| `data_recipient_duty_findings` | array of finding | Where firm is recipient: collection / use / retention / deletion / reauthorization. |
| `screen_scraping_inventory` | array of object | Each: integration name, credential-storage location, target deprecation date, status. |
| `cyber_findings` | array of finding | Encryption, key lifecycle, MFA / FAPI level, monitoring, incident response. |
| `privacy_findings` | array of finding | GLBA / Reg P, state privacy law, secondary use, signal handling. |
| `vendor_register` | array of object | Vendor, function, criticality, evidence-of-oversight. |
| `self_evidence_index` | array of object | Control reference, artifact, owner role, last-refreshed date, freshness flag. |
| `gaps` | array of gap | Description, source citation with date, severity, owner, target close date. |
| `issues` | array of issue | Material issues elevated. |
| `recommended_disposition` | enum (`ready_for_review`, `ready_with_conditions`, `remediate_then_re_review`, `not_ready`) | Second-line recommendation. |
| `conditions` | array of string | Conditions attached to a ready-with-conditions disposition. |
| `open_items` | array of item | Description, owner, target date. |
| `source_citations` | array of citation | Source name, section reference, retrieval date, URL; §1033 retrieval date is mandatory. |

## Two example scenarios (public-source-derived, anonymous)

1. **Mid-tier data-provider fintech preparing the developer-interface and authorization stack ahead of its §1033 tier date.** Public anchor: CFPB §1033 Final Rule (October 2024) [verify date and firm's tier]; FFIEC Authentication Guidance (August 2021); FAPI 1.0 Final. Scenario: the firm is a data provider for checking-equivalent and credit-card-equivalent products, currently exposes a partner-portal API but does not enforce per-consumer authorization scope, charges aggregators a per-call fee, and has no documented one-year reauthorization mechanism. Skill output: developer-interface gap (per-consumer scope and free-access), authorization-stack gap (reauthorization and scope-narrowing), and a §1033 status note with the firm's tier date and the litigation-status caveat as of the engagement date.
2. **Account aggregator (data recipient) migrating screen-scraping integrations to API-tokenized access.** Public anchor: §1033 final rule data-recipient duties (collection / use / retention / secondary use); GLBA Safeguards Rule §314.4; relevant CFPB and FTC enforcement actions in the aggregator space [verify which are current]. Scenario: the aggregator stores hashed-but-recoverable credentials for legacy data providers in a vault, has no end-to-end deletion path for consumer-revoked authorizations, and the consumer-facing scope description is broader than the actual data flow. Skill output: screen-scraping deprecation gap (credential-vault retirement and timeline), data-recipient duty gap (revocation-propagated deletion path), authorization-stack gap (scope description vs actual flow), and the §1033 status note plus the GLBA Safeguards §314.4(f) service-provider oversight artifacts list.

Both scenarios use only public sources. No named aggregators or providers are used as fact-specific examples; public CFPB and FTC actions in the aggregator and credential-storage space are the conceptual reference.

## Common pitfalls

- Stating the §1033 effective date without checking it on the date of analysis. The rule has been subject to litigation; tier dates and stays may have changed. The artifact has to date-stamp this.
- Assuming a screen-scraping integration is fine because it has been in production for years. The migration path is the artifact's centre of gravity, not a footnote.
- Drafting data-provider duties without separately drafting data-recipient duties when the firm acts as both. They are different control families with different evidence.
- Mixing GLBA Safeguards controls and §1033 controls into one undifferentiated list. They overlap but they are not the same; a gap in one is not automatically a gap in the other.
- Leaving the consumer-authorization scope language as marketing copy. Examiners and plaintiffs will read the scope vs the actual flow side by side.
- Treating FDX as a regulator. FDX is industry; alignment is supervisory expectation but not a legal obligation by itself.
- Skipping the developer-portal vendor in the fourth-party register. The portal vendor is in the data path and inherits the obligations.
- Asserting categorical "covered data" answers without checking the rule's specific list and the firm's account scope. The rule's coverage is more granular than a single sentence.
