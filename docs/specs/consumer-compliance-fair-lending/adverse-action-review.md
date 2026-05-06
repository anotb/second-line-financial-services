# adverse-action-review — Phase 1 spec sheet

Date: 2026-05-06
Plugin: consumer-compliance-fair-lending
Phase: 1 (per-skill scoping; no SKILL.md content)

## Activation-tuned description

Reviews a portfolio of adverse action decisions and notices for ECOA / Regulation B compliance: timing, content, specific-reason accuracy, traceability of cited reasons back to the model and data, and disparate-impact red flags. Produces a reviewable second-line memo that flags non-compliant notices, model-supported reason gaps, and likely fair-lending concerns for human decision.

Best for:
- A consumer compliance team is sampling adverse action notices (declines, counter-offers, terms-less-favorable) on a credit product and needs a second-line review of the notice population against Reg B 1002.9.
- Model risk or fair-lending review of a credit decision model (including AI / ML scorecards) where adverse action reasons are produced from feature contributions; reviewer needs to test that the cited reasons are the principal reasons supported by the model.
- Triage of consent-order remediation around adverse action notice deficiencies (post-CFPB / FDIC / OCC enforcement).

Not the right tool when:
- The question is the underwriting model's predictive performance or stability (use ai-governance-model-risk validation-plan).
- The question is the pricing tier or ATR calculation, not the adverse action notice (use compliance-testing or product-level review).
- The reviewer needs a final fair-lending determination or a credit decision (this skill does not approve, deny, or finalize; it surfaces red flags).

Anchored to: ECOA 15 U.S.C. §1691; Regulation B 12 CFR 1002.9 (notification of action taken); 12 CFR 1002.9(a)(2) (statement of specific reasons); 12 CFR 1002.9(b)(2) (form of ECOA notice); CFPB Circular 2022-03 (May 26, 2022, adverse action notification requirements in connection with credit decisions based on complex algorithms); CFPB Circular 2023-03 (September 19, 2023, adverse action notices and the use of AI / complex credit models — specific and accurate reasons); Joint Statement on Enforcement of Civil Rights, Fair Lending, Fair Housing, and Consumer Financial Protection Laws (CFPB / DOJ / FTC / EEOC, April 2023); Fair Housing Act 42 U.S.C. §3604–§3605.

## Source anchors

- ECOA 15 U.S.C. §1691(d) — adverse action statement of reasons requirement.
- Regulation B 12 CFR 1002.2(c) — definition of adverse action.
- Regulation B 12 CFR 1002.9(a)(1) — timing: 30 days after receiving completed application; 30 days after counteroffer not accepted; 90 days for incomplete applications under §1002.9(c).
- Regulation B 12 CFR 1002.9(a)(2)(i) — statement of specific reasons or disclosure of right to request.
- Regulation B 12 CFR 1002.9(b)(2) — content and form of the ECOA notice (with FCRA and disparate-treatment overlay where applicable).
- Official Staff Commentary to Regulation B §1002.9 — specificity standard, principal reasons, prohibited generic phrasing.
- CFPB Circular 2022-03 (May 26, 2022) — confirms that ECOA's specific-reason requirement applies to creditors using complex algorithms; "the technology is too complex" is not a defense.
- CFPB Circular 2023-03 (September 19, 2023) [verify exact title and date] — adverse action notices using AI / complex credit models; reasons must be specific and accurate, not boilerplate sample-form reasons that do not actually reflect the basis for the action.
- Joint Statement on Enforcement of Civil Rights, Fair Lending, Fair Housing, and Consumer Financial Protection Laws (CFPB / DOJ / FTC / EEOC, April 25, 2023) — algorithmic discrimination is enforceable under existing laws; agencies will use existing authorities.
- Fair Housing Act 42 U.S.C. §3604, §3605 — discrimination in residential real estate transactions including dwelling-secured credit.
- Fair Credit Reporting Act 15 U.S.C. §1681m — adverse action overlay where credit report or risk score was used (Reg V 12 CFR 1022.74).
- CFPB consent orders on adverse action notice deficiencies (public dockets) — used as example anchors only; cite by name and date when used.
- Recent CFPB / FRB / OCC supervisory observations on adverse action notice quality [verify edition].

## Sector overlays needed

- `references/sector-overlays/banking.md` — depository creditor scope under Reg B; FCRA risk-score disclosure (Reg V) overlay; HMDA-reportable HELOC and mortgage flow; CRA assessment area considerations.
- `references/sector-overlays/capital-markets.md` — securities-based lending and margin call as adverse action treatment; broker-dealer credit extension; treatment of institutional vs. retail.
- `references/sector-overlays/payments-fintech.md` — sponsor bank vs. fintech-of-record responsibility; BNPL adverse action treatment under Reg Z and Reg B (CFPB 2024 BNPL interpretive rule on Reg Z [verify]); fintech model-risk review depth where decisioning is vendor-supplied.
- `references/sector-overlays/insurance.md` — bank-affiliated insurance products where credit-style decisioning is used (limited scope); generally insurance underwriting is NAIC / state DOI rather than ECOA, so this overlay flags scope boundary not duty.

## Cross-cutting overlays

- `references/cross-cutting/privacy.md` — GLBA Safeguards Rule 16 CFR 314 (data used in adverse action analytics is customer NPI); state privacy implications (CCPA / CPRA, Colorado, Virginia, Connecticut etc. — varies by state, evolving) [verify state-specific scope]; treatment of consumer attribute data (BISG-derived race/ethnicity proxies) under privacy and fair-lending tension.
- (AI-related cross-cutting is implicit on this skill.) MUST cite CFPB Circulars 2022-03 and 2023-03 and the April 2023 Joint Statement on algorithmic discrimination. Where the underlying decision model is AI / ML, the spec sheet's source-anchors and SKILL.md must reflect that the reason population available to cite must come from the model, not from a stock list of FCRA reason codes.

Climate not applicable. Conduct not applicable as a primary overlay (overlap with udaap-risk-review, but adverse action review is principally an ECOA / fair-lending artifact).

## Output template named sections

1. Decision summary (population reviewed, sampling basis, reviewer, period)
2. Specific reasons cited (per-notice, normalized)
3. Reasons supported by underlying model and data (per-notice, with feature contribution evidence and gap flags)
4. Reg B 1002.9 timing compliance (per-notice, with evidence)
5. Reg B 1002.9 content compliance (per-notice — completeness, ECOA notice text, FCRA overlay if applicable)
6. Race / ethnicity / sex disparate-impact red flags (decline rate disparity, reason-mix disparity, BISG-flagged geographies)
7. AI / complex-model specific findings (cite-back to CFPB Circular 2022-03, 2023-03; Joint Statement)
8. Recommended action (notice re-issuance, model reason-generation fix, fair-lending escalation, training, control change)
9. Open legal / compliance questions for counsel
10. Source trace and confidence label

## Structured output fields

| Field | Type | Purpose |
|---|---|---|
| `review_id` | string | Unique reference for this review. |
| `population` | object | Product, decision type, period, count, sampling basis. |
| `decisions[]` | array of objects | One per sampled decision. |
| `decisions[].decision_id` | string | Internal reference. |
| `decisions[].action` | enum | `denial`, `counteroffer_not_accepted`, `terms_less_favorable`, `incomplete_application`, `existing_account_action`. |
| `decisions[].notice_sent_at` | date | Timing evidence. |
| `decisions[].application_completed_at` | date | Reg B 1002.9(a)(1) start of clock. |
| `decisions[].timing_compliant` | enum | `yes`, `no`, `unverifiable`. |
| `decisions[].reasons_cited[]` | array of strings | As they appear on the notice. |
| `decisions[].reasons_model_supported[]` | array of objects | Reason text, feature reference, contribution score, supported `yes`/`no`/`indeterminate`. |
| `decisions[].fcra_overlay_applied` | bool | Risk score disclosure required under Reg V 1022.74? |
| `decisions[].content_compliant` | enum | `yes`, `no`, `partial`. |
| `decisions[].red_flags[]` | array of strings | E.g., `generic_reason_only`, `model_reason_mismatch`, `protected_class_proxy_in_reasons`. |
| `disparate_impact_signals` | object | Decline rate by demographic proxy, reason-mix variance, BISG-derived race / ethnicity geographies, p-values where computed. |
| `model_reason_generation_review` | object | For AI / complex-model decisions: method (SHAP, LIME, leave-one-out, monotonic constraint trace), validation evidence, gap notes. |
| `recommended_actions[]` | array of objects | Action, owner, due date, named control. |
| `open_questions[]` | array of strings | For counsel. |
| `source_trace[]` | array of objects | Claim, source, evidence, confidence. |

## Example scenarios (public-source-derived, anonymous)

1. A regional bank uses an XGBoost-based credit decisioning model for unsecured personal loans. The adverse action notice template draws reasons from a fixed list of 20 FCRA-style reason codes mapped to feature buckets. A second-line sample of 200 declines from Q3 finds: 18% of notices cite "length of credit history" but the model's top-3 SHAP contributions for those decisions are dominated by debt-to-income and recent inquiries; 6% of notices cite "value of collateral" on unsecured loans (impossible mapping). Cite-back to CFPB Circular 2023-03 on accuracy of cited reasons and Circular 2022-03 on complex-algorithm specificity. Recommended action: notice re-issuance for the 6% impossible-mapping subset; model reason-generation fix; control change to validate reason-feature mapping in the model release process. (Pattern derived from public CFPB enforcement themes on adverse action notices using complex models.)

2. A national bank's mortgage origination platform issued adverse action notices on 1,400 declined HMDA-reportable applications in a quarter. Sample review surfaces: 9 notices sent on day 33 from completed application date (Reg B 1002.9(a)(1) timing breach); a recurring "credit application incomplete" reason cited where the application was actually complete (content breach); BISG analysis shows the decline-rate disparity for one MSA at the 99th percentile vs. comparison MSAs in the same footprint, which is a redlining red flag (cross-references to fair-lending-test-plan). Recommended action: notice re-issuance on the 9 timing breaches; fair-lending team escalation on the redlining red flag; supervisor sign-off on a comparative file review and HMDA outlier review. (Pattern derived from public CFPB / DOJ redlining consent orders.)

## Common pitfalls

1. Reviewing notices without pulling the underlying decision data and model output. Reasons cited may pass a Reg B content check on the face but fail the CFPB Circular 2023-03 accuracy standard. Mitigation: every sampled decision must include feature contribution evidence or a `[evidence needed]` flag.
2. Treating "the model is a black box" as a defense. CFPB Circular 2022-03 forecloses this. Mitigation: SKILL.md and source-anchors must explicitly cite the circular and the firm must produce an explainability artifact for any AI / complex model used in adverse action.
3. Conflating ECOA Reg B notice with FCRA risk-score disclosure. Reg V 12 CFR 1022.74 may also apply. Mitigation: per-decision FCRA overlay flag, with separate compliance check.
4. Missing the disparate-impact dimension. Adverse action review is the most common entry point to a redlining or pricing fair-lending finding. Mitigation: include race / ethnicity / sex decline-rate disparity and reason-mix disparity panels every time, even if BISG only.
5. BISG used as if it were ground truth on race / ethnicity. It is a probabilistic proxy. Mitigation: report disparities as signals with the BISG caveat, not as findings of disparate impact; escalate to formal fair-lending testing for finding-grade work (cross-reference fair-lending-test-plan).
6. Notice population reviewed without reference to counter-offers or terms-less-favorable actions, which are also adverse action under Reg B 1002.2(c). Mitigation: scope must enumerate all Reg B 1002.2(c) categories.
7. Skill produces a final fair-lending determination or instructs notice re-issuance. The skill does not. It surfaces red flags and recommends action for human decision. Mitigation: every output ends with a "Recommended action" section with named owner, not an executed action.

## Guardrail (mandatory in SKILL.md)

This skill does not approve loans, deny adverse-action notices, finalize fair-lending determinations, or take any customer-facing action. It produces review artifacts and surfaces red flags for human decision by qualified compliance, fair-lending, model risk, and legal reviewers.
