# Troubleshooting: llm-vendor-evidence-review

Recurring defects observed in foundation-model vendor evidence reviews. The first three are the failure modes the skill exists to prevent; the rest are rework triggers that show up in second-pass reviews.

## 1. Vendor evidence treated as authoritative without a sufficiency view

**Defect.** The review enumerates documents read (system card, model card, eval report, red-team summary) and concludes "evidence reviewed". The firm inherits the vendor's posture without ever stating what the firm is actually relying on or where the in-firm deployment context diverges from what the evidence covers.

**Fix.** Every criterion in `sufficiency_view[]` has a `basis` field that names what the in-firm use needs and how the vendor evidence reads against that need. A general-purpose hallucination eval is not the same as performance on the firm's KYC corpus; a vendor red-team on direct injection is not the same as coverage of indirect injection over enterprise document stores. The basis column is what makes the review a review and not an inventory.

## 2. Residual reliance left unstated

**Defect.** Gaps are named, supplemental evidence is requested, but the question of what the firm is relying on the vendor for goes unanswered. When the model behaves unexpectedly in production, no one can say what the vendor was supposed to be doing.

**Fix.** The `residual_reliance[]` block names each item the firm is depending on the vendor for, the caveat that scopes it, and the function-level owner who has accepted the reliance. "We rely on the vendor's published refusal-rate posture for the assistant's intended-use scope; caveat is firm-side in-flight monitoring; accepted by AI Governance Lead" is the shape. Anything left implicit becomes a gap when an incident reframes the question.

## 3. Re-review triggers missing or generic

**Defect.** The vendor publishes a new system card, swaps the underlying model, or discloses an incident, and the firm's review is months stale. The trigger list reads "as needed" or is omitted.

**Fix.** `rereview_triggers[]` carries at minimum: vendor model-version swap, vendor new-system-card publication, vendor-disclosed incident affecting the model in scope, vendor change to acceptable-use or responsible-use policy, vendor change to abuse-monitoring or data-retention posture, and any upstream change in the firm's deployment context (new RAG corpora, expanded tool inventory, new use case). For hosted-API and vendor-hosted open-weights forms, the foundation-model swap re-validation flag in change management is non-optional and should already be the upstream `vendor-diligence` finding.

## 4. NDA-bound evidence not flagged as confidential

**Defect.** SOC 2 Type II report, ISO certificate Statement of Applicability, trust-center attestations, or vendor red-team detail read under NDA appear in `evidence_inventory[]` without a `confidentiality` value. The review then surfaces in artefacts read at lower source posture (board pack, examiner response, internal training material) and the audit trail leaks.

**Fix.** Every `evidence_inventory[]` entry carries a `confidentiality` value (public, nda-bound, trust-center-gated, regulator-confidential, firm-internal). Downstream consumers respect the marker. NDA-bound items can be referenced in the review record but cannot be quoted in artefacts read at public posture.

## 5. Vendor self-attestation conflated with third-party attestation

**Defect.** The vendor's red-team summary is recorded next to the SOC 2 report by a named auditor with the same confidence level. The review treats both as equivalent evidence.

**Fix.** Set `vendor_self_attestation = true` on documents the vendor authored (system card, model card, vendor-internal red-team summary, responsible-use policy). Set `vendor_self_attestation = false` on third-party attestations (SOC 2 by named auditor, ISO certificate, third-party red-team report). Source-trace confidence labels for vendor-self-attestation entries should default to vendor-self-attestation; do not collapse to high.

## 6. Evidence-pack scope confused with in-firm deployment scope

**Defect.** The review covers what the evidence pack covers, regardless of what the firm is actually deploying. A vendor system card describes the model on the vendor's benchmarks; the firm's deployment is base + fine-tune + RAG + retrieval scoping + tool inventory + carrier-side guardrails. Reading evidence against the vendor's frame, not the firm's, produces a sufficient view that is sufficient for the wrong question.

**Fix.** `in_firm_use_cases[]` names the use cases this review is scoped to. The `basis` field on every `sufficiency_view[]` entry references the in-firm deployment context, not the vendor's published claim. Where the deployment includes substantial firm-side wrapping (fine-tune, RAG, tool use), the review chains forward to `validation-plan`, `genai-pre-prod-review`, or `prompt-injection-risk` for the firm-side coverage rather than asserting it from vendor evidence.

## 7. Boundary with vendor-diligence collapsed

**Defect.** The review covers vendor financials, contract terms, exit posture, audit rights, sub-contractor footprint, regulatory and legal posture; or the upstream `vendor-diligence` review covers model-evidence depth in addition to entity-level diligence. Both ends produce duplicated and divergent records.

**Fix.** This skill is the model-evidence layer. Entity-level diligence belongs to `vendor-diligence` in `third-party-operational-resilience`. The chain is one-directional: `vendor-diligence` runs first, sets `eval_evidence_status = deferred-to-evidence-review` where the question is "is the vendor's published evidence sufficient for our deployment context", and links to this skill's record by ID. This skill's record carries `linked_vendor_diligence_id` to close the loop. Neither side restates the other.

## 8. EU AI Act GPAI obligations applied where the model is not GPAI

**Defect.** The review imports general-purpose-AI-model documentation expectations regardless of whether the model in scope qualifies under the relevant EU AI Act provisions, and regardless of whether the firm's deployment is in EU scope at all.

**Fix.** GPAI obligations apply where the model meets the GPAI threshold in the loaded `references/cross-cutting/` overlay or sector overlay and where the firm's deployment falls in EU scope. For non-EU-scope deployments, GPAI provider documentation is informational reference, not binding obligation. The overlay carries the named criteria; SKILL.md does not import them by default.

## 9. Open-weights review treated like hosted-API review

**Defect.** The same evidence checklist is applied to a vendor-hosted hosted-API model and to an open-weights model the firm runs on its own infrastructure. Security and privacy posture, abuse-monitoring posture, incident-disclosure history, and support-and-escalation expectations carry different weight in each case.

**Fix.** The `model.deployment_form` field drives evidence-ask scoping. For open-weights-self-hosted, security and privacy posture is the firm's, not the vendor's; the review records `not-applicable` against vendor security posture and the firm-side responsibility shifts to the firm's own validation. For hosted-API and vendor-hosted forms, the vendor security and privacy posture remains a live evidence ask. The `responsible-use-policy` and `abuse-monitoring-and-data-retention` criteria likewise read differently across deployment forms.

## 10. Industry metric frameworks presented as regulatory requirements

**Defect.** Vendor eval reports cite scores against named benchmarks (TruthfulQA, MMLU, HellaSwag, sector-specific harm benchmarks) and the review presents these as evidence against regulatory expectations.

**Fix.** Industry benchmarks are vendor self-reported metrics against shared datasets. They are useful as relative comparison and as evidence of the vendor's testing maturity; they are not, in themselves, regulatory pass criteria. Record them in `sufficiency_view[].basis` as what they are, and route to `validation-plan` for in-firm metric definition where the firm's deployment context demands tighter or domain-specific evaluation.

## 11. Recommended actions without function-level owners

**Defect.** Recommended actions name individuals or name "the vendor" as owner. Either form fails when staffing changes or when the action requires firm-side execution against vendor-side input.

**Fix.** `recommended_actions[].owner_role` is a function (AI Governance Lead, MRMO, Head of TPRM, model owner role, AI risk committee secretary), never an individual. Where the action requires vendor input, the firm-side owner role is named and the vendor request is the action content; the vendor is not the owner.

## 12. The review filed without reviewer attestation

**Defect.** The structured record reaches downstream consumers (`genai-pre-prod-review` gate, `board-ai-risk-pack` summary) before the human reviewer has attested. The skill stops at the recommendation; downstream consumption before attestation is itself a defect.

**Fix.** The `reviewer_attestation` block is filled by the human reviewer (AI Governance Lead, with co-attestation per loaded overlay where the sector overlay or cross-cutting overlay names a co-acceptor). The record is consumed downstream only after attestation. The skill emits the draft and stops.
