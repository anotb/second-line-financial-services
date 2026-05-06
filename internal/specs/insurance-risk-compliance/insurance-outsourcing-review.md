# Spec sheet: insurance-outsourcing-review

Plugin: `sector-plugins/insurance-risk-compliance`
Status: v1 retained skill (genuinely insurance-only).
Phase: 1 (spec only; no SKILL.md content here).

## Why this is a sector-only skill

Insurance outsourcing review is not the same workflow as the bank-flavored `vendor-diligence` in `third-party-operational-resilience`. The statutory frame is the NAIC insurance-holding-company and outsourcing model law family (the regulators who examine this work are state insurance departments, not federal banking agencies), the contractual constructs are MGA / MGU / TPA / claims-handling delegations rather than generic vendor-services agreements, and the core risks (binding authority, claims authority, premium fiduciary handling, producer licensing, policyholder data security under the NAIC Insurance Data Security Model Law) do not appear in the federal-banking third-party guidance. Capability `vendor-diligence` does not produce an artifact that survives a market-conduct exam. This skill does.

## Activation-tuned description

```
Drafts a second-line review pack for an insurance outsourcing or delegated-authority arrangement (MGA, MGU, TPA, claims administrator, underwriting bureau, IT or actuarial outsourcer) against NAIC outsourcing and holding-company expectations and the NAIC Insurance Data Security Model Law, with named gaps, oversight evidence checked, and a recommended supervisor disposition.

Best for:
- A US insurer or reinsurer is onboarding, renewing, or remediating an MGA, MGU, TPA, or claims-administrator arrangement and second-line needs a pre-decision review.
- A market-conduct exam, ORSA cycle, or internal audit has flagged outsourced-function oversight and the team is preparing the response file.
- A reinsurer is reviewing a cedent's delegated-underwriting authority arrangement before treaty placement or renewal.

Not the right tool when:
- The arrangement is a generic IT or SaaS vendor with no delegated underwriting, claims, premium-handling, or policyholder-data role (use third-party-operational-resilience/vendor-diligence with the insurance overlay instead).
- The work is a cyber-incident response for an outsourced provider (use risk-reporting/cyber-disclosure-readiness with the insurance overlay).
- The exposure is captive-reinsurance or affiliate-reinsurance solvency (different model law family; out of scope).

Anchored to: NAIC Insurance Holding Company System Regulatory Act (Model #440) [verify model number]; NAIC Insurance Holding Company System Model Regulation (Model #450) [verify model number]; NAIC Unfair Trade Practices Act (Model #880); NAIC Insurance Data Security Model Law (Model #668); state DOI bulletins on TPA and MGA oversight; NAIC Producer Licensing Model Act where binding authority is delegated.
```

## Source anchors (skill-specific)

Named US sources, with section references where stable:

- NAIC Insurance Holding Company System Regulatory Act, Model #440 [verify model number] — affiliate transactions, ultimate controlling person disclosures, and supervision of intra-group outsourcing.
- NAIC Insurance Holding Company System Model Regulation, Model #450 [verify model number] — Form B (holding-company registration) and Form D (transactions between affiliates) detail.
- NAIC Insurance Data Security Model Law, Model #668 — third-party service-provider oversight (commonly §4.F): written contract requirements, due diligence, ongoing monitoring, incident-response cooperation, breach notification chain to the cedent insurer.
- NAIC Unfair Trade Practices Act, Model #880 — claims-handling standards that follow the function even when delegated to a TPA or claims administrator.
- NAIC Producer Licensing Model Act [verify model number] — licensing required for any party exercising binding or producer authority on the carrier's behalf.
- NAIC Bulletin on the Use of Artificial Intelligence Systems by Insurers, December 2023 — vendor-AI accountability when an MGA, TPA, or claims administrator is using AI tools on the carrier's policies.
- ORSA Model Act, Model #505 — outsourced critical functions belong in the ORSA Summary Report.
- State DOI bulletins on TPA registration and oversight (cite by state when used; treat each as a state-specific overlay).
- HIPAA where the outsourced function touches protected health information (life and health TPAs, claims administrators).

Treat every external source as an anchor, not a substitute for legal interpretation. Date every citation in the output.

## Sector overlays needed

Only `insurance` (this is the sector skill).

## Cross-cutting overlays

- `cross-cutting/cyber.md` — required. Insurance Data Security Model Law §4.F third-party service-provider obligations and breach-notification flow from TPA / MGA to cedent.
- `cross-cutting/privacy.md` — required where the outsourced function handles PHI (HIPAA business-associate posture for life and health TPAs and claims administrators) or state insurance-privacy frameworks (NAIC Insurance Information and Privacy Protection Model Act, Model #670) [verify model number].
- `cross-cutting/conduct.md` — recommended where the TPA handles claims; UDAP and unfair-claims-settlement-practices flow from Model #880 follow the function.

## Output template named sections

Practitioner headings on the default-output template:

1. Arrangement summary (counterparty type, functions delegated, states of operation, lines of business, premium volume, claims volume).
2. Holding-company status and Form D posture (is this an affiliate transaction; is a Form D filing triggered).
3. Producer-licensing and binding-authority confirmation.
4. Contractual-control review against NAIC outsourcing expectations (audit rights, books-and-records access by the commissioner, indemnification, termination, sub-delegation restrictions).
5. Insurance Data Security Model Law §4.F third-party service-provider review (due diligence, written contract clauses, monitoring, incident-response cooperation, breach-notification chain).
6. Claims-handling oversight (Model #880 fair-claims-settlement application to the delegated function, complaint flow, denial-letter review).
7. Premium-handling and fiduciary-account posture (where the TPA collects or holds premium).
8. Vendor-AI exposure (any AI tool used by the TPA or MGA on the carrier's policies; tie-back to NAIC AI Bulletin December 2023 expectations).
9. ORSA fit (is the outsourced function critical; does it appear in the ORSA Summary Report).
10. Gaps, issues, and recommended disposition (approve / approve-with-conditions / remediate / decline).
11. Open items and named follow-ups with owners.
12. Source citations with date.

## Structured output fields

JSON schema fields, each with type and purpose. (Fields, not formats — drafted here for the schema author in phase 2.)

| Field | Type | Purpose |
|---|---|---|
| `arrangement_id` | string | Internal identifier for the outsourcing arrangement under review. |
| `counterparty_type` | enum (`MGA`, `MGU`, `TPA`, `claims_admin`, `underwriting_bureau`, `IT_outsourcer`, `actuarial_outsourcer`, `other`) | Drives which Model expectations apply. |
| `functions_delegated` | array of enum | Underwriting / binding / rating / claims / premium-handling / data-processing / actuarial / IT. |
| `states_of_operation` | array of string | State DOI overlays trigger from this list. |
| `affiliate_status` | enum (`affiliate`, `non_affiliate`) | Determines Form D applicability. |
| `holding_company_disclosure` | object | Form B reference, Form D filing status, ultimate controlling person. |
| `producer_licensing_status` | object | License confirmation per state where binding authority is exercised. |
| `contract_control_findings` | array of finding | Each finding: clause, expectation, present / absent, severity. |
| `data_security_findings` | array of finding | Insurance Data Security Model §4.F third-party clauses present / absent. |
| `claims_handling_findings` | array of finding | Model #880 fair-claims-settlement controls in the delegated function. |
| `vendor_ai_exposure` | object | AI tools used by the counterparty; tie-back to NAIC AI Bulletin Dec 2023 governance expectations. |
| `orsa_inclusion` | boolean | Whether the function is in the ORSA Summary Report. |
| `gaps` | array of gap | Each gap: description, source citation with date, severity, owner, target close date. |
| `issues` | array of issue | Material issues elevated to risk register or audit. |
| `recommended_disposition` | enum (`approve`, `approve_with_conditions`, `remediate_then_re_review`, `decline`) | Second-line recommendation, not a decision. |
| `conditions` | array of string | Conditions attached to an approve-with-conditions disposition. |
| `open_items` | array of item | Each item: description, owner, target date. |
| `source_citations` | array of citation | Each citation: source name, model or section reference, retrieval date, URL where public. |

## Two example scenarios (public-source-derived, anonymous)

1. **Mid-sized P&C carrier renewing a binding-authority MGA across 12 states.** Public anchor: NAIC Producer Licensing Model Act and Insurance Holding Company Model Reg #450 Form D. Scenario: MGA writes commercial-auto on the carrier's paper, books-and-records clause is silent on commissioner access in three of the states, and the MGA recently rolled out a third-party AI rating tool not covered by the original delegation contract. Skill output: contract-control gap (commissioner access), vendor-AI gap (tie-back to NAIC AI Bulletin Dec 2023), and a Form D posture check.
2. **Life carrier renewing a TPA for claims administration on a closed block.** Public anchor: NAIC Insurance Data Security Model Law #668 §4.F and HIPAA business-associate posture. Scenario: TPA handles PHI and recently changed its sub-processor for OCR of claims documents without notice. Skill output: §4.F sub-processor and breach-notification gaps, HIPAA business-associate addendum check, claims-handling fair-settlement (#880) review of the TPA's denial letters, and an ORSA-inclusion recommendation.

Both scenarios use only public sources (NAIC Model text, HIPAA statutory citations, generic carrier role descriptions). No named institutions.

## Common pitfalls

- Treating an MGA review as a vendor-diligence review. Different statutory frame, different artifact, different audience (state DOI not federal banking).
- Missing the Form D filing trigger when the counterparty is an affiliate. The substance of the contract is fine; the procedural filing is not, and that is what the exam picks up.
- Failing to follow the function. UDAP and fair-claims-settlement under Model #880 apply to the delegated function regardless of who performs it. The TPA's letters are the carrier's letters for that purpose.
- Treating Insurance Data Security Model Law §4.F as a copy of the federal third-party guidance. The §4.F clauses are insurance-specific (commissioner access, cedent breach-notification chain) and have to be checked against insurance language, not banking language.
- Skipping vendor-AI exposure. NAIC Bulletin Dec 2023 holds the carrier accountable for AI used by its delegated providers on its policies. Many MGA and TPA shops have rolled out AI tooling without telling the cedent.
- Conflating producer licensing with corporate licensing. The exam reviews per-state per-individual-producer status, not just the entity.
- Drafting the artifact as a contract abstract instead of an oversight memo. Regulators want to see the carrier's oversight, not a recap of the agreement.
