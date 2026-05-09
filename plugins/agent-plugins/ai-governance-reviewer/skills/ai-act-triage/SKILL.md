---
name: ai-act-triage
description: |
  Classifies an AI use case under the EU AI Act (Regulation (EU) 2024/1689) and produces the obligations the firm picks up at the resulting classification. Walks Article 5 prohibited practices, Article 6 high-risk via Annex I product safety legislation or Annex III listed use cases, Article 50 transparency, GPAI Articles 51 to 55, and the operator role determination (provider, deployer, importer, distributor, authorised representative). Output is a draft triage decision plus an obligations checklist, stopped at the legal/compliance review gate.

  Best for:
  - A use case has any EU touch-point (EU users, EU establishment, EU data subjects, market placement) and second-line needs an AI Act classification before pre-prod or before market.
  - A vendor-supplied GenAI assistant is being deployed inside the firm and the firm needs the deployer-versus-provider boundary written down before signing.
  - An AI inventory sweep is checking which use cases are in scope as Article 113 phasing dates land.
  - Legal or compliance is challenging an existing classification and the file needs the row-by-row screen, not a one-liner.

  Not the right tool when:
  - The use case has no EU exposure at all (route to ai-risk-tiering for the firm-internal tier; the AI Act question does not arise).
  - The intake record is missing (route to ai-use-case-intake first; triage runs against a use-case record, not against a hallway description).
  - The artifact required is the Annex IV technical documentation itself (use model-card-builder for the firm-side card; this skill scopes the Annex IV deltas).
  - The work is generic third-party diligence on the vendor (use third-party-operational-resilience vendor diligence with the AI vendor mode).
argument-hint: "[use-case ID, intake record, vendor system card, scope record, or scope statement]"
---

# AI Act triage

The EU AI Act classifies AI systems by the risk they pose. The firm needs to know which class the use case sits in before it builds, buys, deploys, or markets, because the obligations cascade from the class. This skill walks the classification and records the obligations on a single auditable file.

The triage is a draft. The skill stops at legal and compliance review. Operator-role determination, Article 5 screens, Annex III row reads, GPAI thresholds, and Article 113 phasing all hand off to qualified counsel before anything is filed, declared, or relied on for market-placement decisions. This is not legal advice and the artifact says so.

The skill answers four questions in order: does the AI Act apply at all (Article 2 territorial and material scope), what role does the firm play (Article 3 definitions), what classification fits (prohibited, high-risk via Annex I or Annex III, limited-risk transparency, minimal, GPAI, GPAI with systemic risk), and what obligations attach. Each answer is sourced. Each unsourced item is `[evidence needed]` and goes to the engagement issue log.

## Ask first

A handful of facts decide most of the work. If they are not on the table, draft against what is given and flag the defaults.

- Is there any EU touch-point. EU users of the output, EU establishment operating the system, EU data subjects whose data is in scope, or market placement / putting into service in the EU. Article 2 governs scope; one of these is enough to bring the use case in.
- Who built it, who runs it, who imports it. The provider-versus-deployer line is the biggest single source of misclassified obligations. A firm that fine-tunes a vendor model picks up provider obligations for the fine-tuned variant under Article 25; a firm that only consumes a vendor system stays in the deployer lane under Article 26. Naming every operator role for every entity is the audit trail.
- What does the system actually do. Annex III reads against the listed use case, not against the marketing description. "AI assistant" is not a row. "Creditworthiness assessment of natural persons" is a row (Annex III(5)(b)). Force the use case into the Annex's vocabulary before deciding.
- Where is the use case in lifecycle. Pre-build triage scopes obligations early. Pre-prod triage gates the deployment. Post-market triage updates the classification when the system, the data, or the law changes (foundation-model swap, Annex III amendment, Article 113 date landing).
- What is the scope record saying. Sector and cross-cutting overlays load from the scope. The skill does not guess sector.

When the scope record is supplied, the skill consumes it for institution profile, persona, source posture, sector overlays (banking, insurance, capital-markets, payments-fintech), and cross-cutting overlays (cyber, privacy, conduct). Without a scope record the skill asks the practitioner the few facts it needs and proceeds against partial input.

## How the triage walks

Five passes, in order. Skipping a pass on the assumption the answer is obvious is the most common defect; the artifact records every pass, including the ones that do not apply.

**Article 2 scope and operator role.** EU touch-points are enumerated against `eu_exposure` (eu_users, eu_operations, eu_data_subjects, market_placement). At least one true brings the use case into scope; all false ends the triage with a "no AI Act exposure" record and a route to firm-internal tiering. Operator roles per Article 3 are enumerated for every entity in the chain: provider, deployer, importer, distributor, authorised representative. A firm holding multiple roles is the rule, not the exception. Vendor-built plus firm-fine-tuned plus firm-deployed picks up provider obligations under Article 25 for the fine-tuned variant, deployer obligations under Article 26 for the deployment, and importer obligations where the upstream entity is non-EU.

**Article 5 prohibited-practice screen.** Each sub-practice is screened on the record: subliminal or manipulative techniques, exploitation of vulnerabilities, social scoring, real-time remote biometric identification in publicly accessible spaces (limited exceptions for law enforcement), predictive policing based on profiling, untargeted scraping for facial recognition databases, emotion inference in workplace and education (with narrow exceptions), biometric categorisation inferring sensitive attributes. Most financial-services use cases land at "does not apply" across the row; the artifact says so explicitly. Where a sub-practice does apply, the use case is prohibited and the artifact stops at "do not build, do not deploy, route to legal" rather than recommending mitigation.

**Article 6 high-risk classification.** Two routes, walked separately. Route A (Article 6(1) plus Annex I) covers AI systems that are safety components of products covered by Annex I Union harmonisation legislation; rare in financial services, common in adjacent product engineering. Route B (Article 6(2) plus Annex III) walks the listed high-risk use cases row by row. The financial-services-relevant rows are Annex III(5)(b) creditworthiness assessment and credit scoring of natural persons (excluding fraud detection), Annex III(5)(c) risk assessment and pricing for life and health insurance, Annex III(1) biometric identification and categorisation, Annex III(4) employment for staff selection, Annex III(2) critical infrastructure where applicable. Each row is recorded as applies / does not apply with one-line reasoning. Article 6(3) carve-outs (narrow procedural task, improving prior human work, detecting decision-making patterns without replacing human decisions, preparatory tasks) are screened where they could pull a use case back from high-risk; the burden of demonstrating the carve-out sits with the provider and the artifact records the basis.

**Article 50 transparency screen.** Independent of high-risk; a system can be limited-risk-with-transparency, or high-risk-and-also-limited-risk-transparency. The four obligations are walked on the record: AI-system interaction disclosure to natural persons (Article 50(1)), synthetic content marking for AI-generated audio, image, video, or text content (Article 50(2)), deepfake disclosure (Article 50(4) first paragraph), and disclosure for text published to inform the public on matters of public interest (Article 50(4) second paragraph). Emotion recognition and biometric categorisation systems carry their own Article 50(3) disclosure obligation. The "GenAI assistant" that lands at limited-risk usually picks up Article 50(1) plus Article 50(2) plus, where the output is published to customers, the relevant Article 50(4) obligation.

**GPAI screen (Articles 51 to 55).** General-purpose AI models carry their own obligation regime upstream of any deployment. The firm is rarely the GPAI provider in financial services, but is frequently the deployer of a GPAI-based system. The screen records whether a GPAI model is in the chain, whether it meets the systemic-risk threshold under Article 51(2) (the 10^25 FLOP training compute presumption is the published threshold; the AI Office may designate other systemic-risk models), and whether the firm picks up upstream-provider obligations for any fine-tuning that crosses the modification threshold per Article 25.

After the five passes, the artifact records the classification (prohibited, high_risk_annex_I, high_risk_annex_III, limited_risk_article_50, minimal_risk, gpai, gpai_systemic_risk; multi-classification is allowed where high-risk and Article 50 both apply) and enumerates obligations per Article reference, owner role, and target date. Annex IV documentation deltas, Article 71 / Annex VIII registration requirement, Article 27 fundamental-rights impact assessment trigger (where the deployer is a public body, a private operator providing public services, or a credit institution or insurer providing the listed services), and the Article 113 applicable date are each captured as named fields.

## Quality bar

The triage is only credible when these hold:

- Every classification claim cites Article and Annex (or `[verify section]`). Unsourced claims do not enter the artifact.
- The Annex III screen runs row by row, including rows that do not apply. The audit trail is the deliverable; a reviewer in two years' time should see every row was screened.
- The provider-versus-deployer line is enumerated for every entity in the chain. "We are not the provider" is not a sufficient basis to skip Article 25 (substantial modification) or to assume Article 26 deployer obligations are light. Article 26 is substantive: logs (paragraph 6), human oversight (paragraph 2), input-data quality (paragraph 4), serious-incident reporting (paragraph 5), data subject information (paragraph 11), workplace deployment information to workers (paragraph 7).
- Article 27 FRIA is not the GDPR DPIA. Where Article 27 is in scope, the artifact carries an explicit FRIA-versus-DPIA reconciliation note. Legal owns the reconciliation; the skill flags it.
- Article 113 phasing dates are recorded against each obligation. Article 5 prohibited-practice obligations, GPAI obligations, transparency obligations, and high-risk obligations apply on different dates. Missing this puts the firm either ahead of an obligation or, the worse failure, behind one that has already applied.
- No named institutions outside finalised public enforcement actions; examples are anonymised and public-source-derived.
- The triage does not reach a final regulatory determination. The artifact reads "draft for legal/compliance review" on the cover and the schema's `triage_metadata.legal_reviewer` is required before downstream skills consume the record.

## Adaptation

Source posture sets what can be asserted at high confidence and what carries `[evidence needed]`. Sector and cross-cutting overlays load from the scope. Persona sets the review path: an in-house AI governance lead routes to the AI risk committee; an advisory engagement routes to partner approval and counsel sign-off.

## Sector and cross-cutting overlays

Loaded only when the scope names them. Gold-plating with overlays the engagement does not implicate adds noise without challenge value.

- Banking: Annex III(5)(b) for credit scoring of natural persons; sole-trader inclusion is the typical boundary call. Interaction with CRR/CRD model governance (informational); ECB guide on internal models is cited where applicable. EU branches and subsidiaries of US banks pick up deployer obligations on EU-deployed systems.
- Insurance: Annex III(5)(c) for life and health pricing and risk assessment of natural persons. Solvency II governance overlap noted; EIOPA AI principles are non-binding and cited as such. P&C, group, and reinsurance boundary calls per the insurance overlay.
- Capital markets: Article 2 exclusion analysis where the AI system is a MiFID II surveillance tool; high-frequency trading algos are not in Annex III but other rows may apply (Annex III(4) employment for staff selection, Annex III(1) biometric for office access).
- Payments-fintech: Annex III(5)(b) credit scoring relevance for BNPL and consumer-lending fintechs operating into the EU.
- Cyber cross-cutting: Article 15 robustness and cybersecurity interaction with NIS2 and DORA Articles 5 to 14 ICT risk management for high-risk AI deployed by financial entities.
- Privacy cross-cutting: GDPR interaction for high-risk AI processing personal data; Article 27 FRIA versus GDPR Article 35 DPIA reconciliation.
- Conduct cross-cutting: Article 5 manipulative techniques and social-scoring screens overlap with consumer-protection regimes; Article 50 end-user transparency overlaps with conduct disclosures.

Climate is not applicable to AI Act triage.

## Output

Default to drafting the triage record against `templates/default-output.md`. Render as Word for legal/compliance review or another format the audience asks for. Produce the structured record at `schemas/ai-act-triage.schema.json` when downstream skills (`model-card-builder` for Annex IV deltas, `genai-pre-prod-review` for Article 26 obligations, `llm-vendor-evidence-review` for the GPAI screen, `board-ai-risk-pack`) need it. The legal/compliance reviewer block is filled by a human; the triage is filed only after.

Downstream consumers: `model-card-builder` pulls the Annex IV documentation deltas to scope the firm-side card. `genai-pre-prod-review` pulls the Article 50 transparency obligations and the Article 26 deployer obligations into its gate. `llm-vendor-evidence-review` pulls the operator-role determination and the GPAI screen. `board-ai-risk-pack` pulls classification, applicable date, and material open questions. The `ai-governance-reviewer` agent pulls the structured object for second-line challenge. The schema is the input contract; additive changes only, never silent renames.

## Pointers

- `references/source-anchors.md` — citations and section-referenced excerpts for every primary anchor.
- `references/sector-overlays/{banking,insurance,capital-markets,payments-fintech}.md` — sector overlays loaded from scope. The insurance overlay carries the substance of the deprecated `insurance-ai-act-triage` skill.
- `references/cross-cutting/conduct.md` — conduct overlay (cyber and privacy cross-cutting overlays sit in the broader plugin reference set; load when the scope names them).
- `references/firm-overlay.md` — firm policy, taxonomy, named legal/compliance owners (consumed when present).
- `templates/default-output.md` — triage record template.
- `schemas/ai-act-triage.schema.json` — structured-output contract.
- `examples/` — public-source-derived anonymised scenarios (insurance pricing high-risk path; internal tool minimal-risk path).
- `TROUBLESHOOTING.md` — recurring defects in triage records.
