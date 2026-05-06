# Example: pre-prod gate review for a tier-1 KYC analyst assistant

Public-source-derived. No named institution. Pattern aligns with a US national bank holding company moving a GenAI assistant into production for the KYC analyst desk.

## Input description

A US national bank holding company is at the initial-release pre-prod gate for a tier-1 GenAI assistant supporting the KYC analyst desk. The assistant retrieves over the firm's KYC documentation corpus, customer-relationship-history datastore, third-party adverse-media feeds, and beneficial-ownership records, and drafts narrative summaries for analyst review and sign-off. RAG over four corpora; no tools enabled. Foundation model is vendor-hosted with version pinning and contractual change-of-version notice.

Engagement scope provided by `engagement-scoping`:
- Institution type: bank holding company, large-cap, primary regulators OCC and FRB; CFPB for the consumer-banking subsidiary; NYDFS for the NY-chartered subsidiary; FinCEN for BSA/AML scope.
- Persona: AI Governance Lead (second line) consolidating; AI risk committee secretary owns the gate motion.
- Sector overlay: banking. Cross-cutting overlays: cyber (NYDFS Part 500 in NY footprint, October 2024 letter), privacy (regulated NPI), conduct loaded but light (KYC analyst is internal user, not customer-facing).
- Source posture: public-plus-firm-policy-plus-system-of-record-evidence.

Upstream artifacts:
- `ai-use-case-intake`: current.
- `ai-risk-tiering`: tier-1, current.
- `ai-act-triage`: not applicable (no EU establishment in scope).
- `model-card`: current; GenAI overlay sections complete.
- `validation-plan` results: full validation completed; effective challenge questions resolved with evidence.
- `prompt-injection-review`: residual risk medium with monitoring in place; firm-internal red team complete.
- `rag-evaluation-review`: faithfulness above firm threshold; citation precision above threshold; cross-corpus leakage testing passed with two minor findings tracked to closure.
- `llm-vendor-evidence-review`: vendor system card current; swap-revalidation policy documented; vendor SOC 2 Type II current.
- `agentic-ai-controls`: not applicable (no tools, no agentic configuration).

## Output sketch

Sections produced (abbreviated):

- **Recommended decision**: go-with-conditions. Rationale: upstream artifacts current; prompt-injection and RAG evaluation residuals accepted with monitoring; vendor evidence in place; cyber and privacy overlay sign-offs pending pending IR drill and 90-day version pinning. Three blocking conditions pre-go-live; two tracking conditions post-go-live.

- **Upstream artifact roll-up**: nine artifacts, all current; `agentic-ai-controls` and `ai-act-triage` marked not-applicable with basis.

- **Open conditions** (three blocking, two tracking):
  - Blocking, owner role AI Governance Lead with CISO function, SLA pre-prod gate +14 days, severity high: drill the IR procedure on the highest-likelihood incident class (confirmed cross-customer information bleed) before go-live; the existing IR programme has not exercised an AI-specific scenario.
  - Blocking, owner role AI Governance Lead with vendor management, SLA pre-prod gate, severity high: pin the foundation-model version for the first 90 days post-go-live; vendor's published cadence is rolling-with-30-day-notice and the firm has elected to pin during stabilisation.
  - Blocking, owner role AI governance team with model risk, SLA pre-prod gate, severity medium: document refusal-rate baseline for the first 14 days of pilot; without a baseline the post-go-live monitoring threshold has no reference.
  - Tracking, owner role AI Governance Lead, SLA go-live + 60 days, severity medium: weekly AI risk committee escalation on faithfulness sampling for the first 60 days; thereafter move to standard cadence per model card.
  - Tracking, owner role vendor management with AI Governance Lead, SLA on every change-of-version notice, severity high: re-run the prompt-injection review and the RAG evaluation faithfulness block per the foundation-model swap re-validation policy.

- **Residual risk summary** (top 4 for tier-1):
  - Indirect injection in adverse-media retrieved content. Likelihood: low (firm-internal red team coverage in place; source-vetting at the data-vendor layer). Impact: medium (analyst-facing, not customer-facing; analyst sign-off gate). Owner: AI Governance Lead, quarterly review.
  - Cross-corpus retrieval edge cases beyond those tested. Likelihood: low. Impact: high (privacy event, GLBA notification, NYDFS §500.17(a) trigger if confirmed). Owner: CISO function jointly with Privacy Officer; review on retrieval-platform configuration change.
  - Vendor foundation-model swap shifts refusal behaviour and analyst review effort goes up. Likelihood: medium (vendor cadence documented). Impact: medium. Owner: AI Governance Lead with vendor management; review on every change-of-version notice.
  - BSA/AML programme-integrity exposure if KYC narrative quality drifts. Likelihood: low (analyst sign-off gate). Impact: high (programme-integrity examination exposure). Owner: BSA officer; quarterly review with citation-precision and analyst-edit-rate signals.

- **Monitoring readiness** (six signals, all live before go-live except IR drill scope):
  - Refusal rate on out-of-scope queries; threshold drop greater than 20% week-over-week; weekly; AI governance team; escalation: model risk committee, then CISO if cyber correlates.
  - Citation precision sampling on KYC narrative source attributions; 50 cases per week; threshold precision drop greater than 5 points; weekly; AI governance team; escalation: model risk committee.
  - Cross-corpus retrieval audit (random sampling plus rule-based detection); continuous; information security with privacy officer; escalation: CISO and Privacy Officer.
  - Foundation-model version monitoring; threshold any change; continuous; vendor management; escalation: AI Governance Lead.
  - Analyst-edit rate on assistant-drafted narratives; threshold drop below 30% sustained for two periods; weekly; BSA officer with model owner; escalation: BSA committee.
  - Output-anomaly detection (length, refusal pattern); threshold greater than 3 standard deviations; continuous; information security; escalation: CISO.

- **Incident response readiness**: procedures documented in the firm IR programme; drill scheduled but not yet executed (blocking condition). Notification triggers evaluated: NYDFS Part 500 §500.17(a), GLBA Safeguards notification under 16 CFR §314.5(d), state breach laws per the firm's matrix, the 36-hour banking computer-security incident notification rule (12 CFR Part 53). Off-switch documented: pause assistant and revert to manual KYC narrative drafting.

- **Human oversight design**: KYC analyst reviews and signs the assistant-drafted narrative as the in-the-loop decision point; sampling expectation is 50 cases per week double-checked by senior analyst; effective oversight evidence is the analyst-edit-rate baseline collected during pilot; off-switch criterion is analyst-edit-rate below 30% sustained for two consecutive periods (interpreted as rubber-stamping).

- **Foundation-model dependency posture**: dependency present; provider X, model Y, version vN; pinned for first 90 days then rolling-with-notice. Swap re-validation policy: documented in change management with explicit re-run of prompt-injection review, RAG faithfulness block, and refusal-behaviour benchmark on every change-of-version notice. Vendor evidence review record on file.

- **Sector and cross-cutting overlay sign-offs**:
  - Banking (sector): pending; BSA officer signing after IR drill executes.
  - Cyber: pending; CISO function signing after IR drill executes.
  - Privacy: signed-with-conditions; Privacy Officer accepted residual risk on cross-corpus retrieval contingent on the cross-corpus retrieval audit signal staying live.
  - Conduct: not-applicable for this internal-user use case.

- **Sign-off block**: AI risk committee secretary (consolidating role), pending; model risk lead, signed; head of cyber (CISO function), pending pending IR drill; head of compliance, signed; BSA officer, pending pending IR drill and analyst-edit-rate baseline; Privacy Officer, signed-with-conditions.

- **Source trace and confidence**: upstream artifact IDs cited with attested confidence carried forward; vendor evidence at vendor-self-attestation confidence; firm-internal red-team results at high confidence.

## Why this scenario matters

- The scenario is a v1 archetype for the gate review: tier-1 GenAI use case where every upstream artifact is current and the gate review is the integration motion, not the diagnostic motion. Most pre-prod gate failures land here, not in artifact gaps.
- The blocking-versus-tracking distinction is load-bearing: without it, "go-with-conditions" is no-go in disguise or is permission to defer. The scenario shows three legitimate blocking items (IR drill, version pinning, baseline), and two legitimate tracking items.
- The sign-off block has six named roles, each with explicit position; the single-name sign-off failure mode is avoided by construction.
- The sector overlay (banking) brings the BSA officer in as co-signer and adds the 36-hour banking computer-security incident notification rule alongside the cyber-overlay-named NYDFS and SEC triggers; the overlay is consumed, not background reading.
- The foundation-model swap re-validation policy is explicit, with named re-run scope. Silent swap policy is the recurring defect this scenario closes by construction.
