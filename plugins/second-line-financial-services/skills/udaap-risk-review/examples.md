# Examples and troubleshooting

One section per worked example, then troubleshooting. Read only what you need.

## instant-funding-tip-fee

### Example: pre-launch UDAAP review of an instant-funding tip-fee mechanic on a personal-loan product

#### Input

A fintech consumer-credit platform is launching an "instant funding" feature on its personal-loan product. The product is offered through a sponsor-bank arrangement; the bank is the creditor of record. The application page presents an APR that does not include the instant-funding fee. After approval, the consumer reaches a funding-selection step where two options are presented: standard funding (free, 1-3 business day ACH) and instant funding (presented as a "tip" or fee, debited from the loan disbursement). The instant-funding fee is disclosed at the funding-selection step but not on the application page; the APR shown on the application page is the same regardless of which funding option the consumer selects. The marketing copy emphasises "no hidden fees" and the speed of instant funding.

The fintech's product committee has scheduled a launch decision in three weeks. The sponsor bank's consumer-compliance officer (second-line) is asked to produce a UDAAP review memo for the joint product committee read. Source posture is public-plus-firm-policy-plus-evidence; sponsor-bank counsel directs the review for privilege.

#### Why this scenario matters

This is a recurring fintech UDAAP fact pattern flagged in CFPB enforcement themes on instant-funding tips and fees. The sequencing of disclosure (APR at application; funding fee at funding-selection step) and the consumer-journey design (instant funding presented at a moment of high consumer commitment) implicate all three element prongs. The memo has to handle the bank-fintech split (sponsor-bank attribution; joint review and joint approval) and the AI-block (the funding-selection step uses a personalisation engine that varies the friction on the slow-funding option based on observed consumer behavior).

#### Output sketch

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

#### What this memo does and does not do

The memo operationalizes the pre-launch UDAAP review for the joint product committee. It does not finalize a UDAAP determination, approve or block the launch, take down any marketing asset, change any disclosure, or trigger any external action. The joint product committee (sponsor bank and fintech) decides on the recommended remediation; the conduct committee gets a read; the fair-lending committee receives the cross-referenced LDA-search request through `fair-lending-test-plan`; the marketing-compliance committee receives the asset-level review request through `marketing-claim-review`.

The element analysis covers all three prongs because UDAAP is three elements; over-indexing on deception (the easiest to evidence with marketing artifacts) would miss the unfairness analysis on the population and magnitude and the abusiveness analysis on the material-interference of the personalisation engine.

Pattern derived from public CFPB enforcement themes on instant-funding tips and fees and from the general junk-fee framing in the bureau's policy posture. No named institution is implied; the bank-fintech program structure and the funding-selection-step design are the structural patterns, not a specific firm.

## overdraft-apsn-annual-refresh

### Example: annual UDAAP refresh on a regional bank's deposit-overdraft program with APSN findings

#### Input

A $40B regional bank operates a deposit-overdraft program for its consumer checking accounts. The program covers debit-card and ACH transactions; consumers opt in to debit-card overdraft per Reg E §1005.17. The bank's overdraft fee is $35 per item; daily max is 4 items. The bank's annual UDAAP refresh on the deposit-overdraft program is in cycle. Annual transaction-data analysis surfaces an authorize-positive-settle-negative (APSN) pattern: 11 percent of overdraft fees in the prior 12 months were assessed on transactions that were authorized when the available balance was sufficient but settled (and overdrew) after intervening transactions. The complaint-management system shows a cluster of "surprise overdraft" complaints across three of the bank's footprint states.

The CCO and the head of consumer compliance are jointly sponsoring the review. Source posture is public-plus-firm-policy-plus-evidence; the bank has core-banking-system transaction data, account-disclosure documents, complaint records, branch and call-center recordings, and the most recent two CFPB Supervisory Highlights issues. Outside counsel directs the review for privilege.

#### Why this scenario matters

This is the canonical CFPB Circular 2022-06 (Unanticipated Overdraft Fee Assessment Practices) fact pattern. The bureau has been explicit that APSN fees can violate the unfairness prong of CFPA §1031 because consumers cannot reasonably anticipate the fee at the moment of the transaction. The annual refresh has to handle population-and-magnitude analysis (the 11 percent figure plus the aggregate fee-revenue exposure), conduct-risk implications (the bank's overdraft-fee revenue contribution; branch incentive design), and remediation framing (consumer redress for the affected fee population in the lookback period; control change to detect and prevent APSN at posting).

#### Output sketch

```yaml
review_id: UDAAP-2026-DEP-OD-ANN-01
trigger: annual-refresh
as_of_date: 2026-05-06

scope:
  in_scope_subject: "Deposit-overdraft program for consumer checking accounts, including the APSN pattern surfaced by annual transaction-data analysis and the surprise-overdraft complaint cluster in three footprint states."
  subject_type: product
  period: {start: 2025-04-01, end: 2026-03-31}
  channels: [branch, digital, call-center]
  population: "All consumer checking accountholders subject to the overdraft program in the period (approximately 1.8 million accounts; 11 percent APSN concentration on the overdraft-fee subset)."
  exclusions:
    - Commercial overdraft programs (separate review)
    - Reg E §1005.17 opt-in compliance review (covered under the regular Reg E compliance program)
    - Mortgage-servicing fee analysis (separate scope)

reviewer_posture:
  reviewer_role: head-of-consumer-compliance
  review_independence: independent-second-line
  counsel_directing: true

legal_privilege_posture: attorney-client-privileged

evidence_base:
  - {source: "Core-banking transaction data (overdraft and NSF assessment patterns), 2025-04-01 to 2026-03-31", type: transaction-data, date: 2026-04-15, completeness_flag: complete}
  - {source: "Account-disclosure document (deposit account agreement, fee schedule)", type: policy-text, date: 2026-01-15, completeness_flag: complete}
  - {source: "Complaint records (CFPB-portal and firm-direct), 2025-04-01 to 2026-03-31", type: complaint-data, date: 2026-04-30, completeness_flag: complete}
  - {source: "Branch and call-center call recordings sampled on overdraft-related interactions", type: call-recording, date: 2026-04-22, completeness_flag: partial}
  - {source: "CFPB Circular 2022-06 (Unanticipated Overdraft Fee Assessment Practices)", type: regulatory-anchor, date: 2022-10-26, completeness_flag: complete}
  - {source: "CFPB Supervisory Highlights (most recent two issues at memo date)", type: supervisory-highlights-issue, date: 2026-03-31, completeness_flag: complete}
  - {source: "Branch incentive design (overdraft education, account-opening incentives) policy text", type: policy-text, date: 2025-11-15, completeness_flag: complete}

deception:
  representation_or_omission: >
    The deposit account agreement discloses that overdraft fees apply when an
    account is overdrawn at posting. The branch and call-center scripts reinforce
    the same representation: an overdraft fee applies when the consumer overdrafts
    the account. The APSN fact pattern is not represented to consumers; consumers
    are not told that a transaction authorized on a positive available balance
    can later trigger an overdraft fee at settlement.
  likely_to_mislead: yes
  reasonable_consumer_basis: >
    A reasonable consumer reading the disclosure and hearing the branch
    explanation understands "overdraft fee when you overdraft" to mean a fee on
    transactions that the consumer would, at the time of the transaction,
    recognize as overdrawing the account. The APSN pattern departs from that
    understanding.
  materiality: material
  materiality_rationale: >
    A reasonable consumer would consider the difference between fee-on-overdraft
    and fee-on-APSN material to the decision to opt in to the overdraft program
    and to the consumer's transaction behavior.
  evidence_pointers: [account-disclosure document, branch and call-center scripts, complaint records on "surprise overdraft"]

unfairness:
  substantial_injury:
    injury_type: "Per-fee dollar value times the population and frequency. APSN fees are functionally surprise fees that consumers cannot anticipate."
    magnitude_per_consumer: "$35 per item; daily max 4 items. Mean APSN consumer in the period: $X aggregate fees over the period (specific to the affected subset)."
    magnitude_aggregate: "$Y in the lookback period (11 percent of total overdraft-fee revenue subject to APSN classification)."
    population_estimate: "Affected accountholders: approximately 80,000 to 110,000 in the lookback period (the subset of overdraft-fee-paying accountholders with at least one APSN-classified fee)."
    population_evidence_flag: evidenced
  reasonably_avoidable: no
  reasonably_avoidable_analysis: >
    The consumer cannot anticipate the authorization-vs-settlement timing on an
    individual transaction; the fact pattern depends on intervening transactions
    that the consumer may not have visibility into at the moment of the relevant
    transaction. The Reg E §1005.17 opt-in covers debit-card overdraft generally
    but does not surface the APSN sequence specifically. CFPB Circular 2022-06
    is on point.
  countervailing_benefits:
    first_line_assertion: >
      The overdraft program provides liquidity to consumers; the APSN subset is
      a small fraction of the overall program; the program covers consumer
      transactions that would otherwise be declined.
    reviewer_assessment: >
      The countervailing-benefits framing addresses the overdraft program
      generally, not the APSN subset specifically. The benefits accrue to the
      program; the injury accrues to the APSN subset. The two do not net.
    outweighs_injury: no
  evidence_pointers: [transaction-data analysis on APSN, CFPB Circular 2022-06, complaint records]

abusiveness:
  applicability: applicable
  applicability_rationale: >
    The APSN pattern materially interferes with the consumer's ability to
    understand the operative term (when an overdraft fee applies). The unreasonable-
    advantage analysis is supportable on the lack-of-understanding prong.
  material_interference:
    description: >
      The disclosure represents fees on overdraft; the operative practice
      assesses fees on a sequence the consumer cannot observe (authorization
      vs. settlement timing relative to intervening transactions). The
      mismatch is structural and not curable by the consumer.
    evidence: "Account-disclosure document; transaction-data analysis showing the APSN sequence."
  unreasonable_advantage:
    type: lack-of-understanding
    evidence: "Complaint records repeatedly surface 'I had money in the account when I made the purchase'; the consumer's understanding of the operative term is anchored to the moment of the transaction."

consumer_harm:
  population: "Approximately 80,000 to 110,000 accountholders affected in the lookback period (per transaction-data analysis)."
  population_evidence_flag: evidenced
  magnitude: "Aggregate APSN fees: $Y in the period (11 percent of overdraft-fee revenue). Per consumer: variable; mean $Z per affected consumer per period."
  frequency: recurring
  redress_posture: >
    Consumer redress is plausible at the population scale (refund of APSN fees in
    the lookback period). The bureau's framing in Circular 2022-06 supports a
    redress posture; peer consent orders on analogous fact patterns set redress
    benchmarks at one to three years of fees plus interest.

ai_algorithmic_findings:
  ai_in_path: false

severity: critical
severity_per_element:
  deception: high
  unfairness: critical
  abusiveness: high
severity_rationale: >
  Aggregate severity: critical. The APSN pattern matches a CFPB Circular fact
  pattern directly (Circular 2022-06); the population is large; the aggregate
  consumer harm is substantial; the bureau has prosecuted analogous patterns;
  remediation cannot wait for the next committee cycle. Per element: deception
  high (the disclosure-vs-practice mismatch is clear); unfairness critical (the
  CFPB Circular is on point and the elements all support the prong); abusiveness
  high (material interference is supported; the unreasonable-advantage analysis
  on lack-of-understanding is supported).

conduct_risk_implications:
  taxonomy_tie_back: [product-design, communication, customer-outcome, complaint-linkage, incentives]
  conduct_accountable_manager_role: head-of-deposit-products
  conduct_committee_read: true
  conduct_event_candidate: true
  customer_outcome_segments_affected: [low-balance-checking-accountholders, frequent-debit-card-users]
  regulator_engagement_trigger: ""
  complaint_monitoring_loop_closure: >
    Post-remediation monitoring on the "surprise overdraft" complaint code, the
    "overdraft fee disputed" complaint code, and the CFPB-portal flow on overdraft
    complaints. Quarterly read to the conduct committee. Off-cycle re-review
    trigger at any one of: complaint-rate trend not flat after remediation
    cycle 2; CFPB inquiry on the program; peer enforcement on an analogous
    APSN fact pattern.

recommended_remediation:
  - action: "Pause the APSN fee-assessment pattern; re-route APSN-classified fees to non-fee disposition in the core-banking system."
    type: control-change
    owner: head-of-deposit-operations
    due_date: 2026-06-30
    accountable_forum: consumer compliance committee; CCO
  - action: "Consumer-redress program for APSN-classified fees in the lookback period (April 2025 to March 2026 plus extension to one prior year if scoping supports)."
    type: consumer-redress
    owner: head-of-deposit-products (with operations execution; counsel direction)
    due_date: 2026-09-30
    accountable_forum: counsel; consumer compliance committee
  - action: "Control change to detect and prevent APSN at posting (system-side rule; daily monitoring KRI)."
    type: control-change
    owner: head-of-deposit-operations
    due_date: 2026-08-15
    accountable_forum: consumer compliance committee
  - action: "Disclosure refresh to address the APSN sequence explicitly in the account agreement and the branch script."
    type: disclosure-change
    owner: head-of-deposit-products
    due_date: 2026-07-31
    accountable_forum: consumer compliance committee
  - action: "Branch incentive design review: identify any incentive that ties to overdraft-fee revenue or overdraft-program enrollment; remove or restructure."
    type: policy-change
    owner: head-of-branch-operations
    due_date: 2026-09-30
    accountable_forum: conduct committee
  - action: "Quarterly read to the conduct committee on the post-remediation complaint-monitoring posture."
    type: monitoring-uplift
    owner: head-of-complaints
    due_date: 2026-12-31
    accountable_forum: conduct committee

open_questions:
  - "Whether the redress lookback extends beyond one year given the bureau's typical multi-year framing in analogous consent orders. Counsel to direct."
  - "Whether the firm has self-reporting expectations under the bureau's most-current self-reporting posture. Counsel to direct."
  - "Whether the branch-incentive review surfaces any incentive that itself raises a separate UDAAP angle on sales practices (e.g., overdraft-program enrollment incentives)."

cross_references: [complaint-theme-analysis, fair-lending-test-plan]

decision_forum:
  named_forum: consumer compliance committee; CCO; counsel directing
  decision_status: submitted
  decision_date: ""
  conditions: []

assumptions_and_dependencies:
  - "Outside counsel directs the review for the duration; privilege posture as marked."
  - "Transaction-data analysis is complete for the period; APSN classification rule applied per the bureau's Circular 2022-06 framing."
  - "The 11 percent APSN concentration is the operative finding; sensitivity analysis on the classification rule has been run and is consistent within ±1 percentage point."

confidence_label: high
```

#### What this memo does and does not do

The memo operationalizes the annual UDAAP refresh for the deposit-overdraft program under the APSN finding. It does not finalize a UDAAP determination, execute the consumer redress, change the disclosure, or trigger any external action. The consumer compliance committee and the CCO act on the recommended remediation under counsel direction; the conduct committee gets a read; the operations function executes the control change and the redress program; the complaint-monitoring loop is the closing artifact.

The element analysis covers all three prongs because the unfairness prong is the dominant CFPB framing on APSN but the deception prong (the disclosure-vs-practice mismatch) and the abusiveness prong (material interference; lack-of-understanding) both apply and reinforce the severity rating. Severity is critical because the pattern matches a CFPB Circular fact pattern directly and remediation cannot wait.

Pattern derived from CFPB Circular 2022-06 and from public CFPB enforcement and supervisory observations on APSN overdraft practices. No named institution is implied; the APSN pattern and the regional-bank framing are the structural patterns, not a specific firm.

## troubleshooting

### Troubleshooting: udaap-risk-review

Recurring failure modes when a UDAAP review memo looks complete but is not. The drafter should preempt these; the decision-forum reviewer (CCO, conduct-risk lead, head of consumer compliance, fair-lending committee, counsel) should catch the rest.

#### The memo covers only the deception prong

Symptom: the memo lays out the marketing copy and the disclosure document, runs the deception analysis, and stops. Unfairness and abusiveness blocks are absent or marked `not-applicable` without rationale.

Why it happens: deception is the easiest prong to evidence with marketing artifacts; firms over-index on deception because the evidence is on hand and the legal framing is familiar. Unfairness requires population estimates and magnitude analysis; abusiveness requires the consumer-journey design and the material-interference read. Both take more work.

Fix: schema requires `unfairness` and `abusiveness` blocks. Abusiveness can land at `not-applicable` but only with `applicability_rationale` filled. A memo that surfaces only deception is a marketing review, not a UDAAP review.

#### "Some customers were charged" is the unfairness finding

Symptom: the unfairness block has injury_type filled but the population and magnitude fields are vague ("a number of customers", "some accountholders", "the affected segment").

Why it happens: the drafter wrote the unfairness analysis from policy text or marketing assets without pulling transaction-data evidence. UDAAP findings without population and magnitude do not support remediation framing.

Fix: schema requires `unfairness.substantial_injury.population_estimate` and `magnitude_per_consumer` or `magnitude_aggregate`. Where evidence is not yet available, mark `population_evidence_flag: evidence-needed` rather than handwaving. The memo carries the analytical work; vagueness is a reviewer flag.

#### "The disclosure was technically correct" is the deception defence

Symptom: the deception block records the disclosure document and concludes that because the document is materially-correct, deception does not apply.

Why it happens: the drafter is reading the disclosure in isolation from the consumer-journey context. CFPB has consistently pursued context-driven deception; the disclosure document is one input to the analysis, not the analysis.

Fix: the deception block names the consumer-journey context in `representation_or_omission` and reads the reasonable-consumer framing in the actual journey, not from the document text alone. Materially-correct disclosure can still mislead a reasonable consumer in context.

#### Countervailing-benefits read is the first line's marketing pitch

Symptom: the unfairness block records the countervailing-benefits assertion as a list of product features and concludes that the benefits outweigh the injury without independent reviewer assessment.

Why it happens: the drafter consolidated the first-line's marketing pitch into the countervailing-benefits field. The prong is not a sales argument.

Fix: schema separates `first_line_assertion` and `reviewer_assessment`. The reviewer must independently assess; the first-line assertion is recorded but not sufficient. The `outweighs_injury` enum forces a reviewer judgment.

#### AI is in path; AI block is empty

Symptom: the in-scope flow includes an AI / ML / complex-algorithm surface (personalisation engine, retention-offer engine, conversational AI, AI-generated communication), and the `ai_algorithmic_findings` block is empty or marked `ai_in_path: false`.

Why it happens: the drafter built the memo from a non-AI template; or treated AI as a model-risk issue rather than a UDAAP issue; or hesitated to apply UDAAP framing to algorithmic outcomes.

Fix: when AI / ML / complex-algorithm is in the in-scope flow, `ai_in_path: true` and the `model_inventory` and `udaap_theory` fields are populated. The bureau has been explicit under the April 2023 Joint Statement and CFPB Circulars 2022-03 and 2023-03 that existing UDAAP authority reaches algorithmic outcomes; novel technology is not a defence.

#### Severity rating without a rubric

Symptom: aggregate severity is set but no rubric is referenced and no per-element severity is recorded; the rationale field is generic ("significant risk" or "moderate exposure") with no per-element reasoning.

Why it happens: severity drift is the single most common audit finding on UDAAP processes. Drafters set severity by feel.

Fix: schema requires `severity_per_element` and `severity_rationale`. SKILL.md names the rubric (Low / Medium / High / Critical with explicit definitions). The rationale per element is mandatory.

#### Conduct-risk implications block is checkbox content

Symptom: the conduct-risk implications block lists the conduct-risk taxonomy categories as a generic checklist with no narrative; the conduct-accountable manager role is unfilled; the conduct-event candidate flag is missing.

Why it happens: the drafter consumed the conduct overlay as a checklist rather than as a substantive overlay; or treated the conduct-risk function as out of scope.

Fix: conduct overlay is mandatory on this skill. `conduct_risk_implications.taxonomy_tie_back` is populated; `conduct_accountable_manager_role` names a role under SMCR or the firm's conduct framework, distinct from the UDAAP-decision forum. The conduct overlay is what makes UDAAP review more than just element analysis.

#### Recommended remediation reads as generic policy advice

Symptom: the remediation block lists items like "review the disclosure", "update the marketing copy", "consider remediation" without owners, due dates, or accountable forums.

Why it happens: the drafter wrote the remediation in advisory voice rather than as a structured set of recommendations the decision-forum acts on. Generic remediation does not get executed.

Fix: schema requires `recommended_remediation[]` with `action`, `type`, `owner`, `due_date`, and `accountable_forum`. Each entry is specific and verifiable. "Restructure the application-page APR to include the instant-funding fee in the cost-of-credit math by 2026-06-30, owned by the head-of-product (fintech-side), with the joint product committee as the accountable forum" is a remediation. "Review the disclosure" is not.

#### Privilege posture is unfilled or marked `n-a`

Symptom: `legal_privilege_posture` is blank, `n-a`, or marked optimistically as "not privileged" without counsel direction.

Why it happens: the drafter treated privilege as a counsel decision to be made later; or treated the UDAAP memo as a routine compliance artifact that does not need a privilege posture.

Fix: privilege posture is a basic discipline for the UDAAP memo; the field is mandatory. Record `attorney-client-privileged`, `attorney-work-product`, `dual-purpose-business-and-privileged`, `not-privileged`, or `posture-pending-counsel`. If counsel has not yet directed, surface the question to counsel before the memo lands at the decision forum, not after.

#### Decision forum is unnamed

Symptom: the memo is fully drafted, the recommendations are well-specified, and there is no record of which forum decides on the remediation.

Why it happens: the drafter treated the memo as the work product itself rather than as the input to a decision-forum gate.

Fix: `decision_forum.named_forum` is filled. The memo is in `draft` until the named forum decides; the remediation execution does not begin until the gate clears (with the exception of urgent kill-switch or marketing-takedown actions where counsel directs an interim posture).

#### The memo is the determination

Symptom: the memo reads like it has already concluded that a UDAAP violation has occurred; or reads like it has already concluded that no violation has occurred. Either is a failure mode.

Why it happens: the drafter conflated the memo with the determination. The memo is the analytical input; the determination, where required, is reserved for counsel and the bureau or other decision-makers.

Fix: the memo states the element analysis and the severity rating; it does not declare a final UDAAP determination. Where the element analysis supports a finding, the memo carries the recommendation for human decision.

#### Sponsor-bank arrangement treated as a footnote

Symptom: the memo covers a sponsor-bank fintech program and lists the sponsor bank as a passive recipient of the review rather than as the accountable creditor of record (or accountable consumer-relationship holder).

Why it happens: the drafter is operating from the program-operator's perspective and treating sponsor-bank involvement as administrative.

Fix: where the in-scope fact pattern runs through a sponsor-bank arrangement, the bank is the accountable party under most arrangements and the bank's consumer-compliance program owns second-line review. The memo reflects joint ownership, joint approval, and a clear statement of which entity carries which duty.

#### Source trace and confidence label absent

Symptom: the memo cites no sources for material claims. Element-test conclusions appear without citation; population estimates appear without sourcing; the severity rating appears without rubric reference.

Why it happens: the drafter borrowed from prior memos or from external references without recording the source.

Fix: every material claim cites a source from `references/source-anchors.md` (or a loaded overlay) by file path. Source evidence, management assertions, public-source obligations, generated inferences, and open legal questions stay distinguishable. The confidence label at the end reflects how well the memo supports the recommended decision.

#### Element analysis ignores the AI overlay where AI is in path

Symptom: the deception block reviews the marketing copy; the unfairness block reviews the fee mechanics; the AI block is populated, but the element analysis does not specifically address the algorithmic outcome under any of the prongs.

Why it happens: the drafter treated the AI block as a separate section rather than letting it inform the element analysis.

Fix: where AI is in path, the element analysis names the algorithmic outcome specifically. The unfairness analysis addresses substantial injury through the algorithmic outcome and the reasonably-avoidable analysis under the algorithmic-design choice; the deception analysis addresses AI-generated communication where it misleads; the abusiveness analysis addresses algorithmic dark-pattern design where it materially interferes. The AI block is what makes the element analysis specific to the AI-in-path fact pattern.

#### Insurance-side fact pattern in scope

Symptom: the memo is reviewing an insurance underwriting model or an insurance pricing decision and applying the §1031 element tests directly.

Why it happens: the drafter loaded the wrong skill; UDAAP review is not the right tool for most insurance work.

Fix: route to the insurance unfair-trade-practice framework (NAIC Model #880; state-DOI market-conduct procedures; NAIC AI Model Bulletin where AI is involved). The narrow exception is bank-affiliated credit-protection insurance bundled with credit, where the credit-side bundling mechanic is in UDAAP scope and the insurance-side decision is out. The insurance sector overlay names the boundary.
