# Troubleshooting: ai-use-case-intake

Recurring defects in intake records. The intake is the front-door artefact; defects here propagate into every downstream skill that consumes the record. This file is for second-line reviewers and AI Governance Leads challenging an intake before attestation, and for senior practitioners self-reviewing their own draft.

## Foundation-model identity is missing or vague

Symptom: the intake records `model_type = foundation_model` but the foundation-model identity block is empty, vague ("vendor LLM"), or missing the version and pinning posture.

Root cause: the model owner submitted the intake without confirming with the build team which foundation model is in use, or the build team treated the foundation model as an implementation detail.

Fix: the foundation-model identity (provider, model name, version, pinning posture) is load-bearing for `ai-risk-tiering`, `model-card-builder`, `validation-plan`, `prompt-injection-risk`, `rag-evaluation-review`, `genai-pre-prod-review`, and `llm-vendor-evidence-review`. Hold the intake at "accept with conditions" until the block is filled. "Pinned with floating on minor patches" is a different posture from "rolling without notice" and the intake distinguishes them.

## Autonomy level is "human-in-the-loop" but the human review point is rubber-stamp at scale

Symptom: the intake records `autonomy_level = human_in_loop` and the evidence-of-effective-oversight field says "the staff member reviews the output before any use." On inspection, the staff member approves at scale without inspecting (button-push approval; tens of decisions per minute).

Root cause: the intake is recording the existence of a button rather than the evidence that the human review point is effective oversight under NIST Map 3.5 and EU AI Act Article 14.

Fix: surface the autonomy posture as `human_on_loop` or `fully_automated` based on observed behavior, and route an open question to `validation-plan` to test the effective-oversight evidence. Where the evidence is genuinely thin, flag the autonomy level as an open question rather than over-claiming the human-in-the-loop label. The intake is honest about what is observed; the gap is the work product, not a defect to hide.

## Data sensitivity tagged source-level instead of field-level

Symptom: a data source labelled "CRM extract — internal" turns out to contain regulated NPI fields (account numbers, signatory data, customer financial position) inside an otherwise internal aggregate source.

Root cause: source-level tagging is faster, but it hides exposure inside aggregate sources. The downstream tier reviewer cannot score data sensitivity off a source-level tag alone.

Fix: any data source flagged regulated NPI, regulated PHI, regulated PCI, or biometric requires field-level tagging in the `field_level_tagging` field. Hold the intake until the field-level breakout is supplied for each regulated source. The field-level breakout also feeds the privacy overlay's vendor-flow-down questions.

## Sponsor has been pushing the tier downward

Symptom: the preliminary-tier proposal is tier-3 or tier-4 on a use case that has customer-binding decisions, regulated NPI, foundation-model dependence, or multi-state DOI reach. The rationale is thin or names "low complexity" or "internal-use only" without engaging with the customer or regulatory dimensions.

Root cause: a low tier reduces validation depth, reduces gate count, and accelerates time-to-deployment. Sponsor pressure runs both directions; downward is the more frequent direction at intake.

Fix: capture the proposal as the sponsor's view; do not edit it down. The formal tier is decided by `ai-risk-tiering` against the intake record, and the dissent line in the tier decision records the disagreement when it stands. Route an open question to `ai-risk-tiering` flagging the contested factors (customer impact, regulatory impact, GenAI block) so the tier reviewer is on notice.

## GenAI overlay block is empty on a foundation-model intake

Symptom: the intake records `model_type = foundation_model` or `uses_rag = true` or `uses_tools = true`, but the GenAI block (foundation-model identity, RAG corpora and refresh cadence, tool inventory and tool-boundary controls) is sparse or absent.

Root cause: the intake template was filled in linearly without checking whether the architecture flags fired the overlay; the model owner did not know the GenAI block was mandatory once triggered.

Fix: missing the GenAI block on a GenAI intake is what `ai-risk-tiering` flags first when the record lands. Hold the intake at "accept with conditions" until the GenAI block is filled. The block is mandatory once any of the three architecture flags fires.

## Open-questions list is empty on a non-trivial use case

Symptom: the intake's open-questions table is empty on a tier-2 or tier-1 candidate use case with foundation-model dependence, regulated data, or customer-binding posture.

Root cause: either the use case is genuinely tier-4 with no exposure (rare for any use case worth intaking), or the open questions were sanitised to make the intake look clean. Senior reviewers look for the second case more than the first.

Fix: open questions are not defects; they are the work-in-flight handoff to downstream skills. Surface the questions that actually exist with their downstream-skill routing destinations and owners. A clean intake with an empty open-questions list reads to a senior reviewer as a tell that the conversation has not happened.

## Vendor dependency block records a vendor without the change-of-version posture

Symptom: a foundation-model vendor or an ECDIS vendor is named with role and criticality, but the change-of-version notice posture and the firm-side fallback are blank.

Root cause: the contract addendum was not consulted; the build team treated the vendor as a black box.

Fix: change-of-version notice is the operative resilience posture for any vendor whose model behaviour can shift outside the firm's change-control loop. Pull the contract clause and record the posture (e.g., "30-day notice on major version; 7-day on minor patches; rolling not allowed"). Where the contract is silent, flag as an open question for `vendor-diligence` and consider holding the intake.

## EU AI Act Annex III overlap was not flagged

Symptom: the intake is for a US-based credit-decisioning use case, life-insurance underwriting use case, or biometric-identification use case, but the AI Act overlap block reads `high_risk_overlap_likely = false` or is empty.

Root cause: the model owner thought "we don't operate in the EU" was the test for AI Act applicability; in fact the test is whether the use case category is in scope under Article 6 / Annex III, and the routing flag belongs in the intake regardless of EU footprint today.

Fix: the AI Act block in the intake is the routing flag, not the formal classification. The formal classification is owned by `ai-act-triage`. Capture the Annex III category overlap (creditworthiness assessment of natural persons §5(b), risk assessment and pricing in life and health insurance §5(c), biometric identification §1) regardless of EU footprint, and route to `ai-act-triage` for the formal call. The overlap flag also serves as a re-look prompt if EU footprint enters scope.

## Intake is dated more than a quarter old with no version bump

Symptom: the use case is in active production, has had scope or vendor changes, but the intake record is the v1.0 from six months ago.

Root cause: the intake is being treated as a one-time form rather than a living record; the change plan was either blank or not monitored.

Fix: the intake is a living record. A new version is recorded at any of: scope change, autonomy change, customer-surface change, vendor change, regulatory-environment change, lifecycle stage transition. The change-plan field is what catches drift before the use case grows beyond its intake. Where the intake is stale, hold any downstream re-tier or model-card refresh until the intake is re-versioned.

## Sector overlay was loaded but the overlay-specific fields are not in the intake

Symptom: the intake records `overlay_flags = ["banking"]` but the banking-specific intake fields (federal regulator, supervisory cycle posture, BSA officer linkage where applicable, sponsor-bank arrangement counterparty, stress-testing pedigree, risk-appetite-statement linkage) are absent.

Root cause: the overlay was loaded as a routing signal for downstream skills, but the overlay's intake-side fields were not consulted at intake time.

Fix: when an overlay is loaded, the overlay's named fields land in the intake. Treating the overlay as background reading is the failure mode. Each sector overlay (`references/sector-overlays/<sector>.md`) lists the sector-specific intake fields; consult the overlay file when filling the intake.

## Source trace collapses vendor and firm evidence into one line

Symptom: a claim about the foundation model's training-data provenance, fairness evaluation, or safety testing is recorded with `confidence = high` and the source is "vendor".

Root cause: vendor-supplied facts about the vendor's own model carry vendor-self-attestation confidence (typically low to medium); firm-controlled facts carry higher confidence. Collapsing them hides the seam.

Fix: separate vendor-self-attestation evidence from firm-independent evaluation evidence in the source trace. Confidence labels on vendor-supplied facts max at medium absent firm-side independent verification; firm-controlled facts (own contracts, own data classification register, own monitoring rubrics) can be high. The seam between vendor and firm evidence is what `llm-vendor-evidence-review` works against downstream.

## Intake is being filed on a use case that should re-route to a different skill

Symptom: the intake is being attempted on a use case that has already been intaked and tiered, and the question is the model card or validation plan; or the work is procurement-stage diligence on an AI vendor before any internal use case exists; or the artifact required is the EU AI Act Annex IV technical documentation.

Root cause: the wrong skill was reached for; the intake is the front door but it is not the only door.

Fix: route the work. If the use case is intaked and tiered and the next artifact is the model card, route to `model-card-builder`. If procurement-stage diligence is needed, route to `vendor-diligence` in `third-party-operational-resilience` with the AI-vendor scenario mode. If Annex IV technical documentation is the artifact, route to `ai-act-triage` to scope the deltas the firm carries. The intake skill is for use cases that need the front-door record; do not force-fit it where another skill owns the work.
