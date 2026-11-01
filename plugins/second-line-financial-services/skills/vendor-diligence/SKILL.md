---
name: vendor-diligence
description: "Draft a vendor due diligence pack for an ICT, fintech, cloud, data, or AI provider."
argument-hint: "[arrangement: vendor name, service, criticality, deployment context]"
---

# Vendor diligence

A vendor diligence pack is what second-line produces so the named approver, head of TPRM, head of operational resilience, CISO, AI governance lead, business-owner SVP, can decide. The work is reading vendor evidence against the firm's regulatory and operational frame, separating what was inspected from what was claimed, and naming the gaps that have to close before onboarding or recertification. The skill stops at the recommendation. The approver decides.

This skill produces the pack as a markdown artifact (`templates/default-output.md` shape) and a structured record (`schemas/vendor-diligence.schema.json`) that downstream skills consume. Both onboarding diligence and the periodic recertification cycle use the same workflow; the AI-vendor branch flips on for any AI or AI-adjacent provider and surfaces a conditional `ai_specific_findings` block.

## When to use

Drafts a second-line vendor diligence pack for a single ICT, fintech, cloud, data, or AI service provider. Captures inherent risk, criticality input, due-diligence evidence read against named regulatory criteria, residual risk, exit posture, and the gaps a control owner needs to close before onboarding or recertification. Handles AI vendors via an explicit AI-vendor branch in the same workflow.

Best for:
- A first-line owner has proposed a new ICT, fintech, cloud, data, or AI vendor and second-line needs the pre-onboarding pack.
- A vendor risk team is recertifying an existing critical or important vendor and the prior pack is stale.
- An AI vendor (foundation-model API, AI SaaS, embedded-AI feature, agentic system) needs diligence with the second-line lens, not a procurement checklist.
- An exit-triggered or post-incident re-review of an existing vendor.

Not the right tool when:
- The criticality tier has not been set (run `criticality-assessment` first).
- The job is portfolio-level concentration across many vendors (use `concentration-risk-review`).
- The job is contract clause coverage only (use `contract-gap-review`).
- The vendor evidence is a published system card or model report and the question is "is this evidence pack sufficient for our deployment context" — that narrower question goes to `llm-vendor-evidence-review` in `ai-governance-model-risk`. This skill is the firm-side TPRM wrapper.

## Ask first

Before drafting, get plain answers to four things. Most engagements answer them quickly; if not, default and flag.

- **What tier is the vendor.** Sourced from `criticality-assessment`. Do not re-set it here. Tier drives diligence depth: a not-critical vendor gets a shorter pack; a critical vendor gets full depth with reviewer questions clustered for the relevant forums.
- **Is this AI or AI-adjacent.** Treat as a boolean. The AI-vendor branch is a real branch, not a side-note: it conditionally surfaces `ai_specific_findings` and pulls the cyber and privacy overlays in by default. An embedded AI feature that is *off* is not AI-vendor mode; flag re-review on enablement.
- **What is the firm's regulatory profile.** Institution type and primary regulators. Banking is not insurance is not capital markets is not payments-fintech. A dual-registrant or a fintech with a sponsor bank may need two sector overlays.
- **What is the engagement type.** Pre-onboarding, annual recertification, off-cycle trigger, exit-triggered re-review, post-incident re-review, scope-change re-review. Each carries a different evidence-ask and a different decision-forum context.

When `scope` is supplied, the skill consumes it (institution type, sector overlay set, cross-cutting overlay set, persona, source posture). When it is not supplied, ask the four questions and default to public posture if the practitioner declines. Note in the pack that scope was not formalised; do not silently apply a default sector overlay.

## How the pack gets built

The pack has the same spine across vendor types. A senior reviewer fills it in roughly in the order the engagement and the vendor offer evidence, not in a lockstep sequence.

The frame opens with the arrangement: vendor, service, criticality (read from `criticality-assessment`), the supported business process and, if the firm has an IBS map, the important business service. Data scope is named explicitly: NPI, PHI, PCI, customer prompts, model outputs, training data, logs. Data locations and any cross-border flows go here. The `ai_vendor` flag is set at the top; if true, cyber and privacy overlays are default-on for the rest of the pack regardless of how the scope `cross_cutting_overlay_set` reads.

Evidence collection is risk-based. The depth scales to criticality and review type. The standard ask is audited financials (or public filings, D&B, credit rating, runway disclosure for early-stage), SOC 2 Type II (full report, not the short-form summary), ISO/IEC 27001 certificate with the Statement of Applicability, current pen-test summary, vulnerability-management evidence (cadence, MTTR by severity, exception register), BCDR test reports with evidenced recovery objectives, the privacy program (data-processing register, sub-processor list, incident history), the sub-contractor and fourth-party register, and the regulatory and legal posture (sanctions, enforcement, litigation, registrations). For an AI vendor add the published system card or model report, the evaluation report, the red-team summary, the trust-and-safety pages, and the contract addenda on training-data use and abuse monitoring.

Reading the evidence is where the pack earns its keep. Each evidence area gets a status (`sufficient`, `partial`, `missing`, `not-applicable`) and a short note on what was actually inspected. SOC 2 scope and complementary user-entity controls matter, not just the opinion. Vendor RTO/RPO claims are claims; evidenced recovery objectives are facts. Both are read against the firm's impact tolerance for the supported important business service, not against the vendor's published commitment; the vendor's number is the ceiling, not the test. Region-pin promises are promises; data-residency reports are evidence. RFP narrative is not evidence. The pack cites by file path into `references/source-anchors.md` and the loaded overlays; it does not restate excerpts in the body.

The AI overlay, when `ai_vendor=true`, populates `ai_specific_findings`. The high-leverage items: system card fit to deployment (a system card describes the model on the vendor's benchmarks; it does not describe how the model performs on the firm's prompts, customer data, regulatory context, or downstream decisioning); eval coverage on the deployed system (the deployed system is base + fine-tune + RAG + retrieval + carrier-side guardrails, default `false` unless deployment-context evals are evidenced); training-data posture read from contract and trust-and-safety, not the marketing default, with the abuse-monitoring exception scope surfaced; shared-responsibility clarity on prompt-injection defence, retrieval quality, downstream-decisioning quality, and incident-response cooperation, which usually sit firm-side or shared; the prompt-as-customer-data lens, including HIPAA business-associate posture if PHI may appear in narratives; and the model-version pin and deprecation-notice clock, because the deployed checkpoint is a moving target. Agent-tool posture sits next to these for any agentic vendor: agent scope, tool whitelisting, sandbox guarantees, prompt-injection-via-tool-output, and the firm-side guardrails the deployment must add are read here even when the vendor's published evidence pretends the controls are vendor-side. Where the question becomes "is the vendor's published evidence pack sufficient for our deployment context", set `eval_evidence_status = deferred-to-evidence-review`, chain to `llm-vendor-evidence-review` in `ai-governance-model-risk`, record the linked record ID, and do not duplicate model-risk analysis in this pack.

The lifecycle cross-links close the pack. `contract_gap_summary` carries a one-paragraph headline plus a pointer to `contract-gap-review` (a diligence pack without a contract-gap pointer is incomplete). `exit_plan_status` points to `exit-plan` (a critical or important vendor without a current exit plan is itself a finding). `concentration_flag` points to `concentration-risk-review` (raise the flag here, do the portfolio analysis there). For AI vendors, `ai_specific_findings.llm_vendor_evidence_review_record_id` carries the model-risk evidence-review record where chained.

The pack ends with the recommendation: `approve`, `approve-with-conditions`, `defer`, `decline`, or `escalate`. Conditions are specific and verifiable. Open evidence gaps name what was asked, what was not received, and by when. Reviewer questions tie to the decision and cluster for the forum that decides: TPRM forum for an operational arrangement, risk committee for a critical vendor, AI risk committee for an AI vendor, fund board where the arrangement sits inside a registered fund. Name the decision checkpoints the pack must clear (scope, evidence, authority, impact, decision) and the conditions attached to each. The named approver decides.

## Quality bar

Holds across every pack regardless of vendor type, audience, or render format. Every material claim cites a source from `references/source-anchors.md` (or a loaded overlay) by path. Unsupported claims are marked `[evidence needed]`. Section references that cannot be confirmed get `[verify section]` rather than fabricated. Source evidence, vendor management assertion, public-source obligation, generated inference, and open legal or compliance question stay distinguishable in the pack. No named institutions in narrative unless they are public defendants in a finalised enforcement action with a published consent order. The pack stops at the recommendation. RFP narrative is not evidence, anywhere.

## Adaptation

Flexes by engagement. Pack depth and length scale to criticality and review type. Audience drives shape: a TPRM-forum pack reads short and operational; a risk-committee pack for a critical vendor reads longer with reviewer questions clustered for the forum; a fund-board pack reads differently again. Lead with the decision the audience must make. The sector overlay set drives which `references/sector-overlays/<sector>.md` is loaded; a dual-registrant or BaaS arrangement may load two. Cross-cutting overlay loading follows scope plus the rule that cyber and privacy default-on for AI vendors and for any vendor touching NPI, PHI, PCI, or important-business-service controls. Source posture (public-only, public-plus-firm-policy, public-plus-firm-policy-plus-system-of-record-evidence, connector-aware) drives the evidence ask. AI-vendor sub-fields differ by use-case category (foundation-model API, AI SaaS, embedded-AI feature, agentic system, RAG application, fine-tuned model, specialised classifier). Render format (Word, Excel, PowerPoint, Markdown) follows the workflow.

## Pointers

- `references/source-anchors.md` — citations and excerpts for the named anchors.
- `references/sector-overlays/banking.md`, `insurance.md`, `capital-markets.md`, `payments-fintech.md` — sector-specific supervisory frame loaded per scope.
- `references/cross-cutting/cyber.md`, `privacy.md` — cross-cutting flavour; default-on for AI vendors and for any vendor touching regulated data or IBS controls.
- `references/firm-overlay.md` — firm-installed policy, taxonomy, decision forums and reviewer roles beyond the regulatory baseline; consumed when present.
- `templates/default-output.md` — pack template.
- `schemas/vendor-diligence.schema.json` — structured-output contract for downstream consumption.
- `examples/` — cloud IaaS for a regional bank's core deposit and loan platform; foundation-model API for a P&C insurer's first-notice-of-loss triage.
- `TROUBLESHOOTING.md` — recurring pitfalls (system-card-as-substitute, retention defaults, eval coverage, prompts-as-customer-data, the boundary with `llm-vendor-evidence-review`).

The plugin-level shared references (`references/source-map.md`, `references/policy-control-library.md`, `references/review-gates.md`) sit at the plugin root and are consulted alongside the skill-level files.

## Output

The deliverable is the vendor diligence pack. Default to drafting against `templates/default-output.md`. Render as Word, Excel, PowerPoint, or Markdown when the audience or workflow asks for it (a TPRM-forum read may want Word; a multi-vendor review cycle may want a workbook; an AI-risk-committee read may want a deck). Produce the structured record at `schemas/vendor-diligence.schema.json` when downstream automation or a registered consumer needs it.

The downstream chain stays the same regardless of render format. `contract-gap-review` reads the contract-coverage findings via `contract_gap_summary`. `exit-plan` reads `criticality`, `subcontractors`, `data_access`, and the residual-risk read. `concentration-risk-review` reads the `concentration_flag` and the sub-contractor footprint. `dora-register-builder` reads the structured fields for ICT-third-party register entries where DORA applies. `llm-vendor-evidence-review` reads the linked record where `eval_evidence_status = deferred-to-evidence-review`.

When the structured record is produced, treat the schema as a downstream contract: additive changes only. Add fields, do not rename or repurpose them. A breaking change is a versioned migration with the downstream skills told in advance.

## Human review and AI disclosure

Open the deliverable with this line, and remove it only after the review below: `AI-assisted draft. Requires review by a qualified person before use.`

A qualified person with authority to change the output reviews it before it is delivered or relied on, and stays accountable for it. Where the output supports advice to an individual or a decision about an individual (credit, insurance underwriting, pricing or claims, employment, legal rights, or similar), that individual must be told AI was used to produce it. This skill does not make final decisions, file with a regulator, notify customers, execute transactions, or move money or other financial assets.
