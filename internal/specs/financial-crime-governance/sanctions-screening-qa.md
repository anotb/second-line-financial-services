# sanctions-screening-qa — Phase 1 spec sheet

Date: 2026-05-06
Plugin: financial-crime-governance
Phase: 1 (per-skill scoping; no SKILL.md content)

## Activation-tuned description

Reviews sanctions screening program evidence: list-management governance, customer and transaction screening configuration, match-logic and fuzzy-matching tuning, list-update timeliness, alert disposition documentation, false-positive rationale, escalation paths, and 50-percent-rule and sectoral-sanctions handling. Produces a second-line QA memo with material findings, evidence-needed items, and recommendations. Does not approve list configuration, tune match logic, file blocking reports, or close alerts.

Best for:
- Periodic QA over a sample of customer-screening and transaction-screening alert dispositions.
- Pre-validation review of screening configuration evidence to scope the next validation cycle.
- Pre-exam readiness review of sanctions program documentation against the OFAC framework and FFIEC manual.
- Targeted review after a list update event (e.g., new SDN designations, new sectoral sanctions, FSE designation changes).
- Targeted review of screening evasion exposure (cross-cutting cyber overlay).

Not the right tool when:
- The work is a sanctions program risk assessment as a whole (this skill reviews QA evidence; the program risk assessment is a different artifact).
- The work is an AML transaction-monitoring review (use aml-model-monitoring; sanctions is real-time list-match, not behavioral).
- The work is filing or amending an OFAC blocking or rejection report.
- The decision is whether to release, block, or report a transaction or relationship. Skill produces QA artifacts only; humans decide.

Anchored to: A Framework for OFAC Compliance Commitments (OFAC, May 2, 2019) — five components: management commitment, risk assessment, internal controls, testing and auditing, training; OFAC SDN List, Sectoral Sanctions Identifications List, and other OFAC lists; OFAC 50 Percent Rule revised guidance (August 2014) [verify date]; FFIEC BSA/AML Examination Manual, Office of Foreign Assets Control section [verify section anchor]; OFAC Recent Actions and enforcement releases as pattern references; OFAC General Licenses and FAQs as criteria references where applicable [date as-of].

## Source anchors

- A Framework for OFAC Compliance Commitments, May 2, 2019 — https://ofac.treasury.gov/media/16331/download?inline (or current OFAC link) [verify current URL] — five components: management commitment; risk assessment; internal controls; testing and auditing; training.
- OFAC Specially Designated Nationals and Blocked Persons List (SDN List) — https://ofac.treasury.gov/sanctions-programs-and-country-information [verify current URL]; date as-of every workproduct.
- OFAC Sectoral Sanctions Identifications List (SSI List) and other lists (Non-SDN Iran Sanctions Act List, Foreign Sanctions Evaders List, Specially Designated Global Terrorists, etc.) — current OFAC pages [verify current URLs].
- OFAC Revised Guidance on Entities Owned by Persons Whose Property and Interests in Property Are Blocked (50 Percent Rule), August 13, 2014 [verify date] — aggregate ownership ≥ 50% by one or more blocked persons triggers blocking treatment.
- FFIEC BSA/AML Examination Manual — Office of Foreign Assets Control section [verify section anchor].
- OFAC Recent Actions / enforcement releases — used as pattern references for evasion typologies and lessons-learned themes (anonymized in examples; pattern only).
- 31 CFR Chapter V — OFAC sanctions regulations [verify specific program citations as needed].

## Sector overlays needed

- `references/sector-overlays/banking.md` — wire-screening, trade-finance screening, correspondent-banking nested-relationship exposure, customer-screening cycle (delta vs. full re-scan).
- `references/sector-overlays/payments-fintech.md` — payments-rail-specific screening (ACH, wire, card, faster-payments), real-time screening latency tradeoffs, sponsor-bank screening responsibility, MSB screening, crypto on-ramp/off-ramp screening exposure to FinCEN/OFAC convergence.
- `references/sector-overlays/capital-markets.md` — broker-dealer screening obligations, securities-related sanctions (executive orders restricting securities transactions), microcap and offshore-issuer concentration.
- `references/sector-overlays/insurance.md` — covered-products screening, beneficiary screening at claim, ceded/assumed reinsurance counterparty screening.

## Cross-cutting overlays

- `references/cross-cutting/cyber.md` — sanctions screening evasion via cyber and tech: typologies covered include (a) ransomware payments to OFAC-listed groups, (b) virtual-currency obfuscation through mixers and chain-hopping, (c) cyber-enabled identity manipulation that defeats name-and-DOB matching, (d) deepfake / synthetic-identity exposure at onboarding screening, (e) BIN sponsorship and prepaid-card abuse for sanctions circumvention, (f) decentralized finance and bridge exposure for sanctions evasion. Anchored to: OFAC ransomware advisories (current versions, dated) [verify dates]; OFAC sanctions compliance guidance for the virtual currency industry (October 15, 2021) [verify date]; FinCEN/OFAC parallel advisories on virtual currency and ransomware. Decision rationale: included.
  - Decision (vs. flagged in prompt): include the cyber overlay. Rationale: sanctions evasion via cyber and virtual currency is a documented and live regulator concern; OFAC has published industry-specific guidance for virtual currency sanctions compliance and has issued ransomware-related advisories that explicitly intersect screening. The overlay is therefore not speculative, anchors cleanly to public OFAC and FinCEN material, and avoids coupling sanctions screening tightly to general cyber controls (which sit elsewhere in the repo).

Conduct, climate, privacy not in scope at v1.

## Output template named sections

1. Scope and review window (program, list set, screening rails, sample basis)
2. Sanctions risk posture summary (list set in use, jurisdictions, products, customer types)
3. List management governance (list sources, update cadence, last-update evidence, controls over delta-vs-full updates)
4. Screening configuration (customer screening, transaction screening, match logic, fuzzy thresholds, exclusion lists)
5. Alert disposition QA (sample, FP rationale documentation, escalation paths, decision-maker independence)
6. 50 Percent Rule and sectoral sanctions handling (ownership-aggregation evidence, SSI handling)
7. List-update event reviews (recent designations or program changes; institution response evidence)
8. Cyber-evasion exposure (cross-cutting overlay): virtual currency exposure, ransomware-payment exposure, cyber-enabled identity exposure
9. Issues and material findings (criterion-aligned to OFAC Framework five components and FFIEC OFAC section)
10. Recommended human-review gates
11. Source trace and confidence label (with date-as-of for OFAC list citations)

## Structured output fields

| Field | Type | Purpose |
|---|---|---|
| `program_id` | string | Sanctions program identifier (placeholder for sample). |
| `review_window` | object | Sub-fields: start_date, end_date. |
| `list_set` | array of strings | OFAC SDN, SSI, FSE, NS-PLC, other [verify list names]; non-OFAC lists in use (UN, EU, UK OFSI, jurisdictional). |
| `list_management` | object | Sub-fields: update_cadence, last_update_date, delta_vs_full_evidence, open_findings. |
| `screening_configuration` | object | Sub-fields: customer_screening_rules, transaction_screening_rails, match_logic_summary, fuzzy_threshold_setting, exclusion_lists_documented. |
| `alert_disposition_sample` | array of objects | Alert ID, list source, match score, disposition, FP rationale category, decision-maker role, evidence pointer. |
| `fifty_percent_rule_handling` | object | Sub-fields: aggregation_methodology, evidence_basis, edge_case_handling. |
| `list_update_events` | array of objects | Event date, designation type, institution response evidence, response timing. |
| `cyber_evasion_exposure` | object | Sub-fields: virtual_currency_exposure, ransomware_payment_exposure, cyber_identity_exposure, controls_evidence. |
| `material_findings` | array of objects | Finding, criterion (OFAC Framework component, FFIEC manual section), severity, evidence pointer. |
| `recommended_gates` | array of objects | Gate name, criterion, required reviewer, stop condition. |
| `source_trace` | array of objects | Claim, source, date_as_of, confidence label. |

## Example scenarios (public-source-derived, anonymous)

1. Pattern reference: a published OFAC enforcement action against a payments / fintech firm citing screening configuration deficiencies, list-update lag, and 50-percent-rule oversight gaps (use a publicly available OFAC enforcement release; anonymize the institution; cite the release date in the example) [verify specific public release at SKILL.md drafting time]. QA memo scope: customer screening over a 12-month window, two payment rails, sample of 100 alert dispositions. Findings: list-update cadence documented as "daily" but evidence shows lag of 2 to 5 business days for delta updates against OFAC publication date in 12% of in-window updates; FP-rationale documentation generic ("reviewed, not a match") in 30% of sampled dispositions; 50-percent-rule aggregation methodology not documented at the program level; ownership-aggregation handled case-by-case at analyst level. Anchored to: OFAC Framework components risk assessment, internal controls, testing and auditing; 50 Percent Rule guidance. Recommended gates: list-update SLA evidence requirement; FP-rationale documentation standard tied to disposition codes; 50-percent-rule methodology documented at program level and signed by sanctions officer.

2. Regional bank, list-update event review following a hypothetical week of significant new SDN designations. Review window: 14 days after designation date. Findings: full re-scan against new designations completed within 24 hours of list update for customer base; one trade-finance system relied on a delta-update batch and did not include a flagged designation type for 36 hours due to a feed mapping gap; cyber-evasion exposure assessment for the new designations (whether designations include virtual-currency-adjacent typologies) was not performed; cross-rail consistency check (customer hits raised on one rail and cleared on another within the window) not documented. Anchored to: FFIEC OFAC section; OFAC Framework testing and auditing; OFAC ransomware/virtual-currency guidance for the cyber overlay. Recommended gates: feed-mapping completeness check after each material list event; cross-rail consistency check artifact; designation-type cyber-overlay assessment as a standing list-event step.

## Common pitfalls

1. List-update timeliness reported against the institution's own publication of the list rather than against OFAC's publication date. The right benchmark is OFAC publication; the institution's internal lag is what is being measured.
2. Match logic and fuzzy thresholds are not papered. Reviewer cannot reproduce why a specific score crossed or did not cross threshold. Mitigation: screening_configuration field forces structured documentation.
3. False-positive rationale documented at the disposition level as boilerplate ("reviewed, not a match"). No taxonomy of FP categories means tuning evidence is impossible. Mitigation: QA flags generic rationale as a finding.
4. 50 Percent Rule applied case-by-case without a documented aggregation methodology, or applied only at single-owner level. Aggregate ownership across multiple blocked persons is missed. Mitigation: methodology documentation is a structured field.
5. Cyber-evasion exposure treated as a generic cyber control item rather than a sanctions-screening evasion vector. Skill keeps the overlay tight to evasion typologies (ransomware payments, virtual currency, identity manipulation) anchored in OFAC and FinCEN public guidance.
6. Sectoral sanctions and SSI handling treated identically to SDN. Different prohibitions, different blocking versus restriction patterns. QA must distinguish.
7. Reviewer drifts toward instructing a release, block, or report decision on a specific alert. Skill produces QA findings; human decisions sit with the sanctions officer and applicable escalation chain.
8. Date-as-of missing on list citations. OFAC lists change frequently; any sanctions QA artifact that does not date its list citations cannot be relied on.
