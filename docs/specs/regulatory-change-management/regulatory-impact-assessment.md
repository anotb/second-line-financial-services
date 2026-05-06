# Spec: regulatory-impact-assessment

Plugin: regulatory-change-management
Status: phase 1 spec sheet, pending phase 2 build
Date: 2026-05-06

## Activation-tuned description

Drafts a second-line impact assessment for a new rule, guidance item, supervisory letter, circular, or enforcement theme. Output covers in-scope businesses and products, affected obligations and controls, reporting and disclosure impacts, evidence implications, effective-date posture, and the open questions that need legal or business sign-off before the change goes to remediation planning.

Best for:
- A new final rule, supervisory letter, FIL, circular, bulletin, or industry letter has been published and the regulatory-change function needs to scope firm impact before the issue is logged in the inventory.
- An enforcement action or consent order names a peer institution and the firm needs a fast read on whether the same theme applies.
- A supervisory priorities letter or speech has shifted examiner posture and the firm needs to assess where current state may not hold up.

Not the right tool when:
- The rule text has already been parsed and the next step is decomposing it into discrete obligations (use rule-to-obligation-extraction).
- Firm policy text is already drafted and the question is whether it covers the rule (use policy-diff).
- Gaps are already documented and the next step is sequencing the remediation (use implementation-plan).

Anchored to: 12 CFR Part 30 Appendix B (heightened standards) [verify section]; OCC Bulletin 2013-29 (third-party relationships) and 2023 interagency revision; SR 11-7 §V (model risk management); FRB SR 13-19 (operational risk); FDIC FILs as published; CFPB circulars and bulletins as published; NCUA Letters to Credit Unions; NYDFS Industry Letters and Part 500; SEC final rules and adopting releases (Federal Register); FinCEN advisories and final rules; ISO/IEC 42001:2023 §6 and §7; NIST AI RMF 1.0 Govern function.

## Source anchors

- OCC Bulletin 2013-29 (Third-Party Relationships) and revised 2023 interagency third-party risk management guidance, OCC release nr-ia-2023-53.
- FRB SR 11-7 (Guidance on Model Risk Management), §V model documentation; SR 13-19 (Guidance on Managing Outsourcing Risk).
- FDIC FILs as published, indexed by year.
- CFPB Circulars (e.g., 2022-03 adverse action notices using AI [verify]) and Bulletins.
- NCUA Letters to Credit Unions (e.g., 24-CU-XX series) [verify exact letter cited].
- NYDFS Industry Letters (e.g., October 2024 GenAI cybersecurity guidance) and 23 NYCRR Part 500.
- SEC final rules and adopting releases via Federal Register; e.g., Reg S-P amendments, cyber disclosure rule.
- FinCEN advisories and final rules; e.g., 31 CFR 1010.230 beneficial ownership.
- 12 CFR Part 30 Appendix B (Interagency Guidelines Establishing Heightened Standards) [verify section ref for second-line responsibilities].
- ISO/IEC 42001:2023 §6 (planning) and §7 (support) for AI-related rule changes.
- NIST AI RMF 1.0 Govern function for AI-related rule changes.

URLs alone are not sufficient. Spec sheet entries must end up with section refs and publication date in source-anchors.md during phase 2.

## Sector overlays needed

- banking.md — applicability calls for OCC/FRB/FDIC supervised entities (national bank, state member, state non-member, holding company, IDIs); Heightened Standards thresholds; CRA implications where relevant.
- insurance.md — NAIC Model Laws, state insurance departments, NY DFS where applicable; how state-level adoption changes effective dates.
- capital-markets.md — SEC and FINRA registrant impacts; Investment Advisers Act and Investment Company Act overlays; rule 206(4)-7 compliance program implications.
- payments-fintech.md — CFPB authority over non-bank larger participants; state money transmitter overlays; bank-fintech partnership posture.

## Cross-cutting overlays needed

- cyber.md — when the rule touches incident disclosure, security program, or third-party cyber expectations (SEC cyber 8-K, NYDFS Part 500, FFIEC IT booklet).
- privacy.md — GLBA Safeguards, Reg S-P amendments, state privacy laws (CCPA/CPRA), HIPAA where applicable.
- climate.md — SEC climate disclosure rule, federal banking agency climate principles for large banks; only when applicable.
- conduct.md — UDAAP/UDAP, fair-lending, market conduct themes.

## Output template named sections

1. Decision required and recommended posture
2. Source identification (regulator, instrument type, citation, effective date, comment period if any, publication date)
3. In-scope determination (institution type, products, business units, geographies, thresholds)
4. Effective-date posture (mandatory compliance date, transition period, early-adoption considerations)
5. Impacted obligation domains (cross-reference to existing obligation inventory entries by ID)
6. Policy and procedure impact (which firm policies likely need amendment)
7. Control and evidence impact (control objectives potentially affected; evidence gaps anticipated)
8. Reporting and disclosure impact (regulatory reports, public disclosures, board reporting)
9. Technology and data impact (systems of record, data lineage, model inventory)
10. Third-party impact (vendor contracts, exit obligations, register-of-information entries)
11. Open legal and business questions for qualified review
12. Recommended next steps (rule-to-obligation-extraction; policy-diff; implementation-plan)
13. Source trace and confidence labels

## Structured output fields

| Field | Type | Purpose |
|---|---|---|
| assessment_id | string | Stable ID for the impact assessment |
| source_citation | object {regulator, instrument_type, citation, section, publication_date, effective_date, url} | Pinpoint regulatory source |
| in_scope | boolean | Whether firm is in scope; if false, rationale required |
| in_scope_rationale | string | Why in-scope or not, with source pin |
| affected_business_units | array<string> | First-line owners affected |
| affected_products | array<string> | Product lines affected |
| affected_geographies | array<string> | Jurisdictions affected |
| obligation_domains | array<string> | High-level domains (e.g., MRM, TPRM, AML, fair-lending) |
| existing_obligation_refs | array<string> | IDs in obligation inventory potentially affected |
| policy_impact | array<object {policy_name, expected_change_type}> | Policies likely needing amendment |
| control_impact | array<object {control_id, expected_change_type}> | Existing controls likely impacted |
| reporting_impact | array<object {report_name, change_type}> | Regulatory or board reports affected |
| third_party_impact | array<object {arrangement_id, change_type}> | Vendor arrangements likely impacted |
| effective_date | date | Mandatory compliance date |
| transition_period | string | Transition relief if any, with citation |
| open_questions | array<object {question, owner_role, blocker_for}> | Items needing legal or business sign-off |
| recommended_next_steps | array<string> | Skill-level handoffs (extraction, diff, plan) |
| confidence | enum {high, medium, low, unknown} | Per-section confidence label |
| source_trace | array<object {claim, citation}> | Material claims tied to citations |

## Example scenarios (public-source-derived)

1. CFPB 2022 Circular on adverse-action notices when using AI/ML credit decisioning. Impact assessment for a mid-size consumer bank: in-scope determination, affected obligations under ECOA / Reg B §1002.9, policy impacts on adverse-action notice templates, control impacts on model explainability and reason-code generation, open questions on fair-lending model governance handoff to MRM. [verify exact circular number and date]
2. NYDFS October 2024 Industry Letter on cybersecurity risks arising from GenAI. Impact assessment for a state-chartered bank using GenAI for customer service: in-scope determination under Part 500, affected obligations on access controls and data classification, policy impacts on AI use case intake and acceptable-use, control impacts on prompt-injection and data-leakage controls, third-party impact on LLM vendor evidence packs.

## Common pitfalls

1. Treating an impact assessment as legal interpretation. The skill names obligations and flags questions; it does not opine on whether the rule applies as a matter of law.
2. Pulling the rule's plain text into the obligation inventory without tier-1 decomposition. That is the next skill's job (rule-to-obligation-extraction).
3. Failing to flag transition-period and effective-date posture. A high-impact rule with a 24-month transition is a different planning problem from a 90-day one.
4. Missing the cross-cutting hook (cyber/privacy/climate/conduct). A rule labeled "operational resilience" can still carry privacy and conduct implications.
5. Citing only the regulator's press release URL. Source anchors require the rule citation and section, not the news release.
