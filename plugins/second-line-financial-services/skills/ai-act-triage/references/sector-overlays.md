# sector-overlays

One section per sector. Read only the sections the scope calls for.

## banking

### Banking sector overlay for ai-act-triage

When the scope record names sector `banking`, this overlay adds banking-specific scoping, named-source reach, and parallel-regime reconciliation to the EU AI Act triage. EU branches and subsidiaries of US banks, EU-headquartered credit institutions, and EU operations of non-EU banking groups all use this overlay alongside the capability triage. Where there is conflict between the capability defaults and this overlay, the overlay governs the banking-specific elements.

Loaded by: `ai-act-triage/SKILL.md` when `scope.sector_overlay_set` includes `banking`, or when the institution type implicates a banking entity (national bank, state member bank, savings association, bank holding company, foreign banking organization with EU operations, EU credit institution, EU subsidiary or branch of a non-EU banking group). Cited and section-referenced anchors live in `references/source-anchors.md`.

#### What changes for a banking triage

##### 1. Annex III(5)(b) is the spine for credit decisioning

Annex III(5)(b) names "AI systems intended to be used to evaluate the creditworthiness of natural persons or establish their credit score, with the exception of AI systems used for the purpose of detecting financial fraud" as a high-risk use case. This is the most direct route to high-risk classification for banking work. The triage walks Annex III(5)(b) explicitly and records the row whether the answer is "applies" or "does not apply".

Boundary cases the triage flags:

- SME credit decisioning where SMEs include sole traders or micro-enterprises whose obligations attach to a natural person: in scope of (5)(b). Where SMEs are exclusively legal entities, the row does not apply on its face; the triage records the legal-entity-only scope and routes to legal where the firm's product perimeter includes any natural-person exposure.
- Behavioural scoring on existing customers (line management, collections triggers, dynamic credit-limit adjustment) for natural persons: in scope of (5)(b) where the score materially influences credit terms. Recorded explicitly.
- Fraud-detection AI: excluded from (5)(b) by the express carve-out. The triage records the carve-out and confirms the model's purpose is fraud detection rather than creditworthiness; where the same model serves both purposes, the carve-out does not protect the creditworthiness use.
- Consumer-credit affordability assessment: in scope of (5)(b). The triage records the firm's affordability-assessment regime alongside the AI Act analysis.

Article 6(3) derogation analysis is rarely available for credit decisioning models because the model materially influences the credit decision rather than performing a narrow procedural task. The triage records the derogation analysis explicitly and typically does not invoke it for creditworthiness use cases; flag the analysis to legal where invoked.

##### 2. Annex I product-safety route is rarely the route

Annex I high-risk classification (via product-safety legislation) is the alternative high-risk route under Article 6(1). For banking AI, the route is rarely invoked; banking products are not in the Annex I product-safety lists. The triage records the screen running and the typical conclusion (Annex I not invoked).

##### 3. CRR/CRD model-risk overlap and ECB guide on internal models

For credit institutions in the EU, AI use in credit risk modelling intersects with CRR/CRD model-risk expectations and, for IRB-approved institutions, the ECB Guide to internal models. The triage records the overlap and routes to the firm's internal-models function:

- IRB credit-risk models that incorporate AI elements need both the AI Act high-risk obligations (Articles 9 to 15, 26, and where applicable 27) and the CRR Part Three Title II Chapter 3 internal-models regime. The two regimes are independent; satisfying one does not satisfy the other.
- Non-IRB use of AI in credit decisioning still attracts the AI Act high-risk obligations under Annex III(5)(b); the CRR/CRD overlap depends on whether the model is in the regulatory-capital chain.
- Model-risk-management practice under the EBA Guidelines on internal governance and the ECB SREP framework provides the firm-side governance frame; the AI Act adds specific obligations on top.

The triage records the regime overlap as a side-by-side block; reviewers downstream need both lenses visible.

##### 4. EU branches and subsidiaries of US banks

For US banks operating in the EU through a branch, subsidiary, or representative office, the EU entity's deployer or provider role attracts AI Act obligations on the EU side regardless of US-side model-risk practice (the joint interagency Revised Guidance on Model Risk Management, OCC 2026-13 / FRB SR 26-2 / FDIC FIL-15-2026, which in any case is scope-excluded for GenAI and agentic AI per footnote 3). The triage records:

- Which EU entity is the operator (branch, subsidiary, intermediate parent undertaking under the IPU regime).
- Which roles attach (provider, deployer, importer, distributor, authorised representative).
- The reconciliation between the US-side documentation (firm model-risk documentation per the joint interagency bulletin for traditional models, plus the firm's AI governance documentation under NIST AI RMF / NIST AI 600-1 / ISO/IEC 42001 for GenAI use cases, plus model inventory and committee evidence) and the EU-side Article 11 / Annex IV technical documentation. The two artifacts overlap substantially; the triage names the deltas the EU-side artifact must add.

A US-headquartered model used by an EU subsidiary: the EU subsidiary is the deployer. The US parent's role depends on whether the parent develops the model (provider) or simply provides the infrastructure (not provider). The triage records the analysis on the operator-role line.

##### 5. Article 27 FRIA reaches credit institutions explicitly

Article 27(1)(b) names credit institutions as deployers in scope of the FRIA obligation when deploying high-risk AI systems referred to in Annex III. For an EU credit institution deploying an Annex III(5)(b) creditworthiness system, the FRIA is required. The triage records:

- The FRIA-vs-DPIA reconciliation; the GDPR DPIA does not satisfy Article 27 on the fundamental-rights-impact, mitigation, governance, and complaints-handling elements.
- The FRIA owner (typically legal in coordination with conduct or consumer-protection function).
- The FRIA evidence routing to the Article 27(3) notification to the market surveillance authority.

For non-credit-institution banking entities (e.g., a US bank operating in the EU through a branch that is not itself a credit institution under EU classification), the Article 27(1)(b) reach is on the facts; the triage routes to legal.

##### 6. Adverse-action and explainability reach (US-side analogue)

Where the firm has US-side consumer-credit reach (US parent or US subsidiary), Reg B §1002.9 (specific principal reasons for adverse action) and Comment 9(b)(2)-3 of the Official Staff Commentary reach the US-side adverse-action workflow. CFPB Circulars 2022-03 / 2023-03 are **withdrawn May 12, 2025; historical only**; the regulatory text continues to apply on its own terms. The EU AI Act does not directly impose a US-style adverse-action obligation, but Articles 13 (transparency to deployers) and 14 (human oversight) plus the GDPR Article 22 (automated decision-making affecting the data subject) reach the EU side of the same surface.

The triage records the parallel obligations on a side-by-side block where the firm's footprint includes both jurisdictions; the artifact does not collapse the two analyses.

##### 7. AML and BSA models: the financial-fraud carve-out and what it does not cover

The Annex III(5)(b) carve-out for fraud detection covers fraud detection. AML transaction-monitoring, sanctions screening, customer-risk-rating, and PEP screening are not creditworthiness systems and do not fall under (5)(b) at all; the triage records the row as not applicable rather than relying on the carve-out.

For the EU side, the EBA Guidelines on ML/TF risk factors and the AMLR / AMLD6 transposition reach the AML model on a different track. The triage records the AML regime as the operative governance frame and notes that the AI Act high-risk obligations do not attach to AML models on the (5)(b) row; other Annex III rows do not typically reach AML either. The triage walks the rows and records the conclusion.

##### 8. CCAR/DFAST and stress-testing model overlap

For US bank holding companies subject to stress testing, AI elements in stress-projection or allowance models attract SR 15-18 (or successor) US-side documentation. EU subsidiaries of the same group may operate under EBA stress-testing methodology. The AI Act overlay attaches Annex III high-risk classification only where the model is in scope of an Annex III row (typically (5)(b) for natural-person creditworthiness elements within the stress projection). The triage records the cross-walk and routes to the firm's stress-testing owner.

##### 9. Supervisory-relationship cadence

For EU credit institutions, the AI Act supervisor is the relevant member-state competent authority designated under Article 70, plus the AI Office for cross-cutting matters and GPAI provider supervision. The triage records:

- The named NCA in the operating member state.
- The interaction with the prudential supervisor (ECB for SSM-supervised institutions; member-state competent authority for less-significant institutions). The prudential supervisor and the AI Act NCA may be the same body, may be sister bodies, or may be different agencies depending on member-state designation. The triage names both and records the coordination posture where designation is split.

For OCC-, FRB-, FDIC-, or NCUA-supervised US parents, the US-side supervisor is unaffected by the AI Act analysis; the triage records the US-side supervisory relationship for completeness.

##### 10. Banking-AI use-case categories the triage explicitly recognises

The triage labels the use-case category up front because each category lights up different obligations:

- Origination credit decisioning (consumer): Annex III(5)(b) applies for natural persons; Article 27 FRIA required for credit-institution deployers; CFPB-Circular-style adverse-action reach on US side.
- SME credit decisioning: Annex III(5)(b) applies where natural-person exposure is present (sole traders, micro-enterprises); legal-entity-only scope routes outside (5)(b).
- Behavioural scoring (existing-customer line management, collections, dynamic credit limit): Annex III(5)(b) applies where the score materially influences credit terms.
- Fraud detection: excluded from (5)(b) by carve-out; other Annex III rows screened.
- AML transaction monitoring, sanctions screening, customer-risk-rating: not Annex III; record explicitly; route to AML regime.
- Customer-facing chatbot (account servicing, FAQ): not Annex III; Article 50 transparency applies.
- Internal productivity GenAI (drafting, summarisation): not Annex III; Article 50 sub-obligations screened on the facts.
- Marketing personalisation and offer optimisation: typically not Annex III; Article 5(1)(a) manipulation screen runs (conduct overlay) where behavioural-economics levers are in play.
- ECB-supervised IRB credit-risk model with AI elements: Annex III(5)(b) applies plus CRR/CRD internal-models overlay.

#### Banking-specific output template additions

The triage artifact adds the following blocks when this overlay loads:

- A use-case category line at the top (origination credit decisioning / SME credit / behavioural scoring / fraud / AML / customer chatbot / internal productivity / marketing personalisation / IRB credit-risk).
- An EU-entity operator-role table (which EU entity, which role) for cross-border banking groups.
- A CRR/CRD internal-models overlap line for IRB use cases.
- A US-side / EU-side parallel-regime reconciliation block where the firm's footprint spans both (joint interagency model-risk bulletin and AI-specific frameworks to Article 11 / Annex IV mapping; Reg B §1002.9 adverse-action analogue to GDPR Article 22 mapping; CFPB Circulars 2022-03 / 2023-03 are **withdrawn May 12, 2025; historical only**).
- An NCA-and-prudential-supervisor coordination line when designation is split or unclear.
- A FRIA-vs-DPIA reconciliation note for any (5)(b) or other Article 27 trigger.
- An AML-regime routing note where the use case is AML-adjacent and (5)(b) does not apply.

#### Common pitfalls in banking AI Act triages

- Treating (5)(b) as covering all banking credit work; the row is for natural-person creditworthiness and credit scoring with the fraud-detection carve-out, not all credit-related models.
- Skipping the FRIA because the firm has a DPIA; Article 27 reaches credit institutions deploying Annex III high-risk and the DPIA does not cover the FRIA elements.
- Importing SR 11-7 documentation as Annex IV evidence without delta analysis; the artifacts overlap but Annex IV has specific elements (intended purpose, hardware and software, data, methodology, testing, human oversight design, post-market monitoring) that the firm's SR 11-7 documentation may not carry in Annex IV form.
- Conflating the AI Act NCA with the prudential supervisor; designation may be split and coordination is on the firm to manage.
- Treating fraud-detection models as exempt from all AI Act analysis under the (5)(b) carve-out; the carve-out is from (5)(b) only. Other Annex III rows and Article 50 transparency screen separately.
- Missing the IRB / internal-models overlap for credit-risk models that feed regulatory capital; the AI Act and the CRR/CRD regimes are independent and both apply.
- Asserting Article 6(3) derogation for credit decisioning to escape high-risk classification; the derogation is rarely available for systems that materially influence credit decisions.
- Treating EU subsidiaries' AI Act obligations as automatically discharged by US parent's model-risk practice; the EU entity's deployer or provider role attracts EU-side obligations on its own facts.

## capital-markets

### Capital-markets sector overlay for ai-act-triage

When the scope record names sector `capital-markets`, this overlay adds capital-markets-specific scoping, Article 2 exclusion analysis, and parallel-regime reconciliation to the EU AI Act triage. EU branches of US asset managers and broker-dealers, EU-authorised investment firms (MiFID II), UCITS management companies, AIFMs, and EU-authorised central counterparties and trading venues all use this overlay alongside the capability triage. Where there is conflict between the capability defaults and this overlay, the overlay governs the capital-markets-specific elements.

Loaded by: `ai-act-triage/SKILL.md` when `scope.sector_overlay_set` includes `capital-markets`, or when the institution type implicates an investment firm, asset manager, broker-dealer, UCITS ManCo, AIFM, trading venue, central counterparty, central securities depository, or related capital-markets entity. Cited and section-referenced anchors live in `references/source-anchors.md`.

#### What changes for a capital-markets triage

##### 1. Annex III rarely lands directly for adviser and BD use cases

The Annex III high-risk list focuses on use cases with material impact on natural persons (creditworthiness, life and health insurance pricing, employment selection, biometric, education, essential services, law enforcement, migration, justice). Most adviser, BD, asset-management, and trading-venue AI use cases do not land in Annex III directly:

- Investment recommendation and portfolio-management AI: not Annex III. The fiduciary and best-interest analysis sits in MiFID II and member-state conduct frameworks, not in the AI Act high-risk regime.
- Trading and execution algorithms: not Annex III. The MiFID II algorithmic trading regime (Article 17 and RTS 6) reaches separately.
- Surveillance algorithms (insider trading, market abuse, manipulation, layering, spoofing): not Annex III. MAR / market-abuse regime reaches separately.
- Research and marketing GenAI: not Annex III. Article 50 transparency typically applies; Marketing Rule and member-state advertising regimes reach separately.

The triage walks Annex III row by row and records the conclusion. The walk is not perfunctory because boundary cases reach:

- Employment selection AI used by the firm for staff hiring or evaluation: Annex III(4) applies. Common in larger advisers and BDs; the triage flags this as a separate workstream from the investment-side AI.
- Biometric AI for office access or trading-floor identification: Annex III(1) applies in defined circumstances.
- Consumer-credit-style scoring inside a BD retail-onboarding flow: Annex III(5)(b) applies where the BD extends consumer credit (e.g., margin-equivalent products with consumer-credit characteristics); rare but worth the row-by-row check.

##### 2. Article 2 exclusion analysis: the MiFID II surveillance and market-abuse boundary

Article 2(3) of the AI Act excludes AI systems and models specifically developed and put into service for the sole purpose of scientific research and development. This exclusion does not reach production trading-venue surveillance or market-abuse detection systems.

The triage walks Article 2 exclusions on the record where the use case is research-or-pilot adjacent. The triage does not invoke the research exclusion for a system that has moved into production use.

##### 3. MiFID II algorithmic trading regime runs in parallel

For investment firms engaged in algorithmic trading, MiFID II Article 17 and Commission Delegated Regulation 2017/589 (RTS 6) impose substantive governance obligations: governance of the algorithm, testing, kill functionality, change management, conformance testing, and notifications to competent authorities. AI Act obligations attach in addition where a row of Annex III applies, but typically do not for trading algos.

The triage records the regime overlap as a side-by-side block; reviewers downstream need both lenses visible. The side-by-side block names:

- The MiFID II Article 17 / RTS 6 obligations (governance, testing, kill switch, change management, notification).
- The AI Act obligations attaching where any do (rare; typically Article 50 if the algo's outputs reach a natural-person interface, otherwise none from the high-risk regime).
- The reconciliation: MiFID II is the operative governance frame; AI Act adds where it adds.

##### 4. Article 50 transparency for client-facing GenAI

For client-facing AI surfaces (chatbots, RFP-response generation, investment-letter drafting, research summarisation reaching clients), Article 50 sub-obligations screen individually:

- 50(1) AI-interaction disclosure: applies inside the firm and on client surfaces.
- 50(2) synthetic-content marking: applies on outbound text drafts that reach clients.
- 50(3) deepfake disclosure: applies where synthetic image, audio, or video is used in client communications.
- 50(4) AI-generated text on matters of public interest: applies where the firm publishes commentary on matters of public interest (e.g., macro research released publicly) generated or substantially assisted by AI.
- 50(5) emotion recognition / biometric categorisation: typically not applicable to capital-markets use cases.

The disclosure language sits alongside the Marketing Rule disclosures (US-side) and member-state advertising regimes (EU-side). The triage records the disclosure-language posture and routes the language drafting to the firm's marketing-and-disclosures function with legal review.

##### 5. Books-and-records reach for AI-generated content

For US-registered advisers under Rule 204-2 and BDs under Rule 17a-3 / 17a-4, AI-generated content supporting a recommendation or decision falls within books-and-records preservation scope. The EU AI Act does not directly impose a books-and-records obligation on the same surface, but Article 12 (record-keeping obligations on providers of high-risk AI systems) and Article 26(6) (deployer obligation to keep automatically generated logs for at least six months) attach where the system is high-risk.

For most capital-markets use cases that are not high-risk, the books-and-records reach is the US-side or member-state-side regime; the AI Act does not add a parallel obligation. The triage records the operative books-and-records regime per jurisdiction and notes where AI Act Article 12 / 26(6) attaches in addition.

##### 6. Marketing Rule (US) and member-state marketing regimes

For investment advisers under the IAA, Marketing Rule (Rule 206(4)-1) coverage extends to AI-generated client communications, AI-generated hypothetical performance, and AI-generated testimonials/endorsements. For EU-authorised investment firms, the MiFID II marketing communications regime (Article 24 plus Commission Delegated Regulation 2017/565) reaches.

The triage records the marketing-regime reach per jurisdiction; AI Act Article 50 is the AI-side disclosure obligation that runs alongside but does not replace the marketing-regime disclosures.

##### 7. Sub-adviser and fund-board awareness

Where the AI is operated by a sub-adviser or by a delegate of an EU UCITS ManCo or AIFM, the delegation-and-oversight regime applies (UCITS Directive Article 13 and Commission Delegated Regulation 2010/43; AIFMD Article 20 and AIFMR). The triage records:

- The sub-adviser or delegate's operator role under the AI Act (typically deployer).
- The principal entity's oversight obligations under the delegation regime.
- The fund-board reporting posture for material AI use changes.

##### 8. GPAI and vendor-LLM evidence asks

For client-facing GenAI surfaces using a vendor LLM, the vendor's GPAI obligations under Articles 51 to 55 do not transfer to the deploying firm. The deploying firm is the deployer of the system and may be the provider of the system if it builds the system on top of the GPAI model. The triage records:

- The vendor's GPAI status (general-purpose AI model under Article 51; systemic-risk GPAI under Article 51(2) where designated).
- The vendor's Code of Practice signature status (the EU AI Office Code of Practice on General-Purpose AI is voluntary; signature is a deployer-side evidence-quality signal).
- The deployer-side evidence asks: training-data summary per Article 53(1)(d), copyright posture, transparency documentation; routed to vendor diligence.
- The Article 25 flip-to-provider analysis where the firm fine-tunes or substantially modifies the vendor model.

##### 9. AIFMD / MiFID II extraterritorial reach

For US advisers serving EU professional or retail clients, AIFMD (for AIF marketing into the EU) and MiFID II (for cross-border investment-services provision) reach. The AI Act overlay attaches where any Annex III row applies (rare for adviser/BD use cases) or where Article 50 transparency obligations attach to client-facing surfaces. The triage records:

- Whether the US adviser markets AIFs into the EU under AIFMD national private placement regimes.
- Whether the US adviser provides investment services into the EU under MiFID II reverse solicitation, third-country branch regime, or third-country firm access (where established by an equivalence decision).
- The AI Act exposure on the EU side (typically Article 50 transparency for client-facing surfaces; Annex III rare).

##### 10. Capital-markets-AI use-case categories the triage explicitly recognises

The triage labels the use-case category up front:

- Investment-recommendation or portfolio-management AI: not Annex III; MiFID II / IAA fiduciary frame is operative.
- Trading and execution algorithms: not Annex III; MiFID II Article 17 / RTS 6 is operative on the EU side; SEC Rule 15c3-5 on the US side.
- Surveillance and market-abuse detection: not Annex III; MAR (EU) and FINRA / SEC supervisory rules (US) operative.
- Client-facing chatbot or assistant: not Annex III; Article 50 transparency applies.
- Research and marketing GenAI: not Annex III; Article 50 sub-obligations screened; Marketing Rule (US) and MiFID II marketing-communications (EU) overlay.
- Internal productivity GenAI (RFP response, board materials, summarisation): not Annex III; books-and-records reach where output supports a recommendation or decision.
- Employment selection AI for staff hiring: Annex III(4) applies; separate workstream from investment-side AI.
- Biometric AI for office access: Annex III(1) applies in defined circumstances.

#### Capital-markets-specific output template additions

The triage artifact adds the following blocks when this overlay loads:

- A use-case category line at the top (per the categories above).
- A MiFID II Article 17 / RTS 6 cross-walk for any algorithmic-trading use case.
- A Marketing Rule / MiFID II marketing-communications cross-walk for any client-facing GenAI use case.
- A books-and-records reach line per applicable jurisdiction.
- A delegation-and-oversight regime line for sub-adviser or delegate operation.
- A GPAI vendor-evidence-asks block for vendor-LLM-backed surfaces, including Code of Practice signature status.
- An employment-AI separate-workstream flag where staff-hiring AI is on the firm's inventory.

#### Common pitfalls in capital-markets AI Act triages

- Assuming the AI Act has nothing to say about capital-markets AI because Annex III rarely lands directly; Article 50 transparency reaches client-facing GenAI surfaces and the screen must run.
- Conflating the MiFID II Article 17 / RTS 6 algorithmic-trading regime with the AI Act high-risk regime; they are separate and both attach where their own conditions are met.
- Treating books-and-records reach as the AI Act's reach; the operative books-and-records regime is the US-side adviser/BD rule or the member-state-side investment-firm rule; AI Act Article 12 / 26(6) attaches only for high-risk systems.
- Importing US-side Marketing Rule disclosure language as the AI Act Article 50 disclosure; the two are separate and both apply where their conditions are met.
- Skipping the delegation-and-oversight analysis for sub-adviser or delegate AI use; UCITS Article 13 and AIFMD Article 20 reach the principal's oversight obligation regardless of where the AI sits.
- Treating GPAI provider obligations as the deployer's obligations; the deployer's obligations are the deployer's; the GPAI provider obligations sit with the model provider.
- Missing the staff-hiring AI workstream as Annex III(4); the workstream is separate from investment-side AI but reaches under the same triage.
- Asserting MiFID II reverse-solicitation as a basis for ignoring AI Act exposure on EU clients; reverse solicitation does not displace AI Act obligations on the firm where the firm's AI surface reaches EU users.

## insurance

### Insurance sector overlay for ai-act-triage

When the scope record names sector `insurance`, this overlay adds insurance-specific scoping, named-bulletin reach, and parallel-regime reconciliation to the EU AI Act triage.

This overlay carries the substance of the deprecated `insurance-ai-act-triage` skill. A US carrier with EU operations or EU policyholders, an EU carrier in EU-only operations, and a reinsurer with EU cedents all use this overlay alongside the capability triage. Where there is conflict between the capability defaults and this overlay, the overlay governs the insurance-specific elements.

Loaded by: `ai-act-triage/SKILL.md` when `scope.sector_overlay_set` includes `insurance`, or when the institution type implicates an insurance entity (life, health, P&C, reinsurance, captive). Cited and section-referenced anchors live in `references/source-anchors.md`.

#### What changes for an insurance triage

##### 1. Annex III(5)(c) is the spine for life and health

Annex III(5)(c) names "AI systems intended to be used for risk assessment and pricing in relation to natural persons in the case of life and health insurance" as a high-risk use case. This is the most direct route to high-risk classification for insurance work. The triage walks Annex III(5)(c) explicitly and records the row whether the answer is "applies" or "does not apply"; for example, a P&C pricing model is not in (5)(c), and the triage says so on the record.

Boundary cases the triage flags:

- Group health pricing: in scope of (5)(c) when the rating element falls on natural persons (group rating with individual experience-rating components).
- Reinsurance: typically not in scope of (5)(c) directly, because the cedent is a legal entity rather than a natural person; flag whether the reinsurance-pricing model uses individual-policy-level inputs that effectively price natural persons.
- Disability and long-term care: read as in scope of (5)(c) where the product is structured as health or life-equivalent.
- Annuity pricing: read on the facts; longevity-based annuity pricing falls in life; investment-only structures may not.

Article 6(3) derogation analysis is non-trivial for insurance pricing: the model is rarely a "narrow procedural task" or a "preparatory" output, because the price is the product. The triage records the derogation analysis explicitly and typically does not invoke it for pricing or risk-assessment use cases; flag the analysis to legal where invoked.

##### 2. Claims AI is not automatically Annex III, but watch the boundary

Claims AI (FNOL triage, severity prediction, fraud-indicator scoring, claims-handling chatbots) is not directly named in Annex III. The triage records the walk and the conclusion. Boundary conditions to watch:

- Where a claims model determines or materially influences benefit payment (life or health benefits), an analysis under (5)(c) may apply by extension; flag to legal.
- Where the model influences fraud determinations that affect access to health benefits, GDPR Article 22 (automated decision-making affecting the data subject) reaches in addition to AI Act considerations.
- Where the claims chatbot generates output to natural persons, Article 50 transparency obligations apply (50(1) interaction-with-AI disclosure; 50(2) synthetic-content marking on outbound text).

##### 3. NAIC Bulletin (December 2023) is the parallel US-side regime; the triage cross-walks

Even when the EU AI Act applies, the carrier's US-side AIS Program documentation under the NAIC Bulletin runs in parallel. The triage records the cross-walk so the firm does not duplicate work or miss a parallel obligation. The Bulletin is itself a model bulletin; state-by-state adoption is tracked via the NAIC AI Working Group adoption tracker. Cite by jurisdiction; do not assert the Bulletin as binding without state adoption confirmation.

The AIS Program elements (governance, risk management, testing, validation, third-party AI accountability, monitoring, documentation, transparency, fairness) map roughly to the EU obligations under Articles 9, 10, 11, 13, 14, 15, and 26. The mapping is not one-for-one; the triage carries a side-by-side block in the artifact for an in-scope insurance use case so the reviewer sees both lenses.

##### 4. State DOI bulletins extend the bar in named jurisdictions

The triage names the strictest applicable state in the operating footprint and the relevant bulletin. Named bulletins to enumerate when in scope:

- Colorado Division of Insurance regulation implementing SB 21-169 — governance and risk management of External Consumer Data and Information Sources (ECDIS) and predictive models in life-insurance underwriting. ECDIS provenance is a triage-record field when CO is in scope.
- New York DFS Insurance Circular Letter on AI and ECDIS in life-insurance underwriting (January 2024) — governance, fairness testing, disclosure, and consumer-recourse expectations.
- California DOI bulletin on AI use in insurance — broader scoping than CO/NY; informs disclosure posture.

Where any of these bulletins apply alongside the EU AI Act triage, the artifact records both. The triage does not collapse the US-side and EU-side analyses; reviewers downstream need both lenses visible.

##### 5. Insurance-AI use-case categories the triage explicitly recognises

The triage labels the use-case category up front because each category lights up different obligations:

- Accelerated underwriting (life and health): Annex III(5)(c) applies; ECDIS provenance is a triage field if external data is in the input set; HIPAA touch-flag set if PHI; CO/NY DFS bulletins apply.
- Claims AI (triage, FNOL, severity prediction, fraud-indicator scoring, claims chatbots): Annex III not directly; Article 50 applies for chatbots; NAIC Model #880 fair-claims-settlement frame applies regardless of decision technology.
- Pricing and rating ML factors and ECDIS use: Annex III(5)(c) for life and health; state DOI rate-filing regimes apply where the model touches filed rates.
- Marketing AI for product targeting: not Annex III; Article 50 sub-obligations may apply if synthetic content is generated; NAIC Model #275 [verify model number] for annuity-suitability and best-interest reach.
- Agent-facing AI (illustration generation, suitability triage): not Annex III; producer-licensing reach if the AI takes actions that constitute producer activity; suitability and best-interest standards apply.
- Back-office AI (call-center summarisation, mailroom OCR): typically minimal-risk under the AI Act; firm-side governance still applies.

##### 6. Fairness vs unfair-discrimination terminology

EU AI Act Article 10 frames data governance and bias examination using the EU vocabulary (representativeness, errors, biases reasonably foreseeable). State DOI rate analysts and NAIC Bulletin reviewers use the unfair-discrimination test under Model #880 (actuarial justification, permitted versus prohibited rating factors). The triage uses both vocabularies when applicable and records a translation note. Sign-off questions probe whether the test framing matches the regulator's framing for each jurisdiction in the operating footprint.

##### 7. HIPAA scope check

Any insurance AI touching PHI (health-claims AI, life-and-health underwriting using prescription-history or medical data) requires a HIPAA Privacy and Security Rule cross-check that the EU AI Act triage alone will not produce. The triage flags HIPAA touch and routes to the privacy team; for vendor-supplied AI handling PHI, BAA posture is a vendor-diligence item.

##### 8. Producer licensing on consumer-facing AI

A consumer-facing AI that takes binding-equivalent actions (binding, quoting commitments, surrendering, paying claims) can trigger producer-licensing questions in US states; flag for the licensing function. Article 50 transparency applies in the EU for the AI-interaction surface; the licensing question is a separate, US-side workstream.

##### 9. ORSA materiality

For an enterprise-material AI use case (often the case for accelerated underwriting at scale), NAIC ORSA (Model #505) inclusion is required on the US side. The triage flags ORSA inclusion; the EU-side equivalent for Solvency II governance is the ORSA-equivalent under EIOPA and the Central Bank of Ireland (or other EU NSAs); the artifact carries both flags.

##### 10. Vendor-AI accountability

Both regimes hold the carrier accountable for vendor-supplied AI. Under the AI Act, the carrier is the deployer when the vendor is the provider; deployer obligations under Article 26 attach. Under the NAIC Bulletin, third-party AI accountability is one of the AIS Program elements. The triage names the vendor and the firm-side governance regardless of which regime is the lens.

#### Insurance-specific output template additions

The triage artifact adds the following blocks when this overlay loads:

- A use-case category line at the top (accelerated underwriting / claims AI / pricing / marketing AI / agent-facing AI / back-office).
- AIS Program element-by-element status (governance, risk management, testing, validation, third-party AI accountability, monitoring, documentation, transparency, fairness), each tied to evidence.
- Per-state DOI bulletin status (CO, NY DFS, CA at minimum if in operating footprint; strictest applicable state flagged).
- ECDIS provenance for any external-consumer-data input.
- HIPAA touch flag and BAA pointer for any vendor handling PHI.
- Producer-licensing posture for consumer-facing AI taking binding-equivalent actions.
- ORSA inclusion flag (US side) and Solvency II-ORSA equivalent flag (EU side) where the use case is enterprise-material.
- AI Act <-> NAIC Bulletin cross-walk table for the in-scope obligations.
- AI Act <-> Solvency II governance reconciliation note where the EU subsidiary is in scope.

#### Common pitfalls in insurance triages

- Skipping the Annex III(5)(c) walk for a P&C pricing model on the assumption that pricing AI is automatically high-risk; (5)(c) is life and health, not all insurance pricing.
- Treating claims AI as automatically high-risk because it is consumer-facing; the Annex III walk often returns "no row applies" for claims AI, with Article 50 being the operative obligation for chatbot surfaces.
- Treating the NAIC Bulletin as binding when state adoption has not occurred; cite by jurisdiction.
- Carrying generic fairness vocabulary into a state DOI rate-filing context; rate analysts use unfair-discrimination vocabulary under Model #880.
- Conflating the EU-side Article 27 FRIA with the GDPR DPIA; both may be required and they capture different elements.
- Missing ECDIS provenance for a life-underwriting model when CO or NY is in operating footprint.
- Treating EU AI Act high-risk as a US-side obligation by extension; the NAIC Bulletin is the US-side parallel and the obligations attach independently.
- Missing the vendor-AI accountability lens on both sides; the carrier remains accountable regardless of which regime the reviewer is reading.

## payments-fintech

### Payments and fintech sector overlay for ai-act-triage

When the scope record names sector `payments-fintech`, this overlay adds payments-and-fintech-specific scoping, BNPL and consumer-lending reach, and parallel-regime reconciliation to the EU AI Act triage. EU-authorised payment institutions and electronic-money institutions, BNPL and consumer-lending fintechs operating in or into the EU, sponsor-bank-program partners with EU end-customer exposure, and crypto-asset service providers under MiCA all use this overlay alongside the capability triage. Where there is conflict between the capability defaults and this overlay, the overlay governs the payments-and-fintech-specific elements.

Loaded by: `ai-act-triage/SKILL.md` when `scope.sector_overlay_set` includes `payments-fintech`, or when the institution type implicates a payment institution, electronic-money institution, BNPL provider, consumer-lending fintech, sponsor-bank-program partner, or MiCA-authorised crypto-asset service provider with EU operations or EU end-customers. Cited and section-referenced anchors live in `references/source-anchors.md`.

#### What changes for a payments-and-fintech triage

##### 1. Annex III(5)(b) is the spine for BNPL and consumer-lending fintechs

Annex III(5)(b) reaches AI systems used to evaluate creditworthiness or establish credit scores of natural persons, with the fraud-detection carve-out. For BNPL providers, consumer-lending fintechs, and any fintech extending consumer credit in or into the EU, the row is the most direct route to high-risk classification.

Boundary cases the triage flags:

- BNPL with deferred-payment-only structure (no credit charge, single-statement settlement): Consumer Credit Directive II (2023/2225) brings most BNPL into consumer-credit scope from 20 November 2026 transposition; the triage walks Annex III(5)(b) against the BNPL credit-decisioning model and typically lands in scope.
- Sponsor-bank-program decisioning where the fintech operates the model and the bank books the loan: the fintech is the provider (in-house build), the bank is the deployer (uses under its authority on its loan book). The triage records both roles.
- Salary-advance and earned-wage-access products: the EU regulatory perimeter is patchy at member-state level; where the product is consumer credit under member-state law, Annex III(5)(b) reaches.
- Merchant-credit and SME-credit decisioning: in scope of (5)(b) only where natural-person exposure is present (sole traders, micro-enterprises whose obligations attach to a natural person).

Article 6(3) derogation analysis is rarely available for credit-decisioning models that materially influence the lending decision; the triage records the derogation analysis explicitly and typically does not invoke it.

##### 2. Fraud-detection AI: the carve-out and what it does not cover

The (5)(b) carve-out for fraud detection covers fraud detection. Payments fraud, account-takeover detection, transaction-fraud scoring, and chargeback-fraud prediction are not creditworthiness systems and do not fall under (5)(b) at all; the triage records the row as not applicable rather than relying on the carve-out.

Boundary cases the triage flags:

- Risk-rating models that combine fraud signals with credit signals into a single score that influences lending or pricing: the carve-out does not protect the credit-influencing portion of the score; the model is in scope of (5)(b) for the credit use.
- Behavioural authentication AI: not (5)(b); not typically Annex III; Article 50 transparency screened on the user-interface facts.

##### 3. PSD2 / PSD3 / PSR strong customer authentication and AI fraud

For payment institutions and credit institutions providing payment services in the EU, the strong customer authentication regime under PSD2 (and the PSD3 and PSR proposals at the time of writing) reaches the authentication surface. AI used in transaction risk analysis exemptions under Commission Delegated Regulation 2018/389 (the SCA RTS) attaches:

- The SCA TRA exemption regime is the operative governance frame for AI in payment-fraud transaction risk analysis; the AI Act high-risk regime does not attach because (5)(b) is for creditworthiness and the carve-out covers fraud detection.
- The SCA TRA model nonetheless attracts EBA Guidelines on the limited application of the SCA exemption and member-state competent-authority oversight.

The triage records the regime overlap and routes the SCA-TRA model to the firm's payments-compliance function.

##### 4. EMD / EMD2 e-money issuance and AI

For electronic-money institutions issuing e-money in the EU, AI used in onboarding, monitoring, or limit-management decisions reaches the EMI regulatory regime. AI Act high-risk classification attaches only where the use case lands in an Annex III row; for most EMI use cases, the answer is not Annex III. The triage walks the rows and records the conclusion.

##### 5. Sponsor-bank-program partnerships: EU-side exposure for US fintechs

For US fintechs in sponsor-bank-program structures with EU end-customer exposure (e.g., a US BNPL fintech offering checkout into EU merchants whose customers reside in the EU), the AI Act extraterritorial reach under Article 2(1)(c) attaches where the system's output is used in the EU. The triage records:

- The US fintech's role under the AI Act (typically provider of the credit-decisioning model used in the EU).
- The sponsor-bank's role (the US sponsor bank may not have an EU operator role; the EU-side deployer may be a separate EU entity or the analysis may turn on whether the system's output is used in the EU).
- The authorised representative obligation under Article 22 if the US fintech is a provider with EU exposure but no EU establishment; the representative is required.
- The interaction with PSD2 / E-Money Directive licensing for the EU-facing service (typically a separate workstream).

The Article 2(1)(c) extraterritorial reach is the load-bearing analysis for US fintechs without an EU establishment. The triage records the analysis on the operator-role line and routes to legal where the reach is contested.

##### 6. MiCA reach for crypto-asset service providers

For crypto-asset service providers authorised under MiCA (Regulation (EU) 2023/1114), AI used in client-onboarding, transaction monitoring, market-abuse detection (under MiCA Article 92), and ARTs / EMTs operations attaches under MiCA. The AI Act overlay attaches where any Annex III row applies (rare for typical CASP use cases) or where Article 50 transparency obligations attach to client-facing surfaces. The triage records:

- The CASP authorisation status and the MiCA obligations operative for the use case.
- Whether the CASP issues ARTs or EMTs (additional issuer obligations under MiCA Title III and IV).
- The AI Act exposure on the EU side (typically Article 50 transparency for client-facing surfaces; market-abuse detection under MiCA Article 92 runs alongside but does not displace MAR-like AI Act considerations).

##### 7. DORA reach for ICT third-party risk

For payment institutions, EMIs, credit institutions, and CASPs in scope of the Digital Operational Resilience Act (Regulation (EU) 2022/2554), AI vendor relationships are ICT third-party arrangements under DORA. The triage records:

- Whether the AI vendor is an ICT third-party service provider supporting a critical or important function under DORA.
- The DORA register-of-information entry for the AI vendor (cross-link to `dora-register-builder`).
- The DORA exit-strategy and contractual-clauses obligations for AI vendor contracts.
- The interaction with AI Act Article 26 deployer obligations on logging and monitoring (the DORA logging requirements and the AI Act logging requirements both apply; the firm operates one logging stack that satisfies both).

##### 8. Article 27 FRIA reach for credit institutions and certain private operators

Article 27(1) reaches deployers that are public bodies (Article 27(1)(a)), private entities providing public services (also under (1)(a)), credit institutions (Article 27(1)(b)), insurance undertakings ((1)(b)), and deployers using systems intended to evaluate creditworthiness or establish credit score under Annex III(5)(b) ((1)(b)). For payments and fintech entities:

- A consumer-lending fintech that is not a credit institution under EU classification: (1)(b) reaches via the Annex III(5)(b) trigger; the FRIA is required.
- A BNPL fintech under CCD II: same analysis; (1)(b) reaches via the (5)(b) trigger.
- A sponsor-bank-program structure with the credit-institution sponsor as deployer: the credit-institution arm of (1)(b) reaches the bank; the fintech is the provider but not the deployer of the (5)(b) system in the bank's loan book.

The triage records the FRIA-vs-DPIA reconciliation; the GDPR DPIA does not satisfy Article 27 on the fundamental-rights, mitigation, governance, and complaints-handling elements.

##### 9. US-side adverse-action analogue

For US-side consumer-credit reach, Reg B §1002.9 (specific principal reasons) and Comment 9(b)(2)-3 of the Official Staff Commentary reach the US-side adverse-action workflow. CFPB Circulars 2022-03 / 2023-03 are **withdrawn May 12, 2025; historical only**; the regulatory text continues to apply on its own terms. The AI Act does not directly impose a US-style obligation on the EU side, but Articles 13 (transparency to deployers) and 14 (human oversight) plus GDPR Article 22 reach the EU side of the same surface. The triage records the parallel obligations on a side-by-side block where the firm's footprint includes both jurisdictions.

##### 10. Payments-and-fintech-AI use-case categories the triage explicitly recognises

The triage labels the use-case category up front:

- Consumer-credit decisioning (BNPL, consumer-lending fintech, sponsor-bank-program credit): Annex III(5)(b) applies; FRIA via (1)(b); CCD II reach where transposed.
- Payments fraud (transaction-fraud scoring, account-takeover, chargeback-fraud): not Annex III; SCA TRA regime operative.
- KYC / onboarding AI: not Annex III; AML regime (AMLR / AMLD6 transposition) operative.
- Customer-facing chatbot or assistant: not Annex III; Article 50 transparency applies.
- Merchant-credit and SME-credit decisioning: Annex III(5)(b) applies for natural-person exposure; legal-entity-only scope routes outside (5)(b).
- Crypto-asset services AI (CASP): not Annex III typically; MiCA regime operative; Article 50 for client-facing surfaces.
- Internal productivity GenAI: not Annex III; Article 50 sub-obligations screened on the facts.
- Marketing personalisation: typically not Annex III; Article 5(1)(a) manipulation screen runs (conduct overlay) where behavioural-economics levers are in play.

#### Payments-and-fintech-specific output template additions

The triage artifact adds the following blocks when this overlay loads:

- A use-case category line at the top (per the categories above).
- An EU-extraterritorial-reach line where the firm has no EU establishment (Article 2(1)(c) analysis).
- An authorised-representative obligation line (Article 22) where extraterritorial reach attaches and no EU establishment exists.
- A sponsor-bank-program operator-role table (which entity is provider, which is deployer) where the structure applies.
- A SCA TRA regime line for payment-fraud AI use cases.
- A DORA register-and-exit-strategy line for AI vendor relationships in scope.
- A MiCA regime line for CASP use cases.
- A FRIA-vs-DPIA reconciliation note for any (5)(b) use case.
- A US-side / EU-side parallel-regime reconciliation block where the firm's footprint spans both.

#### Common pitfalls in payments-and-fintech AI Act triages

- Treating BNPL as outside consumer-credit and therefore outside (5)(b); CCD II brings most BNPL into consumer-credit scope and the triage must walk (5)(b) on the BNPL credit-decisioning surface.
- Relying on the (5)(b) fraud-detection carve-out for risk-rating models that combine fraud and credit signals; the carve-out does not protect the credit-influencing portion of the score.
- Missing Article 2(1)(c) extraterritorial reach for US fintechs serving EU end-customers without an EU establishment; the reach attaches and the authorised-representative obligation under Article 22 follows.
- Conflating the SCA TRA regime with the AI Act high-risk regime for payment-fraud AI; the SCA TRA regime is the operative governance frame; the AI Act high-risk regime does not attach.
- Skipping the FRIA on the assumption that a payment institution or BNPL fintech is not a credit institution; (1)(b) reaches via the (5)(b) trigger regardless of credit-institution classification.
- Treating sponsor-bank-program AI as the bank's problem; the fintech as provider has Article 11, 13, 14, 15 obligations on its own surface.
- Missing DORA register-of-information entries for AI vendors supporting critical or important functions; the register is operational on 17 January 2025 and the AI vendor relationship is in scope.
- Treating MiCA AI use cases as outside the AI Act because MiCA is the operative regime; Article 50 transparency reaches client-facing CASP surfaces and the screen must run.
- Asserting Article 6(3) derogation for credit-decisioning to escape high-risk classification; the derogation is rarely available for systems that materially influence credit decisions.
