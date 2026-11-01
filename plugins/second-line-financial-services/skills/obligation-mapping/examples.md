# Examples and troubleshooting

One section per worked example, then troubleshooting. Read only what you need.

## bsa-cdd-fintech-bank-sponsor

### Example: FFIEC BSA/AML CDD obligation register for a payments fintech bank-sponsor partnership

#### Input

A consumer-payments fintech operates under a bank-sponsor partnership. The fintech provides the user-facing product; the sponsor bank holds the deposit relationship and bears the BSA/AML obligation as the covered financial institution. The fintech is refreshing its CDD obligation register against the FFIEC BSA/AML Examination Manual (current edition, 2024 update), 31 CFR 1010.230 (beneficial ownership), 31 CFR 1020 (CDD for banks), and the bank-sponsor agreement allocating CDD activities. Source posture is public-plus-firm-policy: the public regulatory anchors plus the executed sponsor agreement and the fintech's CDD policy. The engagement sponsor is the fintech's BSA Officer; legal counsel for the sponsor bank is engaged for cross-party allocation questions.

#### Why this scenario matters

This is the canonical mapping where obligations have to extract on both sides of a third-party relationship. The bank carries the regulatory obligation under 31 CFR 1020 and 1010.230; the fintech carries the operational obligation under the sponsor agreement; the BSA Officer at the bank ultimately attests. The register has to extract the bank-side and fintech-side obligations as separate rows, has to anchor the fintech-side rows in the sponsor agreement (a contractual source) rather than the rule (which addresses the bank), and has to surface the allocation language as the obligation text. It tests the skill's discipline on multi-party source labelling and on the rule-anchored discipline (a fintech-side row whose only source is fintech policy, with no sponsor-agreement clause underneath, fails the discipline).

#### Output sketch

```yaml
register_id: REG-2026-BSA-CDD-FT-01
as_of_date: 2026-05-06
scope_ref: ENG-2026-FT-BSA-01

scope:
  process: customer onboarding, customer due diligence, beneficial ownership identification, ongoing monitoring
  product: consumer payments product under bank-sponsor partnership
  business_unit: payments operations and BSA/AML
  jurisdiction: federal (FinCEN, OCC for sponsor bank)
  period_start: 2026-05-06
  register_type: refresh

source_posture: public-plus-firm-policy

sources:
  - source_name: FFIEC BSA/AML Examination Manual
    issuer: FFIEC
    edition: current online edition, 2024 update referenced
    date: 2024-08-01 [verify update-cycle date]
    url: https://bsaexaminationmanual.ffiec.gov/
    source_type: exam-manual
  - source_name: FinCEN beneficial ownership rule
    issuer: FinCEN
    date: 2018-05-11
    url: https://www.ecfr.gov/current/title-31/subtitle-B/chapter-X/part-1010/subpart-D/section-1010.230
    source_type: rule-text
  - source_name: CDD for banks
    issuer: FinCEN / OCC / FRB / FDIC
    date: as currently codified
    url: https://www.ecfr.gov/current/title-31/subtitle-B/chapter-X/part-1020
    source_type: rule-text
  - source_name: Bank-sponsor agreement, fintech and sponsor bank
    issuer: sponsor bank and fintech (private contract)
    edition: as amended through 2025-Q4
    date: 2025-12-15
    url: internal contract repository, document ID PARTNERSHIP-AGR-2024-001
    source_type: third-party-sla

obligations:
  - obligation_id: OBL-001
    source_citation: FFIEC BSA/AML Examination Manual, Customer Due Diligence section
    source_section: CDD core elements [verify chapter labels in current online edition]
    source_url: https://bsaexaminationmanual.ffiec.gov/
    regulator: FFIEC (bank-sponsor exam authority)
    requirement_summary: >
      The covered financial institution must develop a customer risk profile for each
      customer, including the nature and purpose of the customer relationship, sufficient
      to inform suspicious activity monitoring.
    applicability: >
      Sponsor bank as covered financial institution under 31 CFR 1020; obligation runs
      to the bank, with operational support from the fintech under the sponsor agreement.
    effective_date: in force
    impacted_process: customer onboarding and ongoing monitoring
    control_objective: >
      Every customer record carries a documented customer risk profile reviewed at
      onboarding and refreshed on a risk-based cadence.
    evidence_required:
      - Customer risk profile records in the sponsor bank's BSA system of record
      - Risk-rating refresh cadence sign-off log
    owner: Sponsor bank BSA Officer
    status: approved
    confidence: high
    tags: [financial-crime, bank-side]

  - obligation_id: OBL-002
    source_citation: FinCEN, 31 CFR 1010.230
    source_section: §1010.230(b)(1) (identification) and §1010.230(b)(2) (verification)
    source_url: https://www.ecfr.gov/current/title-31/subtitle-B/chapter-X/part-1010/subpart-D/section-1010.230
    regulator: FinCEN
    requirement_summary: >
      The covered financial institution must identify and verify the identity of each
      beneficial owner of a legal-entity customer at account opening using the
      certification-form mechanism or its substantive equivalent.
    applicability: >
      Sponsor bank as covered financial institution; legal-entity customers opened
      through the fintech-sponsored product flow; not applicable to consumer accounts
      since the rule addresses legal-entity customers.
    effective_date: in force since 2018-05-11
    impacted_process: legal-entity customer onboarding
    control_objective: >
      Every legal-entity customer record contains a §1010.230 certification (or
      substantive equivalent) and verification documentation retained per §1010.230(i).
    evidence_required:
      - §1010.230 certification forms or substantive equivalents in onboarding records
      - Verification documentation (government-issued ID copies, control-prong evidence)
      - Recordkeeping retention proof per §1010.230(i)
    owner: Sponsor bank BSA Officer
    status: approved
    confidence: high
    tags: [financial-crime, bank-side]

  - obligation_id: OBL-003
    source_citation: Bank-sponsor agreement, CDD allocation
    source_section: §4.2 (CDD operational responsibilities of the fintech)
    source_url: internal contract repository, PARTNERSHIP-AGR-2024-001
    regulator: contractual; flows back to the bank's regulatory obligation under 31 CFR 1020
    requirement_summary: >
      The fintech must collect, verify, and transmit CIP and CDD information for each
      customer to the sponsor bank within the timeframes specified in §4.2(c) of the
      sponsor agreement, using the data fields and verification standards the bank's
      written CDD program requires.
    applicability: >
      Fintech onboarding flow for the consumer-payments product; runs only as long as
      the sponsor agreement is in effect.
    effective_date: as of sponsor-agreement execution; current amendment effective 2025-12-15
    impacted_process: customer onboarding (fintech-side)
    control_objective: >
      The fintech delivers CIP and CDD data to the sponsor bank in the §4.2(c) format
      and within the §4.2(c) timeframe, with no incomplete records advancing to the
      bank's BSA system of record.
    evidence_required:
      - Onboarding-flow sample showing field-by-field CIP/CDD capture
      - Daily reconciliation log between fintech onboarding system and bank BSA system
      - Exception report for records that failed verification
    owner: Fintech BSA Lead (operational); sponsor bank BSA Officer (regulatory accountability)
    status: in-review
    confidence: medium
    open_questions:
      - "Whether the §4.2(c) reconciliation cadence (daily) is sufficient if the bank's CDD program later requires near-real-time reconciliation; depends on the bank's program update."
    tags: [financial-crime, fintech-side, third-party-allocation]

  - obligation_id: OBL-004
    source_citation: Bank-sponsor agreement, beneficial-ownership allocation
    source_section: §4.4 (BO collection and verification responsibilities)
    source_url: internal contract repository, PARTNERSHIP-AGR-2024-001
    regulator: contractual; flows to the bank's §1010.230 obligation
    requirement_summary: >
      The fintech must collect and verify §1010.230 beneficial-owner information for
      legal-entity customers it onboards and transmit the certification record to the
      sponsor bank for retention; the sponsor bank retains regulatory accountability.
    applicability: legal-entity customer onboarding through the fintech-sponsored flow
    effective_date: as of sponsor-agreement execution
    impacted_process: legal-entity customer onboarding (fintech-side)
    control_objective: >
      Every legal-entity customer onboarded via the fintech reaches the bank's BSA
      system of record with a §1010.230-compliant certification and verification
      package, or is rejected at the fintech intake gate.
    evidence_required:
      - §1010.230 certification records flowing fintech to bank with timestamped handoff
      - Rejection log for legal-entity customers that failed BO verification at intake
    owner: Fintech BSA Lead (operational); sponsor bank BSA Officer (regulatory accountability)
    status: open-question
    confidence: medium
    open_questions:
      - "Whether the fintech can rely on the sponsor bank's §1010.230 control-prong verification rather than performing its own; depends on bank's written program and the §4.4 carve-out language. Routes to sponsor bank legal."
    tags: [financial-crime, fintech-side, third-party-allocation]

open_question_summary:
  - obligation_ids: [OBL-004]
    question: "Whether fintech can rely on sponsor bank for §1010.230 control-prong verification, or must perform its own; depends on §4.4 sponsor-agreement carve-out and bank's written CDD program"
    reviewer: external-counsel
    target_resolution_date: 2026-06-01
  - obligation_ids: [OBL-003]
    question: "Whether daily reconciliation cadence is sufficient if bank's CDD program later moves to near-real-time"
    reviewer: function-head
    target_resolution_date: 2026-07-01

applicability_notes: >
  Bank-side obligations (OBL-001, OBL-002) flow to the sponsor bank as the covered
  financial institution; the bank's BSA Officer attests these. Fintech-side obligations
  (OBL-003, OBL-004) are contractual and flow back to the bank's regulatory obligation
  through the sponsor agreement; the fintech's BSA Lead is the operational owner, the
  bank's BSA Officer remains regulatorily accountable. The obligation pair-up is the
  point of the register and is explicit in the owner column.

confidence_label: mixed
human_review_required: true

reviewer:
  role: Sponsor bank BSA Officer; fintech BSA Lead countersigns operational rows
  review_status: pending

revisions:
  - date: 2026-05-06
    reason: refresh against 2024 manual update and amended sponsor agreement
    delta: added OBL-003 and OBL-004 to reflect §4.2 and §4.4 amendment language
    approved_by: fintech BSA Lead
```

#### Why the register shape matters downstream

- `control-matrix` builds bank-side rows and fintech-side rows distinctly; the same control objective on both sides will not collapse to one row because the source is different.
- `policy-gap-review` triangulates the fintech's CDD policy against the sponsor agreement and the bank's written CDD program, flagging gaps where the fintech policy does not cover the §4.2 or §4.4 obligations.
- `evidence-binder` reads `OBL-003.evidence_required` and scopes the daily-reconciliation evidence ask, which is the test most likely to surface defects.
- `exam-brief` reads the register if the OCC examiner asks the bank "how do you discharge §1010.230 when the customer was onboarded via the fintech"; OBL-002, OBL-004, and the open-question on §4.4 carve-out are the answer chain.

## section-1071-community-bank

### Example: CFPB Section 1071 obligation register for a community bank

#### Input

A community bank subject to the CFPB Section 1071 small-business lending data collection rule is mapping its obligations from the rule and the final-rule preamble. The bank originates roughly 1,200 covered small-business credit transactions per year, putting it above the **§1071 revised final rule (May 1, 2026)** single 1,000-transaction threshold (which supersedes the 2023 tiered schedule of 2,500 / 500 / 100). Source posture is public-only: 12 CFR 1002.107, 12 CFR 1002.105 (covered financial institution), 12 CFR 1002.110 (reporting), 12 CFR 1002.111 (recordkeeping), the May 2026 revised final rule, and the original CFPB final-rule preamble. The bank's CCO is the engagement sponsor; legal counsel reviews open questions.

#### Why this scenario matters

Section 1071 is the canonical mid-complexity register a community bank stands up: the rule has lifecycle-stage obligations, an applicability threshold that needs explicit reasoning, and at least one design obligation (the firewall) that requires legal review. Under the May 2026 revised final rule, the threshold is a single 1,000-covered-transactions trigger (effective June 30, 2026; compliance January 1, 2028) and the older tier-by-tier compliance-date schedule is gone. The register has to be honest about the threshold and effective-date posture under the revised rule, and has to push the firewall obligation to legal in `open-question` status rather than guessing. It tests the skill's discipline on threshold reasoning, effective-date capture under a recently-amended rule, and routing of design obligations.

#### Output sketch

```yaml
register_id: REG-2026-1071-CB-01
as_of_date: 2026-05-06
scope_ref: ENG-2026-CB-1071-01

scope:
  process: small-business credit application intake, underwriting, recordkeeping, and reporting
  business_unit: small-business lending
  jurisdiction: federal (CFPB)
  period_start: 2026-05-06
  register_type: fresh-build

source_posture: public-only

sources:
  - source_name: CFPB Section 1071 Revised Final Rule
    issuer: CFPB
    edition: Revised final rule, May 1, 2026 (1,000-transaction threshold; effective June 30, 2026; compliance January 1, 2028)
    date: 2026-05-01
    url: https://www.consumerfinance.gov/rules-policy/final-rules/small-business-lending-under-the-equal-credit-opportunity-act-regulation-b/
    source_type: rule-text
  - source_name: CFPB Section 1071 Final Rule (2023, as codified — superseded compliance-date schedule)
    issuer: CFPB
    edition: Final, March 30, 2023, as codified
    date: 2023-03-30
    url: https://www.ecfr.gov/current/title-12/chapter-X/part-1002/subpart-B
    source_type: rule-text

obligations:
  - obligation_id: OBL-001
    source_citation: CFPB, 12 CFR 1002.105
    source_section: §1002.105(b)
    source_url: https://www.ecfr.gov/current/title-12/chapter-X/part-1002/subpart-B/section-1002.105
    regulator: CFPB
    requirement_summary: >
      A covered financial institution that originated at least 1,000 covered originations
      in each of the two preceding calendar years must comply with the data-collection,
      reporting, and recordkeeping requirements of Subpart B (§1002.105(b) under the
      May 2026 revised final rule; supersedes the 2023 100-origination threshold).
    applicability: >
      Community bank originating roughly 1,200 covered small-business credit transactions
      per year; meets the §1002.105(b) revised 1,000-transaction threshold.
    applicability_thresholds:
      covered_origination_threshold: 1000
      notes: bank originated ~1,200 covered transactions in each of 2024 and 2025
    effective_date: 2026-06-30
    effective_date_phase_in: >
      §1071 revised final rule (May 1, 2026): rule effective June 30, 2026; compliance
      date January 1, 2028. The 2023 tiered (high / moderate / low volume) schedule is
      superseded.
    impacted_process: small-business credit application intake
    control_objective: >
      The bank correctly identifies itself as a covered financial institution under §1002.105
      and applies the data-collection regime to all covered applications.
    evidence_required:
      - Annual covered-origination tally with supporting loan-system extract
      - Compliance committee acknowledgement of covered-FI status
    owner: Chief Compliance Officer
    status: in-review
    confidence: high
    tags: [consumer-compliance, fair-lending, banking]

  - obligation_id: OBL-002
    source_citation: CFPB, 12 CFR 1002.107
    source_section: §1002.107(a)
    source_url: https://www.ecfr.gov/current/title-12/chapter-X/part-1002/subpart-B/section-1002.107
    regulator: CFPB
    requirement_summary: >
      The bank must collect and report specified data points for each covered application
      from a small business, including application date, credit type, amount applied for,
      action taken, and the demographic data points listed in §1002.107(a).
    applicability: >
      Community bank, all covered applications from small businesses (as defined in
      §1002.106(b)); compliance begins on §1002.114 compliance date under the May 2026
      revised final rule.
    effective_date: 2028-01-01 [compliance date; rule effective 2026-06-30]
    impacted_process: application intake and underwriting
    control_objective: >
      Every covered application produces a complete §1002.107(a) data record before the
      reporting cycle closes for the year.
    evidence_required:
      - LOS extract showing §1002.107(a) field-by-field completeness
      - QA sample demonstrating 100% of covered applications populated
    owner: Head of Small Business Lending Operations
    status: draft
    confidence: high
    open_questions:
      - "Whether prequalification inquiries that do not become applications need any §1002.107 capture for §1002.103 covered-application boundary purposes"
    tags: [consumer-compliance, fair-lending]

  - obligation_id: OBL-003
    source_citation: CFPB, 12 CFR 1002.108 (firewall)
    source_section: §1002.108(b) [verify subsection labels]
    source_url: https://www.ecfr.gov/current/title-12/chapter-X/part-1002/subpart-B/section-1002.108
    regulator: CFPB
    requirement_summary: >
      Employees and officers involved in making any determination concerning a covered
      application must not have access to the applicant's responses to the §1002.107(a)
      demographic information unless a feasibility determination supports an exception.
    applicability: >
      Covered financial institution; design obligation on the firewall between intake
      capture of demographic data and underwriting decisioning.
    effective_date: 2028-01-01 [compliance date under May 2026 revised final rule]
    impacted_process: application intake and underwriting
    control_objective: >
      Demographic responses captured at intake are not accessible to underwriting
      decision-makers, or a documented feasibility determination supports the exception.
    evidence_required:
      - Firewall design document and access-control walkthrough
      - Feasibility-exception memo if dual-role staffing is being relied on
    owner: Chief Compliance Officer
    status: open-question
    confidence: low
    open_questions:
      - "Whether the bank's loan officers can perform both intake and underwriting under §1002.108 where staffing constraints make full segregation impractical, and what the feasibility-determination evidence has to show. Routes to legal."
    tags: [consumer-compliance, fair-lending, design-obligation]

  - obligation_id: OBL-004
    source_citation: CFPB, 12 CFR 1002.110
    source_section: §1002.110(a)
    source_url: https://www.ecfr.gov/current/title-12/chapter-X/part-1002/subpart-B/section-1002.110
    regulator: CFPB
    requirement_summary: >
      The bank must submit the small-business lending application register to the CFPB
      annually by June 1 of the year following the calendar year covered by the data.
    applicability: covered financial institution; annual federal filing
    effective_date: first filing under §1002.110 falls in the year following the bank's first compliance year; [verify against CFPB filing-instructions guide]
    impacted_process: regulatory reporting
    control_objective: >
      The annual register is filed by June 1 with the §1002.110(b) data fields, and the
      filing acknowledgement is retained.
    evidence_required:
      - Annual CFPB filing acknowledgement
      - Filing-readiness sign-off log from CCO
    owner: Chief Compliance Officer
    status: draft
    confidence: high
    tags: [consumer-compliance, regulatory-reporting]

open_question_summary:
  - obligation_ids: [OBL-003]
    question: "Firewall design where loan officers perform both intake and underwriting; what feasibility-determination evidence is sufficient under §1002.108"
    reviewer: legal
    target_resolution_date: 2026-06-01
  - obligation_ids: [OBL-002]
    question: "Treatment of prequalification inquiries that do not become applications under §1002.103 covered-application definition"
    reviewer: compliance
    target_resolution_date: 2026-06-15

applicability_notes: >
  Bank originated ~1,200 covered transactions in each of 2024 and 2025, meeting the
  §1002.105(b) 1,000-transaction threshold under the May 2026 revised final rule; rule
  effective June 30, 2026 with January 1, 2028 compliance date. Threshold reasoning sits
  in OBL-001's applicability column; open-question on prequalification inquiries depends
  on the §1002.103 covered-application interpretation.

confidence_label: mixed
human_review_required: true

reviewer:
  role: Chief Compliance Officer
  review_status: pending

revisions:
  - date: 2026-05-06
    reason: initial register
    delta: created
    approved_by: Chief Compliance Officer
```

#### Why the register shape matters downstream

- `control-matrix` will anchor its rows on `OBL-001` through `OBL-004`; the firewall row (`OBL-003`) will not move past `open-question` until legal returns the feasibility determination, so the matrix will not yet attempt to map controls against it.
- `policy-gap-review` reads the register against the bank's existing fair-lending policy; the firewall obligation surfaces as a likely policy gap regardless of legal's eventual answer.
- `evidence-binder` reads `OBL-002.evidence_required` and scopes its evidence ask against the LOS extract and the QA sample.
- `exam-brief` reads the register when CFPB exam staff cite §1002.107 or §1002.108; the open-question summary is what the bank shows the examiner if the firewall design is challenged.

## troubleshooting

### Troubleshooting: obligation-mapping

The obligation register is a foundational primitive: control-matrix, policy-gap-review, evidence-binder, exam-brief, and issue-writeup all read it. Defects in the register propagate downstream. This file walks the recurring defects and how to resolve them.

#### 1. The source is a bare URL with no section reference

**Symptom**: A row's source citation is `https://www.federalreserve.gov/...` with no §, paragraph, article, or chapter. Downstream, control-matrix cannot anchor a control to it; exam-brief cannot answer "what part of the rule says this."

**Why it happens**: The practitioner pasted the rule's URL and moved on. Or the source is a long supervisory letter and the section feels like overhead.

**Resolution**:
- The source-citation column carries both URL and section. Mandatory.
- Where the section is genuinely unknown, the row carries `[verify section]`. The placeholder is a deliberate flag, picked up by the open-question summary, never silent.
- For exam manuals and supervisory letters, the section is usually a chapter or numbered subsection name; cite it as the source uses it.
- For SLAs and contracts, the section is the clause number. "§4.2(c)" is a citation; the contract title alone is not.

#### 2. The requirement summary paraphrases away the substance

**Symptom**: A row reads "Firm must do CDD" or "Firm must have appropriate controls." Downstream, control-matrix cannot tell what the obligation actually requires.

**Why it happens**: The practitioner extracted the rule at headline level rather than at substance level. Or the rule was long and summary-fatigue set in.

**Resolution**:
- The summary states what specifically must be done and on whom. "The bank must obtain and verify the identity of each beneficial owner of a legal-entity customer at account opening" preserves substance. "Firm must do CDD" does not.
- Preserve the operative verb (must, shall, should, will). The strength of the obligation is in the verb.
- Preserve the operative object (each customer; each covered application; each material model change). Without the object, the obligation does not bind.
- One sentence is the target, but two sentences for compound obligations is fine. The constraint is substance, not length.

#### 3. Applicability is "all operations"

**Symptom**: Multiple rows carry an applicability column reading "all operations," "the firm," or "every business unit." Downstream skills cannot tell which processes the obligation actually binds.

**Why it happens**: The rule applies broadly within the firm and the practitioner used a shorthand. Or the rule's applicability language was vague and the practitioner did not pin it down.

**Resolution**:
- Applicability names institution type, product, activity, geography, and threshold where the source defines them. Where the source does not, applicability says the source did not specify.
- For tier-dependent rules (1071 by origination volume, NYDFS Part 500 by covered-entity tier, DORA by significance class, Heightened Standards by asset size), capture the threshold and the firm's tier.
- "All operations" is the symptom of unfinished extraction. The rule almost always names a scope (a covered institution, a covered product, a covered activity); the row reflects that.
- For internal-policy sources, applicability is what the policy itself says, not what the practitioner thinks the policy ought to mean.

#### 4. Owner is a department or a collective noun

**Symptom**: Owner column reads "Compliance," "Operations," "the team," or "Risk." Downstream, evidence-binder cannot route an evidence ask, and the human-review gate has no addressee.

**Why it happens**: The role taxonomy was unclear. Or the firm uses a department label as a shorthand for the accountable role.

**Resolution**:
- Owner is a named role with accountability. BSA Officer, Head of Vendor Management, Chief Privacy Officer, Head of Model Risk, ECOA officer, fund CCO, head of credit risk reporting.
- For firm-specific role labels (e.g., "Director, Enterprise Compliance Operations"), the role lives in `references/firm-overlay.md` and the register pulls from there.
- Where two roles share accountability (operational owner and regulatorily accountable owner in a sponsor-bank relationship), the column captures both with the relationship: "Fintech BSA Lead (operational); sponsor bank BSA Officer (regulatory accountability)."
- A row with no clear owner is a row that is not yet complete; flag it as `open-question` rather than ship with a department label.

#### 5. Status pre-decided as approved

**Symptom**: Rows enter the register with `status: approved` directly from extraction.

**Why it happens**: The practitioner treated the extraction as a one-step process. Or the firm's existing register marked rows approved and the refresh inherited the value without re-review.

**Resolution**:
- Status enters at `draft` or `open-question`. Always.
- `approved` is reserved for rows the named reviewer has signed off on. The skill does not set that value itself; the human review gate does.
- For refreshes, inherited statuses are revisited where the source has changed; otherwise the refresh log notes that the prior status carries forward unless the refresh changed substance.
- `not-applicable` is a legitimate value with rationale; it is not a way to mark something approved-by-not-mattering.

#### 6. The register mixes rule and firm policy without anchor

**Symptom**: Rows whose only source is the firm's own policy, with no external rule, supervisory guidance, or contract underneath.

**Why it happens**: The firm's policy library is comprehensive and the practitioner extracted at policy level. The output reads like a policy index rather than an obligation register.

**Resolution**:
- The register is rule-anchored. Internal policy can be a source on a row that also cites an external rule, supervisory guidance, or contract.
- Rows with policy-only sources belong in `policy-gap-review`'s output, not here. The register asks "what does the firm have to do"; the policy library captures "what the firm says it does about it."
- Where the firm has a policy that goes beyond the regulatory baseline (a self-imposed standard), that lives in the firm-overlay and surfaces as a control choice in `control-matrix`, not as an obligation row.

#### 7. Open questions disappear into the row

**Symptom**: Rows carry `status: open-question` but the open-question summary at the tail of the artifact is empty or generic.

**Why it happens**: The practitioner captured the question in the row but did not aggregate it. Downstream legal review has nothing to route against.

**Resolution**:
- The open-question summary is grouped by reviewer (legal, compliance, function head, sponsor). Every `open-question` row appears in exactly one group.
- Each summary entry names the obligation IDs it covers, the question, the reviewer, and the target resolution date.
- A row whose status is `open-question` but whose question is not in the summary is a defect; the summary is the routing artifact, the row is the working content.

#### 8. Confidence label as a single overall value

**Symptom**: The artifact carries one confidence label ("medium") without per-section detail. Downstream, exam-brief cannot tell which rows are pressure-test ready and which are interpretive.

**Why it happens**: The practitioner treated confidence as a summary judgment rather than a per-section discipline.

**Resolution**:
- Confidence tracks by section in the source-trace block, not as a single overall label. Most registers have high-confidence rows (unambiguous source) and low-confidence rows (interpretation involved or single secondary source) side by side.
- Per-row confidence on each obligation is also useful and supported by the schema (`obligation.confidence`).
- The overall `confidence_label` on the register is allowed to be `mixed` and usually is.

#### 9. Effective dates with phase-in collapsed

**Symptom**: A row with a tiered effective date (1071 by volume tier, DORA by entity class, climate disclosure rules with phased-in scope) carries a single date and loses the phase-in.

**Why it happens**: The rule's phase-in language is dense and the practitioner picked the date that applied to the firm without flagging the broader schedule.

**Resolution**:
- `effective_date_phase_in` captures phase-in stages. The applicable-to-firm date sits in `effective_date`; the broader schedule sits in the phase-in field.
- Where the effective date is contingent (rule subject to litigation, guidance subject to revision, sunset awaiting reauthorisation), the row notes the contingency.
- Compliance-date schedules that the firm has not yet hit but will hit are still flagged so the firm sees them coming.

#### 10. The register is built without scope

**Symptom**: Multiple registers across engagements use inconsistent jurisdiction labels, persona vocabulary, and overlay choices. Downstream skills load the wrong overlays or the wrong taxonomy.

**Why it happens**: The skill was invoked without an scope record on file, the practitioner declined the four scoping questions, and the defaults set the wrong tone.

**Resolution**:
- When `scope` is supplied, consume it. Sector overlays, cross-cutting overlays, persona, source posture, jurisdiction all key off the scope record.
- When it is not supplied, ask the four questions. If the practitioner declines, default to public posture and note in the artifact that scope was not formalised.
- For a firm running many registers, the scope record is what keeps them coherent across functions.
