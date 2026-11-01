# sector-overlays

One section per sector. Read only the sections the scope calls for.

## banking

### Banking sector overlay for validation-plan

When the scope record names sector `banking`, this overlay adds banking-specific scope items to the validation plan. Where there is conflict between the capability defaults and this overlay, the overlay governs the banking-sector elements.

Loaded by: `validation-plan/SKILL.md` when `scope.sector_overlay_set` includes `banking`, or when the institution type implicates a federal banking regulator (national bank, state member bank, savings association, bank holding company, foreign banking organization with US operations).

Cited and section-referenced anchors live in `references/source-anchors.md`.

#### What changes for banking validation plans

##### 1. The joint interagency revised guidance is the current binding frame

For federally regulated banks, the binding frame is the joint interagency Revised Guidance on Model Risk Management (OCC 2026-13 / FRB SR 26-2 / FDIC FIL-15-2026, April 17 2026; supersedes SR 11-7 and SR 21-8). The three-pillar structure (conceptual soundness, ongoing monitoring, outcomes analysis) carries forward from SR 11-7 §IV; the plan does not invent an alternative. The bulletin expressly excludes generative AI and agentic AI from its scope (footnote 3); for GenAI use cases the plan's GenAI-overlay validation scope anchors to NIST AI 600-1, ISO/IEC 42001, EU AI Act Article 9 and Article 15 where applicable, and the cyber overlay rather than the bulletin.

For non-bank entities under the same parent (e.g., a sister broker-dealer or asset manager subsidiary), the bulletin reaches by extension only when the bank inherits model risk through transactions, services, or balance-sheet exposure. Plan-writer should not over-claim reach to non-bank entities; the substantive validation expectations are similar but the regulator constellation differs.

##### 2. OCC Heightened Standards (12 CFR Part 30 Appendix D) — independence demand on tier-1

For OCC-supervised large banks subject to Heightened Standards, the validator function for tier-1 models in scope of the risk-appetite statement must be independent of model development. Plan metadata names the validator function and confirms independence at plan acceptance. The Heightened Standards' independent-risk-management expectation maps directly to SR 11-7 §IV.5 effective challenge.

Plan-side implications:

- Plan metadata flags `heightened_standards_inscope = true` for OCC large banks.
- For tier-1 models, the validator function is named with an explicit independence statement.
- Effective challenge questions for tier-1 models include a question on whether the development assumptions have been re-tested in this cycle (challenge to incumbency).

##### 3. ECOA / Reg B fair-lending integration for credit-decisioning models

Where the model influences a credit decision (origination, pricing, line management, collections triggers, fraud-driven adverse action), the validation plan integrates with the firm's fair-lending test plan. The plan and the fair-lending test plan reference each other but stay distinct artifacts (the validator owns the model-risk lens; the consumer-compliance function owns the fair-lending lens).

Plan-side implications:

- Fairness scope includes ECOA / Reg B disparity testing across protected classes per the firm's fair-lending test plan; the plan cites the fair-lending test plan as a dependency.
- Adverse-action notice generation method (typically SHAP-based or reason-code-mapped) is a controls-section validation item, not a fairness-section item; the validator reviews the method and its sampling QC against Reg B §1002.9 (specific principal reasons) and Comment 9(b)(2)-3 of the Official Staff Commentary (cited reasons must accurately describe factors actually considered or scored). CFPB Circulars 2022-03 / 2023-03 are **withdrawn May 12, 2025; historical only**.
- Effective challenge questions probe the proxy-variable post-deployment process (CFPB and OCC fair-lending exam practice probe this seam).

##### 4. CCAR / DFAST overlap for stress-eligible banks

For banks subject to stress testing (DFAST and Federal Reserve CCAR for the largest BHCs), models used in stress projections, allowance methodology (CECL under ASC 326), and capital planning are in scope of additional validation expectations beyond SR 11-7. The plan:

- Flags `stress_testing_inscope = true` and identifies the relevant submission cycle.
- Includes stress-testing-pedigree review in conceptual soundness scope (was the model developed for, validated for, and currently approved for use in the relevant stress submission).
- Lists the annual stress-testing cycle as a re-validation trigger in monitoring scope.
- Cross-links to the firm's CCAR / DFAST owner and SR 15-18 or successor guidance [verify SR letter].

##### 5. AML, BSA, and fraud-model framing

For models supporting BSA/AML transaction monitoring, sanctions screening, customer risk rating, and fraud detection, the FFIEC BSA/AML Examination Manual sets the supervisory frame. The plan:

- Names the BSA officer or designee as a sign-off reviewer when the model touches AML use cases.
- Includes above-the-line / below-the-line testing in outcomes-analysis scope (productivity testing for transaction monitoring).
- Treats threshold tuning as a controls-section validation item; threshold changes that materially shift alert volumes are change-management triggers and re-validation triggers.
- Avoids representing fraud-model performance metrics as AML-effectiveness evidence; the two are doctrinally distinct.

##### 6. CRA-relevant models

For models that influence community-development assessment, low-and-moderate-income outreach, or branch-network analytics where they touch CRA performance, the plan adds a CRA-context note. Firm policy may require the head of community reinvestment as a sign-off reviewer.

##### 7. Banking-specific validation tests and monitoring

In addition to the capability defaults, banking validation plans typically include:

- Population stability index (PSI) monitoring on input features in monitoring scope, with breach thresholds set against firm policy and against industry-typical breaches (PSI > 0.25 typically triggers re-fit consideration).
- Score drift monitoring (KS or PSI on score distribution) against a reference distribution.
- Decisioning-rate drift monitoring (approval rate, override rate, decline rate) by segment.
- Where applicable, complaint-rate drift from the CFPB complaint database plus internal complaint feed.

Each banking monitoring entry retains the validator's `revalidation_trigger` flag in addition to operational alerting.

#### Banking-specific output template additions

The following fields are added to the plan (mapped to schema where present):

- `plan_metadata.heightened_standards_inscope` — boolean, true for OCC large banks subject to 12 CFR Part 30 Appendix D.
- `plan_metadata.bank_charter_type` — national bank / state member / state nonmember / savings association / BHC / FBO.
- `plan_metadata.primary_federal_regulator` — OCC / FRB / FDIC / NCUA.
- `plan_metadata.stress_testing_inscope` — boolean, with cross-reference to CCAR or DFAST submission.
- `data_review.scope_items[]` — CRA-relevance flag for CRA-touching data sources.
- `outcomes_analysis[]` — adverse-action-notice generation method validation when the model is credit-decisioning; above-the-line / below-the-line testing for AML transaction monitoring.
- `effective_challenge_questions[]` — banking-specific (adverse-action method, fair-lending integration, CCAR/DFAST pedigree, BSA officer sign-off where AML model).
- `monitoring[]` — PSI, score drift, decisioning-rate drift, complaint-rate drift entries with `revalidation_trigger` flagged.

#### Common pitfalls in banking validation plans

- Treating CFPB authority as out of scope because the entity is OCC- or FRB-supervised; CFPB consumer-protection authority reaches large banks for ECOA, RESPA, EFTA, and UDAAP purposes.
- Reporting model performance only on a development holdout in outcomes analysis; SR 11-7 §IV expects performance under deployment conditions.
- Omitting the proxy-variable post-deployment process; both CFPB and OCC fair-lending exam practice probe this seam.
- Citing "vendor system card" as standalone evidence for a foundation-model dependency; for banks, vendor evidence supplements but does not substitute for the firm's own validation work.
- Omitting the stress-testing-pedigree review when the model is in fact used in stress; auditors and examiners catch this in the cross-walk.
- Setting validation depth as a single label across all three pillars; SR 11-7 §IV expects depth set per pillar, with justification.

## capital-markets

### Capital markets sector overlay for validation-plan

When the scope record names sector `capital-markets`, this overlay adds capital-markets-specific scope items to the validation plan. Where there is conflict between the capability defaults and this overlay, the overlay governs the capital-markets-sector elements.

Source content derives from the capital-markets lead's overlay snippets and is adapted to the validation-plan context. Cited and section-referenced anchors live in `references/source-anchors.md`.

#### What changes for capital-markets validation plans

##### 1. SR 11-7 reach is partial, not blanket

For investment advisers and broker-dealers that are not part of a bank holding company, SR 11-7 is not directly binding. The plan uses NIST AI RMF Measure function and ISO/IEC 42001 §9 as the primary anchor; SR 11-7 is referenced where the parent BHC inherits model risk through a banking subsidiary. Plan-writer should not assert SR 11-7 reach to standalone advisers / BDs.

The substantive validation expectations (three pillars, depth per pillar, effective challenge, source trace) carry forward; the regulator constellation differs.

##### 2. SEC and FINRA expectations come through Rule 206(4)-7, FINRA 3110, Reg BI, and the Marketing Rule

For an investment adviser, the model's role in the compliance program connects through Rule 206(4)-7 (compliance program adoption and annual review). For a broker-dealer, FINRA Rule 3110 (supervisory system) and Reg BI (best interest, care obligation) are the primary frames.

Plan-side implications:

- For an adviser: the CCO is a plan-acceptance audience; the annual Rule 206(4)-7 review is a re-validation cadence trigger in monitoring scope.
- For a BD: supervisory system documentation is a plan-acceptance audience; FINRA WSPs reference the model.
- For both: validation evidence supports the compliance-program review file.

##### 3. SEC predictive-data-analytics rulemaking

The SEC proposed rules on conflicts of interest in the use of predictive data analytics by broker-dealers and investment advisers (proposed July 2023) [verify current state — proposal, withdrawal, or further action]. The plan flags the conflict-of-interest question for any model that interacts with retail-investor decisions. Where the rule is currently in proposal or non-final state, the plan records the firm's monitoring posture rather than asserting compliance with a non-final rule.

##### 4. Marketing Rule and AI-generated client communications

For investment advisers under the IAA, Marketing Rule (Rule 206(4)-1) coverage extends to AI-generated client communications, AI-generated hypothetical performance, and AI-generated testimonials/endorsements. The plan's outcomes-analysis scope for any model that produces client-facing content includes a Marketing-Rule-required-disclosure check; a Marketing Rule effective-challenge question asks how the firm catches AI-generated content that meets the advertisement definition without manual flagging.

##### 5. Best-execution surveillance, execution algos, and trading models

For execution algorithms and trading-related models, additional anchors apply:

- SEC Rule 15c3-5 (Market Access Rule) controls overlap; the plan's controls scope tests financial and regulatory pre-trade controls per Rule 15c3-5. Kill-switch testing is in robustness scope.
- FINRA Rule 5310 best-execution obligations; for models that influence execution-venue choice, the plan scopes best-execution-monitoring methodology.
- For surveillance models (insider trading, market manipulation, spoofing detection, layering), FINRA Rule 3110 supervisory expectations apply; outcomes-analysis scope includes precision/recall on alert quality and time-to-alert tests.

##### 6. Books-and-records reach (Rule 204-2 for advisers; Rule 17a-3/4 for BDs)

For any model that supports an advisory recommendation or a trading decision, books-and-records rules apply to the model output and to the inputs that drove it. The plan:

- Scopes the firm's books-and-records system of record for AI-generated content (frequent gap on GenAI use cases).
- Adds a retention-evidence check to data-review scope (output retention; input and decision retention where the rule reaches the underlying basis).
- Adds an effective-challenge question on books-and-records reach for AI-generated content.

##### 7. Sub-adviser and fund-board awareness

Where the model is operated by a sub-adviser on the registrant's funds, sub-adviser oversight under 38a-1(a)(4) applies. The plan identifies sub-adviser operation, the firm's oversight cadence, and the fund-board reporting posture. For a 1940 Act fund context, the fund's CCO is a plan-acceptance audience.

##### 8. AIFMD / MiFID II for cross-border activity

For US advisers serving EU professional or retail clients, AIFMD / MiFID II overlay can extend; the plan flags EU client exposure and routes to `ai-act-triage` for the EU-applicability scoping.

#### Capital-markets-specific output template additions

- `plan_metadata.legal_entity_type` — investment adviser / broker-dealer / dual registrant / 1940 Act fund / 1933 Act issuer / municipal-securities entity.
- `plan_metadata.primary_regulator_constellation` — SEC / FINRA / state-IA / MSRB / NYSE / CBOE / FOREX / other.
- `plan_metadata.fund_board_reporting_inscope` — boolean; for 1940 Act fund use cases.
- `plan_metadata.sub_adviser_operated` — boolean; if true, sub-adviser oversight cadence is a controls-scope item.
- `plan_metadata.marketing_rule_reach` — boolean; for AI generating client-facing content.
- `plan_metadata.market_access_rule_inscope` — boolean; for execution algo or order-routing models under Rule 15c3-5.
- `data_review.scope_items[]` — books-and-records retention statement aligned to Rule 204-2 or Rule 17a-3/4 as applicable.
- `outcomes_analysis[]` — execution-algo slippage / market-impact tests; surveillance-model precision/recall and time-to-alert tests; Marketing-Rule-required-disclosure check for AI-generated client content.
- `robustness_testing[]` — kill-switch testing for execution algos under Rule 15c3-5; vendor model-version swap drill where applicable.
- `effective_challenge_questions[]` — capital-markets-specific (CCO sign-off, fund-board reporting posture, books-and-records reach, predictive-analytics rulemaking posture, Marketing Rule reach where applicable).

#### Common pitfalls in capital-markets validation plans

- Importing SR 11-7 vocabulary into an adviser/BD plan without confirming SR 11-7 reach; it does not directly apply to non-bank registrants.
- Omitting books-and-records reach for AI-generated client content; Rule 204-2 catches the firm at exam time.
- Treating the SEC predictive-analytics proposal as binding when it is currently in non-final state; or treating it as irrelevant when the firm's risk register already monitors the proposal.
- Missing Marketing Rule reach for AI-generated investment-letter drafts or RFP-response generation.
- Forgetting fund-board reporting posture for sub-adviser-operated AI on the registrant's funds.
- Treating execution-algo Market Access Rule controls as engineering controls rather than validation-scope controls; Rule 15c3-5 controls are governance controls and belong in the plan.
- Treating surveillance-model alert volume as a quality metric without precision/recall and time-to-alert; FINRA 3110 supervisory expectation is for alert quality, not just alert volume.

## insurance

### Insurance sector overlay for validation-plan

When the scope record names sector `insurance`, this overlay adds insurance-specific scope items to the validation plan. Where there is conflict between the capability defaults and this overlay, the overlay governs the insurance-sector elements.

Source content derives from the insurance lead's overlay snippets and is mapped here into the validation-plan context. Cited and section-referenced anchors live in `references/source-anchors.md`.

#### What changes for insurance validation plans

##### 1. NAIC Bulletin on the Use of Artificial Intelligence Systems by Insurers (December 2023) is the spine

The Bulletin sets out an AIS Program (governance, risk management, testing, validation, third-party AI accountability, monitoring, documentation, transparency, fairness). The validation plan operationalises the testing-and-validation elements for an individual AI use case in a carrier setting. The Bulletin is itself a model bulletin; state-by-state adoption is tracked by the NAIC AI Working Group adoption tracker. Plan-writer flag: cite by jurisdiction, do not assert the Bulletin as binding without state adoption confirmation.

The plan carries an AIS Program element-by-element validation-coverage block in conceptual-soundness scope (testing, validation, third-party AI accountability, monitoring, documentation), tying each element to an outcomes-analysis or monitoring entry.

##### 2. State DOI bulletins extend the bar in named jurisdictions

The plan identifies the operating footprint and aligns to the strictest applicable state. Named bulletins to enumerate when in scope:

- Colorado Division of Insurance regulation implementing SB 21-169 — governance and risk management of External Consumer Data and Information Sources (ECDIS) and predictive models in life-insurance underwriting. ECDIS provenance becomes a data-review scope item when CO is in footprint; unfair-discrimination testing is added to fairness scope.
- New York DFS Insurance Circular Letter on AI and ECDIS in life-insurance underwriting (January 2024) — governance, fairness testing, disclosure, and consumer-recourse expectations. NY-footprint plans add disparate-impact-style monitoring on top of the actuarial-justification test.
- California DOI bulletin on AI use in insurance — broader than CO/NY in scope but informs disclosure posture.

##### 3. Fairness vs unfair-discrimination — vocabulary translation

Capability fairness vocabulary (disparate impact, AIR, demographic parity) and insurance unfair-discrimination vocabulary (NAIC Unfair Trade Practices Act Model #880) are not the same legal test. State insurance code permits actuarially justified rating differences that would be challenged under disparate-impact frameworks elsewhere; conversely, some state insurance code prohibitions reach uses of variables (e.g., credit-based insurance scores in some states) that disparate-impact analysis would not flag.

The plan's fairness scope uses both vocabularies when applicable. The success criterion for a rate-filing model includes the actuarial-justification test under state insurance code in addition to (or instead of) generic disparity ratios. An effective challenge question explicitly asks whether the test framing matches the regulator's test framing.

##### 4. ECDIS-driven rating and underwriting

Where the model uses external consumer data and information sources (third-party data beyond traditional underwriting variables), the plan's data-review scope adds:

- ECDIS provenance for each data source: provider, lineage, refresh, consumer-disclosure posture, consumer-recourse channel.
- Per-state ECDIS treatment: CO regulation imposes specific governance and disclosure on ECDIS use in life underwriting; NY DFS Circular Letter has its own disclosure expectations.
- HIPAA touch flag for any health-data ECDIS feed (cross-link to `references/cross-cutting.md#privacy`).

##### 5. Insurance use-case categories

The plan recognises which insurance-AI use case category applies; the outcomes-analysis and robustness scope differ across them:

- Accelerated underwriting (life, health): ECDIS-related tests; CO/NY DFS bulletin alignment; HIPAA-touch privacy overlay.
- Claims AI (FNOL triage, severity prediction, fraud-indicator scoring, claims chatbot): NAIC Model #880 unfair-claims-settlement standards apply regardless of decision technology; state UCSPA timing and notice obligations apply. Validation includes faithfulness, denial-letter quality, supervisor-override path testing.
- Pricing / rating ML factors: state DOI rate filing and prior-approval regimes apply where the model touches filed rates; rate analyst is a plan-acceptance audience.
- Marketing AI (suitability, replacement risk for annuities): NAIC Model #275 [verify model number] for annuity suitability.
- Agent-AI co-pilots: producer-licensing reach; suitability and best-interest standards.
- Back-office AI (call-center summarisation, mailroom OCR): generally lower tier; lighter validation.

##### 6. ORSA materiality

For an enterprise-material AI use case, NAIC ORSA (Model #505) inclusion is required; the plan flags `orsa_inscope = true` and cross-references the firm's ORSA Summary Report. The plan's effective-challenge questions include an ORSA-fit question for tier-1 use cases.

##### 7. HIPAA scope check

Any insurance AI touching PHI (health-claims AI, life-and-health underwriting using prescription-history or medical data) requires a HIPAA Privacy and Security Rule cross-check; HIPAA business-associate-agreement posture is a data-review scope item for any vendor handling PHI. Cross-link to `references/cross-cutting.md#privacy`.

##### 8. Producer licensing on consumer-facing AI

A consumer-facing AI that takes binding-equivalent actions (binding, quoting commitments, surrendering, paying claims) can trigger producer-licensing questions; flag for the licensing function. Plan effective-challenge questions probe the boundary.

##### 9. Vendor-AI accountability

NAIC Bulletin Dec 2023 holds the carrier accountable for vendor and third-party AI used on its policies. The plan's conceptual-soundness scope names the vendor evidence in scope (system card, evaluation report, red-team summary, contract addenda) and the firm-side rationale memo; vendor self-attestations are recorded but do not substitute for firm-side validation.

#### Insurance-specific output template additions

- `plan_metadata.ais_program_coverage` — element-by-element validation-coverage block (testing, validation, third-party AI accountability, monitoring, documentation, transparency, fairness).
- `plan_metadata.state_doi_status` — per-state status (CO, NY, CA at minimum if in operating footprint).
- `plan_metadata.orsa_inscope` — boolean.
- `plan_metadata.hipaa_touch` — boolean; if true, BAA reference required for any PHI-handling vendor in `data_review`.
- `plan_metadata.producer_licensing_posture` — for consumer-facing AI taking binding-equivalent actions.
- `data_review.scope_items[]` — ECDIS provenance for each data source (provider, lineage, refresh, consumer-disclosure posture, consumer-recourse channel).
- `fairness_explainability[].dimension` — unfair-discrimination dimension under state insurance code (#880 vocabulary) in addition to or in place of generic fairness vocabulary.
- `effective_challenge_questions[]` — insurance-specific (AIS Program element coverage, state DOI strictest-applicable, ECDIS posture, ORSA fit, HIPAA touch, producer-licensing, claims-AI Model #880 fair-claims-settlement test framing).

#### Common pitfalls in insurance validation plans

- Carrying generic fairness vocabulary into a rate-filing context; state DOI rate analysts use unfair-discrimination vocabulary and the actuarial-justification test.
- Treating the NAIC Bulletin as US-uniform; adoption is state-by-state and the Bulletin is itself non-binding until state adoption.
- Omitting ECDIS provenance for a life-underwriting model when CO or NY is in operating footprint.
- Missing HIPAA BAA reference for a vendor handling PHI in the data-review scope.
- Treating claims AI as a pure technology question without the Model #880 fair-claims-settlement frame; validation of a claims chatbot includes denial-letter quality and supervisor-override path testing, not just faithfulness.
- Forgetting that the TPA's controls are the carrier's controls under NAIC Insurance Data Security Model Law (#668) §4.F when the model runs at a TPA; the plan scopes the TPA's monitoring as in scope for the carrier's validation.
- Treating the AIS Program elements as a checklist rather than as scope coverage; the plan ties each element to a named outcomes-analysis or monitoring entry.

## payments-fintech

### Payments and fintech sector overlay for validation-plan

When the scope record names sector `payments-fintech`, this overlay adds payments- and fintech-specific scope items to the validation plan. Where there is conflict between the capability defaults and this overlay, the overlay governs the sector elements.

Loaded by: `validation-plan/SKILL.md` when `scope.sector_overlay_set` includes `payments-fintech`, or when the institution type implicates a money transmitter, payments processor, fintech program, sponsor-bank arrangement, prepaid issuer, BIN sponsor, or non-bank consumer-finance entity.

Cited and section-referenced anchors live in `references/source-anchors.md`.

#### What changes for payments and fintech validation plans

##### 1. Sponsor-bank model risk responsibility allocation

For sponsor-bank programs (a fintech offering deposit, lending, or card products through a sponsor-bank balance sheet), model risk responsibility is allocated by the bank-fintech contract and by the bank's own model risk policy. The plan carries:

- A statement of which legal entity owns the model (sponsor bank / fintech / shared) in plan metadata.
- A statement of which legal entity validates the model (typically the sponsor bank for any model that touches the bank's regulated activity).
- A statement of which regulator examines the model in practice (sponsor-bank's federal banking regulator typically, with CFPB reach for consumer products).
- The firm's posture on the OCC / FRB / FDIC interagency guidance on third-party relationships (June 2023) and the OCC / FRB / FDIC Joint Statement on Bank-Fintech Arrangements (July 2024) [verify date].

Plan-writer flag: in a sponsor-bank arrangement, "the fintech built the model" is not a defence to bank-side validation expectations. The validation plan reads to the bank-side standard regardless of where the model was built.

##### 2. Transaction-monitoring (TM) model validation under BSA/AML

For TM models in payments and money transmission, FinCEN expectations under the BSA, the FFIEC BSA/AML Examination Manual, and (for state-regulated money transmitters) state money-transmission examiners apply. The plan:

- Names the BSA officer or designee as a sign-off audience.
- Adds above-the-line / below-the-line testing in outcomes-analysis scope; this is the productivity test FFIEC examiners look for.
- Treats threshold tuning as a controls-scope validation item; threshold changes that materially shift alert volumes are change-management triggers and re-validation triggers in monitoring scope.
- Does not represent fraud-model performance metrics as AML-effectiveness evidence in outcomes-analysis; the two are doctrinally distinct.

For NY-licensed entities, NYDFS Part 504 senior-officer certification posture for TM models is a plan effective-challenge question.

##### 3. Faster-payments-rail validation specifics

For models operating on FedNow, RTP, or Same Day ACH inbound, the irrevocability-driven typology shift changes the validation surface. The plan:

- Adds rail-by-rail outcomes-analysis cuts where the firm operates on multiple rails.
- Adds request-for-return-of-funds latency as a monitoring metric for FedNow / RTP fraud holds.
- Includes ISO 20022 message-field anomaly tests (suspicious creditor account, suspicious end-to-end ID) in outcomes-analysis scope where applicable.

##### 4. Account-takeover (ATO) and fraud-model validation

For ATO detection, fraud-decline models, and step-up authentication models, the plan adds:

- Authentication-flow integration check in conceptual-soundness scope (which step, which decision boundary, which fallback path).
- False-positive vs false-negative trade-off explicitly in outcomes-analysis scope, with named owners for each side of the trade-off (fraud team vs customer-experience team).
- Reg E reach for unauthorised consumer transactions; the plan flags consumer-recourse for false declines as a controls-scope item.
- For card-program models, network rules (Visa, Mastercard, AmEx) apply; chargeback-rate program escalation (Visa fraud-monitoring program tiers, Mastercard equivalents) is a monitoring entry with re-validation trigger.

##### 5. Onboarding-decisioning models and KYC/CIP

For models that influence onboarding (account-opening risk, KYC document review, identity-verification scoring), the plan carries:

- CIP and KYC integration check in conceptual-soundness scope; the model triages but does not substitute for the CIP rule (31 CFR 1020.220 for banks; 31 CFR 1010.230 for beneficial-ownership where applicable).
- Identity-verification vendor evidence enumerated in dependencies (vendor-supplied evaluation, plus firm-side validation).
- ECOA reach for onboarding implicating credit (e.g., card programs); UDAAP reach for deposit-only programs.

##### 6. CFPB UDAAP and Reg E reach

For consumer-facing payments and fintech models, CFPB has authority under Dodd-Frank Title X for UDAAP and over Reg E (electronic fund transfers) and Reg DD (truth in savings) for deposit programs. The plan:

- Includes consumer-impact framing in any decision that affects a consumer transaction.
- Scopes Reg E error-resolution timing (10 / 45 / 90-day windows) where the model influences a consumer dispute.
- Adds complaint-rate drift to monitoring scope (CFPB complaint database plus internal feed; sponsor-bank-routed feed where applicable).
- Adds the larger-participant rule for digital wallets and payment apps (CFPB final rule, December 2024) [verify Federal Register citation, effective date, and current state including any litigation or congressional review] applicability check in plan metadata.

##### 7. State money-transmission examination reach

For state-licensed money transmitters, state examiners (in many states the financial regulator) apply state-specific exam standards; multi-state CSBS-coordinated exams may apply. The plan flags state-licensure footprint and the strictest-applicable-state posture. NMLS posture and Money Transmitter Modernization Act adoption status [verify state-by-state] enter plan metadata.

##### 8. NACHA Operating Rules — Third-Party Sender risk-management

For ODFIs, the plan's monitoring scope includes return-rate monitoring against current NACHA thresholds (administrative-return, overall-return, unauthorized-return) [verify current thresholds]. Where the firm acts as a Third-Party Sender on another ODFI's authority, registration status and Originator-agreement evidence are dependencies.

#### Payments and fintech-specific output template additions

- `plan_metadata.legal_entity_type` — money transmitter / payments processor / sponsor-bank program / prepaid issuer / BIN sponsor / non-bank consumer-finance / fintech app.
- `plan_metadata.sponsor_bank_arrangement` — boolean; if true, sponsor-bank-side validator and federal banking regulator named.
- `plan_metadata.state_licensure_footprint` — list of states with money-transmission or other licences.
- `plan_metadata.network_rules_inscope` — boolean; if true, named networks (Visa, Mastercard, AmEx, ACH, FedNow, RTP) recorded.
- `plan_metadata.larger_participant_inscope` — boolean; CFPB digital-wallet larger-participant rule applicability.
- `data_review.scope_items[]` — CIP / KYC integration check for onboarding-decisioning models.
- `outcomes_analysis[]` — above-the-line / below-the-line testing for AML TM models; rail-by-rail outcomes for faster-payments models; chargeback-rate-program-tier monitoring for card-program models.
- `monitoring[]` — Reg E error-resolution-timing breach as re-validation trigger; complaint-rate drift; NACHA return-rate against current thresholds.
- `effective_challenge_questions[]` — payments-specific (sponsor-bank validator, BSA officer sign-off, NYDFS Part 504 certification, state money-transmission examiner posture, network-rule reach, larger-participant-rule applicability).

#### Common pitfalls in payments and fintech validation plans

- Treating the fintech as the sole model owner when the sponsor bank inherits the model risk; bank examiners catch this in third-party reviews.
- Omitting BSA officer sign-off on a TM model; FFIEC manual expectation is clear.
- Reporting fraud-model performance as AML-effectiveness evidence in outcomes analysis; the two are doctrinally distinct.
- Missing Reg E error-resolution posture on a model that drives consumer transaction declines or holds.
- Treating state money-transmission exams as a footnote; state examiners regularly review TM models in money-transmission exams.
- Missing NYDFS Part 504 senior-officer certification posture for TM models in NY footprint.
- Asserting that vendor identity-verification scores are sufficient evidence of CIP compliance; CIP is the firm's regulatory obligation, not the vendor's.
- Treating faster-payments rails as ACH-with-shorter-windows; the irrevocability shift changes the typology surface and the validation tests should reflect that.
