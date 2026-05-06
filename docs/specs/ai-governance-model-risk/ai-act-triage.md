# ai-act-triage — Phase 1 spec sheet

Date: 2026-05-06
Plugin: ai-governance-model-risk
Phase: 1 (per-skill scoping; no SKILL.md content)

## Activation-tuned description

Triages an AI use case against the EU AI Act (Regulation (EU) 2024/1689). Determines whether the use case is prohibited (Article 5), high-risk (Article 6 with Annex I or Annex III), limited-risk with transparency obligations (Article 50), or minimal risk. Names the operator role (provider, deployer, importer, distributor, authorised representative). Lists the obligations the firm picks up at the determined classification, with specific Article and Annex references.

Best for:
- A use case has EU customer or EU operations exposure and second-line needs an AI Act classification before pre-prod or before market.
- A vendor-provided GenAI system is being deployed inside the firm and the firm needs to confirm its deployer obligations versus the provider's obligations.
- A periodic AI inventory sweep is checking which use cases are now in or out of scope after AI Act phasing dates.

Not the right tool when:
- The use case has no EU exposure at all (use ai-risk-tiering for the firm-internal tier).
- The work is the model card or validation plan once classification is settled (use model-card-builder or validation-plan).
- The work is general AI vendor due diligence (use vendor-diligence in third-party-operational-resilience with the AI vendor mode).

Anchored to: EU AI Act (Regulation (EU) 2024/1689) Article 5 (prohibited practices), Article 6 (high-risk classification), Annex I and Annex III (high-risk lists), Article 13 (transparency to deployers), Article 14 (human oversight), Article 26 (deployer obligations), Article 50 (transparency), Article 51 (general-purpose AI models), Annex IV (technical documentation), Annex VIII (registration). Phasing: Article 113 entry-into-force schedule.

## Source anchors

- EU AI Act (Regulation (EU) 2024/1689) — published in OJ 12 July 2024.
  - Article 3 (definitions, including AI system, provider, deployer).
  - Article 5 (prohibited AI practices).
  - Article 6 (classification of high-risk AI systems).
  - Annex I (Union harmonisation legislation referenced in Article 6(1)).
  - Annex III (high-risk AI systems referred to in Article 6(2)).
  - Article 9 (risk management system for high-risk AI).
  - Article 10 (data and data governance for high-risk AI).
  - Article 11 and Annex IV (technical documentation).
  - Article 13 (transparency and provision of information to deployers).
  - Article 14 (human oversight).
  - Article 15 (accuracy, robustness, cybersecurity).
  - Article 26 (obligations of deployers).
  - Article 27 (fundamental rights impact assessment for certain deployers).
  - Article 50 (transparency obligations for certain AI systems including GenAI output marking).
  - Article 51 to 55 (general-purpose AI models, including systemic-risk GPAI).
  - Article 71 (EU database registration).
  - Article 113 (entry into force and phased application dates).
- Annex IV technical documentation list — content needed for the high-risk dossier.
- Annex VIII registration content for high-risk AI systems.
- European Commission AI Pact and AI Office guidance and Q&A documents [verify dates] — practical interpretation, not authoritative.
- ISO/IEC 42001:2023 §6.1.2 and §8.1 — used to operationalise Article 9 risk management requirements (informational only, not a substitute).

## Sector overlays needed

- `references/sector-overlays/banking.md` — Annex III (5)(b) creditworthiness and credit scoring relevance; interaction with CRR/CRD and ECB guide on model risk management; deployer obligations of EU branches and subsidiaries of US banks.
- `references/sector-overlays/insurance.md` — Annex III (5)(c) life and health insurance pricing and risk assessment; Solvency II governance overlap; EIOPA AI principles. (NOTE: insurance-ai-act-triage absorbed into this skill; the insurance overlay is required.)
- `references/sector-overlays/capital-markets.md` — Article 2 exclusion analysis where MiFID II surveillance is involved; high-frequency trading algos are not in Annex III but other categories may apply (employment for staff selection, biometric for office access). (NOTE: capital-markets overlay is required.)
- `references/sector-overlays/payments-fintech.md` — Annex III (5)(b) credit scoring relevance for BNPL and consumer lending fintechs operating in or into the EU.

## Cross-cutting overlays

- `references/cross-cutting/cyber.md` — Article 15 (cybersecurity) and the interaction with NIS2 / DORA cyber obligations for high-risk AI deployed by financial entities.
- `references/cross-cutting/privacy.md` — interaction with GDPR for high-risk AI processing personal data; Article 27 fundamental rights impact assessment overlap with DPIA.
- `references/cross-cutting/conduct.md` — Article 5 prohibited practices that overlap with consumer protection (manipulative techniques, social scoring); Article 50 transparency to end users.

Climate not applicable.

## Output template named sections

1. Use case reference and EU exposure summary
2. Operator role determination (provider, deployer, importer, distributor, authorised representative)
3. Article 5 prohibited-practice screen
4. Article 6 high-risk classification (Annex I product safety route or Annex III use case route, with cited row)
5. Article 50 transparency obligations screen (GenAI output marking, deepfake disclosure, emotion recognition, biometric categorisation)
6. General-purpose AI model considerations (Article 51 to 55) where relevant
7. Obligations picked up at the determined classification, with Article references
8. Documentation deltas needed (Annex IV) for high-risk
9. Registration delta (Article 71 / Annex VIII) for high-risk
10. Phasing and applicable date (per Article 113)
11. Open questions and dissent
12. Source trace and confidence label

## Structured output fields

| Field | Type | Purpose |
|---|---|---|
| `use_case_id` | string | Links to intake record. |
| `eu_exposure` | object | Sub-fields: eu_users (bool), eu_operations (bool), eu_data_subjects (bool), market_placement (bool). |
| `operator_roles` | array of enums | One or more of `provider`, `deployer`, `importer`, `distributor`, `authorised_representative`. |
| `prohibited_screen` | object | Each Article 5 sub-practice with `applies` (bool) and `basis`. |
| `classification` | enum | `prohibited`, `high_risk_annex_I`, `high_risk_annex_III`, `limited_risk_article_50`, `minimal_risk`, `gpai`, `gpai_systemic_risk`. |
| `annex_iii_row` | string | Cited Annex III row when applicable (e.g., Annex III (5)(b)). |
| `annex_i_legislation` | string | Cited Annex I product safety legislation when applicable. |
| `transparency_obligations` | array of objects | Article 50 sub-obligation, applies, content of disclosure. |
| `obligations_summary` | array of objects | Obligation, Article reference, owner, target date. |
| `annex_iv_documentation_deltas` | array of objects | Section, current state, gap, owner. |
| `registration_required` | bool | Article 71 / Annex VIII registration required. |
| `applicable_date` | string | Earliest applicable date per Article 113 phasing. |
| `dissent` | array of objects | Reviewer, position, basis. |
| `source_trace` | array of objects | Claim, source (cite Article and Annex), evidence reference, confidence. |

## Example scenarios (public-source-derived, anonymous)

1. A US asset manager with an Irish subsidiary deploys a vendor-provided GenAI assistant to summarise pension scheme documents for EU institutional clients. Triage: deployer role (subsidiary) and provider relationship to vendor. Annex III screen: not credit scoring, not employment, not law enforcement, not essential services for natural persons in the listed sense; not high-risk. Article 50 applies (output is generated text shared with users; marking and disclosure obligations apply). Conclusion: limited-risk with Article 50 transparency obligations, Annex IV not required, no Article 71 registration. Phasing: Article 50 applicable from 2 August 2026.

2. A pan-European bank deploys an in-house ML model that ranks SME credit applications for relationship managers. Triage: provider (in-house build) and deployer. Annex III (5)(b) credit scoring of natural persons applies if SMEs include sole traders; sole traders included means high-risk. Article 9 risk management, Article 10 data governance, Article 11 and Annex IV technical documentation, Article 13 transparency to deployers, Article 14 human oversight, Article 15 robustness and cybersecurity, Article 26 deployer obligations, Article 27 fundamental rights impact assessment (deployer is a credit institution per Article 27(1)(b)) all apply. Annex VIII registration required. Phasing: high-risk obligations applicable from 2 August 2026.

## Common pitfalls

1. Confusing the firm-defined tier with the AI Act classification. The two answer different questions and may disagree (high firm tier, not high-risk under AI Act, or vice versa). Mitigation: required dual-classification line in the output, with reconciliation note.
2. Treating GenAI assistants as automatically high-risk. Article 50 transparency is the more common landing zone unless the use case lands in Annex III. Mitigation: walk Annex III row by row, cite the specific row or "no row applies" with reasoning.
3. Missing the deployer obligations on the assumption that "we are not the provider, the vendor is". Article 26 obligations are substantive (logs, oversight, risk monitoring, incident reporting). Mitigation: dedicated deployer-obligations block in the output.
4. Article 27 fundamental rights impact assessment skipped because the firm already does a DPIA. The two are not the same. Mitigation: required FRIA-vs-DPIA reconciliation when Article 27 is in scope.
5. Phasing dates ignored. The firm prepares for an obligation that does not yet apply or, worse, misses a date that has already applied. Mitigation: required `applicable_date` field with citation to Article 113.
