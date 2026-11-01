# Example: GenAI vendor (foundation-model API for FNOL triage at a P&C insurer)

Public-source-derived. No named vendor. The shape mirrors a common diligence pattern at a mid-sized property-and-casualty insurer evaluating a foundation-model API to triage first-notice-of-loss narratives into severity and routing tiers.

## Input

- **Vendor**: a foundation-model provider offering a hosted API for text generation, classification, and structured-output extraction.
- **Service**: the carrier sends FNOL narratives (text, sometimes with attached photos) to the API; the API returns a triage tier, recommended adjuster skill-set, and structured fields. Outputs feed the carrier's claims workflow as an "advisory" tier suggestion that adjusters can override.
- **Inputs already on file**: vendor's published system card; vendor's published evaluation report; vendor's privacy and trust-and-safety pages; the proposed enterprise contract (with a non-default training-data-opt-out addendum); the carrier's draft criticality-assessment record (criticality = important on first pass; revisited based on diligence findings); deployment architecture diagram showing prompt structure, retention windows, and the carrier-side guardrails.
- **Engagement scope supplied**: institution = insurance company (P&C); primary regulators = state DOIs in the carrier's footprint, with NY DFS in scope; persona = head of TPRM coordinating with AI governance lead and CISO; source posture = public-plus-firm-policy; sector overlay = insurance; cross-cutting overlays = cyber, privacy.
- **AI vendor**: true. The diligence pack runs the AI-overlay branch and the AI-specific findings section is populated.

## Output sketch

- **Service description and risk classification** — embedded in claims-handling, an unfair-claims-settlement-practices-sensitive process. NAIC Bulletin Dec 2023 expects AIS Program elements applied; vendor is a third-party-AI accountability point. PHI may incidentally appear in narratives where the FNOL describes injuries.
- **Risk-based diligence summary** — interagency-guidance-shaped lifecycle, but the operative state-DOI lens is applied via the insurance overlay. NAIC Insurance Data Security Model Law §4.F third-party-service-provider obligations apply in adopted states.
- **Operational resilience evidence** — vendor publishes a status page and an SLA. No public BCDR test report. Carrier impact tolerance for FNOL channel is 1 business day; vendor SLA is high-availability-language without a recovery-time objective. `bcdr_evidence_status = partial`; reviewer question added.
- **Cyber and information-security evidence** — SOC 2 Type II covering the inference platform; ISO 27001 cert; pen-test summary at the platform level; no penetration-test of the carrier's specific deployment. NYDFS Part 500.11 reach if the carrier has a NY licence — yes. `cyber_evidence_status = partial` because deployment-specific testing is not in scope of the published reports.
- **Financial-condition evidence** — vendor is privately held; revenue scale and runway disclosed in commercial conversations only; public 409A or audited financials not available. `financial_condition_status = unknown`; reviewer question recommends a financial-condition representation in the contract.
- **Concentration and sub-contractor footprint** — single hyperscaler underneath the API; named sub-region and dependency on a model-training-and-serving stack. `concentration_flag = watch` and pointer to concentration-risk-review.
- **AI-specific findings** (`ai_vendor = true`):
  - **AI use case category** — foundation-model-api consumed via prompt-and-response, with carrier-side prompt templates and a small RAG component (carrier's claims-handling knowledge base).
  - **Model provenance** — vendor's flagship model family; carrier deploys a dated checkpoint with a vendor-managed deprecation calendar. The deployed system is base + carrier RAG, not vendor-fine-tuned.
  - **Training data posture** — vendor's enterprise-tier default does not retain API content for training; the contract addendum reflects this. The trust-and-safety page documents an abuse-monitoring exception (short retention for safety classifiers). The contract incorporates that exception by reference. Reviewer question added asking whether the abuse-monitoring exception extends to PHI in narratives.
  - **Eval evidence status** — `deferred-to-evidence-review`. The published system card and eval report cover the base model on public benchmarks; the deployed system is base + RAG on FNOL narratives, which is out of coverage. Chained to `llm-vendor-evidence-review` (ai-governance-model-risk skill) for the deeper question. The chain is recorded in `llm_vendor_evidence_review_record_id`.
  - **Eval coverage on deployed system** — `false`. No FNOL-specific evals; no evidence the retrieval and grounding behavior have been tested under the carrier's prompt templates and knowledge-base.
  - **Shared responsibility clarity** — `partial`. Safety, content moderation, and abuse handling are clearly the vendor's; prompt-injection defence and downstream-decisioning quality are the carrier's; the boundary on incident-response notification timing on a model-level safety incident is unclear in the draft contract.
  - **Fine-tune data isolation** — `not-applicable` (no fine-tune in this deployment). Carrier prompts and outputs are isolated per the enterprise-tier default plus contract addendum.
  - **Agent tool posture** — `not-applicable` (no agentic tool-use; output is consumed by adjusters before any action).
  - **System card fit to deployment** — `partial-fit`. The system card describes intended use cases broadly; FNOL triage with PHI-bearing narratives is not addressed; consumer-recourse expectations from state DOI bulletins are not in scope of the system card.
  - **Prompt-as-customer-data assessment** — narratives carry PHI in some claims; carrier's posture is to redact medical detail before sending, but redaction is heuristic and unevidenced. Privacy gap. HIPAA business-associate posture recommended.
- **Contract gap summary** — pointer to contract-gap-review. Headline gaps: model-version pin and deprecation-notice clock missing; PHI handling not addressed; abuse-monitoring exception scope not defined; incident-notification clock at the model-safety-incident level unclear; sub-contractor change consent not addressed; NAIC Insurance Data Security Model Law §4.F drift on third-party-service-provider monitoring.
- **Recommended onboarding decision and review gates** — `defer`. The deeper diligence work needs the `llm-vendor-evidence-review` output, a HIPAA business-associate analysis, a deployment-context evaluation evidence pack, and the contract gap-closure plan before the AI committee and the chief risk officer can approve. Review gates: scope, evidence, authority, impact, decision. Annual recertification at minimum; off-cycle re-review trigger on model-version change or vendor consent-order activity.

## Why this scenario matters

- **AI overlay on a vendor that is "just an API"**: the overlay must not collapse to "treat it like SaaS". The diligence pack must surface model-provenance, training-data posture, eval-coverage on the deployed system, shared-responsibility, and prompt-as-customer-data.
- **Boundary with `llm-vendor-evidence-review`**: the diligence pack does the firm-side TPRM wrapping. The deeper "is this evidence pack sufficient for our deployment context" question is chained to the model-risk function via `eval_evidence_status = deferred-to-evidence-review` and the linked record ID. The skill must hand off cleanly, not duplicate the model-risk review.
- **Insurance overlay engaged**: NAIC Bulletin Dec 2023 third-party-AI accountability and NAIC Insurance Data Security Model Law §4.F apply; both are insurance-only and the bank-flavoured generic skill misses them without the overlay.
- **Privacy overlay engaged**: prompts carry PHI. HIPAA business-associate posture must be raised. The privacy overlay should not be skipped because the vendor markets to enterprises.
- **Recommended decision is `defer`, not `approve`**: the skill stops at the recommendation. It does not approve the vendor. The defer captures the open work; the approver decides.
- **Re-review trigger discipline**: model-version change is a re-review trigger; that is not the default for a non-AI vendor. The AI overlay sets it.

## Anchors

- Interagency Guidance on Third-Party Relationships: Risk Management (OCC/FRB/FDIC, June 2023) — for the lifecycle frame.
- NAIC Bulletin on the Use of Artificial Intelligence Systems by Insurers (December 2023).
- NAIC Insurance Data Security Model Law (Model #668) §4.F.
- NIST AI Risk Management Framework 1.0 — Govern function for AI vendors.
- NIST AI 600-1 (Generative AI Profile) for GenAI-specific vendor diligence considerations.
- NYDFS 23 NYCRR Part 500.11.
- HIPAA Privacy and Security Rules (where PHI is in scope).

See `references/source-anchors.md` for full citations.
