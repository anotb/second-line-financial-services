# Troubleshooting: agentic-ai-controls

Recurring defects from agentic-controls reviews and how to address them. Read alongside the skill's load-bearing list and the loaded sector and cross-cutting overlay common-pitfalls sections.

## Authority statement is descriptive prose with no enumeration of out-of-scope actions

"The agent helps representatives serve customers" tells a reviewer nothing about the boundary. The boundary becomes operational drift inside three months of deployment: the next request adds one more tool, one more customer segment, one more action, and the agent is doing things the original review did not contemplate.

Fix: the out-of-scope action list requires at least three concrete entries, each phrased as a verb against a system. Sector overlays raise the bar (insurance: no claim denial without licensed-adjuster review; banking: no funds movement; capital markets: no order routing outside firm risk thresholds). Generic out-of-scope items ("no harmful actions") are policy assertions, not control surfaces.

## Tool inventory captures tool names but not blast radius

A tool labelled "schedule callback" can spam every customer in a queue if rate-limited badly. A tool labelled "automated payment under threshold" can drain the firm's daily payment cap if the cap is not at the tool layer. A tool labelled "comm-draft" looks harmless until it is wired to a send tool no one noticed.

Fix: every entry in `tool_inventory[]` requires the `blast_radius` field populated in concrete firm policy units (count, value, customers affected, per minute / per shift / per day). The blast-radius framing surfaces the worst-case operational outcome, not the expected outcome. A tool list without blast-radius framing is a list, not a control surface.

## Human oversight is documented but not effective

Reviewers click through. Approval gates become rubber stamps. Sampling is documented but not audited. The control surface looks complete in policy and is hollow in operation.

Fix: every `human_oversight[]` entry requires `evidence_of_effectiveness` populated. The evidence pointer is a gate-decision log, a sampling audit, a drift signal, or a similar artefact that supports the assertion the oversight catches what it is meant to catch. `[evidence needed]` flags route to recommended actions. EU AI Act Article 14 framings on effective oversight apply by analogy outside in-scope deployments. For consequential actions in regulated contexts (claims denial, lending denial, customer communications), block-and-wait is the only acceptable mode; post-hoc sampling on a sent customer-impact communication is not a control.

## Kill switch is documented but never drilled

A kill switch that has not been drilled is theatre. The drill exercises both the technical kill-switch (cutting tool privileges, pausing the model serving endpoint) and the operational decision chain (who calls it, who confirms, who records, who signs off on resumption). Without the drill, the operational decision chain fails on the first real event.

Fix: every `kill_switch[]` entry carries `last_drilled` and `drill_cadence`. If `last_drilled` is older than the tier's required cadence, the entry flags as a gap and routes to recommended actions. Drill cadence: annual at minimum; quarterly for tier-1 use cases; on every tool addition or major version change. The drill record itself enters source trace at high confidence.

## Threat assessment lists generic "prompt injection" with no carrier or class

Indirect injection via retrieved customer-history content is a different control problem from direct injection in the system prompt. Tool hijack via tool output is a different attack class from cross-scope tool query. Excessive agency exploitation is OWASP LLM08 and is mostly invisible at the per-action layer.

Fix: every `threat_assessment[]` entry names attack class, carrier (system prompt, user prompt, retrieved content, tool output, agent memory, multi-agent message, multimodal input), and source taxonomy (MITRE ATLAS technique ID, OWASP LLM identifier, NIST AI 600-1 subcategory). The agentic-specific attack classes that are non-optional for any agent with tool use: tool hijack, cross-scope tool query, excessive agency exploitation, planner-executor seam. Add memory poisoning for persistent-memory systems; multi-agent message injection for multi-agent topologies; sandbox escape for systems with code execution.

## Sandbox guarantees recorded as policy without enforcement evidence

A sandbox the firm has not exercised is a sandbox that does not bind in incident response. "Process isolation: enforced via container runtime" is policy; "process isolation: enforced via container runtime, with last verified-via-test 2026-04-15, test report at <pointer>" is evidence.

Fix: `sandbox_guarantees.enforcement_evidence` must be populated. Policy without enforcement evidence routes to recommended actions, not to coverage. For tool-use-only systems without execution, the explicit boundary statement ("no code-execution surface; agent restricted to enumerated tool calls") is the correct artifact and is required.

## Logging exists but is not actually being written to

A logging entry recorded as policy and never confirmed by reading a sample log line is a frequent finding in pre-prod reviews. The log destination is misconfigured; the retention is not set; the immutability posture is not enforced; the access control list is wrong.

Fix: `logging.exercised_in_test` is set explicitly. Reading a sample log line for each event class (model invocation, tool call, plan step, oversight event, kill-switch event) before pre-prod sign-off is non-optional. False routes to recommended actions.

## Incident response lists procedures without naming the regulator-notification triggers

A procedure pointer alone leaves the firm's notification posture unspecified. NYDFS §500.17(a), 12 CFR Part 53 / Part 225 / Part 304 36-hour rule, SEC 8-K Item 1.05, GLBA Safeguards Rule, state breach laws, sector-specific notifications (state insurance commissioner under the Insurance Data Security Model Law in adopting states, HIPAA breach-notification under §§164.400-414), and producer-licensing notifications may apply concurrently.

Fix: every `incident_response[]` entry populates `regulator_notification_trigger` with the named rule and the relevant condition. Where multiple notification regimes apply, list each separately. Sector overlays carry the sector-specific triggers; load the overlay and surface the triggers in the structured object.

## Off-switch criterion missing on cyber-relevant or customer-impact-relevant incident classes

A confirmed exfiltration with no defined off-switch is a finding. A confirmed UCSPA-violating outcome with no defined off-switch is a fair-claims-settlement violation in waiting. The off-switch criterion is the operational decision the runbook turns on; without it, the runbook stops at "investigate".

Fix: every `incident_response[]` entry populates `off_switch_criterion`. For agentic systems with tool use, the off-switch is typically a combination of cutting tool privileges and pausing the model serving endpoint. For human-in-the-loop systems, the off-switch is typically pausing the agent and switching to the manual workflow. For insurance claims AI, the off-switch pauses claim actuation while leaving human-claims-handling operational. If there is no off-switch, that is itself a critical-severity recommended action.

## Foundation-model swap re-validation flag missing

For any architecture depending on a third-party foundation model, the standard recommended-action item that fires is the `foundation_model_swap_revalidation` flag in change management. A vendor model swap can shift refusal behaviour, alter the effective coverage of the firm's mitigations, change the planner-executor seam dynamics, and invalidate the residual-risk view.

Fix: confirm the `recommended_actions[]` section includes the foundation-model swap re-validation item with explicit re-run on every vendor change-of-version notice. If the foundation-model versioning posture is rolling-with-notice, additionally surface a recommended action to move to pinned versioning for tier-1 and tier-2 use cases.

## Vendor red-team results presented as firm-side coverage

Vendor adversarial-test results test the vendor's foundation-model behaviour against the vendor's test set. They do not test the firm's tool inventory, authority logic, sandbox configuration, or oversight design. Treating vendor coverage as firm coverage is a recurring failure.

Fix: `threat_assessment[]` entries record the tester explicitly (vendor red team, firm-internal red team, third-party assessor). Source-trace entries record vendor evidence at vendor-self-attestation confidence (typically low to medium). Recommended actions surface firm-internal red-team coverage gaps as `[evidence needed]` items.

## Planner-executor seam un-tested

A multi-agent topology with a planner formulating a plan and an executor running it is structurally vulnerable to the planner-executor seam: the planner's authority annotations are dropped, ignored, or downgraded by the executor under specific input distributions. Vendor red-team sets rarely exercise this surface.

Fix: for any multi-agent or planner-executor architecture, the `threat_assessment[]` table includes an explicit `planner_executor_seam` row, sourced from firm-internal red team. The success criterion is that the executor honours the planner's authority annotations in 100% of synthetic test cases. A partial result in this row is typically a critical-severity recommended action that blocks pre-prod sign-off.

## Excessive-agency exploitation under-framed

A series of low-stakes actions chained together into a high-stakes outcome is the canonical agentic failure mode (OWASP LLM08). The per-action guardrails do not catch the chained outcome; the per-day or per-shift caps do.

Fix: for any agent with multiple tools or with iterative tool use within a session, the `threat_assessment[]` table includes an `excessive_agency_chain` row testing chained-action sequences. Daily-aggregate caps and per-shift caps at the identity layer or the tool layer are the load-bearing controls; cap-trip rates are escalation signals. The residual-risk view records the chain-aggregation risk explicitly.

## Reviewer attestation lists named individuals

Reviewer roles are functions, never named individuals. Individuals leave; functions persist. A reviewer-attestation block listing "Jane Doe, AI Governance Lead" creates a fragile artifact.

Fix: replace any named individuals with the function (AI Governance Lead, MRMO, CISO function, Privacy Officer, Claims Operations leadership). Where the firm tracks which individual signed, the firm's gate-decision log records the individual; the controls review references the function.

## Sector overlay loaded but the sector-specific seam not surfaced

Each sector overlay carries seams the controls review tends to miss without the overlay (banking: BSA officer involvement on AML-touching agent flows, 12 CFR Part 53 36-hour rule; insurance: NAIC #880 fair-claims-settlement, NAIC AIS Program element status, NAIC Model #668 §4.F where TPA runs the agent, UPL boundary on consumer-facing chatbots, ORSA materiality; capital markets: Rule 15c3-5 market-access for order-routing agents, FINRA Rule 3110 supervision; payments-fintech: BaaS shared-responsibility allocation, state money-transmitter licensing footprint). Loading the overlay without surfacing the seam is the failure mode.

Fix: re-read the loaded sector overlay against the review and confirm each named overlay-specific consideration is reflected in the authority statement, tool inventory, oversight points, threat assessment, monitoring, incident response, or recommended actions sections. The structured object's `sector_overlay_notes.<sector>` field carries the surfaced seams.

## Cyber overlay loaded but used as background reading

The cyber overlay's load-bearing additions are the regulator-notification triggers, the cyber-tagged mitigations, the cyber-tagged monitoring signals, the sandbox guarantees enforcement evidence, the kill-switch drill records, and the CISO function as co-reviewer. Treating the overlay as background reading and not surfacing these in the structured object is the failure mode.

Fix: confirm `cross_cutting_overlay_notes.cyber` is populated; confirm the cyber-tagged tool-inventory entries, monitoring entries, and incident-response triggers are present; confirm the sandbox guarantees carry enforcement evidence; confirm the kill-switch entries carry drill records; confirm the reviewer attestation block names the CISO function as co-reviewer for cyber-flagged reviews.

## Insurance overlay: relying on a fairness-only test where a fair-claims-settlement test is required

A claims-AI agent that passes a generic fairness eval and fails state UCSPA timing or reasoned-denial requirements is operationally non-compliant. Fair-claims-settlement is governed by NAIC #880 and state UCSPAs; fairness is a different test under a different statutory frame.

Fix: for any insurance claims-AI agent, the controls review records the agent's actuation timing against the most-prescriptive state's UCSPA timing requirement, the reasoned-denial drafting against the named UCSPA reasoning elements, and the human-oversight design against the licensed-adjuster review requirement. Generic fairness testing is recorded separately and does not substitute.

## Insurance overlay: missing the UPL question on consumer-facing chatbots

Where the bot crosses into legal advice or coverage opinions, the carrier risks UPL exposure on top of unfair-trade-practices exposure. The boundary is at the guardrail layer.

Fix: for any consumer-facing claims-AI or insurance chatbot, the guardrails section records UPL-boundary refusal behaviour with an evidence pointer, exercised in firm-internal test. The recommended actions surface the UPL boundary as a recurring monitoring expectation.

## Insurance overlay: TPA-run agents with §4.F evidence not collected

Where a TPA, claims administrator, or other vendor runs the agent on the carrier's policies, NAIC Insurance Data Security Model Law (Model #668) §4.F obligations attach; the carrier remains accountable. Reviewing the carrier's tools without the TPA's tools is half a review.

Fix: for any TPA-run agent, the controls review requests the TPA's §4.F evidence pack (security program, third-party-service-provider obligations, monitoring, incident-response cooperation, breach-notification chain). Gaps carry `[evidence needed]` with the TPA as owner; the carrier's residual-risk acceptance is conditional on the evidence pack.

## Engagement scope not formalised

When the engagement-scope record is not supplied and the practitioner declines to formalise scope, the review still proceeds against a default public posture but should record the omission.

Fix: the review-metadata section notes that engagement scope was not formalised; the recommended-actions section includes formalising engagement scope as a low-or-medium-severity item; the source-trace confidence labels reflect the lack of formalised scope on items that would have been resolved by it.
