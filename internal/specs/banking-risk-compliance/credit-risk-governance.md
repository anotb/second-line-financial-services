# credit-risk-governance — spec sheet

Plugin: `banking-risk-compliance`
Phase 2 owner: TBD
Status: spec locked, content build pending

## Activation-tuned description

Reviews second-line credit risk governance for a US bank lending program: credit policy alignment, underwriting framework, risk-rating discipline, concentration governance, allowance methodology oversight, Reg O and Reg W applicability for affiliated and insider credit, and the second-line challenge of first-line lending decisions. Output is the second-line memo a chief credit officer or chief risk officer hands to the credit risk committee or to OCC / FRB / FDIC examiners reviewing credit administration.

Best for:
- A bank is refreshing its credit policy or credit-risk-rating framework and second-line needs to challenge the first-line proposal against public credit-administration expectations.
- A bank is preparing for a credit-administration examination (OCC asset-quality scope, FDIC asset-quality and management scope, FRB BHC consolidated supervision) and needs the credit-governance evidence pack.
- A bank is responding to an MRA on credit risk-rating discipline, ALLL/CECL methodology, concentration management, or insider-lending governance and needs the second-line review artifact.
- A bank is reviewing affiliated-credit or insider-credit transactions for Reg O / Reg W posture before a transaction or as part of a quarterly Reg O reporting cycle.

Not the right tool when:
- The work is fair-lending or ECOA review on consumer or small-business credit. Use `consumer-compliance-fair-lending` skills (when present); credit-risk-governance covers safety-and-soundness lens, not the fair-lending lens (the two reviews are complementary but not the same artifact).
- The work is model-risk validation of a credit scorecard or PD/LGD model. Use `ai-governance-model-risk/skills/validation-plan` (or `model-card-builder` for documentation); this skill covers second-line oversight of model use within the credit framework, not the validation itself.
- The work is the BSA/AML aspect of customer due diligence on a borrower. Use `financial-crime-governance` skills.
- The work is broader than credit (e.g., enterprise risk-appetite review). Use `risk-reporting/skills/risk-committee-pack`.

Anchored to: OCC Comptroller's Handbook — Loan Portfolio Management, Commercial Lending, Retail Lending, Allowances for Credit Losses, Concentrations of Credit, Rating Credit Risk (current editions) [verify edition dates]; FDIC Risk Management Manual of Examination Policies §3.2 (Asset Quality) [verify section]; FRB SR 06-17 (Interagency Policy Statement on the Allowance for Loan and Lease Losses) [verify continued effectiveness post-CECL]; Interagency Guidance on Credit Risk Review Systems (May 2020) replacing OCC Bulletin 2006-47 [verify]; CECL standard (ASC 326-20) and interagency CECL implementation guidance [verify]; Interagency Guidance on Concentrations in Commercial Real Estate Lending (2006) and any subsequent CRE concentration interagency statements [verify current state]; Regulation O (12 CFR Part 215) on extensions of credit to executive officers, directors, principal shareholders, and their related interests; Regulation W (12 CFR Part 223) on covered transactions with affiliates including credit transactions; 12 CFR Part 30 Appendix D (OCC Heightened Standards) §III risk governance framework [verify section] for covered banks.

## Source anchors

Primary:
- Comptroller's Handbook — Loan Portfolio Management [verify current edition]. Use for: portfolio-management framework, concentration management, exception management, loan-review function expectations.
- Comptroller's Handbook — Commercial Lending [verify current edition]. Use for: commercial credit underwriting standards, financial-statement analysis, repayment-capacity evidence.
- Comptroller's Handbook — Retail Lending [verify current edition]. Use for: consumer credit underwriting and credit-administration expectations.
- Comptroller's Handbook — Allowances for Credit Losses [verify current edition reflecting CECL]. Use for: ALLL/ACL methodology, governance, qualitative-factor framework.
- Comptroller's Handbook — Concentrations of Credit [verify current edition]. Use for: concentration risk-management framework, single-name and industry-segment limits.
- Comptroller's Handbook — Rating Credit Risk [verify current edition]. Use for: risk-rating definitions (pass / special mention / substandard / doubtful / loss), rating-discipline expectations, override governance.
- FDIC Risk Management Manual of Examination Policies, §3.2 Asset Quality. Use for: FDIC asset-quality scope, classified-asset treatment, loan-review function expectations.
- Interagency Guidance on Credit Risk Review Systems (May 2020) — joint OCC, FRB, FDIC guidance replacing OCC Bulletin 2006-47. Use for: independence of credit review, scope and frequency, second-line challenge expectations on first-line risk-rating decisions.
- Interagency Guidance on Concentrations in Commercial Real Estate Lending (December 2006), 71 FR 74580, plus the 2015 interagency statement on prudent risk management for CRE lending. Use for: 100%/300% concentration triggers, risk-management framework expectations, board oversight of concentrations.
- ASC 326-20 (CECL) and interagency CECL implementation guidance (joint statements 2016, 2017, 2019) [verify final post-CECL guidance]. Use for: ACL methodology, qualitative-factor governance, model governance for CECL models, sensitivity analysis.
- Regulation O, 12 CFR Part 215. Sections to cite: §215.3 (extensions of credit), §215.4 (general prohibitions), §215.5 (extensions of credit to executive officers), §215.7 (lending limits to insiders), §215.8 (recordkeeping), §215.9 (reports). Use for: insider-credit governance, prior-board-approval requirements, aggregate-limit testing, recordkeeping expectations.
- Regulation W, 12 CFR Part 223. Sections to cite: §223.11 (quantitative limits), §223.12 (collateral), §223.13 (low-quality assets), §223.14 (general purpose covered transactions), §223.16 (exemptions). Use for: covered-transaction tests on credit transactions with affiliates, collateral and quantitative limits.
- 12 CFR Part 30 Appendix D (OCC Heightened Standards). §III risk governance framework, §III.B risk appetite [verify labels]. Use for: covered-bank credit-risk governance evidence — risk-appetite-statement integration, three-lines-of-defense in credit, board credit committee evidence.

Secondary (overlay only):
- FRB Trading and Capital-Markets Activities Manual [verify] for credit-trading, counterparty-credit-risk governance where the program scope extends to capital-markets credit.
- Interagency guidance on credit-loss disclosures and Pillar 3-style disclosures for applicable banks [verify current state].
- CFPB Section 1071 (Regulation B §1002.107) for small-business credit data — referenced as a `[see-also]` for fair-lending overlap; not the primary anchor for this skill.

Public enforcement reference set:
- OCC, FRB, FDIC published consent orders involving credit-administration weaknesses, risk-rating discipline failures, ALLL/CECL governance findings, and Reg O violations [reference by published case docket; do not invent facts].

## Sector overlays needed

This skill is banking-sector-only by definition. No `references/sector-overlays/` subfolder.

## Cross-cutting overlays needed

- `conduct.md` — Optional, where the credit program touches consumer or small-business borrowers and second-line review needs to surface UDAAP exposure on lending practices. Anchors: CFPB UDAAP exam manual.
- `privacy.md` — Optional, where credit-decision data flows touch consumer-protected information.
- `cyber.md` — Not required at v1 (cyber on the lending platform is a TPRM and operational-resilience artifact, not credit-governance).
- `climate.md` — Optional, where the program scope includes climate-related financial risk (CRE in flood zones, transition-risk concentrations). Mark `[verify current supervisory state]`.

## Output template named sections

Top of artifact:
- Scope and source posture (institution type, primary federal regulator, asset size band, Heightened Standards applicability, lending portfolio in scope [commercial, CRE, residential, consumer, specialty], cycle trigger [policy refresh, exam prep, MRA response, transaction review], source posture)
- Confidence label
- Reviewer questions

Body — eight named sections:

1. **Credit policy alignment**
   - Policy version and effective date
   - Policy coverage cross-walk against Comptroller's Handbook expectations (underwriting standards, exception management, documentation, risk-rating, concentration, ALLL/ACL governance, problem-loan management, loan-review independence)
   - Gaps and second-line recommendations

2. **Underwriting framework**
   - Documented underwriting standards by product
   - Exception governance (exception definition, approval authority, aggregate-tracking, board reporting)
   - Underwriting-data adequacy (cash-flow analysis, collateral valuation, guarantor support)
   - Reviewer questions

3. **Risk-rating discipline**
   - Rating scale (pass / special mention / substandard / doubtful / loss; granularity within pass)
   - Rating-assignment process (initial, annual, event-driven)
   - Rating-override governance
   - Concurrence and challenge by credit-review function
   - Backtesting / migration analysis evidence
   - Reviewer questions

4. **Concentration governance**
   - Concentration definitions (single-name, industry, geography, collateral type, structure)
   - Threshold framework (board-approved limits, escalation triggers)
   - CRE concentration position vs interagency 100%/300% triggers (where applicable)
   - Concentration-management memo cadence
   - Reviewer questions

5. **Allowance methodology oversight (ACL/CECL)**
   - Methodology summary (segmentation, loss-rate approach, qualitative-factor framework, reasonable-and-supportable forecast horizon, reversion approach)
   - Governance (model-validation status, qualitative-factor approval, sensitivity analysis, board reporting)
   - Tie to risk-rating discipline (rating migration into expected-loss inputs)
   - Reviewer questions

6. **Reg O and Reg W applicability**
   - Reg O scope: insider population (directors, executive officers, principal shareholders, related interests), covered transactions, prior-approval gate, aggregate lending-limit headroom, §215.5 executive-officer specific limits, §215.8 recordkeeping, §215.9 reporting
   - Reg W scope: affiliate population, covered transactions inventory, §223.11 10%/20% quantitative limits, §223.12 collateral status, §223.13 low-quality-asset prohibition, applicable exemptions
   - Open positions and reviewer questions

7. **Second-line challenge of first-line lending decisions**
   - Sample-based challenge results (concurrence rate, override rate, escalation pattern)
   - Trend in challenge findings
   - Action items for first-line credit
   - Independence of credit-review function (reporting line, scope authority, evidence)

8. **Heightened Standards posture (covered banks)**
   - Risk-appetite-statement coverage of credit risk
   - Three-lines-of-defense maturity in credit
   - Board credit-committee charter and evidence
   - Risk-governance-framework attestation cross-walk for credit

Tail of artifact:
- Recommended owner actions
- Open issues feeding into MRA-tracking or audit pipeline
- Source trace
- Sign-off block

## Structured output fields

Phase 2 adds `schemas/credit-risk-governance-review.schema.json`. Reuses `obligation.schema.json`, `control.schema.json`, `issue.schema.json`.

Wrapper object:
- `review_id`: string.
- `institution`: object. Same fields as in supervision-readiness wrapper.
- `lending_scope`: array of enums. Subset of: `commercial`, `CRE`, `residential`, `consumer`, `specialty`, `capital-markets-credit`.
- `cycle_trigger`: enum. `policy-refresh`, `exam-prep`, `MRA-response`, `transaction-review`, `annual-credit-review`, `concentration-watch`.
- `policy_alignment`: object. `policy_version` (string), `effective_date` (string, ISO date), `gaps` (array of strings).
- `underwriting`: object. `exception_rate_band` (enum: `<5%`, `5-10%`, `10-20%`, `>20%`, `unknown`), `exception_governance_evidence` (string), `gaps` (array).
- `risk_rating`: object. `scale_definition_aligned` (boolean), `override_rate_band` (enum), `migration_analysis_evidence` (string), `gaps` (array).
- `concentrations`: array of objects with `concentration_type` (enum), `current_position` (string), `threshold` (string), `headroom_band` (enum), `governance_evidence` (string), `gap_description` (string).
- `allowance`: object. `methodology_summary` (string), `model_validation_status` (enum: `validated`, `validation-in-progress`, `findings-open`, `not-validated`), `qualitative_factor_governance` (string), `gaps` (array).
- `reg_o`: object. `applicable` (boolean), `insider_inventory_current` (boolean), `aggregate_limit_headroom_band` (enum), `recordkeeping_evidence` (string), `reporting_evidence` (string), `open_positions` (array), `gaps` (array).
- `reg_w`: object. `applicable` (boolean), `affiliate_inventory_current` (boolean), `covered_transactions` (array), `quantitative_limit_position` (string), `collateral_status` (string), `gaps` (array).
- `second_line_challenge`: object. `sample_size` (integer), `concurrence_rate_band` (enum), `findings_summary` (string), `independence_evidence` (string).
- `heightened_standards`: optional object for covered banks. Same shape as in supervision-readiness wrapper.
- `recommended_owner_actions`: array.
- `confidence_label`: enum.
- `human_review_required`: boolean. Always true for v1.

## Example scenarios

### Scenario 1: Mid-size community bank, CRE concentration policy refresh

Input: a community bank ($6B assets, FDIC-regulated state non-member bank) is refreshing its CRE concentration governance after the loan portfolio passed the 300% of total capital interagency CRE concentration trigger. The credit risk committee has commissioned a second-line review of the proposed updated CRE policy. Source posture: public interagency CRE guidance (2006 + 2015 statement) plus internal policy.

Output emphasizes:
- Credit policy alignment: the proposed CRE policy refresh covers 6 of 7 Comptroller's Handbook Concentrations of Credit framework elements; gap on stress-testing of the CRE portfolio (the policy references stress-testing but does not specify methodology, frequency, or board-reporting cadence).
- Underwriting framework: CRE-specific underwriting standards updated for stabilized-vs-construction; exception rate sits in the 5–10% band for the trailing 12 months; one open MRA-equivalent observation that exception aggregate is reported quarterly without trend commentary.
- Risk-rating discipline: CRE-specific rating drivers documented; reviewer question on whether the granular pass-grade distribution is sufficient to support the ACL segmentation approach.
- Concentration governance: current CRE position is 320% of total capital, above the 300% interagency monitoring threshold; the proposed policy raises the internal limit to 350% — second-line recommendation is to require enhanced board reporting at every 25-basis-point step above 300% rather than a single trip-wire at 350%.
- Allowance methodology: CECL methodology uses a vintage-cohort approach for CRE; reviewer question on whether the qualitative factors capture the post-300% concentration risk premium consistently with the policy refresh.
- Reg O / Reg W: not material in this review (no insider-CRE transactions in the trailing 12 months); confirmation that the Reg O officer's quarterly reporting is current.
- Heightened Standards: not applicable (asset size below $50B).
- Recommended owner actions: chief credit officer to specify CRE stress-testing methodology in the policy; head of credit-risk reporting to add monthly trend commentary to exception reporting; ALLL governance committee to refresh qualitative-factor framework alignment with the concentration policy.
- Confidence: high on policy-alignment scope, medium on concentration governance (driven by the 300% trip-wire question), medium on allowance methodology.
- Public-source basis: anchored to Interagency CRE Guidance December 2006 + 2015 statement, Comptroller's Handbook Concentrations of Credit, FDIC Manual §3.2. Anonymous; no named institutions.

### Scenario 2: Reg O quarterly review for a midsize national bank with director-related credit transactions

Input: a midsize national bank ($18B assets, OCC-regulated) runs a quarterly Reg O review. In the current quarter, two new credit transactions involve related interests of two directors and one new transaction involves a related interest of an executive officer. The Reg O officer requests the second-line review pack ahead of the audit committee meeting and a future OCC examination cycle.

Output emphasizes:
- Reg O scope:
  - Insider population is current; insider-list refresh confirmed within last 30 days.
  - Director-related-interest transactions: two new commercial credit lines, one $4M and one $8M; both went through prior board approval per §215.4(b); aggregate lending limit testing complete with 18% of unimpaired-capital-and-surplus headroom remaining.
  - Executive-officer transaction: one $250k mortgage, within §215.5 specific limits for residential mortgage on principal residence; documentation complete.
  - §215.8 recordkeeping evidence: insider-credit register current and reconciled to GL; reviewer question on whether the system-of-record reconciliation control runs monthly or quarterly.
  - §215.9 reporting: Quarterly Report of Insider Lending complete and submitted; reviewer confirmed against the most recent Call Report Schedule RC-M.
- Reg W scope: not applicable in this quarter (no affiliate transactions); confirmation that the affiliate inventory is current.
- Second-line challenge: sample-based challenge of three transactions confirms documentation completeness; one observation that the related-interest determination memo for the $8M transaction is light on the §215.2(n) related-interest analysis (corporate ownership chain).
- Heightened Standards: not applicable (asset size below $50B).
- Recommended owner actions: Reg O officer to refresh the related-interest determination memo for the $8M transaction; head of credit administration to confirm monthly cadence on the §215.8 reconciliation control.
- Open issues: low-severity observation on related-interest documentation.
- Confidence: high on Reg O scope (driven by clean recordkeeping and reporting), medium on related-interest determination depth.
- Public-source basis: anchored to 12 CFR §215.2, §215.4, §215.5, §215.7, §215.8, §215.9. Anonymous.

## Common pitfalls

1. **Treating credit-risk-governance as fair-lending review.** The two are distinct artifacts. Safety-and-soundness credit governance covers underwriting, rating, ALLL, concentration, insider/affiliate. Fair lending covers ECOA, FHA, Reg B, HMDA, Section 1071, disparate impact and treatment. Don't blur the lenses; cross-reference instead.
2. **Skipping Reg O on quarterly cycles when no transactions occurred.** The §215.8 recordkeeping and §215.9 reporting obligations exist regardless of transaction volume. The pack must confirm posture even on quiet quarters.
3. **Confusing risk-rating override with exception management.** A risk-rating override changes the assigned grade away from the rule-based output. An underwriting exception is a deviation from policy at origination. Both have governance but the artifacts differ; the section structure must keep them separate.
4. **Treating the 300% CRE concentration threshold as a hard limit.** The 2006 interagency CRE guidance treats 300% as a monitoring trigger, not a regulatory cap. The pack must phrase it as a trigger for enhanced risk-management expectations, not a violation.
5. **Confusing CECL model validation with second-line credit governance.** CECL model validation is a model-risk function (use `validation-plan`). This skill covers the second-line oversight of how CECL outputs land into credit governance: methodology approval, qualitative-factor governance, and the linkage to risk-rating migration. Don't replicate validation work here.
6. **Skipping the Heightened Standards posture for covered banks.** For $50B+ banks, the credit-risk-governance artifact must include a Heightened Standards section showing risk-appetite-statement coverage of credit risk and three-lines-of-defense maturity. Examiners read this section first.
7. **Citing a Comptroller's Handbook booklet without verifying current edition.** Booklets are revised periodically. Mark `[verify current edition]` when uncertain. Pin the edition date in the source trace.
