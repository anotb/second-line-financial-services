# Banking sector overlay for ai-act-triage

When the engagement-scope record names sector `banking`, this overlay adds banking-specific scoping, named-source reach, and parallel-regime reconciliation to the EU AI Act triage. EU branches and subsidiaries of US banks, EU-headquartered credit institutions, and EU operations of non-EU banking groups all use this overlay alongside the capability triage. Where there is conflict between the capability defaults and this overlay, the overlay governs the banking-specific elements.

Loaded by: `ai-act-triage/SKILL.md` when `engagement_scope.sector_overlay_set` includes `banking`, or when the institution type implicates a banking entity (national bank, state member bank, savings association, bank holding company, foreign banking organization with EU operations, EU credit institution, EU subsidiary or branch of a non-EU banking group). Cited and section-referenced anchors live in `references/source-anchors.md`.

## What changes for a banking triage

### 1. Annex III(5)(b) is the spine for credit decisioning

Annex III(5)(b) names "AI systems intended to be used to evaluate the creditworthiness of natural persons or establish their credit score, with the exception of AI systems used for the purpose of detecting financial fraud" as a high-risk use case. This is the most direct route to high-risk classification for banking work. The triage walks Annex III(5)(b) explicitly and records the row whether the answer is "applies" or "does not apply".

Boundary cases the triage flags:

- SME credit decisioning where SMEs include sole traders or micro-enterprises whose obligations attach to a natural person: in scope of (5)(b). Where SMEs are exclusively legal entities, the row does not apply on its face; the triage records the legal-entity-only scope and routes to legal where the firm's product perimeter includes any natural-person exposure.
- Behavioural scoring on existing customers (line management, collections triggers, dynamic credit-limit adjustment) for natural persons: in scope of (5)(b) where the score materially influences credit terms. Recorded explicitly.
- Fraud-detection AI: excluded from (5)(b) by the express carve-out. The triage records the carve-out and confirms the model's purpose is fraud detection rather than creditworthiness; where the same model serves both purposes, the carve-out does not protect the creditworthiness use.
- Consumer-credit affordability assessment: in scope of (5)(b). The triage records the firm's affordability-assessment regime alongside the AI Act analysis.

Article 6(3) derogation analysis is rarely available for credit decisioning models because the model materially influences the credit decision rather than performing a narrow procedural task. The triage records the derogation analysis explicitly and typically does not invoke it for creditworthiness use cases; flag the analysis to legal where invoked.

### 2. Annex I product-safety route is rarely the route

Annex I high-risk classification (via product-safety legislation) is the alternative high-risk route under Article 6(1). For banking AI, the route is rarely invoked; banking products are not in the Annex I product-safety lists. The triage records the screen running and the typical conclusion (Annex I not invoked).

### 3. CRR/CRD model-risk overlap and ECB guide on internal models

For credit institutions in the EU, AI use in credit risk modelling intersects with CRR/CRD model-risk expectations and, for IRB-approved institutions, the ECB Guide to internal models. The triage records the overlap and routes to the firm's internal-models function:

- IRB credit-risk models that incorporate AI elements need both the AI Act high-risk obligations (Articles 9 to 15, 26, and where applicable 27) and the CRR Part Three Title II Chapter 3 internal-models regime. The two regimes are independent; satisfying one does not satisfy the other.
- Non-IRB use of AI in credit decisioning still attracts the AI Act high-risk obligations under Annex III(5)(b); the CRR/CRD overlap depends on whether the model is in the regulatory-capital chain.
- Model-risk-management practice under the EBA Guidelines on internal governance and the ECB SREP framework provides the firm-side governance frame; the AI Act adds specific obligations on top.

The triage records the regime overlap as a side-by-side block; reviewers downstream need both lenses visible.

### 4. EU branches and subsidiaries of US banks

For US banks operating in the EU through a branch, subsidiary, or representative office, the EU entity's deployer or provider role attracts AI Act obligations on the EU side regardless of US-side model-risk practice (the joint interagency Revised Guidance on Model Risk Management, OCC 2026-13 / FRB SR 26-2 / FDIC FIL-15-2026, which in any case is scope-excluded for GenAI and agentic AI per footnote 3). The triage records:

- Which EU entity is the operator (branch, subsidiary, intermediate parent undertaking under the IPU regime).
- Which roles attach (provider, deployer, importer, distributor, authorised representative).
- The reconciliation between the US-side documentation (firm model-risk documentation per the joint interagency bulletin for traditional models, plus the firm's AI governance documentation under NIST AI RMF / NIST AI 600-1 / ISO/IEC 42001 for GenAI use cases, plus model inventory and committee evidence) and the EU-side Article 11 / Annex IV technical documentation. The two artifacts overlap substantially; the triage names the deltas the EU-side artifact must add.

A US-headquartered model used by an EU subsidiary: the EU subsidiary is the deployer. The US parent's role depends on whether the parent develops the model (provider) or simply provides the infrastructure (not provider). The triage records the analysis on the operator-role line.

### 5. Article 27 FRIA reaches credit institutions explicitly

Article 27(1)(b) names credit institutions as deployers in scope of the FRIA obligation when deploying high-risk AI systems referred to in Annex III. For an EU credit institution deploying an Annex III(5)(b) creditworthiness system, the FRIA is required. The triage records:

- The FRIA-vs-DPIA reconciliation; the GDPR DPIA does not satisfy Article 27 on the fundamental-rights-impact, mitigation, governance, and complaints-handling elements.
- The FRIA owner (typically legal in coordination with conduct or consumer-protection function).
- The FRIA evidence routing to the Article 27(3) notification to the market surveillance authority.

For non-credit-institution banking entities (e.g., a US bank operating in the EU through a branch that is not itself a credit institution under EU classification), the Article 27(1)(b) reach is on the facts; the triage routes to legal.

### 6. Adverse-action and explainability reach (CFPB Circulars analogue)

Where the firm has US-side consumer-credit reach (US parent or US subsidiary), the CFPB Circulars on adverse-action notification (2022-03 and 2023-03) reach the US-side adverse-action workflow. The EU AI Act does not directly impose a CFPB-style adverse-action obligation, but Articles 13 (transparency to deployers) and 14 (human oversight) plus the GDPR Article 22 (automated decision-making affecting the data subject) reach the EU side of the same surface.

The triage records the parallel obligations on a side-by-side block where the firm's footprint includes both jurisdictions; the artifact does not collapse the two analyses.

### 7. AML and BSA models: the financial-fraud carve-out and what it does not cover

The Annex III(5)(b) carve-out for fraud detection covers fraud detection. AML transaction-monitoring, sanctions screening, customer-risk-rating, and PEP screening are not creditworthiness systems and do not fall under (5)(b) at all; the triage records the row as not applicable rather than relying on the carve-out.

For the EU side, the EBA Guidelines on ML/TF risk factors and the AMLR / AMLD6 transposition reach the AML model on a different track. The triage records the AML regime as the operative governance frame and notes that the AI Act high-risk obligations do not attach to AML models on the (5)(b) row; other Annex III rows do not typically reach AML either. The triage walks the rows and records the conclusion.

### 8. CCAR/DFAST and stress-testing model overlap

For US bank holding companies subject to stress testing, AI elements in stress-projection or allowance models attract SR 15-18 (or successor) US-side documentation. EU subsidiaries of the same group may operate under EBA stress-testing methodology. The AI Act overlay attaches Annex III high-risk classification only where the model is in scope of an Annex III row (typically (5)(b) for natural-person creditworthiness elements within the stress projection). The triage records the cross-walk and routes to the firm's stress-testing owner.

### 9. Supervisory-relationship cadence

For EU credit institutions, the AI Act supervisor is the relevant member-state competent authority designated under Article 70, plus the AI Office for cross-cutting matters and GPAI provider supervision. The triage records:

- The named NCA in the operating member state.
- The interaction with the prudential supervisor (ECB for SSM-supervised institutions; member-state competent authority for less-significant institutions). The prudential supervisor and the AI Act NCA may be the same body, may be sister bodies, or may be different agencies depending on member-state designation. The triage names both and records the coordination posture where designation is split.

For OCC-, FRB-, FDIC-, or NCUA-supervised US parents, the US-side supervisor is unaffected by the AI Act analysis; the triage records the US-side supervisory relationship for completeness.

### 10. Banking-AI use-case categories the triage explicitly recognises

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

## Banking-specific output template additions

The triage artifact adds the following blocks when this overlay loads:

- A use-case category line at the top (origination credit decisioning / SME credit / behavioural scoring / fraud / AML / customer chatbot / internal productivity / marketing personalisation / IRB credit-risk).
- An EU-entity operator-role table (which EU entity, which role) for cross-border banking groups.
- A CRR/CRD internal-models overlap line for IRB use cases.
- A US-side / EU-side parallel-regime reconciliation block where the firm's footprint spans both (joint interagency model-risk bulletin and AI-specific frameworks to Article 11 / Annex IV mapping; CFPB Circulars to GDPR Article 22 mapping).
- An NCA-and-prudential-supervisor coordination line when designation is split or unclear.
- A FRIA-vs-DPIA reconciliation note for any (5)(b) or other Article 27 trigger.
- An AML-regime routing note where the use case is AML-adjacent and (5)(b) does not apply.

## Common pitfalls in banking AI Act triages

- Treating (5)(b) as covering all banking credit work; the row is for natural-person creditworthiness and credit scoring with the fraud-detection carve-out, not all credit-related models.
- Skipping the FRIA because the firm has a DPIA; Article 27 reaches credit institutions deploying Annex III high-risk and the DPIA does not cover the FRIA elements.
- Importing SR 11-7 documentation as Annex IV evidence without delta analysis; the artifacts overlap but Annex IV has specific elements (intended purpose, hardware and software, data, methodology, testing, human oversight design, post-market monitoring) that the firm's SR 11-7 documentation may not carry in Annex IV form.
- Conflating the AI Act NCA with the prudential supervisor; designation may be split and coordination is on the firm to manage.
- Treating fraud-detection models as exempt from all AI Act analysis under the (5)(b) carve-out; the carve-out is from (5)(b) only. Other Annex III rows and Article 50 transparency screen separately.
- Missing the IRB / internal-models overlap for credit-risk models that feed regulatory capital; the AI Act and the CRR/CRD regimes are independent and both apply.
- Asserting Article 6(3) derogation for credit decisioning to escape high-risk classification; the derogation is rarely available for systems that materially influence credit decisions.
- Treating EU subsidiaries' AI Act obligations as automatically discharged by US parent's model-risk practice; the EU entity's deployer or provider role attracts EU-side obligations on its own facts.
