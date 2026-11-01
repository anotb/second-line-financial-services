# sector-overlays

One section per sector. Read only the sections the scope calls for.

## banking

### Banking sector overlay for model-card-builder

When the scope record names sector `banking`, this overlay adds banking-specific fields and review demands to the card. Where there is conflict between the capability defaults and this overlay, the overlay governs the banking-sector elements.

Loaded by: `model-card-builder/SKILL.md` when `scope.sector_overlay_set` includes `banking`, or when the institution type implicates a federal banking regulator (national bank, state member bank, savings association, bank holding company, foreign banking organization with US operations).

#### Source basis

Cited and section-referenced in `references/source-anchors.md`. This overlay names the regulators and sources without restating excerpts.

#### What changes for banking model cards

##### 1. Joint interagency model-risk guidance for federally supervised banks

The 2026 joint interagency Revised Guidance on Model Risk Management (OCC Bulletin 2026-13 / FRB SR 26-2 / FDIC FIL-15-2026, April 17, 2026) is the current model-risk supervisory expectation for OCC-, FRB-, and FDIC-supervised banks. It supersedes SR 11-7 (2011) and SR 21-8 (the 2021 BSA/AML model-risk interagency statement). The model card is the firm-side documentation artifact aligned to the principles in the joint guidance.

Practical reach. The joint guidance is most relevant to banking organizations with over $30 billion in total assets, and is non-binding (does not set enforceable standards). For mid-size and community banks below that threshold, treat the principles as leading-practice rather than as a prudential mandate; firm policy still drives card scope and depth. Generative AI and agentic AI are explicitly out of scope (footnote 3); for those use cases, anchor the card to the AI-specific frameworks (NIST AI RMF, NIST AI 600-1, ISO/IEC 42001) and the cross-cutting overlays. The joint guidance does not reference NIST AI RMF or NIST AI 600-1; do not cite the joint guidance as the controlling anchor for GenAI/agentic documentation.

For non-bank affiliates under the same parent (a sister broker-dealer or asset manager), the joint guidance reaches by extension only when the bank inherits model risk through transactions, services, or balance-sheet exposure. Card-writer should not over-claim reach to non-bank entities.

##### 2. OCC Heightened Standards (12 CFR Part 30 Appendix D)

For OCC-supervised large banks (currently set by asset-size threshold; see source-anchors), the Heightened Standards add a board-level risk-governance frame: independent risk management, risk-appetite statement, and compliance-program elements that reach into model risk. The model card supports the inventory and governance evidence that those board obligations rely on.

Card-side implications:

- Tier-1 models in scope of a category-I/II/III bank typically appear in the risk-appetite statement; the card section "Tier" should reference the firm's appetite statement classification.
- The Heightened Standards' independence requirement maps to the validator/second-line-reviewer fields in card metadata; for tier-1 cards, the second-line reviewer must be independent of model development.

##### 3. ECOA / Reg B adverse action surface for credit-decisioning models

Where the model influences a credit decision (origination, pricing, line management, collections triggers, fraud-driven adverse action), Regulation B requires a specific, accurate adverse action notice. The card's fairness and explainability section, and the controls section, must address adverse action notice generation and quality.

Specifically reference:

- The Reg B §1002.9 specific-reasons requirement and Comment 9(b)(2)-3 of the Official Staff Commentary, which require the cited reasons to relate to and accurately describe the factors actually considered or scored. CFPB Circulars 2022-03 (specific-and-accurate reasons even when the model is complex) and 2023-03 (reasons given must be the actual principal reasons, not sample-form artefacts) **were withdrawn May 12, 2025; historical only**. The regulatory text continues to apply on its own terms.
- The firm's adverse action notice generation method (typically SHAP-based or reason-code-mapped) and any sampling/quality control for notice accuracy.

Sign-off questions (banking, credit-decisioning):
- What is the method of adverse action reason generation, and how is its accuracy sampled?
- How does the firm handle a proxy variable identified post-deployment as fairness-sensitive?
- What is the integration with the firm's fair-lending test plan, and at what cadence?

##### 4. CCAR / DFAST overlap for stress-eligible banks

For banks subject to stress testing (currently DFAST and the Federal Reserve's CCAR for the largest bank holding companies), models used in stress projections, allowance methodology (CECL under ASC 326), and capital planning are in scope. The card for any such model needs:

- Stress-testing pedigree section in the source trace (was the model developed for, validated for, and currently approved for use in the relevant stress submission?).
- Cross-link to the firm's CECL methodology owner, where applicable.
- Re-validation trigger for the annual stress-testing cycle.

Card-writer flag: if the model touches stress, do not rely on this skill alone; the firm's CCAR/DFAST owner has additional model documentation expectations under SR 15-18 or successor guidance [verify SR letter].

##### 5. AML, BSA, and fraud-model framing

For models supporting BSA/AML transaction monitoring, sanctions screening, customer risk rating, and fraud detection, the FFIEC BSA/AML Examination Manual sets the supervisory frame; the card should:

- Name the BSA officer or designee as a signoff reviewer when the card touches AML use cases.
- Record the model's role in the suspicious activity report (SAR) workflow without claiming the model files SARs (the firm files SARs; the model triages or scores).
- Treat threshold tuning as a controls-section item; threshold changes that materially shift alert volumes are change-management triggers.
- Avoid representing fraud-model performance metrics as AML-effectiveness evidence; the two are doctrinally distinct.

##### 6. CRA-relevant models

For models that influence community-development assessment, low-and-moderate-income outreach, or branch-network analytics where they touch CRA performance, the card adds a CRA-context note. Firm policy may require the head of community reinvestment as a signoff reviewer.

##### 7. Banking-specific monitoring expectations

In addition to the capability defaults, banking model cards typically include:

- Population stability index (PSI) monitoring on input features, with breach thresholds set against firm policy and against industry-typical breaches (PSI > 0.25 triggers re-fit consideration).
- Score drift monitoring (KS or PSI on score distribution) against a reference distribution.
- Decisioning-rate drift monitoring (approval rate, override rate, decline rate) by segment.
- Where applicable, complaint-rate drift from the CFPB complaint database plus internal complaint feed.

#### Banking-specific output template additions

The following fields are added to the card (mapped to schema where present):

- `card_metadata.heightened_standards_inscope` — boolean, true for OCC large banks subject to 12 CFR Part 30 Appendix D.
- `card_metadata.bank_charter_type` — national bank / state member / state nonmember / savings association / BHC / FBO.
- `card_metadata.primary_federal_regulator` — OCC / FRB / FDIC / NCUA.
- `card_metadata.stress_testing_inscope` — boolean, with cross-reference to CCAR or DFAST submission.
- `data[].cra_relevance` — boolean flag for CRA-touching data sources.
- `controls[]` — adverse action notice generation control listed explicitly when the model is credit-decisioning.
- `signoff_questions[]` — banking-specific questions (adverse action method, fair-lending integration, CCAR/DFAST pedigree).

#### Common pitfalls in banking model cards

- Treating CFPB authority as out of scope because the entity is OCC- or FRB-supervised; CFPB consumer-protection authority reaches large banks for ECOA, RESPA, EFTA, and UDAAP purposes.
- Reporting model performance only on a development holdout; supervisory expectations look for performance under deployment conditions, not just lab metrics.
- Omitting the proxy-variable post-deployment process; both CFPB and OCC fair-lending exam practice probe this seam.
- Citing "vendor system card" as standalone evidence for a foundation-model dependency; for banks, vendor evidence supplements but does not substitute for the firm's own validation and documentation.
- Omitting the stress-testing pedigree section when the model is in fact used in stress; auditors and examiners catch this in the cross-walk.

## capital-markets

### Capital markets sector overlay for model-card-builder

When the scope record names sector `capital-markets`, this overlay adds capital-markets-specific fields and review demands to the card. Where there is conflict between the capability defaults and this overlay, the overlay governs the capital-markets-sector elements.

Cited and section-referenced anchors in `references/source-anchors.md`.

#### What changes for capital-markets model cards

##### 1. SR 11-7 reach is partial, not blanket

For investment advisers and broker-dealers that are not part of a bank holding company, SR 11-7 is not directly binding. The card uses NIST AI RMF and ISO/IEC 42001 as the primary anchor; SR 11-7 is referenced where the parent BHC inherits the model risk through a banking subsidiary. Card-writer should not assert SR 11-7 reach to standalone advisers/BDs.

The substantive expectations (intended use, data, performance, monitoring, controls, sign-off) are the same; the regulator constellation differs.

##### 2. SEC and FINRA expectations come through Rule 206(4)-7, FINRA 3110, Reg BI, and Marketing Rule

For an investment adviser, the model's role in the compliance program connects through Rule 206(4)-7 (compliance program adoption and annual review). For a broker-dealer, FINRA Rule 3110 (supervisory system) and Reg BI (best interest, care obligation) are the primary frames. The model card supports the supervision and disclosure evidence the rules expect.

Card-side implications:

- For an adviser: the CCO is an audience; the annual Rule 206(4)-7 review is a re-validation cadence trigger.
- For a BD: supervisory system documentation is a card audience; FINRA WSPs reference the model.

##### 3. SEC predictive-data-analytics rulemaking

The SEC proposed rules on conflicts of interest in the use of predictive data analytics by broker-dealers and investment advisers (proposed July 2023) [verify current state — proposal, withdrawal, or further action]. The card flags the conflict-of-interest question for any model that interacts with retail-investor decisions. Where the rule is currently in proposal or non-final state, the card records the firm's monitoring posture rather than asserting compliance with a non-final rule.

##### 4. AI in marketing materials and the Marketing Rule

For investment advisers under the IAA, Marketing Rule (Rule 206(4)-1) coverage extends to AI-generated client communications, AI-generated hypothetical performance, and AI-generated testimonials/endorsements. The card flags Marketing Rule reach when the model output reaches clients or prospective clients; required disclosures are a controls-section item.

##### 5. Best-execution surveillance, execution algos, and trading models

For execution algorithms and trading-related models, additional anchors apply:

- SEC Rule 15c3-5 (Market Access Rule) controls overlap; the card section on controls names financial and regulatory risk management controls per Rule 15c3-5.
- FINRA Rule 5310 best-execution obligations; for models that influence execution venue choice, the card carries a best-execution-monitoring control reference.
- For surveillance models (insider trading, market manipulation, spoofing detection, layering), FINRA Rule 3110 supervisory expectations apply; the card section on controls names the supervisory-system integration.

##### 6. Books-and-records reach (Rule 204-2 for advisers; Rule 17a-3/4 for BDs)

For any model that supports an advisory recommendation or a trading decision, books-and-records rules apply to the model output and to the inputs that drove it. The card carries:

- A retention statement for model outputs that support recommendations.
- A retention statement for inputs and decisions where the rule reaches the underlying basis.
- A note on the firm's books-and-records system of record for AI-generated content (for GenAI use cases, this is a frequent gap).

##### 7. Sub-adviser and fund-board awareness

Where the model is operated by a sub-adviser on the registrant's funds, sub-adviser oversight under 38a-1(a)(4) applies. The card identifies sub-adviser operation, the firm's oversight cadence, and the fund-board reporting posture. For a 1940 Act fund context, the fund's CCO is an additional card audience.

##### 8. AIFMD / MiFID II for cross-border activity

For US advisers serving EU professional or retail clients, AIFMD / MiFID II overlay can extend; the card flags EU client exposure and routes to `ai-act-triage` for the EU-applicability scoping.

#### Capital-markets-specific output template additions

- `card_metadata.legal_entity_type` — investment adviser / broker-dealer / dual registrant / 1940 Act fund / 1933 Act issuer / municipal-securities entity.
- `card_metadata.primary_regulator_constellation` — SEC / FINRA / state-IA / MSRB / NYSE / CBOE / FOREX / other.
- `card_metadata.fund_board_reporting_inscope` — boolean; for 1940 Act fund use cases.
- `card_metadata.sub_adviser_operated` — boolean; if true, sub-adviser oversight cadence is a controls field.
- `card_metadata.marketing_rule_reach` — boolean; for AI generating client-facing content.
- `card_metadata.market_access_rule_inscope` — boolean; for execution algo or order-routing models under Rule 15c3-5.
- `data[].books_and_records_retention` — retention statement aligned to Rule 204-2 or Rule 17a-3/4 as applicable.
- `controls[]` — best-execution monitoring (Rule 5310) where applicable; supervisory-system integration (FINRA 3110) where applicable; conflict-of-interest disclosure where applicable.
- `signoff_questions[]` — capital-markets-specific (CCO sign-off, fund-board reporting posture, books-and-records reach, predictive-analytics rulemaking posture, Marketing Rule reach where applicable).

#### Common pitfalls in capital-markets model cards

- Importing SR 11-7 vocabulary into an adviser/BD card without confirming SR 11-7 reach; it does not directly apply to non-bank registrants.
- Omitting books-and-records reach for AI-generated client content; Rule 204-2 catches the firm at exam time.
- Treating the SEC predictive-analytics proposal as binding when it is currently in non-final state; or treating it as irrelevant when the firm's risk register already monitors the proposal.
- Missing Marketing Rule reach for AI-generated investment-letter drafts or RFP-response generation.
- Forgetting fund-board reporting posture for sub-adviser-operated AI on the registrant's funds.
- Treating execution-algo Market Access Rule controls as engineering controls rather than card-section controls; Rule 15c3-5 controls are governance controls and belong in the card.

## insurance

### Insurance sector overlay for model-card-builder

When the scope record names sector `insurance`, this overlay adds insurance-specific fields and review demands to the card. Where there is conflict between the capability defaults and this overlay, the overlay governs the insurance-sector elements.

Cited and section-referenced anchors in `references/source-anchors.md`.

#### What changes for insurance model cards

##### 1. NAIC Bulletin on the Use of Artificial Intelligence Systems by Insurers (December 2023) is the spine

The Bulletin sets out an AIS Program (governance, risk management, testing, validation, third-party AI accountability, monitoring, documentation, transparency, fairness). The model card is one of the documentation artifacts the AIS Program demands. The Bulletin is itself a model bulletin; state-by-state adoption is tracked by the NAIC AI Working Group adoption tracker. Card-writer flag: cite by jurisdiction, do not assert the Bulletin as binding without state adoption confirmation.

The card carries an AIS Program element-by-element status block (governance, risk management, testing, validation, third-party AI accountability, monitoring, documentation, transparency, fairness), each tied to evidence in the source trace. This is the insurance-specific addition that a state DOI rate analyst will recognise.

##### 2. State DOI bulletins extend the bar in named jurisdictions

The card identifies the operating footprint and flags the strictest applicable state. Named bulletins to enumerate when in scope:

- Colorado Division of Insurance regulation implementing SB 21-169 — governance and risk management of External Consumer Data and Information Sources (ECDIS) and predictive models in life-insurance underwriting. ECDIS provenance is a card field when CO is in scope.
- New York DFS Insurance Circular Letter on AI and ECDIS in life-insurance underwriting (January 2024) — governance, fairness testing, disclosure, and consumer-recourse expectations.
- California DOI bulletin on AI use in insurance — broader than CO/NY in scope but informs disclosure posture.

##### 3. Fairness vs unfair discrimination — vocabulary translation

Capability fairness vocabulary (disparate impact, AIR, demographic parity) and insurance unfair-discrimination vocabulary (NAIC Unfair Trade Practices Act Model #880) are not the same legal test. State insurance code allows actuarially justified rating differences that would be challenged under disparate-impact frameworks elsewhere; conversely, some state insurance code prohibitions reach uses of variables (e.g., credit-based insurance scores in some states) that disparate-impact analysis would not flag.

The card's fairness section uses both vocabularies when applicable, and includes a translation note. The sign-off question explicitly asks whether the test framing matches the regulator's test framing.

##### 4. ECDIS-driven rating and underwriting

Where the model uses external consumer data and information sources (third-party data beyond traditional underwriting variables), the card carries:

- ECDIS provenance for each data source: provider, lineage, refresh, consumer-disclosure posture, consumer-recourse channel.
- Per-state ECDIS treatment: CO regulation imposes specific governance and disclosure on ECDIS use in life underwriting; other states may follow.
- HIPAA touch flag for any health-data ECDIS feed.

##### 5. Insurance use-case categories

The card recognises which insurance-AI use case category applies; the controls and limitations sections differ across them:

- Accelerated underwriting (life, health): tier elevation; ECDIS likely; HIPAA likely; CO/NY DFS bulletins apply.
- Claims AI (FNOL triage, severity prediction, fraud-indicator scoring, claims chatbot): NAIC Model #880 unfair-claims-settlement standards apply regardless of decision technology; state UCSPA timing and notice obligations apply.
- Pricing / rating ML factors: state DOI rate filing and prior-approval regimes apply where the model touches filed rates; rate analyst is a card audience.
- Marketing AI (suitability, replacement risk for annuities): NAIC Model #275 [verify model number] for annuity suitability.
- Agent-AI co-pilots: producer-licensing reach; suitability and best-interest standards.
- Back-office AI (call-center summarisation, mailroom OCR): generally lower tier.

##### 6. ORSA materiality and Holding Company filings

For an enterprise-material AI use case, NAIC ORSA (Model #505) inclusion is required; the card flags ORSA inclusion and cross-references the firm's ORSA Summary Report. Holding Company filings (Form B affiliated services, Form D affiliated transactions) under Model #440 / #450 [verify] apply where the AI is provided by an affiliate.

##### 7. HIPAA scope check

Any insurance AI touching PHI (health-claims AI, life-and-health underwriting using prescription-history or medical data) requires a HIPAA Privacy and Security Rule cross-check; HIPAA business-associate-agreement posture is a card data-section field for any vendor handling PHI.

##### 8. Producer licensing on consumer-facing AI

A consumer-facing AI that takes binding-equivalent actions (binding, quoting commitments, surrendering, paying claims) can trigger producer-licensing questions; flag for the licensing function. Card sign-off questions probe the boundary.

##### 9. Vendor-AI accountability

NAIC Bulletin Dec 2023 holds the carrier accountable for vendor and third-party AI used on its policies. The card's data and controls sections name the vendor, the firm-side governance, and the firm-side monitoring; vendor self-attestations are recorded but do not substitute for firm-side evidence.

#### Insurance-specific output template additions

- `card_metadata.ais_program_status` — element-by-element status block (governance, risk management, testing, validation, third-party AI accountability, monitoring, documentation, transparency, fairness).
- `card_metadata.state_doi_status` — per-state status (CO, NY, CA at minimum if in operating footprint).
- `card_metadata.orsa_inscope` — boolean.
- `card_metadata.hipaa_touch` — boolean; if true, BAA reference required for any PHI-handling vendor.
- `card_metadata.producer_licensing_posture` — for consumer-facing AI taking binding-equivalent actions.
- `data[].ecdis_provenance` — provider, lineage, refresh, consumer-disclosure posture, consumer-recourse channel.
- `fairness_results[].test_framing` — fairness / unfair-discrimination / both.
- `signoff_questions[]` — insurance-specific (AIS Program element status, state DOI strictest-applicable, ECDIS posture, ORSA fit, HIPAA touch, producer-licensing).

#### Common pitfalls in insurance model cards

- Carrying generic fairness vocabulary into a rate-filing context; state DOI rate analysts use unfair-discrimination vocabulary.
- Treating the NAIC Bulletin as US-uniform; adoption is state-by-state and the Bulletin is itself non-binding until state adoption.
- Omitting ECDIS provenance for a life-underwriting model when CO or NY is in operating footprint.
- Missing HIPAA BAA reference for a vendor handling PHI.
- Treating claims AI as a pure technology question without the Model #880 fair-claims-settlement frame.
- Forgetting that the TPA's controls are the carrier's controls under NAIC Insurance Data Security Model Law (#668) §4.F when the model runs at a TPA.
- Treating the AIS Program elements as a checklist; the card is the evidence, the elements are the structure.

## payments-fintech

### Payments and fintech sector overlay for model-card-builder

When the scope record names sector `payments-fintech`, this overlay adds payments- and fintech-specific fields and review demands to the card. Where there is conflict between the capability defaults and this overlay, the overlay governs the sector elements.

Loaded by: `model-card-builder/SKILL.md` when `scope.sector_overlay_set` includes `payments-fintech`, or when the institution type implicates a money transmitter, payments processor, fintech program, sponsor-bank arrangement, prepaid issuer, BIN sponsor, or non-bank consumer-finance entity.

Cited and section-referenced anchors in `references/source-anchors.md`.

#### What changes for payments and fintech model cards

##### 1. Sponsor-bank model risk responsibility allocation

For sponsor-bank programs (a fintech offering deposit, lending, or card products through a sponsor-bank balance sheet), the model risk responsibility is allocated by the bank-fintech contract and by the bank's own model risk policy. The card carries:

- A statement of which legal entity owns the model (sponsor bank / fintech / shared).
- A statement of which legal entity validates the model and signs the card (typically the sponsor bank for any model that touches the bank's regulated activity).
- A statement of which regulator examines the model in practice (sponsor-bank's federal banking regulator typically, with CFPB reach for consumer products).
- The firm's posture on the FDIC and OCC sponsor-bank oversight expectations (joint OCC/FRB/FDIC interagency guidance on third-party relationships, June 2023).

Card-writer flag: in a sponsor-bank arrangement, "the fintech built the model" is not a defence to bank-side documentation expectations.

##### 2. Transaction-monitoring (TM) model risk overlap with BSA/AML

For TM models in payments and money-transmission, FinCEN expectations under the BSA, the FFIEC BSA/AML Examination Manual, and (for state-regulated money transmitters) state money-transmission examiners apply. The card carries:

- BSA officer or designee as a signoff reviewer.
- Threshold-tuning posture as a controls-section item; threshold changes that materially shift alert volumes are change-management triggers.
- The model's role in the SAR workflow without claiming the model files SARs (the firm files SARs; the model triages or scores).
- Above-the-line / below-the-line testing cadence and ownership.

##### 3. Account-takeover (ATO) detection and fraud models

For ATO detection, fraud-decline models, and step-up authentication models, the card adds:

- The model's authentication-flow integration (which step, which decision boundary, which fallback path).
- The fraud-team and customer-experience trade-off statement (false-positive rate vs false-negative rate, with named owners for each).
- Reg E reach for unauthorised consumer transactions; the card flags the consumer-recourse channel for false declines.
- For card-program models, network rules (Visa, Mastercard, AmEx) apply in addition to regulatory expectations; the card flags network rule reach where applicable.

##### 4. Onboarding-decisioning models and KYC/CIP

For models that influence onboarding (account-opening risk, KYC document review, identity-verification scoring), the card carries:

- CIP and KYC integration statement; the model triages but does not substitute for the CIP rule (31 CFR 1020.220 for banks; 31 CFR 1010.230 for beneficial-ownership where applicable).
- Adverse decisioning posture for ECOA reach where the onboarding implicates credit (e.g., card programs); for deposit-only programs, ECOA may not reach but consumer-protection (UDAAP) does.
- Identity-verification vendor evidence (vendor-supplied evaluation, plus firm-side validation).

##### 5. CFPB UDAAP and Reg E reach

For consumer-facing payments and fintech models, the CFPB has authority under Dodd-Frank Title X for UDAAP and over consumer-protection rules including Reg E (electronic fund transfers) and Reg DD (truth in savings) for deposit programs. The card carries:

- Consumer-impact framing for any decision that affects a consumer transaction.
- Reg E error-resolution posture where the model influences a consumer dispute.
- Complaint-rate drift monitoring (CFPB complaint database plus internal feed).

##### 6. State money-transmission examination reach

For state-licensed money transmitters, state examiners (in many states, the financial regulator) apply state-specific exam standards; multi-state Conference of State Bank Supervisors (CSBS) NMLS-coordinated exams may apply. The card flags state-licensure footprint and the strictest-applicable-state posture.

##### 7. NYDFS Part 504 (transaction monitoring) and Part 500 (cyber)

For NY-licensed fintechs and DFS-regulated money transmitters, Part 504 imposes specific TM-program expectations including the senior-officer certification; the card flags NY footprint and the certification posture for TM models. NYDFS Part 500 cyber expectations apply across the operation.

#### Payments and fintech-specific output template additions

- `card_metadata.legal_entity_type` — money transmitter / payments processor / sponsor-bank program / prepaid issuer / BIN sponsor / non-bank consumer-finance / fintech app.
- `card_metadata.sponsor_bank_arrangement` — boolean; if true, sponsor-bank-side validator and federal banking regulator named.
- `card_metadata.state_licensure_footprint` — list of states with money-transmission or other licences.
- `card_metadata.network_rules_inscope` — boolean; if true, named networks (Visa, Mastercard, AmEx, network ACH, RTP) recorded.
- `data[].cip_kyc_integration` — for onboarding-decisioning models.
- `controls[]` — Reg E error-resolution posture (consumer products); SAR-workflow integration (TM models); network-rule controls (card programs).
- `signoff_questions[]` — payments-specific (sponsor-bank validator, BSA officer signoff, NYDFS Part 504 certification, state money-transmission examiner posture, network-rule reach).

#### Common pitfalls in payments and fintech model cards

- Treating the fintech as the sole model owner when the sponsor bank inherits the model risk; bank examiners catch this in third-party reviews.
- Omitting BSA officer signoff on a TM model; FFIEC manual expectation is clear.
- Reporting fraud-model performance as AML-effectiveness evidence; the two are doctrinally distinct.
- Missing Reg E error-resolution posture on a model that drives consumer transaction declines or holds.
- Treating state money-transmission exams as a footnote; state examiners regularly review TM models in money-transmission exams.
- Missing NYDFS Part 504 senior-officer certification posture for TM models in the NY footprint.
- Asserting that vendor identity-verification scores are sufficient evidence of CIP compliance; CIP is the firm's, not the vendor's, regulatory obligation.
