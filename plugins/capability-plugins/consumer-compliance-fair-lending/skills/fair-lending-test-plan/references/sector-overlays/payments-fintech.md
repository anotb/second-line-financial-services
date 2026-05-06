# Payments and fintech sector overlay for fair-lending-test-plan

When the engagement-scope record names sector `payments-fintech`, this overlay adds payments- and fintech-specific scope, methodology, and review-gate detail to the fair-lending test plan. Where there is conflict between the capability defaults and this overlay, the overlay governs the sector elements.

Loaded by: `fair-lending-test-plan/SKILL.md` when `engagement_scope.sector_overlay_set` includes `payments-fintech`, or when the institution type implicates a fintech consumer-credit platform, sponsor-bank-program operator, BNPL provider, merchant cash advance provider, prepaid issuer, or non-bank consumer-finance entity.

Cited and section-referenced anchors live in `references/source-anchors.md`.

## What changes for payments and fintech fair-lending test plans

Fintech consumer credit sits inside ECOA and Regulation B because ECOA reaches every creditor. The fair-lending fabric travels with the credit decision regardless of the entity making it. The overlay carries the structural details that change when the originator is not a depository.

### 1. Sponsor-bank fair-lending duty allocation

Most fintech consumer-credit platforms operate through a sponsor-bank arrangement. The fair-lending duty allocates per the program agreement and per the sponsor bank's fair-lending program. The plan carries:

- A statement of which legal entity is the creditor of record (typically the sponsor bank).
- A statement of which entity owns the underwriting model and the marketing surface (the program operator, in most arrangements).
- A statement of which second-line function reviews the test plan and the test results (typically a sponsor-bank fair-lending officer; sometimes joint with the fintech's compliance team).
- A statement of which committee approves the plan (the sponsor-bank fair-lending committee; sometimes joint with the fintech AI risk committee where AI/ML models drive decisions).

The interagency third-party guidance (June 2023) anchors the bank-side accountability; the program operator is not the sole accountable party even where the operator built and validated the model.

### 2. Alternative-data and ML underwriting

Fintech consumer credit underwriting frequently uses alternative-data inputs (cash-flow signals, bank-data permissions, employment-tenure inferred from payroll integration, device and behavioral signals) layered with ML scoring. The plan must include:

- Per-feature review of alternative-data buckets against protected-class proxies (effects-test screen under Reg B §1002.6).
- LDA search per CFPB Circulars 2022-03 and 2023-03 and the April 2023 Joint Statement: feature-removal sweep on the alternative-data buckets, threshold-adjustment search, alternative-model-class trial. Document rejected alternatives.
- Adverse-action notice review per CFPB Circulars 2022-03 and 2023-03 — the bureau's posture is that complex-model output does not exempt the creditor from the specificity requirement; sample of declined applications, pull model-score and feature-contribution explanation, compare to issued notice.

The model card and the fair-lending test plan are mutually-referencing artifacts; the plan stresses the card's stated intended use, fairness method, and limitations.

### 3. Marketing-funnel skew and digital-channel acquisition

Fintech consumer credit acquisition typically runs through digital channels (search, social, lookalike audiences, partner marketplaces). The plan must include marketing-distribution testing on the acquisition funnel: audience-skew test against an addressable-population baseline, served-impression skew check, and where lookalike models or audience-targeting models are used, an LDA search on those models. The protected-class targeting risk lives upstream of the underwriting decision; redlining-equivalent harm in fintech often occurs at the marketing layer.

Cross-reference marketing-claim-review where the test plan surfaces marketing-content issues alongside distribution issues.

### 4. BNPL and short-term consumer credit

Buy Now Pay Later providers sit at a contested fair-lending boundary. The bureau has signaled treatment of BNPL as credit under TILA / Reg Z (CFPB interpretive rule on BNPL, May 2024 [verify exact title and date]) and the fair-lending fabric travels with that treatment. The plan covers BNPL where the entity's product is in-scope; treat as a consumer-credit decision under ECOA and apply the regular machinery. State-money-transmission and merchant-acquirer compliance are separately scoped.

### 5. Merchant cash advance scope

Merchant cash advance products are commercial credit, not consumer credit; ECOA reaches credit applications generally but the §1002.13 monitoring infrastructure and the CFPB consumer-finance focus do not apply. Where the test plan covers MCA, treat as commercial-credit fair-lending review under ECOA without the consumer overlay; coordinate with the section1071-readiness skill where MCA is in §1071 scope.

### 6. Data-only-decisioning models

Some fintech models decide solely on alternative-data signals with no traditional credit-bureau input. The plan must explicitly review:

- Whether the model has any access to protected-class indicators directly (it should not).
- Whether any feature in the alternative-data set acts as a strong protected-class proxy under the effects-test screen.
- The adverse-action notice generation method given that the model has no traditional credit-reason vocabulary; reasons must still be the actual principal reasons under §1002.9 and the CFPB circulars.

### 7. State licensure and CFPB authority

CFPB consumer-protection authority reaches non-bank consumer-credit providers under Dodd-Frank Title X for ECOA, UDAAP, and the consumer-protection rules. State licensure (consumer lender licences, money-transmission licences) brings state examiners; multi-state CSBS-coordinated exams may apply. The plan flags state-licensure footprint and the strictest-applicable-state posture for any state with prescribed fair-lending content beyond the federal baseline.

## Payments and fintech-specific test-plan template additions

- `scope.legal_entity_type` — fintech-program-operator / sponsor-bank-program / non-bank-consumer-finance / BNPL / merchant-cash-advance / payments-processor.
- `scope.sponsor_bank_arrangement` — boolean; if true, sponsor-bank validator and federal banking regulator named.
- `scope.state_licensure_footprint` — list of states with consumer-lender or money-transmission licences.
- `model_inventory_in_scope[].alternative_data_uses` — list of alternative-data buckets in the model.
- `tests[].marketing_funnel_lda_required` — boolean; if true, LDA search on lookalike or audience-targeting models is required.
- `tests[].adverse_action_review_method` — recording how the AAN reasons are mapped from model-score and feature contributions.
- `committee_approval_gate.joint_with_program_operator` — boolean; if true, fintech AI risk committee or compliance committee joins the sponsor-bank fair-lending committee.

## Common pitfalls in payments and fintech fair-lending test plans

- Assuming the fintech is the sole accountable party when the sponsor bank inherits creditor-of-record duty; bank examiners catch this in third-party reviews.
- Defaulting to BISG without addressing BISG accuracy in the program footprint; program footprints heavy in particular states or surname-distribution patterns may need sensitivity analysis.
- Skipping marketing-funnel testing because the fintech is digital-only; protected-class-targeting risk lives at the marketing layer in digital-only channels.
- Treating the alternative-data buckets as out of scope because they are not traditional credit features; the effects-test screen reaches all features, not only credit-bureau features.
- Treating BNPL as out of fair-lending scope on the assumption that BNPL is not credit; the bureau's interpretive posture and the underlying ECOA framework reach BNPL where the product meets the credit definition.
- Treating MCA as in fair-lending scope under the consumer overlay; MCA is commercial credit and the consumer-finance machinery does not all apply.
- Adverse-action notices generated by template from a complex-model output, with no sampling for accuracy; the bureau's circulars are explicit.
