---
name: contract-gap-review
description: "Review a vendor contract against regulatory clause expectations and report the gaps."
argument-hint: "[contract or MSA: vendor name, criticality tier, sector, AI-vendor flag]"
---

# Contract gap review

A contract gap review is what second-line produces so the named approver, head of TPRM, head of procurement, general counsel, business-owner SVP, can decide whether the contract is fit to sign, renew, or amend. The work is reading the contract against the firm's regulatory and operational frame, naming each clause that is present, partial, absent, or not-applicable, and writing the remediation posture the legal team will redline against. The skill stops at the gap matrix and the legal-review triggers. Counsel drafts language. The approver decides.

This skill produces the gap matrix as a markdown artifact (`templates/default-output.md` shape) and a structured record (`schemas/contract-gap-review.schema.json`) that downstream skills consume. Both pre-signature negotiation and the renewal or amendment cycle use the same workflow. The mandatory-clause overlay flips on for any contract that supports a critical-or-important function under the EU digital-operational-resilience act.

## When to use

Reviews a third-party contract or master services agreement against named regulatory clause-coverage expectations and produces a clause-by-clause gap matrix with severity, remediation posture, and the legal-review triggers a control owner needs before signature, renewal, or assignment. Output is the second-line clause-coverage view that sits next to (not in place of) legal redlines.

Best for:
- A new vendor contract is in negotiation and the firm needs the second-line clause-coverage view before legal redlines land.
- Renewal, assignment, or material amendment of an existing contract triggers a refresh against current regulatory expectations.
- A digital-operational-resilience preparation cycle requires evidence that critical-or-important-function ICT contracts meet the mandatory-clause set.
- A vendor-diligence pack needs the contract-coverage section closed out (chains via `contract_gap_summary`).

Not the right tool when:
- The criticality tier has not been set (run `criticality-assessment` first; clause depth and the mandatory-clause overlay depend on tier).
- The work is the full diligence pack rather than the contract layer (use `vendor-diligence`).
- The work is exit and termination logistics rather than clause coverage (use `exit-plan`).
- The work is portfolio-level concentration across many contracts (use `concentration-risk-review`).

## Ask first

Before drafting, get plain answers to four things. Most engagements answer them in the first conversation; if not, default and flag.

- **What tier is the arrangement.** Sourced from `criticality-assessment`. Do not re-set it here. Tier drives clause depth and which mandatory-clause overlay loads. A non-critical arrangement gets a lighter pass on operational-resilience and exit clauses; a critical arrangement gets the full set with reviewer questions clustered for the forum that decides.
- **Is the arrangement in scope of the EU digital-operational-resilience act as a critical-or-important-function ICT service.** Treat as a boolean. The mandatory-clause overlay is a real branch, not a side-note: when on, the gap matrix surfaces the enhanced clause set (termination triggers tied to supervisory recommendation, full description of services, locations of data processing, sub-outsourcing notification timing, exit-strategy and transitional support, audit-and-access for the firm and the competent authority).
- **What is the firm's regulatory profile.** Institution type and primary regulators determine which sector overlay loads. Banking is not insurance is not capital markets is not payments-fintech. A dual-registrant or a sponsor-bank-program contract may need two sector overlays; flag the choice.
- **What is the review type.** Pre-signature, renewal, assignment or change-of-control, material amendment, exit-triggered re-review, post-incident re-review, regulatory-change-driven re-review. Each carries a different evidence-ask and a different decision-forum context.

When `scope` is supplied, the skill consumes it (institution type, sector overlay set, cross-cutting overlay set, persona, source posture). When it is not supplied, ask the four questions and default to public posture if the practitioner declines. Note in the artifact that scope was not formalised; do not silently apply a default sector overlay.

## How the gap matrix gets built

The matrix has the same spine across contract types. A senior reviewer fills it row by row, working off the contract document and the loaded overlays. Order follows the conversation, not a lockstep sequence.

The frame opens with the arrangement: vendor, contract identifier (MSA, SOW, order form, addenda), the criticality tier read from `criticality-assessment`, the supported business process and (where the firm has an IBS map) the important business service, the data scope (NPI, PHI, PCI, customer prompts, model outputs, training data, logs), the data locations and any cross-border flows, the AI-vendor flag, and the digital-operational-resilience-act in-scope flag. Both flags are set at the top; if either is true, the corresponding overlay is default-on for the rest of the matrix regardless of how the scope `cross_cutting_overlay_set` reads.

The clause-coverage matrix is the body. Every clause topic the regulatory frame names gets a row. The standard clause set spans scope and performance, responsibilities for compliance with applicable laws, audit and reporting rights including regulator examination access, ownership and licences, business-resumption and contingency, sub-contracting, confidentiality and information security, indemnification, limits on liability, insurance, dispute resolution, default and termination, and regulator-access continuity. For each row the matrix records the clause topic, the source criterion with section reference (or `[verify section]`), the contract reference (clause or section number), the coverage status (`present`, `partial`, `absent`, `not-applicable`), the gap rationale in plain language, the recommended-amendment posture (a posture, not legal language), and the severity (`low`, `medium`, `high`).

Reading the contract is where the matrix earns its keep. Each clause status is a finding, not a checkbox. "Right to audit subject to reasonable cooperation" reads as a reservation of vendor discretion, not as audit rights; mark as `partial` and surface the missing scope, frequency, cost-allocation, and remedy when the auditor's findings dispute vendor representations. "Industry-standard SLA" reads as below the firm's tolerance until proven otherwise; compare against the criticality output's RTO and RPO tolerance, not the vendor's default. "Notification of cybersecurity events within a reasonable period" reads against the tightest applicable clock (the firm's public-company materiality determination window where listed; the New York State 72-hour cybersecurity-event-notification clock where the firm is a covered entity; the EU digital-operational-resilience-act major-ICT-related-incident reporting timetable where in scope); flag the contract-clock-versus-regulatory-clock gap and the upstream notification-chain breakage. "Sub-processor flow-down" reads as a contractual mechanic, not visibility; the contract should also require sub-processor identification, change notification, and rejection rights. Limit-of-liability caps below the firm's expected loss are a finding, not a deal-closer.

The mandatory-clause overlay, when the arrangement is in scope of the EU digital-operational-resilience act as a critical-or-important-function service, populates the enhanced clause rows. The high-leverage items: termination rights tied to supervisory recommendation; full description of services; locations of data processing and storage; sub-outsourcing notification timing and rejection rights; exit-strategy and transitional support; audit-and-access rights for the firm and the competent authority. These are mandatory-by-source; absence is a `high`-severity finding regardless of the firm's bilateral position.

The cyber clause cluster carries notification timing, cooperation on incident response, encryption posture in-transit and at-rest, key-management model, vulnerability-management cooperation, pen-test rights, and shared-responsibility-model articulation for cloud arrangements. The privacy clause cluster carries data-processing-agreement coverage, sub-processor change-notice and rejection, deletion-and-return, retention windows, cross-border-transfer mechanism, and (where PHI is in scope) HIPAA business-associate-agreement execution. The AI clause cluster, when `ai_vendor=true`, carries training-data-use commitments, abuse-monitoring exception scope, model-version pin and deprecation-notice clock, evaluation-evidence access, agent-tool sandbox and audit-trail commitments, and incident-notification timing on a model-safety incident.

The matrix closes with the legal-review triggers, the open questions for the contract owner, and the reviewer questions clustered for the forum that decides (TPRM forum for an operational arrangement, risk committee for a critical vendor, AI risk committee for an AI vendor, fund board where the arrangement sits inside a registered fund). The summary severity is the highest individual-clause severity, except where two or more `medium` findings concentrate in a single cluster (audit, termination, incident-notification) and lift the summary to `high` by aggregation.

## Chaining

The skill is downstream of `criticality-assessment` (consumes the tier) and `vendor-diligence` (the diligence pack's `contract_gap_summary` carries a one-paragraph headline plus a pointer to the record produced here). It chains upstream to `exit-plan` (the termination, exit, and transitional-support clauses produced here are read by the exit-plan workflow) and to `dora-register-builder` (the mandatory-clause coverage flags feed the register entries where the arrangement is in scope). Where the diligence pack is being built in parallel, the contract record's `contract_gap_record_id` is the link the diligence pack writes back into `contract_gap_summary`.

## Quality bar

Holds across every gap matrix regardless of contract type, audience, or render format. Every material clause finding cites a source from `references/source-anchors.md` (or a loaded overlay) by path. Unsupported findings are marked `[evidence needed]`. Section references that cannot be confirmed get `[verify section]` rather than fabricated. Source criterion, contract excerpt, generated inference, and open legal question stay distinguishable in the matrix. No named institutions in narrative unless they are public defendants in a finalised enforcement action with a published consent order. The skill stops at the gap matrix and the legal-review triggers. Counsel drafts language; the approver decides. RFP narrative is not evidence, anywhere.

## Adaptation

Flexes by engagement. Matrix depth and length scale to criticality and review type. Audience drives shape: a TPRM-forum matrix reads short and operational; a risk-committee matrix for a critical vendor reads longer with reviewer questions clustered for the forum; a general-counsel-facing matrix reads as a redline-readiness brief. The sector overlay set drives which `references/sector-overlays.md#<sector>` is loaded; a dual-registrant or sponsor-bank-program arrangement may load two. Cross-cutting overlay loading follows scope plus the rule that cyber and privacy default-on for AI vendors and for any contract touching NPI, PHI, PCI, or important-business-service controls. The mandatory-clause overlay loads only when the digital-operational-resilience-act in-scope flag is true. Render format (Word, Excel, PowerPoint, Markdown) follows the workflow.

## Pointers

`references/sector-overlays.md` and `references/cross-cutting.md` hold one section per sector or topic, and `examples.md` one per example. Find the heading and read only that section.

- `references/source-anchors.md` — citations and excerpts for the named anchors.
- `references/sector-overlays.md#banking`, `insurance.md`, `capital-markets.md`, `payments-fintech.md` — sector-specific clause expectations loaded per scope.
- `references/cross-cutting.md#cyber`, `privacy.md` — cross-cutting clause clusters; default-on for AI vendors and for any contract touching regulated data or IBS controls.
- `references/firm-overlay.md` — firm-installed contract policy, paper standards, named legal-review forums beyond the regulatory baseline; consumed when present.
- `templates/default-output.md` — gap matrix template.
- `schemas/contract-gap-review.schema.json` — structured-output contract for downstream consumption.
- `examples.md` — cloud IaaS contract for a regional U.S. bank; digital-operational-resilience-act-in-scope SaaS contract for an EU subsidiary's collections platform.
- `examples.md#troubleshooting` — recurring pitfalls (audit-rights reservation, notification-clock mismatch, sub-processor flow-down conflated with visibility, exit clauses skipped on non-critical, liability cap below expected loss, mandatory-clause overlay missed).

The plugin-level shared references (`references/source-map.md`, `references/policy-control-library.md`, `references/review-gates.md`) sit at the plugin root and are consulted alongside the skill-level files.

## Output

The deliverable is the contract gap matrix. Default to drafting against `templates/default-output.md`. Render as Word, Excel, PowerPoint, or Markdown when the audience or workflow asks for it (a redline-readiness brief for counsel may want Word; a clause-by-clause portfolio cut may want a workbook; a critical-vendor risk-committee read may want a deck). Produce the structured record at `schemas/contract-gap-review.schema.json` when downstream automation or a registered consumer needs it.

Downstream consumers: `vendor-diligence` reads the record summary into `contract_gap_summary` and `contract_gap_record_id`; `exit-plan` reads the termination, transitional-support, and data-return clause findings; `dora-register-builder` reads the mandatory-clause coverage flags for the ICT-third-party register entries where the act applies; `concentration-risk-review` reads the sub-contracting and change-of-control findings where the portfolio analysis needs them.

When the structured record is produced, treat the schema as a downstream contract: additive changes only. Add fields, do not rename or repurpose them. A breaking change is a versioned migration with the downstream skills told in advance.

## Human review and AI disclosure

Open the deliverable with this line, and remove it only after the review below: `AI-assisted draft. Requires review by a qualified person before use.`

A qualified person with authority to change the output reviews it before it is delivered or relied on, and stays accountable for it. Where the output supports advice to an individual or a decision about an individual (credit, insurance underwriting, pricing or claims, employment, legal rights, or similar), that individual must be told AI was used to produce it. This skill does not make final decisions, file with a regulator, notify customers, execute transactions, or move money or other financial assets.
