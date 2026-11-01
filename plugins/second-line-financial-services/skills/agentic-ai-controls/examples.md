# Examples and troubleshooting

One section per worked example, then troubleshooting. Read only what you need.

## csr-copilot-regional-bank

### Example: agentic-controls review for a CSR co-pilot at a regional US bank

Public-source-derived. No named institution. The scenario is the archetype for agentic controls in retail banking: a vendor-hosted GenAI assistant inside the consumer-banking call center that summarises customer state, suggests next-best actions, drafts written follow-ups, and is wired to a small inventory of tools (account-read, card-lock-temp, callback-schedule, comm-draft).

#### Input description

A regional US bank holding company is approaching the pre-prod gate for a CSR co-pilot in the consumer-banking call center. RAG over the bank's customer-history datastore and policy/procedure corpus. Foundation model is vendor-hosted with version pinning and contractual change-of-version notice. The agent has four tools enabled.

Engagement scope provided by `scoping`:

- Institution type: bank holding company, mid-cap, primary regulators FRB and CFPB; OCC for the national-bank subsidiary; NYDFS for the NY footprint.
- Persona: AI Governance Lead (second line); CISO function as cyber co-reviewer; BSA officer not required (no AML-touching flow); privacy officer is a co-reviewer because the agent reads NPI; conduct-team co-reviewer for consumer-facing communication.
- Sector overlay: banking. Cross-cutting overlays: cyber (NYDFS Part 500 in NY, NYDFS October 2024 letter, 12 CFR Part 53 for the national-bank subsidiary), privacy (regulated NPI), conduct (UDAAP exposure on customer-facing communications).
- Source posture: public-plus-firm-policy-plus-system-of-record-evidence.
- Tier: tier-2.

Upstream artifacts: `model-card-builder` output is on file; `validation-plan` robustness block is partially complete (vendor red-team results landed; firm-internal red team scheduled); `prompt-injection-risk` has run and produced its memo.

#### Output sketch

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

#### Why this scenario matters

- The scenario is the archetype for agentic-controls review in retail banking. The most-likely failure modes (cross-customer retrieval bleed, indirect injection in customer history, tool-misuse via repeated card-lock) are surfaced by the threat-assessment table.
- Authority statement enumerates concrete out-of-scope actions, not descriptive prose. The boundary against scope drift is explicit.
- Tool inventory carries blast radius on every entry. A tool list without blast-radius framing would not surface the per-shift abuse case.
- Human oversight entries carry effective-oversight evidence pointers (gate-decision logs, sampling audit logs, send-event logs). Theatrical oversight is the failure mode the section exists to surface.
- Kill switch carries a `last_drilled` date and a quarterly drill cadence per tier-2. Documentation alone is theatre.
- Threat assessment names the carrier, the source taxonomy, and the result on every entry. Generic "prompt injection" with no class or carrier would fail.
- Logging is exercised: sample log lines were read, not just policy-asserted.
- Incident-response section names the regulator-notification triggers (NYDFS §500.17, 12 CFR Part 53 36-hour, SEC 8-K Item 1.05) and the off-switch criterion per class.
- Recommended actions name owners as functions, not individuals; deadlines tie to operational milestones.

## insurance-claims-ai-agent

### Example: agentic-controls review for an insurance claims-AI agent

Public-source-derived. No named institution. This scenario carries the substance of what would otherwise be a standalone claims-AI controls workflow, applied here through the insurance overlay.

#### Input description

A US-only personal-lines auto and homeowners P&C insurer is in pre-prod for an agentic claims-AI system. The agent runs against the carrier's claims platform with a TPA partner handling first-notice-of-loss intake. Architecture: planner-executor split, foundation-model dependent (vendor-pinned), RAG over claims-platform records, OCR-ingested correspondence, repair-estimate documents, police reports; tool inventory includes claim-read, claim-note-write, automated-payment-issue (under threshold), reasoned-denial-draft, claim-acknowledgment-send, callback-schedule, supervisor-escalation-flag.

Engagement scope provided by `scoping`:

- Institution type: stock P&C insurer, multi-state-licensed (35-state footprint including CA, NY, CO, FL, TX); ORSA filer.
- Persona: AI Governance Lead (second line); MRMO and chief actuary as model-risk co-reviewers; CISO function as cyber co-reviewer; privacy officer (HIPAA does not apply for auto/HO P&C, but state breach-law analysis is structural); claims operations leadership as conduct co-reviewer; chief underwriting officer (out of direct scope but informed); state-licensing function for cross-state UCSPA matrix.
- Sector overlay: insurance (carrying the absorbed claims-AI control bar). Cross-cutting overlays: cyber (NYDFS Part 500 in NY, October 2024 letter; state Insurance Data Security Model Law in adopting states), conduct (NAIC #880 fair-claims-settlement and state UCSPA per-state).
- Source posture: public-plus-firm-policy-plus-system-of-record-evidence; TPA-side evidence partial (TPA's §4.F evidence pack requested).
- Tier: tier-1 (consumer-facing actuation, multi-state regulatory exposure, ORSA-material).

Upstream artifacts: `model-card-builder` output is on file; `validation-plan` robustness block partial; `prompt-injection-risk` has run.

#### Output sketch

Sections produced (abbreviated):

- **Agent metadata** — `claims-ai-agent-v0.9`, tier-1, pre-prod, sponsor function: Claims Operations.

- **Scope and authority statement**:
  - In-scope actions: read claim records and supporting documents; draft claim notes for adjuster review; auto-issue payment under $5,000 on routine claims meeting fast-track criteria; draft reasoned denial for licensed-adjuster review and signature; send templated claim-acknowledgment communication; schedule callback; flag claim for supervisor escalation when criteria met.
  - Out-of-scope actions (concrete entries): no claim denial without licensed-adjuster review of the reasoned denial; no claim approval above the $5,000 fast-track threshold without supervisor approval; no policy cancellation; no fee imposition; no out-of-state-licensing-violating actions; no UPL-crossing legal advice or coverage-opinion communications; no SIU referral generation without fraud-investigator review; no policyholder communications outside the templated acknowledgment set without licensed-adjuster review; no third-party (claimant, attorney) communications without licensed-adjuster review.
  - Geographic scope: 35-state footprint with the most-prescriptive state (CA for UCSPA timing, NY for cyber, CO for limited-scope ECDIS-adjacent governance) setting the bar.
  - Customer scope: personal-lines auto and HO P&C policyholders.
  - Financial impact per action: automated-payment-issue capped at $5,000 per claim with daily aggregate cap and per-adjuster-shift cap; reasoned-denial-draft is text-only with no actuation.
  - Reversibility: payment is partially reversible (clawback process); claim-note-write is reversible; reasoned-denial-draft is reversible until adjuster sends.

- **Architecture summary** — planner-executor split; foundation model `vendor-X model-Y vN` pinned with contractual change-of-version notice; RAG over claims-platform records, OCR-ingested correspondence (claimant letters, repair estimates, police reports, attorney correspondence), supporting documents; planner is a single planner; specialist tool-executor agent invokes tools; session memory only; modalities text plus OCR'd image-derived text. Autonomy level: agentic-with-tool-use (with block-and-wait gates on consequential actions).

- **Tool inventory** — each entry with full blast-radius framing:
  - claim-read: claims platform, read, scoped to adjuster's queue, blast radius "could surface up to N claims per session if scoping fails", rate limit 60/min, owner Claims Operations.
  - claim-note-write: claims platform, write, scoped to single claim per call, blast radius "could write up to 10 notes per minute (cumulative log noise)", rate limit 10/min, owner Claims Operations.
  - automated-payment-issue: claims-payment system, write, scoped to single claim under $5,000 with daily aggregate cap of $250,000 per agent and per-shift cap of $50,000, blast radius "could issue up to $5,000 per claim, $250,000/day if abused; not reversible without clawback process", rate limit 1/2-minutes plus daily cap, owner Claims Operations with Treasury concurrence on caps.
  - reasoned-denial-draft: text generation only, no actuation, blast radius "draft text only — no send; absent block-and-wait could be aggregated for queue prioritisation manipulation", rate limit not applicable, owner Claims Operations.
  - claim-acknowledgment-send: outbound communication system, communicate, scoped to single claim per call with templated content only, blast radius "could send up to 60 acknowledgments per hour to in-scope claimants per state UCSPA timing; off-template content not allowed at the send tool", rate limit 1/min, owner Claims Operations with Compliance concurrence.
  - callback-schedule: callback system, write, scoped to single claim per call, blast radius "could schedule up to 60/shift", rate limit 1/min, owner Claims Operations.
  - supervisor-escalation-flag: workflow system, write, scoped to single claim per call, blast radius "could flag up to 60/shift; over-flagging creates supervisor-overload conduct risk", rate limit 1/min, owner Claims Operations.
  - All other tools: not applicable (no policy-cancellation tool, no fee-imposition tool, no SIU-referral tool, no third-party communication tool).

- **Identity and authorisation** — service account `claims-ai-svc-prod`; per-claim and per-adjuster scoping enforced at platform layer; secrets in firm secrets manager rotated quarterly; identity-layer rate limits aligned to per-shift adjuster norms; session boundaries per claim-handling session.

- **Human oversight points**:
  - claim-read and summarisation: post-hoc-sample 5%, weekly audit; reviewer Claims Quality Assurance; evidence audit-log pointer.
  - claim-note-write: post-hoc-sample 5% with quality-grade scoring; reviewer Claims Quality Assurance.
  - automated-payment-issue under threshold: notify-and-revocable; supervisor-notification within 1 hour for any payment; reviewer Claims Supervisor; SLA same-day review of any flagged payment; evidence supervisor-review log.
  - automated-payment-issue at threshold or above (out-of-scope): block-and-wait supervisor approval; reviewer Claims Supervisor; SLA real-time.
  - reasoned-denial-draft: block-and-wait licensed-adjuster review-and-signature; the licensed adjuster is the named reviewer; SLA per-state UCSPA timing (most-prescriptive: CA's reasonable-investigation requirement plus 40-day decision); evidence pointer to denial-review log including timestamp of adjuster sign-off.
  - claim-acknowledgment-send: block-and-wait adjuster confirmation on first acknowledgment per claim; post-hoc-sample 10% on subsequent templated acknowledgments; SLA per-state UCSPA acknowledgment timing.
  - supervisor-escalation-flag: notify-and-revocable; reviewer Claims Supervisor.
  - Daily Quality Assurance review of agent's overall claim-handling pattern with conduct-team participation.

- **Guardrails** — input filter on OCR'd content with adversarial-pattern detection (config link, exercised in firm-internal red team); output filter for prohibited language, UPL-boundary crossings, and state-specific advertising-rule violations; refusal behaviour on out-of-scope queries (vendor-side plus firm-side rules for claims-specific out-of-scope); structured-output enforcement on reasoned-denial template (must include named UCSPA reasoning elements); escalation trigger on detected complaint-language in claimant communications.

- **Threat assessment** (entries name attack class, carrier, source taxonomy):
  - direct prompt injection in adjuster input — system prompt / user prompt; OWASP LLM01, MITRE ATLAS [verify]; vendor red team; pass.
  - indirect injection via OCR'd claimant correspondence — retrieved content; OWASP LLM01 indirect, MITRE ATLAS LLM Prompt Injection; firm-internal red team partial (vendor set, firm-internal scheduled); partial; routed to recommended actions.
  - indirect injection via OCR'd attorney correspondence — retrieved content; same taxonomy; firm-internal red team; partial; routed to recommended actions.
  - tool hijack (instructions in OCR'd correspondence cause automated-payment-issue invocation) — tool output / retrieved content; OWASP LLM07; firm-internal test (200-claim pilot); pass under block-and-wait threshold gate; one near-miss recorded.
  - cross-scope tool query (claim-read on claim outside adjuster's queue) — system prompt / agent reasoning; firm-internal test; partial (one case observed; mitigation in retrieval scoping config strengthened post-test).
  - excessive-agency exploitation (chained note-write, payment-issue, acknowledgment-send aggregating to material claim mishandling) — agent reasoning across actions; OWASP LLM08; firm-internal test (50-claim pilot focused on chained-action sequences); pass under daily-aggregate cap and supervisor-notification on any payment.
  - planner-executor seam (planner formulates plan executor runs without re-checking authority) — multi-agent message; OWASP LLM07/LLM08; firm-internal test; partial (one case where executor proceeded with payment despite planner's "needs supervisor review" annotation); routed to recommended actions and to residual risk.
  - exfiltration of system-prompt content — system prompt; OWASP LLM06; vendor red team; pass.
  - jailbreak to bypass UPL-boundary refusal — system prompt; OWASP LLM01; firm-internal test; pass under guardrail.
  - multi-agent message injection — multi-agent message; tested in planner-executor seam class.
  - memory poisoning — not applicable, session memory only.
  - sandbox escape — not applicable, no code-execution surface.

- **Sandbox and execution-environment guarantees** — `has_code_execution: false`. Explicit boundary statement: "No code-execution surface; agent restricted to enumerated tool calls; OCR pipeline runs in a separate scanned-document service with input-sanitisation at the OCR stage."

- **Kill switch and rollback**:
  - confirmed tool-misuse outside scope: AI-misuse runbook; owner AI Governance Lead with platform on-call and Claims Operations on-call; RTO under 5 minutes; last drilled 2026-04-22; quarterly cadence per tier-1; rollback path (any payment auto-issued in suspect window queued for adjuster re-review and clawback assessment; communications sent in suspect window reviewed for retraction and corrected communication; complaint-management system briefed).
  - confirmed cross-claim or cross-policyholder access: privacy-incident runbook; owner CISO and Privacy Officer; RTO under 5 minutes; off-switch fires immediately on first confirmed event.
  - confirmed planner-executor seam exploitation: AI-misuse runbook; RTO under 10 minutes; rollback path includes the claims-platform audit-log review of all actions in suspect window.
  - foundation-model behaviour shift: AI-vendor incident runbook; owner Vendor Management with AI Governance; RTO under 30 minutes; rollback path (revert to prior pinned version).

- **Logging, traceability, and audit** — log content covers every claim-read, every claim-note-write, every payment-issue, every reasoned-denial-draft, every adjuster sign-off, every supervisor approval, every kill-switch event, every guardrail trip; retention 7 years per state record-retention requirements (most-prescriptive); access controls limited to AI Governance, CISO, Claims Operations Compliance, Audit; immutability append-only with daily off-system snapshot; audit-trail aligned to NYDFS Part 500 §500.6 for NY footprint and to state UCSPA documentation expectations; exercised-in-test confirmed.

- **Incident response**:
  - confirmed tool-misuse outside scope: AI-misuse runbook; regulator-notification triggers NYDFS Part 500 §500.17(a) for NY footprint, state Insurance Data Security Model Law equivalent in adopting states (CA, FL among footprint states), state DOI complaint-of-pattern triggers, NAIC AIS Program documentation update; off-switch criterion: any confirmed event.
  - confirmed cross-claim or cross-policyholder access: state breach-notification analysis (50-state matrix); state Insurance Data Security Model Law equivalent; NYDFS §500.17 for NY-licensed; off-switch criterion: any confirmed event.
  - confirmed UCSPA-violating outcome from agent (untimely denial, unreasoned denial, miscommunication on coverage): state DOI notification per pattern threshold; complaint-management system update; AIS Program documentation reflecting the residual-risk view; off-switch criterion: pattern of three or more confirmed events triggers agent pause pending fix.
  - confirmed planner-executor seam exploitation: AI-misuse runbook plus claims-quality-incident process; if material claim mishandling, state DOI considerations.
  - foundation-model behaviour shift: AI-vendor runbook; cyber-side cooperation with vendor.
  - HIPAA breach: not applicable for auto/HO P&C scope.

- **Escalation triggers**:
  - tool-invocation rate spike per tool (especially payment-issue): threshold +3 std-dev week-over-week; daily; owner AI Governance with Claims Operations; escalation Claims Supervisor and Operations Risk.
  - cross-scope tool query rate: threshold any non-zero; continuous; owner CISO and Privacy Officer; escalation immediate.
  - supervisor-override rate on adjuster-reviewed denials: threshold +2 std-dev; weekly; owner Claims Quality Assurance; escalation Claims Operations with conduct-team.
  - automated-payment-issue rate vs adjuster-reviewed-payment rate: threshold drift greater than 10% week-over-week; weekly; owner Claims Operations; escalation Claims Operations leadership and AI Governance.
  - state UCSPA timing distribution (acknowledgment, decision): threshold drift toward state limits; weekly per state; owner Claims Operations Compliance; escalation per-state.
  - complaint-rate and complaint-code drift: threshold +20% week-over-week or new complaint codes; weekly; owner Conduct Team; escalation Claims Operations leadership.
  - kill-switch activation: any activation; continuous; owner AI Governance; escalation AI risk committee.
  - foundation-model version change: any change; continuous; owner Vendor Management; escalation AI Governance with re-validation.

- **Residual risk** (with basis on every entry):
  - Indirect-injection-driven misleading reasoned-denial-draft escapes adjuster review and is sent. Likelihood low (block-and-wait gate plus structured-output enforcement); impact high (UCSPA violation, state DOI exposure, customer harm). Owner AI Governance with Claims Operations and conduct-team co-sign; quarterly review.
  - Cross-claim or cross-policyholder retrieval bleed beyond pilot scope. Likelihood low (mitigation strengthened post-test); impact high (privacy event, state breach laws, NYDFS §500.17, state Insurance Data Security Model Law in adopting states). Owner CISO with Privacy Officer; conditional acceptance pending firm-internal red-team complete.
  - Planner-executor seam exploitation: planner annotation ignored by executor. Likelihood medium (one case observed pre-fix; fix in place but not exercised in re-test); impact high (potential automated payment outside authority). Owner AI Governance with Claims Operations; review on every change to planner-executor protocol.
  - Vendor foundation-model swap shifts refusal behaviour or planner reasoning. Likelihood medium; impact high. Owner AI Governance with Vendor Management; review on every change-of-version.
  - TPA-run intake side-channel risk: TPA's §4.F evidence pack incomplete; carrier accountable per Model #668 §4.F. Likelihood medium; impact medium-to-high. Owner AI Governance with Vendor Management and Claims Operations; conditional acceptance pending TPA evidence pack.
  - State UCSPA timing variation across 35-state footprint may cause occasional miss on most-prescriptive state. Likelihood low; impact medium. Owner Claims Operations Compliance; quarterly per-state review.
  - Excessive-agency aggregation across a high-volume day creates supervisor-overload pattern. Likelihood low; impact medium. Owner Claims Operations with AI Governance; quarterly review.

- **Recommended owner actions**:
  - Complete firm-internal red-team set on indirect injection in OCR'd claimant and attorney correspondence. Owner AI Governance with InfoSec red team; deadline pre-prod gate +30 days; severity high.
  - Re-test planner-executor seam after fix; certify the planner's authority annotations are honoured by the executor in 100% of synthetic test cases. Owner AI Governance; deadline pre-prod gate; severity critical.
  - Obtain TPA's §4.F evidence pack and reconcile with carrier's controls review. Owner Vendor Management with AI Governance; deadline pre-prod gate; severity high.
  - Drill cross-claim or cross-policyholder access incident-response procedure with Privacy Officer and CISO. Owner AI Governance with CISO; deadline pre-prod gate; severity high.
  - Document state UCSPA timing matrix (35-state footprint) and map agent's actuation timing against the most-prescriptive state. Owner Claims Operations Compliance; deadline pre-prod gate; severity high.
  - Establish complaint-rate and complaint-code baseline by state before go-live. Owner Conduct Team with Claims Operations; deadline pre-prod gate; severity medium.
  - Update NAIC AIS Program documentation to reflect this controls review and the residual-risk acceptance. Owner AI Governance with Compliance; deadline pre-prod gate; severity medium.
  - For NY footprint, map the agent's controls to NYDFS October 2024 letter expectations and Part 500 obligations. Owner AI Governance with CISO; deadline pre-prod gate; severity high.
  - For CO footprint (limited-scope ECDIS-adjacent governance applies indirectly via SB 21-169 to life carriers; this carrier is P&C, but the disclosure-and-recourse framing may inform CA bulletin posture): map disclosure posture per CA bulletin. Owner AI Governance with State Licensing; deadline pre-prod gate; severity medium.
  - Confirm ORSA inclusion: agent named in ORSA Summary Report as an enterprise-material AI use case. Owner Chief Risk Officer with AI Governance; deadline next ORSA cycle; severity medium.
  - Drill kill-switch quarterly per tier-1 cadence; record `last_drilled` in change-management. Owner AI Governance; recurring; severity medium.
  - Add `foundation_model_swap_revalidation` flag to change management. Owner AI Governance with Vendor Management; deadline pre-prod gate; severity high.
  - Per-tool blast-radius re-validation review on any tool addition. Owner AI Governance; recurring; severity medium.
  - Schedule expansion-review trigger on any new sponsor function, geography, customer segment, or tool. Owner AI Governance; recurring; severity medium.

- **Source trace and confidence** — vendor red-team results at vendor-self-attestation confidence (low-to-medium); pilot evidence at high confidence; firm-internal red-team set carries `[evidence needed]` for indirect-injection coverage; planner-executor seam fix not yet exercised at high confidence (re-test required); NAIC #880 / state UCSPA citations at high confidence with section references in `references/source-anchors.md`; NYDFS October 2024 letter and Part 500 alignment at high confidence; TPA §4.F evidence pack carries `[evidence needed]`.

- **Reviewer attestation** — pending; expected decision: reject-and-rework on the planner-executor seam re-test (severity critical), with conditional accept on the remaining items pending firm-internal red team, TPA evidence pack, state-UCSPA matrix, and kill-switch drill. Co-acceptors: MRMO and chief actuary (model-risk overlay); CISO function (cyber overlay); Claims Operations leadership and conduct team (insurance overlay's claims-AI control bar); state-licensing function (cross-state matrix sign-off); chief risk officer (ORSA materiality).

#### Why this scenario matters

- The scenario is the canonical insurance use case carried by the insurance overlay rather than a standalone claims-AI controls skill.
- Authority statement enumerates the claims-AI-specific out-of-scope actions (no denial without licensed-adjuster review, no payment above threshold, no UPL-crossing communications). The fair-claims-settlement bar is structural; the agent cannot move it.
- Tool inventory carries blast-radius framing in claims-specific terms (per-claim cap, daily aggregate cap, per-shift cap, communication blast in policy units).
- Human oversight enforces block-and-wait on reasoned-denial drafting (post-hoc on a sent denial would be a UCSPA violation, not a control). The insurance overlay's claims-AI control bar comes through here.
- Threat assessment surfaces the planner-executor seam as a partial-result class with a critical-severity recommended action; this is the agentic-specific failure mode that vendor red-teams rarely exercise.
- Incident response names state Insurance Data Security Model Law triggers in adopting states, NYDFS Part 500 §500.17, state DOI complaint-of-pattern triggers, and the NAIC AIS Program documentation update obligation.
- TPA-run intake creates a §4.F obligation chain; the controls review records the carrier's accountability and surfaces the TPA-evidence gap explicitly.
- ORSA materiality check is in scope because the agent is enterprise-material; the recommended actions name ORSA inclusion.
- Recommended actions are owner-by-function and tied to operational milestones (pre-prod gate, ORSA cycle); the critical-severity item (planner-executor seam re-test) blocks pre-prod sign-off.

## troubleshooting

### Troubleshooting: agentic-ai-controls

Recurring defects from agentic-controls reviews and how to address them. Read alongside the skill's load-bearing list and the loaded sector and cross-cutting overlay common-pitfalls sections.

#### Authority statement is descriptive prose with no enumeration of out-of-scope actions

"The agent helps representatives serve customers" tells a reviewer nothing about the boundary. The boundary becomes operational drift inside three months of deployment: the next request adds one more tool, one more customer segment, one more action, and the agent is doing things the original review did not contemplate.

Fix: the out-of-scope action list requires at least three concrete entries, each phrased as a verb against a system. Sector overlays raise the bar (insurance: no claim denial without licensed-adjuster review; banking: no funds movement; capital markets: no order routing outside firm risk thresholds). Generic out-of-scope items ("no harmful actions") are policy assertions, not control surfaces.

#### Tool inventory captures tool names but not blast radius

A tool labelled "schedule callback" can spam every customer in a queue if rate-limited badly. A tool labelled "automated payment under threshold" can drain the firm's daily payment cap if the cap is not at the tool layer. A tool labelled "comm-draft" looks harmless until it is wired to a send tool no one noticed.

Fix: every entry in `tool_inventory[]` requires the `blast_radius` field populated in concrete firm policy units (count, value, customers affected, per minute / per shift / per day). The blast-radius framing surfaces the worst-case operational outcome, not the expected outcome. A tool list without blast-radius framing is a list, not a control surface.

#### Human oversight is documented but not effective

Reviewers click through. Approval gates become rubber stamps. Sampling is documented but not audited. The control surface looks complete in policy and is hollow in operation.

Fix: every `human_oversight[]` entry requires `evidence_of_effectiveness` populated. The evidence pointer is a gate-decision log, a sampling audit, a drift signal, or a similar artefact that supports the assertion the oversight catches what it is meant to catch. `[evidence needed]` flags route to recommended actions. EU AI Act Article 14 framings on effective oversight apply by analogy outside in-scope deployments. For consequential actions in regulated contexts (claims denial, lending denial, customer communications), block-and-wait is the only acceptable mode; post-hoc sampling on a sent customer-impact communication is not a control.

#### Kill switch is documented but never drilled

A kill switch that has not been drilled is theatre. The drill exercises both the technical kill-switch (cutting tool privileges, pausing the model serving endpoint) and the operational decision chain (who calls it, who confirms, who records, who signs off on resumption). Without the drill, the operational decision chain fails on the first real event.

Fix: every `kill_switch[]` entry carries `last_drilled` and `drill_cadence`. If `last_drilled` is older than the tier's required cadence, the entry flags as a gap and routes to recommended actions. Drill cadence: annual at minimum; quarterly for tier-1 use cases; on every tool addition or major version change. The drill record itself enters source trace at high confidence.

#### Threat assessment lists generic "prompt injection" with no carrier or class

Indirect injection via retrieved customer-history content is a different control problem from direct injection in the system prompt. Tool hijack via tool output is a different attack class from cross-scope tool query. Excessive agency exploitation is OWASP LLM08 and is mostly invisible at the per-action layer.

Fix: every `threat_assessment[]` entry names attack class, carrier (system prompt, user prompt, retrieved content, tool output, agent memory, multi-agent message, multimodal input), and source taxonomy (MITRE ATLAS technique ID, OWASP LLM identifier, NIST AI 600-1 subcategory). The agentic-specific attack classes that are non-optional for any agent with tool use: tool hijack, cross-scope tool query, excessive agency exploitation, planner-executor seam. Add memory poisoning for persistent-memory systems; multi-agent message injection for multi-agent topologies; sandbox escape for systems with code execution.

#### Sandbox guarantees recorded as policy without enforcement evidence

A sandbox the firm has not exercised is a sandbox that does not bind in incident response. "Process isolation: enforced via container runtime" is policy; "process isolation: enforced via container runtime, with last verified-via-test 2026-04-15, test report at <pointer>" is evidence.

Fix: `sandbox_guarantees.enforcement_evidence` must be populated. Policy without enforcement evidence routes to recommended actions, not to coverage. For tool-use-only systems without execution, the explicit boundary statement ("no code-execution surface; agent restricted to enumerated tool calls") is the correct artifact and is required.

#### Logging exists but is not actually being written to

A logging entry recorded as policy and never confirmed by reading a sample log line is a frequent finding in pre-prod reviews. The log destination is misconfigured; the retention is not set; the immutability posture is not enforced; the access control list is wrong.

Fix: `logging.exercised_in_test` is set explicitly. Reading a sample log line for each event class (model invocation, tool call, plan step, oversight event, kill-switch event) before pre-prod sign-off is non-optional. False routes to recommended actions.

#### Incident response lists procedures without naming the regulator-notification triggers

A procedure pointer alone leaves the firm's notification posture unspecified. NYDFS §500.17(a), 12 CFR Part 53 / Part 225 / Part 304 36-hour rule, SEC 8-K Item 1.05, GLBA Safeguards Rule, state breach laws, sector-specific notifications (state insurance commissioner under the Insurance Data Security Model Law in adopting states, HIPAA breach-notification under §§164.400-414), and producer-licensing notifications may apply concurrently.

Fix: every `incident_response[]` entry populates `regulator_notification_trigger` with the named rule and the relevant condition. Where multiple notification regimes apply, list each separately. Sector overlays carry the sector-specific triggers; load the overlay and surface the triggers in the structured object.

#### Off-switch criterion missing on cyber-relevant or customer-impact-relevant incident classes

A confirmed exfiltration with no defined off-switch is a finding. A confirmed UCSPA-violating outcome with no defined off-switch is a fair-claims-settlement violation in waiting. The off-switch criterion is the operational decision the runbook turns on; without it, the runbook stops at "investigate".

Fix: every `incident_response[]` entry populates `off_switch_criterion`. For agentic systems with tool use, the off-switch is typically a combination of cutting tool privileges and pausing the model serving endpoint. For human-in-the-loop systems, the off-switch is typically pausing the agent and switching to the manual workflow. For insurance claims AI, the off-switch pauses claim actuation while leaving human-claims-handling operational. If there is no off-switch, that is itself a critical-severity recommended action.

#### Foundation-model swap re-validation flag missing

For any architecture depending on a third-party foundation model, the standard recommended-action item that fires is the `foundation_model_swap_revalidation` flag in change management. A vendor model swap can shift refusal behaviour, alter the effective coverage of the firm's mitigations, change the planner-executor seam dynamics, and invalidate the residual-risk view.

Fix: confirm the `recommended_actions[]` section includes the foundation-model swap re-validation item with explicit re-run on every vendor change-of-version notice. If the foundation-model versioning posture is rolling-with-notice, additionally surface a recommended action to move to pinned versioning for tier-1 and tier-2 use cases.

#### Vendor red-team results presented as firm-side coverage

Vendor adversarial-test results test the vendor's foundation-model behaviour against the vendor's test set. They do not test the firm's tool inventory, authority logic, sandbox configuration, or oversight design. Treating vendor coverage as firm coverage is a recurring failure.

Fix: `threat_assessment[]` entries record the tester explicitly (vendor red team, firm-internal red team, third-party assessor). Source-trace entries record vendor evidence at vendor-self-attestation confidence (typically low to medium). Recommended actions surface firm-internal red-team coverage gaps as `[evidence needed]` items.

#### Planner-executor seam un-tested

A multi-agent topology with a planner formulating a plan and an executor running it is structurally vulnerable to the planner-executor seam: the planner's authority annotations are dropped, ignored, or downgraded by the executor under specific input distributions. Vendor red-team sets rarely exercise this surface.

Fix: for any multi-agent or planner-executor architecture, the `threat_assessment[]` table includes an explicit `planner_executor_seam` row, sourced from firm-internal red team. The success criterion is that the executor honours the planner's authority annotations in 100% of synthetic test cases. A partial result in this row is typically a critical-severity recommended action that blocks pre-prod sign-off.

#### Excessive-agency exploitation under-framed

A series of low-stakes actions chained together into a high-stakes outcome is the canonical agentic failure mode (OWASP LLM08). The per-action guardrails do not catch the chained outcome; the per-day or per-shift caps do.

Fix: for any agent with multiple tools or with iterative tool use within a session, the `threat_assessment[]` table includes an `excessive_agency_chain` row testing chained-action sequences. Daily-aggregate caps and per-shift caps at the identity layer or the tool layer are the load-bearing controls; cap-trip rates are escalation signals. The residual-risk view records the chain-aggregation risk explicitly.

#### Reviewer attestation lists named individuals

Reviewer roles are functions, never named individuals. Individuals leave; functions persist. A reviewer-attestation block listing "Jane Doe, AI Governance Lead" creates a fragile artifact.

Fix: replace any named individuals with the function (AI Governance Lead, MRMO, CISO function, Privacy Officer, Claims Operations leadership). Where the firm tracks which individual signed, the firm's gate-decision log records the individual; the controls review references the function.

#### Sector overlay loaded but the sector-specific seam not surfaced

Each sector overlay carries seams the controls review tends to miss without the overlay (banking: BSA officer involvement on AML-touching agent flows, 12 CFR Part 53 36-hour rule; insurance: NAIC #880 fair-claims-settlement, NAIC AIS Program element status, NAIC Model #668 §4.F where TPA runs the agent, UPL boundary on consumer-facing chatbots, ORSA materiality; capital markets: Rule 15c3-5 market-access for order-routing agents, FINRA Rule 3110 supervision; payments-fintech: BaaS shared-responsibility allocation, state money-transmitter licensing footprint). Loading the overlay without surfacing the seam is the failure mode.

Fix: re-read the loaded sector overlay against the review and confirm each named overlay-specific consideration is reflected in the authority statement, tool inventory, oversight points, threat assessment, monitoring, incident response, or recommended actions sections. The structured object's `sector_overlay_notes.<sector>` field carries the surfaced seams.

#### Cyber overlay loaded but used as background reading

The cyber overlay's load-bearing additions are the regulator-notification triggers, the cyber-tagged mitigations, the cyber-tagged monitoring signals, the sandbox guarantees enforcement evidence, the kill-switch drill records, and the CISO function as co-reviewer. Treating the overlay as background reading and not surfacing these in the structured object is the failure mode.

Fix: confirm `cross_cutting_overlay_notes.cyber` is populated; confirm the cyber-tagged tool-inventory entries, monitoring entries, and incident-response triggers are present; confirm the sandbox guarantees carry enforcement evidence; confirm the kill-switch entries carry drill records; confirm the reviewer attestation block names the CISO function as co-reviewer for cyber-flagged reviews.

#### Insurance overlay: relying on a fairness-only test where a fair-claims-settlement test is required

A claims-AI agent that passes a generic fairness eval and fails state UCSPA timing or reasoned-denial requirements is operationally non-compliant. Fair-claims-settlement is governed by NAIC #880 and state UCSPAs; fairness is a different test under a different statutory frame.

Fix: for any insurance claims-AI agent, the controls review records the agent's actuation timing against the most-prescriptive state's UCSPA timing requirement, the reasoned-denial drafting against the named UCSPA reasoning elements, and the human-oversight design against the licensed-adjuster review requirement. Generic fairness testing is recorded separately and does not substitute.

#### Insurance overlay: missing the UPL question on consumer-facing chatbots

Where the bot crosses into legal advice or coverage opinions, the carrier risks UPL exposure on top of unfair-trade-practices exposure. The boundary is at the guardrail layer.

Fix: for any consumer-facing claims-AI or insurance chatbot, the guardrails section records UPL-boundary refusal behaviour with an evidence pointer, exercised in firm-internal test. The recommended actions surface the UPL boundary as a recurring monitoring expectation.

#### Insurance overlay: TPA-run agents with §4.F evidence not collected

Where a TPA, claims administrator, or other vendor runs the agent on the carrier's policies, NAIC Insurance Data Security Model Law (Model #668) §4.F obligations attach; the carrier remains accountable. Reviewing the carrier's tools without the TPA's tools is half a review.

Fix: for any TPA-run agent, the controls review requests the TPA's §4.F evidence pack (security program, third-party-service-provider obligations, monitoring, incident-response cooperation, breach-notification chain). Gaps carry `[evidence needed]` with the TPA as owner; the carrier's residual-risk acceptance is conditional on the evidence pack.

#### Engagement scope not formalised

When the scope record is not supplied and the practitioner declines to formalise scope, the review still proceeds against a default public posture but should record the omission.

Fix: the review-metadata section notes that scope was not formalised; the recommended-actions section includes formalising scope as a low-or-medium-severity item; the source-trace confidence labels reflect the lack of formalised scope on items that would have been resolved by it.
