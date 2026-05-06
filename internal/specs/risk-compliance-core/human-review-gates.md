# human-review-gates — spec sheet

Plugin: `risk-compliance-core`
Phase 2 owner: TBD
Status: spec locked, content build pending

## Activation-tuned description

Builds the named-gate matrix for a workflow, mapping decision points to required human reviewers, criteria, evidence inputs, and stop conditions. Output is a gate matrix and a one-page narrative that an AI governance committee, vendor onboarding committee, or issue-rating committee can adopt as charter language.

Best for:
- Standing up a new committee or governance gate (AI use-case approval, vendor onboarding, model release, issue rating, customer-impact action).
- Auditing an existing workflow for missing or under-specified human-review gates ahead of an exam or internal audit.

Not the right tool when:
- The work is a control matrix for a process (use `control-matrix`; gates are a subset of controls but reviewed differently).
- The work is a single approval memo for a specific decision (out of scope; gates define the recurring review structure, not the per-instance decision).
- The work is the underlying issue or model artifact being gated (use `issue-writeup`, `model-card-builder`, etc.).

Anchored to: SR 11-7 §VI governance, policies, and controls (effective challenge expectations) [verify section]; OCC Bulletin 2026-13 §III.E independent challenge and §III.F human oversight [verify section]; NIST AI RMF 1.0 (January 2023) Govern function GV-1 to GV-6 (accountability and oversight); EU AI Act (Regulation (EU) 2024/1689) Article 14 (human oversight) and Article 26 (deployer obligations); ISO/IEC 42001:2023 §5.3 roles and responsibilities and §8.3 AI system impact assessment [verify section].

## Source anchors

Primary:
- SR 11-7, April 4, 2011. §VI governance, policies, and controls — effective challenge as the conceptual root of human-review gates in model risk. Use for: gate criteria around validation independence, override authority, escalation. [verify section labels]
- OCC Bulletin 2026-13, 2026. §III.E independent challenge, §III.F human oversight, §III.G third-party model gate expectations. Use for: refreshed gate language post-2026 guidance. [verify]
- NIST AI RMF 1.0, January 2023. Govern function categories GV-1 through GV-6. Use for: enterprise-wide AI gate scaffolding (intake, tiering, deployment, ongoing monitoring).
- EU AI Act (Regulation (EU) 2024/1689). Article 14 (human oversight) and Article 26 (deployer obligations of high-risk AI systems). Use for: high-risk AI use-case gates with documented human-in-the-loop or human-on-the-loop posture.
- ISO/IEC 42001:2023 §5.3 (roles, responsibilities, authorities), §8.3 (AI system impact assessment). Use for: AIMS-aligned governance gate documentation. [verify section labels]

Secondary (overlay only):
- U.S. interagency third-party risk management guidance (June 2023) §III.B planning and §III.C due diligence — when the gate is a vendor-onboarding gate.
- CFPB UDAAP exam manual [verify section] — when the gate is on a customer-impacting decision.

## Sector overlays needed

- `banking.md` — Covers OCC heightened standards [verify] expectations on board and risk committee oversight, FRB SR 16-11 [verify] for supervisory expectations on senior management oversight.
- `insurance.md` — Covers NAIC ORSA governance and corporate-governance disclosure requirements [verify section], and state DOI committee-charter conventions.
- `capital-markets.md` — Covers FINRA 3110 supervision [verify], SEC Rule 206(4)-7 (advisers compliance) [verify section] for the adviser oversight gate posture.
- `payments-fintech.md` — Covers OCC bank-fintech partnership oversight expectations [verify] for sponsor-bank gate structures.

## Cross-cutting overlays needed

- `cyber.md` — Required when gates cover incident-response decisions or cyber-disclosure decisions. Anchors: SEC 8-K Item 1.05 disclosure committee posture; NYDFS Part 500 §500.4 senior governing body responsibility.
- `privacy.md` — Optional when gates touch consumer-data decisions.
- `climate.md` — Not required at v1.
- `conduct.md` — Required when gates touch customer-facing decisions (product approval, fee-change approval, marketing approval). Anchors: CFPB UDAAP exam manual [verify section].

## Output template named sections

Top of artifact:
- Workflow in scope (e.g., AI use-case lifecycle, vendor onboarding, issue rating)
- Source posture and confidence label
- Decision authority hierarchy (who can approve, who can challenge, who can escalate)

Body — the gate matrix, one row per gate, with these named columns:
- Gate ID
- Gate name (e.g., "Tier 1 AI use-case go-live gate", "Critical vendor onboarding gate")
- Stage in workflow
- Trigger (what brings a case to this gate)
- Required reviewers (named roles, with primary and backup)
- Required inputs (artifacts that must be present, by ID)
- Decision criteria (named criteria, traceable to source)
- Stop conditions (what blocks pass)
- Escalation path (where a no-pass goes)
- Documentation requirement (what gets captured at the gate)
- Frequency (event-based or periodic)
- Source anchor

Tail of artifact:
- One-page narrative summarising the gate flow for committee adoption (decision authority, gate sequence, escalation, documentation)
- Gaps in current workflow (gates implied by source but not present)
- Recommended charter language (suggested wording for committee charter or policy section)
- Source trace and confidence label
- Sign-off block

## Structured output fields

Wrapper object:
- `gate_matrix_id`: string.
- `workflow_in_scope`: string.
- `decision_authority`: object. `primary_committee` (string), `escalation_committee` (string), `dissent_path` (string).
- `gates`: array of gate objects.
- `gate_gaps`: array of objects with `gap_description` (string), `source_anchor` (string).
- `confidence_label`: enum.
- `reviewer_questions`: array of strings.
- `human_review_required`: boolean. Always true.

Gate object (new schema, phase 2 should add as `schemas/review-gate.schema.json`):
- `gate_id`: string.
- `gate_name`: string.
- `stage`: string.
- `trigger`: string.
- `required_reviewers`: array of objects with `role` (string), `independence_required` (boolean), `is_backup` (boolean).
- `required_inputs`: array of strings (artifact IDs).
- `decision_criteria`: array of objects with `criterion` (string), `source_anchor` (string).
- `stop_conditions`: array of strings.
- `escalation_path`: string.
- `documentation_requirement`: array of strings.
- `frequency`: enum (`event-based`, `daily`, `weekly`, `monthly`, `quarterly`, `annual`).
- `source_anchor`: string.

## Example scenarios

### Scenario 1: AI use-case lifecycle gates for a regional bank

Input: a regional bank's enterprise risk function is standing up an AI governance committee and needs the named gates from intake to retirement. Source posture is OCC 2026-13 plus NIST AI RMF plus the firm's MRM policy. Risk tiering uses tiered impact (T1 high, T2 moderate, T3 low).

Output emphasizes:
- Five gates: intake (any tier), tiering review (any tier), pre-prod gate (T1 and T2), production go-live (T1 only with model risk committee, T2 with line-1 head and second-line concurrence), annual review (any tier).
- Required reviewers for T1 go-live: head of model risk (primary), independent validator (challenge), business head (sponsor), CISO (cyber input). Independence is enforced — validator cannot also be developer.
- Stop conditions on pre-prod gate: open critical or high issues, missing model card, no validation report.
- Cyber overlay flagged for any T1 use case touching customer data.
- Recommended charter language: a three-paragraph block that the AI governance committee charter can adopt directly.
- Gaps in current workflow: no formal annual-review gate today; flagged as governance gap.

### Scenario 2: Critical vendor onboarding gate aligned to interagency TPRM guidance

Input: a mid-sized bank is refreshing its vendor onboarding gates for critical third-party arrangements. Source posture is interagency TPRM guidance (June 2023) plus the firm's third-party policy.

Output emphasizes:
- Four gates aligned to TPRM lifecycle: planning gate (criticality decision), pre-contract gate (due diligence pack review), contract gate (legal and risk concurrence), post-onboarding 90-day gate (operational confirmation).
- Required reviewers for pre-contract gate: head of vendor management (primary), business sponsor, information security, legal, and (for critical arrangements) operational risk committee.
- Stop conditions on pre-contract gate: missing SOC 2 Type II report, no exit plan, unresolved high-residual-risk findings.
- Decision criteria traced to TPRM guidance §III.C on due diligence and selection.
- Documentation requirement names the system of record where each gate's decision is logged.
- Recommended charter language for the operational risk committee terms of reference.

## Common pitfalls

1. Gates without independence. A "review" performed by the same team that produced the artifact is not a gate. The required_reviewers section must mark independence_required where the source guidance demands it (validation independence under SR 11-7, line-1 vs. line-2 separation under interagency TPRM).
2. Stop conditions that are not stops. "Should be reviewed" is not a stop condition. Phase 2 must require declarative stop conditions (e.g., "no go-live if any open critical issue").
3. Gates without artifacts. A gate that says "review the model card" without naming the artifact ID is unauditable. Required_inputs must reference artifact IDs that exist or can be generated.
4. Overloading one committee. If the same committee owns intake, tiering, pre-prod, go-live, and retirement, the firm has one committee, not a gate matrix. Phase 2 should flag this as a governance gap.
5. Conflating documentation with decision. The documentation_requirement is what gets captured. The decision is the gate outcome. A row that names what gets captured but not what counts as pass / fail is incomplete.
