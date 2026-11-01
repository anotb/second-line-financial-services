# Banking sector overlay for fair-lending-test-plan

When the scope record names sector `banking`, this overlay adds banking-specific scope, methodology, and review-gate detail to the fair-lending test plan. Where there is conflict between the capability defaults and this overlay, the overlay governs the banking-sector elements.

Loaded by: `fair-lending-test-plan/SKILL.md` when `scope.sector_overlay_set` includes `banking`, or when the institution type implicates a federal banking regulator (national bank, state member bank, savings association, bank holding company, foreign banking organization with US operations).

Cited and section-referenced anchors live in `references/source-anchors.md`.

## What changes for banking fair-lending test plans

Banking is the heaviest overlay on this skill. Most of the bureau and prudential fair-lending machinery was built for depositories; the test plan inherits that machinery directly.

### 1. Product perimeter

A banking fair-lending test plan typically covers a wider product set than the fintech overlay. Routine plan scope includes:

- HMDA-reportable mortgage (first-lien purchase, first-lien refi, junior-lien refi, home-improvement, HELOC).
- Indirect auto (where the bank is the originator-of-record on third-party-dealer-arranged loans).
- Credit card (originations, line management, repricing, retention offers).
- Unsecured personal loans and overdraft lines of credit.
- Small-business credit (Section 1071 perimeter where the bank is in-scope under the rule's tier phase-in; otherwise, the firm's own small-business fair-lending program).
- Deposit overdraft (where overdraft fairness is treated under the fair-lending program rather than only under UDAAP; firm policy varies on this seam).

CRA assessment-area overlap is load-bearing. Where the fair-lending plan covers a redlining test on an MSA that is also part of the bank's CRA assessment area, the comparator construction and the marketing-distribution evidence interact with the CRA exam preparation work; coordinate with the CRA officer.

### 2. Decision-point coverage

Banking plans typically cover the full set of decision points (marketing, underwriting, pricing, steering, servicing, loss mitigation). Servicing and loss-mitigation review for mortgage is in scope where complaint themes or prior CFPB / OCC focus indicate; servicing fair-lending is doctrinally established under FHA and ECOA but operationally less mature than underwriting and pricing. The plan flags servicing/loss-mit scope explicitly because evidence sources differ (servicer-of-record systems, loss-mit decision logs).

### 3. Demographic proxy methodology

For banks, the proxy choice splits cleanly:

- Mortgage and dwelling-secured products: HMDA self-reported demographics under §1002.13. Stronger evidence than any proxy; use directly.
- Small-business under §1071 once compliance dates apply: §1071 self-reported demographics. Same logic.
- Non-dwelling-secured consumer credit (auto, card, personal): BISG. Record proxy uncertainty; consider geocoded-only or surname-only as sensitivity analysis.

The plan's per-test demographic_proxy_method field is justified per test, not defaulted across the plan.

### 4. Comparative file review machinery

Banking plans typically include comparative file review on at least one product line per cycle. The matched-pair design draws on the FFIEC Interagency Fair Lending Examination Procedures: control group is similarly-situated approved applicants matched on credit and policy-relevant covariates (credit score band, DTI band, LTV band, AUS recommendation, product); test group is the prohibited-basis applicants in the relevant outcome population. Sample size is set by the focal-product population and the firm's policy; 100 to 250 file reviews per product per cycle is the working range though the actual number is set per plan, not by template.

Override and exception coding is the load-bearing detail; the override/exception logs (LO-level pricing exceptions, judgmental denial overrides, secondary-review approvals) are where the comparative-file-review evidence often lives.

### 5. Statistical regression machinery

Banking regression methodology converges on logistic regression for binary outcomes (approve/decline) and OLS regression for continuous outcomes (rate spread, APR, fee). Robust standard errors clustered at the LO or originator level are typical for pricing regressions; the plan should record the clustering choice and rationale.

The model-feature-review test type (per-feature correlation with protected-class proxies; effects-test screen on flagged features) is the bridge between the fair-lending test plan and the model card. Where the bank uses an AUS (Desktop Underwriter, Loan Prospector, in-house equivalent), the AUS recommendation is a control covariate but is not itself out of scope for fair-lending review; the AUS pass-through-deny pattern has bureau focus.

### 6. CFPB authority over banks

CFPB consumer-protection authority reaches large banks (over $10B in assets) for ECOA, RESPA, EFTA, TILA, and UDAAP purposes. Smaller banks fall under the prudential regulator for these areas, but CFPB enforcement reach is not eliminated. Plans for large banks consume the CFPB Fair Lending Report's most recent supervisory-priority signals; plans for smaller banks consume the prudential regulator's exam manual sections.

### 7. Sponsor-bank fair-lending duty

Where the bank operates a sponsor-bank arrangement (deposit, card, lending program for a fintech partner), the fair-lending duty allocates per the program agreement and the bank's own fair-lending program. The interagency third-party guidance (June 2023) anchors the bank-side accountability; the bank's fair-lending second-line typically reviews the program-operator's fair-lending evidence and signs off the test plan jointly with the program-operator's compliance team. The sponsor-bank overlay shows up on the test plan as joint ownership and joint committee approval.

### 8. AI/ML model coverage in scope

Where any in-scope decisioning model is AI/ML, the plan must include:

- Model-feature review (effects-test screen per Reg B §1002.6).
- Less-discriminatory-alternative search (per CFPB Circulars 2022-03 and 2023-03 and the April 2023 Joint Statement). The LDA search includes feature-removal sweeps, threshold-adjustment search, and alternative-model-class trial. Document rejected alternatives.
- Adverse-action notice quality review (per CFPB Circulars 2022-03 and 2023-03). Sample of declined applications, pull the model-score and feature-contribution explanation, compare to the issued notice.

Model-card cross-reference is mandatory: the model card is the firm-side governance artifact, the test plan is the operational verification.

## Banking-specific test-plan template additions

The following fields are added to the plan (mapped to schema where present):

- `scope.cra_assessment_area_overlap` — boolean, true where in-scope geography overlaps the bank's CRA assessment area; CRA officer named as a coordinating reviewer.
- `scope.section_1071_inscope` — boolean, true where small-business products are in-scope under the operative §1071 compliance dates.
- `scope.servicing_loss_mit_inscope` — boolean, true where servicing or loss-mit is in plan scope; servicer-of-record systems named as evidence sources.
- `model_inventory_in_scope[].sponsor_bank_arrangement` — boolean, true for sponsor-bank-program models; cross-reference to program agreement.
- `tests[].aus_treatment` — string, recording how AUS recommendation is handled (control covariate, separate review, exclusion).
- `tests[].clustering_choice` — string, recording standard-error clustering for regressions.
- `committee_approval_gate.cra_officer_coordination` — boolean, true where redlining tests overlap CRA assessment area.

## Common pitfalls in banking fair-lending test plans

- Treating CFPB authority as out of scope because the bank is OCC- or FRB-supervised; CFPB authority reaches large banks for the named consumer-protection statutes.
- Defaulting BISG for mortgage where HMDA self-reported demographics are available; HMDA is stronger evidence and should be used directly.
- Treating AUS recommendation as a clean control covariate without acknowledging that the AUS itself is in the fair-lending perimeter; bureau focus on AUS is established.
- Omitting servicing and loss-mit from plan scope on the assumption that fair-lending is an originations issue; FHA and ECOA reach the full credit transaction.
- Running the test plan in isolation from the model risk machinery on AI/ML models in path; the model card and the test plan are the firm-side and the test-side of the same governance fabric.
- Sponsor-bank programs treated as the program-operator's fair-lending issue; the bank retains accountability under the third-party guidance and the program agreement.
- Writing the plan without coordinating with the CRA officer on overlapping geographies; comparator-MSA selection and the CRA assessment-area construction are not the same exercise but they share evidence sources.
