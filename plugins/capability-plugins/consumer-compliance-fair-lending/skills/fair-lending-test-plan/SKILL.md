---
name: fair-lending-test-plan
description: |
  Drafts a fair-lending test plan covering scope, products, decision points (marketing, underwriting, pricing, steering, servicing, loss mitigation), planned test types (redlining, comparative file review, statistical regression on underwriting and pricing, marketing distribution, steering), demographic-proxy methodology, less-discriminatory-alternative search where AI or ML models drive credit decisions, data and evidence asks, controls hypothesis, owners, and committee approval gate. The plan is the operationalization of the annual fair-lending risk assessment and the artifact a fair-lending committee approves before any test is run.

  Best for:
  - Annual fair-lending risk-assessment refresh where the test plan is the operationalization of the assessment.
  - Pre-exam fair-lending readiness where a regulator has signaled focus on a specific product, MSA, or decision point.
  - Targeted plan after complaint themes (chain to `complaint-theme-analysis`) or adverse-action review (chain to `adverse-action-review`) surface a fair-lending red flag.
  - Bringing an AI or ML decisioning model into the fair-lending testing perimeter, including a less-discriminatory-alternative search.

  Not the right tool when:
  - The team needs the regression or comparative file review run, not the plan. This skill produces the plan; analytics runs the tests.
  - The question is the adverse-action notice itself (use `adverse-action-review`).
  - The question is Section 1071 small-business reporting readiness (use `section1071-readiness`).
  - A final fair-lending determination is required. The plan is reviewed and approved by counsel and the fair-lending committee; the determination follows the test, not the plan.

  Anchored to: ECOA, Regulation B, Fair Housing Act, HUD Disparate Impact Rule, HMDA / Regulation C, FFIEC Interagency Fair Lending Examination Procedures, CFPB Fair Lending Report, CFPB Circulars, Joint Statement on Enforcement Efforts Against Discrimination and Bias in Automated Systems, HUD FHEO algorithmic-underwriting guidance, CFPB UDAAP Examination Manual, DOJ Combatting Redlining Initiative, CFPB BISG methodology, CFPB Section 1071 small-business data rule.
argument-hint: "[risk-assessment ref, complaint-theme output, adverse-action review output, scope statement, model inventory pointer, or exam-readiness brief]"
---

# Fair-lending test plan

A fair-lending test plan is what the second-line fair-lending team produces so the fair-lending committee, the CCO, and (where directing) outside counsel can approve a year of testing before the first regression runs. It sets the products in scope, the decision points covered, the test types planned, the demographic-proxy method per test, the data and evidence asks, the owners and reviewers, and the named approval gate. The plan is the operationalization of the annual risk assessment; without an approved plan, the test is freelance work.

The skill serves both lenses. A 1.5-line fair-lending analyst inside the business uses it to consolidate the plan as it stands today; a 2-line independent fair-lending reviewer or fair-lending statistician uses the same skill to challenge what was drafted and to surface the test specifications that aren't there yet. The seam between the two is the source-trace block, the open-questions list, and the LDA-search posture for any AI or ML model in the perimeter.

The plan is a draft until the fair-lending committee approves it. Approval is the gate; this skill stops short of running tests, finalizing fair-lending determinations, approving credit decisions, finalizing adverse-action notices, or any customer-facing action.

## Ask yourself first

Most of what the plan needs is on the table by the time someone reaches for this skill. A few things to settle before drafting:

- What triggered the plan. Annual risk-assessment refresh, complaint-theme escalation, adverse-action-review red flag, regulator signal, model deployment into the credit-decisioning path, or a prior testing finding. Trigger drives scope and which upstream artifact the plan consumes.
- Who approves the plan. Fair-lending committee is typical; the CCO, head of fair lending, and outside counsel often co-sponsor. Approver drives audience, format, and the privilege posture.
- What products and decision points are in scope. Mortgage, indirect auto, credit card, unsecured installment, small-business, HELOC, and servicing each have their own data and proxy patterns. Decision points cover marketing, underwriting, pricing, steering, servicing, and loss mitigation; not every plan covers all.
- Whether any AI or ML model drives a credit decision in scope. The answer flips on the LDA-search block, pulls in CFPB Circulars 2022-03 and 2023-03 and the April 2023 Joint Statement, and adds a model-feature review for race- or ethnicity-correlated proxies.
- What the source posture is. Public-only, public-plus-firm-policy, public-plus-firm-policy-plus-evidence, or connector-aware. Source posture sets what the plan can ask for and what carries `[evidence needed]`.

When `engagement-scope` is supplied, the skill consumes it for institution, persona, source posture, sector overlay set, and cross-cutting overlay set. Otherwise it asks the practitioner the few facts it needs and defaults to public posture if the practitioner declines, noting in the plan that scope was not formalized.

## How the plan gets built

The plan has the same spine across products and triggers. A senior practitioner walks it roughly in the order below, but the conversation surfaces sections in whatever order the upstream artifacts and the in-scope inventory arrive; the structured record sorts itself.

**Risk-assessment summary.** What the underlying risk assessment said, which complaint themes, prior testing findings, regulator focal items, and exam-cycle posture feed this plan. Pull from the risk-assessment record, the complaint-theme-analysis output, and the adverse-action-review output where those exist. The summary anchors why each test in the plan exists.

**Scope.** Products, decision points, period, geographies, channels, and explicit exclusions. Servicing and loss mitigation are decision points where complaints often originate; if they're out of scope, name them out. Channels (branch, digital, broker, marketplace, partner-of-record) drive the redlining and steering tests.

**Test perimeter and AI / ML model inventory in scope.** List every model in the credit decisioning path: model id, version, decision use (underwriting score, pricing tier, marketing pre-screen, fraud-deny, adverse-action reason coding), AI/ML flag, in-house or vendor, current validation status, model-card pointer. The inventory feeds the LDA-search list and the model-feature review.

**Test types planned.** Each in-scope test gets its own specification block. The standard set:

- *Redlining test.* Peer or comparator selection (HMDA peer aggregate for mortgage; market peer for non-HMDA), MSA or assessment-area scoping, marketing distribution by census-tract demographic, branch and loan-officer distribution, application-volume disparity, origination-volume disparity, and the data anchor (HMDA LAR, §1071 register where operative). Public DOJ Combatting Redlining Initiative consent orders set the comparator-set construction patterns the plan follows.
- *Comparative file review.* Matched-pair design, sampling frame, sample size, exception-coding scheme, override-review approach. Match variables (credit indicia, DTI, LTV, alternative-data feature buckets where the model uses them) are listed; the matching field set is what the second-line reviewer challenges.
- *Statistical regression on underwriting decisions.* Model specification, named controls (creditworthiness variables, capacity variables, collateral variables for secured products), demographic-proxy method, software, statistical-significance threshold, and the population frame. For mortgage, the proxy is HMDA self-reported demographics; for non-mortgage consumer credit, BISG; for §1071-covered small-business, the §1071 self-reported demographics once operative.
- *Statistical regression on pricing.* Rate-spread analysis (mortgage), margin or markup analysis, fee analysis. Same proxy and threshold framing.
- *Marketing distribution test.* Channel, geography, audience targeting, and a dark-pattern check on digital-channel acquisition. Cross-reference `marketing-claim-review` for content-side disparities.
- *Steering test.* Product placement (where multiple products are available), loan-officer incentive design, and AUS-result-vs-actual-product-placed disparities.
- *Servicing and loss mitigation review.* Where in scope; cross-reference complaint themes for outcome disparities in workout, modification, and default-resolution decisions.
- *Less-discriminatory-alternative search.* Required for any AI/ML model in the underwriting, pricing, or marketing pre-screen path. The search documents the alternatives considered, the disparate-impact metric used to compare, the business-necessity framing for the candidate selected, and the residual disparity. The bureau's framing in CFPB Circular 2023-03 and the April 2023 Joint Statement is that creditors using complex models actively look for less-discriminatory alternatives and document the search.

Each test specification names: `test_id`, `test_type`, `decision_point`, `hypothesis`, `method`, `demographic_proxy_method`, `sample_size` where applicable, `data_required[]` (field, system of record, owner, gap flag), `statistical_threshold`, `lda_required` boolean, `owner` (first line), `reviewer` (second line), `due_date`, and `escalation_path`. A regression with no model spec is not a plan; a comparative file review with no matching variables is not a plan.

**Demographic-proxy methodology.** Per-test field is mandatory because defaulting to BISG everywhere ignores HMDA self-reported demographics, which are stronger evidence for mortgage. Plan documents which proxy applies per test, the proxy-uncertainty handling, and the limits of the method (BISG accuracy varies by geography and surname distribution; the CFPB methodology paper documents the limits).

**Less-discriminatory-alternative testing plan.** Where any in-scope decision is AI/ML, the LDA block lists the alternatives to be tested, the disparate-impact metric, the business-necessity framing, and the residual-disparity benchmark. The block cites CFPB Circular 2022-03, CFPB Circular 2023-03, and the April 2023 Joint Statement (loaded from `references/source-anchors.md`). For dwelling-secured credit, the HUD discriminatory-effects framework under 24 CFR §100.500 applies in parallel.

**Controls hypothesis and named first-line controls being relied on.** What controls in the first line the plan assumes are working: marketing-channel monitoring, underwriting-policy-exception logging, pricing-discretion limits, model-monitoring KRIs. The hypothesis is that the controls operate as designed; the test is partly a test of the controls.

**Test owners, reviewers, escalation path, and committee approval gate.** First-line owner per test, second-line reviewer per test, named escalation forum (fair-lending committee, model risk committee for AI/ML models, AI risk committee where one exists), and the committee approval gate the plan must clear before any test runs.

**Reporting plan.** Test-result memo template, fair-lending committee deck shape, regulator-ready summary template if a regulator request is anticipated. The plan does not draft these; it names the templates the test results will land in.

**Open questions and assumptions.** Privilege posture is mandatory because fair-lending testing memos can attract attorney-client and attorney-work-product privilege; the `legal_privilege_posture` field is filled (`attorney-client-privileged`, `attorney-work-product`, `not-privileged`, or `posture-pending-counsel`). Open questions for counsel and the committee land here. Assumptions list the facts being treated as fixed.

**Source trace and confidence.** Every material claim in the plan cites a source from `references/source-anchors.md` (or the relevant overlay) by file path. Vendor and firm-internal evidence carry separate confidence labels; do not collapse them into one line.

### AI / ML overlay

When any in-scope decision involves an AI or ML model, the AI overlay fires inside the named sections rather than as a separate document:

- *Test perimeter:* the model is named in the inventory with version, decision use, validation status, and model-card pointer (consume `model-card-builder` output where present).
- *Test types:* the LDA-search test is mandatory; a model-feature review for protected-class-correlated proxies is added under the regression-on-underwriting block; a Reg B §1002.6 effects-test framing on the feature list is documented.
- *Adverse-action posture:* CFPB Circulars 2022-03 and 2023-03 anchor the sample of adverse-action notices included in the test perimeter; the plan references but does not duplicate `adverse-action-review`.
- *Source anchors:* the April 2023 Joint Statement, both CFPB AI circulars, and the HUD FHEO algorithmic-underwriting guidance are cited from `references/source-anchors.md`.

The overlay is mandatory once triggered. Missing the LDA-search block on a plan that has an AI/ML model in scope is what the second-line reviewer or the fair-lending statistician flags first when the plan lands for committee.

### Sector overlays

When the engagement scope names a sector, load the matching `references/sector-overlays/<sector>.md`:

- *Banking* — depository specifics: HMDA-reportable mortgage and HELOC, indirect auto, credit card, deposit overdraft fairness, CRA assessment-area overlap.
- *Capital markets* — securities-based lending fair-lending scope (limited but in-scope where retail); private-banking and wealth-credit boundary; not principally a fair-lending bucket but the perimeter is named.
- *Payments-fintech* — sponsor-bank model: where fair-lending duty sits between bank and fintech-of-record per the program agreement; BNPL fair-lending under emerging CFPB BNPL guidance; merchant cash advance fair-lending boundary; data-only-decisioning models with no traditional credit data.
- *Insurance* — life and health insurance fair-lending boundary (state-DOI unfair-discrimination, not ECOA / FHA); flag the scope boundary so reviewers do not over-extend ECOA into insurance.

### Cross-cutting overlays

Conduct overlay loads where the plan crosses UDAAP themes (marketing distribution, dark patterns, steering); cross-reference `udaap-risk-review`. Privacy overlay is not primary on this skill (privacy questions sit on `adverse-action-review` and on the analytics workflow that runs the tests). Climate is not applicable.

## What's load-bearing and what flexes

Load-bearing across every plan: every material claim cites a source from `references/source-anchors.md` (or a loaded overlay) by file path; unsupported claims are marked `[evidence needed]`; section references that cannot be confirmed get `[verify section]` in the source-anchors file (not in the plan body); source evidence, management assertions, public-source obligations, generated inferences, and open legal or compliance questions stay distinguishable; no named institutions appear in narrative unless they are public defendants in a finalized enforcement action with a published consent order; the plan stops at draft and the fair-lending committee approves before any test runs; per-test demographic-proxy field is filled (no default-to-BISG-without-justification); LDA-search block is present whenever an AI/ML model is in scope; `legal_privilege_posture` is filled; `committee_approval_gate` is named.

Flexes to the engagement: plan depth and length scale to the trigger and the in-scope inventory. An annual refresh covering one product reads short; a refresh after a regulator signal covering mortgage, indirect auto, and an AI pre-screen reads longer. Audience drives shape: fair-lending committee deck reads structured; outside-counsel direction memo reads denser; statistician working draft reads in test-spec vocabulary. The sector overlay set drives which `references/sector-overlays/<sector>.md` is loaded; a sponsor-bank fintech program may load two. Source posture (public-only through connector-aware) drives the data-required asks; a public-only plan flags the data fields that would be needed but are not yet accessible.

## Pointers

- `references/source-anchors.md` — citations and excerpts for the named anchors.
- `references/sector-overlays/banking.md`, `insurance.md`, `capital-markets.md`, `payments-fintech.md` — sector-specific framing loaded per engagement-scope.
- `references/cross-cutting/conduct.md` — UDAAP overlap, loaded where marketing distribution, steering, or dark-pattern themes are in scope.
- `references/firm-overlay.md` — firm-installed taxonomy, named committees, fair-lending statistician roster, system-of-record paths (consumed when present).
- `templates/default-output.md` — plan template.
- `schemas/fair-lending-test-plan.schema.json` — structured-output contract.
- `examples/mortgage-redlining-test.md`, `examples/algorithmic-underwriting-test.md` — public-source-derived worked examples.

## Output

Two artifacts: the plan in `templates/default-output.md` shape and a structured record conforming to `schemas/fair-lending-test-plan.schema.json`. The fair-lending committee approves the plan; counsel sets privilege posture; downstream consumers (the analytics workflow that runs the tests, the test-result memo template, the regulator-ready summary template) read the structured record. The schema is the cross-skill contract; additive changes only. Add fields, do not rename or repurpose them. A breaking change is a versioned migration with the downstream consumers told in advance.
