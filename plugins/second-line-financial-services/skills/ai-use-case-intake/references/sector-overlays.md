# sector-overlays

One section per sector. Read only the sections the scope calls for.

## banking

### Banking sector overlay for ai-use-case-intake

When the scope record names sector `banking`, this overlay tells the intake what additional fields to capture, which named regulators belong on the regulatory-flags table, and which review gates are firm-policy defaults at federally regulated banks. The overlay does not invent firm taxonomy (those are firm-overlay content); it tells the intake which banking-specific facts are load-bearing for the downstream tier and pre-prod work.

Loaded by: `ai-use-case-intake/SKILL.md` when `scope.sector_overlay_set` includes `banking`, or when the institution type implicates a federal banking regulator (national bank, state member bank, savings association, BHC, FBO with US operations).

#### Source basis

Cited and section-referenced in `references/source-anchors.md`. This overlay names the regulators and sources without restating excerpts.

#### What changes for banking intake

##### 1. Model definition and inventory anchor is the joint interagency revised guidance

For federally regulated banks, the intake record is the entry the use case takes in the model inventory under the joint interagency Revised Guidance on Model Risk Management (OCC 2026-13 / FRB SR 26-2 / FDIC FIL-15-2026, supersedes SR 11-7 and SR 21-8). The bulletin expressly excludes generative AI and agentic AI from its scope (footnote 3); for GenAI use cases the intake captures the architecture fields (foundation-model identity, RAG corpora, tool inventory, autonomy posture) for the firm's broader AI inventory under NIST AI RMF Govern 1.6 / 4.x, not under the bulletin. Intake captures:

- `regulatory_flags`: `OCC_2026_13` (and the parallel FRB SR 26-2 / FDIC FIL-15-2026) for traditional models; for GenAI/agentic, `NIST_AI_RMF` and `NIST_AI_600_1` with the routing destination `ai-risk-tiering`.
- The accountable first-line owner is the model owner role under firm policy, with linkage to the firm's model risk management office.
- The lifecycle stage drives whether the inventory entry is "in development" or "in use" under the firm's MRMO state machine.

For non-bank entities under the same parent, SR 11-7 reach is by extension only when the bank inherits model risk through transactions, services, or balance-sheet exposure. Intake should not over-claim SR 11-7 reach to non-bank entities.

##### 2. ECOA / Reg B adverse-action surface

Where the AI use case influences a credit decision (origination, pricing, line management, collections triggers, fraud-driven adverse action), the intake captures:

- `regulatory_flags`: `Reg_B_1002_9` (specific principal reasons for adverse action) and `Reg_B_OSC_9_b_2_3` (cited reasons must accurately describe factors actually considered or scored) where the use case drives adverse-action notice generation. CFPB Circulars 2022-03 and 2023-03 informed prior intake postures but were **withdrawn May 12, 2025; historical only**. Routing destinations: `ai-risk-tiering` and `validation-plan`.
- `decision_impact.customer_impact`: scored high; basis names the credit-decision touch.
- `decision_impact.regulatory_impact`: scored at least medium with CFPB and prudential reach noted.
- An open question for `validation-plan`: how is the adverse-action reason generation method validated and sampled.

##### 3. CCAR / DFAST and CECL stress-testing exposure

For banks subject to stress testing (DFAST, CCAR for the largest BHCs) and for CECL methodology under ASC 326, models in scope for stress projections, allowance methodology, or capital planning carry stress-side documentation expectations on top of the model risk inventory entry. Intake captures:

- A regulatory flag for stress-eligibility with routing to `ai-risk-tiering` (most firm policies tier stress-eligible models at tier-1 by default regardless of customer-facing posture).
- A vendor dependency entry where the stress engine itself is a vendor model.
- A change-plan field capturing the annual stress-testing cycle as a re-intake trigger.

##### 4. AML, BSA, sanctions, and fraud framing

For models supporting BSA/AML transaction monitoring, sanctions screening, customer risk rating, and fraud detection, the intake captures:

- `regulatory_flags`: `FFIEC_BSA_AML` with routing to `ai-risk-tiering` and `validation-plan`. The FFIEC BSA/AML Examination Manual is the supervisory frame.
- `decision_impact.regulatory_impact`: scored at least medium with FFIEC manual exposure noted.
- `intended_users`: BSA officer or designee should appear in the user roles for any AML use case (the BSA officer is the named approver on triggered gates downstream).
- The intake distinguishes fraud-model purpose from AML-effectiveness purpose; the two are doctrinally distinct and must not be conflated in the purpose statement.

##### 5. Bank-fintech arrangements and sponsor-bank reach

For sponsor-bank programs, OCC Bulletin 2023-17 / FRB SR 23-4 / FDIC FIL-29-2023 (June 2023) and the OCC / FRB / FDIC Joint Statement on Bank-Fintech Arrangements (July 25, 2024) [verify date] are operative. Where the bank inherits AI-model risk from a fintech-supplied model:

- `vendor_dependencies`: name the sponsor-bank counterparty (fintech operator) with role `sponsor_bank` or `data_provider` as appropriate; criticality scores at least `important`.
- `regulatory_flags`: `OCC_2023_17_third_party` and `July_2024_bank_fintech` with routing to `ai-risk-tiering` and `vendor-diligence`.
- An open question for `vendor-diligence`: what is the sponsor-bank's evidence pack for the fintech-supplied AI, and how does the bank's MRMO inherit the model risk.

##### 6. CRA-relevant models

For models that influence community-development assessment, low-and-moderate-income outreach, or branch-network analytics where they touch CRA performance, intake captures the regulatory flag and a routing destination of `ai-risk-tiering`. Firm policy may add the head of community reinvestment as a named reviewer downstream.

##### 7. Heightened Standards reach

For OCC-supervised large banks subject to 12 CFR Part 30 Appendix D (Heightened Standards), intake captures:

- A regulatory flag noting Heightened Standards reach with routing to `ai-risk-tiering` and `board-ai-risk-pack`.
- A note in the change plan that any AI use case named in the firm's risk-appetite statement carries board-level reach; tier-1 models in scope of the appetite statement appear by name or by category at the board.

#### Banking-specific intake fields

In addition to the capability intake spine, the following bank-specific facts belong on the record when relevant:

- Federal regulator (OCC / FRB / FDIC) and supervisory cycle posture (any open MRA, MRIA, consent order touching the model or the business line).
- BSA officer or designee linkage where the use case touches BSA/AML.
- Sponsor-bank arrangement counterparty where applicable.
- Stress-testing pedigree where the model is stress-eligible.
- Risk-appetite-statement linkage where the use case appears by name or category.

#### Common pitfalls in banking intake

- Treating CFPB authority as out of scope because the entity is OCC- or FRB-supervised. CFPB consumer-protection authority reaches large banks for ECOA, RESPA, EFTA, and UDAAP purposes.
- Recording an AML model as "internal use only" with a low decision-impact score; the FFIEC manual exposure and SAR-workflow integration push the regulatory dimension up regardless of customer-facing posture.
- Missing the sponsor-bank reach when the AI runs at the fintech program operator. The bank inherits model risk wholesale under the June 2023 interagency guidance and the July 2024 joint statement.
- Recording a stress-eligible model without flagging the stress-testing pedigree. Auditors and examiners catch this in the cross-walk.
- Underweighting the Heightened Standards bank's risk-appetite-statement linkage; tier-1 models in scope of the appetite statement carry board-level reach.

## capital-markets

### Capital-markets sector overlay for ai-use-case-intake

When the scope record names sector `capital-markets`, this overlay tells the intake what additional fields to capture, which named regulators belong on the regulatory-flags table, and which open questions tag to downstream adviser/BD/fund AI work. The reach is SEC, FINRA, and state-IA; capability-plugin defaults built around bank prudential supervision miss the registration-class lens this sector reads through.

Loaded by: `ai-use-case-intake/SKILL.md` when `scope.sector_overlay_set` includes `capital-markets`, or when the institution type is an investment adviser, broker-dealer, dual-registrant, mutual fund / ETF, hedge fund, private equity adviser, or other SEC/FINRA registrant.

#### Source basis

Cited and section-referenced in `references/source-anchors.md`. This overlay names the regulators and sources without restating excerpts.

#### What changes for capital-markets intake

##### 1. Registration-class lens

The intake purpose statement and intended-users block read against the registration class. Adviser, BD, dual-registrant, fund, and sub-adviser configurations carry different rule-set reach:

- Adviser: Investment Advisers Act §206 antifraud, Rule 206(4)-7 compliance program, Rule 206(4)-1 Marketing Rule, Rule 204-2 books-and-records.
- BD: Securities Exchange Act and FINRA rules, Reg BI care obligation where retail customers are involved, FINRA 3110 supervision, FINRA 4511 books-and-records, Exchange Act Rules 17a-3 / 17a-4.
- Dual-registrant: both rule sets apply; intake should record the registration class for the use case in scope.
- Fund: Investment Company Act, Rule 38a-1 fund compliance program, sub-adviser delegation considerations, fund-board reporting posture.
- Sub-adviser: 38a-1(a)(4) compliance program coverage by the fund's CCO, sub-adviser disclosure to the fund adviser and board.

##### 2. Marketing Rule reach (Rule 206(4)-1)

Where AI output reaches client-facing material — research notes, RFP responses, client letters, marketing claims, AI-generated performance presentations, AI-generated testimonials, AI-personalised marketing — the Marketing Rule applies:

- `regulatory_flags`: `SEC_Marketing_Rule` with routing to `ai-risk-tiering`, `model-card-builder`, `validation-plan`. The basis names the client-facing path.
- An open question for `validation-plan`: how is hypothetical-performance content (where AI generates forward-looking output) controlled against Rule 206(4)-1(d)(6).
- An open question for `model-card-builder`: what is the testimonial/endorsement disclosure posture if AI-generated content includes client-experience claims.

##### 3. Books-and-records reach (Rule 204-2; Rules 17a-3 and 17a-4)

Where AI output supports a recommendation or decision (research summaries, suitability analyses, trade rationales, communications), books-and-records preservation applies:

- `regulatory_flags`: `SEC_204_2_books_records` (advisers) or the BD equivalent (`SEC_17a_3_4_books_records`) with routing to `ai-risk-tiering` and `model-card-builder`.
- An open question for `model-card-builder`: how is AI-generated content captured into the books-and-records system, and what is the preservation format.

##### 4. Reg BI care obligation (BDs serving retail customers)

Where the AI surfaces recommendations to retail customers (or to BD reps who then surface them), Reg BI care obligation applies on top of FINRA suitability:

- `regulatory_flags`: `Reg_BI` with routing to `validation-plan`.
- An open question for `validation-plan`: how does the BD document the care analysis for an AI-recommended product, and how is the analysis sampled.

##### 5. Research-integrity and conduct adjacency

Where the use case is research summarisation, research drafting, or anything adjacent to the firm's research function:

- Reg AC research-analyst certification reach if the AI output is incorporated into a published research note.
- MAR (Market Abuse Regulation) adjacency where the firm operates in the EU and the output could be construed as forward-looking research.
- An open question for `model-card-builder`: what is the analyst review point between AI summary and any incorporation into a research note.

##### 6. SEC Division of Examinations focus on AI / predictive analytics

SEC EXAMS has flagged AI/predictive analytics in adviser practices in recent risk alerts [verify current state and exact reference]. Intake captures:

- A regulatory flag noting EXAMS focus area with routing to `ai-risk-tiering`.
- An open question for downstream work: is the use case in scope for the SEC's proposed conflicts-of-interest rule on predictive data analytics (proposed July 26, 2023) [verify current state — proposal, withdrawal, or further action].

##### 7. Sub-adviser AI disclosure

Where the firm uses sub-adviser AI on fund assets, the fund adviser carries 38a-1 oversight responsibility:

- `vendor_dependencies`: sub-adviser as a vendor with role `model_serving_infrastructure` or `data_provider` as appropriate.
- An open question for `vendor-diligence`: what is the fund adviser's evidence pack for the sub-adviser AI, and how is sub-adviser AI use disclosed to the fund board.

##### 8. AI use in fund-board materials

Where AI is used in 38a-1 materials, 15(c) materials, or fund-board agendas:

- An open question for `model-card-builder`: what is the CCO review posture for AI-drafted board materials.

#### Capital-markets-specific intake fields

In addition to the capability intake spine, the following capital-markets-specific facts belong on the record when relevant:

- Registration class for the use case (adviser, BD, dual-registrant, fund, sub-adviser).
- Client-facing path (whether AI output reaches client-facing material directly, through a representative, or not at all).
- Books-and-records preservation posture.
- Sub-adviser delegation if applicable.
- Fund-board reporting posture if applicable.
- EU footprint where MAR / MiFID II reach is in question.

#### Common pitfalls in capital-markets intake

- Treating an "internal-use" research-summarisation AI as low-impact; if the output is incorporated into a published research note or supports a recommendation, Marketing Rule and books-and-records reach.
- Missing the sub-adviser AI dependency when the fund adviser intakes its own use case; the sub-adviser AI is the fund adviser's responsibility under 38a-1.
- Recording a BD's AI use case without the Reg BI care obligation flag where the AI surfaces recommendations to retail customers.
- Treating Reg AC and MAR adjacency as out of scope on a research summariser; the boundary moves quickly when output crosses into forward-looking content or non-public material.
- Skipping the EU footprint check on advisers serving EU clients (EU AI Act extraterritorial reach plus MiFID II overlap can land high-risk obligations on US-based advisers).

## insurance

### Insurance sector overlay for ai-use-case-intake

When the scope record names sector `insurance`, this overlay tells the intake what additional fields to capture, which named regulators belong on the regulatory-flags table, and which open questions tag to downstream insurance work. The carrier remains accountable for vendor and third-party AI used on its policies (NAIC Model Bulletin December 2023 third-party AI accountability); the intake captures the fields that accountability flows from.

Loaded by: `ai-use-case-intake/SKILL.md` when `scope.sector_overlay_set` includes `insurance`, or when the institution type is an insurer (carrier, reinsurer, MGA, MGU, captive) or insurance group.

#### Source basis

Cited and section-referenced in `references/source-anchors.md`. This overlay names the regulators and sources without restating excerpts.

#### What changes for insurance intake

##### 1. NAIC Bulletin on Use of AI Systems by Insurers (December 2023) — AIS Program spine

For insurers, the intake feeds the AIS Program (governance, risk management, testing, validation, third-party AI accountability, monitoring, documentation, transparency, fairness). Intake captures:

- `regulatory_flags`: `NAIC_Bulletin_AI_2023` with routing to `ai-risk-tiering`, `model-card-builder`, `validation-plan`. Note the state-by-state adoption status (the NAIC AI Working Group adoption tracker is the public reference for which states have adopted) in the basis line; the Bulletin is binding only where adopted.
- `decision_impact.customer_impact`: scored against the Bulletin's spine of "potential to harm consumers" — eligibility, premium, claims, coverage decisions read high; back-office reads lower.
- An open question for `model-card-builder`: which AIS Program elements need explicit coverage in the card.

##### 2. Insurance use case categories the intake must explicitly recognise

Insurance AI clusters into categories with different regulatory weights. The intake purpose statement should name the category:

- Accelerated underwriting (life and health) — state DOI bulletin reach (CO SB 21-169, NY DFS Insurance Circular Letter January 2024, CA bulletin), HIPAA touch on health data, ECDIS provenance question.
- Claims AI (triage, FNOL, severity prediction, fraud-indicator scoring, claims-handling chatbots) — NAIC Model #880 fair-claims-settlement standards, state UCSPA reach, HIPAA touch on health-claims, UPL boundary on consumer-facing chatbots.
- Pricing / rating ML factors and ECDIS use — state DOI rate-filing reach, prohibited rating factor exposure, NAIC Model #880 unfair discrimination.
- Marketing AI for product targeting — TCPA reach where outbound communications, NAIC #275 [verify] suitability where annuities involved.
- Agent-facing AI (illustration generation, suitability triage) — producer-licensing question on consumer-facing actions, NAIC Suitability in Annuity Transactions Model Regulation [verify model number].
- Back-office AI (call-center summarisation, mailroom OCR, claims-letter drafting) — generally lower regulatory weight, but still in scope for the AIS Program if the insurer has adopted it.

##### 3. State DOI bulletins on AI use

Each state-bulletin reach is a separate flag because each state has its own scoping (life-only in CO and NY DFS Circular; broader in NAIC Bulletin and CA bulletin) and consumer-recourse expectations:

- `regulatory_flags`: `CO_SB_21_169` (life-insurance underwriting using ECDIS or predictive models in CO), `NY_DFS_Circular_AI_2024` (life-insurance underwriting and pricing using AI and ECDIS in NY), CA bulletin where applicable. Routing to `ai-risk-tiering` and `model-card-builder`.
- The intake captures the operating footprint by state and lights up the bulletin flag where the use case is in the state's scope.

##### 4. ECDIS data source provenance

Where the use case uses External Consumer Data and Information Sources (e.g., third-party clinical and prescription data, credit-related data outside FCRA, behavioural data), intake captures:

- `data_sources`: each ECDIS source named with provenance, lawful basis, and consumer-recourse channel.
- An open question for `model-card-builder` and `validation-plan`: ECDIS provenance evidence pack and bias-evaluation evidence framed against unfair discrimination (Model #880) terminology in addition to or in place of generic fairness terminology.

##### 5. HIPAA touch on health data

Any insurance AI touching PHI (health-claims AI; life-and-health underwriting AI using prescription-history or medical data) requires a HIPAA cross-check:

- `data_sources`: PHI sources tagged `regulated_phi` with field-level tagging (medical history, prescription history, claims diagnoses) required.
- `regulatory_flags`: `HIPAA` with routing to `ai-risk-tiering` and `validation-plan`.
- Vendor BAA posture as a vendor-dependency note where any vendor handles PHI.

##### 6. ORSA materiality

If the AI use case is enterprise-material under the carrier's ORSA materiality threshold, the use case belongs in the ORSA Summary Report under Model #505. Intake captures:

- An open question for `board-ai-risk-pack` (and a flag in the change plan): does the use case meet the firm's ORSA materiality threshold; if so, the use case feeds the ORSA Summary Report.

##### 7. Producer licensing on consumer-facing actions

Any consumer-facing AI that takes actions on policies (binding, quoting commitments, surrendering, paying claims, agent-AI co-pilots that recommend) can trigger producer-licensing questions:

- An open question for the licensing function: does the use case cross into producer activity without licensing.
- Where the use case is consumer-facing claims AI, an additional UPL boundary check (does the chatbot cross into legal advice or coverage opinions).

##### 8. Vendor-AI accountability

NAIC Bulletin December 2023 holds the carrier accountable for vendor and third-party AI used on its policies. Intake captures:

- `vendor_dependencies`: each AI vendor named with role and criticality, with the AIS Program third-party-AI elements as routing notes for `vendor-diligence`.
- A regulatory flag for `NAIC_Bulletin_AI_2023` third-party AI accountability with routing to `vendor-diligence`.

#### Insurance-specific intake fields

In addition to the capability intake spine, the following insurance-specific facts belong on the record when relevant:

- Operating footprint by state (which DOI bulletins are in scope).
- AIS Program element coverage status (governance, risk management, testing, validation, third-party AI accountability, monitoring, documentation, transparency, fairness).
- ORSA-materiality posture.
- TPA / claims-administrator role where the AI runs at a TPA on the carrier's policies (NAIC Insurance Data Security Model Law #668 §4.F third-party service-provider obligations apply; the TPA's controls are the carrier's controls for §4.F purposes).
- HIPAA touch and BAA posture.
- ECDIS provenance for any data input the AI uses.

#### Common pitfalls in insurance intake

- Treating the NAIC Bulletin as US-uniform when it is state-by-state in adoption.
- Recording an underwriting-AI use case with "fairness" framing only; insurance regulators use unfair discrimination under Model #880, which has a different test (actuarial justification matters; permitted vs prohibited rating factors are state-defined).
- Missing the ECDIS provenance question on a use case using third-party data inputs; CO and NY DFS Circular both turn on ECDIS-specific governance.
- Treating a TPA's AI as out-of-scope because the TPA runs it; the carrier remains accountable under the NAIC Bulletin and the Model #668 third-party service-provider obligations.
- Skipping the HIPAA flag on a life-underwriting AI that uses prescription-history data; the data category triggers the rule regardless of whether the carrier considers itself in the health business.
- Recording a consumer-facing claims chatbot as low decision-impact on the basis of "the human reviews the denial letter." Where the bot crosses into legal advice or coverage opinions, the UPL question is open and the decision-impact reads higher than the human-review point suggests.

## payments-fintech

### Payments-fintech sector overlay for ai-use-case-intake

When the scope record names sector `payments-fintech`, this overlay tells the intake what additional fields to capture, which named regulators belong on the regulatory-flags table, and which sponsor-bank and money-transmitter facts are load-bearing. Payments-fintech intakes break differently from bank intakes: the program operator may not be the supervised entity, but the AI runs in the program operator's stack, and both the operator and the sponsor bank carry the consequences.

Loaded by: `ai-use-case-intake/SKILL.md` when `scope.sector_overlay_set` includes `payments-fintech`, or when the institution type is a fintech program operator, BaaS platform, money transmitter, MSB, processor, BIN sponsor, or sponsor bank reviewing a fintech-supplied AI use case.

#### Source basis

Cited and section-referenced in `references/source-anchors.md`. This overlay names the regulators and sources without restating excerpts.

#### What changes for payments-fintech intake

##### 1. Sponsor-bank arrangement is the dominant intake pattern

Most fintech AI use cases run inside a sponsor-bank program. The intake captures both sides:

- `vendor_dependencies`: sponsor bank named with role `sponsor_bank` and criticality `critical`. Where a BIN sponsor is separate, named separately.
- `regulatory_flags`: `OCC_2023_17_third_party` and `July_2024_bank_fintech` with routing to `ai-risk-tiering` and `vendor-diligence`. The basis names which side the firm is on (program operator or sponsor bank).
- An open question for `vendor-diligence`: the program operator's evidence flow up to the sponsor bank, and the sponsor bank's downstream visibility into the operator's AI.
- The intake records the rail-by-rail role (ACH, Same Day ACH, wire, FedNow, RTP, card debit / credit, check, cross-border) the AI use case touches; different rails have different irrevocability and customer-protection clocks.

##### 2. Money transmitter and MSB framing

Where the program operator is itself a money transmitter or registered MSB, FinCEN MSB rules (31 CFR Part 1022) and state MTL regimes apply:

- `regulatory_flags`: `FinCEN_MSB` and state-by-state MTL flags as applicable, with routing to `ai-risk-tiering` and `validation-plan`.
- The intake captures NMLS posture state-by-state (which states the firm is licensed in for money transmission) and Money Transmitter Modernization Act adoption status [verify state-by-state adoption status as of date of analysis].
- An open question for downstream work: where the use case touches BSA/AML, CIP, SAR-filing, or sanctions screening, the intake routes to `aml-model-monitoring` (in financial-crime-governance) and to `sanctions-screening-qa`.

##### 3. Reg E reach on consumer-facing payment errors

Where the use case touches consumer-payment error resolution (intake of error claims, dispute routing, denial generation) under Reg E (12 CFR Part 1005), the intake captures:

- `regulatory_flags`: `Reg_E` with the §1005.11 timing posture (10 / 45 / 90-day clocks) named in the basis. Routing to `validation-plan` and `udaap-risk-review` (in consumer-compliance-fair-lending).
- An open question: the program-agreement allocation of error-resolution operational ownership between sponsor bank and program operator.

##### 4. NACHA Operating Rules where the firm acts as ODFI, RDFI, or Third-Party Sender

For ACH-related AI use cases, NACHA Operating Rules (current edition) apply [verify current rule citations]:

- `regulatory_flags`: `NACHA_Operating_Rules` with routing to `validation-plan`. The basis names the role (ODFI, RDFI, Third-Party Sender) and the relevant return-rate threshold (administrative-return, overall-return, unauthorized-return) [verify current thresholds].
- An open question for `validation-plan`: how is the use case's contribution to the firm's return-rate posture monitored against current NACHA thresholds.

##### 5. Card-network rules

Where the use case touches card debit or credit rails:

- `vendor_dependencies`: BIN sponsor named with role and criticality.
- `regulatory_flags`: card-network rules referenced as "Visa Core Rules and Visa Product and Service Rules; Mastercard Rules — current edition; specific sections to be confirmed against the firm's licensed copy" because the rulebooks are not public.
- An open question for `vendor-diligence`: the BIN sponsor's chargeback-rights posture and fraud-rate program escalation handling for the use case.

##### 6. Faster-payments and irrevocability

For FedNow, RTP, and Same Day ACH use cases:

- The intake captures the irrevocability posture (real-time settlement finality on FedNow / RTP means the fraud playbook is request-for-return-of-funds plus monitoring escalation, not chargeback).
- An open question for downstream work: the fraud-typology library covers faster-payments-specific patterns (mule patterns on instant-funded accounts, ISO 20022 message-field anomalies, irrevocability-driven typology shift).

##### 7. CFPB direct supervision under §1024 larger-participant rule

The digital wallets and payment apps larger-participant rule (December 2024) [verify Federal Register citation, effective date, and current state including any litigation or congressional review] designates a covered cohort of non-bank firms for direct CFPB supervision:

- An applicability check belongs in the intake: is the firm in scope for the larger-participant rule.
- Where in scope, `regulatory_flags`: `CFPB_larger_participant` with routing to `ai-risk-tiering` and `udaap-risk-review`.

##### 8. UDAAP themes specific to fintech

CFPB Supervisory Highlights and consent orders (2023-26) have signalled on fintech UDAAP themes [verify which actions are current as of date of analysis]:

- Account closures and account holds without adequate notice or recourse.
- Reg E error-resolution timing failures presented as UDAAP rather than as Reg E findings.
- Fee disclosure failures (junk-fee themes, surprise-fee patterns).
- Marketing-claim review for FDIC-insurance representation (post-Synapse-era).
- BNPL UDAAP themes (the CFPB BNPL interpretive rule was **nullified by Pub. L. 119-11 (May 9, 2025); historical only**, but BNPL conduct under UDAAP §1031 and Reg B §1002.9 still reaches the same fact patterns).
- Dark-pattern risk in onboarding and product-selection flows.

For any AI use case that touches these themes, intake captures the regulatory flag and routes to `udaap-risk-review`.

#### Payments-fintech-specific intake fields

In addition to the capability intake spine, the following payments-fintech-specific facts belong on the record when relevant:

- Sponsor-bank counterparty (or "no sponsor bank" if direct-licensed money transmitter).
- Rail-by-rail role for the use case (ACH / Same Day ACH / wire / FedNow / RTP / card debit / card credit / check / cross-border).
- NMLS state-by-state licensure posture if direct-licensed money transmitter.
- BIN sponsor counterparty if card rails are in scope.
- Larger-participant rule applicability.
- BSA/AML role (bank-side, fintech-side, or split via program agreement).

#### Common pitfalls in payments-fintech intake

- Recording a fintech AI use case without the sponsor-bank dependency. The program operator may not be the supervised entity, but the bank-side risk is the bank's regardless.
- Treating "vendor concentration" as a single number; sponsor-bank, BIN-sponsor, and processor are three distinct concentration axes that fail differently.
- Missing the rail-specific Reg E §1005.11 clock on consumer-facing error-resolution AI; the clock does not stop because the AI is making the call.
- Missing the Money Transmitter Modernization Act state adoption check on a multi-state money-transmitter use case.
- Missing the larger-participant rule applicability on a digital-wallet or payment-app use case at scale; the rule changes the supervisory posture from indirect-via-sponsor to direct-CFPB.
- Treating FDIC-insurance representation framing as marketing detail rather than as a UDAAP and FDIC misrepresentation rule (12 CFR Part 328 Subpart B, **2023 final rule with 2024-2025 effective-date extensions** — verify current effective date for the engagement) flag.
