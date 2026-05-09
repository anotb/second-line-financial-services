# Example: prompt-injection review for a vendor-hosted GenAI customer-support assistant

Public-source-derived. No named institution. Pattern aligns with the same scenario carried by `model-card-builder/examples/genai-customer-support.md`; this review consumes that card and returns a focused prompt-injection memo.

## Input description

A regional US bank holding company is approaching the pre-prod gate for a vendor-hosted GenAI assistant inside the consumer-banking call center. The assistant summarises customer history, suggests next-best-action steps, and drafts written follow-ups for the agent to review and send. RAG over the bank's customer-history datastore and policy/procedure corpus. No tools enabled. Foundation model is vendor-hosted with version pinning and contractual change-of-version notice.

Engagement scope provided by `scoping`:
- Institution type: bank holding company, mid-cap, primary regulators FRB and CFPB; OCC for the national-bank subsidiary; NYDFS for the NY footprint.
- Persona: AI Governance Lead (second line), with CISO function as cyber co-reviewer.
- Sector overlay: banking. Cross-cutting overlays: cyber (NYDFS Part 500 in NY footprint, NYDFS October 2024 letter), privacy (regulated NPI), conduct (UDAAP exposure on customer-facing communications).
- Source posture: public-plus-firm-policy-plus-system-of-record-evidence.
- Tier: tier-2.

Upstream artifacts: `model-card-builder` output is on file; `validation-plan` robustness block is partially complete (vendor red-team results landed; firm-internal red team scheduled).

## Output sketch

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

## Why this scenario matters

- The scenario is the v1 archetype for prompt-injection review: a RAG-using GenAI assistant where the highest-likelihood vector is indirect injection in retrieved customer content, not direct injection by the user. Direct-only reviews miss the spine.
- Trust posture is the spine of the threat surface table; the scenario shows partially-trusted carriers where the trust basis is operational, not architectural.
- The mitigations list links each control to evidence and to the test that exercised it; mitigations without exercise become recommended actions, not assertions of coverage.
- Residual risk uses likelihood-and-impact framing with a one-line basis; "low" without basis is opinion, not analysis.
- The cyber overlap is explicit: cross-customer disclosure crosses NYDFS Part 500 §500.17 and state breach-law thresholds; the incident-response section names the trigger, not just the procedure.
- Recommended actions name owners as roles, not individuals, and tie deadlines to operational milestones (pre-prod gate, days post-go-live).
