# llm-vendor-evidence-review — Phase 1 spec sheet

Date: 2026-05-06
Plugin: ai-governance-model-risk
Phase: 1 (per-skill scoping; no SKILL.md content)
Status: NEW for v1 (GenAI expansion).

## Activation-tuned description

Reviews a large-language-model vendor's published evidence (system card, model card, evaluation reports, red-team results, responsible-scaling or use-policy documents, security and privacy attestations) against firm criteria. Produces a sufficiency view, named gaps, supplemental evidence requested, and the residual reliance the firm is taking. The artifact a model risk lead, AI risk committee, or vendor-diligence officer uses to decide whether to depend on a foundation model in scope. Companion to vendor-diligence in third-party-operational-resilience: this skill goes deep on the model-evidence layer; vendor-diligence handles entity-level diligence.

Best for:
- A new foundation-model vendor is being onboarded for one or more in-scope use cases.
- A foundation-model provider has published a new system card or model version and the firm needs the delta review.
- A periodic re-attestation cycle requires updated evidence-pack review for in-flight vendor models.

Not the right tool when:
- The work is entity-level vendor diligence (financial health, security attestations, contracts) — use vendor-diligence in third-party-operational-resilience with the AI vendor mode.
- The vendor is in-house or open-source and there is no published system card (use validation-plan; the deep work on a model that the firm controls is internal validation, not vendor-evidence review).
- The work is the deployment-level pre-prod gate (use genai-pre-prod-review; this skill feeds it).

Anchored to: NIST AI RMF 1.0 Govern 6.1 (third-party considerations); NIST AI RMF Generative AI Profile (NIST AI 600-1) Govern 6.x and Manage 3.x (third-party / foundation-model considerations); ISO/IEC 42001:2023 §7.4 (communication) and §8.x (operational controls including supplier obligations); SR 11-7 §VI (vendor and third-party models); OCC Bulletin 2026-13 (revised interagency model risk management guidance, 2026) [verify section on third-party AI]; US interagency third-party risk management guidance (2023) for the entity-level wrapper. Pattern reference: Anthropic Claude system cards, OpenAI system cards, Google Gemini cards as the public form factor for the evidence under review.

## Source anchors

- SR 11-7 §VI — vendor and third-party models, including expectations on validation evidence from vendors.
- OCC Bulletin 2026-13 (revised interagency model risk guidance, 2026) [verify section] — refreshed expectations including AI/ML and GenAI vendor evidence.
- US interagency third-party risk management guidance (June 2023) — informational reference for the entity-level wrapper around the evidence-pack review.
- NIST AI RMF 1.0 Govern 6.1 (third-party considerations).
- NIST AI RMF Generative AI Profile (NIST AI 600-1) — Govern 6.x and Manage 3.x: foundation-model provider considerations, including system-card review, dangerous-capability evaluations, content-provenance, and incident-disclosure expectations [verify exact subcategory numbering].
- ISO/IEC 42001:2023 §7.4 (communication including supplier-side obligations), §8.1 (operational planning), §8.3 (AI system lifecycle controls).
- EU AI Act Articles 51 to 55 (general-purpose AI models, including systemic-risk GPAI documentation and information-sharing obligations) — informational where the model is a GPAI under the EU AI Act.
- NYDFS Industry Letter on Cybersecurity Risks Arising from AI (October 2024) — third-party AI cyber expectations for covered entities.
- Public model and system card precedents — pattern reference only:
  - Anthropic Claude system cards.
  - OpenAI system cards (e.g., GPT-4 / GPT-4o / o-series system cards).
  - Google Gemini cards.
  These are the public form factor for the evidence pack the firm reviews. The skill does not endorse specific vendors; the references illustrate the documentation pattern.

## Sector overlays needed

- `references/sector-overlays/banking.md` — bank-vendor expectations (regulator visibility, exam evidence, audit rights, exit posture); SR 11-7 §VI alignment.
- `references/sector-overlays/insurance.md` — insurance-vendor expectations (state department visibility, NAIC Model Bulletin alignment, fairness-evidence expectations).
- `references/sector-overlays/capital-markets.md` — broker-dealer / investment-adviser vendor expectations (FINRA, SEC visibility, surveillance and execution adjacency).
- `references/sector-overlays/payments-fintech.md` — sponsor-bank visibility, BSA program coverage of vendor.

## Cross-cutting overlays

- `references/cross-cutting/cyber.md` — primary overlay. NYDFS October 2024 alignment; vendor cyber attestations (SOC 2, ISO 27001) and AI-specific cyber posture (red-team scope, prompt-injection testing, content-provenance).
- `references/cross-cutting/privacy.md` — vendor data-handling attestations; training-data sourcing posture; opt-out and confidentiality posture.
- `references/cross-cutting/conduct.md` — vendor responsible-use posture; harmful-content and misuse policies; restricted-use enforcement.

Climate not applicable.

## Output template named sections

1. Vendor and model metadata (vendor, model, version, evidence-pack date, scope of in-firm use cases)
2. Evidence inventory (named documents reviewed, with date and source URL where public)
3. Sufficiency view by criterion (intended-use scope, training-data posture, evaluation coverage, dangerous-capability evaluations, red-team coverage, security and privacy posture, content-provenance, incident-disclosure history, support and escalation, regulator-engagement history, change and version control)
4. Named gaps (criterion, gap, severity, supplemental evidence requested, owner)
5. Residual reliance (what the firm is relying on the vendor for, with named caveats)
6. Recommended owner actions (gaps to close, deadlines)
7. Re-review triggers (named events that require a re-review: model-version swap, new system card, incident, regulatory change)
8. Source trace and confidence label

## Structured output fields

| Field | Type | Purpose |
|---|---|---|
| `vendor` | string | Vendor name. |
| `model` | string | Model name and version. |
| `evidence_pack_date` | string | ISO date of the evidence pack reviewed. |
| `in_firm_use_cases` | array of strings | Use case IDs in scope of this evidence review. |
| `evidence_inventory` | array of objects | Each: document, date, source_url (if public), confidentiality. |
| `sufficiency_view` | array of objects | Each: criterion, status (sufficient/partial/insufficient/missing), basis, evidence_ref. |
| `gaps` | array of objects | Each: criterion, gap, severity, supplemental_evidence_requested, owner, deadline. |
| `residual_reliance` | array of objects | Each: reliance, caveat, accepted_owner. |
| `recommended_actions` | array of objects | Each: gap, owner, deadline, severity. |
| `rereview_triggers` | array of strings | Named events. |
| `source_trace` | array of objects | Claim, source, evidence reference, confidence. |

## Example scenarios (public-source-derived, anonymous)

1. A US bank reviews the evidence pack from a major foundation-model vendor for use in a tier-1 KYC assistant. Evidence inventory: vendor system card (public, dated), model card (public, dated), evaluation report on hallucination and harmful content (public), red-team summary including prompt-injection scope (public), trust centre attestations (SOC 2, ISO 27001 — confidential under NDA), responsible-use policy and acceptable-use rules (public). Sufficiency view: intended-use scope sufficient, evaluation coverage sufficient on hallucination but partial on financial-services-specific harmful content, red-team coverage sufficient on direct injection but partial on indirect injection over enterprise-corpora, content-provenance partial (provider does not yet provide watermarking for the model in question). Gaps: financial-services-specific harmful content expansion requested as supplemental evidence; indirect-injection adversarial coverage requested. Residual reliance: firm relies on vendor's hallucination-rate posture for the assistant's intended use; caveat is that the firm runs in-flight monitoring and reserves the right to swap-revalidate on any vendor-disclosed incident.

2. A regional life insurer reviews the evidence pack from a vendor providing a smaller open-weights model that the firm runs on its own infrastructure for the claims summarisation pilot. Evidence inventory: vendor model card (public, dated), evaluation report (public), responsible-use policy (public), training-data disclosure (public, partial). Sufficiency view: training-data disclosure partial (provider lists data categories but not all sources), evaluation coverage partial (no PHI-specific evaluation, expected for a general-purpose model), security and privacy posture not directly applicable since the firm runs the model on its own infrastructure (firm posture takes over). Gaps: training-data disclosure expansion requested but accepted-as-best-available given the open-weights posture; in-firm PHI-specific evaluation required and is in scope of validation-plan. Residual reliance: firm relies on the vendor's published model card and shifts most validation responsibility in-house; caveat is documented at the gate review.

## Common pitfalls

1. The review treats vendor evidence as authoritative without a sufficiency view. The firm inherits the vendor's posture without naming what the firm is relying on. Mitigation: required sufficiency view by criterion, with explicit residual reliance.
2. Public evidence is taken as evidence of what the firm needs without testing the in-firm fit. A general-purpose hallucination evaluation is not the same as the firm's domain. Mitigation: each criterion's basis must reference what the in-firm use needs, not just the vendor's general claims.
3. Re-review triggers are missing. The vendor publishes a new system card or swaps the model and the review is stale. Mitigation: required `rereview_triggers` field with at least version-swap and new-system-card listed.
4. Confidential evidence (NDA-bound) is read but not recorded as confidential in the inventory. The audit trail leaks. Mitigation: confidentiality field on each evidence-inventory entry.
5. The skill is used for entity-level vendor diligence (financial health, contract, exit posture) and ignores model-evidence depth, or vice versa. Mitigation: the description's not-the-right-tool block makes the boundary explicit; this skill is the model-evidence layer; vendor-diligence handles the entity layer.
