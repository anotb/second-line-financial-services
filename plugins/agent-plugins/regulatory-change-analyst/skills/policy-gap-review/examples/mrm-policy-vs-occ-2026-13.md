# Example: legacy SR 11-7-aligned MRM policy benchmarked against OCC Bulletin 2026-13

## Input

A national bank's Model Risk Management Office is reviewing the firm's Model Risk Management Policy ahead of an OCC safety-and-soundness examination scheduled for the second half of 2026. The policy was last refreshed in 2019 and is anchored on SR 11-7. OCC Bulletin 2026-13, the revised interagency model risk management guidance, was published earlier in 2026 and the bank's Model Risk Committee directed the MRMO to identify gaps before the exam. Source posture is mixed: SR 11-7 and OCC Bulletin 2026-13 (public) plus the firm's MRM policy v6.1 (firm-policy overlay) and a supporting Model Validation Standard v3.0 (firm-policy overlay). Sector overlay: banking. No cross-cutting overlays loaded; this matrix is policy-on-policy and does not run cyber rows.

## Why this scenario matters

This is the canonical legacy-SR 11-7-vs-2026-13 application of the matrix. OCC Bulletin 2026-13 layers AI-system extensions onto the SR 11-7 frame: definitions for AI systems vs statistical models, GenAI-specific governance, agentic-AI control expectations, refreshed control-environment language. Policies anchored only to SR 11-7 (which describes most US banks' MRM policies) almost always carry `outdated` or `partial` rows when benchmarked against 2026-13. The example tests three things at once: the discipline of classifying gaps (`outdated` for the AI-system extensions, `partial` for the third-party-model expansions, `weak` for the legacy validation rigor), the severity rationale (supervisory exposure under an active 2026 exam cycle, the bank's published commitment to AI use), and the recommended-edit fragments at a level the policy-rewrite team can work from.

## Output sketch

```yaml
review_id: PGR-2026-MRM-04
as_of_date: 2026-05-06
engagement_id: ENG-2026-MRM-EXAM-PREP

policy_under_review:
  policy_name: "Model Risk Management Policy"
  policy_version: "v6.1"
  effective_date: 2019-09-15
  owner_role: "Head of Model Risk"
  document_identifier: "intranet:/policies/risk/mrm/v6.1"
  supporting_artefacts:
    - {artefact_name: "Model Validation Standard", artefact_version: "v3.0", owner_role: "Head of Model Validation"}

benchmark_sources:
  - {source_name: "SR 11-7 / OCC Bulletin 2011-12 — Supervisory Guidance on Model Risk Management",
     edition: "April 4, 2011",
     section_references: ["§IV development, implementation, and use", "§V validation", "§VI governance, policies, and controls"]}
  - {source_name: "OCC Bulletin 2026-13 — Revised Interagency Model Risk Management Guidance",
     edition: "2026",
     section_references: ["§III.A control environment refresh", "§III.B third-party model controls", "AI-system extensions"]}

scope_of_review:
  - {policy_section: "§2 Definitions and scope", benchmark_sources_used: ["OCC 2026-13 AI-system extensions"]}
  - {policy_section: "§3 Model lifecycle", benchmark_sources_used: ["SR 11-7 §IV", "OCC 2026-13 §III.A"]}
  - {policy_section: "§4 Validation", benchmark_sources_used: ["SR 11-7 §V"]}
  - {policy_section: "§5 Governance and roles", benchmark_sources_used: ["SR 11-7 §VI", "OCC 2026-13 §III.A"]}
  - {policy_section: "§6 Third-party models", benchmark_sources_used: ["OCC 2026-13 §III.B"]}

source_posture: mixed

gaps:
  - gap_id: GAP-001
    benchmark_requirement: "Firm policy defines AI systems and brings them within the model inventory and tiering taxonomy."
    benchmark_source_anchor: {source_name: "OCC Bulletin 2026-13", section: "AI-system extensions"}
    policy_text_excerpt: "Policy is silent. §2 definitions cover statistical and machine-learning models; AI systems and GenAI are not named."
    policy_location: "§2 Definitions and scope"
    gap_classification: outdated
    severity: high
    severity_rationale: "OCC published the revised guidance earlier in 2026; an exam under the new framing is scheduled for H2 2026. Bank has publicly disclosed AI-use in retail credit and customer service. Policy silence on AI systems is the most-probed gap site this exam cycle. No compensating practice in place; AI use is governed by an informal AI Council charter that is not policy-tier."
    recommended_edit: "Insert §2.4 defining AI systems and GenAI consistent with OCC Bulletin 2026-13 terminology; bring AI systems within the inventory in §3.1; tier by use-case impact rather than statistical complexity in §3.2."
    evidence_needed:
      - "Refresh of Model Inventory taxonomy in the GRC platform"
      - "Training session for model owners and developers on AI-system classification"
      - "Documented mapping from existing inventory to the refreshed taxonomy"
    linked_obligation_ids: [OBL-OCC-2026-13-IIIA]
    linked_control_ids: [C-MRM-INV-001]
    owner_role: "Head of Model Risk"

  - gap_id: GAP-002
    benchmark_requirement: "Firm policy addresses GenAI-specific governance: prompt-injection risk, training-data provenance, hallucination handling, agentic-AI tool-and-action boundary."
    benchmark_source_anchor: {source_name: "OCC Bulletin 2026-13", section: "AI-system extensions"}
    policy_text_excerpt: "Policy is silent on GenAI. §4 validation contemplates statistical performance metrics; no GenAI-relevant validation expectations."
    policy_location: "§3 Model lifecycle, §4 Validation"
    gap_classification: missing
    severity: high
    severity_rationale: "Bank has GenAI use in production (customer-service summarisation, internal knowledge retrieval). OCC Bulletin 2026-13 expects firm policy to address GenAI-specific risks proportionate to use-case impact. Active OCC supervisory letter from 2025 to a peer bank cited GenAI policy silence; supervisory exposure is concrete."
    recommended_edit: "Insert new §3.5 GenAI-specific governance covering: (a) training-data provenance and licensing review at intake, (b) prompt-injection and adversarial-input testing as part of validation, (c) hallucination detection and response in production, (d) agentic-AI tool-and-action boundary review where applicable. Validation Standard §3 to add GenAI-relevant testing methods."
    evidence_needed:
      - "Validation Standard refresh"
      - "GenAI-specific testing playbook"
      - "Prompt-injection red-team testing program"
      - "Updated validation report template that surfaces GenAI-specific testing"
    linked_obligation_ids: [OBL-OCC-2026-13-IIIA]
    linked_control_ids: []
    owner_role: "Head of Model Risk"

  - gap_id: GAP-003
    benchmark_requirement: "Firm policy addresses third-party model controls including vendor model documentation, validation expectations on vendor models, and ongoing monitoring of vendor-model performance."
    benchmark_source_anchor: {source_name: "OCC Bulletin 2026-13", section: "§III.B third-party model controls"}
    policy_text_excerpt: "§6 Third-party models requires that vendor models be 'validated where feasible' and references the firm's Vendor Management Policy for ongoing monitoring."
    policy_location: "§6 Third-party models"
    gap_classification: partial
    severity: moderate
    severity_rationale: "Policy addresses vendor models but at lower rigor than 2026-13 §III.B expects. 'Validated where feasible' is a hedge that 2026-13 narrows; bank's vendor-model inventory includes three Tier-1 models on the lending side. Compensating practice: firm-side reduced-form testing on vendor model outputs is documented in the Validation Standard, but reduced-form testing alone does not satisfy §III.B."
    recommended_edit: "Replace §6.2 'validated where feasible' with explicit expectations under 2026-13 §III.B: vendor-model documentation review, conceptual-soundness assessment, ongoing-performance monitoring with named KRIs, and a documented basis for any feasibility-based limitation on validation depth."
    evidence_needed:
      - "Refresh of Vendor Model Validation Standard"
      - "Per-vendor-model validation work papers reflecting the refreshed standard"
      - "Cross-policy alignment with Vendor Management Policy on monitoring KRIs"
    linked_obligation_ids: [OBL-OCC-2026-13-IIIB]
    linked_control_ids: [C-MRM-VND-002]
    owner_role: "Head of Model Risk"

  - gap_id: GAP-004
    benchmark_requirement: "Firm policy articulates the control environment refresh under 2026-13 §III.A: roles for development, validation, use, and ongoing monitoring; segregation between developer and validator; material model change management."
    benchmark_source_anchor: {source_name: "OCC Bulletin 2026-13", section: "§III.A control environment refresh"}
    policy_text_excerpt: "§5.2 names roles for development, validation, and use. Segregation between developer and validator is implicit in role definitions but not articulated. Material change management is in §3.4 but the trigger criteria are not named."
    policy_location: "§5.2 Roles, §3.4 Change management"
    gap_classification: weak
    severity: moderate
    severity_rationale: "Policy addresses the topics but at lower rigor than 2026-13 §III.A expects. Segregation expectations are implicit, not articulated; change-management triggers are unspecified. Compensating practice: MRMO operating procedures cover both, but operating procedures sit below the policy in the firm's hierarchy."
    recommended_edit: "Refresh §5.2 to articulate segregation between developer and validator as an explicit control attribute (validator is independent of development team and reports through Model Risk function). Refresh §3.4 to name change-management triggers: feature change, training-window shift, score-cutoff change, performance-breach-driven re-fit."
    evidence_needed:
      - "Updated MRMO RACI consistent with refreshed §5.2"
      - "Change-management workflow refresh in the Model Inventory"
    linked_obligation_ids: [OBL-OCC-2026-13-IIIA, OBL-SR11-7-VI]
    linked_control_ids: [C-MRM-301]
    owner_role: "Head of Model Risk"

coverage_summary:
  total_benchmark_items: 22
  covered_items: 16
  partial_items: 4
  missing_items: 1
  inconsistent_items: 0
  outdated_items: 1

out_of_scope_items:
  - item: "OCC Bulletin 2026-13 expectations on FedNow / payment-system models"
    rationale: "Bank does not operate FedNow or payment-system models within the MRM policy scope; payment-system models are governed under the Treasury and Payments operating policy with a separate review cycle."

cross_policy_interactions:
  - other_policy: "Vendor Management Policy v4.2"
    interaction_type: dependency
    description: "GAP-003 (third-party model controls) requires alignment with the Vendor Management Policy on monitoring KRIs and ongoing-performance review cadence. Co-fix needed; routing to Head of Vendor Management."
    linked_gap_ids: [GAP-003]
  - other_policy: "AI Council Charter (operating document, not policy-tier)"
    interaction_type: overlap
    description: "GAP-001 and GAP-002 partially overlap with AI Council operating document. Recommend retiring the operating document and bringing its content into the refreshed MRM policy plus a successor AI-Governance Policy at policy-tier."
    linked_gap_ids: [GAP-001, GAP-002]

recommended_next_steps:
  - "Draft revisions on §2.4 (AI definitions), §3.1-§3.2 (inventory and tiering), §3.5 (GenAI governance), §4 (Validation Standard updates), §5.2 (roles), §6.2 (third-party models) ready for legal review by 2026-06-15."
  - "Route to Compliance and Risk Committee for tabling on 2026-07."
  - "Schedule policy-owner working session with Head of Vendor Management on cross-policy alignment by 2026-06-01."
  - "Schedule training refresh on changed sections within 60 days of approval."

confidence_label: high

reviewer_questions:
  - "GAP-001 severity is rated `high` based on the published 2026-13 timing and the H2 2026 exam scope. Should severity escalate to `critical` if the exam window opens before recommended-edit approval?"
  - "GAP-002 names agentic-AI tool-and-action boundary in the recommended edit. Bank has not yet deployed agentic-AI in production. Should the policy carry the language proactively or wait for the first production agentic-AI use case?"
  - "GAP-003 references the Vendor Management Policy as a dependency. The Vendor Management Policy is itself due for refresh against the June 2023 interagency TPRM guidance; should the two refreshes be sequenced or coupled?"

human_review_required: true

revisions:
  - {date: 2026-05-06, reason: "initial review", delta: "created during MRM exam-prep engagement", approved_by: "Head of Model Risk"}
```

## What the matrix surfaces

- The `outdated` classification fires once (GAP-001 — AI-system definitions). The `missing` classification fires once (GAP-002 — GenAI-specific governance). The `partial` classification fires twice (GAP-003 — third-party models; GAP-004 — control-environment articulation). The matrix discipline distinguishes the four classifications rather than collapsing them.
- Severity rationale on each row references supervisory exposure (active 2026 exam cycle, peer-bank supervisory letter on GenAI), materiality (bank's published AI use, three Tier-1 vendor models), and compensating practice (informal AI Council charter, firm-side reduced-form testing). Severity is paired with rationale, not asserted.
- Coverage summary is integer counts. The matrix does not assert "we cover most of 2026-13"; it carries 16 covered, 4 partial, 1 missing, 1 outdated against 22 in-scope benchmark items.
- Cross-policy interactions are surfaced explicitly. The Vendor Management Policy interaction creates a dependency that the recommended-next-steps block routes to the head of vendor management. The AI Council operating document overlap creates a recommendation to retire the operating document and elevate its content to policy-tier.
- Recommended edits are declarative and at summary-draft level. They name the policy section, the change, and what the changed text accomplishes; they are not just "add language on AI."

## Downstream uses

- `issue-writeup` consumes GAP-001 and GAP-002 as findings to be papered with severity, owner, and target date for the firm's issue log; the supervisory exposure rationale carries directly into the severity_rationale field of the issue write-up.
- `obligation-mapping` consumes GAP-001 and GAP-002 to confirm OBL-OCC-2026-13-IIIA covers AI-system extensions; if the obligation register did not yet carry the AI-system rows, the obligation register reopens.
- `control-matrix` consumes GAP-003 and GAP-004 against C-MRM-VND-002 and C-MRM-301; the operating-effectiveness rating on those rows is re-tested in light of the policy fix.
- `evidence-binder` consumes the `evidence_needed` arrays to scope the evidence pack the next exam will inspect.
- The downstream `regulatory-change-management/policy-diff` skill (when the rewrite ships) compares v6.1 to v6.2 and confirms the recommended edits landed; the gap matrix sets the v6.2 acceptance criteria.
