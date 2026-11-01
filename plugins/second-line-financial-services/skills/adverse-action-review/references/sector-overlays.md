# sector-overlays

One section per sector. Read only the sections the scope calls for.

## banking

### Banking sector overlay for adverse-action-review

When the scope record names sector `banking`, this overlay adds banking-specific scope, methodology, and review-gate detail to the adverse-action notice review. Where there is conflict between the capability defaults and this overlay, the overlay governs the banking-sector elements.

Loaded by: `adverse-action-review/SKILL.md` when `scope.sector_overlay_set` includes `banking`, or when the institution type implicates a federal banking regulator (national bank, state member bank, savings association, bank holding company, foreign banking organization with US operations).

Cited and section-referenced anchors live in `references/source-anchors.md`.

#### What changes for banking adverse-action review

Banking is the heaviest overlay on this skill. The §1002.9 machinery, the FCRA risk-score disclosure overlay, and the model-risk fabric were all built for depositories; the adverse-action review inherits that machinery directly.

##### 1. Notice population scope

A banking adverse-action review typically covers a wider product set than the fintech overlay. Routine review scope includes:

- HMDA-reportable mortgage (first-lien purchase, first-lien refi, junior-lien refi, home-improvement, HELOC) — declines, withdrawals coded as denials, counteroffers not accepted.
- Indirect auto declines (where the bank is the originator-of-record on third-party-dealer-arranged loans), with attention to the dealer-markup and minimum-rate-floor mechanics that have driven prior bureau focus.
- Credit card declines, line-decrease actions on existing accounts, and account closures coded as adverse action under §1002.2(c).
- Unsecured personal loan declines and overdraft-line-of-credit declines.
- Small-business credit declines on the §1071 perimeter where the bank is in-scope under the operative tier phase-in; the small-business adverse-action review consumes §1071 demographic data once the rule is operative for the bank's tier.

The review records the §1002.2(c) action category per decision (`denial`, `counteroffer_not_accepted`, `terms_less_favorable`, `incomplete_application`, `existing_account_action`); a review covering only outright denials misses populations that are also adverse action.

##### 2. FCRA / Regulation V overlay is routine

Most banking adverse-action decisions involve a consumer report and / or a credit score. The per-decision `fcra_overlay_applied` flag is true for the bulk of the population; the notice must include the FCRA disclosure content (consumer reporting agency name, address, and telephone; statement that the agency did not make and cannot explain the decision; right to a free copy and to dispute) under 15 U.S.C. §1681m, and where a credit score was used, the score, range, and key factors under §1022.74. The combined Reg B / Reg V notice is the operational artifact in most banking templates; the review tests both regimes per notice.

##### 3. Model-supported reasons review and SR 11-7 fabric

Where the underwriting decision uses an internal scorecard or AI / ML model, the adverse-action review consumes model documentation produced under the bank's MRM program. The cross-references are:

- Model card (intended use, feature list, monitoring KRIs) from the MRM model-risk inventory.
- Validation-plan output (performance, stability, fairness method, limitations).
- Per-decision feature contribution evidence (SHAP, LIME, leave-one-out, monotonic constraint trace, or the bank's named explainability method).

The review tests that the notice's cited reasons are the principal feature contributions, not a closest-sample-form proxy. The CFPB Circulars 2022-03 and 2023-03 are the operative anchors; the bank's MRM machinery is the evidence pipe.

##### 4. Comparative file review interaction

Banking adverse-action review interacts with comparative file review (covered in `fair-lending-test-plan`). The overlap is the matched-pair on similarly-situated approved applicants: the adverse-action sample frames the test population, and the matched-pair review surfaces disparate-treatment evidence the notice review alone cannot. The review records `cross_reference: fair-lending-test-plan` in the assumptions block where comparative file review is in flight or planned.

##### 5. CRA assessment-area overlap on redlining red flags

Where the disparate-impact red-flag panel surfaces an MSA-level decline-rate disparity, the bank's CRA assessment area is a load-bearing context. A redlining red flag inside the CRA assessment area routes to the CRA officer alongside the fair-lending committee; outside the assessment area, the routing is fair-lending only. The review records the CRA assessment-area overlap per flagged geography.

##### 6. Sponsor-bank arrangements

Where the bank operates a sponsor-bank arrangement (deposit, card, lending program for a fintech partner), adverse-action notice and decision-model accountability allocates per the program agreement and the bank's own fair-lending program. The interagency third-party guidance (June 2023) anchors the bank-side accountability; the bank's compliance second-line typically reviews the program-operator's adverse-action notices and decision evidence and signs off jointly with the program-operator's compliance team. See `payments-fintech.md` for the program-operator-side detail.

##### 7. CFPB authority over banks

CFPB consumer-protection authority reaches large banks (over $10 billion in assets) for ECOA, RESPA, EFTA, TILA, and UDAAP purposes. Smaller banks fall under the prudential regulator for these areas, but CFPB enforcement reach is not eliminated. Reviews for large banks consume the CFPB Fair Lending Report's most recent supervisory-priority signals; reviews for smaller banks consume the prudential regulator's exam manual sections.

#### Banking-specific review additions

The following additions sharpen the artifact's named sections:

- `population.product_set[]` enumerates the banking product perimeter explicitly (mortgage / HELOC / indirect-auto / card / unsecured / overdraft-line / small-business).
- `decisions[].cra_assessment_area_overlap` boolean per dwelling-secured decision.
- `decisions[].sponsor_bank_arrangement` boolean where applicable.
- `model_reason_generation_review.mrm_model_id` references the bank's MRM inventory ID.
- `recommended_actions[].cra_officer_coordination` boolean where a redlining red flag is inside the CRA assessment area.

#### Common pitfalls in banking adverse-action review

- Reviewing only outright denials and missing the counteroffer-not-accepted and terms-less-favorable populations that are also adverse action under §1002.2(c).
- Treating the combined Reg B / Reg V notice as a single compliance test; the two regimes carry separate content requirements and the review tests each.
- Treating model-supported reasons as out of scope on the basis that the model is an internal scorecard rather than AI / ML; the principal-reasons specificity standard applies to all credit-scoring systems under the Staff Commentary, with the AI-specific framing layered on top by the CFPB Circulars.
- Routing a redlining red flag inside the CRA assessment area only to fair lending; the CRA officer's exam-cycle preparation work overlaps and the routing is joint.
- Treating sponsor-bank-program adverse action as the program-operator's compliance issue; the bank retains accountability under the third-party guidance and the program agreement.
- Defaulting BISG everywhere on the disparate-impact panel; HMDA self-reported demographics are stronger evidence for dwelling-secured products and should be used directly.
- Producing a finding of disparate impact on a BISG-flagged red flag; BISG is a probabilistic proxy, the red flag is a signal, and the finding follows formal fair-lending testing (route to `fair-lending-test-plan`).

## capital-markets

### Capital markets sector overlay for adverse-action-review

When the scope record names sector `capital-markets`, this overlay adds capital-markets-specific scope to the adverse-action notice review. The overlay is narrow because most capital-markets credit extension is institutional and outside ECOA scope.

Loaded by: `adverse-action-review/SKILL.md` when `scope.sector_overlay_set` includes `capital-markets`, or when the institution type is a broker-dealer, prime broker, or wealth-management entity extending credit to retail customers.

Cited and section-referenced anchors live in `references/source-anchors.md`.

#### What changes for capital-markets adverse-action review

The skill's core machinery is built for consumer credit. The capital-markets overlay flags the narrow population that comes inside ECOA / Reg B scope and the wider population that does not.

##### 1. ECOA scope boundary

ECOA and Reg B apply to credit primarily for personal, family, or household purposes; commercial and institutional credit extension by a broker-dealer falls outside that scope. The adverse-action review applies where the institution extends credit to retail customers for consumer purposes. The bulk of broker-dealer margin lending is to retail customers buying or carrying securities, which is consumer-purpose only when the securities are being held as a personal investment in the retail customer's individual capacity; institutional and commercial accounts are out of scope.

The review records the population's consumer-vs-institutional split at the population level and excludes institutional decisions from the §1002.9 perimeter explicitly.

##### 2. Securities-based lending and margin calls

Securities-based lending (SBL) extends non-purpose credit to retail customers collateralized by their securities portfolio; margin loans extend purpose credit for securities purchases. Both can be consumer-purpose where the retail customer is the borrower in an individual capacity.

Adverse action on SBL declines and margin-application declines falls under §1002.9. Margin calls and forced liquidations on existing accounts are a different question: the action is taken under the customer margin agreement and Reg T (12 CFR Part 220), not under ECOA. The §1002.2(c) "existing account adverse change" category does not extend to actions taken under the customer agreement's pre-disclosed margin mechanics. The review records margin-call actions out of §1002.9 scope but inside the firm's customer-disclosure and conduct review.

##### 3. Wealth-channel credit boundary

Where a broker-dealer affiliate of a bank holding company offers wealth-channel credit (lombard loans, securities-backed lines of credit, jumbo mortgage referrals to the bank affiliate), the credit decision and the §1002.9 obligation sit with the lender of record. Wealth-channel referrals to the bank affiliate are reviewed under the banking overlay; loans extended by the broker-dealer affiliate directly are reviewed here.

##### 4. Disparate-impact panel applies narrowly

The disparate-impact red-flag panel runs on the consumer-purpose population only. Wealth-channel populations are typically small, demographically clustered, and statistically thin; the BISG signal is often unreliable on this scale. The review may produce qualitative red flags but should not produce statistical disparity findings on small wealth populations; flag and route to `fair-lending-test-plan` for any quantitative work.

#### Capital-markets-specific review additions

- `population.consumer_purpose_subset` boolean per decision; ECOA scope applies only to the subset.
- `population.margin_call_subset` excluded from §1002.9 timing-compliance and content-compliance fields; reviewed instead under conduct and customer-disclosure framing.
- `decisions[].sbl_or_margin` enum (`sbl`, `margin`, `wealth_loan`, `n_a`).

#### Common pitfalls in capital-markets adverse-action review

- Pulling the full margin-decision population into ECOA scope; institutional accounts and commercial-purpose extensions are out of scope.
- Treating margin calls and forced liquidations as adverse action under §1002.9; these are taken under the customer agreement, not under Reg B.
- Running disparate-impact statistics on a small wealth-channel population; the BISG signal on small clustered populations is unreliable, and the artifact should flag the limitation rather than produce a finding.
- Reviewing wealth-channel referral declines without identifying whether the broker-dealer or the bank affiliate was the creditor of record; the §1002.9 obligation follows the lender of record.

## insurance

### Insurance sector overlay for adverse-action-review

When the scope record names sector `insurance`, this overlay flags the scope boundary. Insurance underwriting and pricing is regulated under state-DOI unfair-discrimination statutes, not under ECOA / Regulation B; the adverse-action review does not extend to insurance underwriting decisions.

Loaded by: `adverse-action-review/SKILL.md` when `scope.sector_overlay_set` includes `insurance`. The default behavior on this trigger is to confirm scope with the engagement lead before proceeding.

Cited and section-referenced anchors live in `references/source-anchors.md`.

#### What this overlay does

Stops scope creep. The skill is built for ECOA-covered credit decisions; insurance underwriting is a different legal regime, a different vocabulary ("unfair discrimination" rather than "adverse action"), a different test framing (actuarial-justification rather than ECOA effects-test), and a different supervisor (state DOI, NAIC model laws).

##### 1. Out of scope: insurance underwriting and pricing decisions

Life, health, annuity, P&C, and title insurance underwriting decisions are out of scope for this skill. The applicable regime is the state-DOI unfair-discrimination statute, with NAIC Model #880 (Unfair Trade Practices Act) as the model law and individual state implementations carrying the operational detail. Adverse decisions on insurance applications follow state-specific notice and reason-disclosure requirements, not §1002.9.

Where the engagement lead has called this skill on an insurance-underwriting question, route to a state-DOI / NAIC-aware compliance review and note the scope boundary in the artifact.

##### 2. In scope: bank-affiliated credit-protection insurance bundled with credit

Where a credit-protection insurance product (credit life, credit disability, debt-cancellation product, debt-suspension product) is bundled with a credit decision and the credit decision itself is in ECOA scope, the credit-side decision is in scope. The insurance-side underwriting is out of scope; the skill reviews the credit decision and flags the bundled-insurance pattern for separate review.

The bundled-insurance pattern carries UDAAP exposure under the unfairness and abusiveness prongs (the bureau has historically focused on credit-insurance and debt-cancellation products as conduct-risk surfaces); cross-reference `udaap-risk-review` from the consumer-compliance-fair-lending plugin where the bundled product is in scope.

##### 3. In scope: bank-affiliated insurance referrals where credit-style decisioning is used

Some bank-affiliated insurance affiliates use credit-style decisioning (credit-bureau pull, credit-score-driven premium banding, FICO-based underwriting tiers). Where the credit-style decisioning interacts with a credit relationship at the bank affiliate, the credit-side question is in scope; the insurance-side question is out of scope and routes to the state-DOI / NAIC overlay.

#### Insurance-specific review additions

- `population.bundled_insurance_present` boolean; if true, the credit decision is reviewed here and the bundled-insurance product flags for `udaap-risk-review`.
- `recommended_actions[].naic_routing_required` boolean where an insurance-underwriting question has been incorrectly routed to this skill.

#### Common pitfalls

- Treating an insurance-underwriting decline as an "adverse action" under §1002.9; it is not. The notice obligation is set by the state-DOI unfair-discrimination statute and the state-specific notice rules.
- Reviewing a bundled credit-protection insurance product under ECOA effects-test framing; the framing applies to the credit decision, not to the insurance underwriting.
- Running BISG-driven disparate-impact panels on insurance populations using the ECOA / Reg B template; the legal regime is different and the actuarial-justification framework changes the test design. Route to the state-DOI / NAIC overlay.

## payments-fintech

### Payments / fintech sector overlay for adverse-action-review

When the scope record names sector `payments-fintech`, this overlay adds payments / fintech-specific scope, methodology, and review-gate detail to the adverse-action notice review.

Loaded by: `adverse-action-review/SKILL.md` when `scope.sector_overlay_set` includes `payments-fintech`, or when the institution type is a non-bank lender, BNPL provider, marketplace lender, or fintech operating under a sponsor-bank arrangement.

Cited and section-referenced anchors live in `references/source-anchors.md`.

#### What changes for payments / fintech adverse-action review

The payments / fintech overlay turns on three structural questions: who is the creditor of record, where the model and notice template live, and whether the program-operator or the sponsor bank carries the §1002.9 obligation.

##### 1. Sponsor-bank vs. fintech-of-record allocation

In a typical sponsor-bank lending program, the bank is the creditor of record and the fintech operates the marketing, application, and decisioning workflow as a service provider under the program agreement. Reg B obligations rest on the creditor; the bank is the §1002.9 obligor. The interagency third-party guidance (June 2023) anchors the bank-side accountability, and the program agreement allocates operational duties.

Where the fintech is the lender of record (true-lender direct lending, state-licensed lender programs), the fintech carries the §1002.9 obligation directly. The review records the creditor-of-record per program at the population level, not per decision.

Joint review is the operational norm: the bank's compliance second-line and the fintech's compliance team review the notice population jointly, with sign-off allocated per the program agreement. The artifact records both review owners and both committee gates.

##### 2. BNPL adverse-action posture

The CFPB Interpretive Rule on BNPL (May 2024) was **nullified by Pub. L. 119-11 (May 9, 2025); historical only.** The earlier framing treated certain BNPL lenders that issue digital user accounts as card issuers under Regulation Z; that Reg Z reach is no longer in force. Reg B and ECOA continue to apply to BNPL credit decisions on their own terms. Adverse action on a BNPL decline (including soft-decline patterns where the customer is shown only longer-tenor or smaller-amount offers) falls under §1002.9.

The §1002.2(c) action category is load-bearing: a BNPL flow that presents the customer with a smaller amount or longer tenor than requested is a counteroffer; if not accepted, it is adverse action. Many BNPL flows do not surface this as an adverse-action event today; the review tests the flow against the §1002.2(c) categories.

##### 3. Vendor-supplied decisioning model

Where the underwriting decision uses a vendor-supplied model (turn-key fraud-deny, identity-deny, alternative-data score, open-banking cash-flow score), the fintech and the sponsor bank inherit the model-supported-reasons obligation. The vendor may not produce per-decision feature contributions out of the box; the review records the vendor's explainability artifact as evidence and flags where it is absent.

Vendor-of-record reason coding is a recurring defect: vendor returns a numeric score and a small set of reason flags from a fixed dictionary, the fintech's notice template selects the closest sample-form match, and neither the vendor nor the fintech can demonstrate per-decision feature contributions. Reg B §1002.9 and Comment 9(b)(2)-3 of the Official Staff Commentary are the operative anchors (CFPB Circulars 2022-03 / 2023-03 are **withdrawn May 12, 2025; historical only.**); the review records vendor explainability as a named gap when absent.

##### 4. Alternative-data feature posture

Fintech underwriting models often use alternative data (cash-flow patterns, employment-platform attestations, telecom and utility tradelines, device and behavioral signals). The model-supported-reasons review tests that cited reasons reflect the actual feature contributions; "insufficient credit history" cited on a model that did not use traditional credit-bureau data, or "value of collateral" cited on an unsecured product, are recurring impossible-mapping defects.

The fair-lending exposure of alternative-data features (proxy-for-protected-class concerns) is not the adverse-action review's lane; the review flags suspicious features and routes to `fair-lending-test-plan`.

##### 5. Program-agreement and exit-clause interactions

The sponsor-bank program agreement typically grants the bank approval rights over the fintech's notice template, model release, and reason-code dictionary. The review records the version of the notice template in scope and the date of the bank's last approval; out-of-version notices are an immediate finding regardless of substantive compliance. Where the program has an exit clause active or a remediation plan in flight, the review records the program status because notice-fix recommendations may interact with exit timing.

#### Payments / fintech-specific review additions

- `population.creditor_of_record` enum (sponsor-bank, fintech-of-record, joint).
- `population.program_agreement_version` and `population.notice_template_version_approved_date`.
- `decisions[].vendor_decisioning_model_id` and `decisions[].vendor_explainability_artifact_present` boolean.
- `decisions[].alternative_data_feature_present` boolean.
- `model_reason_generation_review.vendor_explainability_method` string (vendor-named method) and `vendor_explainability_artifact_evidence_path`.
- `recommended_actions[].joint_committee_routing` boolean (bank fair-lending committee plus fintech compliance committee).

#### Common pitfalls in payments / fintech adverse-action review

- Treating Reg B as the bank's problem when the fintech operates the workflow; the bank is the §1002.9 obligor in a sponsor-bank arrangement and the fintech is the operational owner. Both audiences read the artifact.
- Treating BNPL adverse action as a Reg Z question (the May 2024 Interpretive Rule was about Reg Z and is **nullified by Pub. L. 119-11 (May 9, 2025); historical only.**); ECOA and Reg B apply on their own terms.
- Missing the soft-decline counteroffer pattern on BNPL, where the customer is shown a smaller amount or longer tenor. Counteroffers not accepted are adverse action.
- Accepting a vendor's fixed reason-code dictionary as the creditor's compliance evidence; the creditor must demonstrate the cited reasons reflect the actual principal feature contributions per Reg B §1002.9 and Comment 9(b)(2)-3 of the Official Staff Commentary.
- Reviewing notices against the current template version when the population was decided under an earlier version; the population review tests the template version that was in force at decision time.
- Routing a finding only to the fintech compliance team where the sponsor-bank program agreement requires joint sign-off; both routes are needed and the artifact names both.
