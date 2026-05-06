---
name: llm-vendor-evidence-review
description: |
  Reviews a foundation-model vendor's published evidence pack (system card, model card, evaluation reports, red-team summaries, security and privacy attestations, responsible-use policies, trust-and-safety pages) against firm criteria for the firm's deployment context. Produces a sufficiency view, named gaps with supplemental evidence requested, residual reliance with caveats, recommended owner actions, and re-review triggers. The artefact a model risk lead, AI risk committee, or vendor-diligence officer uses to decide whether to depend on a foundation model in scope. The model-evidence layer that pairs with vendor-diligence in third-party-operational-resilience for the entity-level wrapper.

  Best for:
  - A new foundation-model vendor is being onboarded for one or more in-scope use cases and the model-evidence layer is needed for the deployment-context decision.
  - A foundation-model provider has published a new system card, model variant, or version and the firm needs the delta review.
  - A periodic re-attestation cycle requires updated evidence-pack review for in-flight vendor models.
  - An upstream vendor-diligence record has set eval_evidence_status to deferred-to-evidence-review and chained the model-evidence question over.

  Not the right tool when:
  - The work is entity-level vendor diligence (financial health, security attestations as entity-level evidence, contract terms, exit posture, sub-contractor footprint). Use vendor-diligence in third-party-operational-resilience.
  - The vendor model is in-house or open-source with no published vendor evidence pack (the deep work is internal validation under validation-plan).
  - The work is the deployment-level pre-prod gate; this skill feeds genai-pre-prod-review.
  - The work is the focused prompt-injection deep-dive on the deployed system (use prompt-injection-risk).

  Anchored to: US interagency model risk guidance, US interagency third-party risk-management guidance, NIST AI RMF and the Generative AI Profile, ISO/IEC 42001, EU AI Act provisions on general-purpose AI models, NYDFS cyber expectations on third-party AI, SOC 2 and ISO/IEC 27001 third-party attestation form-factors, and public foundation-model provider system-card and model-card pattern references. Citations and excerpts live in `references/source-anchors.md`.
argument-hint: "[vendor, model, version, deployment form, in-firm use case IDs, evidence pack scope, or pointer to upstream vendor-diligence record where eval_evidence_status = deferred-to-evidence-review]"
---

# LLM vendor evidence review

The work this skill produces is the second-line read of a foundation-model vendor's published evidence against the firm's deployment context. The pack on the table is typically a system card, a model card for the specific variant, evaluation reports, a red-team summary, security and privacy attestations under NDA, the vendor's responsible-use and acceptable-use policy, the trust-centre page on data handling and abuse monitoring, and the vendor's incident-disclosure history. The output is a sufficiency view by criterion, named gaps with supplemental evidence requested, the residual reliance the firm is taking with named caveats, recommended owner actions, and the named events that trigger a re-review.

This is the model-evidence layer. It pairs with the entity-level layer in `vendor-diligence` (third-party-operational-resilience): vendor-diligence handles financial health, contracts, exit posture, sub-contractor footprint, and entity-level security attestations as entity evidence; this skill goes deep on whether the vendor's published evidence about the model itself is sufficient for the firm's deployment context. The chain is one-directional: vendor-diligence runs first, sets `eval_evidence_status = deferred-to-evidence-review` where the question is "is the vendor's published evidence pack sufficient for our deployment context", and links to this skill's record by ID. This skill closes the loop with `linked_vendor_diligence_id`. Neither side restates the other.

The audience reads from three angles at once. The AI Governance Lead owns the artefact and consolidates the analysis. The model risk function (MRMO) co-reviews where the firm's model risk programme treats the use case as in scope, and is the primary co-attestor in bank-affiliated entities. The vendor-diligence officer or head of TPRM consumes the structured record back into the entity-level vendor record. The CISO function co-reviews the security and privacy criteria for any deployment with a cyber overlay (which is most v1 GenAI deployments). The chief privacy officer co-reviews where regulated personal data flows to vendor-side processing. The CCO co-reviews where the use case touches consumer-facing communications, recommendation, or decisioning.

The review is a draft until the named reviewers attest. The skill stops at the recommendation.

## Ask first

Most of what the review needs is on the table by the time someone reaches for this skill. A few things to settle before drafting:

- What is the deployment form. Hosted-API, open-weights-self-hosted, open-weights-vendor-hosted, on-prem-appliance, or fine-tuned-derivative. The form rewires the evidence-ask: an open-weights model the firm runs on its own infrastructure has security and privacy posture as firm-side, not vendor-side; a hosted-API model has them as live vendor evidence-asks. Get this on the table first; it sets the rest of the spine.

- What is the in-firm deployment context. The use cases in scope, the architecture (foundation-model only, RAG, tool use, multi-agent, persistent memory, multimodal), and the model-card record from `model-card-builder` if it has run. The basis for every sufficiency-view criterion is what the in-firm use needs, not what the vendor's general claim covers; without the deployment context, the sufficiency view collapses into an inventory.

- What evidence is actually in hand. The pack as it sits today, with confidentiality markers. NDA-bound items can be reviewed but cannot be quoted in artefacts read at lower source posture; flag the confidentiality on every entry and respect it downstream.

- Who co-reviews and attests. The named co-attestors flow from the loaded sector overlay and cross-cutting overlays: MRMO for banking, chief privacy officer for any regulated-data-touching deployment, CISO function for any cyber-flagged review, CCO for any consumer-facing or decisioning-touching deployment.

When the engagement-scope record is supplied, the skill consumes it for institution, persona, source posture, sector and cross-cutting overlays, and the use-case context. Otherwise it asks the practitioner the few facts it needs, and source posture sets what the review can assert at high confidence and what carries `[evidence needed]`.

## How the review gets filled in

The review has the same spine across vendors and deployment forms. The order below is the dependency chain a senior practitioner walks; sections without dependencies fill in as evidence arrives.

Deployment form drives evidence-ask scoping; settle it before reading any criterion. The in-firm deployment context drives the basis column on every sufficiency-view entry; it must be in hand before the sufficiency view is filled. The sufficiency view drives the gap list and the residual-reliance read; both depend on it.

**Review and vendor-and-model metadata** name the reviewer role, review stage (onboarding, version-delta, periodic-reattestation, post-incident, exam-readiness), the vendor and model with version, the deployment form and version-pinning posture, the evidence-pack date, and the in-firm use cases in scope. Where this review chains from `vendor-diligence`, the linked vendor-diligence ID is recorded; where it chains forward to `genai-pre-prod-review` or `validation-plan`, those links populate at the recommended-actions section. Reviewer roles are functions, never named individuals.

**Evidence inventory** lists the documents reviewed with date, source URL where public, and confidentiality marker. The vendor-self-attestation flag distinguishes vendor-authored documents (system card, model card, vendor red-team summary, vendor responsible-use policy) from third-party attestations (SOC 2 by named auditor, ISO certificate). The distinction carries forward to confidence labelling in the source trace; vendor-authored documents default to vendor-self-attestation confidence and never collapse to high. Confidentiality is required on every entry; NDA-bound items are flagged and respected downstream.

**Sufficiency view by criterion** is where the review earns its keep. Each criterion gets a status (sufficient, partial, insufficient, missing, not-applicable) and a basis that names what the in-firm use needs and how the vendor evidence reads against that need. The criteria set covers intended-use scope, training-data posture, evaluation coverage, dangerous-capability evaluations, red-team coverage, security posture, privacy posture, content provenance, incident-disclosure history, support and escalation, regulator-engagement history, change and version control, responsible-use policy, and abuse-monitoring and data retention. The basis column is the load-bearing one: a general-purpose hallucination evaluation is not the same as performance on the firm's domain; a vendor red-team on direct injection is not the same as coverage of indirect injection over the firm's RAG corpora. Criteria not applicable to the deployment form are explicit "not-applicable" with the basis (security posture is not-applicable for open-weights-self-hosted because the firm controls the serving plane; the firm-side responsibility shift is recorded), not omitted.

**Named gaps** turn partial and insufficient sufficiency-view entries into actionable items. Each gap has a criterion link, a concrete description, severity, the supplemental evidence requested, the function-level owner, and a deadline. A gap marked "accepted-as-best-available" is one where the firm acknowledges the residual is unfillable (typical for open-weights training-data disclosure, typical for content-provenance where the vendor does not yet provide watermarking) and absorbs the residual in the residual-reliance section.

**Residual reliance** is the section that distinguishes a review from an inventory. For each item the firm is depending on the vendor for, the section names the reliance, the scoping caveat that limits it, and the function-level owner who has accepted it. "Firm relies on vendor's published refusal-rate posture for the assistant's intended-use scope; caveat is firm-side in-flight monitoring; accepted by AI Governance Lead" is the shape. Anything left implicit becomes a gap when an incident reframes the question.

**Recommended owner actions** carry each gap to a function-level owner with a deadline and a severity. Critical-severity items typically block deployment until closed. Where the action requires vendor input, the firm-side owner role is named and the vendor request is the action content; the vendor is not the owner.

**Re-review triggers** name the events that require this review to be re-run. At minimum, for hosted-API and vendor-hosted forms: vendor model-version swap; vendor new-system-card publication; vendor-disclosed incident affecting the model variant; vendor change to acceptable-use or responsible-use policy; vendor change to abuse-monitoring or data-retention default; expansion of in-firm deployment context (new RAG corpora, expanded tool inventory, new use case). Loaded sector and cross-cutting overlays append their named triggers.

**Source trace and confidence** records every material claim, its source, the evidence pointer, and a confidence label. Vendor red-team results carry vendor-self-attestation confidence (typically low to medium); third-party attestations from named auditors carry higher confidence. Do not collapse vendor and third-party evidence into one line. Items without evidence carry `[evidence needed]` and route to recommended actions, not silently into the review body.

Depth flexes with deployment form, tier, and sector. A hosted-API tier-1 review with banking and cyber overlays runs longest. An open-weights-self-hosted tier-2 review compresses the security-posture and privacy-posture sections to "not-applicable" and shifts weight onto the firm-side responsibility shift. Empty named sections are not acceptable, but compression is.

## Sector and cross-cutting overlays

When the engagement scope names a sector (banking, insurance, capital-markets, payments-fintech), load the matching `references/sector-overlays/<sector>.md`. Each overlay carries sector-specific evidence asks, co-reviewer expectations, re-review triggers, and the named additions to the structured-output `sector_overlay_notes` block. Treating the overlay as background reading is the failure mode; the overlay's named additions land in the review.

The cyber cross-cutting overlay should be considered the default for v1 foundation-model evidence reviews. The threat surface a foundation-model vendor exposes is, in the named regulatory anchors' framing, a cybersecurity risk class; the CISO function co-reviews the security and privacy criteria. The privacy and conduct overlays load when the engagement scope flags them: privacy where regulated personal data may flow to vendor-side processing; conduct where the use case touches consumer-facing communications, recommendation, or decisioning. Climate is not applicable.

Load only the overlays the engagement scope names. Gold-plating with overlays the engagement does not implicate adds noise without challenge value.

## What's load-bearing and what flexes

A handful of things do not flex:

- Every material claim cites a source. Unsupported items carry `[evidence needed]` and route to recommended actions, not silently into the review body.
- The sufficiency view is read against the in-firm deployment context, not against the vendor's general claim. The basis column on every criterion is required.
- Vendor self-attestation is distinguished from third-party attestation. Vendor-authored documents default to vendor-self-attestation confidence; do not collapse to high.
- Confidentiality is recorded on every evidence-inventory entry. NDA-bound items are not quoted in artefacts read at lower source posture.
- Residual reliance is named with caveats and a function-level accepted owner. Implicit reliance is a gap in waiting.
- Re-review triggers are explicit, not "as needed". For hosted-API and vendor-hosted forms, vendor model-version swap and vendor new-system-card publication are non-optional.
- Owner roles are functions, never named individuals.
- The boundary with `vendor-diligence` is respected. This skill is the model-evidence layer; entity-level diligence sits in `vendor-diligence`. The chain is one-directional and the linked record IDs close the loop.
- No fabricated regulatory facts. Unknown section references stay as `[verify section]` flags in the source-anchors file (not in the review body).
- The review is a draft until the named reviewers attest.

Everything else adapts to context. Deployment form rewires the evidence-ask scoping. Tier drives depth. Review stage drives which sections lean heavy (onboarding emphasises the full sufficiency view; version-delta focuses on what changed against the prior review and the re-review triggers that fired; post-incident emphasises incident-disclosure history and the linked-incident analysis). Audience drives tone. Sector and cross-cutting overlays load from the engagement scope. Where firm-specific policy or taxonomy applies, it lives in `references/firm-overlay.md` (consumed when present) and never in the review directly.

## Output

Two artefacts: the review per `templates/default-output.md`, and the structured object per `schemas/llm-vendor-evidence-review.schema.json`. The reviewer-attestation block is filled by the named human reviewers (AI Governance Lead with co-attestors per loaded overlays); the review is filed only after.

Downstream consumers: `genai-pre-prod-review` consumes the structured object for the gate decision (the linked review ID is part of the gate inputs); `vendor-diligence` consumes the linked record ID and the high-severity gaps and recommended actions back into the entity-level vendor record; `board-ai-risk-pack` pulls the residual-reliance summary, high-severity gaps, and material re-review triggers; the firm's TPRM forum consumes the review summary as the model-evidence input to the entity-level decision; the AI risk committee consumes the review for any tier-1 deployment. The schema is the input contract for those consumers; additive changes only. Add fields, do not rename or repurpose them.

## Pointers

- `references/source-anchors.md` — citations and excerpts for the named anchors.
- `references/sector-overlays/{banking,insurance,capital-markets,payments-fintech}.md` — sector overlays loaded from engagement scope.
- `references/cross-cutting/{cyber,privacy,conduct}.md` — cross-cutting overlays; cyber is the default for v1 GenAI reviews.
- `references/firm-overlay.md` — firm policy, taxonomy, named owners (consumed when present).
- `templates/default-output.md` — review template.
- `schemas/llm-vendor-evidence-review.schema.json` — structured-output contract.
- `examples/` — anonymised public-source-derived scenarios (regional bank reviewing a major-vendor hosted-API for a tier-1 KYC assistant; regional life insurer reviewing an open-weights model for a claims-summarisation pilot).
- `TROUBLESHOOTING.md` — recurring defects.
