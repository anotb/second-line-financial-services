# Example: agentic-controls review for an insurance claims-AI agent

Public-source-derived. No named institution. This scenario carries the substance of what would otherwise be a standalone claims-AI controls workflow, applied here through the insurance overlay.

## Input description

A US-only personal-lines auto and homeowners P&C insurer is in pre-prod for an agentic claims-AI system. The agent runs against the carrier's claims platform with a TPA partner handling first-notice-of-loss intake. Architecture: planner-executor split, foundation-model dependent (vendor-pinned), RAG over claims-platform records, OCR-ingested correspondence, repair-estimate documents, police reports; tool inventory includes claim-read, claim-note-write, automated-payment-issue (under threshold), reasoned-denial-draft, claim-acknowledgment-send, callback-schedule, supervisor-escalation-flag.

Engagement scope provided by `scoping`:

- Institution type: stock P&C insurer, multi-state-licensed (35-state footprint including CA, NY, CO, FL, TX); ORSA filer.
- Persona: AI Governance Lead (second line); MRMO and chief actuary as model-risk co-reviewers; CISO function as cyber co-reviewer; privacy officer (HIPAA does not apply for auto/HO P&C, but state breach-law analysis is structural); claims operations leadership as conduct co-reviewer; chief underwriting officer (out of direct scope but informed); state-licensing function for cross-state UCSPA matrix.
- Sector overlay: insurance (carrying the absorbed claims-AI control bar). Cross-cutting overlays: cyber (NYDFS Part 500 in NY, October 2024 letter; state Insurance Data Security Model Law in adopting states), conduct (NAIC #880 fair-claims-settlement and state UCSPA per-state).
- Source posture: public-plus-firm-policy-plus-system-of-record-evidence; TPA-side evidence partial (TPA's §4.F evidence pack requested).
- Tier: tier-1 (consumer-facing actuation, multi-state regulatory exposure, ORSA-material).

Upstream artifacts: `model-card-builder` output is on file; `validation-plan` robustness block partial; `prompt-injection-risk` has run.

## Output sketch

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

## Why this scenario matters

- The scenario is the canonical insurance use case carried by the insurance overlay rather than a standalone claims-AI controls skill.
- Authority statement enumerates the claims-AI-specific out-of-scope actions (no denial without licensed-adjuster review, no payment above threshold, no UPL-crossing communications). The fair-claims-settlement bar is structural; the agent cannot move it.
- Tool inventory carries blast-radius framing in claims-specific terms (per-claim cap, daily aggregate cap, per-shift cap, communication blast in policy units).
- Human oversight enforces block-and-wait on reasoned-denial drafting (post-hoc on a sent denial would be a UCSPA violation, not a control). The insurance overlay's claims-AI control bar comes through here.
- Threat assessment surfaces the planner-executor seam as a partial-result class with a critical-severity recommended action; this is the agentic-specific failure mode that vendor red-teams rarely exercise.
- Incident response names state Insurance Data Security Model Law triggers in adopting states, NYDFS Part 500 §500.17, state DOI complaint-of-pattern triggers, and the NAIC AIS Program documentation update obligation.
- TPA-run intake creates a §4.F obligation chain; the controls review records the carrier's accountability and surfaces the TPA-evidence gap explicitly.
- ORSA materiality check is in scope because the agent is enterprise-material; the recommended actions name ORSA inclusion.
- Recommended actions are owner-by-function and tied to operational milestones (pre-prod gate, ORSA cycle); the critical-severity item (planner-executor seam re-test) blocks pre-prod sign-off.
