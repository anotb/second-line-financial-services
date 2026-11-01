# Prompt-injection review: [use case name and version]

Starting structure for a second-line prompt-injection review memo. Depth flexes with tier, lifecycle stage, and audience; the section list does not. A pre-prod gate review compresses production-monitoring evidence; an in-prod review expands it. Items without evidence carry `[evidence needed]` and route to recommended actions, not silently into the memo.

The memo is a draft until the human reviewer attests.

---

## 1. Review metadata

- Reviewer role: [function, e.g. AI Governance Lead, MRMO, second-line cyber]
- Review stage: [pre-prod-gate / in-prod-periodic / post-incident / exam-readiness]
- Review date: [YYYY-MM-DD]
- Engagement-scope ID (if `scoping` was run): [ID]
- Model card ID (links to `model-card-builder`): [ID]
- Validation plan ID (links to `validation-plan`): [ID]

---

## 2. Use case reference and architecture summary

- Use case ID (links to `ai-use-case-intake`): [ID]
- Tier: [tier-1 / tier-2 / tier-3 / tier-4 / tier-unassigned, with reference to `ai-risk-tiering` output]
- Lifecycle stage: [development / pre-prod / prod / monitoring-only / retirement]
- Foundation model: provider, name, version, version pinning posture (pinned, floating, rolling-with-notice, unknown)
- RAG: corpora named, retrieval scoping rules, refresh cadence; or "not applicable"
- Tools: tool inventory, tool-boundary controls; or "not applicable"
- Multi-agent: yes / no; if yes, name the topology (planner / specialist agents / orchestrator pattern)
- Memory: none / session / persistent-per-user / persistent-shared / unknown
- Autonomy level: [advisory / advisory-with-suggested-action / human-in-the-loop / human-on-the-loop / agentic-with-tool-use / fully-autonomous]

A short architecture diagram or pointer to the model card's system description is preferable to re-restating the system here.

---

## 3. Threat surface

For each carrier the system presents, name the trust posture and the controls that sit at the carrier:

| Carrier | Trust posture | Trust basis | Controls at carrier | Notes |
|---|---|---|---|---|
| System prompt | trusted / partially-trusted / untrusted / unknown | [why] | [controls] | [notes] |
| User input | | | | |
| Retrieved content (per RAG corpus) | | | | |
| Tool output (per tool) | | | | |
| Memory | | | | |
| Multi-agent message | | | | |
| Multimodal input (per modality) | | | | |

Every carrier the system actually has appears as a row, even if the trust posture is "trusted". Carriers not in the system are marked "not applicable" rather than omitted; the omission would otherwise read as oversight.

The trust basis column is the load-bearing one. "Trusted because it is firm-controlled" is different from "trusted because it is authenticated" is different from "trusted because the schema is validated upstream"; the basis is what fails first when the assumption changes.

---

## 4. Tested attack classes

For each attack class tested:

| Attack class | Method | Dataset / red-team ref | Tester | Success criterion | Result | Date |
|---|---|---|---|---|---|---|
| [name] | [direct / indirect / jailbreak / exfiltration / tool_hijack / agent_redirect / multimodal / data_poisoning] | [dataset ID, vendor set, firm-internal red-team report] | [firm internal / vendor / third-party / `[evidence needed]`] | [what counts as success against this system] | [success or partial / fail / not-tested] | [YYYY-MM-DD] |

Empty rows for attack classes that are not applicable to this architecture (e.g., `tool_hijack` on a system with no tools) are explicit "not applicable", not omitted.

The baseline attack-class set for a typical text-only RAG-using GenAI system is: direct system-prompt override, indirect injection in retrieved content, exfiltration of system-prompt content, jailbreak. For tool-using or agentic systems add tool hijack, agent redirect, multi-agent message injection. For multimodal systems add multimodal injection per modality. For systems with persistent memory add memory poisoning.

---

## 5. Mitigations in place

For each mitigation:

| Mitigation | Type | Owner | Evidence pointer | Exercised in test? |
|---|---|---|---|---|
| [name] | [input_filter / output_filter / source_vetting / tool_boundary / structured_output / refusal_behavior / content_provenance / sandboxing / human_in_the_loop_gate / rate_limit / logging_and_monitoring / model_supply_chain] | [function] | [config link, test report, change record, or `[evidence needed]`] | [yes / no] |

A mitigation without an evidence pointer is policy, not a control. A mitigation listed but not exercised in any tested attack is recorded with `exercised_in_test = no` and routed to recommended actions; do not treat it as coverage.

---

## 6. Residual risk

For each named residual risk:

| Risk | Likelihood | Impact | Basis | Accepted owner role | Accepted date | Review cadence |
|---|---|---|---|---|---|---|
| [concrete description] | [low / medium / high] | [low / medium / high] | [one-line basis] | [role, never an individual] | [YYYY-MM-DD] | [quarterly / on foundation-model swap / on RAG corpus change / etc.] |

"Low" without a basis is opinion. The basis column is required.

Cross-reference any partial or fail result in `tested_attacks[]` to a residual risk row; an unaccepted partial result is itself a finding.

---

## 7. Monitoring and detection

For each signal:

| Signal | Threshold | Frequency | Owner | Escalation path |
|---|---|---|---|---|
| [name] | [value, in firm policy units] | [continuous / daily / weekly / monthly] | [function] | [named committee, officer, or process; CISO function for cyber-tagged signals] |

All five columns required on every entry. A signal without a threshold sits in a dashboard nobody reads; a signal without an owner has no one to escalate to.

The baseline signal set for a typical GenAI system is: refusal rate, output-filter trip rate, anomalous output length (exfiltration leading indicator), foundation-model version monitoring. For RAG-using systems add retrieval-source audit and citation-precision sampling. For tool-using or agentic systems add tool-invocation rate and pattern, inter-agent message structured-output trip rate, cross-scope tool query anomaly. For systems with persistent memory add memory-content sampling.

---

## 8. Incident response

For each incident class:

| Incident class | Procedure | Regulator-notification trigger | Off-switch criterion |
|---|---|---|---|
| [e.g., confirmed system-prompt exfiltration] | [pointer to named runbook] | [NYDFS Part 500 §500.17 / SEC 8-K Item 1.05 / GLBA Safeguards / state breach laws / not applicable] | [condition that takes the system out of service] |

The off-switch criterion is the operational decision the runbook turns on. If there is no off-switch, that is itself a recommended action.

For NY-footprint covered entities under 23 NYCRR Part 500, prompt-injection-driven cyber events that meet the 72-hour notice criteria are reportable; cite §500.17(a). For public registrants, the 8-K Item 1.05 materiality assessment runs in parallel for material cybersecurity incidents. Sector-specific notification triggers (state insurance commissioner, state breach laws, GLBA Safeguards Rule notification under 16 CFR 314.5(d)) are loaded from the relevant overlay.

---

## 9. Recommended owner actions

For each gap:

| Gap | Owner role | Deadline | Severity | Depends on |
|---|---|---|---|---|
| [concrete gap] | [function, never an individual] | [YYYY-MM-DD] | [low / medium / high / critical] | [other action / upstream artifact / external dependency] |

Severity is the second-line judgement, not the owner's. Critical-severity items typically block pre-prod sign-off.

The standard recommended-actions item that fires for any architecture depending on a third-party foundation model is the `foundation_model_swap_revalidation` flag in change management: an explicit re-run of the prompt-injection review on every vendor change-of-version notice. Missing this flag on a foundation-model-dependent system is itself a finding.

---

## 10. Source trace and confidence

For every material claim in the memo:

| Claim | Source | Evidence reference | Confidence |
|---|---|---|---|
| [claim] | [document, system, person, vendor evidence, or `[evidence needed]`] | [pointer] | [high / medium / low / evidence-needed] |

Vendor red-team results carry vendor-self-attestation confidence (typically low to medium). Firm-internal red-team results carry higher confidence. Do not collapse vendor and firm evidence into one line. `[evidence needed]` flags route to recommended actions.

---

## 11. Sector and cross-cutting overlay notes (when applicable)

When the scope names a sector, the matching `references/sector-overlays.md#<sector>` adds named fields here. Examples:

- Banking: sponsor-bank GenAI shared-responsibility allocation; FFIEC IT Examination Handbook touchpoint; NYDFS Part 500 covered-entity status.
- Insurance: claims-AI carrier (NAIC Bulletin AIS Program element status); ECDIS-driven underwriting injection surface; HIPAA touch on PHI carriers.
- Capital markets: Marketing Rule and books-and-records reach for AI-generated client-facing content; surveillance-system injection surface; SR/IA fiduciary-lens framing.
- Payments and fintech: BaaS GenAI bank-fintech responsibility allocation; account-takeover fraud-model adjacency; transaction-monitoring injection surface.

When the scope flags cross-cutting overlays, add the matching `references/cross-cutting.md#<topic>` fields:

- Cyber: NYDFS October 2024 industry-letter alignment; NYDFS Part 500 incident-notice posture; SEC cyber 8-K and Reg S-K Item 106 for public registrants; tool-boundary and model-supply-chain framing.
- Privacy: PII / NPI / PHI exfiltration as a privacy event class; GLBA, HIPAA, state privacy law touchpoints; consumer-recourse posture.
- Conduct: customer-facing harm from injection-driven offensive output, false promises, off-label financial advice; complaint-rate and complaint-code drift as conduct signals.

If no overlay is loaded, this section is omitted.

---

## Reviewer attestation block

The memo is reviewable when sections 2 through 10 are filled and source trace is complete. The human reviewer attests:

- **Reviewer**: [role, function]
- **Reviewer date**: [YYYY-MM-DD]
- **Decision**: [accept / accept-with-conditions / reject-and-rework]
- **Conditions (if any)**: [conditions, owner roles, dates]
- **Onward routing**: [AI risk committee / pre-prod gate / CISO incident-response chain / exam response file / board pack]

The memo is filed only after attestation.
