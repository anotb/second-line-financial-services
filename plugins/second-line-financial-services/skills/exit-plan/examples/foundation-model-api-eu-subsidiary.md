## Example: foundation-model API exit plan at an EU subsidiary

Public-source-derived. No named vendor or firm. The shape mirrors a DORA-in-scope arrangement at a credit-institution EU subsidiary using a foundation-model API for KYC narrative summarisation in the AML investigations workflow.

## Input

- **Vendor**: a non-EU foundation-model API provider with an EU data-residency commitment, a published system card, and an enterprise data-handling addendum.
- **Service**: foundation-model API consumed by the firm's AML case-management system to summarise narrative artefacts (transaction-explanation memos, customer-correspondence excerpts, public-source notes) for AML investigators.
- **Business process supported**: AML investigations and SAR-narrative drafting support.
- **Important business service**: financial-crime investigations (firm IBS map names a tolerance for investigator workflow disruption).
- **Inputs already on file**: vendor-diligence record (criticality = important; subcontractors include the upstream cloud providers; data_access includes model-prompts containing customer name, narrative excerpts, and identifiers; residual risk = medium; exit_plan_status = draft); the executed enterprise contract carrying training-use disabled by default with a 30-day abuse-monitoring exception; system card and trust-and-safety pages on file; `llm-vendor-evidence-review` record open with `eval_evidence_status = deferred-to-evidence-review`.
- **Engagement scope supplied**: institution = credit-institution EU subsidiary; primary regulators = ECB SSM, national competent authority; persona = head of operational resilience; source posture = public-plus-firm-policy; sector overlay = banking; cross-cutting overlays = cyber, privacy.
- **DORA in scope**: true. The arrangement supports a function the firm has classified as critical or important under DORA Article 28(8); Article 30(3) [verify subarticle] expects exit-strategy and transitional-support clauses in the contract.
- **AI vendor**: true.

## Output sketch

The skill produces an exit plan. Headlines:

- **Triggers** — vendor-driven (vendor-side enterprise terms change, model deprecation, prolonged regulator-driven service restriction in non-EU jurisdiction); firm-driven (model-risk-committee decision to switch vendors after eval drift, AI-policy-driven retirement of the use case); regulator-driven (DORA-driven supervisory direction, EU AI Act-driven obligation that the vendor cannot meet, customer-data-incident at the vendor with EU regulator-led action); market-driven (vendor distress, geopolitical sanctions affecting the vendor's home jurisdiction, hyperscaler-region disruption).
- **Transition target options** — substitute-vendor as primary (substitute-foundation-model with portable prompt-template library and sanitised RAG corpus, viability `viable` only after prompt-template portability and RAG corpus migration are tested; in-source as `weak` because the firm has no GPU capacity for a self-hosted model of comparable capability; retire-service-and-fall-back-to-pre-AI-investigator-workflow as `viable` for transitional use, viability `viable` as a graceful-degradation option). Selected primary: substitute-vendor; secondary: graceful-degradation to pre-AI workflow.
- **Time-to-transition vs tolerance** — `near`. Substitute-vendor cutover is months not weeks; graceful-degradation cutover is days because the pre-AI workflow still exists. Within tolerance under graceful-degradation; near-tolerance under substitute-vendor cutover.
- **Data return and destruction** — prompts, completions, and any vendor-side abuse-monitoring retention must be returned and destroyed; vendor must provide a destruction certificate covering the abuse-monitoring window and any logs; encryption-key revocation and credential rotation choreographed against cutover.
- **AI-specific transition considerations** — prompt-template portability is unproven (templates have only ever been engineered against the incumbent model); RAG corpus migration requires re-embedding and re-indexing because vector spaces are model-specific; fine-tune artifacts are not in scope for this use case; model-version pin handling driven by vendor's deprecation-notice clock; carrier-side guardrails (PII redaction at prompt entry, output-quality gates) need rework on the substitute model; agent tool offboarding not applicable (no agent integration in scope).
- **Knowledge transfer** — prompt library, evaluation harness, prompt-template engineering decisions, redaction-rule library all owned firm-side; vendor knowledge transfer covers operational integration only.
- **Contract termination mechanics** — clause reference cited; termination-for-convenience present; transition-assistance period limited to API access continuity; regulator-directed-termination clause absent — flag to `contract-gap-review` because DORA Article 30(3) [verify subarticle] expects this; in-flight data lock-in low because deployment is stateless other than the abuse-monitoring window.
- **Customer notice posture** — no customer-facing change at cutover (the AI is in the investigator workflow, not customer-facing). No regulated customer-notice clock applies.
- **Regulator notice posture** — DORA Article 28 [verify subarticle] register-of-information update on the substitute vendor required; ECB SSM notification posture per the firm's significant-incident reporting policy where exit triggers on a vendor incident; supervisory engagement on the model-risk-committee-driven switch.
- **Supervisory readiness during transition** — model-risk evidence carries over (the model-risk evaluation lives in the firm's MRM, not at the vendor); evidence of evaluation on the substitute model required before cutover; the substitute model's diligence pack and `llm-vendor-evidence-review` record both required as preconditions.
- **Fourth-party dependencies** — vendor's upstream compute provider is not the firm's choice; geopolitical exposure on the upstream provider feeds the trigger set.
- **Testing plan** — quarterly tabletop with model-risk and TPRM functions; annual rehearsal of switching vendors for a low-risk subset of prompts (sandboxed); data-extraction rehearsal annually. `last_test_date = none`, `last_test_outcome = never-tested`.
- **Cost estimate range** — moderate range; cost drivers named (prompt re-engineering effort, RAG re-embedding, evaluation re-baselining, dual-vendor period).
- **Approver** — head of operational resilience and head of model risk jointly; reviewer questions clustered for the AI risk committee.

The plan stops at the recommendation.

## Why this scenario matters

- **DORA Article 28(8) is the primary anchor.** The exit-strategy expectation drives the plan's existence; the contract gap on Article 30(3) [verify subarticle] exit-strategy clauses gets surfaced and chained to `contract-gap-review`.
- **Prompt and RAG portability is the AI-specific transition-engineering problem.** A non-AI exit plan would treat data extraction as schema mapping; an AI vendor exit plan must address prompt re-engineering and re-embedding because vector spaces and model behaviour are model-specific.
- **Graceful degradation is a real option for AI vendors.** The pre-AI investigator workflow still exists; treating it as a fallback keeps the impact tolerance achievable under any forced cutover.
- **The substitute vendor's diligence is a precondition, not an afterthought.** A new model vendor needs its own `vendor-diligence` record and `llm-vendor-evidence-review` record before cutover.
- **Customer notice does not always apply.** AI used in investigator workflows triggers no customer-facing notice clock. Regulator notice still applies via DORA register update and SSM-level supervisory engagement.

## Anchors

- DORA, Regulation (EU) 2022/2554, Article 28(8) exit strategies [verify subarticle] and Article 30(3) exit-related contractual provisions [verify subarticle].
- EBA Guidelines on outsourcing arrangements (EBA/GL/2019/02), exit-strategy section [verify section].
- NIST AI Risk Management Framework 1.0 (NIST AI 100-1, January 2023), Govern function [verify subsection].
- NIST AI 600-1, Generative AI Profile (July 2024) [verify subsection].
- EU AI Act, Regulation (EU) 2024/1689 [verify Annex III item number where applicable].

See `references/source-anchors.md` for full citations.
