# Example: agentic-controls review for a CSR co-pilot at a regional US bank

Public-source-derived. No named institution. The scenario is the v1 archetype for agentic controls in retail banking: a vendor-hosted GenAI assistant inside the consumer-banking call center that summarises customer state, suggests next-best actions, drafts written follow-ups, and is wired to a small inventory of tools (account-read, card-lock-temp, callback-schedule, comm-draft).

## Input description

A regional US bank holding company is approaching the pre-prod gate for a CSR co-pilot in the consumer-banking call center. RAG over the bank's customer-history datastore and policy/procedure corpus. Foundation model is vendor-hosted with version pinning and contractual change-of-version notice. The agent has four tools enabled.

Engagement scope provided by `engagement-scoping`:

- Institution type: bank holding company, mid-cap, primary regulators FRB and CFPB; OCC for the national-bank subsidiary; NYDFS for the NY footprint.
- Persona: AI Governance Lead (second line); CISO function as cyber co-reviewer; BSA officer not required (no AML-touching flow); privacy officer is a co-reviewer because the agent reads NPI; conduct-team co-reviewer for consumer-facing communication.
- Sector overlay: banking. Cross-cutting overlays: cyber (NYDFS Part 500 in NY, NYDFS October 2024 letter, 12 CFR Part 53 for the national-bank subsidiary), privacy (regulated NPI), conduct (UDAAP exposure on customer-facing communications).
- Source posture: public-plus-firm-policy-plus-system-of-record-evidence.
- Tier: tier-2.

Upstream artifacts: `model-card-builder` output is on file; `validation-plan` robustness block is partially complete (vendor red-team results landed; firm-internal red team scheduled); `prompt-injection-risk` has run and produced its memo.

## Output sketch

Sections produced (abbreviated):

- **Agent metadata** — `csr-copilot-v1.0`, tier-2, pre-prod, sponsor function: Consumer Banking Call Center Operations.

- **Scope and authority statement**:
  - In-scope actions: summarise customer state for the CSR; suggest next-best-action steps; draft a written follow-up communication for CSR review; place a temporary card-lock on a single card on CSR-initiated trigger; schedule a callback for the customer.
  - Out-of-scope actions (concrete entries): no funds movement of any kind; no permanent card cancellation; no fee imposition or fee waiver; no rate or term modification; no account closure or opening; no sending of customer communications without CSR review; no cross-customer access.
  - Geographic scope: US footprint. Customer scope: consumer-banking customers only; commercial and wealth customers explicitly out of scope.
  - Financial impact per action: card-lock-temp action is reversible and zero-financial-impact in itself; comm-draft is text-only with no actuation. No high-financial-impact action surface.
  - Reversibility: all in-scope actions are reversible.

- **Architecture summary** — pointer to model card. Foundation model `vendor-X model-Y vN`, pinned, change-of-version notice required by contract. RAG: customer-history datastore (per-customer scoping), policy/procedure corpus (read-only, refreshed weekly). Single-agent. Session memory only; no persistent memory. Modalities: text. Autonomy level: human-in-the-loop (CSR must initiate every action and review every comm-draft).

- **Tool inventory**:
  - account-read: customer account database, read, scoped to CSR's authorised customer-set per session, blast radius "could surface up to N customer records per session if scoping fails"; rate limit 30 reads/min; owner Consumer Banking Operations; evidence link to retrieval-platform config.
  - card-lock-temp: card-management platform, write, scoped to single card per call, blast radius "could lock up to 60 cards per CSR shift if abused", rate limit 1/minute; owner Card Operations; evidence link to card-platform config.
  - callback-schedule: callback system, write, scoped to customer-of-record per call, blast radius "could schedule up to 60 callbacks per shift if abused", rate limit 1/minute; owner Operations; evidence link to callback-platform config.
  - comm-draft: text generation only, no actuation, blast radius "draft text only — no send", rate limit not applicable; owner AI Governance; evidence: model output is text, with explicit no-send wiring at the platform layer.
  - All other tools: not applicable.

- **Identity and authorisation** — agent service account `csr-copilot-svc-prod` separate from any human identity; scopes scoped to CSR's authorised customer-set per session, with per-session expiry; secrets in firm secrets manager, rotation cadence 90 days, identity-team-owned; identity-layer rate limits aligned to per-shift CSR norms; session boundaries enforced at platform layer with per-session expiry on customer-set.

- **Human oversight points**:
  - account-read summarisation output: post-hoc-sample mode, sample 5%, audit cadence weekly; reviewer role CSR supervisor; SLA n/a (post-hoc); evidence pointer to weekly-sample audit log.
  - next-best-action suggestion: notify-and-revocable; CSR may accept or override; reviewer role CSR; SLA real-time; evidence pointer to action-decision log.
  - card-lock-temp action: block-and-wait CSR confirmation; reviewer role CSR; SLA real-time; evidence pointer to gate-decision log.
  - callback-schedule: block-and-wait CSR confirmation; reviewer role CSR; SLA real-time.
  - comm-draft: block-and-wait CSR review-and-send; reviewer role CSR; SLA real-time; evidence pointer to send-event log showing CSR review timing.
  - Post-hoc supervisor sampling 1% on all comm-drafts sent; reviewer role CSR supervisor; cadence weekly.

- **Guardrails** — input filter on pasted customer-supplied content (config link, exercised in vendor red-team); output filter for prohibited language and policy-fact accuracy (regex set on file with Consumer Banking Compliance, exercised in citation-precision sampling); refusal behaviour on out-of-scope queries (vendor-side, exercised in vendor red-team set); structured-output enforcement on summary format (vendor-side); content provenance tag on retrieved customer-history content.

- **Threat assessment**:
  - direct prompt injection in CSR input — vendor red-team set; tester vendor; result pass.
  - indirect injection in customer-history retrieved content — firm-internal red team scheduled; partial coverage from vendor set; result partial; routed to recommended actions.
  - tool hijack (instruction in customer history causes card-lock-temp invocation outside CSR intent) — firm-internal test (50-call pilot); result pass under block-and-wait CSR confirmation; recorded with the human-in-the-loop assumption explicit.
  - cross-scope tool query (account-read on customer outside CSR's authorised set) — firm-internal test (1,000-call pilot); result partial (two cases observed; mitigation in retrieval scoping config; routed to recommended actions and to residual risk).
  - excessive-agency exploitation (chained tool calls aggregating customer data) — firm-internal test; result pass under per-session scoping.
  - planner-executor seam — not applicable, single-agent architecture.
  - exfiltration of system-prompt content — vendor red-team; result pass.
  - jailbreak to bypass refusal — vendor red-team; result pass.
  - multi-agent message injection — not applicable.
  - memory poisoning — not applicable, session memory only.
  - sandbox escape — not applicable, no code-execution surface.

- **Sandbox and execution-environment guarantees** — `has_code_execution: false`. Explicit boundary statement: "No code-execution surface; agent restricted to enumerated tool calls."

- **Kill switch and rollback**:
  - confirmed tool-misuse outside scope: procedure pointer to firm AI-misuse runbook; owner role AI Governance Lead with platform on-call; RTO under 5 minutes; last drilled 2026-04-15; drill cadence quarterly per tier-2; rollback path (any actuation in suspect window queued for CSR re-review; communications drafted but not sent are flagged; communications sent in suspect window reviewed for retraction).
  - confirmed cross-customer access: same procedure; off-switch fires immediately on first confirmed event.
  - foundation-model behaviour shift suggesting upstream issue: procedure pointer to AI-vendor incident runbook; owner role AI Governance Lead with vendor management; RTO under 30 minutes; rollback path (revert to prior pinned version).

- **Logging, traceability, and audit** — log content covers every agent invocation, every tool call, every plan step, every CSR oversight action, every comm-draft (whether sent or discarded), every kill-switch event; retention 7 years per firm record-retention policy; access controls limited to AI Governance, CISO function, BSA officer (read-only), Consumer Banking audit; immutability append-only with daily off-system snapshot; audit-trail aligned to NYDFS Part 500 §500.6; exercised-in-test confirmed by reading sample log lines.

- **Incident response**:
  - confirmed tool-misuse outside scope: procedure pointer to firm AI-misuse runbook; regulator-notification trigger NYDFS Part 500 §500.17(a) for NY footprint, 12 CFR Part 53 36-hour rule for the national-bank subsidiary, SEC 8-K Item 1.05 materiality assessment for the holding company; off-switch criterion: any confirmed event takes the agent offline pending remediation.
  - confirmed cross-customer information disclosure: privacy-incident runbook; GLBA Safeguards notification considered; NYDFS §500.17(a) 72-hour notice if cyber-event criteria met; state breach-law notification per state; off-switch criterion: any confirmed event.
  - foundation-model behaviour shift: AI-vendor incident runbook; cyber-side cooperation with vendor; off-switch criterion: confirmed deviation from baseline behaviour profile.
  - sandbox-escape attempt: not applicable.

- **Escalation triggers**:
  - tool-invocation rate spike per tool: threshold +3 std-dev week-over-week; continuous; owner AI Governance; escalation AI risk committee.
  - cross-scope tool query rate: threshold any non-zero; continuous; owner CISO function; escalation CISO and Privacy Officer.
  - human-oversight rejection rate: threshold +2 std-dev week-over-week (CSR overriding the agent); weekly; owner Consumer Banking Operations; escalation AI Governance.
  - refusal-rate drop on out-of-scope queries: threshold -20% week-over-week; weekly; owner AI Governance; escalation model risk committee then CISO.
  - kill-switch activation: threshold any activation; continuous; owner AI Governance; escalation AI risk committee.
  - foundation-model version change: threshold any change; continuous; owner Vendor Management; escalation AI Governance with re-validation.

- **Residual risk**:
  - Cross-customer retrieval edge cases beyond the two observed in the pilot. Likelihood low; impact high (privacy event, GLBA / NYDFS Part 500 §500.17 trigger if covered entity, state breach laws). Owner CISO function jointly with Privacy Officer; accepted only with the firm-internal red team complete.
  - Indirect-injection-driven misleading comm-draft escapes CSR review and is sent. Likelihood low (block-and-wait gate); impact medium (UDAAP and complaint-rate exposure). Owner AI Governance Lead with conduct-team co-sign; quarterly review.
  - Vendor foundation-model swap shifts refusal behaviour and the human-in-the-loop assumption no longer holds for the same input distribution. Likelihood medium; impact medium. Owner AI Governance Lead with Vendor Management; review on every change-of-version notice.
  - Excessive-agency aggregation across a CSR shift surfaces more customer data than per-action guardrails would justify. Likelihood low; impact medium. Owner AI Governance with CISO; quarterly review.

- **Recommended owner actions**:
  - Complete firm-internal red-team set on indirect injection in customer-history retrieved content. Owner AI Governance with InfoSec red team; deadline pre-prod gate +30 days; severity high.
  - Add per-source provenance tag to all retrieved customer-history content. Owner Retrieval Platform Owner; deadline pre-prod gate; severity medium.
  - Drill the cross-customer-disclosure incident-response procedure with the privacy officer and CISO. Owner AI Governance with CISO; deadline 60 days post-go-live; severity medium.
  - Document the refusal-rate baseline before go-live. Owner AI Governance; deadline pre-prod gate; severity medium.
  - Establish complaint-rate and complaint-code baseline before go-live. Owner Conduct team with AI Governance; deadline pre-prod gate; severity medium.
  - Add `foundation_model_swap_revalidation` flag to change management with explicit re-run on every change-of-version notice. Owner AI Governance with Vendor Management; deadline pre-prod gate; severity high.
  - Drill kill-switch quarterly per tier-2 cadence; record `last_drilled` in change-management. Owner AI Governance; recurring; severity medium.
  - Per-tool blast-radius re-validation review on any tool addition. Owner AI Governance; recurring; severity medium.

- **Source trace and confidence** — vendor red-team results at vendor-self-attestation confidence (low-to-medium); pilot evidence at high confidence; firm-internal red-team carries `[evidence needed]`; NYDFS October 2024 letter alignment at high confidence; 12 CFR Part 53 alignment at high confidence; logging-exercised confirmed at high confidence (sample log lines read).

- **Reviewer attestation** — pending; expected decision: accept-with-conditions, conditional on the firm-internal red team, the per-source provenance tagging, the kill-switch drill, and the complaint-rate baseline. Co-acceptors: CISO function (cyber overlay), Privacy Officer (privacy overlay), Consumer Banking Compliance (conduct overlay).

## Why this scenario matters

- The scenario is the v1 archetype for agentic-controls review in retail banking. The most-likely failure modes (cross-customer retrieval bleed, indirect injection in customer history, tool-misuse via repeated card-lock) are surfaced by the threat-assessment table.
- Authority statement enumerates concrete out-of-scope actions, not descriptive prose. The boundary against scope drift is explicit.
- Tool inventory carries blast radius on every entry. A tool list without blast-radius framing would not surface the per-shift abuse case.
- Human oversight entries carry effective-oversight evidence pointers (gate-decision logs, sampling audit logs, send-event logs). Theatrical oversight is the failure mode the section exists to surface.
- Kill switch carries a `last_drilled` date and a quarterly drill cadence per tier-2. Documentation alone is theatre.
- Threat assessment names the carrier, the source taxonomy, and the result on every entry. Generic "prompt injection" with no class or carrier would fail.
- Logging is exercised: sample log lines were read, not just policy-asserted.
- Incident-response section names the regulator-notification triggers (NYDFS §500.17, 12 CFR Part 53 36-hour, SEC 8-K Item 1.05) and the off-switch criterion per class.
- Recommended actions name owners as functions, not individuals; deadlines tie to operational milestones.
