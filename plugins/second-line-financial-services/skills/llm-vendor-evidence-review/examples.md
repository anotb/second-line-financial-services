# Examples and troubleshooting

One section per worked example, then troubleshooting. Read only what you need.

## life-insurer-open-weights-claims-summary

### Example: regional life insurer reviews open-weights model for claims summarisation pilot

#### Input

A regional US life insurer (state-chartered, primary regulator state DOI; NAIC Model Bulletin adopted in domicile state) is piloting a smaller open-weights model from a foundation-model vendor for claims-narrative summarisation. The model is downloaded under the vendor's open-weights licence and run on the firm's own infrastructure (private cloud, no vendor-side traffic). The pilot is tier-2; the use case has cleared `ai-use-case-intake` and `ai-risk-tiering`. The scope record is supplied: institution-type insurer, primary-regulator state-DOI, sector-overlay insurance, cross-cutting-overlay set [privacy, conduct], persona AI Governance Lead with MRMO co-reviewer, source-posture public-plus-firm-policy.

The evidence pack on the table is thinner by design (open-weights, vendor-hosted-nothing):

- Vendor model card for the open-weights variant (public, dated)
- Vendor evaluation report on the variant covering general benchmarks and named safety evaluations (public)
- Vendor responsible-use policy and acceptable-use rules covering open-weights distribution (public)
- Vendor training-data disclosure (public, partial: data categories named; sources not at line-item granularity)
- Vendor model-card section on intended-use, limitations, known failure modes (public)
- No SOC 2 (the model is vendor-distributed, not vendor-hosted; SOC 2 is not the relevant attestation here)
- No vendor incident-disclosure history specific to the open-weights variant (vendor publishes platform-level incident history; not directly mappable)

#### Output sketch

**Deployment form.** open-weights-self-hosted. This drives the evidence-ask scoping below.

**Sufficiency view (abbreviated).**

| Criterion | Status | Basis |
|---|---|---|
| intended-use-scope | sufficient | Vendor model card scopes the variant for general assistive use including summarisation; PHI-aware deployment is firm-side responsibility, not vendor-side. |
| training-data-posture | partial | Data categories named at provider level; sources not at line-item granularity. Accepted-as-best-available given the open-weights distribution pattern; the firm absorbs the disclosure-depth residual. |
| evaluation-coverage | partial | Vendor evals are general-purpose. No PHI-specific or claims-domain evaluation expected. In-firm domain-specific evaluation is in scope of `validation-plan`; routes accordingly. |
| dangerous-capability-evaluations | sufficient | Vendor model card includes the named evaluations for the model class. Out-of-scope for claims-summarisation deployment. |
| red-team-coverage | partial | Vendor red-team summary covers direct injection and jailbreak at vendor level. Indirect-injection coverage in the deployed architecture (claims documents as input) routes to `prompt-injection-risk`. |
| security-posture | not-applicable | The firm hosts the model. Security posture is the firm's, not the vendor's. CISO function and firm cloud-security posture take over. Recorded as not-applicable to the vendor; firm-side responsibility shift documented. |
| privacy-posture | not-applicable | The firm controls the data plane. Vendor has no access to prompts, outputs, or claims content. Privacy posture is the firm's HIPAA-compliant-environment responsibility. Recorded as not-applicable; firm-side responsibility documented in the privacy overlay notes. |
| content-provenance | insufficient | No content-provenance signal from the vendor for the open-weights variant. Firm-side downstream tagging (output-source labelling in the claims-summary UI) compensates. |
| incident-disclosure-history | partial | No variant-specific incident history; vendor publishes platform-level history. Re-review trigger set on platform-level incident disclosures that name the variant or model family. |
| support-and-escalation | partial | Vendor offers community support for the open-weights variant; no enterprise SLAs on the variant itself. Firm absorbs the support-tier residual or contracts separately. |
| change-and-version-control | sufficient | Open-weights checkpoint is firm-pinned (the firm controls when it upgrades). Vendor publishes new variants on its own cadence; firm chooses adoption. |
| responsible-use-policy | sufficient | Vendor responsible-use policy covers the open-weights variant; firm acceptable-use policy adopts vendor restrictions and adds firm-specific restrictions. |
| abuse-monitoring-and-data-retention | not-applicable | No vendor-side traffic. Firm-side logging and retention apply per firm policy. |

**Gaps (high-severity excerpted).**

- PHI-specific evaluation: required for the deployment; in scope of `validation-plan`. Owner role: model owner role, MRMO oversight; deadline before pre-prod gate.
- Training-data disclosure expansion: requested but accepted-as-best-available given open-weights distribution. Owner role: AI Governance Lead acknowledges acceptance.
- Vendor incident-disclosure subscription: in-firm process to monitor vendor platform-level disclosures and assess applicability to the variant in use. Owner role: AI Governance Lead.

**Residual reliance (excerpted).**

- Firm relies on vendor's model-card description of intended-use, limitations, and known failure modes. Caveat: caveat is documented at the gate review and revisited on every variant upgrade. Accepted by AI Governance Lead with MRMO co-attest.
- Firm shifts most validation responsibility in-house. Vendor evidence is starting context, not coverage. Accepted by MRMO.
- Firm subscribes to vendor disclosure feeds and treats new-disclosure-affecting-the-variant as a re-review trigger.

**Re-review triggers.**

Vendor publishes new variant in the same model family; vendor publishes incident disclosure naming the variant or family; vendor changes responsible-use policy; firm decides to upgrade to a newer checkpoint; expansion of pilot beyond claims summarisation; introduction of any tool-use, RAG-corpora, or PHI scope expansion.

#### Why this scenario matters

It exercises the open-weights branch where deployment form rewires the evidence-ask. Security and privacy posture shift from vendor-side to firm-side; abuse-monitoring becomes not-applicable; SOC 2 stops being the relevant attestation; vendor incident-disclosure history is partial-by-design rather than a vendor failing. The review correctly routes most validation responsibility to `validation-plan` and the firm's PHI-handling environment, and absorbs the training-data-disclosure residual rather than treating it as a blocking gap. It also exercises the insurance sector overlay (NAIC Model Bulletin AIS Program elements as the supervisory frame; state-DOI lens) and the privacy and conduct cross-cutting overlays (HIPAA on PHI; consumer-recourse posture on claims-narrative outputs).

## regional-bank-kyc-assistant

### Example: regional bank reviews evidence pack for tier-1 KYC assistant

#### Input

A regional US bank (commercial-bank charter, primary regulator OCC) is preparing to onboard a major foundation-model vendor's hosted-API model for a tier-1 KYC research and summarisation assistant. The use case has cleared `ai-use-case-intake` and `ai-risk-tiering`; `vendor-diligence` has run and set `eval_evidence_status = deferred-to-evidence-review` for the model-evidence layer. The scope record is supplied: institution-type commercial-bank, primary-regulator OCC, sector-overlay banking, cross-cutting-overlay set [cyber, privacy], persona AI Governance Lead, source-posture public-plus-firm-policy.

The evidence pack on the table:

- Vendor system card (public, dated current quarter)
- Model card for the specific model variant (public, dated)
- Vendor evaluation report covering hallucination rate, harmful-content refusal, jailbreak resistance (public)
- Vendor red-team summary covering direct prompt injection and jailbreak (public, partial detail)
- SOC 2 Type II report from named auditor (NDA-bound, current period)
- ISO/IEC 27001 certificate with Statement of Applicability (NDA-bound)
- Vendor responsible-use policy and acceptable-use rules (public)
- Trust-center page covering data-handling, retention defaults, abuse-monitoring scope (public)
- Vendor incident-disclosure history page covering the past 24 months (public)

#### Output sketch

**Sufficiency view (abbreviated).**

| Criterion | Status | Basis |
|---|---|---|
| intended-use-scope | sufficient | Vendor system card scopes intended-use to assistive research and summarisation; KYC research-assistant deployment is in-scope. |
| training-data-posture | partial | Vendor model card describes data categories at provider level; does not name sources at line-item granularity. Bank's KYC compliance counsel notes the disclosure is at common industry baseline. Accepted-as-best-available pending GPAI-style transparency report. |
| evaluation-coverage | partial | Vendor evals cover general hallucination and harmful-content. No financial-services-specific or KYC-domain evaluation surfaced. Routes to `validation-plan` for in-firm domain-specific evaluation. |
| dangerous-capability-evaluations | sufficient | Vendor system card includes named dangerous-capability evaluations relevant to the model class. Out-of-scope for KYC assistant deployment. |
| red-team-coverage | partial | Vendor red-team covers direct injection and jailbreak. Indirect injection over enterprise-document RAG corpus (the deployed architecture) not covered. Firm-internal red-team gap routes to `prompt-injection-risk` and `validation-plan`. |
| security-posture | sufficient | SOC 2 Type II opinion clean, scope covers the relevant service organisation; complementary user-entity controls reviewed and tracked separately by CISO function. |
| privacy-posture | partial | Vendor data-handling policy and trust-center page describe the default-zero-retention posture for the enterprise tier; abuse-monitoring exception scope is named (humans review flagged inputs under defined conditions). NPI-handling implications recorded in privacy overlay notes. |
| content-provenance | insufficient | Vendor does not currently provide watermarking or content-provenance signal for the model variant in scope. Firm absorbs the residual or downstream-controls (audit logging, output-tagging in the assistant UI) compensate. |
| incident-disclosure-history | sufficient | Vendor publishes incident disclosures with named taxonomy and dates; 24-month history reviewed. |
| support-and-escalation | sufficient | Enterprise-tier support contract with named SLAs and escalation matrix. Recorded in TPRM record. |
| change-and-version-control | partial | Vendor publishes deprecation notice with named lead time but version-pinning posture is rolling-with-notice rather than firm-pinned. Re-validation flag fires on every notice. |

**Gaps (high-severity excerpted).**

- Financial-services-specific harmful-content evaluation: requested as supplemental evidence; owner role AI Governance Lead; deadline before pre-prod gate.
- Indirect-injection adversarial coverage over enterprise-document RAG corpora: in-firm red-team scope routes to `prompt-injection-risk`; vendor-side coverage requested as supplemental for context.
- Content-provenance gap: accepted-as-best-available; downstream control compensates via audit logging and assistant UI output-tagging.

**Residual reliance (excerpted).**

- Firm relies on vendor's published refusal-rate and harmful-content posture for the assistant's intended-use scope. Caveat: firm runs in-flight monitoring of refusal rate, output-filter trip rate, and complaint signals; firm reserves the right to swap-revalidate on any vendor-disclosed incident affecting the model variant. Accepted by AI Governance Lead.
- Firm relies on vendor's default-zero-retention posture for enterprise-tier API traffic. Caveat: abuse-monitoring exception scope is documented; firm-side prompt logging captures what is sent. Accepted by Head of Privacy.
- Firm relies on vendor's incident-disclosure cadence. Caveat: cadence is vendor-defined; firm subscribes to vendor disclosure feeds and treats new-disclosure as a re-review trigger.

**Re-review triggers.**

Vendor model-version swap; vendor new-system-card publication; vendor-disclosed incident affecting the model variant; vendor change to acceptable-use or responsible-use policy; vendor change to abuse-monitoring or data-retention default; expansion of in-firm RAG corpus beyond current scope; addition of tool-use to the deployment.

#### Why this scenario matters

It exercises the core boundary case: a hosted-API foundation-model deployment from a major vendor at tier-1, where the vendor's published evidence is genuinely substantial but does not, on its own, cover the firm's deployment context. The review separates what the vendor evidence is sufficient for (intended-use scope, base-model security posture) from what the firm is responsible for (in-firm domain-specific evaluation, indirect-injection coverage, downstream content-provenance compensation). It also exercises the chain to `prompt-injection-risk` and `validation-plan` rather than collapsing those into the evidence-pack review.

The banking sector overlay loads (FFIEC IT Handbook touchpoint on third-party application security, interagency third-party risk-management guidance for the entity-level wrapper); the cyber overlay loads (NYDFS Part 500 §500.11 third-party service-provider security alignment for the NY-footprint subsidiary, vendor red-team taxonomy framing); the privacy overlay loads (GLBA Safeguards posture on prompts as customer information, abuse-monitoring exception scope as a privacy seam).

## troubleshooting

### Troubleshooting: llm-vendor-evidence-review

Recurring defects observed in foundation-model vendor evidence reviews. The first three are the failure modes the skill exists to prevent; the rest are rework triggers that show up in second reviews.

#### 1. Vendor evidence treated as authoritative without a sufficiency view

**Defect.** The review enumerates documents read (system card, model card, eval report, red-team summary) and concludes "evidence reviewed". The firm inherits the vendor's posture without ever stating what the firm is actually relying on or where the in-firm deployment context diverges from what the evidence covers.

**Fix.** Every criterion in `sufficiency_view[]` has a `basis` field that names what the in-firm use needs and how the vendor evidence reads against that need. A general-purpose hallucination eval is not the same as performance on the firm's KYC corpus; a vendor red-team on direct injection is not the same as coverage of indirect injection over enterprise document stores. The basis column is what makes the review a review and not an inventory.

#### 2. Residual reliance left unstated

**Defect.** Gaps are named, supplemental evidence is requested, but the question of what the firm is relying on the vendor for goes unanswered. When the model behaves unexpectedly in production, no one can say what the vendor was supposed to be doing.

**Fix.** The `residual_reliance[]` block names each item the firm is depending on the vendor for, the caveat that scopes it, and the function-level owner who has accepted the reliance. "We rely on the vendor's published refusal-rate posture for the assistant's intended-use scope; caveat is firm-side in-flight monitoring; accepted by AI Governance Lead" is the shape. Anything left implicit becomes a gap when an incident reframes the question.

#### 3. Re-review triggers missing or generic

**Defect.** The vendor publishes a new system card, swaps the underlying model, or discloses an incident, and the firm's review is months stale. The trigger list reads "as needed" or is omitted.

**Fix.** `rereview_triggers[]` carries at minimum: vendor model-version swap, vendor new-system-card publication, vendor-disclosed incident affecting the model in scope, vendor change to acceptable-use or responsible-use policy, vendor change to abuse-monitoring or data-retention posture, and any upstream change in the firm's deployment context (new RAG corpora, expanded tool inventory, new use case). For hosted-API and vendor-hosted open-weights forms, the foundation-model swap re-validation flag in change management is non-optional and should already be the upstream `vendor-diligence` finding.

#### 4. NDA-bound evidence not flagged as confidential

**Defect.** SOC 2 Type II report, ISO certificate Statement of Applicability, trust-center attestations, or vendor red-team detail read under NDA appear in `evidence_inventory[]` without a `confidentiality` value. The review then surfaces in artefacts read at lower source posture (board pack, examiner response, internal training material) and the audit trail leaks.

**Fix.** Every `evidence_inventory[]` entry carries a `confidentiality` value (public, nda-bound, trust-center-gated, regulator-confidential, firm-internal). Downstream consumers respect the marker. NDA-bound items can be referenced in the review record but cannot be quoted in artefacts read at public posture.

#### 5. Vendor self-attestation conflated with third-party attestation

**Defect.** The vendor's red-team summary is recorded next to the SOC 2 report by a named auditor with the same confidence level. The review treats both as equivalent evidence.

**Fix.** Set `vendor_self_attestation = true` on documents the vendor authored (system card, model card, vendor-internal red-team summary, responsible-use policy). Set `vendor_self_attestation = false` on third-party attestations (SOC 2 by named auditor, ISO certificate, third-party red-team report). Source-trace confidence labels for vendor-self-attestation entries should default to vendor-self-attestation; do not collapse to high.

#### 6. Evidence-pack scope confused with in-firm deployment scope

**Defect.** The review covers what the evidence pack covers, regardless of what the firm is actually deploying. A vendor system card describes the model on the vendor's benchmarks; the firm's deployment is base + fine-tune + RAG + retrieval scoping + tool inventory + carrier-side guardrails. Reading evidence against the vendor's frame, not the firm's, produces a sufficient view that is sufficient for the wrong question.

**Fix.** `in_firm_use_cases[]` names the use cases this review is scoped to. The `basis` field on every `sufficiency_view[]` entry references the in-firm deployment context, not the vendor's published claim. Where the deployment includes substantial firm-side wrapping (fine-tune, RAG, tool use), the review chains forward to `validation-plan`, `genai-pre-prod-review`, or `prompt-injection-risk` for the firm-side coverage rather than asserting it from vendor evidence.

#### 7. Boundary with vendor-diligence collapsed

**Defect.** The review covers vendor financials, contract terms, exit posture, audit rights, sub-contractor footprint, regulatory and legal posture; or the upstream `vendor-diligence` review covers model-evidence depth in addition to entity-level diligence. Both ends produce duplicated and divergent records.

**Fix.** This skill is the model-evidence layer. Entity-level diligence belongs to `vendor-diligence` in `third-party-operational-resilience`. The chain is one-directional: `vendor-diligence` runs first, sets `eval_evidence_status = deferred-to-evidence-review` where the question is "is the vendor's published evidence sufficient for our deployment context", and links to this skill's record by ID. This skill's record carries `linked_vendor_diligence_id` to close the loop. Neither side restates the other.

#### 8. EU AI Act GPAI obligations applied where the model is not GPAI

**Defect.** The review imports general-purpose-AI-model documentation expectations regardless of whether the model in scope qualifies under the relevant EU AI Act provisions, and regardless of whether the firm's deployment is in EU scope at all.

**Fix.** GPAI obligations apply where the model meets the GPAI threshold in the loaded `references/cross-cutting.md` overlay or sector overlay and where the firm's deployment falls in EU scope. For non-EU-scope deployments, GPAI provider documentation is informational reference, not binding obligation. The overlay carries the named criteria; SKILL.md does not import them by default.

#### 9. Open-weights review treated like hosted-API review

**Defect.** The same evidence checklist is applied to a vendor-hosted hosted-API model and to an open-weights model the firm runs on its own infrastructure. Security and privacy posture, abuse-monitoring posture, incident-disclosure history, and support-and-escalation expectations carry different weight in each case.

**Fix.** The `model.deployment_form` field drives evidence-ask scoping. For open-weights-self-hosted, security and privacy posture is the firm's, not the vendor's; the review records `not-applicable` against vendor security posture and the firm-side responsibility shifts to the firm's own validation. For hosted-API and vendor-hosted forms, the vendor security and privacy posture remains a live evidence ask. The `responsible-use-policy` and `abuse-monitoring-and-data-retention` criteria likewise read differently across deployment forms.

#### 10. Industry metric frameworks presented as regulatory requirements

**Defect.** Vendor eval reports cite scores against named benchmarks (TruthfulQA, MMLU, HellaSwag, sector-specific harm benchmarks) and the review presents these as evidence against regulatory expectations.

**Fix.** Industry benchmarks are vendor self-reported metrics against shared datasets. They are useful as relative comparison and as evidence of the vendor's testing maturity; they are not, in themselves, regulatory success criteria. Record them in `sufficiency_view[].basis` as what they are, and route to `validation-plan` for in-firm metric definition where the firm's deployment context demands tighter or domain-specific evaluation.

#### 11. Recommended actions without function-level owners

**Defect.** Recommended actions name individuals or name "the vendor" as owner. Either form fails when staffing changes or when the action requires firm-side execution against vendor-side input.

**Fix.** `recommended_actions[].owner_role` is a function (AI Governance Lead, MRMO, Head of TPRM, model owner role, AI risk committee secretary), never an individual. Where the action requires vendor input, the firm-side owner role is named and the vendor request is the action content; the vendor is not the owner.

#### 12. The review filed without reviewer attestation

**Defect.** The structured record reaches downstream consumers (`genai-pre-prod-review` gate, `board-ai-risk-pack` summary) before the human reviewer has attested. The skill stops at the recommendation; downstream consumption before attestation is itself a defect.

**Fix.** The `reviewer_attestation` block is filled by the human reviewer (AI Governance Lead, with co-attestation per loaded overlay where the sector overlay or cross-cutting overlay names a co-acceptor). The record is consumed downstream only after attestation. The skill emits the draft and stops.
