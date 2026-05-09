# Troubleshooting: prompt-injection-risk

Recurring defects from prompt-injection reviews and how to address them. Read alongside the skill spec sheet's common-pitfalls list and the cross-cutting cyber overlay's common-pitfalls section.

## The review covers direct injection only; indirect injection is missing or compressed

Direct injection (the user typing "ignore previous instructions") is the easiest attack to test against and the least common practical vector for a deployed FS GenAI system. Indirect injection (instructions arriving through retrieved content, tool output, multi-agent message, memory, or multimodal input) is the more common practical vector and the harder one to test.

Fix: the threat-surface table requires every carrier the system has, with trust posture and trust basis on each. If a carrier's row is missing or compressed to "trusted, no controls", the table is wrong. Re-run the carrier enumeration against the architecture summary; if the system has retrieval, tool use, persistent memory, multi-agent topology, or multimodal input, the corresponding carrier rows are non-optional.

## Mitigations are listed without evidence and without test coverage

A mitigation entry without an evidence pointer is policy, not a control. A mitigation entry with `exercised_in_test = false` is asserted coverage, not demonstrated coverage.

Fix: each `mitigations[]` entry requires an evidence pointer (config link, test report, change record, or `[evidence needed]`). Each entry needs `exercised_in_test` set explicitly. Mitigations marked `[evidence needed]` or `exercised_in_test = false` route to recommended actions, not silently into the memo body.

## Residual risk recorded as "low" without basis

"Low" without a one-line basis is opinion. The residual-risk table requires likelihood, impact, and basis on every entry.

Fix: re-write each residual-risk entry with the basis populated. The basis names the controls that hold the likelihood down, the failure mode that drives the impact, and the assumption that fails first when the control set degrades. If the basis cannot be written, the rating is unsupported and routes to recommended actions for further analysis.

## Monitoring signals listed without thresholds, owners, or escalation paths

A signal without a threshold sits in a dashboard nobody reads. A signal without an owner has no one to escalate to. A signal without an escalation path stops at the dashboard.

Fix: every `monitoring_detection[]` entry requires all five fields (signal, threshold, frequency, owner, escalation path). The threshold is in firm policy units (not "high" or "anomalous") with a numeric or rule-based definition. The owner is a function (named role), not an individual. The escalation path is a named committee, officer, or process.

## No off-switch criterion on cyber-relevant incident classes

The off-switch criterion is the operational decision the runbook turns on. A confirmed exfiltration with no defined off-switch is a finding, not an acceptable position.

Fix: every `incident_response[]` entry should populate `off_switch_criterion`. For agentic systems with tool use, the off-switch is typically a combination of cutting the tool privileges and pausing the model serving endpoint. For human-in-the-loop systems, the off-switch is typically a combination of pausing the assistant and switching to the manual workflow. If there is no off-switch, that is itself a critical-severity recommended action.

## Foundation-model swap re-validation flag missing

For any architecture depending on a third-party foundation model, the standard recommended-action item that fires is the `foundation_model_swap_revalidation` flag in change management: an explicit re-run of the prompt-injection review on every vendor change-of-version notice. A vendor model swap can shift refusal behaviour, alter the effective coverage of the firm's mitigations, and invalidate the residual-risk view.

Fix: confirm the recommended-actions section includes the foundation-model swap re-validation item. If the foundation-model versioning posture is rolling-with-notice, additionally surface a recommended action to move to pinned versioning for tier-1 and tier-2 use cases.

## Vendor red-team results presented as firm-side coverage

Vendor adversarial-test results test the vendor's foundation-model behaviour against the vendor's test set. They do not test the firm's prompt template, retrieval corpus, tool inventory, or multi-agent topology. Treating vendor coverage as firm coverage is a recurring failure.

Fix: the `tested_attacks[]` entries record the tester explicitly (vendor red team, firm-internal red team, third-party assessor). Source-trace entries record vendor evidence at vendor-self-attestation confidence (typically low to medium). Recommended actions surface firm-internal red-team coverage gaps as `[evidence needed]` items.

## Multi-agent and tool-use topologies under-tested

Vendor red-team sets rarely exercise multi-agent topologies and rarely exercise firm-specific tool inventories. The agent-redirect and multi-agent-message-injection attack classes are firm-side responsibilities.

Fix: for agentic systems with tool use or multi-agent orchestration, the `tested_attacks[]` table includes explicit rows for tool hijack, agent redirect, and multi-agent message injection, sourced from firm-internal red team. Coverage gaps route to recommended actions.

## Memory poisoning ignored on persistent-memory systems

Persistent memory (per-user or shared) is a sustained attack vector. Adversarial content placed in memory by past sessions can persist across foundation-model swaps and influence later sessions.

Fix: for any system with persistent memory, the `tested_attacks[]` table includes a memory-poisoning row (write-and-recall test); the threat-surface table records memory's trust posture; the mitigations include memory-content sampling and a defined memory-expiry default; the monitoring section includes memory-content sampling as a signal.

## Regulator-notification triggers not evaluated per incident class

The incident-response section that lists procedures without naming the regulator-notification triggers leaves the firm exposed. NYDFS §500.17(a), SEC 8-K Item 1.05, GLBA Safeguards Rule, state breach laws, sector-specific notifications, and (for bank-affiliated entities) the 36-hour banking computer-security incident notification rule may apply concurrently.

Fix: each `incident_response[]` entry populates `regulator_notification_trigger` with the named rule and the relevant condition. Where multiple notification regimes apply, list each separately. Sector overlays (banking, insurance, payments-fintech) carry the sector-specific triggers.

## Cyber overlay loaded but used as background reading

The cyber overlay's load-bearing additions are the regulator-notification triggers, the cyber-tagged mitigations, the cyber-tagged monitoring signals, and the CISO function as co-reviewer. Treating the overlay as background reading and not surfacing these in the structured object is the failure mode.

Fix: confirm `cross_cutting_overlay_notes.cyber` is populated; confirm the cyber-tagged mitigations, monitoring entries, and incident-response triggers are present; confirm the reviewer attestation block names the CISO function as co-reviewer for cyber-flagged reviews.

## Sector overlay loaded but the sector-specific seam not surfaced

Each sector overlay carries seams the prompt-injection review tends to miss without the overlay (banking BSA officer involvement; insurance HIPAA / NAIC AIS Program documentation; capital markets Marketing Rule reach; payments-fintech sponsor-bank co-acceptance). Loading the overlay without surfacing the seam in the review is the failure mode.

Fix: re-read the loaded sector overlay against the review and confirm each named overlay-specific consideration is reflected in the threat surface, mitigations, monitoring, incident response, or recommended actions sections.

## Engagement scope not formalised

When the scope record is not supplied and the practitioner declines to formalise scope, the review still proceeds against a default public posture but should record the omission.

Fix: the review-metadata section notes that scope was not formalised; the recommended-actions section includes formalising scope as a low-or-medium-severity item; the source-trace confidence labels reflect the lack of formalised scope on items that would have been resolved by it.
