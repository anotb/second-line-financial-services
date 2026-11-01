# sector-overlays

One section per sector. Read only the sections the scope calls for.

## banking

### Banking sector overlay for ai-risk-tiering

When the scope record names sector `banking`, this overlay tells the tier rubric what is banking-specific and which named regulators and bulletins set the bar. The overlay does not invent tier names or cutoffs (those are firm policy); it tells the rubric which factors elevate, which gates trigger by default, and which re-tiering events to name.

Loaded by: `ai-risk-tiering/SKILL.md` when `scope.sector_overlay_set` includes `banking`, or when the institution type implicates a federal banking regulator (national bank, state member bank, savings association, BHC, FBO with US operations).

#### Source basis

Cited and section-referenced in `references/source-anchors.md`. This overlay names the regulators and sources without restating excerpts.

#### What changes for banking tiering decisions

##### 1. SR 11-7 §III risk-based principle is binding

For federally regulated banks, the tier produced by this skill is the firm-side artefact that operationalises the materiality-based risk-rating principle. The current binding anchor is the joint interagency Revised Guidance on Model Risk Management (OCC 2026-13 / FRB SR 26-2 / FDIC FIL-15-2026, April 17 2026; supersedes SR 11-7 and SR 21-8) for traditional statistical and quantitative models. The bulletin expressly excludes generative AI and agentic AI from its scope (footnote 3); for those use cases the rubric's GenAI-specific factor anchors to NIST AI 600-1, ISO/IEC 42001, and the cyber overlay rather than the bulletin. Tier names and cutoffs remain firm policy; the materiality factors (purpose, decision influence, financial exposure, complexity, uncertainty, vendor dependence) are the spine of the rubric.

For non-bank registrants under the same parent, SR 11-7 reaches by extension only when the bank inherits model risk through transactions, services, or balance-sheet exposure. Tiering record should not over-claim SR 11-7 reach to non-bank entities.

##### 2. OCC Heightened Standards (12 CFR Part 30 Appendix D)

For OCC-supervised large banks, the Heightened Standards add a board-level risk-governance frame; risk-appetite statements name model risk and tier-1 models typically appear by name or by category. Tier-side implications:

- The tier decision references the firm's risk-appetite-statement classification where the bank is in scope.
- Tier-1 cards in scope of an in-scope bank trigger AI risk committee approval at minimum; firm policy may stack additional approvals.

##### 3. ECOA / Reg B adverse-action surface

Where the AI use case influences a credit decision (origination, pricing, line management, collections triggers, fraud-driven adverse action), the tier rubric reads the conduct factor as high and the regulatory factor as high. Specifically:

- Reg B §1002.9: a creditor must provide specific principal reasons for adverse action; the tier decision flags adverse-action notice generation as a triggered control gate.
- Comment 9(b)(2)-3 of the Official Staff Commentary: the cited reasons must relate to and accurately describe the factors actually considered or scored; the tier decision flags adverse-action notice quality sampling as a monitoring gate.
- CFPB Circulars 2022-03 (complex algorithms do not excuse the specific-reasons requirement) and 2023-03 (reasons must be actual principal reasons) are **withdrawn May 12, 2025; historical only**. The conduct and regulatory factor scoring stands on Reg B and the Official Staff Commentary; the tier decision does not depend on the withdrawn circulars.

Default sign-off questions added at tier-1 for credit-decisioning use cases:

- What is the method of adverse-action reason generation, and how is its accuracy sampled?
- How does the firm handle a proxy variable identified post-deployment as fairness-sensitive?
- What is the integration with the firm's fair-lending test plan, and at what cadence?

##### 4. CCAR / DFAST and CECL overlap

For banks subject to stress testing (DFAST, CCAR for the largest BHCs) and for CECL methodology under ASC 326, models in scope for stress projections, allowance methodology, or capital planning are read as tier-1 by default under most firm policies regardless of customer-facing posture. The tier decision:

- Flags the stress-testing pedigree as a triggered control gate.
- Names the annual stress-testing cycle as a re-tiering trigger.
- Cross-references CCAR/DFAST owner; this skill does not own the stress-testing-side documentation expectations.

Tiering-record flag: a stress-eligible model carries SR 15-18 or successor-letter expectations [verify SR letter] in addition to the joint interagency Revised Guidance on Model Risk Management (OCC 2026-13 / FRB SR 26-2 / FDIC FIL-15-2026).

##### 5. AML, BSA, sanctions, and fraud framing

For models supporting BSA/AML transaction monitoring, sanctions screening, customer risk rating, and fraud detection, the FFIEC BSA/AML Examination Manual sets the supervisory frame. Tier-side implications:

- Threshold tuning and SAR-workflow integration push the regulatory and conduct factors upward.
- BSA officer or designee is a named approver on triggered gates when the use case touches AML.
- The tier decision distinguishes fraud-model performance from AML-effectiveness evidence; the two are doctrinally distinct and must not be conflated at tier-decision time.

##### 6. Bank-fintech arrangements and sponsor-bank reach

For sponsor-bank programs, OCC Bulletin 2023-17 / FRB SR 23-4 / FDIC FIL-29-2023 (June 2023) and the OCC / FRB / FDIC Joint Statement on Bank-Fintech Arrangements (July 25, 2024) [verify date] are operative. Where the bank inherits model risk from a fintech-supplied model:

- Vendor-dependence factor scores at minimum medium; concentration-risk factor scores upward when a single fintech is the dominant program.
- The tier decision names the sponsor-bank validator and the bank-side committee path even when day-to-day operation sits at the fintech.
- A re-tiering trigger fires on any change in the sponsor-bank-fintech arrangement, including program expansion or contraction.

##### 7. CRA-relevant models

For models that influence community-development assessment, low-and-moderate-income outreach, or branch-network analytics where they touch CRA performance, the regulatory factor scores at least medium. Firm policy may add the head of community reinvestment as an approver on triggered gates.

#### Banking-specific tier-elevation factors

In addition to the capability rubric, the following bank-specific factors elevate the tier:

- In-scope CCAR/DFAST or CECL use case → tier-1 by default under most firm policies.
- Customer-binding credit decisioning under ECOA / Reg B → conduct factor high, regulatory factor high.
- AML, sanctions, or BSA transaction-monitoring use case at scale → regulatory factor high, FFIEC manual exposure named.
- OCC Heightened Standards bank with model in risk-appetite statement → tier-1 by default for the named model.
- Sponsor-bank arrangement with fintech-supplied AI → vendor-dependence and concentration factors elevated; bank-side committee path named.

#### Banking-specific re-tiering triggers

Add to the re-tiering trigger block for banking sector use cases:

- Annual stress-testing cycle (where in scope). Owner: stress-testing function. Detection: stress-testing calendar.
- Adverse-action notice generation method change. Owner: consumer compliance with model owner. Detection: change-management notice.
- Material change in NACHA, OFAC, or FFIEC manual expectations relevant to the use case. Owner: regulatory change function. Detection: regulatory horizon scan.
- Sponsor-bank-fintech arrangement change (program expansion, dual-sponsor add, sponsor exit). Owner: bank's third-party risk function. Detection: third-party-risk reporting plus contract change-control.
- MRA / MRIA issued against the use case or against a closely related model. Owner: regulatory affairs. Detection: examiner correspondence.

#### Common pitfalls in banking tiering

- Treating CFPB authority as out of scope because the entity is OCC- or FRB-supervised; CFPB consumer-protection authority reaches large banks for ECOA, RESPA, EFTA, and UDAAP purposes.
- Treating an AML model's tier as low because operations are internal; FFIEC manual exposure and SAR-workflow integration push the regulatory factor upward regardless of customer-facing posture.
- Omitting CCAR/DFAST pedigree on a stress-eligible model; auditors and examiners catch this in the cross-walk.
- Tiering a sponsor-bank-fintech AI use case as if the bank's exposure were limited to vendor risk; the bank inherits model risk wholesale under the June 2023 interagency guidance and the July 2024 joint statement.
- Underweighting the OCC Heightened Standards bank's risk-appetite-statement linkage; tier-1 models in scope of the appetite statement carry board-level reach.

## capital-markets

### Capital markets sector overlay for ai-risk-tiering

When the scope record names sector `capital-markets`, this overlay tells the tier rubric what is adviser-, broker-dealer-, and fund-specific. Tier names and cutoffs are firm policy; this overlay names which factors elevate, which gates trigger by default, and which re-tiering events to name.

Loaded by: `ai-risk-tiering/SKILL.md` when `scope.sector_overlay_set` includes `capital-markets`. Source content derived from the capital-markets lead's overlay snippets, mapped here into the tiering context. Cited and section-referenced anchors live in `references/source-anchors.md`.

#### Source basis

- The bank model-risk anchor (the joint interagency Revised Guidance on Model Risk Management, OCC 2026-13 / FRB SR 26-2 / FDIC FIL-15-2026; supersedes SR 11-7) reach is partial for non-bank registrants (advisers and BDs that are not part of a BHC); the rubric falls back on NIST AI RMF and ISO/IEC 42001 as the primary anchor and reaches the bank bulletin only where the parent BHC inherits the model risk through a banking subsidiary, and only for traditional non-generative models (the bulletin excludes GenAI and agentic AI per footnote 3).
- SEC Investment Advisers Act Rule 206(4)-7 (compliance program) and Rule 206(4)-1 (Marketing Rule).
- FINRA Rule 3110 (supervisory system); FINRA Rule 5310 (best execution); SEC Reg BI for BDs.
- SEC Rule 15c3-5 (Market Access Rule) for execution algos and order-routing models.
- SEC Investment Adviser Books-and-Records Rule 204-2 and BD Rules 17a-3 / 17a-4.
- Investment Company Act Rule 38a-1 for fund context, including sub-adviser oversight under §38a-1(a)(4).
- SEC proposed rules on conflicts of interest in the use of predictive data analytics (proposed July 2023) [verify current state — proposal, withdrawal, or further action].
- SEC Division of Examinations risk alerts on AI / predictive analytics in adviser practices [verify current state and exact reference].

#### Capital-markets tier criteria

The tier rubric's regulatory and conduct factors absorb capital-markets-specific elevation factors. The use-case categories below are the most-frequent shapes; tier values remain firm policy.

##### Execution algorithms and order-routing models

- The model directs or influences routing, order-placement, or order-handling decisions; SEC Rule 15c3-5 controls are operative and the regulatory factor scores high.
- Market integrity exposure (FINRA Rule 5310 best execution; spoofing, layering, and other market-abuse surfaces) elevates the conduct factor.
- For the largest BDs, the model risk pedigree feeds into the firm's market-access controls; the tier decision flags Rule 15c3-5 control overlap as a triggered gate.
- Default tier elevation: tier-1 or tier-2 in firm-policy-typical mappings.

##### Surveillance models (insider trading, market manipulation, layering, spoofing)

- The model triages or scores potentially unlawful conduct; FINRA Rule 3110 supervisory expectations apply.
- False-negative cost is doctrinally distinct from false-positive cost (missed surveillance hit vs analyst time); the tier decision names both as monitoring metrics.
- Default tier elevation: tier-2 in firm-policy-typical mappings, with conduct factor high.

##### AI in marketing materials and client communications

- For investment advisers, Rule 206(4)-1 (Marketing Rule) reaches AI-generated client communications, AI-generated hypothetical performance, and AI-generated testimonials/endorsements.
- The tier decision flags Marketing Rule reach when output reaches clients or prospective clients; required disclosures are a triggered control gate.
- Books-and-records reach under Rule 204-2 (advisers) or Rule 17a-3 / 17a-4 (BDs) applies to AI-generated content supporting recommendations.
- Default tier elevation: tier-2 in firm-policy-typical mappings; tier-1 if the AI is unreviewed before client receipt.

##### Research summarisation and analyst-facing GenAI

- Where the use case is internal-only and ingests public material, tier holds at tier-3 by default; Marketing Rule reach is the dominant re-tiering trigger.
- Reg AC research independence and MAR-adjacency apply where forward-looking content is generated; conduct factor scores at minimum medium.
- Books-and-records reach applies to AI-generated content that supports an analyst recommendation.
- Default tier: tier-3, elevating to tier-2 if any client-facing path opens or scope expands to non-public material.

##### Sub-adviser-operated AI and fund-board reporting

- Where the model is operated by a sub-adviser on the registrant's funds, sub-adviser oversight under 38a-1(a)(4) applies.
- Fund-board reporting posture is a triggered gate; the fund's CCO is an audience.
- Default tier elevation: at least tier-2 when the model touches fund operations, fund-board materials, or fund-side recommendations.

##### Reg BI care obligation

- For BDs, where the AI surfaces a recommendation to a retail customer, Reg BI's care obligation applies; the tier decision flags the care-analysis documentation as a triggered control gate.
- Default tier elevation: tier-1 or tier-2 depending on the directness of the AI's role in the recommendation.

#### Cross-cutting tier modifiers

- **EU client base**: AIFMD / MiFID II overlay extends; the AI Act overlap factor flags Article 6 / Annex III routing to `ai-act-triage`.
- **Predictive-analytics rulemaking**: where the SEC proposal is in non-final state, the tier records the firm's monitoring posture rather than asserting compliance with a non-final rule. A re-tiering trigger fires on SEC final action.
- **Books-and-records reach**: any model whose output supports a recommendation or trading decision elevates the regulatory factor on books-and-records grounds; the tier records the firm's books-and-records system of record for AI-generated content (a frequent gap in GenAI use cases).

#### Capital-markets-specific tier-elevation factors

In addition to the capability rubric:

- Market access AI (Rule 15c3-5 controls) → regulatory factor high.
- Marketing Rule reach (Rule 206(4)-1) → conduct factor at minimum medium; high if disclosures are not operationalised.
- Sub-adviser-operated AI on registrant's funds → fund-board reporting posture as a triggered gate; CCO audience.
- Reg BI care obligation (BDs) → conduct factor high when AI surfaces recommendations to retail customers.
- Books-and-records preservation gap on GenAI output → regulatory factor elevated; control gate triggered.

#### Capital-markets-specific re-tiering triggers

Add to the re-tiering trigger block for capital-markets sector use cases:

- Output reaches a client-facing surface for the first time (research note published, client letter, marketing material, RFP response). Owner: research compliance with CCO. Detection: change-management notice and quarterly Marketing Rule reach review.
- Sub-adviser scope change (new sub-adviser added, AI capability extended). Owner: fund administration. Detection: 38a-1(a)(4) oversight cycle.
- SEC final action on the predictive-data-analytics rulemaking (where in scope). Owner: regulatory change function. Detection: regulatory horizon scan.
- Annual Rule 206(4)-7 review where scope or risk profile has materially changed. Owner: CCO. Detection: annual review calendar.
- New Annex III overlap surfaces (EU client base added, cross-border activity triggers MiFID II reach). Owner: regulatory change function. Detection: business expansion notice and regulatory horizon scan.

#### Common pitfalls in capital-markets tiering

- Importing SR 11-7 vocabulary into an adviser/BD tier decision without confirming SR 11-7 reach; it does not directly apply to non-bank registrants.
- Omitting books-and-records reach for AI-generated client content; Rule 204-2 catches the firm at exam time and the tier should reflect that exposure now.
- Treating the SEC predictive-analytics proposal as binding when it is currently in non-final state; the tier records monitoring posture, not assumed compliance.
- Missing Marketing Rule reach on an AI tool that drafts investment-letter content or RFP responses; advisor-side AI is the high-frequency gap.
- Forgetting fund-board reporting posture for sub-adviser-operated AI on the registrant's funds; sub-adviser oversight under §38a-1(a)(4) is the gate that audits will probe.
- Treating execution-algo Rule 15c3-5 controls as engineering controls rather than tier-decision controls; market access controls are governance controls and the tier elevation has to reflect them.

## insurance

### Insurance sector overlay for ai-risk-tiering

When the scope record names sector `insurance`, this overlay tells the tier rubric what is insurance-specific and which named bulletins set the bar. Tier names and cutoffs are firm policy; this overlay names which factors elevate, which gates trigger by default, and which re-tiering events to name.

Loaded by: `ai-risk-tiering/SKILL.md` when `scope.sector_overlay_set` includes `insurance`. Cited and section-referenced anchors live in `references/source-anchors.md`.

#### Source basis

- NAIC Bulletin on the Use of Artificial Intelligence Systems by Insurers (December 2023) is the spine. The Bulletin frames a graduated expectation: greater oversight where AI affects consumers in eligibility, premium, claims, or coverage; lighter touch where the use case is back-office. The tier rubric reads "potential to harm consumers" as the test that drives elevation, not a bolt-on label.
- Colorado Division of Insurance regulation implementing SB 21-169 (life-underwriting AI / ECDIS) [verify regulation number].
- New York DFS Insurance Circular Letter on AI and ECDIS in life-insurance underwriting (January 2024).
- California DOI bulletin on AI use in insurance.
- NAIC Unfair Trade Practices Act (Model #880) for unfair-claims-settlement and unfair-discrimination framing in claims AI.
- NAIC ORSA (Model #505) for enterprise materiality.
- HIPAA Privacy and Security Rules where PHI is in the data flow.

#### Insurance-specific tier criteria

The insurance use-case categories fall into a graduated structure that the tier rubric absorbs. The categories are anchored to the NAIC Bulletin; tier values remain firm policy.

##### Accelerated underwriting AI (life and health)

- The use case influences eligibility, rating class, premium, or coverage in life or health. Customer-binding by definition.
- ECDIS likely in the input set; CO regulation and NY DFS Circular Letter elevate the regulatory factor when the operating footprint includes those states.
- HIPAA touch is frequent (prescription history, medical underwriting data); privacy factor elevates.
- AIS Program element-by-element coverage demanded under the NAIC Bulletin; documentation factor reads as primary.
- Default tier elevation: tier-1 in firm-policy-typical mappings; gates include full validation, AIS Program element status, ECDIS-provenance review, state-DOI-strictest disclosure posture.

##### Claims AI (FNOL triage, severity prediction, fraud-indicator scoring, claims chatbot)

- The use case affects claim acceptance, denial, severity, or fraud-indicator routing. Customer-binding for any decision that touches claim outcome.
- NAIC Model #880 unfair-claims-settlement standards apply regardless of decision technology; conduct factor elevates.
- State unfair-claims-settlement-practices acts set timing, notice, and reasoned-denial requirements; regulatory factor elevates.
- HIPAA touch is frequent (health and life claims); privacy factor elevates.
- Where the AI is consumer-facing (claims chatbot), UPL and producer-licensing boundaries matter and the conduct factor scores at minimum medium.
- Default tier elevation: tier-1 or tier-2 in firm-policy-typical mappings depending on autonomy and customer-facing posture; gates include claim-handling control family review against Model #880 and state UCSPA.

##### Marketing AI to existing policyholders

- The use case touches product targeting, replacement-risk scenarios, or annuity suitability.
- NAIC Model #275 [verify model number] for annuity suitability, where in scope, elevates the conduct factor.
- TCPA / Do-Not-Call where outbound communications are involved.
- Default tier elevation: tier-2 in firm-policy-typical mappings when annuity suitability is implicated; tier-3 otherwise.

##### Pricing / rating ML factors

- State DOI rate-filing and prior-approval regimes apply where the model touches filed rates; the regulatory factor elevates and the rate analyst is a downstream audience.
- Unfair-discrimination test under Model #880 applies; the fairness vocabulary differs from ECOA / Reg B disparate-impact framing.
- Default tier elevation: tier-1 or tier-2 depending on filed-rate reach and state footprint.

##### Agent-AI co-pilots (producer-AI tools)

- Suitability and best-interest standards apply; the human-in-the-loop control must be designed against those standards rather than against generic AI fairness.
- Default tier elevation: tier-2 in firm-policy-typical mappings when the co-pilot influences suitability or best-interest analysis.

##### Back-office AI (call-centre summarisation, mailroom OCR)

- No customer-facing decision; no rate or claim impact; no PHI unless flagged.
- Default tier: tier-3 or tier-4. AIS Program documentation expectations remain (proportional).

#### Cross-cutting tier modifiers

- **State DOI bulletin in operating footprint**: the presence of a state DOI bulletin on AI in insurance in the operating footprint raises the disclosure and governance demands of the tier (not necessarily the inherent risk). The strictest applicable state sets the floor.
- **ORSA materiality**: any AI use case meeting the carrier's ORSA materiality threshold under Model #505 lands in the top tier for governance purposes regardless of the rubric's other dimensions.
- **HIPAA touch**: any insurance AI use case that processes PHI gets a privacy-flag tier modifier; the privacy cross-cutting overlay carries the data-sensitivity scoring.
- **Vendor-supplied AI**: per NAIC Bulletin December 2023 third-party AI accountability, vendor-supplied AI used on the carrier's policies elevates the vendor-dependence factor and pulls AIS Program third-party-AI element coverage into triggered gates.
- **TPA / claims-administrator operation**: where the AI runs at a TPA on the carrier's policies, NAIC Insurance Data Security Model Law (Model #668) §4.F third-party service-provider obligations apply. The tier decision names the TPA's controls as the carrier's controls for §4.F purposes.

#### Worked tier-criterion table (illustrative, firm policy governs)

| Use case category | Default tier | Dominant factor elevation | Default triggered gates |
|---|---|---|---|
| Accelerated underwriting (life/health, ECDIS) | tier-1 | customer_impact, conduct, data_sensitivity (PHI), regulatory (CO/NY) | Full validation; AIS Program coverage; ECDIS provenance; state-DOI strictest-applicable disclosure |
| Claims AI (decisioning) | tier-1 or tier-2 | customer_impact, conduct (Model #880), data_sensitivity (PHI) | Claim-handling control review; Model #880 UCSPA controls; HIPAA controls; UPL boundary check on chatbots |
| Pricing / rating ML | tier-1 or tier-2 | regulatory (state rate filing), conduct (#880 unfair discrimination) | Rate-filing alignment; unfair-discrimination test; state DOI exam-prep posture |
| Marketing AI (annuity/suitability) | tier-2 | conduct (#275 suitability), regulatory (TCPA) | Suitability control review; outbound communications controls |
| Agent-AI co-pilots | tier-2 | conduct (suitability / best-interest) | Human-in-the-loop control design against suitability standards |
| Back-office AI (OCR, summarisation) | tier-3 or tier-4 | none dominant | AIS Program proportional documentation |

#### Insurance-specific re-tiering triggers

Add to the re-tiering trigger block for insurance sector use cases:

- State DOI bulletin adoption or amendment in the operating footprint (CO, NY, CA, others). Owner: regulatory change function with insurance compliance. Detection: regulatory horizon scan.
- ORSA materiality reassessment. Owner: ORSA function. Detection: annual ORSA review or material business change.
- ECDIS source addition or substitution. Owner: data governance with insurance compliance. Detection: change-management notice.
- HIPAA BAA posture change with a vendor handling PHI. Owner: vendor management with privacy office. Detection: vendor contract management.
- TPA AI scope change on the carrier's policies. Owner: outsourcing governance. Detection: TPA contract change-control.

#### Common pitfalls in insurance tiering

- Treating the NAIC Bulletin as US-uniform; adoption is state-by-state and the Bulletin is itself non-binding until state adoption.
- Importing ECOA / Reg B fairness vocabulary without translating to Model #880 unfair-discrimination framing; the test is different and a state DOI rate analyst will read the wrong artefact.
- Tiering claims AI low because the chatbot "just answers questions"; Model #880 fair-claims-settlement standards apply regardless of who or what produces the claim decision, and an unmonitored chatbot is a control gap not a low-tier feature.
- Missing HIPAA touch on a life-underwriting AI using prescription-history data; the privacy factor stays low when it should be high.
- Forgetting that the TPA's controls are the carrier's controls under Model #668 §4.F; tiering the use case as if the TPA's posture absolves the carrier.
- Treating the AIS Program elements as a checklist rather than a structure; the tier decision evidences each element with source-trace pointers, not just a tick.

## payments-fintech

### Payments and fintech sector overlay for ai-risk-tiering

When the scope record names sector `payments-fintech`, this overlay tells the tier rubric what is rail-, sponsor-bank-, and money-transmitter-specific. Tier names and cutoffs are firm policy; this overlay names which factors elevate, which gates trigger by default, and which re-tiering events to name.

Loaded by: `ai-risk-tiering/SKILL.md` when `scope.sector_overlay_set` includes `payments-fintech`, or when the institution type implicates a money transmitter, payments processor, fintech program, sponsor-bank arrangement, BIN sponsor, prepaid issuer, or non-bank consumer-finance entity.

Source content derived from the payments-fintech lead's overlay snippets, mapped here into the tiering context. Cited and section-referenced anchors live in `references/source-anchors.md`.

#### Source basis

- OCC Bulletin 2023-17 / FRB SR 23-4 / FDIC FIL-29-2023 (Interagency Guidance on Third-Party Relationships, June 6, 2023) for sponsor-bank programs.
- OCC / FRB / FDIC Joint Statement on Bank-Fintech Arrangements (July 25, 2024) [verify date and title] as the operative document for sponsor-bank deposit programs.
- FFIEC BSA/AML Examination Manual for transaction monitoring, sanctions screening, customer risk rating.
- FinCEN MSB rules at 31 CFR Part 1022 where the operator is itself a money transmitter.
- NACHA Operating Rules (current edition) Third-Party Sender registration and risk-management rules [verify rule citations].
- Reg E (12 CFR Part 1005), Reg DD (12 CFR Part 1030); CFPB UDAAP authority under Dodd-Frank Title X.
- NYDFS 23 NYCRR Part 504 (transaction monitoring) and Part 500 (cyber) for NY-licensed entities.
- CFPB Larger-Participant Rule for Digital Wallets and Payment Apps (December 2024) [verify Federal Register citation, effective date, and current state].

#### Payments and fintech tier criteria

The use-case categories below are the most-frequent shapes; tier values remain firm policy.

##### Onboarding-decisioning AI (KYC scoring, account-opening risk, identity-verification scoring)

- The model triages or scores onboarding outcomes; CIP and KYC integration is a downstream control, not a tier-down feature.
- Adverse-decisioning posture for ECOA reach where the onboarding implicates credit (card programs); for deposit-only programs, ECOA may not reach but UDAAP does.
- Default tier elevation: tier-1 or tier-2 for credit-implicating onboarding; tier-2 for deposit-only with UDAAP reach.

##### Transaction-monitoring (TM) AI for AML/BSA

- The model triages or scores potentially suspicious activity; FFIEC manual exposure is operative; BSA officer or designee is a named approver.
- For NYDFS Part 504 covered entities, the senior-officer certification posture elevates the regulatory factor.
- For state-licensed money transmitters, state TM-program expectations layer on top of FFIEC manual.
- Default tier elevation: tier-1 for any TM model in scope; tier-2 minimum even where the rule reach is debated.

##### Sanctions-screening AI

- OFAC compliance program structure is operative; corridor-by-corridor screening posture, fuzzy-matching threshold setting, and false-positive disposition QA are tier-side controls.
- Cross-border payments and correspondent flows elevate the regulatory factor; virtual-currency exposure layers FinCEN guidance on top.
- Default tier elevation: tier-1 in firm-policy-typical mappings.

##### Fraud and ATO detection AI

- The model decides or scores fraud holds, declines, and step-up authentication.
- Reg E reach for unauthorised consumer transactions; the tier flags the consumer-recourse channel for false declines as a triggered control gate.
- For card programs, network rules apply in addition to regulatory expectations.
- Default tier elevation: tier-1 or tier-2 depending on autonomy and customer-impact directness.

##### Consumer-facing GenAI (chatbots, support agents, dispute intake)

- The model interacts with customers in service, dispute, or sales surfaces; UDAAP reach is operative for any interaction that could be deceptive, unfair, or abusive.
- Reg E error-resolution timing applies if the bot intakes claims; the 10 / 45 / 90-day clock does not stop because intake is automated.
- Account-closure and account-hold themes (CFPB's most-frequent fintech UDAAP enforcement theme) elevate the conduct factor when the bot can effect or confirm account actions.
- Default tier elevation: tier-1 if the bot can take account-affecting actions; tier-2 advisory-only.

##### Underwriting and pricing AI for non-bank consumer finance

- Where the use case influences credit-limit, APR, or approval/decline decisions outside a sponsor-bank context, the consumer-protection authority sits with the CFPB plus state regulators.
- ECOA / Reg B applies to the credit decision; Reg B §1002.9 and Comment 9(b)(2)-3 read directly on the adverse-action notice (CFPB Circulars 2022-03 / 2023-03 **withdrawn May 12, 2025; historical only**); conduct factor scores high.
- Default tier elevation: tier-1.

#### Cross-cutting tier modifiers

- **Sponsor-bank arrangement**: where the AI sits in the program operator's stack but the regulated activity sits at the sponsor bank, the tier decision names the sponsor bank's federal banking regulator and the bank-side committee path. Vendor-dependence and concentration factors elevate. The bank-fintech contract allocates model-risk responsibility but the bank inherits the model risk under the June 2023 interagency guidance.
- **State money-transmitter footprint**: state-by-state MTL exam expectations elevate the regulatory factor; the strictest state in the footprint sets the floor for licensure-tied gates.
- **NYDFS Part 504 covered entity**: senior-officer certification posture for TM models is a triggered gate; the regulatory factor scores high for any TM, sanctions-screening, or KYC use case.
- **CFPB larger-participant rule for digital consumer payment applications** (12 CFR Part 1090, finalized November 21, 2024) — verify current operative status on the engagement date (CFPB has been reconsidering and litigating multiple late-2024 final rules); where in scope and operative, the entity is under direct CFPB supervisory authority and the regulatory factor elevates for any consumer-facing AI.
- **Concentration risk on sponsor-bank, processor, BIN sponsor**: three distinct concentration axes; each fails differently. The concentration factor scores against the dominant axis for the use case.
- **Faster-payments rails (FedNow, RTP, Same Day ACH inbound)**: irrevocability shifts the fraud-control playbook; the conduct factor reads against request-for-return-of-funds dynamics rather than chargeback paths.

#### Payments-fintech-specific tier-elevation factors

In addition to the capability rubric:

- Sponsor-bank arrangement → vendor-dependence and concentration factors elevate; bank-side committee path named.
- TM, sanctions-screening, or KYC use case → regulatory factor high (FFIEC manual exposure named); BSA officer signoff as triggered gate.
- NYDFS Part 504 senior-officer certification posture → regulatory factor high.
- CFPB Larger-Participant Rule in scope → regulatory factor elevated for consumer-facing AI.
- Reg E reach on consumer-facing AI that intakes claims or affects transactions → conduct factor at minimum medium.
- FDIC misrepresentation rule (12 CFR Part 328 Subpart B; **2023 final rule with 2024-2025 effective-date extensions** — verify current effective date for the engagement): any "FDIC-insured" framing on a fintech surface elevates the conduct factor and triggers a customer-disclosure control gate.

#### Payments-fintech-specific re-tiering triggers

Add to the re-tiering trigger block for payments-fintech sector use cases:

- Sponsor-bank change (new sponsor, dual-sponsor add, sponsor exit). Owner: program operations with bank's third-party risk function. Detection: program-agreement change-control plus bank-side notification.
- Rail expansion (adding FedNow, RTP, Same Day ACH, cross-border corridor). Owner: payments operations. Detection: change-management notice.
- New state MTL or BitLicense in the operating footprint. Owner: licensing function. Detection: NMLS filing plus regulatory horizon scan.
- CFPB Larger-Participant Rule applicability change (volume threshold crossing). Owner: regulatory change function with CCO. Detection: volume monitoring plus annual self-assessment.
- NYDFS Part 504 senior-officer certification cycle. Owner: BSA officer with CCO. Detection: annual certification calendar.
- Material change in NACHA Third-Party Sender posture, Visa / Mastercard fraud-rate program escalation, or processor change. Owner: payments operations with vendor management. Detection: rule-change notice plus return-rate / fraud-rate monitoring.

#### Common pitfalls in payments-fintech tiering

- Treating the fintech as the sole owner of model risk when a sponsor-bank arrangement is operative; the bank inherits the model risk wholesale and the tier should reflect bank-side reach.
- Omitting BSA officer signoff on a TM model; FFIEC manual expectation is clear and the gate should fire at tier decision, not at validation hand-off.
- Reporting fraud-model performance as AML-effectiveness evidence; the two are doctrinally distinct and conflating them at tier-decision time hides the real exposure.
- Missing Reg E error-resolution posture on a chatbot or support-agent AI that intakes claims or confirms account actions; the 10 / 45 / 90-day clock applies regardless of who or what intakes the claim.
- Treating state money-transmission exams as a footnote; state examiners regularly review TM and onboarding models in money-transmission exams and the regulatory factor should reflect that.
- Underweighting concentration risk on sponsor-bank, processor, or BIN-sponsor axis; the three axes fail differently and a single concentration metric hides the failure mode.
- Treating "FDIC-insured" framing on a fintech surface as a marketing question; under the FDIC misrepresentation rule the framing is a regulatory-factor input and the tier should reflect the disclosure gate.
- Missing the irrevocability shift on faster-payments rails; the fraud playbook is request-for-return-of-funds plus monitoring escalation, not chargeback, and the conduct factor reads differently.
