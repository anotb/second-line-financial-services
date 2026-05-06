# Example: annual UDAAP refresh on a regional bank's deposit-overdraft program with APSN findings

## Input

A $40B regional bank operates a deposit-overdraft program for its consumer checking accounts. The program covers debit-card and ACH transactions; consumers opt in to debit-card overdraft per Reg E §1005.17. The bank's overdraft fee is $35 per item; daily max is 4 items. The bank's annual UDAAP refresh on the deposit-overdraft program is in cycle. Annual transaction-data analysis surfaces an authorize-positive-settle-negative (APSN) pattern: 11 percent of overdraft fees in the prior 12 months were assessed on transactions that were authorized when the available balance was sufficient but settled (and overdrew) after intervening transactions. The complaint-management system shows a cluster of "surprise overdraft" complaints across three of the bank's footprint states.

The CCO and the head of consumer compliance are jointly sponsoring the review. Source posture is public-plus-firm-policy-plus-evidence; the bank has core-banking-system transaction data, account-disclosure documents, complaint records, branch and call-center recordings, and the most recent two CFPB Supervisory Highlights issues. Outside counsel directs the review for privilege.

## Why this scenario matters

This is the canonical CFPB Circular 2022-06 (Unanticipated Overdraft Fee Assessment Practices) fact pattern. The bureau has been explicit that APSN fees can violate the unfairness prong of CFPA §1031 because consumers cannot reasonably anticipate the fee at the moment of the transaction. The annual refresh has to handle population-and-magnitude analysis (the 11 percent figure plus the aggregate fee-revenue exposure), conduct-risk implications (the bank's overdraft-fee revenue contribution; branch incentive design), and remediation framing (consumer redress for the affected fee population in the lookback period; control change to detect and prevent APSN at posting).

## Output sketch

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

## What this memo does and does not do

The memo operationalizes the annual UDAAP refresh for the deposit-overdraft program under the APSN finding. It does not finalize a UDAAP determination, execute the consumer redress, change the disclosure, or trigger any external action. The consumer compliance committee and the CCO act on the recommended remediation under counsel direction; the conduct committee gets a read; the operations function executes the control change and the redress program; the complaint-monitoring loop is the closing artifact.

The element analysis covers all three prongs because the unfairness prong is the dominant CFPB framing on APSN but the deception prong (the disclosure-vs-practice mismatch) and the abusiveness prong (material interference; lack-of-understanding) both apply and reinforce the severity rating. Severity is critical because the pattern matches a CFPB Circular fact pattern directly and remediation cannot wait.

Pattern derived from CFPB Circular 2022-06 and from public CFPB enforcement and supervisory observations on APSN overdraft practices. No named institution is implied; the APSN pattern and the regional-bank framing are the structural patterns, not a specific firm.
