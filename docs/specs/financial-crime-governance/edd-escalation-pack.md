# edd-escalation-pack — Phase 1 spec sheet

Date: 2026-05-06
Plugin: financial-crime-governance
Phase: 1 (per-skill scoping; no SKILL.md content)

## Activation-tuned description

Drafts an EDD escalation pack for a higher-risk customer profile (PEP, high-risk jurisdiction nexus, cash-intensive business, correspondent banking, private banking, complex ownership, MSB-affiliated, sanctions-adjacent). The pack assembles source-of-funds and source-of-wealth analysis, beneficial ownership chain, expected versus actual activity, adverse media findings, sanctions screening posture, conduct-risk indicators, and reviewer questions for the EDD committee. Produces a review artifact only; the EDD committee or designated approver makes the relationship decision.

Best for:
- A baseline CDD review (use cdd-risk-review first if not done) has flagged EDD escalation, and the next artifact is the pack the EDD committee will review.
- A periodic high-risk customer refresh where existing EDD content needs to be re-papered against current activity, ownership, and adverse-media posture.
- A relationship-exit deliberation where the EDD pack is the basis for the deliberation memo.

Not the right tool when:
- Baseline CDD review has not run or is incomplete (use cdd-risk-review first).
- The work is alert disposition or SAR decision QA on this customer (use sar-decision-qa).
- The work is a single adverse media hit triage with no broader EDD context (use negative-news-triage).
- The decision is the final EDD committee approval, retention, or exit. Skill produces review artifacts only; humans decide.

Anchored to: FFIEC BSA/AML Examination Manual, sections on Politically Exposed Persons, Private Banking Due Diligence Programs (Non-U.S. Persons), Correspondent Accounts (Foreign), and Customer Due Diligence (current online manual) [verify section anchors]; FinCEN CDD Final Rule (May 2016, effective May 11, 2018); 31 CFR 1010.620 (private banking) and 31 CFR 1010.610 (correspondent banking) [verify section]; OCC, FRB, FDIC, NCUA Joint Statement on Risk-Focused BSA/AML Supervision (July 2021); Wolfsberg Group guidance on PEPs and source of wealth (public).

## Source anchors

- FFIEC BSA/AML Examination Manual — Politically Exposed Persons section [verify section anchor].
- FFIEC BSA/AML Examination Manual — Private Banking Due Diligence Programs (Non-U.S. Persons) section [verify section anchor]; reflects 31 CFR 1010.620.
- FFIEC BSA/AML Examination Manual — Correspondent Accounts (Foreign) section [verify section anchor]; reflects 31 CFR 1010.610.
- FFIEC BSA/AML Examination Manual — Customer Due Diligence section: https://bsaaml.ffiec.gov/manual/AssessingComplianceWithBSARegulatoryRequirements/02
- FinCEN CDD Final Rule (81 FR 29397, May 11, 2016; compliance May 11, 2018) — risk-based EDD where warranted; ongoing monitoring as a CDD pillar.
- 31 CFR 1010.230 — Beneficial Ownership Requirements for Legal Entity Customers (Cornell LII).
- 31 CFR 1010.620 — Due diligence programs for private banking accounts [verify section].
- 31 CFR 1010.610 — Due diligence programs for correspondent accounts for foreign financial institutions [verify section].
- OCC, FRB, FDIC, NCUA Joint Statement on Risk-Focused BSA/AML Supervision, July 22, 2021.
- Wolfsberg Group Guidance on Politically Exposed Persons (most recent public version) [verify date]; Wolfsberg Source of Wealth and Source of Funds guidance — public industry standard reference, not a regulator anchor.

## Sector overlays needed

- `references/sector-overlays/banking.md` — private banking (31 CFR 1010.620), correspondent banking (31 CFR 1010.610), Section 311 special measures considerations [verify], Section 312 enhanced due diligence on foreign correspondent and private banking accounts.
- `references/sector-overlays/payments-fintech.md` — high-risk customer types in payments (MSB-affiliated, crypto on-ramp/off-ramp, third-party payment processors); sponsor-bank EDD reliance arrangements.
- `references/sector-overlays/capital-markets.md` — broker-dealer high-risk customer types (foreign omnibus accounts, prime brokerage, microcap concentration); investment adviser AML rule overlay [verify effective date].
- `references/sector-overlays/insurance.md` — covered products only (permanent life, annuities); single-premium and large-premium triggers as EDD drivers.

## Cross-cutting overlays

- `references/cross-cutting/conduct.md` — conduct-risk indicators that intersect EDD: PEP and family/close-associate adverse-conduct exposure, complaint-pattern indicators tied to the relationship, vulnerable-customer overlap with high-risk profiles, market-conduct exposures (e.g., suitability, sales-practice patterns) for private banking and wealth segments. Sources: FCA conduct guidance (where firm has UK nexus) [verify]; FFIEC manual treatment of relationship behavior as a risk driver; CFPB UDAAP framing where retail harm is in scope.

Cyber, privacy, climate not in scope for this skill at v1.

## Output template named sections

1. Customer identifier and EDD trigger
2. Customer summary and product footprint
3. Beneficial ownership chain (legal entities, trusts, nominees; control parties)
4. PEP, sanctions-adjacency, and high-risk-jurisdiction posture
5. Source of funds and source of wealth (statement, corroboration evidence, residual gaps)
6. Expected vs. actual activity (with monitoring scenario links)
7. Adverse media and reputational findings (with negative-news-triage outputs if applicable)
8. Conduct-risk indicators (cross-cutting overlay)
9. Sanctions screening posture (current and historical hits, dispositions)
10. Open issues and reviewer questions for the EDD committee
11. Recommended human-review gates (committee composition, decision options, stop conditions)
12. Source trace and confidence label

## Structured output fields

| Field | Type | Purpose |
|---|---|---|
| `customer_id` | string | Canonical customer identifier (placeholder for sample). |
| `edd_trigger` | enum | `pep`, `private_banking`, `correspondent`, `cash_intensive`, `high_risk_jurisdiction`, `complex_ownership`, `msb_affiliated`, `sanctions_adjacent`, `event_driven`, `other`. |
| `product_footprint` | array of strings | Product or service lines used. |
| `beneficial_ownership_chain` | array of objects | Layer, entity or person, role (control / ownership), evidence pointer, residual_uncertainty. |
| `pep_posture` | object | Sub-fields: pep_status (`pep`, `family_close_associate`, `none`, `unknown`), source_of_pep_finding, date_assessed. |
| `sof_sow` | object | Sub-fields: sof_statement, sow_statement, corroboration_evidence (array), residual_gaps (array). |
| `expected_vs_actual` | object | Sub-fields: expected_profile, actual_profile_summary, deviation_findings, scenario_links. |
| `adverse_media` | array of objects | Hit summary, source reliability, date, materiality, linkage confidence (delegate to negative-news-triage outputs where present). |
| `conduct_indicators` | array of objects | Indicator type, evidence, severity, regulator-anchor reference. |
| `sanctions_posture` | object | Sub-fields: current_screening_status, historical_hits (array of dispositions), list_coverage. |
| `committee_questions` | array of strings | Tagged by topic (ownership, SoW, activity, conduct, sanctions). |
| `recommended_gates` | array of objects | Gate name, criterion, required reviewer, decision options, stop condition. |
| `source_trace` | array of objects | Claim, source, confidence label. |

## Example scenarios (public-source-derived, anonymous)

1. Mid-size US bank, private banking client who is an immediate family member of a senior foreign government official (PEP-adjacent under FFIEC manual and Wolfsberg PEP guidance). Account opened five years ago, EDD pack last refreshed 30 months ago. Refresh triggered by periodic cycle plus a recent media report on the family member's involvement in a foreign procurement matter. Pack assembles: ownership chain through two foreign holding entities; SoW based on a self-attested family-trust distribution; SoF on inbound wires routed through a foreign correspondent. Public criteria reference: FFIEC manual private banking section requires SoW corroboration and ongoing scrutiny for senior foreign political figures and their family/close associates; 31 CFR 1010.620 enhanced scrutiny obligations [verify section]. Reviewer findings: SoW corroboration weak; deviation between expected wire activity profile and actual; adverse media hit material and linked. Pack flags conduct overlay (foreign-procurement exposure). Recommended gates: EDD committee review with relationship-exit option on the table.

2. Regional bank correspondent account for a small foreign bank in a higher-risk jurisdiction (per FATF mutual evaluation public reports for that jurisdiction). EDD pack scope: Section 312 EDD on foreign correspondent accounts under 31 CFR 1010.610 [verify section]. Pack assembles: respondent bank ownership and management; respondent's AML program summary based on respondent's questionnaire (Wolfsberg CBDDQ format) and public information; respondent's regulatory standing per home regulator's public registry; nested-correspondent exposure (whether respondent provides correspondent services to other banks); volume and pattern of transactions through the respondent; sanctions exposure through respondent's customer base by jurisdiction. Public criteria reference: FFIEC manual correspondent section; 31 CFR 1010.610 EDD elements (ownership, AML record, supervisory regime, customer base in the U.S.). Reviewer findings: nested-correspondent disclosure incomplete; sanctions exposure through respondent's customer base by jurisdiction not quantified; respondent's regulatory standing current. Recommended gates: EDD committee review with conditions (improved nested-correspondent disclosure within X cycles, transaction volume cap pending).

## Common pitfalls

1. PEP status assessed once at onboarding and treated as immutable. Family / close-associate status, political role changes, and adverse-media accumulation are missed. Mitigation: pack records date-of-assessment and source-of-finding; refresh trigger ties to PEP-status checks.
2. Source of wealth treated as the customer's narrative rather than a documented chain to corroborating evidence. The pack must distinguish statement, corroboration evidence, and residual gap.
3. Adverse media imported as raw hits without linkage analysis. Mitigation: skill cites negative-news-triage outputs where present; pack does not independently re-litigate hit triage.
4. Expected versus actual activity reduced to dollar bands without scenario-link narrative. Pack must connect deviation to specific monitoring scenarios so the EDD committee can act on the deviation.
5. Conduct overlay is folded in as a label rather than an indicator-with-evidence. Mitigation: dedicated conduct-indicators section with evidence pointers and regulator-anchor references.
6. Pack drifts toward a recommendation to retain or exit. Skill recommends gates, decision options, and stop conditions; the EDD committee or approver decides.
7. Beneficial ownership chain stops at the legal-entity certification form layer and ignores trusts, nominees, or layered foreign holding companies. Pack must reflect residual uncertainty at each layer.
