# policy-gap-review — spec sheet

Plugin: `risk-compliance-core`
Phase 2 owner: TBD
Status: spec locked, content build pending

## Activation-tuned description

Compares a firm policy or procedure against an obligation set or public-source-informed control expectations and produces a gap table with severity, evidence needs, and recommended policy edits. Output is a side-by-side gap matrix plus a remediation list, not a marked-up policy document.

Best for:
- Refreshing a policy ahead of a regulator exam, internal audit, or post-enforcement uplift.
- Comparing an existing policy against a newly published rule or refreshed guidance (e.g., OCC 2026-13 against legacy SR 11-7-aligned MRM policy).

Not the right tool when:
- The work is extracting obligations from source (use `obligation-mapping`).
- The work is mapping obligations to controls (use `control-matrix`).
- The work is drafting a finding from a single policy gap (use `issue-writeup`).
- The work is the policy rewrite itself (out of scope; this skill produces the gap list, not the redline).

Anchored to: SR 11-7 §VI governance, policies, controls (policy expectations) [verify section]; OCC Bulletin 2026-13 §III.A control environment and §III.B model risk management policy [verify section]; FFIEC BSA/AML Examination Manual — BSA/AML Compliance Program section, expectations on written policy [verify section]; U.S. interagency third-party risk management guidance (June 2023) §III.A planning [verify section] for third-party-policy expectations; CFPB UDAAP exam manual [verify section] for consumer-facing policy expectations; NIST AI RMF 1.0 (January 2023) Govern function for AI-policy expectations.

## Source anchors

Primary:
- SR 11-7 §VI, April 4, 2011 — policy and governance expectations for model risk. Use for: MRM policy gap reviews. [verify]
- OCC Bulletin 2026-13, 2026 — refreshed model risk guidance. §III.A and §III.B for policy expectations including AI-system extensions. [verify]
- FFIEC BSA/AML Examination Manual, current edition. BSA/AML Compliance Program section (written policy expectations), Customer Due Diligence section. Use for: AML / financial-crime policy gap reviews. [verify section labels]
- U.S. interagency third-party risk management guidance, June 2023. §III.A, §III.B, §III.C, §III.D, §III.E. Use for: TPRM policy gap reviews.
- CFPB UDAAP exam manual, current edition. Use for: consumer-compliance policy gap reviews. [verify section labels]
- NIST AI RMF 1.0, January 2023. Govern function. Use for: AI-policy gap reviews where the firm has an AI policy benchmarked against AI RMF.

Secondary (overlay only):
- ISO/IEC 42001:2023 §6 (planning), §7 (support), §8 (operation). Use for: AI-management-system policy gap reviews. [verify section labels]
- DORA Articles 5–14 ICT risk management framework, when reviewing an EU ICT-policy. [verify]

## Sector overlays needed

- `banking.md` — Covers OCC heightened standards [verify] policy expectations, FRB SR letters as policy benchmark, FDIC FILs.
- `insurance.md` — Covers NAIC Model Audit Rule, ORSA policy expectations, state DOI conduct-of-business policy expectations.
- `capital-markets.md` — Covers SEC Rule 206(4)-7 (advisers compliance program) [verify section], FINRA 3110 supervisory procedures [verify], SEC Rule 38a-1 (fund compliance) where applicable.
- `payments-fintech.md` — Covers OCC fintech bank-partnership policy expectations [verify], CFPB consumer-compliance policy expectations.

## Cross-cutting overlays needed

- `cyber.md` — Required when the policy in scope is a cybersecurity policy. Anchors: NYDFS Part 500 §500.3 cybersecurity policy expectations; FFIEC IT Examination Handbook, Information Security booklet §II.A; SEC Reg S-K Item 106 [verify] for governance disclosure expectations.
- `privacy.md` — Required when the policy in scope is a privacy or data-handling policy. Anchors: GLBA Safeguards (16 CFR 314.4) [verify section], state privacy laws.
- `climate.md` — Optional, when the policy in scope is a climate-risk policy. Anchors: SEC climate disclosure rule [verify status post-2025], TCFD-aligned reporting expectations.
- `conduct.md` — Required when the policy in scope is a customer-facing policy (product approval, marketing, complaints). Anchors: CFPB UDAAP exam manual.

## Output template named sections

Top of artifact:
- Policy in scope (name, version, effective date, owner)
- Benchmark sources (named, dated, with section references)
- Scope of review (which sections of the policy were reviewed)
- Source posture and confidence label

Body — the gap matrix, one row per gap, with these named columns:
- Gap ID
- Benchmark requirement (named source with section)
- Policy text (verbatim or paraphrased with location reference)
- Gap classification (missing / partial / weak / inconsistent / outdated)
- Severity (low / moderate / high / critical) with rationale
- Recommended policy edit (declarative; what the policy should say)
- Evidence needed (what would close the gap operationally, beyond text)
- Linked obligation IDs
- Linked control IDs
- Owner (named role accountable for the policy section)

Tail of artifact:
- Coverage summary: percentage of benchmark requirements covered by the policy (with caveats)
- Out-of-scope items (benchmark items deliberately not covered, with rationale)
- Cross-policy interactions (where this policy depends on or conflicts with another firm policy)
- Recommended next steps (e.g., draft revisions, route for legal review, schedule committee approval)
- Source trace and confidence label
- Sign-off block

## Structured output fields

Wrapper object:
- `review_id`: string.
- `policy_under_review`: object. `policy_name`, `policy_version`, `effective_date`, `owner`, `policy_doc_id`.
- `benchmark_sources`: array of objects with `source_name`, `edition`, `date`, `section_references` (array of strings).
- `scope_of_review`: array of strings (policy sections reviewed).
- `gaps`: array of gap objects.
- `coverage_summary`: object. `total_benchmark_items` (integer), `covered_items` (integer), `partial_items` (integer), `missing_items` (integer).
- `out_of_scope_items`: array of objects with `item` (string), `rationale` (string).
- `cross_policy_interactions`: array of objects with `other_policy` (string), `interaction_type` (enum: `dependency`, `conflict`, `overlap`), `description` (string).
- `confidence_label`: enum.
- `human_review_required`: boolean. Always true.

Gap object (new schema, phase 2 should add as `schemas/policy-gap.schema.json`):
- `gap_id`: string.
- `benchmark_requirement`: string.
- `benchmark_source_anchor`: object. `source_name`, `section`, `date`, `url`.
- `policy_text_excerpt`: string.
- `policy_location`: string (section number or heading in the policy).
- `gap_classification`: enum (`missing`, `partial`, `weak`, `inconsistent`, `outdated`).
- `severity`: enum (`low`, `moderate`, `high`, `critical`).
- `severity_rationale`: string.
- `recommended_edit`: string.
- `evidence_needed`: array of strings.
- `linked_obligation_ids`: array of strings.
- `linked_control_ids`: array of strings.
- `owner`: string (role).

## Example scenarios

### Scenario 1: Legacy SR 11-7-aligned MRM policy benchmarked against OCC 2026-13

Input: a national bank's model risk management policy (last refreshed in 2019, anchored to SR 11-7) is being reviewed against OCC Bulletin 2026-13. Source posture is public-only (SR 11-7 plus OCC 2026-13).

Output emphasizes:
- Gap rows on AI-system extensions in OCC 2026-13 not addressed in the legacy policy: policy lacks definitions for AI systems vs. statistical models, no GenAI-specific governance, no agentic-AI control expectations.
- Severity high on AI-system extensions; rationale ties to current supervisory posture and active model-risk exam priorities.
- Recommended edit fragments are declarative: "Add a section §X defining AI systems and bringing them within the inventory and tiering scope; add GenAI-specific governance addressing prompt-injection risk."
- Coverage summary: 73 percent of OCC 2026-13 expectations covered by current policy, 18 percent partial, 9 percent missing.
- Cross-policy interactions: dependency on the firm's third-party risk policy for vendor-model handling; overlap with AI governance committee charter.

### Scenario 2: Vendor-management policy benchmarked against interagency TPRM guidance (June 2023)

Input: a regional bank's vendor-management policy (last refreshed pre-2023) is being reviewed against the U.S. interagency TPRM guidance issued June 2023.

Output emphasizes:
- Gap rows on planning-phase criticality assessment (legacy policy moves directly to due diligence), ongoing monitoring KRIs (legacy policy refers to "annual review" only), exit planning (legacy policy has no exit-plan-testing requirement), subcontractor oversight (legacy policy is silent).
- Severity high on exit planning; rationale ties to operational resilience expectations and the absence of compensating control.
- Recommended edits address each of the four lifecycle gaps with declarative wording.
- Out-of-scope items: legacy policy intentionally excludes non-ICT third parties (cleaning, catering); rationale is documented and accepted.
- Cross-policy interactions: dependency on operational-risk policy for resilience expectations, conflict with information-security policy on subcontractor due-diligence depth — flagged for resolution.

## Common pitfalls

1. Reviewing the policy against itself. Without a named, dated benchmark source with section references, the review is internal-consistency editing, not a gap review. Phase 2 must enforce a benchmark_sources list with at least one external anchor.
2. Severity without rationale. Calling a gap "high" without tying it to materiality, supervisory exposure, customer impact, or operational risk is opinion. Severity_rationale is mandatory.
3. Recommended edit that just restates the gap. "Add language on AI systems" is not a recommended edit. The recommended_edit field must be declarative and at least summary-drafted.
4. Confusing policy gap with control gap. A policy can require a control that does not exist operationally; a control can exist operationally without policy support. The evidence_needed field captures the operational dimension; phase 2 should require it on every row classified higher than `partial`.
5. Coverage percentage without the underlying counts. A coverage summary like "we cover most of the rule" is unverifiable. Coverage_summary fields require integer counts.
6. Missing cross-policy interactions. Most material gaps interact with at least one other policy (vendor policy and infosec, MRM and AI governance, BSA/AML and consumer compliance). Phase 2 should prompt for cross-policy interactions explicitly.
