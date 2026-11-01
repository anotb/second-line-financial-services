# Fair Lending Test Plan output template

> Status: draft until the fair-lending committee approves. The plan is the operationalization of the annual fair-lending risk assessment; without an approved plan, the test is freelance work. The skill stops at draft and does not run tests, finalize fair-lending determinations, approve credit decisions, finalize adverse-action notices, or take any customer-facing action.

## Executive summary
- [Trigger and scope in one line]
- [Material risk or focal area driving the plan]
- [Approval gate and committee]

## Scope
| Field | Value |
|---|---|
| Plan ID | `[plan_id]` |
| Risk-assessment reference | `[ra_id]` |
| Trigger | annual-refresh / complaint-theme-trigger / adverse-action-review-trigger / regulator-signal / model-deployment / prior-testing-finding / other |
| As of date | `[YYYY-MM-DD]` |
| Jurisdiction | |
| Institution type | |
| Products in scope | mortgage / indirect-auto / credit-card / unsecured-installment / small-business / HELOC / servicing / other |
| Decision points in scope | marketing / underwriting / pricing / steering / servicing / loss-mitigation |
| Period | `[start] to [end]` |
| Geographies | |
| Channels | branch / digital / broker / marketplace / partner-of-record / sponsor-bank-program-operator |
| Sector overlay set | banking / payments-fintech / capital-markets / insurance |
| Cross-cutting overlay set | conduct (where loaded) |
| Source posture | public-only / public-plus-firm-policy / public-plus-firm-policy-plus-evidence / connector-aware |
| Exclusions | `[explicit out-of-scope items]` |
| Assumptions | |

## Test perimeter and AI / ML model inventory in scope

| Model ID | Version | Decision use | AI/ML | Vendor or in-house | Validation status | Card reference |
|---|---|---|---|---|---|---|
| | | underwriting-score / pricing-tier / marketing-pre-screen / fraud-deny / adverse-action-reason-coding | true / false | vendor / in-house / vendor-fine-tuned | validated / in-validation / not-validated / unknown | |

## Test specifications

One block per planned test. The standard set covered in `SKILL.md` "Test types planned": redlining, comparative file review, regression on underwriting, regression on pricing, marketing distribution, steering, servicing and loss mitigation, less-discriminatory-alternative search, model-feature review (where AI/ML in scope). A regression with no model spec is not a plan; a comparative file review with no matching variables is not a plan. Default the field set; flag what is not yet pinned.

### Test [test_id]

- **Test type**: redlining / comparative-file-review / regression-underwriting / regression-pricing / marketing-distribution / steering / servicing-loss-mitigation / model-feature-review / lda-search
- **Decision point**: marketing / underwriting / pricing / steering / servicing / loss-mitigation / adverse-action
- **Hypothesis**: `[stated as a testable claim, not a question]`
- **Scope**: `[products, period, geographies, channels for this test]`
- **Method**: `[model spec for regression; matched-pair design for comparative file review; comparator-set construction for redlining; audience-skew test for marketing distribution; per SKILL.md test-type guidance]`
- **Demographic-proxy method**: HMDA-self-reported / BISG / §1071-self-reported / geocoded / other
- **Demographic-proxy caveats**: `[BISG accuracy variation, proxy-uncertainty handling, sub-sample reruns]`
- **Sample size** (where applicable): `[n with sampling frame]`
- **Controls / matching variables**: `[creditworthiness, capacity, collateral for secured products; matching field set for comparative file review]`
- **Statistical threshold**: `[p-value, effect-size threshold, SMD threshold; cite firm fair-lending policy or anchor]`
- **Data required**:
  - `{field, system_of_record, owner, gap_flag: available / partial / missing}`
- **LDA required**: yes / no (yes whenever an AI/ML model drives the in-scope decision)
- **LDA method** (where required): `[feature-removal sweep, threshold-adjustment search, alternative-model class trial; per SKILL.md LDA block]`
- **AAN-coverage method** (where the test touches adverse-action reason-coding): `[sample plan, comparison to model-card reasoning, Reg B §1002.9 specificity check]`
- **Owner** (first line): `[role]`
- **Reviewer** (second line): `[role]`
- **Due date**: `[YYYY-MM-DD]`
- **Decision points** (committee gates and stop conditions for this test): `[named forum and stop condition]`
- **Evidence pointers**: `[file paths into the source-anchors file or firm-overlay; redlining cites public DOJ Combatting Redlining Initiative consent-order patterns where applicable]`
- **Escalation path**: `[committee, joint-read forum where applicable]`

> Repeat the block per test. If any field is not yet pinned, flag with `[evidence needed]` rather than leaving blank. Default-and-flag, not gate-and-stop; the second-line reviewer surfaces what is missing in the open-questions section.

## Demographic-proxy methodology

- Per-test method documented above; defaulting to BISG everywhere ignores HMDA self-reported demographics for mortgage. CFPB methodology paper documents BISG limits.
- Proxy-uncertainty handling: `[describe; high-uncertainty subset rerun where applicable]`

## Less-discriminatory-alternative testing plan

(Required where any in-scope decision is AI/ML; per-test LDA blocks are above. Anchors: Reg B §1002.6(a) effects-test framing; HUD 24 CFR §100.500 for dwelling-secured credit; April 2023 Joint Statement. The withdrawn CFPB Circulars 2022-03 / 2023-03 are preserved in `references/source-anchors.md` as historical context.)

- Alternatives to be tested: `[per test_id]`
- Disparate-impact metric: `[metric per test]`
- Business-necessity framing: `[per candidate model]`
- Residual-disparity benchmark: `[threshold or comparator]`

## Controls hypothesis and named first-line controls being relied on

- `[control: marketing-channel monitoring / underwriting-policy-exception logging / pricing-discretion limits / model-monitoring KRIs]`
- The test is partly a test of the controls; name the assumption the plan rests on.

## Test owners, reviewers, escalation path, and committee approval gate

| Role | Name (or role-of-record) | Function |
|---|---|---|
| First-line owner per test | | |
| Second-line reviewer per test | | |
| Named escalation forum | | fair-lending committee / model risk committee / AI risk committee |
| Committee approval gate | | `[forum and approval criteria]` |

## Reporting plan

- Test-result memo template: `[reference]`
- Fair-lending committee deck shape: `[reference]`
- Regulator-ready summary template (where anticipated): `[reference]`

## Open questions and assumptions

- **Legal privilege posture**: attorney-client-privileged / attorney-work-product / not-privileged / posture-pending-counsel
- `[items deferred to counsel and the committee]`
- `[assumptions being treated as fixed]`

## Source trace and confidence

| Claim | Source | Section | Date | URL or file path |
|---|---|---|---|---|
| | | | | |

- Confidence label per major test: high / medium / low / unknown
- Vendor and firm-internal evidence carry separate confidence labels; do not collapse them.

## Decision forum

- Named forum: fair-lending committee / CCO / outside counsel direction / model risk committee / AI risk committee
- Decision status: draft / submitted / in-review / approved / deferred / rejected
- Decision date: `[YYYY-MM-DD]`
- Conditions: `[where applicable]`
