# Example: intake for an accelerated-underwriting ML model at a regional life insurer

Public-source-derived. No named institution. Patterns drawn from NAIC Model Bulletin on the Use of Artificial Intelligence Systems by Insurers (December 2023), Colorado SB 21-169 implementing regulation, and the NYDFS Insurance Circular Letter on AI and ECDIS in life-insurance underwriting (January 2024).

## Input description

A regional life insurer (term and whole-life lines, multi-state, sells in CO, NY, CA, and 18 other states) is intaking an in-house ML accelerated-underwriting model for term-life applications under $500K face amount. The model uses the carrier's own historical underwriting data plus third-party clinical and prescription history (ECDIS) to produce a risk score; applicants below a tuned threshold receive an auto-accept (no fluid testing required), applicants in a middle band route to a human underwriter with the score as one input, applicants above the threshold route to a human underwriter without auto-decline. Model is in-house developed; no foundation model; no agentic behaviour. Sponsor (head of life-underwriting) proposes tier-1.

Engagement scope provided by `scoping`:
- Institution type: state-licensed life insurer; multi-state, including CO, NY, CA.
- Persona: AI Governance Lead (hybrid AI governance / model risk function), reporting to chief actuary with dotted line to chief compliance officer.
- Sector overlay: insurance. Cross-cutting overlays: privacy (PHI from prescription and clinical data; NPI from financial sections of the application), conduct (customer-binding underwriting decision with adverse-action implications under state insurance fairness rules and NAIC Model #880).
- Source posture: public-plus-firm-policy-plus-evidence.

## Output sketch

### 1. Identity and sponsor

- Use case ID: AI-2026-LU-003
- Use case version: 1.0
- Use case name: Term-life accelerated-underwriting risk score
- Engagement scope ID: ES-2026-AIGOV-014
- Intake date: 2026-05-06
- Next review due: 2026-08-06 (quarterly cadence; tier-1 proposed)
- Sponsor business unit: life underwriting
- Accountable first-line owner: head of life-underwriting (model owner role under firm policy)
- AI Governance Lead reviewer: AI Governance Lead, hybrid AI governance / model risk function
- Lifecycle stage: limited production (live in CO and three non-DOI-bulletin states; pre-deployment in NY and CA pending state-bulletin readiness review)

### 2. Business purpose and target outcome

The model produces a risk score for term-life applications under $500K face amount, used to route applications to one of three paths: auto-accept (no fluid testing), human-underwriter-with-score, or human-underwriter-without-auto-decline. Target outcome: reduce time-to-decision on auto-accept-eligible applications from 14 days to 24 hours; maintain mortality-claims experience consistent with the carrier's actuarial assumptions (measured at policy duration 5 years and beyond); avoid disparate impact across protected classifications under state insurance code and against unfair discrimination under NAIC Model #880.

### 3. Intended users and decision points

| User role | Decision influenced | Human review point |
|---|---|---|
| Underwriting routing system (automated) | Routing decision (auto-accept / human-with-score / human-without-auto-decline) | None at the routing step itself; human review at the decision step for the latter two paths |
| Life underwriter | Auto-accept score is the binding decision; human-with-score path uses the score as one input; human-without-auto-decline path uses the score informationally only | Underwriter signs the decision in human-routed paths |
| Applicant (indirect) | Receives auto-accept, request for additional information, or denial via adverse-action notice | Adverse-action notice generated under state insurance code and ECOA-equivalent expectations |

### 4. Decision impact

| Dimension | Score | Basis |
|---|---|---|
| Customer impact | High | Customer-binding underwriting decision; adverse-action implications; eligibility, premium, and coverage are influenced |
| Financial impact | Medium | New-business mortality experience flows to product profitability; misclassification at scale affects reserves but not balance-sheet capital adequacy |
| Regulatory impact | High | NAIC Bulletin AIS Program reach; CO SB 21-169 reach for life-insurance ECDIS use; NY DFS Insurance Circular reach for life-insurance AI; state insurance code unfair discrimination under Model #880; HIPAA on PHI inputs |
| Operational impact | Medium | Accelerated-underwriting throughput is dependent on the model; failure or pause increases time-to-decision and loses sales but does not break a critical operational process |

### 5. Autonomy level

- Level: human-on-the-loop for the auto-accept path (the routing decision is automated; the auto-accept itself is an automated bind once the score crosses the threshold); human-in-the-loop for the human-routed paths.
- Evidence of effective oversight: monthly underwriter team-lead review of 5% of auto-accept decisions for outlier patterns; quarterly actuarial review of mortality experience by score band and by ECDIS-input-driven segments; monthly disparate-impact monitoring report to the AI Governance Lead. The auto-accept path's "human-on-the-loop" framing is intentional and reflects that the human is reviewing patterns rather than each decision.

### 6. Architecture

- Model type: ML
- Deployment posture: in-house
- Foundation-model identity: n/a
- RAG architecture: n/a
- Tool inventory: n/a (the model produces a score; the routing logic is rule-based downstream of the score)

### 7. Data sources

| Source | Sensitivity | Field-level tagging | Purpose | Lawful basis |
|---|---|---|---|---|
| Carrier historical underwriting data (ten years) | regulated NPI | Applicant identifying information, financial information, occupation, prior policy history | training and reference | Carrier's existing underwriting use of customer data |
| ECDIS — clinical history vendor | regulated PHI | Diagnosis history, medical procedure history | training and inference input | HIPAA authorisation obtained at application; vendor BAA in place |
| ECDIS — prescription history vendor | regulated PHI | Prescription drug history (categories, dates, dosage indicators) | training and inference input | HIPAA authorisation obtained at application; vendor BAA in place |
| MIB Group code data | regulated NPI plus PHI proxy | MIB-coded medical and risk information | training and inference input | MIB membership and applicant authorisation |
| Application form data | regulated NPI | Identifying, financial, occupation, beneficiary | inference input | Application consent |

### 8. Vendor and third-party dependencies

| Vendor | Role | Criticality | Change-of-version notice | Fallback posture |
|---|---|---|---|---|
| [Clinical history ECDIS vendor] | data_provider | critical | Quarterly data refresh; vendor SLA on data freshness; no change-of-version concept (data updates rather than model version) | Manual underwriting fallback for affected segments; pause auto-accept |
| [Prescription history ECDIS vendor] | data_provider | critical | Same as above | Same as above |
| MIB Group | data_provider | critical | Industry-standard refresh | Manual underwriting fallback |

### 9. Regulatory exposure flags

| Flag | Basis | Routes to |
|---|---|---|
| NAIC_Bulletin_AI_2023 | Insurer use of AI for underwriting; AIS Program elements apply (state-by-state adoption per NAIC tracker) | ai-risk-tiering, model-card-builder, validation-plan |
| CO_SB_21_169 | CO operating footprint for life-insurance underwriting using ECDIS and predictive models | ai-risk-tiering, model-card-builder, validation-plan |
| NY_DFS_Circular_AI_2024 | Pre-deployment for NY footprint; life-insurance underwriting and pricing using AI and ECDIS | ai-risk-tiering, model-card-builder |
| HIPAA | PHI in clinical-history and prescription-history inputs; vendor BAA posture | validation-plan |
| State insurance code unfair discrimination (NAIC_Model_880) | Customer-binding underwriting decision; protected classifications under state code | validation-plan |

### 10. Preliminary tier proposal

- Proposed tier: tier-1
- Rationale: customer-binding underwriting decision with adverse-action implications, ECDIS use in CO and pre-deployment in NY, HIPAA-PHI inputs, and state insurance unfair-discrimination test reach. The AIS Program proportionality reads high. Sponsor and AI Governance Lead concur.

### 11. Proposed review gates and human oversight

| Gate | Owner function | Frequency | Stop condition |
|---|---|---|---|
| Independent validation (full; conceptual soundness, data quality, benchmarking, outcomes analysis) | model risk team | Pre-deployment per state and annual | Validation findings unresolved |
| AI risk committee approval | AI risk committee secretary | Pre-deployment per state and on material change | Conditional approval revoked |
| Pre-prod gate | AI Governance Lead | Per-state pre-deployment | Pre-prod gate fails |
| ECDIS vendor diligence | vendor management with AI governance | Annual and on vendor data-source change | Vendor evidence pack does not meet firm criteria |
| Disparate-impact monitoring | AI Governance Lead with consumer compliance | Monthly | Disparate-impact threshold breach |
| Mortality-experience monitoring | actuarial function | Quarterly aggregate; annual by segment | Mortality experience breach against actuarial assumptions |
| Adverse-action notice quality sampling | consumer compliance | Quarterly | Sample shows specific-reasons defect |

### 12. Open questions for second-line follow-up

| Question | Routes to | Owner | Due date |
|---|---|---|---|
| What is the AIS Program element-by-element coverage status; are governance, third-party AI accountability, monitoring, and transparency elements at firm-policy maturity for this use case? | model-card-builder | AI governance | 2026-06-30 |
| For NY deployment, what is the consumer-disclosure language and the consumer-recourse channel; does it meet NY DFS Circular expectations? | model-card-builder, consumer compliance review | consumer compliance | 2026-07-15 |
| For CO deployment, the ECDIS provenance evidence pack: is it complete and current as of the deployment date? | validation-plan, vendor-diligence | vendor management | 2026-06-15 |
| Bias-evaluation evidence framed against unfair discrimination (Model #880) is the operative test, not generic fairness. What is the evidence pack and the segment-level test posture? | validation-plan | model risk team | 2026-07-30 |
| Does the use case meet the firm's ORSA materiality threshold? If yes, the use case feeds the ORSA Summary Report. | board-ai-risk-pack | enterprise risk function | 2026-08-30 |
| TPA / claims-administrator overlap is not present today; if a TPA were ever interposed for binding decisions, NAIC Model #668 §4.F third-party service-provider obligations would attach. Flag for change-plan monitoring. | (no immediate route) | head of life-underwriting | n/a (monitoring) |

### 13. Twelve-month change plan

- Named owner: head of life-underwriting
- Scope changes: NY deployment expected Q3 2026; CA deployment expected Q4 2026; planned face-amount expansion from $500K to $1M in Q1 2027 (any face-amount expansion triggers re-intake plus tiering revisit because financial-impact and mortality-tail change).
- Autonomy uplift: no planned uplift; the auto-accept threshold may be re-tuned based on mortality experience but the routing structure is not changing.
- Customer surface expansion: no change to direct-customer surface; the adverse-action notice content is being reviewed against NY DFS Circular expectations as part of NY deployment.
- Vendor changes: ECDIS vendor evaluation cycle in Q4 2026 may result in change to one or both ECDIS vendors; either outcome triggers re-intake.

### 14. Sector and cross-cutting overlay flags

- Sector overlay applied: insurance
- Cross-cutting overlays applied: privacy, conduct
- Overlay-specific notes: insurance overlay flags AIS Program element coverage, state-by-state DOI bulletin status, ECDIS provenance, HIPAA touch, ORSA materiality check; privacy overlay flags field-level PHI tagging on ECDIS inputs and BAA posture; conduct overlay flags Model #880 unfair-discrimination test as the operative legal frame (not generic fairness) and adverse-action notice quality as the conduct-monitoring point.

### 15. AI Act overlap

- High-risk overlap likely: yes
- Annex III categories flagged: §5(c) "risk assessment and pricing in life and health insurance" (the use case is squarely in scope)
- Provider or deployer role: deployer (the firm is the deployer; no EU footprint today, so most operative obligations do not attach. Flagged for re-look if an EU branch or EU reinsurance arrangement enters scope. The Annex III flag is the routing signal regardless.)
- Routed to ai-act-triage: yes (formal classification owned by ai-act-triage; intake captures the routing signal)

### 16. Source trace and confidence

| Claim | Source | Evidence reference | Confidence |
|---|---|---|---|
| Auto-accept routing structure | Firm system design document | SDD-2026-LU-003 §2 | High |
| ECDIS vendor identification and contract status | Firm vendor register | VR-2026-LU-003 | High |
| HIPAA authorisation in application; vendor BAAs in place | Firm consent and contract files | CCF-2026-LU-003 | High |
| AIS Program element coverage status | Firm AI governance maturity assessment | AGMA-2026-Q1 | Medium (assessment dated Q1 2026; specific use-case maturity per element to be confirmed by AIS Program review) |
| State operating footprint | Firm licensure register | LR-2026 | High |
| Disparate-impact monitoring rubric | Firm-policy-attested rubric | Rubric DI-2026-014 | High |
| Mortality experience monitoring methodology | Firm actuarial methodology document | AMD-2026 | High |

## Reviewer attestation (sketch)

- Reviewer role: AI Governance Lead, hybrid AI governance / model risk function
- Decision: accept with conditions
- Conditions: (a) AIS Program element coverage open question closed before NY deployment; (b) NY DFS Circular consumer-disclosure language and recourse channel reviewed and signed by consumer compliance before NY deployment; (c) Model #880 bias-evaluation evidence pack closed before any further deployment; (d) ORSA materiality determination made before next quarterly enterprise risk forum; (e) re-intake required at any of: face-amount expansion, ECDIS vendor change, EU footprint addition, autonomy structure change.
- Attestation date: 2026-05-09
- Onward routing: ai-risk-tiering; ai-act-triage (Annex III §5(c) routing); model-card-builder; validation-plan; vendor-diligence; board-ai-risk-pack (pending ORSA materiality determination)

## Why this scenario matters

- It exercises the customer-binding-high case. Customer impact is high; financial impact is medium; regulatory impact is high; operational impact is medium. The tier proposal lands at tier-1, and sponsor and AI Governance Lead concur (no dissent).
- It exercises the insurance overlay end-to-end. AIS Program element coverage, state-by-state DOI bulletin status (CO live, NY pre-deployment, CA pre-deployment), ECDIS provenance, HIPAA-PHI tagging, ORSA materiality check are all on the intake.
- It exercises the conduct-overlay distinction between fairness and unfair discrimination. The intake records Model #880 as the operative legal frame and routes the bias-evaluation evidence question to validation-plan with the right framing.
- It exercises the EU AI Act Annex III §5(c) routing signal. The intake does not classify the use case under the AI Act (that is `ai-act-triage`'s job), but it captures the routing flag because §5(c) (life and health insurance pricing and risk assessment) is the most-frequent FS Annex III trigger and the intake is where it gets caught.
- It exercises the change-plan field on a high-stakes use case. Face-amount expansion, vendor change, EU footprint, autonomy change are each named events tied to re-intake; the use case does not drift inside annual review cadence.
- It exercises the no-foundation-model branch of the architecture block. Not every AI use case is a GenAI use case; the intake structure handles in-house ML cleanly without forcing the GenAI overlay.
