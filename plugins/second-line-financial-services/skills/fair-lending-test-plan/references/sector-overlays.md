# sector-overlays

One section per sector. Read only the sections the scope calls for.

## banking

### Banking sector overlay for fair-lending-test-plan

When the scope record names sector `banking`, this overlay adds banking-specific scope, methodology, and review-gate detail to the fair-lending test plan. Where there is conflict between the capability defaults and this overlay, the overlay governs the banking-sector elements.

Loaded by: `fair-lending-test-plan/SKILL.md` when `scope.sector_overlay_set` includes `banking`, or when the institution type implicates a federal banking regulator (national bank, state member bank, savings association, bank holding company, foreign banking organization with US operations).

Cited and section-referenced anchors live in `references/source-anchors.md`.

#### What changes for banking fair-lending test plans

Banking is the heaviest overlay on this skill. Most of the bureau and prudential fair-lending machinery was built for depositories; the test plan inherits that machinery directly.

##### 1. Product perimeter

A banking fair-lending test plan typically covers a wider product set than the fintech overlay. Routine plan scope includes:

- HMDA-reportable mortgage (first-lien purchase, first-lien refi, junior-lien refi, home-improvement, HELOC).
- Indirect auto (where the bank is the originator-of-record on third-party-dealer-arranged loans).
- Credit card (originations, line management, repricing, retention offers).
- Unsecured personal loans and overdraft lines of credit.
- Small-business credit (Section 1071 perimeter where the bank is in-scope under the rule's tier phase-in; otherwise, the firm's own small-business fair-lending program).
- Deposit overdraft (where overdraft fairness is treated under the fair-lending program rather than only under UDAAP; firm policy varies on this seam).

CRA assessment-area overlap is load-bearing. Where the fair-lending plan covers a redlining test on an MSA that is also part of the bank's CRA assessment area, the comparator construction and the marketing-distribution evidence interact with the CRA exam preparation work; coordinate with the CRA officer.

##### 2. Decision-point coverage

Banking plans typically cover the full set of decision points (marketing, underwriting, pricing, steering, servicing, loss mitigation). Servicing and loss-mitigation review for mortgage is in scope where complaint themes or prior CFPB / OCC focus indicate; servicing fair-lending is doctrinally established under FHA and ECOA but operationally less mature than underwriting and pricing. The plan flags servicing/loss-mit scope explicitly because evidence sources differ (servicer-of-record systems, loss-mit decision logs).

##### 3. Demographic proxy methodology

For banks, the proxy choice splits cleanly:

- Mortgage and dwelling-secured products: HMDA self-reported demographics under §1002.13. Stronger evidence than any proxy; use directly.
- Small-business under §1071 once compliance dates apply: §1071 self-reported demographics. Same logic.
- Non-dwelling-secured consumer credit (auto, card, personal): BISG. Record proxy uncertainty; consider geocoded-only or surname-only as sensitivity analysis.

The plan's per-test demographic_proxy_method field is justified per test, not defaulted across the plan.

##### 4. Comparative file review machinery

Banking plans typically include comparative file review on at least one product line per cycle. The matched-pair design draws on the FFIEC Interagency Fair Lending Examination Procedures: control group is similarly-situated approved applicants matched on credit and policy-relevant covariates (credit score band, DTI band, LTV band, AUS recommendation, product); test group is the prohibited-basis applicants in the relevant outcome population. Sample size is set by the focal-product population and the firm's policy; 100 to 250 file reviews per product per cycle is the working range though the actual number is set per plan, not by template.

Override and exception coding is the load-bearing detail; the override/exception logs (LO-level pricing exceptions, judgmental denial overrides, secondary-review approvals) are where the comparative-file-review evidence often lives.

##### 5. Statistical regression machinery

Banking regression methodology converges on logistic regression for binary outcomes (approve/decline) and OLS regression for continuous outcomes (rate spread, APR, fee). Robust standard errors clustered at the LO or originator level are typical for pricing regressions; the plan should record the clustering choice and rationale.

The model-feature-review test type (per-feature correlation with protected-class proxies; effects-test screen on flagged features) is the bridge between the fair-lending test plan and the model card. Where the bank uses an AUS (Desktop Underwriter, Loan Prospector, in-house equivalent), the AUS recommendation is a control covariate but is not itself out of scope for fair-lending review; the AUS pass-through-deny pattern has bureau focus.

##### 6. CFPB authority over banks

CFPB consumer-protection authority reaches large banks (over $10B in assets) for ECOA, RESPA, EFTA, TILA, and UDAAP purposes. Smaller banks fall under the prudential regulator for these areas, but CFPB enforcement reach is not eliminated. Plans for large banks consume the CFPB Fair Lending Report's most recent supervisory-priority signals; plans for smaller banks consume the prudential regulator's exam manual sections.

##### 7. Sponsor-bank fair-lending duty

Where the bank operates a sponsor-bank arrangement (deposit, card, lending program for a fintech partner), the fair-lending duty allocates per the program agreement and the bank's own fair-lending program. The interagency third-party guidance (June 2023) anchors the bank-side accountability; the bank's fair-lending second-line typically reviews the program-operator's fair-lending evidence and signs off the test plan jointly with the program-operator's compliance team. The sponsor-bank overlay shows up on the test plan as joint ownership and joint committee approval.

##### 8. AI/ML model coverage in scope

Where any in-scope decisioning model is AI/ML, the plan must include:

- Model-feature review (effects-test screen per Reg B §1002.6).
- Less-discriminatory-alternative search (per CFPB Circulars 2022-03 and 2023-03 and the April 2023 Joint Statement). The LDA search includes feature-removal sweeps, threshold-adjustment search, and alternative-model-class trial. Document rejected alternatives.
- Adverse-action notice quality review (per CFPB Circulars 2022-03 and 2023-03). Sample of declined applications, pull the model-score and feature-contribution explanation, compare to the issued notice.

Model-card cross-reference is mandatory: the model card is the firm-side governance artifact, the test plan is the operational verification.

#### Banking-specific test-plan template additions

The following fields are added to the plan (mapped to schema where present):

- `scope.cra_assessment_area_overlap` — boolean, true where in-scope geography overlaps the bank's CRA assessment area; CRA officer named as a coordinating reviewer.
- `scope.section_1071_inscope` — boolean, true where small-business products are in-scope under the operative §1071 compliance dates.
- `scope.servicing_loss_mit_inscope` — boolean, true where servicing or loss-mit is in plan scope; servicer-of-record systems named as evidence sources.
- `model_inventory_in_scope[].sponsor_bank_arrangement` — boolean, true for sponsor-bank-program models; cross-reference to program agreement.
- `tests[].aus_treatment` — string, recording how AUS recommendation is handled (control covariate, separate review, exclusion).
- `tests[].clustering_choice` — string, recording standard-error clustering for regressions.
- `committee_approval_gate.cra_officer_coordination` — boolean, true where redlining tests overlap CRA assessment area.

#### Common pitfalls in banking fair-lending test plans

- Treating CFPB authority as out of scope because the bank is OCC- or FRB-supervised; CFPB authority reaches large banks for the named consumer-protection statutes.
- Defaulting BISG for mortgage where HMDA self-reported demographics are available; HMDA is stronger evidence and should be used directly.
- Treating AUS recommendation as a clean control covariate without acknowledging that the AUS itself is in the fair-lending perimeter; bureau focus on AUS is established.
- Omitting servicing and loss-mit from plan scope on the assumption that fair-lending is an originations issue; FHA and ECOA reach the full credit transaction.
- Running the test plan in isolation from the model risk machinery on AI/ML models in path; the model card and the test plan are the firm-side and the test-side of the same governance fabric.
- Sponsor-bank programs treated as the program-operator's fair-lending issue; the bank retains accountability under the third-party guidance and the program agreement.
- Writing the plan without coordinating with the CRA officer on overlapping geographies; comparator-MSA selection and the CRA assessment-area construction are not the same exercise but they share evidence sources.

## capital-markets

### Capital markets sector overlay for fair-lending-test-plan

When the scope record names sector `capital-markets`, this overlay adds the narrow set of capital-markets fair-lending considerations to the test plan. The overlay is short on purpose: most capital-markets activity sits outside the ECOA and FHA perimeter. Where it does touch, the touch points are predictable.

Loaded by: `fair-lending-test-plan/SKILL.md` when `scope.sector_overlay_set` includes `capital-markets`, or when the institution type implicates a broker-dealer, investment adviser, private bank, or wealth-management entity that extends credit to retail clients.

Cited and section-referenced anchors live in `references/source-anchors.md`.

#### What changes for capital-markets fair-lending test plans

##### 1. Scope boundary first

Most capital-markets activity is not in fair-lending scope. Securities trading, asset management, institutional brokerage, and investment-adviser portfolio management do not extend credit; ECOA does not reach them. The capital-markets fair-lending perimeter is narrow:

- Securities-based lending (SBL) to retail clients (including individual customers of private-bank and wealth-management businesses).
- Margin lending to retail customers (subject to FINRA Rule 4210 and Reg T; the credit-decision component is in ECOA scope).
- Mortgage origination by capital-markets-affiliated entities (where the bank holding company operates a mortgage subsidiary; the mortgage entity carries the banking-overlay machinery).
- Wealth-credit products (jumbo mortgages, lines of credit secured by assets) where the bank or broker-dealer is the creditor.

Activity that is not credit (advisory recommendations, trade execution, custody) is outside fair-lending scope. Sales-practice fairness and best-interest framing apply (Reg BI for broker-dealers, fiduciary duty for advisers) but those are not ECOA tests.

##### 2. SBL and margin-lending test plan content

Where SBL or retail margin lending is in scope, the test plan applies the regular ECOA machinery:

- Underwriting decision review (eligibility, line-size determination).
- Pricing review (rate spread, fee determination).
- Marketing distribution review (where SBL or margin is marketed to a defined retail audience).
- Demographic proxy method: BISG; record proxy-uncertainty handling. The wealth-customer demographic distribution may be skewed in ways that affect proxy accuracy.

LDA search applies where any AI/ML model drives the decision. Most retail SBL and margin-eligibility decisions are model-light or judgmental; record the model inventory honestly and scope LDA where it actually applies.

##### 3. Wealth-credit boundary

Wealth-credit products to high-net-worth and ultra-high-net-worth clients raise an under-discussed fair-lending question: the addressable population for these products is itself skewed by wealth concentration, which correlates with race and ethnicity. The test plan should record this as an open question for the fair-lending committee where the institution is sizing a wealth-credit fair-lending review for the first time. The plan does not resolve the question; it surfaces it.

##### 4. Non-applicability for trading-and-execution activity

Trading desks, execution algorithms, market-making, and surveillance models are out of fair-lending scope. They sit under Rule 15c3-5 (broker-dealer market-access controls), FINRA supervision rules, SEC market-integrity rules, and the firm's market-conduct framework. Do not extend the fair-lending test plan into trading activity; flag the scope boundary and refer to the firm's market-conduct surveillance program.

#### Capital-markets-specific test-plan template additions

- `scope.product_perimeter` includes a capital-markets enum: `securities-based-lending`, `retail-margin`, `wealth-mortgage`, `wealth-line-of-credit`. Trading and execution products are excluded.
- `scope.wealth_population_caveat` — boolean; if true, wealth-population-skew open question is recorded for committee.
- `committee_approval_gate.private_bank_or_wealth_committee` — boolean; private-bank or wealth-management committee approval may join the fair-lending committee approval where the products are in their book.

#### Common pitfalls in capital-markets fair-lending test plans

- Extending fair-lending scope into trading and execution activity; the perimeter is credit, not market activity.
- Treating SBL and margin as out of scope because they are capital-markets products; the credit-decision component is in ECOA scope.
- Ignoring the wealth-population-skew question; the test plan should at minimum surface the question for the fair-lending committee even where the firm has not yet designed a sizing-review framework.
- Defaulting to BISG without acknowledging that proxy accuracy may degrade in wealth-customer surname distributions.

## insurance

### Insurance sector overlay for fair-lending-test-plan

When the scope record names sector `insurance`, this overlay sets the scope boundary first. Insurance underwriting and pricing discrimination is regulated under state-DOI unfair-discrimination statutes, not under ECOA or the FHA. The fair-lending test-plan skill is the wrong tool for most insurance review work.

Loaded by: `fair-lending-test-plan/SKILL.md` when `scope.sector_overlay_set` includes `insurance`, or when the institution type implicates a life, health, or property-and-casualty insurer.

Cited and section-referenced anchors live in `references/source-anchors.md`.

#### Scope boundary

The vocabulary differs. Insurance regulators talk about "unfair discrimination" under the NAIC Unfair Trade Practices Act (Model #880) and state-DOI statutes implementing the model. The substantive tests differ from ECOA: the actuarial-justification framing centers on whether the rate or underwriting outcome reflects a sound actuarial basis and is not unfairly discriminatory between similarly-situated risks; the ECOA effects-test framing centers on disparate impact relative to legitimate business necessity with an LDA search.

For most insurance fair-treatment review work, route to:

- The firm's own insurance-conduct or market-conduct review program.
- The NAIC AI Model Bulletin (December 2023) where the institution uses AI/ML in underwriting, pricing, marketing, claims, or fraud detection.
- The NYDFS Insurance Circular Letter on AI and ECDIS in life-insurance underwriting (January 2024) for NY-licensed life insurers.
- The Colorado Division of Insurance regulation implementing SB 21-169 for CO life-insurance underwriting using ECDIS or predictive models.

Those are the operative regimes. The fair-lending test plan is built around ECOA and FHA and does not naturally extend into them.

#### Where the fair-lending test plan does apply on the insurance side

Two narrow cases:

##### 1. Credit-protection insurance bundled with a credit product

Where the institution sells credit-protection insurance (e.g., credit life, debt-cancellation product) bundled with an underlying credit product (mortgage, card, personal loan), the credit-side decision is in ECOA scope and the fair-lending test plan covers it normally. The insurance-side decision (eligibility, pricing) is out of fair-lending scope and routes to the insurance-conduct framework.

The bundled-product seam is a recurring complaint-theme source; coordinate with complaint-theme-analysis where complaint signals indicate cross-product issues.

##### 2. Insurance products marketed alongside credit

Where the institution operates a marketing surface that distributes both credit and insurance products to overlapping customer audiences, the marketing-distribution test on the credit side is in fair-lending scope. The insurance-distribution side routes separately to the insurance-conduct framework. The plan flags the boundary so reviewers do not over-extend ECOA into insurance-marketing review.

#### What does not extend into the fair-lending test plan

- Life-insurance underwriting and pricing — out of fair-lending scope. Apply the NAIC AI Model Bulletin, the NYDFS Insurance Circular Letter, the CO regulation per state footprint.
- Health-insurance underwriting and pricing — out of fair-lending scope. ACA non-discrimination provisions and HHS / state-DOI regimes apply.
- P&C insurance underwriting and pricing — out of fair-lending scope. State-DOI unfair-discrimination statutes apply; the NAIC AI Model Bulletin reaches insurer use of AI systems.
- Insurance claims handling — out of fair-lending scope. Bad-faith claims-handling and unfair-claims-settlement-practice statutes apply.

The fair-lending test plan does not resize itself into an insurance unfair-discrimination plan. Reviewers asked to do insurance unfair-discrimination work should route to the insurance-side skill set.

#### Common pitfalls when insurance is flagged

- Building an ECOA test plan for an insurance underwriting model; the regime is wrong. Route to the insurance unfair-discrimination framework.
- Treating the NAIC AI Model Bulletin as an ECOA-equivalent obligation; the bulletin sets governance and AIS-program expectations, not ECOA-style effects-test expectations.
- Extending BISG-based regression methodology into insurance pricing without acknowledging that the test framing differs (actuarial-justification vs. business-necessity); the methodology is portable but the legal frame is not.
- Reading the bundled-credit-protection seam without separating the credit-side decision (in scope) from the insurance-side decision (out of scope).

## payments-fintech

### Payments and fintech sector overlay for fair-lending-test-plan

When the scope record names sector `payments-fintech`, this overlay adds payments- and fintech-specific scope, methodology, and review-gate detail to the fair-lending test plan. Where there is conflict between the capability defaults and this overlay, the overlay governs the sector elements.

Loaded by: `fair-lending-test-plan/SKILL.md` when `scope.sector_overlay_set` includes `payments-fintech`, or when the institution type implicates a fintech consumer-credit platform, sponsor-bank-program operator, BNPL provider, merchant cash advance provider, prepaid issuer, or non-bank consumer-finance entity.

Cited and section-referenced anchors live in `references/source-anchors.md`.

#### What changes for payments and fintech fair-lending test plans

Fintech consumer credit sits inside ECOA and Regulation B because ECOA reaches every creditor. The fair-lending fabric travels with the credit decision regardless of the entity making it. The overlay carries the structural details that change when the originator is not a depository.

##### 1. Sponsor-bank fair-lending duty allocation

Most fintech consumer-credit platforms operate through a sponsor-bank arrangement. The fair-lending duty allocates per the program agreement and per the sponsor bank's fair-lending program. The plan carries:

- A statement of which legal entity is the creditor of record (typically the sponsor bank).
- A statement of which entity owns the underwriting model and the marketing surface (the program operator, in most arrangements).
- A statement of which second-line function reviews the test plan and the test results (typically a sponsor-bank fair-lending officer; sometimes joint with the fintech's compliance team).
- A statement of which committee approves the plan (the sponsor-bank fair-lending committee; sometimes joint with the fintech AI risk committee where AI/ML models drive decisions).

The interagency third-party guidance (June 2023) anchors the bank-side accountability; the program operator is not the sole accountable party even where the operator built and validated the model.

##### 2. Alternative-data and ML underwriting

Fintech consumer credit underwriting frequently uses alternative-data inputs (cash-flow signals, bank-data permissions, employment-tenure inferred from payroll integration, device and behavioral signals) layered with ML scoring. The plan must include:

- Per-feature review of alternative-data buckets against protected-class proxies (effects-test screen under Reg B §1002.6).
- LDA search per CFPB Circulars 2022-03 and 2023-03 and the April 2023 Joint Statement: feature-removal sweep on the alternative-data buckets, threshold-adjustment search, alternative-model-class trial. Document rejected alternatives.
- Adverse-action notice review per CFPB Circulars 2022-03 and 2023-03 — the bureau's posture is that complex-model output does not exempt the creditor from the specificity requirement; sample of declined applications, pull model-score and feature-contribution explanation, compare to issued notice.

The model card and the fair-lending test plan are mutually-referencing artifacts; the plan stresses the card's stated intended use, fairness method, and limitations.

##### 3. Marketing-funnel skew and digital-channel acquisition

Fintech consumer credit acquisition typically runs through digital channels (search, social, lookalike audiences, partner marketplaces). The plan must include marketing-distribution testing on the acquisition funnel: audience-skew test against an addressable-population baseline, served-impression skew check, and where lookalike models or audience-targeting models are used, an LDA search on those models. The protected-class targeting risk lives upstream of the underwriting decision; redlining-equivalent harm in fintech often occurs at the marketing layer.

Cross-reference marketing-claim-review where the test plan surfaces marketing-content issues alongside distribution issues.

##### 4. BNPL and short-term consumer credit

Buy Now Pay Later providers sit at a contested fair-lending boundary. The CFPB Interpretive Rule on BNPL (May 2024) was **nullified by Pub. L. 119-11 (May 9, 2025); historical only.** ECOA / Reg B continue to apply on their own terms where the BNPL product extends credit; the fair-lending fabric travels with the underlying credit-decisioning structure rather than through the nullified interpretive rule. The plan covers BNPL where the entity's product is in-scope; treat as a consumer-credit decision under ECOA and apply the regular machinery. State-money-transmission and merchant-acquirer compliance are separately scoped.

##### 5. Merchant cash advance scope

Merchant cash advance products are commercial credit, not consumer credit; ECOA reaches credit applications generally but the §1002.13 monitoring infrastructure and the CFPB consumer-finance focus do not apply. Where the test plan covers MCA, treat as commercial-credit fair-lending review under ECOA without the consumer overlay; coordinate with the section1071-readiness skill where MCA is in §1071 scope.

##### 6. Data-only-decisioning models

Some fintech models decide solely on alternative-data signals with no traditional credit-bureau input. The plan must explicitly review:

- Whether the model has any access to protected-class indicators directly (it should not).
- Whether any feature in the alternative-data set acts as a strong protected-class proxy under the effects-test screen.
- The adverse-action notice generation method given that the model has no traditional credit-reason vocabulary; reasons must still be the actual principal reasons under §1002.9 and the CFPB circulars.

##### 7. State licensure and CFPB authority

CFPB consumer-protection authority reaches non-bank consumer-credit providers under Dodd-Frank Title X for ECOA, UDAAP, and the consumer-protection rules. State licensure (consumer lender licences, money-transmission licences) brings state examiners; multi-state CSBS-coordinated exams may apply. The plan flags state-licensure footprint and the strictest-applicable-state posture for any state with prescribed fair-lending content beyond the federal baseline.

#### Payments and fintech-specific test-plan template additions

- `scope.legal_entity_type` — fintech-program-operator / sponsor-bank-program / non-bank-consumer-finance / BNPL / merchant-cash-advance / payments-processor.
- `scope.sponsor_bank_arrangement` — boolean; if true, sponsor-bank validator and federal banking regulator named.
- `scope.state_licensure_footprint` — list of states with consumer-lender or money-transmission licences.
- `model_inventory_in_scope[].alternative_data_uses` — list of alternative-data buckets in the model.
- `tests[].marketing_funnel_lda_required` — boolean; if true, LDA search on lookalike or audience-targeting models is required.
- `tests[].adverse_action_review_method` — recording how the AAN reasons are mapped from model-score and feature contributions.
- `committee_approval_gate.joint_with_program_operator` — boolean; if true, fintech AI risk committee or compliance committee joins the sponsor-bank fair-lending committee.

#### Common pitfalls in payments and fintech fair-lending test plans

- Assuming the fintech is the sole accountable party when the sponsor bank inherits creditor-of-record duty; bank examiners catch this in third-party reviews.
- Defaulting to BISG without addressing BISG accuracy in the program footprint; program footprints heavy in particular states or surname-distribution patterns may need sensitivity analysis.
- Skipping marketing-funnel testing because the fintech is digital-only; protected-class-targeting risk lives at the marketing layer in digital-only channels.
- Treating the alternative-data buckets as out of scope because they are not traditional credit features; the effects-test screen reaches all features, not only credit-bureau features.
- Treating BNPL as out of fair-lending scope on the assumption that BNPL is not credit; the underlying ECOA framework reaches BNPL where the product meets the credit definition. (The May 2024 CFPB BNPL Interpretive Rule was **nullified by Pub. L. 119-11 (May 9, 2025); historical only** — anchor the analysis to the regulatory text and product structure.)
- Treating MCA as in fair-lending scope under the consumer overlay; MCA is commercial credit and the consumer-finance machinery does not all apply.
- Adverse-action notices generated by template from a complex-model output, with no sampling for accuracy; Reg B §1002.9 and Comment 9(b)(2)-3 of the Official Staff Commentary are explicit on principal-reasons specificity. (CFPB Circulars 2022-03 / 2023-03 are **withdrawn May 12, 2025; historical only.**)
