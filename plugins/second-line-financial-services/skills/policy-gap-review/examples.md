# Examples and troubleshooting

One section per worked example, then troubleshooting. Read only what you need.

## mrm-policy-vs-occ-2026-13

### Example: legacy SR 11-7-aligned MRM policy benchmarked against the April 2026 joint guidance

#### Input

A national bank's Model Risk Management Office is reviewing the firm's Model Risk Management Policy ahead of an OCC safety-and-soundness examination scheduled for the second half of 2026. The policy was last refreshed in 2019 and is anchored on SR 11-7. The Joint Interagency Revised Guidance on Model Risk Management (OCC Bulletin 2026-13 / FRB SR 26-2 / FDIC FIL-15-2026, April 17, 2026) was published earlier in 2026 and the bank's Model Risk Committee directed the MRMO to identify gaps before the exam. The bank holds total assets above $30 billion, so the joint guidance is supervisor-relevant. Source posture is mixed: SR 11-7 and the April 2026 joint guidance (public) plus the firm's MRM policy v6.1 (firm-policy overlay) and a supporting Model Validation Standard v3.0 (firm-policy overlay). Sector overlay: banking. No cross-cutting overlays loaded; this matrix is policy-on-policy and does not run cyber rows.

The bank also has GenAI in production (customer-service summarisation, internal knowledge retrieval) and is piloting agentic-AI use cases in operations. GenAI and agentic-AI governance are explicitly out of scope of the April 2026 joint guidance (footnote 3); the gap matrix treats them as a separate workstream and does not benchmark MRM-policy sections against the bulletin for those uses. The Head of Model Risk has commissioned a parallel AI-policy gap review against NIST AI RMF 1.0, NIST AI 600-1, and the firm's draft AI Governance Framework; that review is referenced in this matrix's cross-policy-interactions section but is not this matrix's subject.

#### Why this scenario matters

This is the canonical legacy-SR 11-7-vs-April-2026-joint-guidance application of the matrix for traditional models. The April 2026 joint guidance refreshes the SR 11-7 frame for traditional statistical and quantitative models and non-generative, non-agentic AI models; it also explicitly excludes GenAI and agentic AI from scope. Policies anchored only to SR 11-7 (which describes most US banks' MRM policies) typically carry `outdated` or `partial` rows when benchmarked against the April 2026 refresh on the traditional-model side. The example tests three things at once: the discipline of classifying gaps for traditional-model coverage, the severity rationale (supervisory exposure under an active 2026 exam cycle, the bank's scale above the $30 billion supervisory-relevance threshold), and the recommended-edit fragments at a level the policy-rewrite team can work from. The example also shows the discipline of routing GenAI / agentic-AI policy gaps to a separate workstream rather than collapsing them into the joint-guidance matrix.

#### Output sketch

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
     edition: "April 4, 2011 (superseded April 17, 2026)",
     section_references: ["§IV development, implementation, and use", "§V validation", "§VI governance, policies, and controls"]}
  - {source_name: "Joint Interagency Revised Guidance on Model Risk Management — OCC Bulletin 2026-13 / FRB SR 26-2 / FDIC FIL-15-2026",
     edition: "April 17, 2026",
     section_references: ["Section II (scope and definitions)", "Section III (control environment, third-party model controls)"]}

scope_of_review:
  - {policy_section: "§2 Definitions and scope", benchmark_sources_used: ["April 2026 joint guidance Section II"]}
  - {policy_section: "§3 Model lifecycle", benchmark_sources_used: ["SR 11-7 §IV", "April 2026 joint guidance Section III"]}
  - {policy_section: "§4 Validation", benchmark_sources_used: ["SR 11-7 §V"]}
  - {policy_section: "§5 Governance and roles", benchmark_sources_used: ["SR 11-7 §VI", "April 2026 joint guidance Section III"]}
  - {policy_section: "§6 Third-party models", benchmark_sources_used: ["April 2026 joint guidance Section III"]}

source_posture: mixed

gaps:
  - gap_id: GAP-001
    benchmark_requirement: "Firm policy reflects the April 2026 refreshed model definition and scope (statistical / quantitative models and non-generative, non-agentic AI models in scope; simple arithmetic / spreadsheet calculations, deterministic rule-based processes, GenAI and agentic AI explicitly out of scope)."
    benchmark_source_anchor: {source_name: "OCC Bulletin 2026-13 / FRB SR 26-2 / FDIC FIL-15-2026", section: "Section II (scope and definitions)"}
    policy_text_excerpt: "§2 definitions cover statistical and machine-learning models; the definition predates the April 2026 refresh and does not articulate the inclusion of non-generative, non-agentic AI models or the explicit exclusion of GenAI and agentic AI from this policy's scope."
    policy_location: "§2 Definitions and scope"
    gap_classification: outdated
    severity: high
    severity_rationale: "Joint guidance was published April 17, 2026; an exam under the refreshed framing is scheduled for H2 2026. Bank holds assets above $30 billion (the joint guidance's supervisory-relevance threshold). The model definition in §2 has not been refreshed since 2019. No compensating practice in place. Distinguishing the in-scope traditional / non-generative-AI population from the out-of-scope GenAI / agentic-AI population in the policy itself is the cleanest way to avoid a supervisory finding that the firm's MRM policy is silent on the post-2026 frame."
    recommended_edit: "Refresh §2 with the joint guidance's model definition; articulate the inclusion of non-generative, non-agentic AI models within the model inventory; articulate the exclusion of GenAI and agentic AI from this policy and reference the firm's separate AI Governance Framework as the controlling policy for those uses; preserve the spreadsheet / deterministic-rule exclusions consistent with the joint guidance."
    evidence_needed:
      - "Refresh of Model Inventory taxonomy in the GRC platform to reflect refreshed definition"
      - "Training session for model owners on refreshed scope"
      - "Cross-reference between MRM policy and AI Governance Framework so the boundary between the two is unambiguous"
    linked_obligation_ids: [OBL-MRM-2026-DEF]
    linked_control_ids: [C-MRM-INV-001]
    owner_role: "Head of Model Risk"

  - gap_id: GAP-002
    benchmark_requirement: "Firm policy articulates the control environment refresh in Section III: roles for development, validation, use, and ongoing monitoring; segregation between developer and validator; material model change management triggers."
    benchmark_source_anchor: {source_name: "OCC Bulletin 2026-13 / FRB SR 26-2 / FDIC FIL-15-2026", section: "Section III (control environment)"}
    policy_text_excerpt: "§5.2 names roles for development, validation, and use. Segregation between developer and validator is implicit in role definitions but not articulated. Material change management is in §3.4 but the trigger criteria are not named."
    policy_location: "§5.2 Roles, §3.4 Change management"
    gap_classification: weak
    severity: moderate
    severity_rationale: "Policy addresses the topics but at lower rigor than Section III expects. Segregation expectations are implicit rather than articulated; change-management triggers are unspecified. Compensating practice: MRMO operating procedures cover both, but operating procedures sit below the policy in the firm's hierarchy."
    recommended_edit: "Refresh §5.2 to articulate segregation between developer and validator as an explicit control attribute (validator is independent of development team and reports through the Model Risk function). Refresh §3.4 to name change-management triggers: feature change, training-window shift, score-cutoff change, performance-breach-driven re-fit."
    evidence_needed:
      - "Updated MRMO RACI consistent with refreshed §5.2"
      - "Change-management workflow refresh in the Model Inventory"
    linked_obligation_ids: [OBL-MRM-2026-CTRL, OBL-SR11-7-VI]
    linked_control_ids: [C-MRM-301]
    owner_role: "Head of Model Risk"

  - gap_id: GAP-003
    benchmark_requirement: "Firm policy addresses third-party model controls including vendor model documentation, validation expectations on vendor models, and ongoing monitoring of vendor-model performance."
    benchmark_source_anchor: {source_name: "OCC Bulletin 2026-13 / FRB SR 26-2 / FDIC FIL-15-2026", section: "Section III (third-party model controls)"}
    policy_text_excerpt: "§6 Third-party models requires that vendor models be 'validated where feasible' and references the firm's Vendor Management Policy for ongoing monitoring."
    policy_location: "§6 Third-party models"
    gap_classification: partial
    severity: moderate
    severity_rationale: "Policy addresses vendor models but at lower rigor than the joint guidance's Section III expects. 'Validated where feasible' is a hedge that the joint guidance narrows; bank's vendor-model inventory includes three Tier-1 models on the lending side. Compensating practice: firm-side reduced-form testing on vendor model outputs is documented in the Validation Standard, but reduced-form testing alone does not satisfy the joint guidance's third-party-model expectations."
    recommended_edit: "Replace §6.2 'validated where feasible' with explicit expectations under the joint guidance's third-party-model controls: vendor-model documentation review, conceptual-soundness assessment, ongoing-performance monitoring with named KRIs, and a documented basis for any feasibility-based limitation on validation depth."
    evidence_needed:
      - "Refresh of Vendor Model Validation Standard"
      - "Per-vendor-model validation work papers reflecting the refreshed standard"
      - "Cross-policy alignment with Vendor Management Policy on monitoring KRIs"
    linked_obligation_ids: [OBL-MRM-2026-3P]
    linked_control_ids: [C-MRM-VND-002]
    owner_role: "Head of Model Risk"

  - gap_id: GAP-004
    benchmark_requirement: "Firm policy reflects the joint guidance's documentation expectations for the model-validation evidence pack at the supervisory-relevance threshold."
    benchmark_source_anchor: {source_name: "OCC Bulletin 2026-13 / FRB SR 26-2 / FDIC FIL-15-2026", section: "Section III (documentation expectations)"}
    policy_text_excerpt: "§4 Validation references SR 11-7 §V categories (conceptual soundness, ongoing monitoring, outcomes analysis, benchmarking) but does not reflect the documentation expectations articulated in the April 2026 refresh."
    policy_location: "§4 Validation, §4.6 Documentation expectations"
    gap_classification: outdated
    severity: moderate
    severity_rationale: "Policy reflects the prior framing. The joint guidance is non-binding (does not set forth enforceable standards), but supervisory examination teams have signalled they will read against the refreshed framing. Compensating practice: validation reports on Tier-1 models already reflect a richer documentation discipline than §4 prescribes."
    recommended_edit: "Refresh §4.6 to incorporate the joint guidance's documentation expectations for validation packs and tie them to the firm's Validation Standard so the actual evidence pack discipline is reflected at policy-tier."
    evidence_needed:
      - "Refresh of Model Validation Standard documentation section"
      - "Updated validation report template that surfaces the refreshed documentation expectations"
    linked_obligation_ids: [OBL-MRM-2026-DOC]
    linked_control_ids: [C-MRM-VAL-DOC-001]
    owner_role: "Head of Model Risk"

coverage_summary:
  total_benchmark_items: 22
  covered_items: 18
  partial_items: 1
  missing_items: 0
  inconsistent_items: 0
  outdated_items: 3

out_of_scope_items:
  - item: "Generative AI and agentic AI model governance"
    rationale: "Footnote 3 of the joint April 2026 guidance excludes GenAI and agentic AI from scope. GenAI and agentic-AI policy gaps are addressed in a separate workstream benchmarking the firm's draft AI Governance Framework against NIST AI RMF 1.0, NIST AI 600-1 (Generative AI Profile), and ISO/IEC 42001. Cross-referenced under cross-policy interactions."
  - item: "Bank Secrecy Act / Anti-Money Laundering model risk (formerly SR 21-8)"
    rationale: "SR 21-8 was superseded by the April 2026 joint guidance. The BSA/AML model population is covered by this matrix to the extent BSA/AML models are traditional statistical or quantitative models; BSA/AML-specific exam manual provisions remain a separate benchmark for sanctions-screening model tuning evidence and are addressed in the BSA/AML model-monitoring matrix."

cross_policy_interactions:
  - other_policy: "Vendor Management Policy v4.2"
    interaction_type: dependency
    description: "GAP-003 (third-party model controls) requires alignment with the Vendor Management Policy on monitoring KRIs and ongoing-performance review cadence. Co-fix needed; routing to Head of Vendor Management."
    linked_gap_ids: [GAP-003]
  - other_policy: "AI Governance Framework (draft, separate workstream)"
    interaction_type: dependency
    description: "GAP-001 names the boundary between MRM-policy scope (traditional / non-generative, non-agentic models) and AI Governance Framework scope (GenAI and agentic AI). The AI Governance Framework is being benchmarked separately against NIST AI RMF 1.0, NIST AI 600-1, and ISO/IEC 42001. Both refreshes need to land together so the boundary is unambiguous."
    linked_gap_ids: [GAP-001]

recommended_next_steps:
  - "Draft revisions on §2 (definitions and scope), §3.4 (change management), §4.6 (documentation), §5.2 (roles), §6.2 (third-party models) ready for legal review by 2026-06-15."
  - "Route to Compliance and Risk Committee for tabling on 2026-07."
  - "Schedule policy-owner working session with Head of Vendor Management on cross-policy alignment by 2026-06-01."
  - "Coordinate sequencing with the AI Governance Framework gap review so the MRM-policy / AI-policy boundary lands cleanly."
  - "Schedule training refresh on changed sections within 60 days of approval."

confidence_label: high

reviewer_questions:
  - "GAP-001 severity is rated `high` based on the published April 2026 timing and the H2 2026 exam scope. Should severity escalate to `critical` if the exam window opens before recommended-edit approval?"
  - "GAP-001's recommended edit references the firm's separate AI Governance Framework as the controlling policy for GenAI and agentic AI. The AI Governance Framework is currently in draft and not yet board-approved. Should the MRM-policy refresh wait, or should §2 carry a pointer to 'AI Governance Framework or its successor' for now?"
  - "GAP-003 references the Vendor Management Policy as a dependency. The Vendor Management Policy is itself due for refresh against the June 2023 interagency TPRM guidance; should the two refreshes be sequenced or coupled?"

human_review_required: true

revisions:
  - {date: 2026-05-06, reason: "initial review", delta: "created during MRM exam-prep engagement", approved_by: "Head of Model Risk"}
```

#### What the matrix surfaces

- The `outdated` classification fires twice (GAP-001 — refreshed model definition and scope; GAP-004 — documentation expectations). The `weak` classification fires once (GAP-002 — articulation of segregation and change-management triggers). The `partial` classification fires once (GAP-003 — third-party models). The matrix discipline distinguishes the classifications rather than collapsing them.
- Severity rationale on each row references supervisory exposure (active H2 2026 exam cycle; supervisory-relevance threshold met at $30B), materiality (three Tier-1 vendor models, validation evidence on Tier-1 models), and compensating practice (operating procedures, firm-side reduced-form testing). Severity is paired with rationale, not asserted.
- Coverage summary is integer counts. The matrix does not assert "we cover most of the joint guidance"; it carries 18 covered, 1 partial, 0 missing, 2 outdated, 0 inconsistent against 22 in-scope benchmark items.
- Out-of-scope items name the GenAI / agentic-AI exclusion explicitly (per footnote 3) and route those gaps to a separate AI Governance Framework workstream. The matrix does not benchmark the MRM policy against the joint guidance for GenAI or agentic-AI uses; doing so would misrepresent the bulletin's scope.
- Cross-policy interactions are surfaced explicitly. The Vendor Management Policy interaction creates a dependency that the recommended-next-steps block routes to the head of vendor management. The AI Governance Framework dependency makes the MRM-policy / AI-policy boundary visible.
- Recommended edits are declarative and at summary-draft level. They name the policy section, the change, and what the changed text accomplishes.

#### Downstream uses

- `issue-writeup` consumes GAP-001, GAP-002, and GAP-004 as findings to be papered with severity, owner, and target date for the firm's issue log; the supervisory exposure rationale carries directly into the severity_rationale field of the issue write-up.
- `obligation-mapping` consumes the gap rows whose `linked_obligation_ids` reference the April 2026 joint guidance to confirm the obligation register carries the refreshed-scope rows; if not, the obligation register reopens.
- `control-matrix` consumes GAP-002 and GAP-003 against C-MRM-301 and C-MRM-VND-002; the operating-effectiveness rating on those rows is re-tested in light of the policy fix.
- `evidence-binder` consumes the `evidence_needed` arrays to scope the evidence pack the next exam will inspect.
- The AI Governance Framework gap review (separate workstream) consumes the cross-policy-interactions row that names the MRM-policy / AI-policy boundary.
- The downstream `policy-diff` skill (when the rewrite ships) compares v6.1 to v6.2 and confirms the recommended edits landed; the gap matrix sets the v6.2 acceptance criteria.

## vendor-policy-vs-2023-tprm

### Example: pre-2023 vendor-management policy benchmarked against the June 2023 interagency TPRM guidance

#### Input

A $40B regional bank's Third-Party Risk Management Office is reviewing the firm's Vendor Management Policy ahead of the FRB's planned safety-and-soundness examination of operational resilience. The policy was last refreshed in 2021 and was anchored on the legacy OCC Bulletin 2013-29. The June 2023 interagency third-party risk management guidance (jointly issued by OCC, FRB, and FDIC) replaced 2013-29 and the bank's TPRMO has been operating against the 2023 guidance informally; the policy refresh has been on the backlog for 18 months. Source posture is mixed: the June 2023 interagency guidance (public) plus the firm's Vendor Management Policy v3.4 (firm-policy overlay) and a supporting Vendor Lifecycle Standard v2.1 (firm-policy overlay). Sector overlay: banking. Cross-cutting overlay: cyber (the policy includes a §7 information-security section that benchmarks against NYDFS Part 500 §500.11 for the bank's NYDFS-licensed entities and against the cyber overlay's third-party-cyber expectations).

#### Why this scenario matters

This is the canonical pre-2023-vs-2023 vendor-policy refresh. The June 2023 guidance reorganised the third-party lifecycle into five named phases (planning, due diligence and selection, contract negotiation, ongoing monitoring, termination), introduced explicit subcontractor-oversight expectations, and reframed exit planning from a periodic exercise to a tested capability. Policies anchored on 2013-29 typically miss four lifecycle dimensions: planning-phase criticality assessment as a discrete step (legacy policies move directly to due-diligence), ongoing-monitoring KRIs (legacy policies refer to "annual review" only), exit planning with periodic testing (legacy policies have no exit-plan-testing requirement), and subcontractor oversight (legacy policies are typically silent). The example tests gap classifications across the four dimensions and the cross-policy interaction with the bank's information-security policy on subcontractor cyber depth.

#### Output sketch

```yaml
review_id: PGR-2026-TPRM-02
as_of_date: 2026-05-06
engagement_id: ENG-2026-OPRES-EXAM-PREP

policy_under_review:
  policy_name: "Vendor Management Policy"
  policy_version: "v3.4"
  effective_date: 2021-11-04
  owner_role: "Head of Vendor Management"
  document_identifier: "intranet:/policies/risk/vmp/v3.4"
  supporting_artefacts:
    - {artefact_name: "Vendor Lifecycle Standard", artefact_version: "v2.1", owner_role: "Head of Vendor Management"}

benchmark_sources:
  - {source_name: "Interagency Guidance on Third-Party Relationships: Risk Management",
     edition: "June 6, 2023",
     section_references: ["§III.A planning", "§III.B due diligence and selection", "§III.C contract negotiation", "§III.D ongoing monitoring", "§III.E termination"]}
  - {source_name: "OCC Bulletin 2014-39 — Risk Governance for Banks",
     edition: "2014",
     section_references: ["governance expectations on third-party risk under heightened standards"]}

scope_of_review:
  - {policy_section: "§2 Definitions and scope", benchmark_sources_used: ["June 2023 guidance §III.A"]}
  - {policy_section: "§3 Vendor lifecycle", benchmark_sources_used: ["June 2023 guidance §III.A through §III.E"]}
  - {policy_section: "§4 Criticality and risk tiering", benchmark_sources_used: ["June 2023 guidance §III.A"]}
  - {policy_section: "§5 Due diligence", benchmark_sources_used: ["June 2023 guidance §III.B"]}
  - {policy_section: "§6 Contracts", benchmark_sources_used: ["June 2023 guidance §III.C"]}
  - {policy_section: "§7 Information security and cyber", benchmark_sources_used: ["June 2023 guidance §III.B/§III.D", "NYDFS §500.11", "cyber overlay"]}
  - {policy_section: "§8 Ongoing monitoring", benchmark_sources_used: ["June 2023 guidance §III.D"]}
  - {policy_section: "§9 Termination and exit", benchmark_sources_used: ["June 2023 guidance §III.E"]}

source_posture: mixed

gaps:
  - gap_id: GAP-001
    benchmark_requirement: "Firm policy treats planning-phase criticality assessment as a discrete lifecycle step preceding due diligence."
    benchmark_source_anchor: {source_name: "Interagency Guidance June 2023", section: "§III.A planning"}
    policy_text_excerpt: "§3 Vendor lifecycle moves from 'engagement initiation' directly to 'due diligence'. §4 Criticality and risk tiering applies criticality scoring after due diligence completes."
    policy_location: "§3 Vendor lifecycle, §4 Criticality and risk tiering"
    gap_classification: partial
    severity: moderate
    severity_rationale: "Policy addresses criticality but in the wrong lifecycle position. June 2023 guidance §III.A expects criticality and risk-tiering to drive due-diligence depth; running tiering after due diligence inverts the expected flow. Compensating practice: TPRMO operating procedures already follow the June 2023 sequencing informally; the gap is policy-text rather than operational."
    recommended_edit: "Restructure §3 to introduce a §3.1 'Planning' step covering: (a) initial criticality assessment based on activity description, (b) preliminary risk tiering, (c) due-diligence scope determination based on tiering. Move existing §4 content into the planning step."
    evidence_needed:
      - "Refresh of Vendor Lifecycle Standard to mirror the policy structure"
      - "Refresh of GRC platform workflow sequencing"
      - "Training of vendor risk analysts on the planning-step framing"
    linked_obligation_ids: [OBL-TPRM-2023-IIIA]
    linked_control_ids: [C-VND-001]
    owner_role: "Head of Vendor Management"

  - gap_id: GAP-002
    benchmark_requirement: "Firm policy specifies named ongoing-monitoring KRIs and a documented review cadence proportionate to vendor criticality."
    benchmark_source_anchor: {source_name: "Interagency Guidance June 2023", section: "§III.D ongoing monitoring"}
    policy_text_excerpt: "§8 Ongoing monitoring requires 'annual review' for all vendors. KRIs are not named; cadence does not vary by criticality."
    policy_location: "§8 Ongoing monitoring"
    gap_classification: weak
    severity: high
    severity_rationale: "Policy addresses monitoring but at lower rigor than §III.D expects. Annual-review-only is the legacy 2013-29 framing; June 2023 guidance expects KRIs aligned to vendor criticality and a documented cadence varying by tier. Bank has 14 critical vendors and 9 of them have not had a sub-annual touchpoint in the last 12 months. Supervisory exposure on operational-resilience exam is concrete."
    recommended_edit: "Rewrite §8 to specify: (a) named ongoing-monitoring KRIs (financial health, performance SLAs, security posture, change events, complaint volume, sub-service-provider changes), (b) cadence varying by tier (critical: quarterly; high: semi-annual; moderate and low: annual), (c) escalation triggers when KRIs breach defined thresholds, (d) documented evidence of monitoring in the GRC platform."
    evidence_needed:
      - "KRI definitions and threshold framework"
      - "GRC platform configuration to track tier-specific cadence"
      - "Updated monitoring-evidence templates"
      - "Backfill of sub-annual touchpoints on critical vendors as interim mitigation"
    linked_obligation_ids: [OBL-TPRM-2023-IIID]
    linked_control_ids: [C-VND-008]
    owner_role: "Head of Vendor Management"

  - gap_id: GAP-003
    benchmark_requirement: "Firm policy requires exit planning with periodic testing for critical vendor relationships."
    benchmark_source_anchor: {source_name: "Interagency Guidance June 2023", section: "§III.E termination"}
    policy_text_excerpt: "Policy is silent on exit planning. §9 Termination and exit covers contractual termination clauses but does not require exit-plan documentation or testing."
    policy_location: "§9 Termination and exit"
    gap_classification: missing
    severity: high
    severity_rationale: "Operational-resilience expectations across multiple supervisor surfaces (FRB, OCC, FDIC under June 2023 guidance; UK PRA / EBA equivalents for the bank's London branch) treat exit planning as a foundational operational-resilience capability. The bank's three most-critical fintech-platform vendors have no documented exit plan; under stress, the bank would be reliant on contract termination clauses without an inventory of resumption alternatives. The FRB exam scope explicitly references operational resilience."
    recommended_edit: "Insert §9.2 Exit planning requiring: (a) documented exit plan for every critical vendor relationship covering trigger events, alternative-provider inventory, data-portability assessment, and customer-impact assessment; (b) periodic exit-plan testing on a documented cadence (typically annual for critical vendors); (c) board reporting on exit-plan readiness."
    evidence_needed:
      - "Exit-plan template"
      - "Exit plans for the 14 critical vendors"
      - "Annual exit-plan testing program design"
      - "Board reporting on exit-plan readiness"
      - "Cross-functional working session with Operational Resilience team and Business Continuity team"
    linked_obligation_ids: [OBL-TPRM-2023-IIIE]
    linked_control_ids: []
    owner_role: "Head of Vendor Management"

  - gap_id: GAP-004
    benchmark_requirement: "Firm policy addresses subcontractor oversight including identification of material subcontractors and risk-based depth of subcontractor due diligence."
    benchmark_source_anchor: {source_name: "Interagency Guidance June 2023", section: "§III.B due diligence and §III.D ongoing monitoring"}
    policy_text_excerpt: "Policy is silent on subcontractor oversight. §5 Due diligence and §8 Ongoing monitoring focus on the direct vendor; subcontractors are referenced once in §6 Contracts (notice-of-subcontracting clause) without due-diligence expectations."
    policy_location: "§5 Due diligence, §8 Ongoing monitoring"
    gap_classification: missing
    severity: high
    severity_rationale: "June 2023 guidance is explicit that institutions retain accountability for the activities performed by subcontractors. Bank uses cloud-hosted SaaS for several critical functions where the SaaS provider's hosting subcontractor is itself a material concentration risk. Subcontractor invisibility is a frequent enforcement trigger on operational-resilience and information-security findings. Cross-policy interaction with §7 Information security and cyber section is direct."
    recommended_edit: "Insert §5.4 Subcontractor due diligence requiring: (a) identification of material subcontractors at intake, (b) risk-based due-diligence depth on subcontractors based on criticality and information access, (c) ongoing monitoring of material subcontractor changes, (d) contract-level requirements for subcontractor disclosure and change notice. Cross-reference to Information Security Policy §4.2 for subcontractor cyber depth."
    evidence_needed:
      - "Material-subcontractor identification across the existing vendor portfolio"
      - "Refresh of due-diligence work-paper template to capture subcontractor due diligence"
      - "Updated contract template clauses on subcontractor disclosure and change notice"
      - "Cross-policy alignment with Information Security Policy on subcontractor cyber expectations"
    linked_obligation_ids: [OBL-TPRM-2023-IIIB, OBL-TPRM-2023-IIID]
    linked_control_ids: []
    owner_role: "Head of Vendor Management"

  - gap_id: GAP-005
    benchmark_requirement: "Firm cybersecurity expectations on third-party service providers (NYDFS §500.11 equivalent for non-NYDFS entities) are addressed at the rigor the cyber overlay expects."
    benchmark_source_anchor: {source_name: "23 NYCRR Part 500 (post-November 2023 amendment)", section: "§500.11 third-party service-provider security policy"}
    policy_text_excerpt: "§7 Information security and cyber requires vendors to 'maintain reasonable cybersecurity controls' and references the firm's Information Security Policy. §500.11 content elements (encryption, MFA, notice of cybersecurity events, due-diligence framework on cyber posture) are not directly addressed."
    policy_location: "§7 Information security and cyber"
    gap_classification: partial
    severity: moderate
    severity_rationale: "Policy addresses third-party cyber but at lower rigor than NYDFS §500.11 expects (and parallel expectations under FFIEC IT Handbook Information Security booklet for the bank's non-NYDFS entities). Information Security Policy §4 covers the cyber expectations in more detail, so cross-policy compensation exists; the gap is the cross-reference precision and the contract-clause linkage."
    recommended_edit: "Refresh §7 to: (a) cross-reference Information Security Policy §4.2 explicitly for third-party cyber depth; (b) require contract clauses on encryption, MFA on accounts accessing nonpublic information, cyber-incident notice within named timing (24-72 hours), and the due-diligence framework on cyber posture; (c) clarify that for NYDFS-licensed entities, §500.11 governs and Information Security Policy §4.2 implements it."
    evidence_needed:
      - "Cross-policy alignment with Information Security Policy §4.2"
      - "Contract template refresh on cyber-incident notice timing"
      - "Per-vendor inventory of contract compliance with refreshed cyber clauses"
    linked_obligation_ids: [OBL-NYDFS-500.11, OBL-TPRM-2023-IIIB]
    linked_control_ids: [C-VND-CYBER-001]
    owner_role: "Head of Vendor Management"
    row_confidence: high

coverage_summary:
  total_benchmark_items: 31
  covered_items: 22
  partial_items: 4
  missing_items: 3
  inconsistent_items: 1
  outdated_items: 1

out_of_scope_items:
  - item: "Non-ICT third parties (cleaning, catering, building services)"
    rationale: "Legacy policy intentionally excludes non-ICT third parties from the vendor-management framework. Documented in §2.1 of the policy and accepted by the firm's Operational Risk Committee in 2018; the June 2023 guidance does not mandate inclusion."

cross_policy_interactions:
  - other_policy: "Information Security Policy v5.2"
    interaction_type: dependency
    description: "GAP-004 and GAP-005 both depend on alignment with Information Security Policy §4.2 on subcontractor and third-party cyber expectations. Co-fix needed."
    linked_gap_ids: [GAP-004, GAP-005]
  - other_policy: "Information Security Policy v5.2"
    interaction_type: conflict
    description: "Information Security Policy §4.2 expects subcontractor due-diligence depth at a rigor that the Vendor Management Policy §5 does not provide for. The two policies disagree on subcontractor scoping. Resolution required at the level of policy ownership."
    linked_gap_ids: [GAP-004]
  - other_policy: "Operational Resilience Policy v1.3"
    interaction_type: dependency
    description: "GAP-003 (exit planning) requires alignment with the Operational Resilience Policy framework on critical operations and impact tolerances."
    linked_gap_ids: [GAP-003]
  - other_policy: "Business Continuity and Disaster Recovery Standard v2.0"
    interaction_type: overlap
    description: "GAP-003 (exit planning) overlaps with the BCDR Standard on critical-vendor scenario testing. Recommend coordinated test design rather than parallel testing programs."
    linked_gap_ids: [GAP-003]

recommended_next_steps:
  - "Draft revisions on §3 (lifecycle restructure), §5.4 (subcontractor due diligence), §7 (cyber alignment), §8 (ongoing-monitoring KRIs and cadence), §9.2 (exit planning) ready for legal review by 2026-06-30."
  - "Convene cross-policy working session with Head of Information Security, Head of Operational Resilience, and Head of Business Continuity by 2026-06-15 to resolve GAP-004 conflict and GAP-003 overlap."
  - "Backfill sub-annual touchpoints on the 14 critical vendors as interim mitigation pending §8 refresh; deadline 2026-07-31."
  - "Route to Risk Committee for tabling on 2026-08."
  - "Schedule training refresh for vendor risk analysts and vendor relationship managers within 60 days of approval."

confidence_label: high

reviewer_questions:
  - "GAP-002 severity is rated `high` partly because 9 critical vendors have not had a sub-annual touchpoint. If the interim backfill completes before exam fieldwork, does severity reduce to `moderate`?"
  - "GAP-003 (exit planning) names exit-plan testing as a benchmark expectation. The firm's Operational Resilience Policy is itself due for a refresh; should exit-plan testing live in the Vendor Management Policy or in the Operational Resilience Policy? The reviewer questions hand to the cross-policy working session."
  - "GAP-004 names a conflict with the Information Security Policy on subcontractor scoping. Which policy governs at the seam, and which is the operating policy that defers? The Compliance Committee tabling should resolve."
  - "GAP-005 row confidence is rated high because the cross-policy compensation in Information Security Policy §4.2 is verifiable. If the Information Security Policy is itself in scope of a separate refresh, does the matrix re-test?"

human_review_required: true

revisions:
  - {date: 2026-05-06, reason: "initial review", delta: "created during operational-resilience exam-prep engagement", approved_by: "Head of Vendor Management"}
```

#### What the matrix surfaces

- The four lifecycle gap dimensions land cleanly: GAP-001 (planning) as `partial`, GAP-002 (ongoing monitoring) as `weak`, GAP-003 (exit planning) as `missing`, GAP-004 (subcontractor oversight) as `missing`. The classifications are not interchangeable; the matrix shows the discipline of picking the right one.
- Severity rationale on GAP-002 references the operational fact (9 of 14 critical vendors without sub-annual touchpoints) and pairs it with the supervisory exposure (operational-resilience exam scope). This is the kind of pairing that survives reviewer challenge.
- Cross-policy interactions are extensive (four other policies named, two linked-gap-ids cross-references). The matrix surfaces the dependencies and the one explicit conflict (GAP-004 with the Information Security Policy on subcontractor scoping). A vendor-policy refresh that ignored these interactions would create downstream inconsistency.
- Out-of-scope rationale is documented (non-ICT third parties, accepted by the Operational Risk Committee in 2018). This is the audit-defence artefact the matrix exists to surface.
- Coverage summary integer counts: 22 covered, 4 partial, 3 missing, 1 inconsistent, 1 outdated against 31 in-scope benchmark items. The matrix does not assert "we cover most of the rule" without the underlying counts.

#### Downstream uses

- `issue-writeup` consumes GAP-002 (ongoing monitoring), GAP-003 (exit planning), and GAP-004 (subcontractor oversight) as findings to be papered into the firm's issue log; the operational-fact severity rationale carries directly into the CCCE structure.
- `obligation-mapping` confirms the obligation register carries OBL-TPRM-2023-IIIA through OBL-TPRM-2023-IIIE; if any are missing, the register reopens.
- `control-matrix` re-tests C-VND-001, C-VND-008, and C-VND-CYBER-001 in light of the policy fix; the operating-effectiveness ratings adjust for the refreshed policy text.
- `evidence-binder` consumes the `evidence_needed` arrays to scope the evidence pack the next operational-resilience exam will inspect, especially the exit-plan testing program and the material-subcontractor inventory.
- The cross-policy interactions feed parallel reviews of the Information Security Policy and the Operational Resilience Policy; both are scheduled for refresh and the gap matrix's interaction notes set the cross-policy working-session agenda.

## troubleshooting

### Troubleshooting: policy-gap-review

Recurring failure modes when a policy gap matrix looks complete but is not. The reviewer review should catch these; the builder review should preempt them.

#### 1. The matrix has no external benchmark

Symptom: the matrix is full of gap rows, but the benchmark sources block is empty or names only the firm's own policies and standards.

Why it happens: the scope did not pin down the external benchmark, or the practitioner anchored on the firm's own framework documents because they are easier to cite.

Fix: the matrix has at least one named, dated external benchmark with section references. Reviewing a policy against itself or against generic guidance fragments without anchored sources is internal-consistency editing, not a gap review. The schema enforces `benchmark_sources` with `minItems: 1` and `section_references` with `minItems: 1`. Pull the benchmark from `obligation-mapping` output, or name the rule and guidance directly with section refs from `references/source-anchors.md`.

#### 2. Severity assigned without rationale

Symptom: every row carries a severity rating; rationale fields are blank, or read "high because high impact."

Why it happens: severity feels obvious to the practitioner who built the matrix; rationale feels redundant.

Fix: severity is paired with rationale referencing materiality (against firm thresholds where they exist), supervisory exposure (active examination scope, MRA/MRIA-eligibility, recent enforcement against similar weaknesses), customer impact, operational risk, and compensating practice. Severity without rationale is opinion. The schema enforces `severity_rationale` as required. A reviewer who cannot challenge a severity rating cannot attest it.

#### 3. Recommended edit just restates the gap

Symptom: row's recommended edit reads "add language on AI systems" or "address vendor monitoring."

Why it happens: the gap is identified, the next step feels obvious, the practitioner does not write the next step.

Fix: the recommended edit is declarative and at least summary-drafted. "Add §X.4 stating that AI systems are within the model inventory, tiered by use-case impact, and require validation evidence proportionate to use-case impact" is a recommended edit. "Add language on AI systems" is not. The summary draft does not have to be the final wording (that is the policy author's job), but it has to be a starting point.

#### 4. Gap classification collapses missing into partial

Symptom: row's policy-text field reads "policy is silent" but the classification is `partial`.

Why it happens: `partial` feels softer than `missing`, and the practitioner softens.

Fix: the five classifications are not interchangeable. `missing` is silence on the requirement. `partial` is addressing some of the requirement but stopping short. Conflating the two understates the gap and makes the recommended edit harder to scope. The schema does not enforce the distinction; the reviewer has to. A row whose policy-text reads "silent" is `missing`, not `partial`.

#### 5. Evidence-needed empty on partial-or-worse rows

Symptom: rows classified `partial`, `weak`, `inconsistent`, or `outdated` have empty `evidence_needed` arrays.

Why it happens: the practitioner focuses on the text fix and forgets the operational dimension. The text edit feels like the whole story.

Fix: evidence-needed is mandatory on rows classified `partial`, `weak`, `inconsistent`, or `outdated`. The text fix alone rarely closes an operational gap; the matrix surfaces the operational dimension explicitly. Evidence needed names the standards updates, training, workflow changes, attestations, or system configuration the firm would inspect to confirm closure.

#### 6. Coverage summary as percentage, no counts

Symptom: coverage summary reads "we cover most of the rule" or "approximately 70% covered."

Why it happens: the practitioner has a sense of coverage but did not enumerate the benchmark items.

Fix: coverage summary fields are integer counts. Total benchmark requirements in scope, covered items, partial items, missing items. Percentages are derived for the surface artifact; the structured record carries counts. A summary like "most of the rule is covered" without counts fails the matrix's audit-defensibility test. The schema enforces integer counts.

#### 7. Owner is a department, not a role

Symptom: owner field reads "Compliance," "TPRM," "the policy team."

Why it happens: the engagement has not pinned down the named accountable role at the section level, and the department-level label feels right at the level of generality the matrix was drafted at.

Fix: owner is a named role with accountability: Head of Model Risk, Head of Vendor Management, Chief Privacy Officer, BSA Officer, Head of Consumer Compliance. Where the role taxonomy is firm-specific, it lives in `references/firm-overlay.md`. "Compliance" is not an owner; "Head of Compliance Operations" is.

#### 8. Cross-policy interactions buried in commentary

Symptom: the matrix body has rich commentary on how the gap relates to other firm policies; the `cross_policy_interactions` array is empty.

Why it happens: the commentary feels like enough; the structured field feels redundant.

Fix: most material gaps interact with at least one other firm policy. Vendor policy and information-security policy on subcontractor depth. MRM policy and AI governance committee charter. BSA/AML and consumer-compliance on customer-onboarding flows. The interaction is named (`dependency`, `conflict`, `overlap`) and described in the structured record so the cross-policy fix can route to the right co-owner. Burying interactions in commentary breaks the firm's overall governance architecture.

#### 9. Outdated misclassified as partial when the benchmark refreshed

Symptom: row policy-text references SR 11-7 with no acknowledgement of OCC Bulletin 2026-13, or references OCC 2013-29 with no acknowledgement of the June 2023 interagency guidance. Classification is `partial`.

Why it happens: the practitioner reads the policy as substantively addressing the topic, classifies as `partial`, and misses that the policy reflects an obsolete benchmark.

Fix: `outdated` is the classification when the policy reflects a prior edition of the benchmark that has since been refreshed. The recommended edit names the refreshed benchmark; the gap is not just about content, it is about the version the policy traces to. The June 2023 TPRM guidance and OCC Bulletin 2026-13 both create a wave of `outdated` rows in policies that have not been refreshed; the matrix should call them by name.

#### 10. Out-of-scope items unwritten

Symptom: `out_of_scope_items` is empty. The matrix benchmarks against a rule with multiple exemptions, threshold-based provisions, or institution-type carve-outs, but does not name them.

Why it happens: the practitioner did not document the rationale for skipping benchmark items the firm does not cover.

Fix: out-of-scope items name the benchmark item the firm deliberately does not cover and the rationale (threshold not met, institution-type exemption, deferred effective date, explicit carve-out). This is an audit-defence artefact; reconstructed rationale is harder than written rationale. A regulator who asks "why didn't you address §X" is happier with "we did, here is the rationale" than with silence.

#### 11. The matrix is signed off without independent reviewer

Symptom: sign-off block names the practitioner who built the matrix and the policy owner; no independent severity reviewer is named.

Why it happens: the engagement compresses the review machinery, especially when the practitioner is the policy owner.

Fix: severity assignment always carries human review, and the severity reviewer is independent of the author for severity attestation. For 1.5-line-built matrices, the 2-line function reviews severity. For 2-line-built matrices, internal audit or an independent peer reviews. The policy owner concurs on the recommended edits but the severity reviewer is a separate seat; a single name in both seats fails the independence test.

#### 12. The matrix tries to be the policy redline

Symptom: recommended edits read as full draft text, with markup-style annotations, and the matrix begins to look like a marked-up policy.

Why it happens: the recommended edit feels easier to write at full draft length than at summary-draft length, and the practitioner over-runs the boundary with the policy rewrite.

Fix: this skill produces the gap list and summary-draft recommended edits. The redline lives in the policy-rewrite cycle (which the policy owner runs, or which `policy-diff` tracks once two versions exist). Recommended edit is declarative and at summary-draft level; the policy author works it up to final wording. The matrix that reads as a redline has overrun the boundary.

#### 13. Boundary with policy-diff is unclear

Symptom: the engagement has both an old version and a new version of the same policy and is asking this skill to compare them.

Why it happens: the boundary between policy-gap-review (policy vs benchmark) and policy-diff (version vs version) is not always intuitive.

Fix: this skill compares one policy to an external benchmark (rule, guidance, obligation register). `policy-diff` compares two versions of the same policy. If the engagement has v3.4 and v4.0 of the same policy and wants to know what changed and whether the changes address the benchmark, run policy-diff first (what changed) and policy-gap-review second (does what changed close the gaps). Confusing the two leads to a matrix that reads as a poor redline rather than a gap inventory.

#### 14. Linked obligation IDs fabricated when register did not yet carry them

Symptom: `linked_obligation_ids` array is populated with IDs that do not exist in the obligation register.

Why it happens: the practitioner assumed the obligation register would carry the obligation, drafted an ID, and moved on.

Fix: where the obligation register did not yet carry the obligation, the gap row leaves `linked_obligation_ids` empty and routes a back-reference into `obligation-mapping`. The register reopens for the section the gap surfaced. Fabricating an obligation ID breaks the cross-skill foreign-key contract and creates phantom rows downstream.

#### 15. The skill stops too late

Symptom: the matrix is "signed off" with severity ratings asserted and recommended-edit approvals claimed, without independent attestation.

Why it happens: builder over-runs the human-review gate.

Fix: the matrix is a draft until the named reviewer attests. Severity assignment always carries human review. The skill stops at the draft and surfaces the reviewer questions; it does not assert severity sign-off, distribute the matrix to committee, or post recommended edits to the policy management system. The `human_review_required` field is always true.
