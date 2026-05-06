# fair-lending-test-plan — Phase 1 spec sheet

Date: 2026-05-06
Plugin: consumer-compliance-fair-lending
Phase: 1 (per-skill scoping; no SKILL.md content)

## Activation-tuned description

Drafts a fair-lending test plan covering scope, products, decision points (marketing / underwriting / pricing / steering / servicing / loss mitigation), test types (redlining test, comparative file review, statistical regression on underwriting and pricing, marketing distribution, BISG-based outcomes review), data and evidence requirements, controls hypothesis, and expected outputs. Produces a second-line plan for fair-lending committee review.

Best for:
- Annual fair-lending risk-assessment refresh; the test plan is the operationalization of the risk-assessment.
- Pre-exam fair-lending readiness: regulator has indicated focus on a specific product, MSA, or decision point.
- Targeted plan after complaint themes (cross-reference complaint-theme-analysis) or adverse action review (cross-reference adverse-action-review) surface a fair-lending red flag.
- Integration of an AI / ML decisioning model into the fair-lending testing perimeter.

Not the right tool when:
- The team needs the regression or comparative file review run, not the plan (use a downstream analytics workflow; this skill produces the plan, not the result).
- The question is the adverse action notice itself (use adverse-action-review).
- The question is Section 1071 small-business reporting readiness (use section1071-readiness).
- A specific final fair-lending determination is required (this skill does not finalize; it plans).

Anchored to: ECOA 15 U.S.C. §1691 and Regulation B 12 CFR 1002 (entire); Fair Housing Act 42 U.S.C. §3601–§3619; HMDA / Regulation C 12 CFR 1003; Interagency Fair Lending Examination Procedures (FFIEC, current edition); CFPB Fair Lending Report (most recent annual report); CFPB Circular 2022-03 (May 26, 2022) and CFPB Circular 2023-03 (September 19, 2023) on AI / complex models in credit decisioning; Joint Statement on Enforcement of Civil Rights, Fair Lending, Fair Housing, and Consumer Financial Protection Laws (CFPB / DOJ / FTC / EEOC, April 25, 2023) — algorithmic discrimination; HUD discrimination guidance on AI / algorithmic underwriting [verify exact citation, e.g., 24 CFR 100.500 Disparate Impact Rule, HUD AI guidance updates].

## Source anchors

- ECOA 15 U.S.C. §1691 — prohibition on discrimination in credit transactions.
- Regulation B 12 CFR 1002.4 (general rule), 1002.6 (use of information; effects test), 1002.7 (rules concerning extensions of credit).
- Fair Housing Act 42 U.S.C. §3604, §3605 — prohibition on discrimination in residential real estate transactions; §3606; §3608 affirmative obligation.
- HUD Disparate Impact Rule 24 CFR 100.500 (current text) — disparate impact framework under FHA.
- HMDA / Regulation C 12 CFR 1003 — data points used in mortgage fair-lending testing; LAR fields including action taken, applicant demographics, AUS results, denial reasons, rate spread.
- Interagency Fair Lending Examination Procedures (FFIEC, current edition) [verify edition / date] — comparative file review methodology, scoping factors, statistical analysis expectations.
- CFPB Fair Lending Report (most recent annual report to Congress) [verify edition] — bureau focus areas, enforcement themes, supervisory observations.
- CFPB Circular 2022-03 (May 26, 2022) — adverse action notification with complex algorithms; relevant to model-based underwriting in scope.
- CFPB Circular 2023-03 (September 19, 2023) — adverse action accuracy with AI / complex models.
- Joint Statement on Enforcement of Civil Rights, Fair Lending, Fair Housing, and Consumer Financial Protection Laws (CFPB / DOJ / FTC / EEOC, April 25, 2023) — algorithmic discrimination is enforceable under existing laws.
- HUD guidance on AI / algorithmic underwriting [verify exact title and date — HUD has issued multiple Office of Fair Housing communications post-2023].
- DOJ Combatting Redlining Initiative public statements and consent orders (post-October 2021) — comparator MSA selection, peer set construction.
- CFPB and OCC public consent orders on redlining and pricing discrimination (used as worked-example anchors).
- BISG methodology — CFPB Using publicly available information to proxy for unidentified race and ethnicity (BISG) reference (Summer 2014, with current updates) [verify current methodology document].
- ECOA Reg B 12 CFR 1002.13 — collection of information for monitoring purposes (mortgage and other dwelling-secured credit).

## Sector overlays needed

- `references/sector-overlays/banking.md` — depository specifics: HMDA-reportable mortgage and HELOC, indirect auto, credit card, deposit overdraft fairness, CRA assessment area overlap.
- `references/sector-overlays/capital-markets.md` — securities-based lending fair-lending scope (limited but in-scope where retail); private banking and wealth credit boundary; not principally a fair-lending bucket but call out the perimeter.
- `references/sector-overlays/payments-fintech.md` — sponsor bank model: where fair-lending duty sits between bank and fintech-of-record; BNPL fair-lending under emerging CFPB BNPL guidance [verify]; merchant cash advance fair-lending boundary; data-only-decisioning models with no traditional credit data.
- `references/sector-overlays/insurance.md` — life / health insurance fair-lending boundary (largely state-DOI, not ECOA / FHA); flag scope boundary so reviewers do not over-extend ECOA into insurance.

## Cross-cutting overlays

- AI-related cross-cutting is mandatory on this skill where the in-scope decisioning model is AI / ML. SKILL.md and source-anchors MUST cite the CFPB Circulars (2022-03, 2023-03), the April 2023 Joint Statement on algorithmic discrimination, and HUD AI / algorithmic underwriting guidance. The test plan must include explicit testing of the model for disparate-treatment proxies (use of protected-class-correlated features) and disparate-impact testing (less-discriminatory-alternative search; outcomes testing across protected classes).
- Privacy not applicable as a primary overlay (handled at adverse-action-review).
- Conduct: complaint linkage flagged; not a primary overlay.

## Output template named sections

1. Risk-assessment summary (inputs from prior risk-assessment, complaints, prior testing, regulator focus)
2. Scope (products, decision points, period, geographies, channels)
3. Test perimeter and AI / ML model inventory in scope
4. Test types planned:
   a. Redlining test plan (peer / comparator selection, MSA / assessment area, marketing distribution, branch and LO distribution, application volume disparity, origination disparity, HMDA / 1071 data anchor)
   b. Comparative file review plan (matched-pair design, sampling frame, sample size, exception coding, override review)
   c. Statistical regression on underwriting decisions (model specification, controls, demographic proxy method, software used, statistical-significance threshold)
   d. Statistical regression on pricing (rate spread analysis, margin analysis, fee analysis)
   e. Marketing distribution test (channel, geography, audience targeting, dark-pattern check — cross-reference marketing-claim-review)
   f. Steering test (product placement, LO incentive design)
   g. Servicing and loss mitigation review (where in scope; cross-reference complaint-theme-analysis themes)
5. Data and evidence required (with named system of record per data point and gap flags)
6. Demographic proxy methodology (BISG, surname-only, geocoded; with caveat language)
7. Less-discriminatory-alternative testing plan for AI / ML models
8. Controls hypothesis and named first-line controls being relied on
9. Test owners, reviewers, escalation path, and committee approval gate
10. Reporting plan (test result memo, fair-lending committee deck, regulator-ready summary if needed)
11. Open questions and assumptions (including legal-privilege questions)
12. Source trace and confidence label

## Structured output fields

| Field | Type | Purpose |
|---|---|---|
| `plan_id` | string | Unique reference. |
| `risk_assessment_ref` | string | Link to underlying risk assessment. |
| `scope` | object | Products, decision points, period, geographies, channels. |
| `model_inventory_in_scope[]` | array of objects | Model id, version, decision use, AI/ML flag, vendor or in-house, validation status. |
| `tests[]` | array of objects | One per planned test. |
| `tests[].test_id` | string | Stable reference. |
| `tests[].test_type` | enum | `redlining`, `comparative_file_review`, `regression_underwriting`, `regression_pricing`, `marketing_distribution`, `steering`, `servicing_loss_mit`, `lda_search`, `other`. |
| `tests[].decision_point` | string | Where in the credit lifecycle. |
| `tests[].method` | string | Specification, sampling design, statistical approach. |
| `tests[].demographic_proxy_method` | enum | `BISG`, `surname_only`, `geocoded`, `self_reported_HMDA`, `1071_self_reported`, `n_a`, `other`. |
| `tests[].sample_size` | int | Where applicable. |
| `tests[].data_required[]` | array of objects | Field, system of record, owner, gap flag. |
| `tests[].statistical_threshold` | string | E.g., `p < 0.05`, named effect-size threshold. |
| `tests[].lda_required` | bool | Less-discriminatory-alternative testing required. |
| `tests[].owner` | string | First-line owner. |
| `tests[].reviewer` | string | Second-line reviewer. |
| `tests[].due_date` | date | Plan due date. |
| `tests[].escalation_path` | string | Named committee. |
| `controls_hypothesis[]` | array of strings | Controls being relied on. |
| `committee_approval_gate` | object | Named committee, approval criteria. |
| `legal_privilege_posture` | string | E.g., `attorney-client privileged`, `attorney work-product`, `not privileged`. |
| `open_questions[]` | array of strings | For counsel and committee. |
| `source_trace[]` | array of objects | Claim, source, evidence, confidence. |

## Example scenarios (public-source-derived, anonymous)

1. A regional bank's annual fair-lending risk-assessment refresh focuses on residential mortgage and indirect auto. Plan includes: redlining test on three MSAs flagged by complaint themes and HMDA outlier review; comparative file review of 200 mortgage decisions matched on credit / DTI / LTV; regression on rate-spread for first-lien mortgage purchase loans; LO-channel steering test on the indirect auto book. Demographic proxy: HMDA self-reported for mortgage; BISG for indirect auto. Plan flags an AI / ML pre-screen model used in indirect auto and adds a less-discriminatory-alternative search for that model with a named statistical-significance threshold and a cite-back to CFPB Circular 2023-03. (Pattern derived from public DOJ Combatting Redlining Initiative consent orders and public CFPB enforcement priorities.)

2. A fintech personal-loan platform with sponsor bank uses an alternative-data ML underwriting model. Test plan covers: comparative file review of declines (matched-pair on credit indicia + alternative-data feature buckets); BISG-based regression on the entire underwriting population for a 12-month period; LDA search documented per the bureau's expectation that creditors using AI / complex models actively look for less-discriminatory alternatives; marketing distribution test on the digital-channel acquisition funnel for protected-class skew (cross-reference marketing-claim-review); ECOA Reg B 1002.6 effects-test analysis on a list of features that are race- or ethnicity-correlated. Plan calls out sponsor bank's role and where second-line review duty sits per the sponsor agreement. (Pattern derived from public CFPB and FTC algorithmic discrimination enforcement themes.)

## Common pitfalls

1. The plan is a checklist of test types without a specification per test. A regression with no model spec is not a plan. Mitigation: every test must include method, sample, threshold, and data requirements.
2. Demographic proxy not chosen consciously. Defaulting to BISG everywhere ignores HMDA self-reported demographics, which are stronger evidence for mortgage. Mitigation: per-test demographic proxy field is mandatory and justified.
3. AI / ML models in scope without a less-discriminatory-alternative testing block. Mitigation: where any in-scope decision is AI / ML, LDA testing is required and the spec sheet's source-anchors must cite the CFPB circulars and Joint Statement.
4. Plan ignores marketing distribution and steering. These are decision points before underwriting, where redlining and protected-class targeting also live. Mitigation: scope must explicitly cover marketing and steering, with a cross-reference to marketing-claim-review.
5. Plan written without legal-privilege posture. Fair-lending testing memos can attract privilege; making the posture explicit is a basic discipline. Mitigation: legal_privilege_posture field is mandatory.
6. Plan written without committee approval gate. The plan that is never approved is the plan that is never run. Mitigation: committee_approval_gate is mandatory; the plan is not finalized without it.
7. Skill produces fair-lending findings or runs the tests. It does not. The skill produces the plan; the plan is run by analytics and reviewed by counsel and the fair-lending committee.

## Guardrail (mandatory in SKILL.md)

This skill does not approve loans, deny adverse-action notices, finalize fair-lending determinations, run fair-lending tests, or take any customer-facing action. It produces a fair-lending test plan and surfaces hypotheses and red flags for human decision by qualified fair-lending, model risk, legal, and audit reviewers.
