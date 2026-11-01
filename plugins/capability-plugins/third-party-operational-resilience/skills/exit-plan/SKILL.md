---
name: exit-plan
description: |
  Drafts the second-line exit plan for a critical or important third-party arrangement. Covers trigger events across vendor, firm, regulator, and market drivers; transition target options scored against impact tolerance; data return-and-destruction choreography; contract-termination mechanics; customer- and regulator-notice posture; supervisory readiness through a multi-month transition; testing cadence; named approver. Consumes the vendor-diligence record (criticality, subcontractors, data_access, residual_risk, exit_plan_status). Handles AI vendors via an explicit AI-vendor branch covering prompt-template portability, RAG migration, model-version pin handling, and agent-tool offboarding.

  Best for:
  - A new critical or important arrangement is being onboarded and the exit plan is required as part of pre-onboarding evidence.
  - Annual recertification of an existing critical or important vendor where the prior plan is stale, untested, or absent.
  - DORA preparation for critical-or-important-function arrangements where Article 28(8) requires a documented and tested exit strategy.
  - A concentration-risk-review or resilience-test surfaces a single point of failure and the exit posture needs hardening.
  - A vendor incident or distress signal opens an off-cycle re-review.

  Not the right tool when:
  - The criticality tier has not been set (run `criticality-assessment` first).
  - The arrangement is genuinely low risk and firm policy does not require a formal exit plan (record the rationale and stop).
  - The job is full diligence on the vendor (use `vendor-diligence`) or contract-clause coverage (use `contract-gap-review`).
  - The job is the integrated test programme across many arrangements (use `resilience-testing-pack`).
argument-hint: "[arrangement: vendor name, service, criticality, vendor-diligence record ID]"
---

# Exit plan

An exit plan is what second-line produces so the firm can transition out of a critical or important third-party arrangement under any plausible trigger, on a clock the supported important business service can absorb, with the data, customer, regulator, and audit posture intact. It is built once and tested on a schedule. The plan stops at the recommendation; the named approver, head of operational resilience or the IBS owner per firm policy, decides.

This skill produces the plan as a markdown artifact (`templates/default-output.md` shape) and a structured record (`schemas/exit-plan.schema.json`) that downstream skills consume. It chains into and out of `vendor-diligence` (consuming criticality, subcontractors, data access, residual risk), `contract-gap-review` (flagging clause gaps it surfaces), `concentration-risk-review` (feeding the substitutability read), `resilience-testing-pack` (placing the exit-rehearsal in the integrated test programme), and `dora-register-builder` (where DORA applies).

## Ask first

Before drafting, get plain answers to four things. Most engagements answer them quickly; if not, default and flag.

- **What tier is the arrangement and is it DORA-in-scope.** Tier is sourced from the linked `vendor-diligence` record. DORA-in-scope is the boolean that pulls the EU exit-strategy and enhanced-contractual expectations on top of the firm's baseline policy (see `references/source-anchors.md`). Plan depth scales accordingly.
- **What important business service does this arrangement support, and what is the firm's impact tolerance for it.** The tolerance is the test the realistic time-to-transition must meet. Without the tolerance the plan cannot test itself; record the IBS, get the tolerance from the firm's IBS map, and proceed.
- **Is this AI or AI-adjacent.** Treat as a boolean. AI-vendor mode is a real branch: prompt-template portability, RAG-corpus migration, model-version pin handling, guardrail and eval porting, agent-tool offboarding all sit in an AI-specific transition-engineering section that does not collapse into generic data-extraction language. An embedded AI feature that is *off* is not AI-vendor mode.
- **What is the engagement type.** Pre-onboarding, annual recertification, off-cycle trigger, post-incident re-review, concentration-driven re-review, scope-change re-review. Each carries a different decision-forum context and a different plan depth.

When `scope` is supplied, the skill consumes it (institution type, sector overlay set, cross-cutting overlay set, persona, source posture). When it is not supplied, ask the four questions and default to public posture if the practitioner declines. Note in the plan that scope was not formalised; do not silently apply a default sector overlay.

## How the plan gets built

The plan has the same spine across arrangement types. The senior reviewer fills it in roughly in the order the arrangement and the available evidence allow, not in a lockstep sequence.

The frame opens with the arrangement and criticality input. Vendor, service, business process supported, and the named important business service. Data scope at termination is named: NPI, PHI, PCI, books-and-records, model-prompts, model-outputs, training-data, derivative artifacts. Subcontractors known. Criticality, residual risk, and exit_plan_status come straight from the linked `vendor-diligence` record; the plan consumes, it does not re-set. DORA-in-scope flags whether Article 28(8) expectations apply.

Triggers come next, covering all four categories — vendor-driven, firm-driven, regulator-driven, market-driven — with realistic lead-time assumptions and the detection signal that would tell the firm a trigger has fired. A plan that covers only one category leaves the firm exposed on the day a different one fires. Distress and unexpected termination usually have shorter lead times than a planned migration; that asymmetry has to drive the substitute-readiness posture.

Transition target options are scored honestly. Substitute-vendor as primary is normal but rarely the only viable path. In-source, hybrid, retire-service, and graceful-degradation each get a viability read (`primary | viable | weak | not-viable`), a realistic time-to-transition with named assumptions, and the dependency set required to make the option real. The selected primary and a secondary target are both named; relying on a single target is a single point of failure dressed up as a plan. Time-to-transition is then tested against the impact tolerance for the supported IBS. `within | near | breach | unknown` is the readout. A `breach` is itself a finding that goes to the IBS owner and the COO, not a number to dress up.

Data return and destruction are built for every data category in `data_access`. Extraction format, schema mapping, volume, extraction window, validation against firm-of-record, vendor and firm obligations, destruction-evidence form, post-termination retention carve-outs (regulatory archive, fraud investigation, legal hold, anti-abuse retention windows for AI vendors), and the cyber choreography of key rotation and access revocation. An export API is the start of the work, not its conclusion. Derivative artifacts (caches, indexes, vector embeddings, fine-tune artifacts, log archives, BCDR replicas) are explicitly in scope; missing one of them leaks data after cutover.

Knowledge transfer is the documentation, personnel, and code-and-artifact-escrow set. For AI vendors, the firm-side prompt library, the evaluation harness, and the redaction-rule library are firm-owned regardless; vendor-side knowledge transfer is the operational integration layer.

Contract termination mechanics read the operative termination terms with a pointer to `contract-gap-review` for the clause-by-clause read. Termination-for-convenience, transition-assistance period, fees, regulator-directed-termination clause, and in-flight data lock-in. The vendor's transition-assistance commitment is a clause; the plan is the firm's playbook. Different things.

Customer-notice posture and regulator-notice posture each get a named lead time and the regulated clock that drives it. The longer of the operative consumer-protection clocks usually controls (the sector overlays carry the specific clocks: change-in-terms windows for deposit and EFT services in banking, policyholder-notice statutes in insurance, fund-board notice timing for registered funds, NACHA timing for ACH originators). Supervisory notice runs in parallel: register updates and material-vendor-change notification on the bank side, brochure and census-report updates on the adviser and fund side, ORSA and holding-company filings on the insurer side, NYDFS event reporting where applicable. Critical or important function exits warrant proactive supervisory engagement, not only paper notice. The sector overlay carries the named clocks; the source-anchors file carries the citations.

Cyber and privacy considerations follow, drawing on the cross-cutting overlays. Cyber covers secure data extraction, key rotation and credential revocation, access-revocation choreography, vendor-side destruction certification, SIEM and DLP cutover, and SEC cyber-disclosure exposure on a forced or contested termination at a publicly-listed registrant. Privacy covers GLBA Safeguards data handling, state-privacy-law deletion and return obligations, HIPAA business-associate transition, cross-border data flows, and customer-privacy-elections continuity. Both overlays default-on for AI vendors and for any vendor reaching regulated data or IBS controls.

Supervisory readiness during transition is the dual-running, evidence-collection, and examination-access-continuity posture across the cutover window. A multi-month transition runs alongside live supervisory and audit activity. Bank Service Company Act §1867(c) examination-access continuity for banks; books-and-records continuity under Rule 204-2, Rule 17a-4, and Rule 31a for advisers, BDs, and funds; MRA / MRIA exposure tracked; an examination scheduled in the cutover quarter pre-briefed.

Fourth-party dependencies pull through from the linked diligence record. The vendor's own subcontractors are often the bottleneck on transition (hyperscaler region, BIN-sponsor processor, KYC vendor, fund-accountant subcontractor, foundation-model upstream); name them and their transition impact.

The AI-specific transition section, when `ai_vendor=true`, addresses prompt-template portability (templates are usually model-specific), RAG corpus migration (vector spaces are model-specific; expect re-embedding and re-indexing), fine-tune artifact handling, model-version pin handling against the vendor's deprecation calendar, guardrail and eval porting, and agent tool offboarding for agentic vendors. None of these collapse cleanly into generic data-extraction language. The substitute model vendor's diligence pack and `llm-vendor-evidence-review` record are preconditions to cutover.

The plan closes with the cost-and-resourcing estimate, the testing plan (cadence, methods, last-test date and outcome, next-test due, with `never tested` honestly recorded and surfaced as a reviewer question), the open-dependencies-and-risks list, the reviewer questions clustered for the forum that decides, and the named owner and approver. The named approver decides; the plan stops.

## Quality bar

Holds across every plan regardless of arrangement type, audience, or render format. Every material claim cites a source from `references/source-anchors.md` (or a loaded overlay) by path. Unsupported claims are marked `[evidence needed]`. Section references that cannot be confirmed get `[verify section]` rather than fabricated. Source evidence, vendor commitment, public-source obligation, generated inference, and open legal or compliance question stay distinguishable in the plan. No named institutions in narrative unless they are public defendants in a finalised enforcement action with a published consent order. The plan stops at the recommendation. The contract clause is not the plan, anywhere. The vendor's marketing-page transition-assistance language is not the plan, anywhere.

## Adaptation

Flexes by engagement. Plan depth and length scale to criticality and DORA-in-scope status. An important-tier non-DORA arrangement collapses several sections to a paragraph; a critical or DORA-in-scope arrangement runs full depth with reviewer questions clustered for the operational-resilience committee, the AI risk committee (AI vendors), or the fund board (registered funds). The sector overlay set drives which `references/sector-overlays/<sector>.md` is loaded; a dual-registrant or BaaS arrangement may load two. Cross-cutting overlay loading follows scope plus the rule that cyber and privacy default-on for AI vendors and for any arrangement holding regulated data or IBS controls at termination. Source posture (public-only, public-plus-firm-policy, public-plus-firm-policy-plus-system-of-record-evidence, connector-aware) drives the evidence ask. The transition-engineering depth differs by vendor type (cloud IaaS, core platform, transfer agent, custodian, fund accountant, sub-adviser, claims TPA, processor, BIN sponsor, foundation-model API, AI SaaS, agentic system). Render format (Word, Excel, PowerPoint, Markdown) follows the workflow.

## Pointers

- `references/source-anchors.md` — citations and excerpts for the named anchors.
- `references/sector-overlays/banking.md`, `insurance.md`, `capital-markets.md`, `payments-fintech.md` — sector-specific transition mechanics loaded per scope. Capital-markets carries the substantive fund service-provider transition mechanics under ICA §15 and Rule 38a-1.
- `references/cross-cutting/cyber.md`, `privacy.md` — cross-cutting flavour for transition; default-on for AI vendors and for any vendor holding regulated data or IBS controls at termination.
- `references/firm-overlay.md` — firm-installed policy, taxonomy, decision forums, and IBS map pointers beyond the regulatory baseline; consumed when present.
- `templates/default-output.md` — plan template.
- `schemas/exit-plan.schema.json` — structured-output contract for downstream consumption.
- `examples/` — core-banking SaaS exit at a community bank; foundation-model API exit at an EU subsidiary (DORA-in-scope, AI vendor).
- `TROUBLESHOOTING.md` — recurring pitfalls (clause-as-plan, single-trigger-category, single-target, tolerance-test skip, derivative-artifact destruction scope, fourth-party bottleneck, AI-vendor portability assumptions, never-tested as posture).

The plugin-level shared references (`references/source-map.md`, `references/policy-control-library.md`, `references/review-gates.md`) sit at the plugin root and are consulted alongside the skill-level files.

## Output

The deliverable is the exit plan. Default to drafting against `templates/default-output.md`. Render as Word, Excel, PowerPoint, or Markdown when the audience or workflow asks for it (an operational-resilience-committee read may want a deck or memo; a transition workstream may want a workbook for the data-extraction choreography). Produce the structured record at `schemas/exit-plan.schema.json` when downstream automation or a registered consumer needs it.

Downstream consumers: `vendor-diligence` reads `exit_plan_status` and the linked record back into the diligence pack (a critical or important vendor without a current plan is itself a finding); `contract-gap-review` reads the clause-gap flags this plan surfaces; `concentration-risk-review` reads the substitutability findings; `resilience-testing-pack` reads the `testing_plan` block to place the exit-rehearsal scenario inside the integrated test programme; `dora-register-builder` reads the structured fields for ICT-third-party register entries where DORA applies.

When the structured record is produced, treat the schema as a downstream contract: additive changes only. Add fields, do not rename or repurpose them. A breaking change is a versioned migration with the downstream skills told in advance.

## Human review and AI disclosure

Open the deliverable with this line, and remove it only after the review below: `AI-assisted draft. Requires review by a qualified person before use.`

A qualified person with authority to change the output reviews it before it is delivered or relied on, and stays accountable for it. Where the output supports advice to an individual or a decision about an individual (credit, insurance underwriting, pricing or claims, employment, legal rights, or similar), that individual must be told AI was used to produce it. This skill does not make final decisions, file with a regulator, notify customers, execute transactions, or move money or other financial assets.
