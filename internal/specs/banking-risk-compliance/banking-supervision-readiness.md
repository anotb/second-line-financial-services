# banking-supervision-readiness — spec sheet

Plugin: `banking-risk-compliance`
Phase 2 owner: TBD
Status: spec locked, content build pending

## Activation-tuned description

Prepares a US bank or bank holding company for a supervisory cycle: CAMELS-component readiness, examiner-letter response readiness, MRA / MRIA closure evidence, and management-action tracking against open supervisory findings. Output is the supervision-readiness pack a chief risk officer or chief compliance officer hands to the OCC, FRB, or FDIC examiner-in-charge at entry, plus the internal cross-walk that ties remediation evidence to specific findings.

Best for:
- A bank is preparing for an OCC, FRB, or FDIC full-scope or targeted examination (safety-and-soundness, compliance, BSA, IT) and needs the entry-meeting pack and CAMELS-component preparation.
- A bank is building the response package to an examiner letter, MRA, MRIA, or a published consent-order requirement and needs the structured cross-walk between finding, action, evidence, and closure status.
- A bank holding company is preparing for an FRB BHC supervisory cycle under SR 12-17 (and successors) and needs the BHC-rated-component readiness view.
- A bank is mid-cycle and needs the issue-status pack for the audit committee or risk committee in advance of a regulator update.

Not the right tool when:
- The work is a generic exam-readiness brief for a non-banking entity (use `regulatory-change-management/skills/exam-brief` for a non-bank or sector-neutral exam).
- The work is a single MRA write-up artifact (use `risk-compliance-core/skills/issue-writeup` for the issue artifact itself; this skill consumes issue-writeup outputs and bundles them).
- The work is a regulatory change impact analysis on new rule text (use `regulatory-change-management/skills/regulatory-impact-assessment`).
- The work is an internal-audit readiness pack (use compliance-testing artifacts).

Anchored to: Federal Reserve SR 12-17 / Bank Holding Company Supervision Manual (current edition) §2000–§5000 [verify section] for BHC supervision and rated components; OCC Comptroller's Handbook, Bank Supervision Process booklet (current edition) [verify edition date] for OCC examination process; FDIC Risk Management Manual of Examination Policies (current edition) Sections 1.1, 4.1, 5.1 [verify section] for FDIC examination scope and CAMELS approach; Uniform Financial Institutions Rating System (CAMELS), revised effective January 1, 1997, codified in interagency guidance and FDIC Manual Section 5.1 [verify]; FFIEC Examination Modernization Project materials (FFIEC press releases and supervisory updates) [verify current effective initiatives]; OCC, FRB, FDIC Heightened Standards (12 CFR Part 30 Appendix D) Sections II–IV [verify section labels] for large covered banks; FRB SR 13-17 / SR 22-3 [verify] for treatment of MRAs and MRIAs and their relationship to supervisory ratings.

## Source anchors

Primary:
- FRB Bank Holding Company Supervision Manual (current edition). Sections to cite: §2000 (rated supervisory framework), §3000 (risk-focused supervision), §4000 (consolidated supervision), §5000 (specialty examinations) [verify section labels]. Use for: BHC supervisory cycle scoping, RFI/C(D) component approach, BHC rating cross-walk.
- FRB SR 12-17 — Consolidated Supervision Framework for Large Financial Institutions (December 17, 2012). Use for: large BHC supervisory framework, areas of focus, governance and risk-management evaluations.
- OCC Comptroller's Handbook — Bank Supervision Process [verify current edition]. Use for: OCC examination cycle, scoping, supervisory letter mechanics, MRA categorization.
- OCC Comptroller's Handbook — relevant topical booklets aligned to CAMELS components: Capital and Dividends; Liquidity; Earnings; Management; Asset Quality (e.g., Allowances for Credit Losses, Concentrations of Credit, Commercial Lending); Sensitivity to Market Risk (Interest Rate Risk). Cite the current-edition booklet for the component being prepared. [verify current edition dates]
- FDIC Risk Management Manual of Examination Policies. Sections to cite: 1.1 (Basic Examination Concepts and Guidelines), 4.1 (Management), 5.1 (Uniform Financial Institutions Rating System), 6.1 (Liquidity and Funds Management), 7.1 (Sensitivity to Market Risk), 8.1 (Internal Routine and Controls). Use for: FDIC-led safety-and-soundness scoping, CAMELS component evidence expectations.
- Uniform Financial Institutions Rating System (CAMELS) — revised composite and component definitions, effective January 1, 1997. Use for: CAMELS component preparation, rating-driver vocabulary in the readiness pack.
- 12 CFR Part 30 Appendix D (OCC Heightened Standards). Sections to cite: II (covered bank), III (risk governance framework), IV (board's role) [verify labels]. Use for: large covered banks ($50B+ avg total consolidated assets) supervisory expectations and board-level reporting evidence.
- FRB SR letters on MRAs and MRIAs [verify which SR letters define and govern, e.g., SR 13-17, SR 22-3]. Use for: MRA / MRIA definitions, expected closure cadence, evidence sufficiency, escalation to enforcement.
- FFIEC Examination Modernization Project — public materials and FFIEC member-agency releases. Use for: current-state references to risk-focused examination, technology-aided examiner workflows, examination scope tailoring.

Secondary (overlay only):
- Comptroller's Handbook — Internal and External Audits, and Compliance booklet. Use for: management-rating evidence (independence of audit and compliance, follow-up on findings).
- FDIC Compliance Examination Manual. Use for: consumer-compliance-component preparation when the cycle includes a compliance examination.
- Interagency Statement on Pandemic Planning [verify current effective] and operational-resilience-related interagency materials. Use for: management-component evidence on resilience.

Public enforcement reference set:
- OCC, FRB, FDIC published consent orders illustrating MRA-to-enforcement progression [reference by published case docket; do not invent facts].

## Sector overlays needed

This skill is banking-sector-only by definition. No `references/sector-overlays/` subfolder.

## Cross-cutting overlays needed

- `cyber.md` — Required. The Management and Sensitivity components increasingly absorb cyber and IT risk; FFIEC IT booklet and 23 NYCRR Part 500 are routine examiner topics for state-chartered banks. Anchors: FFIEC IT Examination Handbook Information Security booklet, NYDFS Part 500, SEC cyber-disclosure framework (for the BHC).
- `conduct.md` — Optional, where the supervisory cycle includes consumer-compliance scope. Anchors: CFPB UDAAP exam manual, FDIC compliance examination manual, OCC consumer-compliance handbook.
- `privacy.md` — Optional, where the cycle includes IT or compliance with information-security overlap. Anchors: GLBA Safeguards Rule (16 CFR 314.4), Reg P (12 CFR 1016).
- `climate.md` — Not required at v1 for general supervision-readiness. Climate-related financial-risk supervision is evolving; flag as a `[verify current state]` reviewer question rather than an embedded overlay.

## Output template named sections

Top of artifact:
- Scope and source posture (institution type [bank, BHC, savings association, IHC], primary federal regulator, asset size band, charter type, exam cycle [full-scope, targeted, point-in-time, BSA, IT, CRA, compliance], cycle dates, source posture)
- Confidence label
- Reviewer questions

Body — three-part structure:

### Part A — CAMELS preparation by component

One subsection per CAMELS component, each with the same internal shape:

1. **C — Capital adequacy**
   - Component summary (capital position, ratios, trends, distribution policy, capital-planning posture)
   - Public criteria (FDIC Manual §3.1 / Comptroller's Handbook Capital and Dividends [verify]; Heightened Standards §IV [verify] for covered banks)
   - Evidence inventory (call report extracts, capital-plan owner sign-off, board capital actions, stress-test results [DFAST / CCAR for applicable BHCs])
   - Open issues and trend
   - Reviewer questions

2. **A — Asset quality**
   - Component summary (concentration profile, classified assets, ALLL/CECL trend, charge-off trend, non-accrual trend, OREO)
   - Public criteria (Comptroller's Handbook Asset Quality booklets; FDIC Manual §3.2; interagency CRE concentration guidance [verify])
   - Evidence inventory (loan-review reports, classified-asset listings, CECL methodology and back-testing, concentration reports)
   - Open issues and trend
   - Reviewer questions

3. **M — Management**
   - Component summary (board oversight, three-lines-of-defense maturity, audit and compliance independence, MRA/MRIA closure trend, governance policies)
   - Public criteria (FDIC Manual §4.1 Management; Heightened Standards §III risk governance framework for covered banks; FRB SR 12-17 governance expectations)
   - Evidence inventory (board minutes redacted to non-confidential, risk-committee charter and minutes, audit-plan coverage, MRA/MRIA closure log)
   - Open issues and trend
   - Reviewer questions

4. **E — Earnings**
   - Component summary (net interest margin, fee-income mix, expense trend, earnings stability, dividend coverage)
   - Public criteria (Comptroller's Handbook Earnings; FDIC Manual §6.1 [verify section])
   - Evidence inventory (call report income statements, budget vs actual, earnings-at-risk reporting)
   - Open issues and trend
   - Reviewer questions

5. **L — Liquidity**
   - Component summary (funding mix, contingency funding plan, LCR/NSFR positions for applicable banks, deposit-runoff assumptions, brokered-deposit reliance)
   - Public criteria (Comptroller's Handbook Liquidity; FDIC Manual §6.1; interagency liquidity risk-management guidance [verify])
   - Evidence inventory (liquidity reports, CFP test record, deposit-concentration reports, broker-deposit listing, sponsor-program FBO-deposit treatment if applicable)
   - Open issues and trend
   - Reviewer questions

6. **S — Sensitivity to market risk**
   - Component summary (interest-rate-risk profile, EVE / NII sensitivities, model governance for IRR models)
   - Public criteria (Comptroller's Handbook Interest Rate Risk; interagency IRR guidance [verify])
   - Evidence inventory (ALCO packs, IRR model validations, back-testing)
   - Open issues and trend
   - Reviewer questions

(For BHC supervisory cycles, replace CAMELS with the RFI/C(D) component framework or successor as applicable [verify current FRB rating system].)

### Part B — Examiner-letter response readiness

For each open or expected examiner-letter item (MRA, MRIA, supervisory recommendation, consent-order article):
- Item ID and source (letter date, finding number, regulator)
- Finding text (verbatim or summary if confidential)
- Component / topical link (CAMELS component, BSA, compliance, IT)
- Action plan summary (named owner, milestones, target dates)
- Evidence pointer (where the closure evidence lives)
- Closure status (open, in-remediation, sustained-remediation, ready-for-validation, closed-pending-examiner-confirmation)
- Aging vs target
- Risk of escalation flag

### Part C — MRA/MRIA closure cross-walk

A matrix view, one row per finding, with columns:
- Finding ID, finding text, regulator, date issued, response date
- Action taken
- Evidence type (policy update, control implementation, training, system change, sustained-operation period)
- Sustained-operation period (months observed)
- Closure-readiness assessment (low / medium / high)
- Owner (named role)
- Last status update date

Tail of artifact:
- Heightened Standards readiness (where applicable): risk-governance framework attestation, board independent-risk-committee evidence, risk-appetite cross-walk, three-lines-of-defense maturity
- Recommended owner actions before entry meeting
- Source trace
- Sign-off block

## Structured output fields

Phase 2 adds `schemas/supervision-readiness.schema.json`. Reuses `issue.schema.json` for individual findings and `control.schema.json` for control evidence.

Wrapper object:
- `pack_id`: string.
- `institution`: object. `legal_name` (string), `type` (enum: `national-bank`, `state-member-bank`, `state-non-member-bank`, `savings-association`, `BHC`, `IHC`), `primary_federal_regulator` (enum: `OCC`, `FRB`, `FDIC`), `asset_size_band` (enum: `<10B`, `10B-50B`, `50B-100B`, `100B-250B`, `>250B`), `heightened_standards_applicable` (boolean).
- `cycle`: object. `type` (enum: `full-scope`, `targeted`, `BSA`, `IT`, `CRA`, `compliance`, `BHC-supervisory`, `point-in-time`), `start_date` (string, ISO date), `end_date` (string, ISO date), `examiner_in_charge_role` (string).
- `camels_components`: array of objects, one per component (`C`, `A`, `M`, `E`, `L`, `S`), each with `component_summary` (string), `evidence_inventory` (array of strings), `open_issue_ids` (array of strings, foreign keys to `issue.schema.json`), `confidence` (enum), `reviewer_questions` (array).
- `bhc_components`: optional, for BHC cycles. Mirrors CAMELS shape with BHC-rating components.
- `examiner_letter_items`: array of objects with `item_id` (string), `source_letter` (object: `regulator`, `letter_date`, `finding_number`), `category` (enum: `MRA`, `MRIA`, `recommendation`, `consent-order-article`, `pre-finding-question`), `finding_text` (string), `component_link` (string), `action_plan_summary` (string), `closure_status` (enum), `evidence_pointer` (string), `aging_days` (integer), `escalation_risk` (enum: `low`, `medium`, `high`).
- `heightened_standards`: optional object for covered banks. `risk_governance_framework_attestation` (boolean), `independent_risk_committee_evidence` (string), `risk_appetite_crosswalk` (string), `three_lines_maturity` (object).
- `recommended_owner_actions`: array.
- `confidence_label`: enum.
- `human_review_required`: boolean. Always true for v1.

## Example scenarios

### Scenario 1: OCC full-scope safety-and-soundness exam — CAMELS readiness for a midsize national bank

Input: a midsize national bank ($35B assets, OCC-regulated, not yet a Heightened Standards covered bank but trending toward the $50B threshold) is six weeks out from an OCC full-scope exam. The exam cycle is a 12-month supervisory plan. The chief risk officer needs the entry-meeting pack and the CAMELS-component preparation. Source posture: public regulatory criteria plus internal evidence from named systems of record.

Output emphasizes:
- Cycle scope: full-scope, OCC-led, 12-month plan, examiner-in-charge from the OCC Northeastern district.
- CAMELS preparation:
  - C: capital position strong; CET1 ratio above well-capitalized threshold; capital-action history clean; reviewer question on capital-planning maturity now that the bank approaches the $50B threshold and Heightened Standards trigger.
  - A: CRE concentration ratio at 280% of total capital, above the 300% threshold trigger in interagency CRE guidance is the watch item; reviewer question on whether the concentration-risk management framework satisfies §III.B.4 [verify] of the CRE guidance; classified-asset trend stable.
  - M: two open MRAs from prior cycle; one is closed-pending-examiner-confirmation, one is in remediation with a 60-day milestone; reviewer questions on independence of internal audit's MRA closure validation.
  - E: earnings stable, NIM under pressure, no flag.
  - L: liquidity well-positioned but contingency funding plan was last tabletop-tested 14 months ago; reviewer recommendation to schedule a CFP test pre-entry.
  - S: IRR exposure within board-approved limits; one model-validation finding open on the EVE model.
- Heightened Standards readiness: the bank is approaching the threshold; the pack includes a placeholder section assessing readiness to comply on a forward-looking basis (not currently applicable).
- Recommended owner actions before entry meeting: schedule CFP tabletop within 30 days; close the older MRA validation; refresh the CRE concentration management memo for the audit committee.
- Confidence: high on C and E; medium on A (CRE concentration), M (MRA closure aging), L (CFP test recency); low on S (model-validation finding).
- Public-source basis: anchored to FDIC Manual §5.1, Comptroller's Handbook (Capital, Asset Quality, Liquidity, Interest Rate Risk), interagency CRE concentration guidance, OCC Bank Supervision Process booklet. Anonymous; no named institutions.

### Scenario 2: MRIA closure cross-walk for a state member bank with an FRB consent order

Input: a state member bank (~$15B assets, FRB-regulated) is operating under an FRB consent order with eight articles spanning BSA/AML, third-party risk, and IT. The bank is preparing the quarterly remediation update for the FRB Reserve Bank, which includes the MRIA closure cross-walk. Two MRIAs are in sustained-operation, three are in remediation, three are still in action-plan stage. Source posture: public consent order text plus internal evidence.

Output emphasizes:
- Examiner-letter response readiness section: eight-row table with action plan, evidence pointer, and closure status for each consent-order article; named role owners for each (BSA officer for BSA articles, head of vendor management for TPRM articles, CIO for IT articles).
- MRIA closure cross-walk: two findings ready for examiner validation, three with sustained-operation periods of 4, 6, and 8 months respectively (the bank's policy targets 12 months before requesting validation, so reviewer question whether earlier validation is acceptable to the FRB), three with action plans dated within last 30 days.
- CAMELS-component link: M-component evidence package highlights the consent-order remediation cadence, board oversight minutes, and independence of internal audit's validation.
- Heightened Standards: not applicable (asset size below $50B). Reviewer note that the FRB applies enhanced expectations for institutions under consent orders regardless of asset size.
- Aging analysis: oldest open action item is 14 months old, against the bank's internal target of 12 months; escalation risk flagged as medium.
- Recommended owner actions: BSA officer to formalize sustained-operation evidence package for the two ready-for-validation findings; head of vendor management to accelerate one TPRM action-plan target by 60 days; chief audit executive to confirm independent validation cadence.
- Confidence: high on closed and in-validation items, medium on in-remediation, low on action-plan-only items.
- Public-source basis: anchored to FRB Bank Holding Company Supervision Manual, FRB SR 13-17 [verify] / SR 22-3 [verify] on MRA/MRIA framework, the public FRB consent order text. Anonymous; consent order referenced by docket only.

## Common pitfalls

1. **Treating the pack as a generic risk inventory.** The CAMELS / BHC components are the spine. A pack that does not organize by component is a risk register, not a supervision-readiness pack — examiners skim component-by-component.
2. **Confusing MRA with MRIA.** MRAs are matters requiring attention; MRIAs are matters requiring immediate attention. Aging tolerance, escalation risk, and board-reporting expectations differ. The pack must categorize correctly. If the regulator labels the item differently than the bank's tracker, defer to the regulator's label.
3. **Over-claiming closure readiness.** Closure-readiness `high` requires a documented sustained-operation period (firms typically use 6–12 months internally; examiners apply judgement). A pack that marks every item closure-ready without sustained-operation evidence reads as overconfident and triggers examiner skepticism. Default to medium when the sustained-operation period is below the firm's policy threshold.
4. **Skipping Heightened Standards readiness for banks approaching the threshold.** 12 CFR Part 30 Appendix D applies to covered banks ($50B+ avg total consolidated assets). Banks at $40B+ approaching the threshold need a forward-looking readiness section even if the framework is not yet binding, because OCC examiners will probe it.
5. **Treating board minutes as the only Management-component evidence.** Minutes are necessary but insufficient. The Management component pulls from internal-audit independence, compliance independence, MRA closure trend, three-lines-of-defense maturity, and risk-appetite calibration. Build the evidence inventory across all of these.
6. **Listing an FFIEC Examination Modernization reference without confirming current effective state.** The Project's deliverables and effective initiatives evolve. Mark as `[verify current state]` when the pack relies on a specific Modernization Project initiative.
7. **Not differentiating BHC supervisory cycle from depository-institution cycle.** A BHC cycle uses the FRB BHC supervision framework and the BHC rating system; a depository institution cycle uses CAMELS. A holding-company organization typically gets both in different forms — the pack must be built for the cycle in scope, not collapsed into one.
