# Example: regional life insurer reviews open-weights model for claims summarisation pilot

## Input

A regional US life insurer (state-chartered, primary regulator state DOI; NAIC Model Bulletin adopted in domicile state) is piloting a smaller open-weights model from a foundation-model vendor for claims-narrative summarisation. The model is downloaded under the vendor's open-weights licence and run on the firm's own infrastructure (private cloud, no vendor-side traffic). The pilot is tier-2; the use case has cleared `ai-use-case-intake` and `ai-risk-tiering`. The scope record is supplied: institution-type insurer, primary-regulator state-DOI, sector-overlay insurance, cross-cutting-overlay set [privacy, conduct], persona AI Governance Lead with MRMO co-reviewer, source-posture public-plus-firm-policy.

The evidence pack on the table is thinner by design (open-weights, vendor-hosted-nothing):

- Vendor model card for the open-weights variant (public, dated)
- Vendor evaluation report on the variant covering general benchmarks and named safety evaluations (public)
- Vendor responsible-use policy and acceptable-use rules covering open-weights distribution (public)
- Vendor training-data disclosure (public, partial: data categories named; sources not at line-item granularity)
- Vendor model-card section on intended-use, limitations, known failure modes (public)
- No SOC 2 (the model is vendor-distributed, not vendor-hosted; SOC 2 is not the relevant attestation here)
- No vendor incident-disclosure history specific to the open-weights variant (vendor publishes platform-level incident history; not directly mappable)

## Output sketch

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

## Why this scenario matters

It exercises the open-weights branch where deployment form rewires the evidence-ask. Security and privacy posture shift from vendor-side to firm-side; abuse-monitoring becomes not-applicable; SOC 2 stops being the relevant attestation; vendor incident-disclosure history is partial-by-design rather than a vendor failing. The review correctly routes most validation responsibility to `validation-plan` and the firm's PHI-handling environment, and absorbs the training-data-disclosure residual rather than treating it as a blocking gap. It also exercises the insurance sector overlay (NAIC Model Bulletin AIS Program elements as the supervisory frame; state-DOI lens) and the privacy and conduct cross-cutting overlays (HIPAA on PHI; consumer-recourse posture on claims-narrative outputs).
