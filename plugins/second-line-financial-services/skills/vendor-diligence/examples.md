# Examples and troubleshooting

One section per worked example, then troubleshooting. Read only what you need.

## genai-fnol-triage-pc-insurer

### Example: GenAI vendor (foundation-model API for FNOL triage at a P&C insurer)

Public-source-derived. No named vendor. The shape mirrors a common diligence pattern at a mid-sized property-and-casualty insurer evaluating a foundation-model API to triage first-notice-of-loss narratives into severity and routing tiers.

#### Input

- **Vendor**: a foundation-model provider offering a hosted API for text generation, classification, and structured-output extraction.
- **Service**: the carrier sends FNOL narratives (text, sometimes with attached photos) to the API; the API returns a triage tier, recommended adjuster skill-set, and structured fields. Outputs feed the carrier's claims workflow as an "advisory" tier suggestion that adjusters can override.
- **Inputs already on file**: vendor's published system card; vendor's published evaluation report; vendor's privacy and trust-and-safety pages; the proposed enterprise contract (with a non-default training-data-opt-out addendum); the carrier's draft criticality-assessment record (criticality = important on first pass; revisited based on diligence findings); deployment architecture diagram showing prompt structure, retention windows, and the carrier-side guardrails.
- **Engagement scope supplied**: institution = insurance company (P&C); primary regulators = state DOIs in the carrier's footprint, with NY DFS in scope; persona = head of TPRM coordinating with AI governance lead and CISO; source posture = public-plus-firm-policy; sector overlay = insurance; cross-cutting overlays = cyber, privacy.
- **AI vendor**: true. The diligence pack runs the AI-overlay branch and the AI-specific findings section is populated.

#### Output sketch

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

#### Why this scenario matters

- **AI overlay on a vendor that is "just an API"**: the overlay must not collapse to "treat it like SaaS". The diligence pack must surface model-provenance, training-data posture, eval-coverage on the deployed system, shared-responsibility, and prompt-as-customer-data.
- **Boundary with `llm-vendor-evidence-review`**: the diligence pack does the firm-side TPRM wrapping. The deeper "is this evidence pack sufficient for our deployment context" question is chained to the model-risk function via `eval_evidence_status = deferred-to-evidence-review` and the linked record ID. The skill must hand off cleanly, not duplicate the model-risk review.
- **Insurance overlay engaged**: NAIC Bulletin Dec 2023 third-party-AI accountability and NAIC Insurance Data Security Model Law §4.F apply; both are insurance-only and the bank-flavoured generic skill misses them without the overlay.
- **Privacy overlay engaged**: prompts carry PHI. HIPAA business-associate posture must be raised. The privacy overlay should not be skipped because the vendor markets to enterprises.
- **Recommended decision is `defer`, not `approve`**: the skill stops at the recommendation. It does not approve the vendor. The defer captures the open work; the approver decides.
- **Re-review trigger discipline**: model-version change is a re-review trigger; that is not the default for a non-AI vendor. The AI overlay sets it.

#### Anchors

- Interagency Guidance on Third-Party Relationships: Risk Management (OCC/FRB/FDIC, June 2023) — for the lifecycle frame.
- NAIC Bulletin on the Use of Artificial Intelligence Systems by Insurers (December 2023).
- NAIC Insurance Data Security Model Law (Model #668) §4.F.
- NIST AI Risk Management Framework 1.0 — Govern function for AI vendors.
- NIST AI 600-1 (Generative AI Profile) for GenAI-specific vendor diligence considerations.
- NYDFS 23 NYCRR Part 500.11.
- HIPAA Privacy and Security Rules (where PHI is in scope).

See `references/source-anchors.md` for full citations.

## saas-customer-support-platform

### Example: SaaS customer-support platform at a regional bank

Public-source-derived. No named vendor. The shape mirrors a common diligence pattern at $50-100B regional banks evaluating a SaaS customer-support platform that surfaces depositor and small-business-borrower inquiries to call-centre agents.

#### Input

- **Vendor**: a US-incorporated SaaS provider offering a customer-support and ticketing platform with telephony integration. Hosted on a single hyperscaler, two regions in scope.
- **Service**: customer-support agent workspace; customer-call recording; ticket management; agent-side knowledge-base search.
- **Business process supported**: contact-centre operations covering deposit-account servicing, debit-card disputes, and consumer-loan servicing.
- **Inputs already on file**: criticality-assessment record (criticality = important; not critical because deposit account servicing has paper-and-IVR fallback within tolerance); SOC 2 Type II report covering 12 months; ISO 27001 certificate (current); annual pen-test executive summary; the vendor's published BCDR plan; the proposed contract draft; firm's third-party-risk-policy citing the interagency third-party guidance and OCC Heightened Standards.
- **Engagement scope supplied**: institution = state member bank; primary regulators = FRB, state DFI; persona = head of TPRM; source posture = public-plus-firm-policy-plus-system-of-record-evidence; sector overlay = banking; cross-cutting overlays = cyber, privacy.
- **AI vendor**: false. The platform has an embedded summarisation feature flagged as "optional"; the firm has not yet enabled it. Treated as not-AI for this pass; if the firm enables the feature, the diligence pack is re-opened with `ai_vendor=true` and the AI overlay is applied.

#### Output sketch

The skill produces a vendor diligence pack. Headlines:

- **Service description and risk classification** — important-tier vendor; consumer-facing impact via the contact-centre channel; NPI in scope (account numbers, balances, dispute narratives); call recordings carry voice biometrics.
- **Risk-based diligence summary** — interagency-guidance-aligned: planning, due-diligence, contract, ongoing-monitoring posture all summarised. Reviewer questions clustered for the TPRM forum.
- **Operational resilience evidence** — vendor RTO of 4 hours and RPO of 15 minutes claimed; BCDR test report covers the primary region but not the failover region tabletop; firm impact tolerance for the contact-centre channel is 4 hours, so the claim meets tolerance only if the failover-region tabletop is evidenced. `bcdr_meets_firm_tolerance = false` until that gap closes.
- **Cyber and information-security evidence** — SOC 2 Type II clean opinion; scope excludes the telephony module; CUEC list includes customer-managed encryption keys (not enabled by the firm in the proposed configuration); ISO 27001 statement of applicability not provided. Pen-test executive summary cites two medium findings open at report date with vendor remediation commitments. `cyber_evidence_status = partial`.
- **Financial-condition evidence** — vendor is a public-company subsidiary; parent-level audited financials and most-recent 10-K reviewed; status `sound`. Going-concern qualifier absent.
- **Concentration and sub-contractor footprint** — single hyperscaler in two regions; same hyperscaler is the firm's primary IaaS for several other vendors. `concentration_flag = watch` and pointer to concentration-risk-review for portfolio analysis.
- **AI-specific findings** — section omitted (`ai_vendor = false`).
- **Contract gap summary** — pointer to the contract-gap-review record. Headline gaps: missing examiner-access clause under Bank Service Company Act, missing breach-notification clock at the platform-incident level (only at the customer-data-incident level), and silence on subcontractor change consent.
- **Recommended onboarding decision and review gates** — `approve-with-conditions`. Conditions: failover-region BCDR tabletop evidenced before go-live; examiner-access clause inserted; breach-notification clock added; subcontractor change consent added; firm enables customer-managed keys before NPI flows to the platform. Review gates: scope, evidence, authority, impact, decision. Decision sits with the head of TPRM and the business-owner SVP per the firm's policy for important-tier vendors. Annual recertification scheduled.

The pack stops at the recommendation. It does not approve the vendor.

#### Why this scenario matters

- **Boundary check on AI-vendor mode**: the platform has an embedded AI feature, but it is off. The skill must avoid pulling the AI overlay in by reflex. The right answer is `ai_vendor = false` now, with a note that re-review is triggered if the feature is enabled.
- **Boundary check on cyber overlay**: cyber overlay applies even though the vendor is not categorised as a "cyber vendor". The skill must apply cyber by default to a vendor that touches NPI.
- **Boundary check on banking sector overlay**: examiner-access under Bank Service Company Act is a banking-only contract clause. Without the banking overlay, the skill misses the gap.
- **Boundary check on impact tolerance**: vendor RTO meets tolerance on paper. The skill must read whether the BCDR test evidence covers the failover scenario, not just the steady-state recovery objective.
- **Boundary check on concentration**: a single-vendor diligence pack is the right place to raise the flag, not to do the portfolio analysis.

#### Anchors

- Interagency Guidance on Third-Party Relationships: Risk Management (OCC/FRB/FDIC, June 2023).
- Bank Service Company Act, 12 USC §1867(c).
- 12 CFR Part 30 Appendix D (OCC Heightened Standards).
- FFIEC IT Examination Handbook — Outsourcing Technology Services.
- GLBA Safeguards Rule (16 CFR Part 314 as amended).

See `references/source-anchors.md` for full citations.

## troubleshooting

### Troubleshooting: vendor-diligence

Recurring pitfalls. Read before producing the pack and again before sign-off.

#### Generic vendor diligence

##### Treating procurement RFP responses as evidence

RFP responses are vendor self-attestation. Diligence requires inspectable artifacts: third-party audit reports, pen-test summaries, BCDR test reports, breach-notification logs, sub-processor lists, region-pinning evidence. If the only thing on file is RFP narrative, mark `cyber_evidence_status` and `bcdr_evidence_status` as `partial` or `missing` regardless of how confident the narrative reads.

##### Reading SOC 2 Type II as a green light

A clean SOC 2 opinion covers the auditor's selected criteria over the auditor's selected period. The diligence must read scope (which trust-services criteria), period (continuous coverage of the firm's onboarding window), exceptions (any noted, even minor), and complementary user entity controls (CUECs that the firm must implement for the vendor's controls to be effective). A clean SOC 2 with critical CUECs unaddressed is not a green light.

##### Setting RTO/RPO to the vendor's claim

The vendor's claim is the ceiling on what the vendor delivers. The firm's impact tolerance for the supported important business service is the test the vendor must meet. `bcdr_meets_firm_tolerance = true` only when the vendor's evidenced (not claimed) recovery objectives meet the firm's impact tolerance.

##### Skipping fourth-party visibility because the contract has flow-down clauses

Flow-down does not equal visibility. The pack must show what the firm actually knows about the subcontractor chain, where visibility stops, and what the change-notice mechanism is.

##### Skipping concentration because "it is just one vendor"

Concentration is sector-wide and portfolio-level, not vendor-by-vendor. Raise the flag here and pass the analysis to `concentration-risk-review`. Common single-vendor flags: hyperscaler region, sponsor-bank, BIN sponsor, claims TPA, transfer agent, foundation-model vendor.

##### Forgetting the exit-plan handoff

A critical or important vendor without a current exit plan is itself a finding. Always evidence `exit_plan_status`. If `missing`, add it to `open_evidence_gaps` and to the `reviewer_questions`.

##### Treating the diligence pack as the decision

The pack stops at the recommendation. The named approver decides under the firm's third-party-risk policy for the criticality tier. The skill outputs `recommended_decision`, not `decision`.

#### AI-vendor-specific pitfalls

##### Treating a published system card as a substitute for vendor-specific evidence on the firm's deployment context

A system card describes the model on the vendor's benchmarks and intended use. It does not describe how the model performs on the firm's prompts, customer data, regulatory context, or downstream decisioning. Mark `system_card_fit_to_deployment` honestly; `partial-fit` and `not-fit` are common outcomes for FNOL triage, claims chatbots, RAG over customer documents, and agent-driven workflows.

##### Accepting "we do not retain training data" without reading the contract and the trust-and-safety pages

The enterprise default is rarely the consumer default; the contract addendum and the trust-and-safety pages set the operative posture. The diligence cites the contractual data-handling commitment and the abuse-monitoring exception, not the marketing default. Common pattern: enterprise default disables training use but retains a rolling abuse-monitoring window under a published exception. That is a privacy fact and lands in `ai_specific_findings.training_data_posture` and the privacy overlay read.

##### Treating evaluation evidence on the base model as coverage for the deployed system

The deployed system is base + fine-tune + RAG + retrieval + carrier-side guardrails. Evaluation must cover the deployed system, including retrieval quality and grounding behavior. Set `eval_coverage_on_deployed_system = false` as the default; flip to `true` only when deployment-context evals are evidenced.

##### Skipping the prompt-as-customer-data privacy lens

Customer prompts can carry NPI, PHI, PCI, or other regulated data the firm did not intend to share. Privacy overlay applies to AI vendors by default. Always populate `ai_specific_findings.prompt_as_customer_data_assessment`. HIPAA business-associate analysis is required where PHI may incidentally appear in narratives.

##### Confusing the boundary with `llm-vendor-evidence-review`

`vendor-diligence` is the firm-side TPRM wrapping (criticality, cyber, BCDR, financial condition, contract, exit, concentration, with the AI overlay layered on). `llm-vendor-evidence-review` (in `ai-governance-model-risk`) is the model-risk lens on whether the published evidence pack is sufficient for the firm's deployment context. Hand off via `ai_specific_findings.eval_evidence_status = deferred-to-evidence-review` and the linked record ID. Do not duplicate model-risk analysis here.

##### Missing the model-version pin and deprecation-notice clock

For foundation-model vendors, the deployed checkpoint is a moving target. The contract must address model-version pinning and deprecation-notice timing; the operational change-management process must consume the notice. Re-review trigger on a model-version change is part of the AI overlay; that is not the default for a non-AI vendor.

##### Treating an "embedded AI feature" as automatically AI-vendor mode

If the AI feature is off and the firm has no plan to turn it on, the diligence is not in AI-vendor mode. Mark `ai_vendor = false` and add a re-review trigger if the feature is enabled. Do not pull the AI overlay in by reflex.

##### Reading shared-responsibility as "the vendor is responsible"

Shared responsibility is a split, not a transfer. Prompt-injection defence, retrieval-quality, downstream-decisioning quality, and incident-response cooperation are usually firm responsibilities or shared. Set `shared_responsibility_clarity` honestly; `partial` and `unclear` are common.

#### Engagement-scope pitfalls

##### Running without scope

If the scope record is missing, ask the four questions (institution type, primary regulator(s), persona/audience, source posture) and default to public posture if the practitioner declines. Note in the artifact that scope was not formalised. Do not silently apply a default sector overlay.

##### Loading the wrong sector overlay

Institution type and primary regulator constellation determine the sector overlay set. Banking is not insurance is not capital markets is not payments-fintech. A dual-registrant or a fintech with a sponsor bank may need two overlays. Do not collapse to one.

##### Skipping cyber or privacy because "it is not a cyber or privacy vendor"

Cyber applies whenever the vendor touches NPI, PHI, PCI, customer prompts, or any control on the firm's important-business-service path. Privacy applies whenever the vendor processes regulated personal data, including customer prompts. Both default-on for AI vendors.

#### Output discipline

##### Citing without sections

Every regulator citation in the pack carries a section reference or a `[verify section]` placeholder. URL alone fails the source-anchor depth check. Use `references/source-anchors.md` for the canonical citation set; do not restate excerpts in the pack body.

##### Marking unsupported claims silently

Use `[evidence needed]` explicitly. An inferred claim presented as evidenced is the failure mode.

##### Closing with too much certainty

The confidence label is `high` only when the source posture, the evidence set, and the residual-risk read line up. `medium` and `low` are normal for early-stage diligence; `unknown` is honest where the firm has not yet resourced the evidence ask.
