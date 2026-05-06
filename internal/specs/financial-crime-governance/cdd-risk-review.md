# cdd-risk-review — Phase 1 spec sheet

Date: 2026-05-06
Plugin: financial-crime-governance
Phase: 1 (per-skill scoping; no SKILL.md content)

## Activation-tuned description

Reviews a customer due diligence file (new account, periodic refresh, or event-driven refresh) against CDD program expectations: customer identification, beneficial ownership identification and verification, risk rating, expected activity profile, ongoing-monitoring trigger conditions, and EDD upgrade criteria. Produces a second-line review memo with material gaps, evidence-needed items, and recommended human-review gates. Does not approve onboarding, set the customer risk rating, or close the file.

Best for:
- Second-line QA over a sample of new-account CDD files (banking, payments, broker-dealer, MSB).
- Periodic refresh review where risk-rating drivers, beneficial ownership data, or expected activity may have shifted.
- Event-driven refresh triggered by negative news, sanctions hit, transaction-monitoring alert, or change in beneficial ownership.

Not the right tool when:
- The customer profile already meets EDD criteria and the next artifact is the EDD pack itself (use edd-escalation-pack).
- The work is sanctions screening match disposition, not customer due diligence (use sanctions-screening-qa).
- The work is alert disposition or SAR decision QA (use sar-decision-qa).
- The decision is a final onboarding approval, rating change, or relationship exit. Skill produces review artifacts only; humans decide.

Anchored to: FFIEC BSA/AML Examination Manual, Customer Due Diligence and Beneficial Ownership Requirements for Legal Entity Customers sections (current online manual, last updated 2018 / 2020) [verify section anchors]; FinCEN Customer Due Diligence Final Rule (May 2016, effective May 11, 2018); 31 CFR 1010.230 Beneficial Ownership Rule via Cornell LII; FinCEN Beneficial Ownership Information Reporting Rule (CTA implementing rule, effective January 1, 2024) [verify current effectiveness given CTA litigation timeline]; OCC, FRB, FDIC, NCUA Joint Statement on Risk-Focused BSA/AML Supervision (July 2021).

## Source anchors

- FFIEC BSA/AML Examination Manual — Customer Due Diligence section [verify exact URL anchor; current online manual]: https://bsaaml.ffiec.gov/manual/AssessingComplianceWithBSARegulatoryRequirements/02
- FFIEC BSA/AML Examination Manual — Beneficial Ownership Requirements for Legal Entity Customers section [verify section anchor]: https://bsaaml.ffiec.gov/manual
- FinCEN CDD Final Rule (81 FR 29397, May 11, 2016; compliance date May 11, 2018) — four pillars of CDD: customer identification and verification; beneficial ownership identification and verification; understanding the nature and purpose of the customer relationship; ongoing monitoring for reporting suspicious transactions and on a risk basis maintaining and updating customer information.
- 31 CFR 1010.230 — Beneficial Ownership Requirements for Legal Entity Customers (text via Cornell LII): https://www.law.cornell.edu/cfr/text/31/1010.230
- FinCEN Beneficial Ownership Information Reporting Rule (CTA implementing rule, 31 CFR 1010.380) — entities filing BOI reports with FinCEN; [verify current effectiveness for which entity classes given Corporate Transparency Act litigation history and any subsequent legislation; date filings as-of every workproduct].
- OCC, FRB, FDIC, NCUA Joint Statement on Risk-Focused BSA/AML Supervision, July 22, 2021 — risk-focused supervision of BSA/AML compliance programs.
- FinCEN/Federal Banking Agencies Joint Statement on Innovation in BSA/AML Compliance, December 3, 2018 — innovative approaches in BSA/AML compliance.
- 31 CFR 1020.220 (banks), 31 CFR 1023.220 (broker-dealers), and parallel rules — Customer Identification Program rules.

## Sector overlays needed

- `references/sector-overlays/banking.md` — CDD for retail, commercial, private banking, correspondent banking (Section 312 due diligence on foreign correspondent and private banking accounts under 31 CFR 1010.610 and 1010.620 [verify section]); deposit operations CIP triggers; cash-intensive business risk drivers.
- `references/sector-overlays/payments-fintech.md` — sponsor-bank relationship CDD reliance, money services business registration, agent of payee considerations, fintech onboarding velocity tradeoffs vs. CDD depth.
- `references/sector-overlays/capital-markets.md` — broker-dealer CIP under 31 CFR 1023.220, investment adviser AML rule (FinCEN final rule for investment advisers, August 2024) [verify current effective date].
- `references/sector-overlays/insurance.md` — covered products under 31 CFR 1025.210 (insurance companies) [verify section]; CDD scope limited to covered products (permanent life, annuities, others as defined).

## Cross-cutting overlays

None planned at v1. Conduct intersects more sharply with edd-escalation-pack (PEP, high-risk customer profile) than with baseline CDD review. Cyber and privacy intersections are present (NPI handling) but covered at the program level, not at this skill's review artifact level.

## Output template named sections

1. File identifier and review scope (new account, periodic, event-driven; trigger if event-driven)
2. Customer profile summary (entity type, products, expected activity)
3. Customer identification and verification (CIP coverage, evidence pointers)
4. Beneficial ownership (control prong, ownership prong, certification reliance, BOI reporting status if applicable)
5. Customer risk rating (drivers, current rating, basis, reasonableness)
6. Expected activity profile and ongoing-monitoring triggers
7. EDD escalation criteria (met / not met / borderline; rationale)
8. Material gaps and evidence-needed items
9. Reviewer findings (criteria-aligned)
10. Recommended human-review gates and owner actions
11. Source trace and confidence label

## Structured output fields

| Field | Type | Purpose |
|---|---|---|
| `file_id` | string | Canonical CDD file identifier (placeholder for sample). |
| `review_type` | enum | `new_account`, `periodic_refresh`, `event_driven_refresh`. |
| `trigger` | string | Event description if event-driven; null otherwise. |
| `customer_type` | enum | `individual`, `legal_entity`, `trust`, `correspondent`, `other`. |
| `cip_coverage` | object | Sub-fields: identifying_info_collected (bool), verification_method (documentary, non-documentary, both), discrepancies. |
| `beneficial_ownership` | object | Sub-fields: control_prong_identified (bool), ownership_prong_identified (bool), certification_form_on_file (bool), boi_filing_status (`required`, `not_required`, `unknown`, `[verify]`). |
| `risk_rating` | object | Sub-fields: current_rating, rating_drivers (array), rating_reasonable (bool), rationale. |
| `expected_activity` | object | Sub-fields: documented (bool), specificity (`generic`, `specific`, `quantified`), monitoring_triggers (array). |
| `edd_status` | enum | `not_required`, `borderline`, `required_pending`, `in_place`. |
| `material_gaps` | array of objects | Gap description, criterion violated, evidence needed, severity. |
| `recommended_gates` | array of objects | Gate name, criterion, required reviewer, stop condition. |
| `source_trace` | array of objects | Claim, source (named regulatory anchor or file evidence), confidence label. |

## Example scenarios (public-source-derived, anonymous)

1. Mid-size US community bank, new account opening for a legal entity customer (LLC) operating a cash-intensive convenience-store business. CDD file shows beneficial ownership certification form on file with a single 100% beneficial owner (control prong and ownership prong satisfied by the same individual). Expected activity is documented as "general business banking" with no quantified cash-deposit profile. Risk rating recorded as "medium" with drivers listed as "small business, cash deposits". Public criteria reference: FFIEC manual treats cash-intensive businesses as a risk driver; expected activity for cash-intensive businesses should be quantified to support ongoing monitoring. Reviewer findings: expected activity insufficiently specific; risk rating drivers do not address cash-intensity beyond a label; CIP and beneficial ownership look complete on face. Material gaps: quantified cash-activity profile; customer-stated rationale for cash levels. Recommended gates: monitoring threshold tuning review at 90 days post-activation.

2. Regional broker-dealer periodic refresh on a high-net-worth individual customer with international wire activity. Original CDD captured residence, ID, source-of-wealth statement. Refresh triggered by 24-month periodic cycle. Public criteria reference: FFIEC manual periodic CDD refresh expectations; 31 CFR 1023.220 CIP retention rules; expected activity update on a risk basis. Reviewer findings: source-of-wealth statement stale and not corroborated by any independent source on file; expected activity profile predates a documented change in client's business circumstances (publicly known professional change). Material gaps: corroboration evidence for source of wealth; updated expected activity profile; consideration of whether change in business circumstances triggers re-rating or PEP-adjacent assessment. Recommended gates: EDD upgrade decision; refresh-cycle interval recalibration.

## Common pitfalls

1. Beneficial ownership treated as a one-time form. A legal entity customer's ownership changes between refresh cycles and the file does not reflect it. Mitigation: review checks for inconsistency between certification form date, latest entity filings, and activity that implies undisclosed control parties.
2. Risk rating drivers listed as labels ("cash-intensive", "international", "PEP-adjacent") without any link to evidence on file. Reviewer treats labels as conclusions instead of asking for the evidence underneath them.
3. Expected activity captured as boilerplate ("general business banking", "personal banking") that cannot drive monitoring scenario tuning. Mitigation: review flags non-specific expected activity statements as a material gap.
4. CIP completeness conflated with CDD completeness. CIP is identification and verification at onboarding; CDD adds the beneficial ownership pillar, the nature-and-purpose pillar, and the ongoing-monitoring pillar. Skill must surface gaps against all four pillars, not just the first.
5. BOI reporting status treated as known when it is genuinely uncertain given the CTA litigation timeline. Reviewer must mark BOI filing status `[verify]` rather than asserting required or not required without grounding.
6. Reviewer extends the file's risk rating into a relationship-exit recommendation. Skill produces gaps and review-gate recommendations; humans rate, file SARs, and exit relationships.
