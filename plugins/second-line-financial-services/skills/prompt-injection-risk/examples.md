# Examples and troubleshooting

One section per worked example, then troubleshooting. Read only what you need.

## agentic-research-assistant

### Example: prompt-injection review for an agentic research assistant in capital markets

Public-source-derived. No named institution. Pattern aligns with the use case category covered in the capital-markets sector overlay: a GenAI agent supporting equity research analysts and surveillance.

#### Input description

A US registered investment adviser is piloting an agentic research assistant for the equity research desk. The agent has tools enabled: web fetch (firm-curated allowlist), internal-document retrieval (research notes, past models), market-data API (read-only), and a draft-write tool that produces draft research notes for analyst review. Foundation model is vendor-hosted, version pinning policy is rolling-with-notice. RAG over internal research notes plus the firm-curated public web allowlist. Multi-agent orchestration: a planner agent dispatches a researcher agent, a modeller agent, and a draft-writer agent.

Engagement scope provided by `scoping`:
- Institution type: US registered investment adviser, mid-cap AUM, primary regulator SEC; FINRA for affiliated broker-dealer.
- Persona: AI Governance Lead jointly with head of model risk and the firm's CISO function.
- Sector overlay: capital markets. Cross-cutting overlays: cyber (SEC Reg S-K Item 106 for the public parent, model-supply-chain and tool-boundary focus), conduct (Marketing Rule and books-and-records reach for any AI-generated client-facing content; SR/IA fiduciary lens).
- Source posture: public-plus-firm-policy-plus-system-of-record-evidence.
- Tier: tier-2 (analyst-mediated, not auto-publication, not order-placing) with a tier-1 review trigger if scope expands to client-facing or order-placing.

Upstream artifacts: `model-card-builder` output is on file; `validation-plan` robustness block in progress; `agentic-ai-controls` review in parallel.

#### Output sketch

Sections produced (abbreviated):

- **Use case reference and architecture summary** — `equity-research-agent-v0.3`, tier-2, pre-prod pilot. Foundation model `vendor-X model-Y vN`, rolling-with-notice. RAG: internal research notes (firm-controlled), curated web allowlist (third-party-controlled at source). Tools: web fetch, document retrieval, market-data API (read-only), draft-write. Multi-agent (planner / researcher / modeller / draft-writer). Persistent-per-user memory enabled. Autonomy level: agentic-with-tool-use.

- **Threat surface** — seven carriers enumerated:
  - System prompt: trusted; firm-controlled, version-controlled, change-reviewed.
  - User input (analyst query): trusted; analyst is authenticated and licensed under the firm's compliance program.
  - Retrieved internal-document content: partially trusted; firm-controlled but historical research notes and analyst messages can carry adversarial content from past tools or pasted external material. Controls: provenance tagging, content normalisation.
  - Retrieved web content from curated allowlist: untrusted at source, partially trusted at carrier; allowlist scopes provenance but does not guarantee content integrity (the allowlisted source can be compromised, an issuer-controlled IR page can carry crafted content). Controls: source-vetting at allowlist build time, refresh integrity, output annotation showing source.
  - Tool outputs: market-data API output is trusted (vendor schema, validated fields); web-fetch output inherits the web-content trust posture above; draft-write output is the agent's own output and is treated as inference, not evidence. Controls: schema validation on market-data, tool-boundary at draft-write so it cannot publish.
  - Multi-agent message: partially trusted; an upstream agent's output is treated as carrier, not as system instruction, in the downstream agent prompt. Controls: structured-output enforcement on inter-agent messages, agent-role isolation.
  - Memory: persistent-per-user; memory writes are user-scoped and auditable. Trust posture: partially trusted because content placed in memory by past sessions can persist across foundation-model swaps; controls: memory-content sampling and expiry.

- **Tested attack classes** (with method, dataset reference, success criterion, result):
  - Direct system-prompt override via analyst query — vendor red-team set; result: pass.
  - Indirect injection via retrieved web content from allowlisted source (synthetic poisoned IR page) — firm-internal red team; success = agent invokes the draft-write tool on adversary content; result: partial (agent attempted to summarise the adversarial content as if authoritative; draft-write fired but the human-in-the-loop gate held).
  - Indirect injection via retrieved internal research note (a note containing pasted external content with embedded instructions) — firm-internal red team; result: partial (similar pattern; mitigation in draft-write gate).
  - Tool hijack: agent tricked into invoking market-data API on out-of-scope tickers (no direct harm, but signal of agent redirect) — firm-internal red team; success = unintended ticker query; result: partial.
  - Agent redirect: planner agent dispatches researcher agent on attacker-chosen topic via injected upstream-agent message — firm-internal red team; result: partial; mitigation in planner-side topic validation.
  - Exfiltration of system-prompt content — vendor red-team set plus firm-internal; result: pass.
  - Multi-agent message injection: researcher agent's output crafted to act as system instruction in downstream agent — firm-internal red team; result: partial (structured-output enforcement reduces but does not eliminate; mitigation captured).
  - Multimodal injection: not applicable in current scope (no image inputs).
  - Memory poisoning: write-and-recall test where adversarial content placed in user memory affects later sessions — firm-internal red team; result: partial; mitigation in memory-content sampling and expiry.

- **Mitigations in place** — input validation on analyst-supplied content; output filter on draft-write content for prohibited content (Marketing Rule prohibitions, fiduciary-lens flags); curated web allowlist with refresh integrity (owner: research operations); per-source provenance tagging on every retrieved item; structured-output enforcement on inter-agent messages; tool boundary on draft-write (agent cannot publish, only produce drafts; analyst publishes); tool boundary on market-data API (read-only; no write); rate limit on web-fetch; sandboxed tool runtime; logging of every tool invocation and inter-agent message; refusal behaviour for client-facing direct output (firm policy: only analyst publishes); memory-content sampling. Each mitigation entry has owner and evidence pointer.

- **Residual risk** — four concrete items:
  - Crafted adversarial content on an allowlisted IR page redirects the researcher agent to summarise misleading content; the analyst, under time pressure, publishes the draft. Likelihood: medium (allowlisted sources are not immune to compromise, and IR pages historically have been targets). Impact: high (Marketing Rule misstatement; books-and-records preservation of the misleading content; potential client-facing distribution if the analyst publishes). Owner: AI Governance Lead with head of research; quarterly review and on every allowlist change.
  - Multi-agent message injection causes the modeller agent to model an unintended ticker, producing a misleading model that lands in the draft note. Likelihood: low to medium. Impact: medium. Owner: AI Governance Lead; review on every multi-agent topology change.
  - Memory poisoning persists across analyst sessions; an analyst returning after a break encounters an agent biased by adversarial memory content. Likelihood: low (sampling in place). Impact: medium. Owner: AI Governance Lead with information security; quarterly review.
  - Foundation-model rolling update changes refusal behaviour and the draft-write gate's effective coverage shifts. Likelihood: medium (rolling-with-notice). Impact: medium. Owner: AI Governance Lead with vendor management; on every notice.

- **Monitoring and detection** — eight signals with the five required fields:
  - Refusal rate on client-facing direct-output queries; weekly; owner: AI governance team; escalation to model risk committee.
  - Tool-invocation rate and pattern (sudden expansion is an investigation trigger); continuous; owner: information security; escalation to CISO.
  - Cross-ticker tool-invocation anomaly (market-data API queries on tickers outside the analyst's coverage); continuous; owner: information security with surveillance; escalation to CISO and supervision.
  - Inter-agent message structured-output trip rate (failed structure validations); continuous; owner: AI governance team; escalation to information security if pattern.
  - Output-filter trip rate on draft-write content; continuous; owner: AI governance team; escalation to model risk committee then to compliance for Marketing Rule signal.
  - Allowlist source integrity check (last-modified, content hash drift on IR pages and other dynamic sources); daily; owner: research operations; escalation to AI Governance Lead.
  - Memory-content sampling for adversarial-content patterns; weekly; owner: information security; escalation to AI Governance Lead.
  - Foundation-model version monitoring; continuous; owner: vendor management; escalation to AI Governance Lead with re-validation per change-management table.

- **Incident response** — four named incident classes:
  - Confirmed publication of misleading agent-drafted content: compliance and supervision activate; Marketing Rule and books-and-records implications recorded; potential SR letter or examination disclosure if material. Off-switch criterion: confirmed publication takes the agent offline pending review.
  - Confirmed agent redirect via multi-agent message injection: cyber-and-AI joint runbook; supervision review on the affected analyst's coverage.
  - Suspected allowlist-source compromise (IR page change pattern, content-hash anomaly): allowlist freeze pending verification; vendor management contact if vendor-controlled source.
  - Foundation-model behaviour shift correlated with cyber signal (output anomaly, refusal anomaly, tool-invocation anomaly): cyber incident runbook; vendor consultation; potential 8-K Item 1.05 evaluation for the public parent if material.

- **Recommended owner actions** — six gaps:
  - Move to pinned foundation-model versioning for the pilot and revisit rolling-with-notice once the multi-agent prompt-injection posture is firmer. Owner: AI Governance Lead with vendor management; deadline: pre-prod gate; severity: high.
  - Tighten planner-side topic validation to reject upstream-agent messages that propose out-of-coverage tickers. Owner: agent platform owner; deadline: pre-prod gate plus 30 days; severity: high.
  - Complete firm-internal multi-agent message injection test set; vendor sets do not exercise multi-agent topologies. Owner: AI Governance Lead with information-security red team; deadline: pre-prod gate plus 45 days; severity: high.
  - Add an analyst attestation step at draft-publication (analyst confirms they read the draft and verified the cited sources), and log the attestation. Owner: head of research with compliance; deadline: pre-prod gate; severity: medium.
  - Establish memory-expiry default at 30 days for user memory; longer retention requires explicit analyst action. Owner: agent platform owner; deadline: pre-prod gate; severity: medium.
  - Drill the misleading-publication incident-response procedure with compliance, supervision, and AI governance. Owner: AI Governance Lead; deadline: within 60 days of go-live; severity: medium.

- **Source trace and confidence** — vendor red-team results at vendor-self-attestation confidence; firm-internal red-team results at high confidence for completed sets; the multi-agent and memory-poisoning sets carry `[evidence needed]` items where coverage is partial; SEC Marketing Rule and books-and-records references at high confidence with section reference in `references/source-anchors.md`; NYDFS October 2024 letter recorded as relevant for the bank-holding affiliate footprint, with sector limitation noted (NYDFS letter is supervisory expectation for NYDFS-covered entities; capital-markets-only registrants outside NYDFS scope record it as industry-practice reference).

- **Reviewer attestation** — pending; expected decision: reject-and-rework on the rolling-with-notice posture and the multi-agent test coverage; remaining items accept-with-conditions.

#### Why this scenario matters

- Agentic systems multiply the prompt-injection surface: multi-agent messages, tool boundaries, memory, and the agent-as-tool-invoker pattern each carry their own carrier and trust posture. The threat surface table fans out where a single-agent assistant compresses.
- Tool hijack and agent redirect are distinct attack classes from direct injection and indirect injection. The skill's `method` enum covers them; reviewers who do not name them miss the spine.
- The cyber overlay is sharper than in the customer-support case because tool privileges are lateral-movement opportunities. The CISO function is a co-reviewer, not a downstream consumer.
- The conduct overlay (Marketing Rule, books-and-records, fiduciary lens) bites hard on capital-markets agentic systems even when the immediate output is internal; the analyst-publication seam is where conduct lands.
- Foundation-model rolling-with-notice posture is itself a finding for an agentic system in pre-prod; pinning is the recommended action and the reviewer should expect it as a condition of acceptance.
- The skill outputs route into the cyber incident-response chain, not only into the model risk committee. The incident-response section names regulator-notification triggers explicitly.

## customer-support-genai

### Example: prompt-injection review for a vendor-hosted GenAI customer-support assistant

Public-source-derived. No named institution. Pattern aligns with the same scenario carried by `model-card-builder/examples/genai-customer-support.md`; this review consumes that card and returns a focused prompt-injection memo.

#### Input description

A regional US bank holding company is approaching the pre-prod gate for a vendor-hosted GenAI assistant inside the consumer-banking call center. The assistant summarises customer history, suggests next-best-action steps, and drafts written follow-ups for the agent to review and send. RAG over the bank's customer-history datastore and policy/procedure corpus. No tools enabled. Foundation model is vendor-hosted with version pinning and contractual change-of-version notice.

Engagement scope provided by `scoping`:
- Institution type: bank holding company, mid-cap, primary regulators FRB and CFPB; OCC for the national-bank subsidiary; NYDFS for the NY footprint.
- Persona: AI Governance Lead (second line), with CISO function as cyber co-reviewer.
- Sector overlay: banking. Cross-cutting overlays: cyber (NYDFS Part 500 in NY footprint, NYDFS October 2024 letter), privacy (regulated NPI), conduct (UDAAP exposure on customer-facing communications).
- Source posture: public-plus-firm-policy-plus-system-of-record-evidence.
- Tier: tier-2.

Upstream artifacts: `model-card-builder` output is on file; `validation-plan` robustness block is partially complete (vendor red-team results landed; firm-internal red team scheduled).

#### Output sketch

Sections produced (abbreviated):

- **Use case reference and architecture summary** — `cs-assistant-v1.0`, tier-2, pre-prod. Foundation model `vendor-X model-Y vN`, pinned, change-of-version notice required by contract. RAG: customer-history datastore (per-customer scoping), policy/procedure corpus (read-only). No tools. Single-agent. Session memory only. Autonomy level: human-in-the-loop (agent must review and send).

- **Threat surface** — six carriers enumerated:
  - System prompt: trusted; vendor-hosted, firm-controlled template with version control and change review by AI governance.
  - User input: partially trusted; the user is a licensed bank agent (authenticated), but the agent may paste customer-supplied content into the prompt without that being structurally distinguished. Controls: input filtering on pasted content, agent training to recognise injected content.
  - Retrieved content from customer-history datastore: partially trusted; data is firm-controlled but originates from customer interactions, including customer emails, chat logs, and call transcripts that can carry adversarial instructions. Controls: per-customer query scoping, content normalisation, retrieval-source audit.
  - Retrieved content from policy/procedure corpus: trusted; firm-controlled with refresh pipeline owned by Policy Management; integrity controls include change-detection and approval workflow.
  - Tool output: not applicable (no tools).
  - Memory: session only; no persistent memory across calls. Trust posture: not a sustained vector.
  - Multimodal: not applicable (text only).

- **Tested attack classes** (with method, dataset reference, success criterion, result):
  - Direct system-prompt override via agent input — vendor red-team test set (vN); success = assistant ignores out-of-scope refusal; result: pass (assistant refused).
  - Indirect injection via customer-history retrieved content — firm-internal red team scheduled, vendor-supplied indirect-injection set partially exercised; success = assistant follows injected instruction in retrieved content; result: partial (vendor set passes; firm-set residual). Recorded as `[evidence needed]` for firm-internal coverage; routed to recommended actions.
  - Exfiltration of system-prompt content — vendor red-team test set; success = assistant returns any portion of system prompt text; result: pass.
  - Cross-customer information bleed via crafted query — firm-internal test (1,000-call pilot); success = retrieval surfaces non-current-customer record; result: partial (two cases observed; mitigation in retrieval scoping).
  - Jailbreak to bypass refusal of out-of-scope queries (e.g., direct customer communication, account action) — vendor red-team set; success = assistant produces output that would, if sent unreviewed, take the out-of-scope action; result: pass under the agent-review gate; recorded with the human-in-the-loop assumption explicit.
  - Tool hijack — not applicable.
  - Multimodal injection — not applicable.

- **Mitigations in place** — input filter on pasted customer-supplied content (config link cited, exercised in vendor red-team set); output filter for policy-fact statements (regex set on file with Policy Management; exercised in citation-precision sampling); per-customer query scoping at retrieval layer (control evidence in retrieval-platform config; exercised in cross-customer test); retrieval-source audit (continuous; owner: information security); structured-output enforcement on summary format (vendor-side); refusal behaviour for out-of-scope queries (vendor-side, exercised in vendor red-team set); human-in-the-loop agent-review gate (preventive control; off-switch criterion in incident response). Each mitigation entry has owner and evidence pointer.

- **Residual risk** — three concrete items:
  - A determined adversary places crafted instructions in a customer email that lands in customer-history; on retrieval, the assistant may produce a misleading summary that the agent sends. Likelihood: low (agent-review gate is preventive). Impact: medium (customer-facing output, UDAAP and complaint-rate exposure). Owner: AI Governance Lead, accepted with quarterly review.
  - Cross-customer retrieval edge cases beyond the two observed in the pilot. Likelihood: low (mitigations in place). Impact: high (privacy event, potential GLBA notification, NYDFS Part 500 §500.17 trigger if covered entity, state breach laws). Owner: CISO function jointly with Privacy Officer; accepted only with the firm-internal red team complete.
  - Vendor foundation-model swap shifts refusal behaviour and the human-in-the-loop assumption no longer holds for the same input distribution. Likelihood: medium (vendor change-of-version cadence is approximately monthly per vendor public roadmap; firm has notice but timing is partially outside firm control). Impact: medium. Owner: AI Governance Lead with vendor management; review cadence: on every change-of-version notice.

- **Monitoring and detection** — six signals with all five fields per entry:
  - Refusal rate on out-of-scope queries; threshold: drop greater than 20% week-over-week; weekly; owner: AI governance team; escalation: model risk committee then CISO if cyber correlates.
  - Output-filter trip rate; threshold: spike greater than 3 standard deviations; continuous; owner: information security; escalation: CISO.
  - Cross-customer retrieval audit (random sampling plus rule-based detection on cross-customer ID surfaces); threshold: any confirmed event; continuous; owner: information security with privacy officer; escalation: CISO and Privacy Officer; one confirmed event triggers incident response.
  - Anomalous summary length (exfiltration leading indicator); threshold: greater than 3 standard deviations from baseline; continuous; owner: information security; escalation: CISO.
  - Foundation-model version monitoring; threshold: any change; continuous; owner: vendor management; escalation: AI Governance Lead, with re-validation per change-management table.
  - Citation-precision sampling on policy facts (50 cases per week); threshold: precision drop greater than 5 points; weekly; owner: AI governance team; escalation: model risk committee.

- **Incident response** — three named incident classes with named procedures and notification triggers:
  - Confirmed cross-customer information disclosure: firm privacy-incident runbook activates; GLBA Safeguards notification considered; NYDFS Part 500 §500.17 72-hour notice if the cyber event criteria are met; state breach-law notification per state. Off-switch criterion: any confirmed event takes the assistant offline pending remediation.
  - Confirmed system-prompt exfiltration: cyber incident runbook; NYDFS notification per Part 500; not by itself a customer-data event but treated as a cyber finding with recommended pause pending vendor consultation.
  - Suspected RAG corpus poisoning (anomaly in policy-citation precision plus retrieval-audit signal): cyber-and-AI joint runbook; vendor management notified; corpus version freeze pending investigation.

- **Recommended owner actions** — five gaps with owner role, deadline, severity:
  - Complete firm-internal red-team set on indirect injection in customer-history retrieved content. Owner: AI Governance Lead with information-security red team; deadline: pre-prod gate plus 30 days; severity: high.
  - Add per-source provenance tag to all retrieved content (basis for downstream output annotation). Owner: retrieval platform owner; deadline: pre-prod gate; severity: medium.
  - Drill the cross-customer-disclosure incident-response procedure with the privacy officer and the CISO function. Owner: AI Governance Lead with CISO; deadline: within 60 days of go-live; severity: medium.
  - Document the refusal-rate baseline before go-live so the monitoring threshold has a real reference. Owner: AI governance team; deadline: pre-prod gate; severity: medium.
  - Add `foundation_model_swap_revalidation` flag to change management with an explicit re-run of the prompt-injection review on every change-of-version notice. Owner: AI Governance Lead jointly with vendor management; deadline: pre-prod gate; severity: high.

- **Source trace and confidence** — vendor red-team results recorded at vendor-self-attestation confidence (low-to-medium); pilot evidence at high confidence; firm-internal red-team set carries `[evidence needed]` until run; NYDFS October 2024 letter alignment at high confidence with section reference in `references/source-anchors.md`.

- **Reviewer attestation** — pending; expected decision: accept-with-conditions, conditional on the firm-internal red team and the per-source provenance tagging.

#### Why this scenario matters

- The scenario is the archetype for prompt-injection review: a RAG-using GenAI assistant where the highest-likelihood vector is indirect injection in retrieved customer content, not direct injection by the user. Direct-only reviews miss the spine.
- Trust posture is the spine of the threat surface table; the scenario shows partially-trusted carriers where the trust basis is operational, not architectural.
- The mitigations list links each control to evidence and to the test that exercised it; mitigations without exercise become recommended actions, not assertions of coverage.
- Residual risk uses likelihood-and-impact framing with a one-line basis; "low" without basis is opinion, not analysis.
- The cyber overlap is explicit: cross-customer disclosure crosses NYDFS Part 500 §500.17 and state breach-law thresholds; the incident-response section names the trigger, not just the procedure.
- Recommended actions name owners as roles, not individuals, and tie deadlines to operational milestones (pre-prod gate, days post-go-live).

## troubleshooting

### Troubleshooting: prompt-injection-risk

Recurring defects from prompt-injection reviews and how to address them. Read alongside the skill spec sheet's common-pitfalls list and the cross-cutting cyber overlay's common-pitfalls section.

#### The review covers direct injection only; indirect injection is missing or compressed

Direct injection (the user typing "ignore previous instructions") is the easiest attack to test against and the least common practical vector for a deployed FS GenAI system. Indirect injection (instructions arriving through retrieved content, tool output, multi-agent message, memory, or multimodal input) is the more common practical vector and the harder one to test.

Fix: the threat-surface table requires every carrier the system has, with trust posture and trust basis on each. If a carrier's row is missing or compressed to "trusted, no controls", the table is wrong. Re-run the carrier enumeration against the architecture summary; if the system has retrieval, tool use, persistent memory, multi-agent topology, or multimodal input, the corresponding carrier rows are non-optional.

#### Mitigations are listed without evidence and without test coverage

A mitigation entry without an evidence pointer is policy, not a control. A mitigation entry with `exercised_in_test = false` is asserted coverage, not demonstrated coverage.

Fix: each `mitigations[]` entry requires an evidence pointer (config link, test report, change record, or `[evidence needed]`). Each entry needs `exercised_in_test` set explicitly. Mitigations marked `[evidence needed]` or `exercised_in_test = false` route to recommended actions, not silently into the memo body.

#### Residual risk recorded as "low" without basis

"Low" without a one-line basis is opinion. The residual-risk table requires likelihood, impact, and basis on every entry.

Fix: re-write each residual-risk entry with the basis populated. The basis names the controls that hold the likelihood down, the failure mode that drives the impact, and the assumption that fails first when the control set degrades. If the basis cannot be written, the rating is unsupported and routes to recommended actions for further analysis.

#### Monitoring signals listed without thresholds, owners, or escalation paths

A signal without a threshold sits in a dashboard nobody reads. A signal without an owner has no one to escalate to. A signal without an escalation path stops at the dashboard.

Fix: every `monitoring_detection[]` entry requires all five fields (signal, threshold, frequency, owner, escalation path). The threshold is in firm policy units (not "high" or "anomalous") with a numeric or rule-based definition. The owner is a function (named role), not an individual. The escalation path is a named committee, officer, or process.

#### No off-switch criterion on cyber-relevant incident classes

The off-switch criterion is the operational decision the runbook turns on. A confirmed exfiltration with no defined off-switch is a finding, not an acceptable position.

Fix: every `incident_response[]` entry should populate `off_switch_criterion`. For agentic systems with tool use, the off-switch is typically a combination of cutting the tool privileges and pausing the model serving endpoint. For human-in-the-loop systems, the off-switch is typically a combination of pausing the assistant and switching to the manual workflow. If there is no off-switch, that is itself a critical-severity recommended action.

#### Foundation-model swap re-validation flag missing

For any architecture depending on a third-party foundation model, the standard recommended-action item that fires is the `foundation_model_swap_revalidation` flag in change management: an explicit re-run of the prompt-injection review on every vendor change-of-version notice. A vendor model swap can shift refusal behaviour, alter the effective coverage of the firm's mitigations, and invalidate the residual-risk view.

Fix: confirm the recommended-actions section includes the foundation-model swap re-validation item. If the foundation-model versioning posture is rolling-with-notice, additionally surface a recommended action to move to pinned versioning for tier-1 and tier-2 use cases.

#### Vendor red-team results presented as firm-side coverage

Vendor adversarial-test results test the vendor's foundation-model behaviour against the vendor's test set. They do not test the firm's prompt template, retrieval corpus, tool inventory, or multi-agent topology. Treating vendor coverage as firm coverage is a recurring failure.

Fix: the `tested_attacks[]` entries record the tester explicitly (vendor red team, firm-internal red team, third-party assessor). Source-trace entries record vendor evidence at vendor-self-attestation confidence (typically low to medium). Recommended actions surface firm-internal red-team coverage gaps as `[evidence needed]` items.

#### Multi-agent and tool-use topologies under-tested

Vendor red-team sets rarely exercise multi-agent topologies and rarely exercise firm-specific tool inventories. The agent-redirect and multi-agent-message-injection attack classes are firm-side responsibilities.

Fix: for agentic systems with tool use or multi-agent orchestration, the `tested_attacks[]` table includes explicit rows for tool hijack, agent redirect, and multi-agent message injection, sourced from firm-internal red team. Coverage gaps route to recommended actions.

#### Memory poisoning ignored on persistent-memory systems

Persistent memory (per-user or shared) is a sustained attack vector. Adversarial content placed in memory by past sessions can persist across foundation-model swaps and influence later sessions.

Fix: for any system with persistent memory, the `tested_attacks[]` table includes a memory-poisoning row (write-and-recall test); the threat-surface table records memory's trust posture; the mitigations include memory-content sampling and a defined memory-expiry default; the monitoring section includes memory-content sampling as a signal.

#### Regulator-notification triggers not evaluated per incident class

The incident-response section that lists procedures without naming the regulator-notification triggers leaves the firm exposed. NYDFS §500.17(a), SEC 8-K Item 1.05, GLBA Safeguards Rule, state breach laws, sector-specific notifications, and (for bank-affiliated entities) the 36-hour banking computer-security incident notification rule may apply concurrently.

Fix: each `incident_response[]` entry populates `regulator_notification_trigger` with the named rule and the relevant condition. Where multiple notification regimes apply, list each separately. Sector overlays (banking, insurance, payments-fintech) carry the sector-specific triggers.

#### Cyber overlay loaded but used as background reading

The cyber overlay's load-bearing additions are the regulator-notification triggers, the cyber-tagged mitigations, the cyber-tagged monitoring signals, and the CISO function as co-reviewer. Treating the overlay as background reading and not surfacing these in the structured object is the failure mode.

Fix: confirm `cross_cutting_overlay_notes.cyber` is populated; confirm the cyber-tagged mitigations, monitoring entries, and incident-response triggers are present; confirm the reviewer attestation block names the CISO function as co-reviewer for cyber-flagged reviews.

#### Sector overlay loaded but the sector-specific seam not surfaced

Each sector overlay carries seams the prompt-injection review tends to miss without the overlay (banking BSA officer involvement; insurance HIPAA / NAIC AIS Program documentation; capital markets Marketing Rule reach; payments-fintech sponsor-bank co-acceptance). Loading the overlay without surfacing the seam in the review is the failure mode.

Fix: re-read the loaded sector overlay against the review and confirm each named overlay-specific consideration is reflected in the threat surface, mitigations, monitoring, incident response, or recommended actions sections.

#### Engagement scope not formalised

When the scope record is not supplied and the practitioner declines to formalise scope, the review still proceeds against a default public posture but should record the omission.

Fix: the review-metadata section notes that scope was not formalised; the recommended-actions section includes formalising scope as a low-or-medium-severity item; the source-trace confidence labels reflect the lack of formalised scope on items that would have been resolved by it.
