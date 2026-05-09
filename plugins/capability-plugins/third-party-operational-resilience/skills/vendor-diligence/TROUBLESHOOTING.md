# Troubleshooting: vendor-diligence

Recurring pitfalls. Read before producing the pack and again before sign-off.

## Generic vendor diligence

### Treating procurement RFP responses as evidence

RFP responses are vendor self-attestation. Diligence requires inspectable artifacts: third-party audit reports, pen-test summaries, BCDR test reports, breach-notification logs, sub-processor lists, region-pinning evidence. If the only thing on file is RFP narrative, mark `cyber_evidence_status` and `bcdr_evidence_status` as `partial` or `missing` regardless of how confident the narrative reads.

### Reading SOC 2 Type II as a green light

A clean SOC 2 opinion covers the auditor's selected criteria over the auditor's selected period. The diligence must read scope (which trust-services criteria), period (continuous coverage of the firm's onboarding window), exceptions (any noted, even minor), and complementary user entity controls (CUECs that the firm must implement for the vendor's controls to be effective). A clean SOC 2 with critical CUECs unaddressed is not a green light.

### Setting RTO/RPO to the vendor's claim

The vendor's claim is the ceiling on what the vendor delivers. The firm's impact tolerance for the supported important business service is the test the vendor must meet. `bcdr_meets_firm_tolerance = true` only when the vendor's evidenced (not claimed) recovery objectives meet the firm's impact tolerance.

### Skipping fourth-party visibility because the contract has flow-down clauses

Flow-down does not equal visibility. The pack must show what the firm actually knows about the subcontractor chain, where visibility stops, and what the change-notice mechanism is.

### Skipping concentration because "it is just one vendor"

Concentration is sector-wide and portfolio-level, not vendor-by-vendor. Raise the flag here and pass the analysis to `concentration-risk-review`. Common single-vendor flags: hyperscaler region, sponsor-bank, BIN sponsor, claims TPA, transfer agent, foundation-model vendor.

### Forgetting the exit-plan handoff

A critical or important vendor without a current exit plan is itself a finding. Always evidence `exit_plan_status`. If `missing`, add it to `open_evidence_gaps` and to the `reviewer_questions`.

### Treating the diligence pack as the decision

The pack stops at the recommendation. The named approver decides under the firm's third-party-risk policy for the criticality tier. The skill outputs `recommended_decision`, not `decision`.

## AI-vendor-specific pitfalls

### Treating a published system card as a substitute for vendor-specific evidence on the firm's deployment context

A system card describes the model on the vendor's benchmarks and intended use. It does not describe how the model performs on the firm's prompts, customer data, regulatory context, or downstream decisioning. Mark `system_card_fit_to_deployment` honestly; `partial-fit` and `not-fit` are common outcomes for FNOL triage, claims chatbots, RAG over customer documents, and agent-driven workflows.

### Accepting "we do not retain training data" without reading the contract and the trust-and-safety pages

The enterprise default is rarely the consumer default; the contract addendum and the trust-and-safety pages set the operative posture. The diligence cites the contractual data-handling commitment and the abuse-monitoring exception, not the marketing default. Common pattern: enterprise default disables training use but retains a rolling abuse-monitoring window under a published exception. That is a privacy fact and lands in `ai_specific_findings.training_data_posture` and the privacy overlay read.

### Treating evaluation evidence on the base model as coverage for the deployed system

The deployed system is base + fine-tune + RAG + retrieval + carrier-side guardrails. Evaluation must cover the deployed system, including retrieval quality and grounding behavior. Set `eval_coverage_on_deployed_system = false` as the default; flip to `true` only when deployment-context evals are evidenced.

### Skipping the prompt-as-customer-data privacy lens

Customer prompts can carry NPI, PHI, PCI, or other regulated data the firm did not intend to share. Privacy overlay applies to AI vendors by default. Always populate `ai_specific_findings.prompt_as_customer_data_assessment`. HIPAA business-associate analysis is required where PHI may incidentally appear in narratives.

### Confusing the boundary with `llm-vendor-evidence-review`

`vendor-diligence` is the firm-side TPRM wrapping (criticality, cyber, BCDR, financial condition, contract, exit, concentration, with the AI overlay layered on). `llm-vendor-evidence-review` (in `ai-governance-model-risk`) is the model-risk lens on whether the published evidence pack is sufficient for the firm's deployment context. Hand off via `ai_specific_findings.eval_evidence_status = deferred-to-evidence-review` and the linked record ID. Do not duplicate model-risk analysis here.

### Missing the model-version pin and deprecation-notice clock

For foundation-model vendors, the deployed checkpoint is a moving target. The contract must address model-version pinning and deprecation-notice timing; the operational change-management process must consume the notice. Re-review trigger on a model-version change is part of the AI overlay; that is not the default for a non-AI vendor.

### Treating an "embedded AI feature" as automatically AI-vendor mode

If the AI feature is off and the firm has no plan to turn it on, the diligence is not in AI-vendor mode. Mark `ai_vendor = false` and add a re-review trigger if the feature is enabled. Do not pull the AI overlay in by reflex.

### Reading shared-responsibility as "the vendor is responsible"

Shared responsibility is a split, not a transfer. Prompt-injection defence, retrieval-quality, downstream-decisioning quality, and incident-response cooperation are usually firm responsibilities or shared. Set `shared_responsibility_clarity` honestly; `partial` and `unclear` are common.

## Engagement-scope pitfalls

### Running without scope

If the scope record is missing, ask the four questions (institution type, primary regulator(s), persona/audience, source posture) and default to public posture if the practitioner declines. Note in the artifact that scope was not formalised. Do not silently apply a default sector overlay.

### Loading the wrong sector overlay

Institution type and primary regulator constellation determine the sector overlay set. Banking is not insurance is not capital markets is not payments-fintech. A dual-registrant or a fintech with a sponsor bank may need two overlays. Do not collapse to one.

### Skipping cyber or privacy because "it is not a cyber or privacy vendor"

Cyber applies whenever the vendor touches NPI, PHI, PCI, customer prompts, or any control on the firm's important-business-service path. Privacy applies whenever the vendor processes regulated personal data, including customer prompts. Both default-on for AI vendors.

## Output discipline

### Citing without sections

Every regulator citation in the pack carries a section reference or a `[verify section]` placeholder. URL alone fails the source-anchor depth check. Use `references/source-anchors.md` for the canonical citation set; do not restate excerpts in the pack body.

### Marking unsupported claims silently

Use `[evidence needed]` explicitly. An inferred claim presented as evidenced is the failure mode.

### Closing with too much certainty

The confidence label is `high` only when the source posture, the evidence set, and the residual-risk read line up. `medium` and `low` are normal for early-stage diligence; `unknown` is honest where the firm has not yet resourced the evidence ask.
