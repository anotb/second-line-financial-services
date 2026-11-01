# Examples and troubleshooting

One section per worked example, then troubleshooting. Read only what you need.

## critical-vendor-onboarding-gates

### Example: Critical-vendor onboarding gates aligned to interagency TPRM guidance

#### Input

A mid-sized US bank ($12B assets, FRB- and FDIC-supervised state-member, sub-Heightened-Standards but with a material vendor footprint) is refreshing its critical-vendor onboarding gate matrix to align with the Interagency Guidance on Third-Party Relationships (June 2023). The current onboarding workflow has a single "vendor approval" gate that compresses planning, due diligence, contract review, and operational confirmation into one Vendor Risk Committee decision; the bank's own internal audit raised this as a finding in the most recent audit cycle. The refresh is also responsive to a recent FDIC supervisory letter that cited insufficient documentation of ongoing-monitoring decisions. Source posture is mixed: Interagency TPRM Guidance (June 2023), the firm's existing Third-Party Risk Management Policy v3.5, and the audit-finding remediation memorandum. Engagement scope is supplied: institution type state-member bank, primary regulators FRB and FDIC, persona Head of Vendor Risk Management, source posture mixed, sector overlay banking, no AI cross-cutting overlay (vendor portfolio is conventional). Audience is the Vendor Risk Committee adopting the matrix as charter language, with copy to the Operational Risk Committee.

#### Why this scenario matters

Vendor risk management is the most-examined second-line function at most US banks because the Interagency Guidance is explicit and the federal supervisors have prioritised vendor oversight in recent exam cycles. A common failure mode (one-committee monoculture compressing all vendor decisions into one gate) is exactly what this engagement is correcting. The example tests: distinct gates aligned to TPRM lifecycle phases (planning, due diligence, contract, ongoing monitoring, termination); criticality-driven gate intensity; line-1 / line-2 separation under the interagency guidance; documentation that survives an FDIC examination; the gap where an exit-plan gate is implicit but not yet operationally gated; and recommended charter language for the Vendor Risk Committee.

#### Output sketch (gate matrix excerpt)

```yaml
gate_matrix_id: GM-2026-VRC-Critical-Vendor-Lifecycle-001
workflow_in_scope: "Critical-vendor onboarding lifecycle: planning, due diligence, contract, ongoing monitoring, termination. Critical vendors only; non-critical vendors flow through a lighter workflow not in scope of this matrix."
scope_notes: "Critical vendor definition per firm TPRM policy v3.5 §2.1: vendors providing services material to operational resilience, vendors with access to NPI, vendors providing critical-platform technology. Excludes intra-group affiliates supervised under separate enterprise-resilience framework."
source_posture: mixed
engagement_id: ENG-2026-VRC-Charter-Refresh

decision_authority:
  primary_committee: "Vendor Risk Committee (VRC)"
  escalation_committee: "Operational Risk Committee, escalating to Risk Committee of the Board for material termination or material onboarding"
  dissent_path: "Any VRC member may record a dissent in the meeting minutes; recorded dissents on critical-vendor gates trigger automatic escalation to the Operational Risk Committee."
  board_oversight: "Quarterly summary of critical-vendor portfolio status to Board Risk Committee; annual report on TPRM program effectiveness."

gates:
  - gate_id: GATE-VEN-001
    gate_name: "Critical-vendor planning gate"
    stage: planning
    trigger: "Business sponsor proposes engagement of a critical vendor (per firm criticality definition); planning gate fires before any due-diligence work begins"
    required_reviewers:
      - role: "Head of Vendor Risk Management (line 2)"
        is_primary: true
        independence_required: true
        independence_basis: "Interagency TPRM §III.A; firm TPRM Policy v3.5 §3.1"
      - role: "Business Sponsor (line 1)"
        is_primary: false
      - role: "Head of Procurement (operational coordination)"
        is_primary: false
    required_inputs:
      - "Business case with named line-1 owner"
      - "Strategic alignment statement"
      - "Initial criticality classification"
      - "Initial risk assessment (data sensitivity, operational dependence, customer-impact)"
    decision_criteria:
      - criterion: "Engagement aligns with firm strategy and risk appetite"
        source_anchor: "Interagency TPRM §III.A; references/source-anchors.md#interagency-tprm"
      - criterion: "Initial criticality classification is supported"
        source_anchor: "references/firm-overlay.md#criticality-definition"
      - criterion: "Named line-1 owner accepts ongoing-monitoring accountability"
        source_anchor: "references/source-anchors.md#interagency-tprm"
    stop_conditions:
      - "No advance to due-diligence without line-1 owner acceptance of monitoring accountability"
      - "No advance if business case lacks strategic-alignment rationale"
    escalation_path:
      escalation_committee: "Operational Risk Committee"
      time_to_escalate: "Next scheduled VRC meeting"
      escalation_owner: "Head of Vendor Risk Management"
    documentation_requirement:
      - "Planning decision in VRC minutes"
      - "Business case and initial assessment retained in GRC platform vendor record"
    frequency: event-based
    source_anchor: "Interagency TPRM Guidance §III.A; references/source-anchors.md#interagency-tprm-2023"

  - gate_id: GATE-VEN-002
    gate_name: "Pre-contract due-diligence gate"
    stage: due-diligence
    trigger: "Due-diligence work substantially complete; vendor identified as preferred candidate; gate fires before contract negotiation begins"
    required_reviewers:
      - role: "Head of Vendor Risk Management (line 2)"
        is_primary: true
        independence_required: true
        independence_basis: "Interagency TPRM §III.B; firm TPRM Policy v3.5 §4.1"
      - role: "Business Sponsor (line 1)"
        is_primary: false
      - role: "CISO (cyber due diligence)"
        is_primary: false
        independence_basis: "Interagency TPRM §III.B; FFIEC IT Booklet"
      - role: "General Counsel (legal due diligence)"
        is_primary: false
      - role: "Chief Privacy Officer (when NPI is in scope)"
        is_primary: false
      - role: "Operational Risk Committee (concurrence required for highest-criticality vendors per firm policy)"
        is_primary: false
    required_inputs:
      - "Due-diligence pack covering financial condition, business reputation, technology and infrastructure, information security, business resilience, fee structures and incentives, qualifications and experience of key personnel, risk management"
      - "SOC 2 Type II report or equivalent, with firm review of qualifying opinions"
      - "Cybersecurity assessment and any third-party penetration-test attestations"
      - "Resolution of any high-residual-risk findings or documented mitigation"
      - "Initial draft exit plan (criticality-driven; required for highest-criticality vendors)"
    decision_criteria:
      - criterion: "Due diligence covers each named area in TPRM §III.B"
        source_anchor: "Interagency TPRM §III.B; references/source-anchors.md#interagency-tprm"
      - criterion: "Identified residual risks are mitigated, documented, or accepted by VRC"
        source_anchor: "Interagency TPRM §III.B"
      - criterion: "SOC 2 report covers the relevant Trust Services Criteria for the services in scope; qualified opinions are reviewed and addressed"
        source_anchor: "references/cross-cutting.md#cyber (loaded if cyber overlay flagged)"
      - criterion: "Exit-plan readiness is documented for highest-criticality vendors"
        source_anchor: "Interagency TPRM §III.E; references/firm-overlay.md#exit-plan-policy"
    stop_conditions:
      - "No proceed to contract gate without resolution of high-residual-risk findings"
      - "No proceed without SOC 2 Type II (or equivalent) where applicable to the service"
      - "No proceed without initial exit plan for highest-criticality vendors"
      - "No proceed without CISO concurrence on cyber-due-diligence completeness"
    escalation_path:
      escalation_committee: "Operational Risk Committee"
      time_to_escalate: "Next scheduled meeting; emergency convening for material delays"
      escalation_owner: "Head of Vendor Risk Management"
    documentation_requirement:
      - "Due-diligence decision in VRC minutes with named attesters"
      - "Due-diligence pack retained in GRC platform vendor record (system: GRC-Vendor-Records)"
      - "SOC 2 report and attestation retained in GRC platform"
      - "Cyber assessment retained per firm cyber-records retention"
    frequency: event-based
    source_anchor: "Interagency TPRM Guidance §III.B (due diligence and selection); references/source-anchors.md#interagency-tprm-2023"

  - gate_id: GATE-VEN-003
    gate_name: "Contract gate"
    stage: contract
    trigger: "Contract substantially negotiated; gate fires before contract execution"
    required_reviewers:
      - role: "Head of Vendor Risk Management (line 2)"
        is_primary: true
      - role: "General Counsel"
        is_primary: false
      - role: "Business Sponsor"
        is_primary: false
      - role: "Head of Operational Risk (concurrence on critical contracts)"
        is_primary: false
        independence_basis: "Interagency TPRM §III.C"
      - role: "CISO (concurrence on contracts with cyber implications)"
        is_primary: false
    required_inputs:
      - "Negotiated contract with all material terms"
      - "Risk-management terms summary (information rights, audit rights, performance metrics, fourth-party considerations, exit terms)"
      - "Service-level commitments aligned to firm operational-resilience requirements"
      - "Updated exit plan reflecting contract terms"
    decision_criteria:
      - criterion: "Contract addresses each TPRM-named risk-management area appropriately for the criticality"
        source_anchor: "Interagency TPRM §III.C; references/source-anchors.md#interagency-tprm"
      - criterion: "Information and audit rights enable firm-side oversight at the criticality level"
        source_anchor: "Interagency TPRM §III.C"
      - criterion: "Exit terms are workable and align with the exit-plan readiness"
        source_anchor: "Interagency TPRM §III.E"
    stop_conditions:
      - "No execution without complete risk-management terms"
      - "No execution if information or audit rights are not commensurate with criticality"
      - "No execution if exit terms render exit plan unexecutable"
    escalation_path:
      escalation_committee: "Operational Risk Committee, escalating to Risk Committee of the Board for materially long-tail contracts"
      time_to_escalate: "Within 5 business days of contested terms"
      escalation_owner: "General Counsel and Head of Vendor Risk Management"
    documentation_requirement:
      - "Contract gate decision in VRC minutes"
      - "Final contract retained in contract management system"
      - "Risk-management terms summary retained in GRC platform"
    frequency: event-based
    source_anchor: "Interagency TPRM Guidance §III.C (contract negotiation); references/source-anchors.md#interagency-tprm-2023"

  - gate_id: GATE-VEN-004
    gate_name: "Post-onboarding 90-day operational confirmation gate"
    stage: ongoing-monitoring
    trigger: "90 days post-go-live with the vendor; first formal ongoing-monitoring touchpoint"
    required_reviewers:
      - role: "Head of Vendor Risk Management"
        is_primary: true
      - role: "Business Sponsor"
        is_primary: false
      - role: "Vendor Relationship Manager (firm-side single point of contact)"
        is_primary: false
    required_inputs:
      - "First 90 days of operational performance against SLAs"
      - "First 90 days of monitoring evidence (SOC report cycle status, incident history, complaint history if applicable)"
      - "Confirmation that contracted controls are operating as designed"
    decision_criteria:
      - criterion: "Vendor performance meets contracted SLAs and risk-management commitments at 90 days"
        source_anchor: "Interagency TPRM §III.D; firm TPRM Policy v3.5 §5.1"
      - criterion: "No material monitoring exceptions in the 90-day window"
        source_anchor: "references/source-anchors.md#interagency-tprm"
      - criterion: "Annual ongoing-monitoring schedule is populated in GRC platform"
        source_anchor: "references/firm-overlay.md#monitoring-cadence"
    stop_conditions:
      - "No advance to standard ongoing monitoring if material SLA failures are unresolved"
      - "Re-engagement of due-diligence gate if unforeseen material risks have surfaced"
    escalation_path:
      escalation_committee: "Operational Risk Committee"
      time_to_escalate: "Next VRC meeting"
      escalation_owner: "Head of Vendor Risk Management"
    documentation_requirement:
      - "90-day decision in VRC minutes"
      - "Performance pack retained in GRC platform"
    frequency: event-based
    frequency_detail: "90 days post-go-live; one-time gate"
    source_anchor: "Interagency TPRM Guidance §III.D (ongoing monitoring); references/source-anchors.md#interagency-tprm-2023"

  - gate_id: GATE-VEN-005
    gate_name: "Annual ongoing-monitoring gate"
    stage: ongoing-monitoring
    trigger: "Annual ongoing-monitoring cycle for each critical vendor"
    required_reviewers:
      - role: "Head of Vendor Risk Management"
        is_primary: true
      - role: "Business Sponsor"
        is_primary: false
      - role: "CISO (when cyber-relevant)"
        is_primary: false
      - role: "Operational Risk Committee (concurrence on highest-criticality vendors)"
        is_primary: false
    required_inputs:
      - "Annual SOC report review"
      - "Annual cyber assessment refresh (when cyber-relevant)"
      - "Year of monitoring evidence (SLAs, incidents, complaints, financial-condition signals)"
      - "Updated exit plan reflecting any year-on-year changes"
      - "Refreshed criticality classification"
    decision_criteria:
      - criterion: "Vendor continues to meet contracted commitments and risk-management expectations"
        source_anchor: "Interagency TPRM §III.D"
      - criterion: "No accumulated monitoring exceptions unresolved"
      - criterion: "Exit plan remains workable and tested within last 12 months for highest-criticality vendors"
        source_anchor: "Interagency TPRM §III.E"
    stop_conditions:
      - "Re-engagement of full due-diligence if vendor's financial condition or business has materially changed"
      - "Acceleration to termination gate if material risk-management failures are unresolved"
    documentation_requirement:
      - "Annual ongoing-monitoring decision in VRC minutes"
      - "Refresh pack retained in GRC platform"
      - "Cross-reference to any related issue write-ups"
    frequency: annual
    source_anchor: "Interagency TPRM Guidance §III.D; references/source-anchors.md#interagency-tprm-2023"

  - gate_id: GATE-VEN-006
    gate_name: "Termination gate"
    stage: termination
    trigger: "Decision to terminate critical-vendor relationship (firm-initiated, vendor-initiated, or contract-end)"
    required_reviewers:
      - role: "Head of Vendor Risk Management"
        is_primary: true
      - role: "Business Sponsor"
        is_primary: false
      - role: "General Counsel"
        is_primary: false
      - role: "Head of Operational Risk"
        is_primary: false
      - role: "Operational Risk Committee (full committee concurrence on termination of highest-criticality vendors)"
        is_primary: false
        independence_basis: "Interagency TPRM §III.E"
    required_inputs:
      - "Exit plan with named milestones, owners, and dates"
      - "Customer-impact analysis"
      - "Data-return and data-destruction plan"
      - "Service-continuity plan (replacement vendor, in-house substitute, customer notification if applicable)"
    decision_criteria:
      - criterion: "Exit plan is workable and addresses each TPRM-named termination area"
        source_anchor: "Interagency TPRM §III.E; references/source-anchors.md#interagency-tprm"
      - criterion: "Customer impact is assessed and any customer-notification or transition obligations are met"
        source_anchor: "Interagency TPRM §III.E; CFPB CMS framework"
      - criterion: "Data-return and data-destruction plan addresses all NPI and other firm data"
        source_anchor: "Interagency TPRM §III.E; GLBA Safeguards Rule"
    stop_conditions:
      - "No termination execution without OpRC concurrence for highest-criticality vendors"
      - "No termination execution without confirmed customer-impact analysis"
      - "No termination execution if exit plan is not workable on stated timeline"
    escalation_path:
      escalation_committee: "Risk Committee of the Board"
      time_to_escalate: "Within the termination notice window; emergency convening if termination is regulator-driven"
      escalation_owner: "Head of Vendor Risk Management; General Counsel for legal-driven terminations"
    documentation_requirement:
      - "Termination decision in VRC and OpRC minutes"
      - "Exit plan execution evidence retained in GRC platform"
      - "Data-return and data-destruction attestation retained"
    frequency: event-based
    source_anchor: "Interagency TPRM Guidance §III.E (termination); references/source-anchors.md#interagency-tprm-2023"

gate_gaps:
  - implied_gate_name: "Exit-plan readiness gate (separate from termination gate)"
    gap_description: "Current workflow assumes the exit plan exists if the termination gate fires; the Interagency TPRM Guidance §III.E and the firm's own audit finding (memo IA-2026-Q1-014) both point to exit-plan readiness as a continuous obligation rather than a termination-gate input. Implies a periodic exit-plan readiness assessment with a named gate, distinct from the termination gate that consumes the exit plan when terminating."
    source_anchor: "Interagency TPRM §III.E; firm internal audit memo IA-2026-Q1-014"
    recommended_action: "Add an exit-plan tabletop / readiness gate at criticality-driven cadence (annual for highest criticality, biennial otherwise). The annual-monitoring gate can incorporate the exit-plan readiness check, but the testing of the plan (tabletop) is a separate gate with named participants."
  - implied_gate_name: "Fourth-party risk gate for material subcontractors"
    gap_description: "Current workflow does not separately gate the firm's exposure to the vendor's material subcontractors. Interagency TPRM §III.D names fourth-party risk as part of ongoing monitoring; some firms gate it as a distinct decision."
    source_anchor: "Interagency TPRM §III.D"
    recommended_action: "At due-diligence and at annual monitoring, identify material subcontractors and assess fourth-party risk; document in vendor record. A separate gate may not be necessary if the existing gates explicitly address fourth-party considerations."

recommended_charter_language: |
  The Vendor Risk Committee (the Committee) is the firm's primary governance body for critical-vendor relationships across the third-party-risk lifecycle from planning through termination. The Committee operates with decision authority on critical-vendor onboarding, contract approval, ongoing monitoring, and termination, with the Operational Risk Committee as the named escalation body for highest-criticality decisions and recorded dissents.

  The Committee carries six named gates: planning, pre-contract due diligence, contract, post-onboarding 90-day operational confirmation, annual ongoing monitoring, and termination. Each gate has named decision criteria sourced from the Interagency Guidance on Third-Party Relationships (June 2023) and the firm's Third-Party Risk Management Policy. Stop conditions are declarative; the gates are not advisory. The Committee's gate decisions are documented in the meeting minutes with named attesters and the documentation is retained in the firm's governance system per the firm's records-retention schedule (typically 7-year retention aligned to federal banking exam-file expectations).

  For highest-criticality vendors, contract gates and termination gates require Operational Risk Committee concurrence; the Committee reports to the Board Risk Committee on the critical-vendor portfolio quarterly with material decisions surfaced for board-level oversight. Cyber considerations engage the Chief Information Security Officer as a required reviewer at due-diligence, contract, and annual monitoring gates whenever the vendor's services touch firm information assets, customer data, or privileged-system access.

reviewer_questions:
  - "Should the firm adopt a separate exit-plan readiness gate as recommended in the gap section, or fold the testing into the annual ongoing-monitoring gate? Operational risk and audit views may differ."
  - "For the Operational Risk Committee concurrence requirement on highest-criticality contract and termination gates, what is the firm's escalation cadence (next scheduled meeting vs. emergency convening) and is the OpRC charter aligned with this expectation?"
  - "Does the firm's current critical-vendor population permit annual SOC report review for every critical vendor, or does the cadence need adjustment based on vendor SOC reporting cycles?"
  - "For fourth-party risk, is a separate gate necessary or do the existing gates' decision criteria (fourth-party language at due diligence and annual monitoring) suffice?"

confidence_label: medium
human_review_required: true
```

#### What the matrix surfaces

- **Six distinct gates aligned to TPRM lifecycle**. Planning, due diligence, contract, 90-day operational confirmation, annual monitoring, termination. Each ties directly to a TPRM section. Not the one-committee monoculture the audit flagged.
- **Independence on line-2 and CISO slots**. Head of Vendor Risk Management has independence flagged at planning and due-diligence with the source anchor; CISO independence flagged at due-diligence with the FFIEC and TPRM anchors. Operational Risk Committee independence flagged at contract and termination for highest-criticality.
- **OpRC concurrence on highest-criticality**. The matrix names OpRC concurrence as a required reviewer at the contract gate and termination gate for highest-criticality vendors, distinct from VRC quorum. This addresses the FDIC supervisory-letter concern about insufficient documentation of material vendor decisions.
- **Documentation discipline tied to FDIC examination posture**. Retention named at 7 years; system of record named (GRC-Vendor-Records); board reporting cadence named.
- **Real gap surfaced**. The exit-plan readiness gate is implicit in TPRM §III.E and explicit in the firm's own audit finding; the gap section names this with the source anchor and the recommended action. Fourth-party risk also surfaced, with the recommendation to fold into existing gates rather than create a new one (right-sized).
- **Recommended charter language as committee-adoptable**. Three paragraphs, names the gates, the criticality-driven OpRC concurrence pattern, and the cyber-CISO engagement.
- **Reviewer questions tie to live decisions**. Exit-plan readiness gate scope, OpRC escalation cadence, SOC review cadence for the vendor portfolio, fourth-party gate scope. Each is a real call the committee needs to make.

#### Downstream uses

- `vendor-diligence` references GATE-VEN-002 (due diligence) in its sign-off block; the diligence pack maps to required_inputs.
- `exit-plan` references GATE-VEN-003 (contract; exit terms) and GATE-VEN-006 (termination); the exit plan is a required input.
- `compliance-testing` for the TPRM control test reads the gates as the named decision points; the test workpaper samples gate-decision documentation.
- `risk-committee-pack` for the next OpRC reads termination-gate decisions and material onboarding decisions; for the next Board Risk Committee reads the quarterly summary.
- `issue-writeup` for any vendor-monitoring exception links to the relevant gate; the issue's severity drops the vendor's effective-monitoring rating until closure.

## regional-bank-ai-lifecycle-gates

### Example: AI use-case lifecycle gates for a regional bank

#### Input

A US regional bank ($35B assets, OCC-supervised national bank, not yet at the Heightened Standards threshold but tracking towards it) is standing up an AI Governance Committee and needs a named gate matrix for the full AI use-case lifecycle. The bank already runs a Model Risk Committee for traditional models under SR 11-7; the AI committee will partner with the MRC for AI-extended models and stand alone for non-model AI use cases (operational AI, contact-center AI, document-extraction AI). Source posture is mixed: OCC Bulletin 2026-13, NIST AI RMF 1.0 and AI 600-1 Generative AI Profile, the firm's existing Model Risk Management Policy v4.1, and a draft AI Governance Policy v1.0. Risk tiering uses a tiered impact framework: T1 (high-impact, customer-facing or material financial-decision use cases), T2 (moderate-impact internal-decision use cases), T3 (low-impact operational use cases). Engagement scope is supplied: institution type national-bank, primary regulator OCC, persona Head of Model Risk Management, source posture mixed, sector overlay banking, cross-cutting overlay cyber. Audience is the AI Governance Committee adopting the matrix as charter language.

#### Why this scenario matters

AI governance is one of the most-asked second-line topics in 2026 because the regulator constellation is unsettled (OCC 2026-13 plus NIST AI RMF plus EU AI Act for EU-touching firms plus state-DFS letters plus NAIC and state DOI bulletins for insurers). Banks frequently confuse AI governance with model risk governance and end up with one committee owning everything, which fails Heightened Standards-adjacent expectations on independent risk management and three-lines-of-defense. The example tests: distinct gates for distinct lifecycle stages; independence on a real specific control attribute (developer-validator separation under SR 11-7, layered for AI use cases); coordination with the Model Risk Committee for AI-extended models without collapsing the two committees; tier-driven gate intensity; the cyber overlay firing on customer-data-touching use cases; the gap where the firm has no formal annual review gate; and recommended charter language the committee can adopt.

#### Output sketch (gate matrix excerpt)

```yaml
gate_matrix_id: GM-2026-AIGC-AI-Lifecycle-001
workflow_in_scope: "AI use-case lifecycle: intake, tiering, pre-prod, go-live, ongoing monitoring, retirement, for all AI use cases firm-wide."
scope_notes: "Includes AI-extended models (joint with Model Risk Committee). Excludes pure-research / sandbox-only AI work that has not exited research."
source_posture: mixed
engagement_id: ENG-2026-AIGC-Charter-Refresh

decision_authority:
  primary_committee: "AI Governance Committee (AIGC)"
  escalation_committee: "Operational Risk Committee, escalating to Board Risk Committee for material decisions"
  dissent_path: "Any AIGC member may record a dissent in the meeting minutes; a recorded dissent on a T1 go-live triggers automatic escalation to the Operational Risk Committee."
  board_oversight: "Annual report from AIGC chair to Board Risk Committee; quarterly summary of T1 use cases and material decisions."

gates:
  - gate_id: GATE-AI-001
    gate_name: "AI use-case intake gate"
    stage: intake
    trigger: "Submission of AI Use Case Intake Form by a business sponsor"
    required_reviewers:
      - role: "Head of AI Governance (firm-overlay path)"
        is_primary: true
        independence_required: false
      - role: "Business Sponsor (line 1)"
        is_primary: false
        independence_required: false
    required_inputs:
      - "AI Use Case Intake Form (firm-overlay-defined)"
      - "Business Sponsor attestation of intended use, data scope, model dependencies"
    decision_criteria:
      - criterion: "Use case is in scope of AI Governance (per firm-overlay AI definition; excludes traditional rule-based automation)"
        source_anchor: "references/firm-overlay.md#ai-definition"
      - criterion: "Sponsor has named accountable line-1 owner"
        source_anchor: "references/source-anchors.md#nist-ai-rmf-gv-2"
    stop_conditions:
      - "No proceed if no accountable line-1 owner is named"
      - "No proceed if intake form is incomplete on data scope or intended use"
    escalation_path:
      escalation_committee: "Operational Risk Committee"
      time_to_escalate: "Next scheduled AIGC meeting + 5 business days"
      escalation_owner: "Head of AI Governance"
    documentation_requirement:
      - "Intake decision in AIGC minutes"
      - "Intake form retained in GRC platform AI use-case record"
    frequency: event-based
    frequency_detail: "Submission of intake form by sponsor"
    source_anchor: "NIST AI RMF GV-2.1 (accountability structures); references/firm-overlay.md#aigc-charter"

  - gate_id: GATE-AI-002
    gate_name: "Risk tiering gate"
    stage: tiering
    trigger: "Completed intake; AIGC review of risk-tier classification within 10 business days of intake"
    required_reviewers:
      - role: "Head of AI Governance"
        is_primary: true
      - role: "Head of Model Risk Management"
        is_primary: false
        independence_required: true
        independence_basis: "SR 11-7 §VI; for AI-extended models, MRMO classification requires independence from developer"
      - role: "Head of Operational Risk"
        is_primary: false
      - role: "Chief Privacy Officer (when use case touches NPI)"
        is_primary: false
    required_inputs:
      - "Intake form with sponsor attestation"
      - "Data inventory (data sources, classification, NPI flag)"
      - "Use-case description with intended decision impact"
    decision_criteria:
      - criterion: "Tier classification (T1/T2/T3) is supported by the use-case impact assessment per firm tiering policy"
        source_anchor: "references/firm-overlay.md#ai-tiering-v2"
      - criterion: "Use case is or is not an AI-extended model (drives MRC coordination)"
        source_anchor: "OCC Bulletin 2026-13 §III.F; references/source-anchors.md#occ-2026-13"
    stop_conditions:
      - "No advance to pre-prod if tier classification is contested without resolution by the AIGC"
      - "No T1 classification without Chief Privacy Officer concurrence when NPI is in scope"
    escalation_path:
      escalation_committee: "Operational Risk Committee"
      time_to_escalate: "Within 10 business days of contested tiering"
      escalation_owner: "Head of AI Governance"
    documentation_requirement:
      - "Tiering decision with rationale in AIGC minutes"
      - "Tiering memorandum retained in GRC platform"
    frequency: event-based
    source_anchor: "OCC Bulletin 2026-13; NIST AI RMF MAP function; references/firm-overlay.md#ai-tiering-v2"

  - gate_id: GATE-AI-003
    gate_name: "Pre-prod gate (T1 and T2)"
    stage: pre-prod
    trigger: "Use case ready for pre-production deployment; T3 use cases skip this gate per firm tiering policy"
    required_reviewers:
      - role: "Head of AI Governance"
        is_primary: true
      - role: "Independent Validator (line 2; for AI-extended models, the Model Risk validator)"
        is_primary: false
        independence_required: true
        independence_basis: "SR 11-7 §V; OCC Bulletin 2026-13 §III.E; firm AI Governance Policy v1.0 §4.2"
      - role: "CISO (when cyber overlay loaded)"
        is_primary: false
        independence_basis: "NYDFS §500.4 (where covered); firm cyber policy"
      - role: "Head of Model Risk Management (for AI-extended models; joint MRC coordination)"
        is_primary: false
    required_inputs:
      - "Model card per `model-card-builder` skill"
      - "Validation report per `validation-report` skill (or model-validator equivalent)"
      - "Issue log status — no open critical or high issues against the use case"
      - "Cyber security architecture review for use cases touching customer data or privileged systems"
    decision_criteria:
      - criterion: "Validation independence is established (validator is not the developer; documented chain)"
        source_anchor: "references/source-anchors.md#sr-11-7"
      - criterion: "Model card is complete per firm template"
        source_anchor: "references/firm-overlay.md#model-card-template"
      - criterion: "No open critical or high issues against the use case"
        source_anchor: "references/source-anchors.md#sr-11-7"
      - criterion: "Cyber architecture review is complete with no unmitigated high-severity findings (when in scope)"
        source_anchor: "references/cross-cutting.md#cyber"
    stop_conditions:
      - "No advance to go-live with any open critical or high issue"
      - "No advance with missing model card or validation report"
      - "No advance with validator-developer overlap (independence violation)"
      - "No advance with unmitigated cyber high-severity findings"
    escalation_path:
      escalation_committee: "Operational Risk Committee (joint with Model Risk Committee for AI-extended models)"
      time_to_escalate: "Next scheduled committee meeting"
      escalation_owner: "Head of AI Governance"
    documentation_requirement:
      - "Pre-prod gate decision with attesters in AIGC minutes"
      - "Validation report and model card retained in GRC platform AI use-case record"
      - "Issue log snapshot retained as gate evidence"
    frequency: event-based
    source_anchor: "SR 11-7 §V, §VI; OCC Bulletin 2026-13 §III.E; references/source-anchors.md#sr-11-7"

  - gate_id: GATE-AI-004
    gate_name: "T1 production go-live gate"
    stage: go-live
    trigger: "T1 use case ready for production; T2 and T3 use cases pass through a lighter go-live workflow that does not require AIGC committee gate"
    required_reviewers:
      - role: "AI Governance Committee (committee decision; not individual reviewer)"
        is_primary: true
      - role: "Head of Model Risk Management (for AI-extended models)"
        is_primary: false
        independence_required: true
      - role: "Business Head (line 1 sponsor)"
        is_primary: false
      - role: "CISO (when cyber overlay loaded)"
        is_primary: false
      - role: "Chief Privacy Officer (when NPI in scope)"
        is_primary: false
    required_inputs:
      - "All pre-prod gate evidence"
      - "Production-readiness assessment (operations, monitoring, incident-response)"
      - "Business owner attestation of go-live readiness"
      - "Annual-review schedule populated in GRC platform"
    decision_criteria:
      - criterion: "All pre-prod gate criteria continue to be satisfied"
        source_anchor: "references/source-anchors.md#sr-11-7"
      - criterion: "Production monitoring plan is complete with named monitoring owner and named thresholds"
        source_anchor: "NIST AI RMF MEASURE function; references/firm-overlay.md#monitoring-plan"
      - criterion: "Annual-review date is scheduled in GRC platform"
        source_anchor: "OCC Bulletin 2026-13 §III.E; firm AI Governance Policy v1.0 §6.1"
    stop_conditions:
      - "No go-live without unanimous AIGC concurrence on T1 use case"
      - "No go-live without scheduled annual-review date"
      - "No go-live for AI-extended models without Model Risk Committee concurrence"
    escalation_path:
      escalation_committee: "Board Risk Committee (for T1 go-live; AIGC dissent or split vote escalates)"
      time_to_escalate: "Next Board Risk Committee meeting; emergency convening for material delay"
      escalation_owner: "AI Governance Committee Chair"
    documentation_requirement:
      - "Go-live decision in AIGC minutes with named attesters and any recorded dissents"
      - "Production-readiness assessment retained in GRC platform"
      - "Cross-reference to MRC minutes for AI-extended models"
    frequency: event-based
    source_anchor: "SR 11-7 §VI; OCC Bulletin 2026-13 §III.E and §III.F; references/source-anchors.md#occ-2026-13"

  - gate_id: GATE-AI-005
    gate_name: "Annual review gate"
    stage: ongoing-monitoring
    trigger: "Annual review date for any in-production AI use case (cadence per tier: T1 annual; T2 annual or 18-month per AIGC discretion; T3 every 24 months or on material change)"
    required_reviewers:
      - role: "Head of AI Governance"
        is_primary: true
      - role: "Independent Validator (refresh validation for T1)"
        is_primary: false
        independence_required: true
      - role: "Business Owner"
        is_primary: false
      - role: "CISO (refresh cyber review when applicable)"
        is_primary: false
    required_inputs:
      - "Production monitoring history since last review"
      - "Issue log against the use case"
      - "Refresh validation report (T1) or refresh assessment (T2/T3)"
      - "Updated model card with any material changes"
    decision_criteria:
      - criterion: "Use case continues to perform within established tolerances"
        source_anchor: "NIST AI RMF MEASURE/MANAGE; firm monitoring policy"
      - criterion: "No accumulated open critical or high issues unresolved"
        source_anchor: "references/source-anchors.md#sr-11-7"
      - criterion: "Use case continues to fit firm tiering classification (re-tier if necessary)"
        source_anchor: "references/firm-overlay.md#ai-tiering-v2"
    stop_conditions:
      - "No continued production if material drift in performance is unmitigated"
      - "No continued production with unresolved critical issues"
      - "Re-tier required if use case has materially changed since last review"
    documentation_requirement:
      - "Annual review decision in AIGC minutes"
      - "Refresh validation / assessment retained in GRC platform"
      - "Updated model card retained"
    frequency: annual
    frequency_detail: "Annual for T1 and T2 (T2 may extend to 18 months at AIGC discretion); 24-month or on-material-change for T3"
    source_anchor: "OCC Bulletin 2026-13 §III.E; NIST AI RMF MANAGE function; firm AI Governance Policy v1.0 §6.1"

gate_gaps:
  - implied_gate_name: "Annual review gate"
    gap_description: "Current workflow has no formal annual-review gate for in-production AI use cases. SR 11-7 §V (model validation refresh) and OCC Bulletin 2026-13 §III.E (refreshed effective challenge) imply periodic refresh; firm has been performing ad-hoc refresh on a use-case-by-use-case basis without a calendar mechanism."
    source_anchor: "references/source-anchors.md#sr-11-7; references/source-anchors.md#occ-2026-13"
    recommended_action: "Adopt GATE-AI-005 as drafted; populate annual-review schedule in GRC platform for all in-production AI use cases within 90 days of charter adoption."
  - implied_gate_name: "Third-party AI / vendor-AI gate"
    gap_description: "Current workflow does not separately gate vendor-provided AI use cases (vendor models, vendor-AI-extended platforms). NIST AI RMF GV-6 (third-party considerations) and OCC Bulletin 2026-13 §III.G (third-party model gate expectations) imply vendor-AI use cases require coordinated AIGC and Vendor Risk Committee gates."
    source_anchor: "references/source-anchors.md#nist-ai-rmf; references/source-anchors.md#occ-2026-13"
    recommended_action: "Add vendor-AI specific intake and onboarding gate that coordinates AIGC and VRC; align documentation cadence with TPRM ongoing-monitoring."

recommended_charter_language: |
  The AI Governance Committee (the Committee) is the firm's primary governance body for artificial intelligence use cases across the AI lifecycle from intake through retirement. The Committee operates with decision authority on use cases at all tier levels, with specific gating responsibility for tier-1 production go-live decisions.

  The Committee carries five named gates. Intake gates ensure every AI use case is registered with named line-1 ownership before development proceeds. Tiering gates classify use cases by impact, with the Committee's classification driving downstream gate intensity. Pre-production gates apply to tier-1 and tier-2 use cases and require complete model documentation, independent validation, and (where applicable) cyber and privacy concurrence before any production deployment. Tier-1 production go-live gates require unanimous Committee concurrence with a scheduled annual-review date in the firm's governance system; tier-1 dissents escalate to the Operational Risk Committee with onward escalation to the Board Risk Committee at the Chair's discretion. Annual review gates apply to in-production use cases with cadence by tier and are the mechanism through which the Committee maintains effective challenge over the production AI portfolio.

  For AI-extended models, the Committee coordinates with the Model Risk Committee with both committees concurring on tier-1 production go-live. The Committee reports to the Board Risk Committee annually on the AI use-case portfolio, the gate-decision history, and any material exceptions or dissents. The Committee's gate decisions are documented in the meeting minutes with named attesters and any recorded dissents; documentation is retained in the firm's governance system per the firm's records-retention schedule.

reviewer_questions:
  - "Should the AIGC and the Model Risk Committee adopt joint quorum requirements for AI-extended-model T1 go-live decisions, or is sequential sign-off sufficient?"
  - "For T2 use cases, is annual review the right cadence or should the firm adopt an 18-month cadence with on-material-change triggers as the default?"
  - "Does the firm need to separately stand up a third-party AI gate as recommended in the gap section, or is the existing Vendor Risk Committee sufficient with a charter amendment that flags vendor-AI as a distinct category?"
  - "Where the AIGC has Chief Privacy Officer concurrence required, is the CPO function staffed at sufficient stature to act as a true independent reviewer, or does this need a structural lift before charter adoption?"

confidence_label: medium
human_review_required: true
```

#### What the matrix surfaces

- **Five distinct gates with real spine**. Intake, tiering, pre-prod, go-live, annual review. Each has a real trigger, named reviewers with independence flagged where source guidance demands, declarative stop conditions, and named documentation. Not ten gates padded for comprehensiveness.
- **Tier-driven gate intensity**. T1 use cases hit all five gates; T2 skips the formal go-live committee gate but still hits pre-prod and annual review; T3 skips pre-prod but is annual-reviewed at lighter cadence. The matrix encodes the firm's risk-based proportionality.
- **Validator independence on AI-extended models**. The independence_required flag fires on the Independent Validator slot at pre-prod and annual review, with the source anchor citing SR 11-7 §V and the firm's AI Governance Policy. The matrix names the structural separation explicitly.
- **MRC coordination without committee collapse**. AI-extended models flow through both the AIGC and the MRC; the matrix names the coordination without collapsing the two committees. The gap section does not flag this as a redundancy because the AIGC's scope is broader (non-model AI) and the MRC's scope is narrower (model risk).
- **Cyber overlay firing on customer-data use cases**. The CISO is named as a required reviewer at pre-prod and annual review when the cyber overlay is loaded; the source anchor cites the cyber overlay file path.
- **Real gap surfaced**. The annual-review gate is implied by source guidance but does not exist in the firm's current workflow; the gap is explicit with the source anchor and the recommended action. A clean-looking matrix with no gap usually means the gap was buried.
- **Recommended charter language as adoptable prose**. Three paragraphs that read as charter language, not as matrix commentary. The committee can adopt the language directly into its terms of reference.
- **Reviewer questions that point to live decisions**. Joint quorum, T2 cadence, third-party AI gate, CPO stature. Each question points to a specific decision the committee will need to make.

#### Downstream uses

- `model-card-builder` references GATE-AI-003 (pre-prod) and GATE-AI-004 (T1 go-live) in the model card's sign-off block; T1 model cards trace through both AIGC and MRC.
- `vendor-diligence` references the third-party-AI gap and (post-remediation) the vendor-AI specific gate.
- `risk-committee-pack` for the next AIGC reads GATE-AI-005 (annual review) and surfaces overdue annual reviews; for the next Board Risk Committee reads the AIGC quarterly summary and flags any T1 dissent escalations.
- `issue-writeup` for any issue against an AI use case links to the relevant gate via the issue's linked-control-id, and the issue's severity drops the use case's "current effective challenge" rating until closure.

## troubleshooting

### Troubleshooting: human-review-gates

Recurring failure modes when a gate matrix looks complete but is not. The reviewer pass should catch these; the builder pass should preempt them.

#### 1. One committee owns everything

Symptom: the same committee owns intake, tiering, pre-prod, go-live, ongoing monitoring, and retirement. The decision-authority block reads as a single committee with no escalation path.

Why it happens: the firm has not yet stood up the differentiated governance the source guidance assumes. Smaller firms run with one committee out of pragmatism; larger firms accumulate gates onto an existing committee without splitting.

Fix: a single committee owning the full lifecycle is one committee, not a gate matrix. The matrix's `gate_gaps` section flags this with the specific source-guidance citation that implies separation (Heightened Standards Standard II for line-1/line-2 separation; SR 11-7 §V/§VI for developer/validator separation; Interagency TPRM §III for TPRM-lifecycle differentiation). The recommended action either splits the committee, names sub-committees with charter clarity, or defines an escalation path through which one committee's decisions are reviewed by another. One committee is acceptable when the firm's scale genuinely fits it; one committee with no escalation is not.

#### 2. Stop conditions that are not stops

Symptom: stop conditions read "should be reviewed", "consider whether", "as appropriate", or "review for completeness". The gate's decision criteria are advisory rather than declarative.

Why it happens: the practitioner is uncomfortable with binary stops because real production decisions involve judgement, and writing a binary stop feels rigid.

Fix: stop conditions are declarative and binary. "No go-live if any open critical or high issue against the use case" is a stop. "Should be reviewed for open issues" is not. The gate's decision criteria carry the judgement (the criteria are evaluated by the named reviewers); the stop conditions are the binary blockers that fire when criteria fail. If the gate genuinely has no binary stops, the gate is advisory, not gating; the matrix's gap section flags this and recommends adding declarative stops.

#### 3. Required reviewers are committees, not roles

Symptom: required_reviewers reads "Risk Committee", "Compliance Function", or "Senior Management" without naming individual roles.

Why it happens: the engagement has not yet specified which named roles within the committee carry the decision; the practitioner writes the committee name as a placeholder.

Fix: the required reviewers are named roles. "Head of Model Risk Management", "Independent Validator", "CISO", "Chief Compliance Officer", "Business Sponsor", "General Counsel". Where the gate is a committee-level decision (the AI Governance Committee renders the T1 go-live decision), the matrix can name the committee as the decision authority but still name the required individual roles whose attestation forms the committee record. Pure committee-named reviewers without role-named members fail the audit-trace test; an examiner cannot tell who attested.

#### 4. Independence flag missing where source guidance demands it

Symptom: a model-risk gate has no `independence_required` flag on the validator slot; a third-party gate has no independence flag on the line-2 reviewer; an audit-committee gate has no independence flag on the audit committee.

Why it happens: the matrix builder did not yet pull the source-anchor file into the construction; independence is a per-reviewer attribute that is easy to miss at first pass.

Fix: every gate's required_reviewers list is reviewed against the source anchor. SR 11-7 §V demands validation independence from development. Interagency TPRM §III.B demands line-2 independence on critical-vendor due diligence. EU AI Act Article 14 demands competent oversight by persons with authority. NAIC Model Audit Rule demands audit committee member independence. Where the source guidance demands independence, the `independence_required` field is true and `independence_basis` cites the source. The check is mechanical; the source-anchors file enumerates the demands.

#### 5. Required inputs read as "what is available"

Symptom: required_inputs reads "review what's available", "current state of the artifact", or "any relevant documentation".

Why it happens: the matrix builder is uncertain what artifacts will be available at the gate, or wants to leave room for flexibility.

Fix: required inputs are named artifacts, by ID where the artifact is a structured record produced by a sibling skill (model card from `model-card-builder`, validation report from `validation-report` or model-validator equivalent, due-diligence pack from `vendor-diligence`, issue write-up from `issue-writeup`, exit plan from `exit-plan`). Where the artifact is a regulatory deliverable, name the deliverable (SOC 2 Type II report, attestation letter, supervisor-correspondence record). Flexibility is fine on the artifact's content; the gate is firm on its presence.

#### 6. Documentation requirement reads as "minutes"

Symptom: documentation_requirement reads "minutes" or "noted" without naming what gets captured.

Why it happens: minute-taking discipline varies; the matrix builder is unsure what the firm's minutes actually carry.

Fix: documentation requirement names what gets captured: the decision (pass or fail / conditional), the rationale, the named attesters, the date, the artifact references, and the system of record that holds the record. "Minutes" is acceptable when the firm's minute discipline is robust and the minutes name attesters and decisions; it is not acceptable when the minutes are summary-only. The matrix's documentation requirement carries the granularity needed for the named system of record (board portal, GRC platform, regulator filing). For board-committee gates, named attesters and recorded dissents are explicit; for line-2 committee gates, the GRC-platform record is named.

#### 7. Frequency conflated with cadence

Symptom: frequency is set to "annual" but the gate is actually event-based (fires when a use case reaches that lifecycle stage); or frequency is "event-based" but the gate is actually periodic (fires on a calendar regardless of use cases moving through the workflow).

Why it happens: practitioners conflate the gate's firing pattern with the gate's review cadence.

Fix: frequency is event-based or periodic, with the periodic gate naming the cadence (daily, weekly, monthly, quarterly, annual). A gate that fires on go-live is event-based; a gate that fires on the annual review cycle for in-production use cases is annual. Some workflows have both: a use case has an event-based pre-prod gate (fires once when the use case is ready) and an annual review gate (fires every year while the use case is in production). The matrix carries them as two distinct gates with distinct frequencies.

#### 8. Recommended charter language reads as matrix commentary

Symptom: the recommended_charter_language section is a bulleted list of gate-matrix observations rather than charter prose.

Why it happens: the matrix builder uses the same voice for the matrix and the charter language; the charter is a different artifact with a different audience.

Fix: charter language reads as committee charter prose: declarative, named, committee-voice. Three paragraphs typically: (1) the committee's purpose and decision authority; (2) the gate sequence and stop-condition discipline; (3) the escalation, dissent, documentation, and reporting cadence. The charter language is the language the committee adopts; the matrix is the operational reference. Voice shift; not a copy of the matrix bullets.

#### 9. Gap section is empty

Symptom: gate_gaps is an empty array.

Why it happens: the matrix builder has not stress-tested the matrix against the source-guidance expectations, or has buried gaps in narrative commentary.

Fix: a clean-looking matrix with no gaps usually means the gaps were buried. Stress-test the matrix: does every source-guidance gate have a corresponding matrix gate? Does every reviewer-independence demand have a flag? Does every gate have stop conditions? Does the workflow have an annual-review gate where the source guidance implies one? Does the workflow have a termination / exit gate where the source guidance demands one? The gap section names the implied gates that are missing or under-specified; if the gap section is empty after stress-testing, it stays empty, but the test should run.

#### 10. Validator-as-developer (or equivalent) buried in role overlap

Symptom: the matrix names "Independent Validator" as a required reviewer but the firm's actual organizational structure has the validator role reporting to the developer's chain.

Why it happens: the matrix is constructed against the source guidance without reconciling against the firm's current role assignments. The gate matrix says "independent validator"; the firm's reality is that the only validator is in the development team.

Fix: the matrix names independence as a structural requirement; the gap section flags any current organizational reality that fails the requirement. SR 11-7 demands developer/validator independence; if the firm's current state does not satisfy this, the gate is gating on a fiction. The matrix surfaces the structural-independence gap, recommends a structural fix (separate validator role, third-party validation, or escalation to model-risk function outside development), and notes that the gate is not yet operationally enforceable until the structural gap closes.

#### 11. SAR / regulator-filing gates without BSA Officer or compliance-officer attestation

Symptom: a SAR-filing gate or regulator-filing gate names a committee or general role as the decision-holder without naming the BSA Officer (for SAR) or the named compliance officer (for other regulator filings) as the attester.

Why it happens: SAR and regulator-filing gates often inherit a generic "compliance approval" framing rather than naming the regulatory-officer-of-record.

Fix: SAR-filing gates name the BSA Officer as the attester (FinCEN BSA program-officer requirement). Regulator-filing gates name the compliance officer or general counsel of record. The decision criteria reference the BSA Officer's attestation as the regulator-recognised sign-off. The documentation requirement names the SAR record, the BSA Officer attestation, and the FinCEN filing record.

#### 12. The matrix tries to be the runbook

Symptom: the matrix runs to many pages of process detail (how the gate fires operationally, who hands off to whom, what the screen-share looks like in the meeting).

Why it happens: the matrix builder is documenting the gate as a process rather than as a decision architecture.

Fix: the matrix is the gate-decision architecture. The runbook is downstream, the operational documentation that names how the gate fires day-to-day. The matrix names the gate, the trigger, the reviewers, the criteria, the stop conditions, the escalation, the documentation, the frequency, the source. The runbook (or the firm's GRC platform workflow) carries the operational detail. Cross-reference the runbook in the firm-overlay; do not pull the runbook into the matrix.

#### 13. The matrix stops too late

Symptom: the skill produces a matrix asserting committee adoption, charter language signed off, and decision authority finalized, without the named reviewer having attested.

Why it happens: builder over-runs the human-review gate.

Fix: gate architecture is committee-adopted; the skill stops at draft. The matrix is a draft until the named reviewer attests. The `human_review_required` field is always true; committee adoption is the named gate (the gate matrix's own meta-gate). The skill surfaces reviewer questions and recommended charter language; it does not assert sign-off, distribute, or post the matrix as adopted.
