---
name: resilience-testing-pack
description: "Draft an operational resilience testing pack with severe-but-plausible scenarios."
argument-hint: "[subject: IBS name or arrangement (vendor + service) and criticality, plus scope or pointer]"
---

# Resilience-testing pack

A resilience-testing pack is what second-line produces so the firm's testing programme has a defensible design before the exercise runs and a defensible read-out shape before the post-mortem starts. The pack covers the subject under test, the impact tolerance the recovery posture has to meet, the severe-but-plausible scenarios chosen for this cycle, the method per scenario, the success criteria, the evidence-collection and observation plan, the communication plan, the locked read-out template, the findings-and-actions flow, and the post-test remediation set. The skill stops at the design and the read-out template; the exercise itself is run by the firm's resilience function with the second-line role limited to challenge and observation as appropriate.

This skill produces the pack as a markdown artifact (`templates/default-output.md` shape) and a structured record (`schemas/resilience-testing-pack.schema.json`) that downstream skills consume. It chains into and out of `vendor-diligence` (consuming criticality, subcontractors, data-access for arrangement-level packs), `exit-plan` (placing the exit-rehearsal inside the integrated test programme; flowing post-test findings back into the plan's testing history), `concentration-risk-review` (consuming portfolio concentrations as scenario inputs), and `dora-register-builder` (where DORA applies). Findings flow into the firm's issue-management cycle through `issue-writeup`.

## When to use

Drafts a second-line resilience-testing pack for an important business service or for a critical-or-important third-party arrangement. Captures the mapping under test, the firm's impact tolerance as the success or fail line, the severe-but-plausible scenario set, the test-design choices per scenario (tabletop, walkthrough, partial simulation, full live exercise, data-extraction rehearsal, shadow cutover), success criteria, the evidence-collection and observation plan, the locked read-out template, the lessons-learned-and-findings flow into issue management, the post-test remediation set, and the named approver. Consumes the IBS map, vendor-diligence records, and exit-plan records. Surfaces an explicit AI branch when an AI dependency sits on the chain under test, and a TLPT-scoping line where advanced testing is in scope.

Best for:
- Annual or quarterly resilience-testing cycle planning for an important business service.
- A critical or important third-party arrangement where the diligence pack flagged untested exit posture or untested BCDR claims.
- Preparation for the digital operational resilience testing programme at an in-scope firm, including TLPT scoping.
- A regulator-driven request following a sector-wide event (cloud outage, market-data disruption, payments-rails incident).
- An exit-plan rehearsal that needs to sit inside the integrated testing programme rather than run as a one-off.
- A post-incident retrospective that needs the next cycle's pack designed against the lessons.

Not the right tool when:
- The IBS or arrangement has not yet been mapped or tiered (use `criticality-assessment` first).
- The job is to write the exit plan itself (use `exit-plan` to draft, then this skill to design the test of the plan).
- The job is the test execution itself (this skill drafts the pack and the read-out template; execution is run by the firm's resilience function).
- The job is full vendor diligence on a single arrangement (use `vendor-diligence`).
- The job is portfolio-level concentration analysis (use `concentration-risk-review`; that output may then feed concentration scenarios into this pack).

## Ask first

Before drafting, get plain answers to a few things. Most engagements answer them quickly; if not, default and flag.

- **What is the subject of test, and at what level.** An IBS-level pack (the whole chain, multiple vendors, internal systems) is a different shape than an arrangement-level pack (one vendor, one service) or a portfolio cut (a hyperscaler-region exposure across many arrangements). Subject type drives mapping consumption and scenario design.
- **What is the firm's impact tolerance for the supported important business service.** Sourced from the firm's IBS map. Without the tolerance the pack cannot calibrate success criteria; if the IBS map is missing, capture what is asserted, mark the source, and surface the gap as a reviewer question. The vendor's published SLA is not a substitute.
- **Is the firm in scope for the digital operational resilience testing programme, and is the firm a candidate for advanced testing.** Both are real branches. Programme-in-scope drives the alignment to the firm's documented testing programme; TLPT scoping pulls in legal and supervisory engagement preconditions and lives as its own workstream rather than collapsing into the operational testing cycle.
- **Is an AI dependency on the chain under test.** Treat as a boolean. AI-on-the-chain surfaces AI-specific scenarios (model regression, eval drift, prompt-injection on the deployed agent, vendor model deprecation, training-data incident) and pulls the model-risk function into the room.
- **What is the engagement type.** Annual programme cycle, quarterly cycle, off-cycle trigger, post-incident rehearsal, post-onboarding validation, regulator-driven, exit-rehearsal. Each carries a different decision-forum context, a different scenario count, and a different read-out cadence.

When the scope record is supplied, the skill consumes it (institution type, sector overlay set, cross-cutting overlay set, persona, source posture). When it is not supplied, the skill asks the questions above and defaults to public posture if the practitioner declines. Note in the pack that scope was not formalised; do not silently apply a default sector overlay.

## How the pack gets built

The pack has the same spine across subject types. The senior reviewer fills it in roughly in the order the subject and the available evidence allow, not in a lockstep sequence.

The frame opens with the subject of test and the mapping summary. For an IBS-level pack, the chain is described end-to-end with the third parties and material fourth parties named (hyperscaler regions, BIN-sponsor processors, KYC vendors, foundation-model upstreams). For an arrangement-level pack, the vendor, the service, the supported business process, and the IBS the arrangement sits in are named. For a portfolio cut, the concentration under test is described and the in-scope arrangements named. Mapping is consumed from the firm's IBS map and the linked vendor-diligence records; the pack does not redo mapping.

Impact tolerance comes next, sourced from the IBS map. RTO, RPO, customer-impact threshold, regulatory-impact threshold, financial-impact threshold where applicable. The tolerance is the test the recovery posture must meet. Vendor SLAs go in the diligence record; they are not the test. Where the IBS map gives one tolerance and the vendor's contract gives a different commitment, the IBS-map tolerance controls the success criteria.

Scenario selection is the cycle's load-bearing decision. Severe-but-plausible is the supervisory frame, not a probability judgement; "low likelihood" is not a basis for exclusion. Each scenario carries a public-source plausibility anchor (a real prior event of the same shape in another firm or sector, a regulator-cited scenario, an industry tabletop pack). Scenarios stress the primary path, secondary paths, fourth-party dependencies, and any concentration points surfaced in `concentration-risk-review`. AI-on-the-chain pulls in AI-specific scenarios alongside generic-vendor-outage scenarios; the model-risk function reviews the AI scenario set. A scenario set that covers only the planned-failover path leaves the firm exposed on the day a different scenario fires.

Test design per scenario is the next decision. Method, cadence, preconditions, safety controls, exit triggers, participants, vendor participation. Methods escalate in fidelity and operational risk: tabletop, walkthrough, partial simulation, full live exercise, data-extraction rehearsal, shadow cutover. Mix the methods across the programme; tabletop everywhere is not a tested programme, full-live everywhere is reckless. Vendor participation is named explicitly: a test the vendor declines to join tests the technology, not the partnership. Partial-simulation and full-live exercises carry mandatory safety controls (kill-switch, customer-impact-threshold for early termination, comms-suppression while in-test) and named exit triggers. Where the firm is a candidate for advanced testing, TLPT scoping is its own workstream with its own approver path; the operational testing pack records the scoping line.

Success criteria are tied to the impact tolerance, with measurable thresholds and a tolerance link per criterion. A review that cannot be evidenced is not a pass. The evidence-collection plan names what is captured during the exercise (telemetry, vendor-side status feeds, customer-channel error rates, comms-bridge transcripts, observer notes per workstream), by whom, in what form, and how it is preserved (retention windows usually align to supervisory inspection cycles). The observation method states whether observation is in-room per workstream, recorded video, command-and-control bridge transcript, or after-action interviews. Independent observation is the second-line role; first-line runs the exercise.

The communication plan covers internal pre-test, in-test, and post-test, plus customer communication where the test may surface real customer impact, regulator communication where supervisory observation or notification applies, and vendor communication. Customer-comms templates are pre-positioned for any scenario that may surface real customer impact, even when the plan is to suppress comms in-test; the exit-condition path needs a comms-ready posture.

The read-out template is locked at design time. The committee's narrative shape is set on day one, not invented under time pressure on read-out day. The locked sections cover exercise summary, scenarios run and method per scenario, results against tolerance, findings, root cause, remediation owners and clocks, programme-cycle implications, and the regulator-programme implications where applicable (DORA programme cycle, Reg SCI submission, AI risk committee escalation).

The findings-and-actions framework specifies how findings flow from the exercise into the firm's issue-management cycle through `issue-writeup`. Each finding gets an owner, a due date, a verification path, and an issue ID. A finding without an owner and a clock dies in the post-exercise deck. Lessons-learned capture is wider than findings (process improvements, runbook updates, training implications, programme-design adjustments) and is filed against the IBS or arrangement so the next cycle benefits. The post-test remediation set names the actions arising and tracks them against close-out; a pack that does not produce remediation has not tested anything that mattered.

The pack closes with the programme-alignment cross-references (where the pack sits in the firm's annual programme; the digital operational resilience testing programme link where in scope; the Reg SCI programme link where applicable; the TLPT cross-reference where in scope), the cross-references to exit-plan and vendor-diligence records, the reviewer questions clustered for the forum that decides, the named owner and approver, the next-cycle trigger, and the source trace. The named approver decides; the resilience function runs the exercise.

## Quality bar

Holds across every pack regardless of subject, audience, or render format. Every material claim cites a source from `references/source-anchors.md` (or a loaded overlay) by path. Unsupported claims are marked `[evidence needed]`. Section references that cannot be confirmed get `[verify section]` rather than fabricated. Source evidence, vendor commitment, public-source obligation, generated inference, and open legal or compliance question stay distinguishable in the pack. No named institutions in narrative unless they are public defendants in a finalised enforcement action with a published consent order. The pack stops at the design and the read-out template. The firm's impact tolerance is the test, not the vendor's SLA. Partial-simulation and full-live exercises carry mandatory safety controls and named exit triggers.

## Adaptation

Flexes by engagement. Pack depth and length scale to subject criticality, programme-in-scope status, and TLPT-scoping status. An arrangement-level non-DORA pack collapses several sections to a paragraph; an IBS-level pack at a DORA-in-scope firm with TLPT scoping runs full depth with reviewer questions clustered for the operational-resilience committee, the AI risk committee (where AI in scope), the audit committee, and the supervisor. The sector overlay set drives which `references/sector-overlays.md#<sector>` is loaded; a dual-registrant or BaaS arrangement may load two. Cross-cutting overlay loading follows scope plus the rule that cyber default-on for any chain reaching firm controls and customer data, and privacy default-on for any chain reaching personal data. Source posture (public-only, public-plus-firm-policy, public-plus-firm-policy-plus-system-of-record-evidence, connector-aware) drives the evidence ask. Method mix differs by subject (an IBS-level pack mixes more methods than an arrangement-level pack, which usually pivots on one or two methods per scenario). Render format (Word, Excel, PowerPoint, Markdown) follows the workflow.

## Pointers

`references/sector-overlays.md` and `references/cross-cutting.md` hold one section per sector or topic, and `examples.md` one per example. Find the heading and read only that section.

- `references/source-anchors.md` — citations and excerpts for the named anchors.
- `references/sector-overlays.md#banking`, `insurance.md`, `capital-markets.md`, `payments-fintech.md` — sector-specific testing-programme nuance loaded per scope.
- `references/cross-cutting.md#cyber`, `privacy.md` — cross-cutting flavour for testing; cyber default-on for any chain reaching firm controls; privacy default-on for any chain reaching personal data.
- `references/firm-overlay.md` — firm-installed policy, taxonomy, decision forums, IBS map pointers, and programme-document pointers beyond the regulatory baseline; consumed when present.
- `templates/default-output.md` — pack template.
- `schemas/resilience-testing-pack.schema.json` — structured-output contract for downstream consumption.
- `examples.md` — annual resilience-testing pack for the card-payment authorisation IBS at a US bank; DORA resilience-testing pack for an EU subsidiary's customer-onboarding IBS including TLPT scoping and an AI vendor in the chain.
- `examples.md#troubleshooting` — recurring pitfalls (tolerance-vs-SLA conflation, tabletop everywhere, missing safety controls, vendor-participation skipped, read-out template not locked at design, findings as ad-hoc, programme alignment skipped, TLPT collapsed into the operational cycle, AI-scenario set treated as generic-vendor-outage).

The plugin-level shared references (`references/source-map.md`, `references/policy-control-library.md`, `references/review-gates.md`) sit at the plugin root and are consulted alongside the skill-level files.

## Output

The deliverable is the resilience-testing pack. Default to drafting against `templates/default-output.md`. Render as Word, Excel, PowerPoint, or Markdown when the audience or workflow asks for it (a programme-cycle steering read may want a deck; a scenario-by-method matrix may want a workbook; a TLPT-scoping write-up may want a memo). Produce the structured record at `schemas/resilience-testing-pack.schema.json` when downstream automation or a registered consumer needs it.

Downstream consumers: `exit-plan` reads `testing_plan` cross-references back into the plan's testing history (a never-tested critical exit plan is itself a finding); `vendor-diligence` consumes findings that affect residual risk on the linked arrangements; `concentration-risk-review` consumes portfolio-scenario findings that affect substitutability reads; `dora-register-builder` reads programme-alignment fields where DORA applies; `issue-writeup` consumes the findings-and-actions records.

When the structured record is produced, treat the schema as a downstream contract: additive changes only. Add fields, do not rename or repurpose them. A breaking change is a versioned migration with the downstream skills told in advance.

## Human review and AI disclosure

Open the deliverable with this line, and remove it only after the review below: `AI-assisted draft. Requires review by a qualified person before use.`

A qualified person with authority to change the output reviews it before it is delivered or relied on, and stays accountable for it. Where the output supports advice to an individual or a decision about an individual (credit, insurance underwriting, pricing or claims, employment, legal rights, or similar), that individual must be told AI was used to produce it. This skill does not make final decisions, file with a regulator, notify customers, execute transactions, or move money or other financial assets.
