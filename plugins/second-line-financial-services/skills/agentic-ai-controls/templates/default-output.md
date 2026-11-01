# Agentic AI controls review: [agent name and version]

Starting structure for a second-line agentic-controls review. Depth flexes with tier, lifecycle stage, audience, and loaded overlays; the section list does not. Items without evidence carry `[evidence needed]` and route to recommended actions, not silently into the artifact.

The artifact is a draft until the human reviewer attests.

---

## 1. Review metadata

- Reviewer role: [function, e.g. AI Governance Lead, MRMO, second-line cyber]
- Review stage: [pre-prod-gate / in-prod-periodic / post-incident / expansion-review / exam-readiness]
- Review date: [YYYY-MM-DD]
- Engagement-scope ID: [ID, when `scoping` was run]
- Model card ID: [ID, links to `model-card-builder`]
- Validation plan ID: [ID, links to `validation-plan`]
- Prompt-injection review ID: [ID, links to `prompt-injection-risk` where it has run]

---

## 2. Agent metadata

- Agent ID and version: [ID]
- Use case ID: [ID, links to `ai-use-case-intake`]
- Tier: [tier-1 / tier-2 / tier-3 / tier-4 / tier-unassigned, with reference to `ai-risk-tiering` output]
- Lifecycle stage: [development / pre-prod / prod / monitoring-only / retirement]
- Sponsor function: [function, never an individual]

---

## 3. Scope and authority statement

The most load-bearing section. The out-of-scope list is the firewall against scope drift.

**In-scope actions** (concrete verbs against concrete systems):

- [action 1, e.g., "place temporary card-lock on a single card on representative-initiated trigger"]
- [action 2]
- [action 3]
- ...

**Out-of-scope actions** (at least three concrete entries):

- [out-of-scope 1, e.g., "no funds movement of any kind"]
- [out-of-scope 2, e.g., "no permanent card cancellation"]
- [out-of-scope 3, e.g., "no fee adjustments or fee waivers"]
- ...

- **Geographic scope**: [in-scope jurisdictions]
- **Customer scope**: [customer segments in scope; carrier-policy or account scoping]
- **Financial impact per action**: [maximum financial-impact framing per action class]
- **Reversibility per action**: [reversible / partially reversible / irreversible per action class]

---

## 4. Architecture summary

A pointer to the model card's system description is preferable to restating; this artifact is not the place to re-derive architecture.

- Planner / executor model: [identifier]
- Foundation model: provider, name, version, pinning posture (pinned, floating, rolling-with-notice, unknown)
- RAG: corpora named with retrieval scoping rules and refresh cadence; or "not applicable"
- Multi-agent: yes / no; if yes, name the topology (planner / specialist agents / orchestrator pattern)
- Memory: none / session / persistent-per-user / persistent-shared / unknown
- Modalities: text / image / audio / video / code (or combinations)
- Autonomy level: [advisory / advisory-with-suggested-action / human-in-the-loop / human-on-the-loop / agentic-with-tool-use / fully-autonomous]

---

## 5. Tool inventory

Per tool the agent can invoke:

| Tool | System of record | Action type | Permission | Blast radius if misused | Rate limit | Owner | Evidence |
|---|---|---|---|---|---|---|---|
| [name] | [system] | [read / write / execute / communicate / compute] | [least-privilege scope] | [concrete worst-case framing in firm policy units] | [value] | [function] | [pointer or `[evidence needed]`] |

Blast-radius column is required on every entry. A tool list without blast-radius framing is not a control surface.

Tools the agent does not have are explicit "not applicable" rather than omitted.

---

## 6. Identity and authorisation

- Service account: [identifier; separate from any human identity]
- Scopes: [least-privilege scopes per tool, per customer, per case, per session]
- Secret management: [where credentials live, who can rotate them, who can read them]
- Rate limit at identity layer: [value]
- Session boundaries: [per-session, per-customer, per-case scoping rules]

For agents acting on regulated systems, NIST SP 800-53 AC-family mapping lands here when the cyber overlay is loaded.

---

## 7. Human oversight points

Per consequential decision class:

| Decision class | Oversight mode | Reviewer role | SLA | Sampling expectation | Evidence of effectiveness |
|---|---|---|---|---|---|
| [class] | [block-and-wait / notify-and-revocable / post-hoc-sample / autonomous] | [function] | [time in firm policy units] | [sampling rate and audit cadence, when applicable] | [pointer to gate-decision log, sampling audit, drift signal, or `[evidence needed]`] |

Effective-oversight evidence is what fails most reviews. The evidence pointer supports the assertion that the oversight catches what it is meant to catch. Reviewers click through; theatrical oversight is the failure mode.

EU AI Act Article 14 framings apply to in-scope deployments; the bar applies by analogy elsewhere.

---

## 8. Guardrails

| Guardrail | Type | Owner | Evidence pointer | Exercised in test? |
|---|---|---|---|---|
| [name] | [input_filter / output_filter / refusal_behavior / escalation_trigger / structured_output / content_provenance] | [function] | [pointer or `[evidence needed]`] | [yes / no] |

A guardrail without an evidence pointer is policy, not a control.

---

## 9. Threat assessment

Prompt-injection-via-tool-output and tool-misuse attack classes. If `prompt-injection-risk` has run, consume its tables and add agentic-specific classes here.

| Attack class | Carrier | Source taxonomy | Method | Dataset / red-team ref | Tester | Success criterion | Result | Date |
|---|---|---|---|---|---|---|---|---|
| [name, e.g., tool_hijack / cross_scope_tool_query / excessive_agency_chain / planner_executor_seam / multi_agent_message_injection / memory_poisoning / sandbox_escape / direct_injection / indirect_injection / jailbreak / exfiltration] | [system_prompt / user_prompt / retrieved_content / tool_output / agent_memory / multi_agent_message / multimodal_input] | [MITRE ATLAS technique ID / OWASP LLM identifier / NIST AI 600-1 subcategory] | [direct / indirect / chain / etc.] | [dataset ID, vendor set, firm-internal red-team report] | [firm internal / vendor / third-party / `[evidence needed]`] | [what counts as success against this agent] | [pass or partial / fail / not-tested] | [YYYY-MM-DD] |

The agentic-specific attack classes that are non-optional for any agent with tool use:

- Tool hijack — instructions in agent input or tool output cause invocation of a different tool than intended.
- Cross-scope tool query — agent invokes a tool with arguments outside its allowed scope.
- Excessive agency exploitation — agent chains low-stakes actions into a high-stakes outcome the per-action guardrails do not catch (OWASP LLM08).
- Planner-executor seam — planner formulates a plan the executor runs without re-checking the planner's authority.

Add memory poisoning for persistent-memory systems; multi-agent message injection for multi-agent topologies; sandbox escape for systems with code execution.

---

## 10. Sandbox and execution-environment guarantees

For systems with code execution, browser automation, or shell access:

- Process isolation: [mechanism]
- Filesystem scoping: [rules]
- Network egress controls: [outbound-call constraints]
- Secret isolation: [credentials are not in the executable context]
- Time-bounded execution: [maximum runtime per action]
- Resource quotas: [memory, CPU, file-descriptor limits]
- Snapshot-and-rollback posture: [state-reversion capability]
- Enforcement evidence: [pointer or `[evidence needed]`]

For tool-use-only systems without execution:

- Explicit boundary statement: "No code-execution surface; agent is restricted to enumerated tool calls."

Sandbox guarantees that exist as policy without enforcement evidence are routed to recommended actions, not recorded as coverage.

---

## 11. Kill switch and rollback

| Incident class | Procedure | Owner role | RTO | Last drilled | Drill cadence | Rollback path |
|---|---|---|---|---|---|---|
| [name] | [pointer to runbook] | [function with authority] | [time to offline] | [YYYY-MM-DD] | [tier-driven cadence] | [state reversion / compensating actions / resumption sign-off] |

A documented but never-drilled kill switch is theatre. The drill record is the load-bearing field. If `last_drilled` is older than the tier's required cadence, the entry flags as a gap.

---

## 12. Logging, traceability, and audit

- Log content: [what is logged on every agent invocation, tool call, plan step, oversight event, kill-switch action]
- Retention: [period in firm policy units]
- Access controls: [who can read the logs]
- Immutability posture: [append-only / hash-chained / off-system snapshot]
- Audit-trail alignment: [NYDFS Part 500 §500.6, FFIEC IT Handbook, sector-specific expectations per overlay]
- Exercised in test? [yes / no — confirmed by reading a sample log line, not asserted from policy. False routes to recommended actions.]

---

## 13. Incident response

| Incident class | Procedure | Regulator-notification trigger | Off-switch criterion |
|---|---|---|---|
| [e.g., confirmed tool-misuse outside scope] | [pointer to named runbook] | [NYDFS Part 500 §500.17(a) / SEC 8-K Item 1.05 / GLBA Safeguards / state breach laws / 12 CFR Part 53/225/304 36-hour rule / sector-specific / not applicable] | [condition that takes the agent out of service] |

The off-switch criterion is the operational decision the runbook turns on. Off-switch is non-optional on cyber-relevant and customer-impact-relevant classes.

For NY-footprint covered entities under 23 NYCRR Part 500, agentic-AI-driven cyber events that meet the §500.17 criteria are reportable. For public registrants, the 8-K Item 1.05 materiality assessment runs in parallel. For bank-affiliated entities, the 12 CFR Part 53 / Part 225 / Part 304 36-hour notification rule may apply concurrently. Sector-specific triggers (state insurance commissioner notices, HIPAA breach notification, GLBA Safeguards Rule notification under 16 CFR 314.5(d)) are loaded from the relevant overlay.

---

## 14. Escalation triggers

Production-monitoring conditions that surface to senior reviewers without waiting for the periodic review.

| Signal | Threshold | Frequency | Owner | Escalation path |
|---|---|---|---|---|
| [name] | [value, in firm policy units] | [continuous / daily / weekly / monthly] | [function] | [named committee, officer, or process] |

The standard agentic trigger set: tool-invocation-rate spike per tool; cross-scope tool query rate above zero; human-oversight rejection rate above baseline; refusal-rate drop; kill-switch activation; foundation-model version change; drift in any blast-radius-relevant metric.

All five fields required on every entry.

---

## 15. Residual risk

| Risk | Likelihood | Impact | Basis | Accepted owner role | Accepted date | Review cadence |
|---|---|---|---|---|---|---|
| [concrete description] | [low / medium / high] | [low / medium / high] | [one-line basis] | [role, never an individual] | [YYYY-MM-DD] | [quarterly / on foundation-model swap / on tool-inventory change / etc.] |

"Low" without basis is opinion. The basis column is required.

Cross-reference any partial or fail result in `threat_assessment[]` to a residual-risk row; an unaccepted partial result is itself a finding. For agents with tool use, residual risk on the planner-executor seam, on the cross-scope query class, and on the excessive-agency class is non-optional.

---

## 16. Recommended owner actions

| Gap | Owner role | Deadline | Severity | Depends on |
|---|---|---|---|---|
| [concrete gap] | [function, never an individual] | [YYYY-MM-DD] | [low / medium / high / critical] | [other action / upstream artifact / external dependency] |

Severity is the second-line judgement, not the owner's. Critical-severity items typically block pre-prod sign-off.

Standard items that fire for any agentic deployment:

- `foundation_model_swap_revalidation` flag in change management — explicit re-run on every vendor change-of-version notice.
- Kill-switch drill cadence ratification per tier.
- Per-tool blast-radius re-validation on any tool addition.
- Expansion-review trigger on any new sponsor, geography, customer segment, or tool added post-deployment.

---

## 17. Source trace and confidence

| Claim | Source | Evidence reference | Confidence |
|---|---|---|---|
| [claim] | [document, system, person, vendor evidence, or `[evidence needed]`] | [pointer] | [high / medium / low / evidence-needed] |

Vendor red-team results carry vendor-self-attestation confidence (typically low to medium). Firm-internal red-team results carry higher confidence. Drill records, gate-decision logs, and configuration evidence carry higher confidence than attestations. Do not collapse vendor and firm evidence into one line.

---

## 18. Sector and cross-cutting overlay notes (when applicable)

When the scope names a sector, the matching `references/sector-overlays.md#<sector>` adds named fields here. Examples:

- Banking: 12 CFR Part 53 / Part 225 / Part 304 36-hour notification posture; FFIEC IT Examination Handbook touchpoint; sponsor-bank shared-responsibility allocation for fintech-backed banking-as-a-service flows; BSA officer involvement on AML-touching agent flows.
- Insurance (carrying the absorbed claims-AI control bar): claims-AI carrier (NAIC #880 fair-claims-settlement coverage; state UCSPA per-state mapping; NAIC AIS Program element status; HIPAA touch where PHI flows; NAIC Model #668 §4.F where TPA runs the agent; UPL boundary on consumer-facing chatbots; ORSA materiality if enterprise-material).
- Capital markets: Rule 15c3-5 market-access controls for order-routing agents; FINRA Rule 3110 supervision; surveillance-system overlap; SEC Marketing Rule reach for adviser-side AI-generated communications; books-and-records preservation under Rule 204-2.
- Payments and fintech: BaaS bank-fintech responsibility allocation; CFPB UDAAP exposure on consumer-facing actuation; state money-transmitter licensing where applicable; sponsor-bank co-acceptance.

When the scope flags cross-cutting overlays, add the matching `references/cross-cutting.md#<topic>` fields:

- Cyber: NYDFS October 2024 industry-letter alignment; NYDFS Part 500 incident-notice posture; SEC cyber 8-K and Reg S-K Item 106 for public registrants; NIST SP 800-53 control-family tagging on threat-surface, mitigations, monitoring, incident response.
- Privacy: PII / NPI / PHI exfiltration as a privacy event class; GLBA, HIPAA, state privacy law touchpoints; consumer-recourse posture; per-customer scoping evidence.
- Conduct: customer-facing harm from agent actions or communications; CFPB UDAAP framings; complaint-rate and complaint-code drift as conduct signals; in insurance, fair-claims-settlement standards under #880 and state UCSPA; state insurance advertising rules where applicable.

If no overlay is loaded, this section is omitted.

---

## Reviewer attestation block

The artifact is reviewable when sections 2 through 17 are filled and source trace is complete. The human reviewer attests:

- **Reviewer**: [role, function]
- **Co-acceptors**: [CISO function for cyber-flagged reviews; privacy officer where PHI flows; claims operations leadership for insurance claims AI; sector co-reviewers per overlay]
- **Reviewer date**: [YYYY-MM-DD]
- **Decision**: [accept / accept-with-conditions / reject-and-rework]
- **Conditions (if any)**: [conditions, owner roles, dates]
- **Onward routing**: [AI risk committee / pre-prod gate / CISO incident-response chain / exam response file / board pack / model inventory of record]

The artifact is filed only after attestation.
