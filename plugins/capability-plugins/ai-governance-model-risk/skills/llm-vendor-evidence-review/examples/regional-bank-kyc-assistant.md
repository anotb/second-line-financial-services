# Example: regional bank reviews evidence pack for tier-1 KYC assistant

## Input

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

## Output sketch

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

## Why this scenario matters

It exercises the core boundary case: a hosted-API foundation-model deployment from a major vendor at tier-1, where the vendor's published evidence is genuinely substantial but does not, on its own, cover the firm's deployment context. The review separates what the vendor evidence is sufficient for (intended-use scope, base-model security posture) from what the firm is responsible for (in-firm domain-specific evaluation, indirect-injection coverage, downstream content-provenance compensation). It also exercises the chain to `prompt-injection-risk` and `validation-plan` rather than collapsing those into the evidence-pack review.

The banking sector overlay loads (FFIEC IT Handbook touchpoint on third-party application security, interagency third-party risk-management guidance for the entity-level wrapper); the cyber overlay loads (NYDFS Part 500 §500.11 third-party service-provider security alignment for the NY-footprint subsidiary, vendor red-team taxonomy framing); the privacy overlay loads (GLBA Safeguards posture on prompts as customer information, abuse-monitoring exception scope as a privacy seam).
