# Example: pre-launch UDAAP review of an instant-funding tip-fee mechanic on a personal-loan product

## Input

A fintech consumer-credit platform is launching an "instant funding" feature on its personal-loan product. The product is offered through a sponsor-bank arrangement; the bank is the creditor of record. The application page presents an APR that does not include the instant-funding fee. After approval, the consumer reaches a funding-selection step where two options are presented: standard funding (free, 1-3 business day ACH) and instant funding (presented as a "tip" or fee, debited from the loan disbursement). The instant-funding fee is disclosed at the funding-selection step but not on the application page; the APR shown on the application page is the same regardless of which funding option the consumer selects. The marketing copy emphasises "no hidden fees" and the speed of instant funding.

The fintech's product committee has scheduled a launch decision in three weeks. The sponsor bank's consumer-compliance officer (second-line) is asked to produce a UDAAP review memo for the joint product committee read. Source posture is public-plus-firm-policy-plus-evidence; sponsor-bank counsel directs the review for privilege.

## Why this scenario matters

This is a recurring fintech UDAAP fact pattern flagged in CFPB enforcement themes on instant-funding tips and fees. The sequencing of disclosure (APR at application; funding fee at funding-selection step) and the consumer-journey design (instant funding presented at a moment of high consumer commitment) implicate all three element prongs. The memo has to handle the bank-fintech split (sponsor-bank attribution; joint review and joint approval) and the AI-block (the funding-selection step uses a personalisation engine that varies the friction on the slow-funding option based on observed consumer behavior).

## Output sketch

```yaml
review_id: UDAAP-2026-FT-PL-IF-01
trigger: pre-launch-gate
as_of_date: 2026-05-06

scope:
  in_scope_subject: "Instant-funding fee mechanic on the personal-loan product, including the funding-selection step UI and the relationship between the application-page APR and the post-approval funding-fee disclosure."
  subject_type: customer-experience-flow
  period: {start: 2026-05-01, end: 2026-08-31}
  channels: [digital-direct]
  population: "All approved personal-loan applicants who reach the funding-selection step. Estimated 40,000 to 70,000 applicants per quarter at projected volume."
  exclusions:
    - Underwriting decisioning (separate fair-lending-test-plan review)
    - Servicing fee mechanics (out of scope this cycle)
    - Adverse-action notice content (separate adverse-action-review)

reviewer_posture:
  reviewer_role: sponsor-bank-consumer-compliance-officer
  review_independence: independent-second-line
  counsel_directing: true

legal_privilege_posture: attorney-client-privileged

evidence_base:
  - {source: "Application-page mockups and live-test recordings", type: marketing-asset, date: 2026-04-22, completeness_flag: complete}
  - {source: "Funding-selection-step UI specifications and live-test recordings", type: marketing-asset, date: 2026-04-22, completeness_flag: complete}
  - {source: "Personalisation-engine model card MC-IF-PERSONALIZE-v1", type: model-card, date: 2026-04-15, completeness_flag: partial}
  - {source: "Sponsor-bank product-launch policy, section 4.3 (UDAAP review gate)", type: policy-text, date: 2025-11-01, completeness_flag: complete}
  - {source: "CFPB Circulars 2022-04 and 2022-06 (junk-fee and overdraft framings) and Supervisory Highlights coverage of instant-funding fees", type: regulatory-anchor, date: 2024-09-30, completeness_flag: partial}

deception:
  representation_or_omission: >
    The application-page APR represents the cost of credit but does not include the
    instant-funding fee that is presented at funding-selection. The marketing copy
    emphasises "no hidden fees" while structurally placing the funding fee outside
    the cost-of-credit framing on the application page.
  likely_to_mislead: yes
  reasonable_consumer_basis: >
    A reasonable consumer reaching the funding-selection step has already received
    the application-page APR as the represented cost of credit. The instant-funding
    fee is functionally part of the cost of credit (it is debited from the loan
    disbursement) but is presented separately. The "no hidden fees" framing
    reinforces the consumer's expectation that the application-page APR is
    inclusive.
  materiality: material
  materiality_rationale: >
    A reasonable consumer would consider the funding-fee material to the decision
    to take the loan; the fee can equal 5 to 15 percent of small-balance
    disbursements at the projected fee schedule.
  evidence_pointers: [application-page mockups, funding-selection-step recordings, marketing copy library]

unfairness:
  substantial_injury:
    injury_type: "Cost-of-credit obscuration; consumer pays a fee not represented in the APR."
    magnitude_per_consumer: "Fee schedule: 5 to 15 percent of disbursement; mean estimate 8 percent at projected take-rate."
    magnitude_aggregate: "Projected aggregate fee revenue $X to $Y per quarter at the projected take-rate; aggregate consumer-cost equal."
    population_estimate: "All approved applicants electing instant funding; projected take-rate 60 to 75 percent."
    population_evidence_flag: evidenced
  reasonably_avoidable: indeterminate
  reasonably_avoidable_analysis: >
    The slow-funding alternative is functionally available but the funding-selection
    UI structurally de-emphasises it. The personalisation engine adjusts the friction
    on the slow-funding option based on observed consumer behavior; reasonable
    avoidability turns on whether the slow-funding alternative is symmetrically
    presented. As currently specified, the symmetry is not present; the analysis
    pivots on whether the firm restores symmetric presentation before launch.
  countervailing_benefits:
    first_line_assertion: >
      Instant funding provides genuine speed value for consumers with urgent funding
      needs; the fee is the price of the speed and consumers can elect not to pay it.
    reviewer_assessment: >
      The benefit is real but the unfairness analysis is not dispositive on the
      benefit; it is dispositive on the relationship between the represented APR
      and the actual cost of credit and on the symmetry of the alternative.
    outweighs_injury: no
  evidence_pointers: [funding-selection-step recordings, personalisation-engine card, projected fee schedule]

abusiveness:
  applicability: applicable
  applicability_rationale: >
    The funding-selection step is reached at a moment of high consumer commitment
    (the application has been approved; the consumer is in active funding mode).
    The personalisation-engine variation in the slow-funding friction can be read
    as material interference with the consumer's ability to understand the cost
    structure.
  material_interference:
    description: >
      The application-page APR sets the consumer's expectation of the cost of
      credit; the funding-selection step introduces a fee that is functionally
      part of the cost of credit but presented as a separate "tip" or "fee".
      The personalisation engine adjusts the friction on the slow-funding
      alternative; consumers in segments where the engine increases the friction
      may experience material interference with the choice architecture.
    evidence: "Personalisation-engine card MC-IF-PERSONALIZE-v1; UI specifications for the funding-selection step."
  unreasonable_advantage:
    type: lack-of-understanding
    evidence: >
      The consumer's understanding of the cost of credit at the funding-selection
      step is anchored to the application-page APR. The funding fee is not
      anchored to that representation. The personalisation engine takes
      advantage of this mismatch by varying the friction on the alternative.

consumer_harm:
  population: "All approved applicants reaching the funding-selection step (projected 40,000 to 70,000 per quarter)."
  population_evidence_flag: evidenced
  magnitude: "Per consumer: 5 to 15 percent of disbursement; aggregate: $X to $Y per quarter at projected take-rate."
  frequency: one-time per loan
  redress_posture: "Pre-launch; redress not yet implicated. Post-launch, redress would be plausible if the launch goes through with the current structure and the bureau opens an inquiry."

ai_algorithmic_findings:
  ai_in_path: true
  model_inventory:
    - model_id: MC-IF-PERSONALIZE-v1
      version: 1.0.0
      decision_use: friction-personalisation-on-slow-funding
      ai_ml: true
      vendor_or_inhouse: in-house
      validation_status: in-validation
      card_reference: MC-IF-PERSONALIZE-v1
  udaap_theory: >
    The unfairness prong applies on the algorithmic outcome (the personalisation
    engine adjusts the slow-funding friction in a way that materially affects
    reasonable-avoidability of the instant-funding fee). The abusiveness prong
    applies on the material-interference and the lack-of-understanding analysis.
    The April 2023 Joint Statement is cited as the cross-agency anchor for
    reaching the algorithmic outcome under existing UDAAP authority.
  joint_statement_cite: true
  fair_lending_cross_reference: true

severity: high
severity_per_element:
  deception: high
  unfairness: high
  abusiveness: medium
severity_rationale: >
  Deception: high because the application-page APR representation is materially
  inconsistent with the actual cost of credit at the funding-selection step.
  Unfairness: high because the population and magnitude are large and the
  reasonably-avoidable analysis turns on a UI design choice that is currently
  asymmetric. Abusiveness: medium because the material-interference analysis is
  supported but not dispositive without the personalisation-engine evidence
  developed further. Aggregate: high. Pattern matches a Supervisory Highlights
  focal item; remediation needed within one committee cycle. Pre-launch is the
  cycle.

conduct_risk_implications:
  taxonomy_tie_back: [product-design, communication, customer-outcome, ai-algorithmic-surface]
  conduct_accountable_manager_role: head-of-consumer-credit (sponsor-bank-side); head-of-product (fintech-side)
  conduct_committee_read: true
  conduct_event_candidate: false
  customer_outcome_segments_affected: [low-balance-borrowers, urgent-need-borrowers]
  regulator_engagement_trigger: ""
  complaint_monitoring_loop_closure: >
    Post-launch, monitor CFPB-portal complaints in the "personal-loan fee" and
    "personal-loan disclosure" buckets, plus app-store review patterns, plus
    firm-direct complaints in the "funding fee" bucket. Trigger an off-cycle
    UDAAP re-review at any one of: 25 percent quarter-over-quarter increase
    in any of those buckets; a CFPB inquiry; a peer enforcement action on an
    analogous fact pattern.

recommended_remediation:
  - action: "Restructure the application-page APR to include the instant-funding fee in the cost-of-credit math (or add a disclosed alternative APR for the instant-funding path)."
    type: disclosure-change
    owner: head-of-product (fintech-side)
    due_date: 2026-06-30
    accountable_forum: joint product committee (sponsor-bank and fintech)
  - action: "Re-design the funding-selection-step UI so the slow-funding default is symmetric with instant funding (visual weight; default state; CTA placement)."
    type: control-change
    owner: head-of-product (fintech-side)
    due_date: 2026-06-30
    accountable_forum: joint product committee
  - action: "Pause or constrain the personalisation engine on the funding-selection step until the LDA-search analysis (separate fair-lending-test-plan) completes."
    type: model-change-candidate
    owner: head-of-ML
    due_date: 2026-07-15
    accountable_forum: sponsor-bank fair-lending committee; fintech AI risk committee
  - action: "Marketing review on the 'no hidden fees' copy across all assets where the instant-funding fee is in scope."
    type: marketing-takedown-candidate
    owner: head-of-marketing-compliance
    due_date: 2026-06-15
    accountable_forum: marketing-compliance committee (cross-reference marketing-claim-review)
  - action: "Post-launch monitoring uplift on the four named complaint buckets with a quarterly read to the conduct committee."
    type: monitoring-uplift
    owner: head-of-complaints
    due_date: 2026-09-30
    accountable_forum: conduct committee

open_questions:
  - "Whether sponsor-bank counsel directs the LDA-search work product as joint-defense under the program agreement."
  - "Whether a state AG enforcement angle is plausible on the disclosure-and-fee mechanic in any of the program states; coordinate with state-licensure compliance."
  - "Whether the credit-card late-fee rule litigation outcome materially changes the bureau's posture on adjacent junk-fee fact patterns and what (if anything) that means for this memo."

cross_references: [complaint-theme-analysis, marketing-claim-review, fair-lending-test-plan, model-card-builder]

decision_forum:
  named_forum: joint sponsor-bank product committee and fintech product committee
  decision_status: submitted
  decision_date: ""
  conditions: []

assumptions_and_dependencies:
  - "Sponsor-bank counsel directs the review for the duration; privilege posture as marked."
  - "Personalisation-engine card MC-IF-PERSONALIZE-v1 is the operative governance artifact; in-validation status flagged."
  - "Projected fee revenue and take-rate are first-line estimates; second-line has not independently validated; flag for monitoring uplift."

confidence_label: medium
```

## What this memo does and does not do

The memo operationalizes the pre-launch UDAAP review for the joint product committee. It does not finalize a UDAAP determination, approve or block the launch, take down any marketing asset, change any disclosure, or trigger any external action. The joint product committee (sponsor bank and fintech) decides on the recommended remediation; the conduct committee gets a read; the fair-lending committee receives the cross-referenced LDA-search request through `fair-lending-test-plan`; the marketing-compliance committee receives the asset-level review request through `marketing-claim-review`.

The element analysis covers all three prongs because UDAAP is three elements; over-indexing on deception (the easiest to evidence with marketing artifacts) would miss the unfairness analysis on the population and magnitude and the abusiveness analysis on the material-interference of the personalisation engine.

Pattern derived from public CFPB enforcement themes on instant-funding tips and fees and from the general junk-fee framing in the bureau's policy posture. No named institution is implied; the bank-fintech program structure and the funding-selection-step design are the structural patterns, not a specific firm.
