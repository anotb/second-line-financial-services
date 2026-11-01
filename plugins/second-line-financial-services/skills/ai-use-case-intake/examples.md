# Examples and troubleshooting

One section per worked example, then troubleshooting. Read only what you need.

## accelerated-underwriting-life-insurer

### Example: intake for an accelerated-underwriting ML model at a regional life insurer

Public-source-derived. No named institution. Patterns drawn from NAIC Model Bulletin on the Use of Artificial Intelligence Systems by Insurers (December 2023), Colorado SB 21-169 implementing regulation, and the NYDFS Insurance Circular Letter on AI and ECDIS in life-insurance underwriting (January 2024).

#### Input description

A regional life insurer (term and whole-life lines, multi-state, sells in CO, NY, CA, and 18 other states) is intaking an in-house ML accelerated-underwriting model for term-life applications under $500K face amount. The model uses the carrier's own historical underwriting data plus third-party clinical and prescription history (ECDIS) to produce a risk score; applicants below a tuned threshold receive an auto-accept (no fluid testing required), applicants in a middle band route to a human underwriter with the score as one input, applicants above the threshold route to a human underwriter without auto-decline. Model is in-house developed; no foundation model; no agentic behaviour. Sponsor (head of life-underwriting) proposes tier-1.

Engagement scope provided by `scoping`:
- Institution type: state-licensed life insurer; multi-state, including CO, NY, CA.
- Persona: AI Governance Lead (hybrid AI governance / model risk function), reporting to chief actuary with dotted line to chief compliance officer.
- Sector overlay: insurance. Cross-cutting overlays: privacy (PHI from prescription and clinical data; NPI from financial sections of the application), conduct (customer-binding underwriting decision with adverse-action implications under state insurance fairness rules and NAIC Model #880).
- Source posture: public-plus-firm-policy-plus-evidence.

#### Output sketch

##### 1. Identity and sponsor

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

##### 2. Business purpose and target outcome

The model produces a risk score for term-life applications under $500K face amount, used to route applications to one of three paths: auto-accept (no fluid testing), human-underwriter-with-score, or human-underwriter-without-auto-decline. Target outcome: reduce time-to-decision on auto-accept-eligible applications from 14 days to 24 hours; maintain mortality-claims experience consistent with the carrier's actuarial assumptions (measured at policy duration 5 years and beyond); avoid disparate impact across protected classifications under state insurance code and against unfair discrimination under NAIC Model #880.

##### 3. Intended users and decision points

| User role | Decision influenced | Human review point |
|---|---|---|
| Underwriting routing system (automated) | Routing decision (auto-accept / human-with-score / human-without-auto-decline) | None at the routing step itself; human review at the decision step for the latter two paths |
| Life underwriter | Auto-accept score is the binding decision; human-with-score path uses the score as one input; human-without-auto-decline path uses the score informationally only | Underwriter signs the decision in human-routed paths |
| Applicant (indirect) | Receives auto-accept, request for additional information, or denial via adverse-action notice | Adverse-action notice generated under state insurance code and ECOA-equivalent expectations |

##### 4. Decision impact

| Dimension | Score | Basis |
|---|---|---|
| Customer impact | High | Customer-binding underwriting decision; adverse-action implications; eligibility, premium, and coverage are influenced |
| Financial impact | Medium | New-business mortality experience flows to product profitability; misclassification at scale affects reserves but not balance-sheet capital adequacy |
| Regulatory impact | High | NAIC Bulletin AIS Program reach; CO SB 21-169 reach for life-insurance ECDIS use; NY DFS Insurance Circular reach for life-insurance AI; state insurance code unfair discrimination under Model #880; HIPAA on PHI inputs |
| Operational impact | Medium | Accelerated-underwriting throughput is dependent on the model; failure or pause increases time-to-decision and loses sales but does not break a critical operational process |

##### 5. Autonomy level

- Level: human-on-the-loop for the auto-accept path (the routing decision is automated; the auto-accept itself is an automated bind once the score crosses the threshold); human-in-the-loop for the human-routed paths.
- Evidence of effective oversight: monthly underwriter team-lead review of 5% of auto-accept decisions for outlier patterns; quarterly actuarial review of mortality experience by score band and by ECDIS-input-driven segments; monthly disparate-impact monitoring report to the AI Governance Lead. The auto-accept path's "human-on-the-loop" framing is intentional and reflects that the human is reviewing patterns rather than each decision.

##### 6. Architecture

- Model type: ML
- Deployment posture: in-house
- Foundation-model identity: n/a
- RAG architecture: n/a
- Tool inventory: n/a (the model produces a score; the routing logic is rule-based downstream of the score)

##### 7. Data sources

| Source | Sensitivity | Field-level tagging | Purpose | Lawful basis |
|---|---|---|---|---|
| Carrier historical underwriting data (ten years) | regulated NPI | Applicant identifying information, financial information, occupation, prior policy history | training and reference | Carrier's existing underwriting use of customer data |
| ECDIS — clinical history vendor | regulated PHI | Diagnosis history, medical procedure history | training and inference input | HIPAA authorisation obtained at application; vendor BAA in place |
| ECDIS — prescription history vendor | regulated PHI | Prescription drug history (categories, dates, dosage indicators) | training and inference input | HIPAA authorisation obtained at application; vendor BAA in place |
| MIB Group code data | regulated NPI plus PHI proxy | MIB-coded medical and risk information | training and inference input | MIB membership and applicant authorisation |
| Application form data | regulated NPI | Identifying, financial, occupation, beneficiary | inference input | Application consent |

##### 8. Vendor and third-party dependencies

| Vendor | Role | Criticality | Change-of-version notice | Fallback posture |
|---|---|---|---|---|
| [Clinical history ECDIS vendor] | data_provider | critical | Quarterly data refresh; vendor SLA on data freshness; no change-of-version concept (data updates rather than model version) | Manual underwriting fallback for affected segments; pause auto-accept |
| [Prescription history ECDIS vendor] | data_provider | critical | Same as above | Same as above |
| MIB Group | data_provider | critical | Industry-standard refresh | Manual underwriting fallback |

##### 9. Regulatory exposure flags

| Flag | Basis | Routes to |
|---|---|---|
| NAIC_Bulletin_AI_2023 | Insurer use of AI for underwriting; AIS Program elements apply (state-by-state adoption per NAIC tracker) | ai-risk-tiering, model-card-builder, validation-plan |
| CO_SB_21_169 | CO operating footprint for life-insurance underwriting using ECDIS and predictive models | ai-risk-tiering, model-card-builder, validation-plan |
| NY_DFS_Circular_AI_2024 | Pre-deployment for NY footprint; life-insurance underwriting and pricing using AI and ECDIS | ai-risk-tiering, model-card-builder |
| HIPAA | PHI in clinical-history and prescription-history inputs; vendor BAA posture | validation-plan |
| State insurance code unfair discrimination (NAIC_Model_880) | Customer-binding underwriting decision; protected classifications under state code | validation-plan |

##### 10. Preliminary tier proposal

- Proposed tier: tier-1
- Rationale: customer-binding underwriting decision with adverse-action implications, ECDIS use in CO and pre-deployment in NY, HIPAA-PHI inputs, and state insurance unfair-discrimination test reach. The AIS Program proportionality reads high. Sponsor and AI Governance Lead concur.

##### 11. Proposed review gates and human oversight

| Gate | Owner function | Frequency | Stop condition |
|---|---|---|---|
| Independent validation (full; conceptual soundness, data quality, benchmarking, outcomes analysis) | model risk team | Pre-deployment per state and annual | Validation findings unresolved |
| AI risk committee approval | AI risk committee secretary | Pre-deployment per state and on material change | Conditional approval revoked |
| Pre-prod gate | AI Governance Lead | Per-state pre-deployment | Pre-prod gate fails |
| ECDIS vendor diligence | vendor management with AI governance | Annual and on vendor data-source change | Vendor evidence pack does not meet firm criteria |
| Disparate-impact monitoring | AI Governance Lead with consumer compliance | Monthly | Disparate-impact threshold breach |
| Mortality-experience monitoring | actuarial function | Quarterly aggregate; annual by segment | Mortality experience breach against actuarial assumptions |
| Adverse-action notice quality sampling | consumer compliance | Quarterly | Sample shows specific-reasons defect |

##### 12. Open questions for second-line follow-up

| Question | Routes to | Owner | Due date |
|---|---|---|---|
| What is the AIS Program element-by-element coverage status; are governance, third-party AI accountability, monitoring, and transparency elements at firm-policy maturity for this use case? | model-card-builder | AI governance | 2026-06-30 |
| For NY deployment, what is the consumer-disclosure language and the consumer-recourse channel; does it meet NY DFS Circular expectations? | model-card-builder, consumer compliance review | consumer compliance | 2026-07-15 |
| For CO deployment, the ECDIS provenance evidence pack: is it complete and current as of the deployment date? | validation-plan, vendor-diligence | vendor management | 2026-06-15 |
| Bias-evaluation evidence framed against unfair discrimination (Model #880) is the operative test, not generic fairness. What is the evidence pack and the segment-level test posture? | validation-plan | model risk team | 2026-07-30 |
| Does the use case meet the firm's ORSA materiality threshold? If yes, the use case feeds the ORSA Summary Report. | board-ai-risk-pack | enterprise risk function | 2026-08-30 |
| TPA / claims-administrator overlap is not present today; if a TPA were ever interposed for binding decisions, NAIC Model #668 §4.F third-party service-provider obligations would attach. Flag for change-plan monitoring. | (no immediate route) | head of life-underwriting | n/a (monitoring) |

##### 13. Twelve-month change plan

- Named owner: head of life-underwriting
- Scope changes: NY deployment expected Q3 2026; CA deployment expected Q4 2026; planned face-amount expansion from $500K to $1M in Q1 2027 (any face-amount expansion triggers re-intake plus tiering revisit because financial-impact and mortality-tail change).
- Autonomy uplift: no planned uplift; the auto-accept threshold may be re-tuned based on mortality experience but the routing structure is not changing.
- Customer surface expansion: no change to direct-customer surface; the adverse-action notice content is being reviewed against NY DFS Circular expectations as part of NY deployment.
- Vendor changes: ECDIS vendor evaluation cycle in Q4 2026 may result in change to one or both ECDIS vendors; either outcome triggers re-intake.

##### 14. Sector and cross-cutting overlay flags

- Sector overlay applied: insurance
- Cross-cutting overlays applied: privacy, conduct
- Overlay-specific notes: insurance overlay flags AIS Program element coverage, state-by-state DOI bulletin status, ECDIS provenance, HIPAA touch, ORSA materiality check; privacy overlay flags field-level PHI tagging on ECDIS inputs and BAA posture; conduct overlay flags Model #880 unfair-discrimination test as the operative legal frame (not generic fairness) and adverse-action notice quality as the conduct-monitoring point.

##### 15. AI Act overlap

- High-risk overlap likely: yes
- Annex III categories flagged: §5(c) "risk assessment and pricing in life and health insurance" (the use case is squarely in scope)
- Provider or deployer role: deployer (the firm is the deployer; no EU footprint today, so most operative obligations do not attach. Flagged for re-look if an EU branch or EU reinsurance arrangement enters scope. The Annex III flag is the routing signal regardless.)
- Routed to ai-act-triage: yes (formal classification owned by ai-act-triage; intake captures the routing signal)

##### 16. Source trace and confidence

| Claim | Source | Evidence reference | Confidence |
|---|---|---|---|
| Auto-accept routing structure | Firm system design document | SDD-2026-LU-003 §2 | High |
| ECDIS vendor identification and contract status | Firm vendor register | VR-2026-LU-003 | High |
| HIPAA authorisation in application; vendor BAAs in place | Firm consent and contract files | CCF-2026-LU-003 | High |
| AIS Program element coverage status | Firm AI governance maturity assessment | AGMA-2026-Q1 | Medium (assessment dated Q1 2026; specific use-case maturity per element to be confirmed by AIS Program review) |
| State operating footprint | Firm licensure register | LR-2026 | High |
| Disparate-impact monitoring rubric | Firm-policy-attested rubric | Rubric DI-2026-014 | High |
| Mortality experience monitoring methodology | Firm actuarial methodology document | AMD-2026 | High |

#### Reviewer attestation (sketch)

- Reviewer role: AI Governance Lead, hybrid AI governance / model risk function
- Decision: accept with conditions
- Conditions: (a) AIS Program element coverage open question closed before NY deployment; (b) NY DFS Circular consumer-disclosure language and recourse channel reviewed and signed by consumer compliance before NY deployment; (c) Model #880 bias-evaluation evidence pack closed before any further deployment; (d) ORSA materiality determination made before next quarterly enterprise risk forum; (e) re-intake required at any of: face-amount expansion, ECDIS vendor change, EU footprint addition, autonomy structure change.
- Attestation date: 2026-05-09
- Onward routing: ai-risk-tiering; ai-act-triage (Annex III §5(c) routing); model-card-builder; validation-plan; vendor-diligence; board-ai-risk-pack (pending ORSA materiality determination)

#### Why this scenario matters

- It exercises the customer-binding-high case. Customer impact is high; financial impact is medium; regulatory impact is high; operational impact is medium. The tier proposal lands at tier-1, and sponsor and AI Governance Lead concur (no dissent).
- It exercises the insurance overlay end-to-end. AIS Program element coverage, state-by-state DOI bulletin status (CO live, NY pre-deployment, CA pre-deployment), ECDIS provenance, HIPAA-PHI tagging, ORSA materiality check are all on the intake.
- It exercises the conduct-overlay distinction between fairness and unfair discrimination. The intake records Model #880 as the operative legal frame and routes the bias-evaluation evidence question to validation-plan with the right framing.
- It exercises the EU AI Act Annex III §5(c) routing signal. The intake does not classify the use case under the AI Act (that is `ai-act-triage`'s job), but it captures the routing flag because §5(c) (life and health insurance pricing and risk assessment) is the most-frequent FS Annex III trigger and the intake is where it gets caught.
- It exercises the change-plan field on a high-stakes use case. Face-amount expansion, vendor change, EU footprint, autonomy change are each named events tied to re-intake; the use case does not drift inside annual review cadence.
- It exercises the no-foundation-model branch of the architecture block. Not every AI use case is a GenAI use case; the intake structure handles in-house ML cleanly without forcing the GenAI overlay.

## relationship-manager-assistant-bank

### Example: intake for a foundation-model-based RM assistant at a regional bank

Public-source-derived. No named institution. Patterns drawn from NIST AI 600-1 Generative AI Profile (Govern 1.6, Map 1.1), public model and system card precedents from frontier labs as a documentation form factor, and the joint interagency Revised Guidance on Model Risk Management (OCC 2026-13 / FRB SR 26-2 / FDIC FIL-15-2026; supersedes SR 11-7) for traditional-model inventory framing, with the bulletin's GenAI/agentic scope exclusion (footnote 3) noted.

#### Input description

A mid-size US regional bank (commercial banking focus, asset size in the $25-50B band, OCC-supervised national bank) is intaking a foundation-model-based assistant for relationship managers. The assistant ingests internal CRM notes and call summaries plus public earnings transcripts of the RM's coverage portfolio, and produces structured client-meeting prep notes (recent activity recap, talking points, follow-ups). The assistant runs vendor-API foundation model with version pinning, RAG over the firm's CRM corpus and a vendor-supplied earnings-transcript corpus, no tools, no agentic behaviour, advisory-only with the RM editing before any client-facing use. Sponsor (head of commercial-banking RM technology) proposes tier-2.

Engagement scope provided by `scoping`:
- Institution type: national bank, OCC-supervised, asset size $25-50B band, US-only footprint.
- Persona: AI Governance Lead, second line, reporting to the head of model risk.
- Sector overlay: banking. Cross-cutting overlays: cyber (vendor-hosted foundation model is a supply-chain surface; NYDFS Part 500 reach for the NY footprint of part of the commercial portfolio), privacy (CRM contains GLBA-regulated NPI on commercial customers and on individual signatories).
- Source posture: public-plus-firm-policy-plus-evidence.

#### Output sketch

##### 1. Identity and sponsor

- Use case ID: AI-2026-CB-014
- Use case version: 1.0
- Use case name: RM client-meeting prep assistant
- Engagement scope ID: ES-2026-AIGOV-009
- Intake date: 2026-05-06
- Next review due: 2026-11-06 (six months; tier-2 cadence)
- Sponsor business unit: commercial banking
- Accountable first-line owner: head of commercial-banking RM technology
- AI Governance Lead reviewer: AI Governance Lead, model risk function
- Lifecycle stage: limited production (pilot to 30 RMs in two regions)

##### 2. Business purpose and target outcome

The assistant produces structured client-meeting prep notes from internal CRM notes, call summaries, and public earnings transcripts of each RM's coverage portfolio. Target outcome: reduce RM prep time per client meeting from 45 minutes to 15 minutes while maintaining or improving the quality of the structured talking-points (measured by RM acceptance rate on the talking-point list and by post-meeting client follow-through rate). The assistant does not generate client-facing material; the RM edits before any use, and the bank's existing client-communication review applies to anything the RM emails or files.

##### 3. Intended users and decision points

| User role | Decision influenced | Human review point |
|---|---|---|
| Relationship manager | Choice of talking points, follow-up actions, recap framing | RM edits the draft before any internal use; client-communication review applies to any client-facing output |
| RM team lead (sample reviewer) | Quality assurance on assistant output across the team | Weekly sample review; not in the per-meeting flow |

##### 4. Decision impact

| Dimension | Score | Basis |
|---|---|---|
| Customer impact | Low | Internal-use only; RM is the user and the editor; no customer-binding decision |
| Financial impact | Low | Productivity tool; no balance-sheet, capital, or fee impact |
| Regulatory impact | Medium | Firm AI inventory entry under joint interagency Revised Guidance for traditional components and NIST AI RMF Govern for the GenAI use case (the 2026 bulletin excludes GenAI per footnote 3); GLBA Safeguards reach via CRM data; NYDFS Part 500 reach for NY-footprint commercial portfolio |
| Operational impact | Low | Failure of the assistant degrades RM productivity but does not break a critical process |

##### 5. Autonomy level

- Level: human-in-the-loop
- Evidence of effective oversight: weekly sample-review by RM team lead with a structured rubric (accuracy, talking-point relevance, hallucination flag, source-citation completeness); monthly aggregate report to the AI Governance Lead. Sample size 10% of generated notes per RM per week. The sample-review rubric is firm-policy attested.

##### 6. Architecture

- Model type: foundation model
- Deployment posture: vendor API
- Foundation-model identity:
  - Provider: [vendor]
  - Model name: [vendor flagship general-purpose LLM, current generation]
  - Version: [pinned version]
  - Pinning posture: pinned, with floating-with-notice on minor patches
- RAG architecture:
  - Corpora: firm CRM corpus (per-RM scoping, refreshed nightly), vendor-supplied earnings-transcript corpus (vendor-refreshed quarterly)
  - Provenance: firm-controlled for CRM; vendor-supplied for transcripts
- Tool inventory: none (the assistant produces text only; no tool actions)

##### 7. Data sources

| Source | Sensitivity | Field-level tagging | Purpose | Lawful basis |
|---|---|---|---|---|
| Firm CRM corpus | regulated NPI | Customer name, signatory name, account numbers, contact information, internal notes referencing customer financial position | retrieval | Firm's existing customer-information processing under GLBA |
| Vendor-supplied earnings-transcript corpus | public | n/a | retrieval | Public information |

##### 8. Vendor and third-party dependencies

| Vendor | Role | Criticality | Change-of-version notice | Fallback posture |
|---|---|---|---|---|
| [LLM provider] | foundation_model_provider | important | 30-day notice on major version; 7-day on minor patches; rolling not allowed by contract | Switch to fallback LLM provider already evaluated; the assistant is non-critical so a 2-week pause is tolerable |
| [Earnings-transcript corpus provider] | data_provider | standard | Quarterly refresh; vendor SLA on data freshness | Internal manual transcript collection as backup |

##### 9. Regulatory exposure flags

| Flag | Basis | Routes to |
|---|---|---|
| SR_11_7 | Use case is in scope of bank's model definition under §III; inventory entry required | ai-risk-tiering |
| OCC_2026_13 | Bank has migrated to revised guidance; AI/ML inclusion attaches | ai-risk-tiering |
| GLBA_Safeguards | CRM corpus contains regulated NPI; safeguards apply to retrieval and to model serving | ai-risk-tiering, validation-plan |
| NYDFS_Part_500 | NY footprint of commercial portfolio; covered-entity status | ai-risk-tiering |
| NYDFS_AI_letter_2024 | Foundation-model dependence with prompt and retrieval surfaces; covered-entity AI risk | ai-risk-tiering, prompt-injection-risk, genai-pre-prod-review |
| OCC_2023_17_third_party | LLM vendor and transcript-corpus vendor are third parties | vendor-diligence |

##### 10. Preliminary tier proposal

- Proposed tier: tier-2
- Rationale: foundation-model dependence with NPI in the retrieval corpus and NYDFS Part 500 covered-entity reach push the tier up from a tier-3 advisory-only baseline. Customer-binding is absent and autonomy is human-in-the-loop with sampled effective-oversight evidence. The formal tier is decided downstream.

##### 11. Proposed review gates and human oversight

| Gate | Owner function | Frequency | Stop condition |
|---|---|---|---|
| Independent validation (targeted, focused on hallucination, citation accuracy, NPI handling) | model risk team | Pre-prod and semi-annual | Hallucination rate above firm threshold or NPI leakage detected in output |
| AI risk committee approval | AI risk committee secretary | Pre-prod and on material change | Conditional approval revoked |
| Pre-prod gate | AI Governance Lead | One-time | Pre-prod gate fails |
| Vendor diligence (foundation-model vendor evidence review) | vendor management with AI governance | Annual and on vendor swap | Vendor evidence pack does not meet firm criteria |
| Monitoring cadence | model risk team | Quarterly | Performance breach for two consecutive periods |
| Sample-review by RM team lead | commercial banking | Weekly | Aggregate quality score below firm threshold |

##### 12. Open questions for second-line follow-up

| Question | Routes to | Owner | Due date |
|---|---|---|---|
| What is the prompt-injection exposure given that CRM notes contain unstructured customer-supplied content (emails, call notes including customer dictation)? | prompt-injection-risk | AI governance with CISO | 2026-06-15 |
| What is the NPI-leakage test posture in vendor evaluation? Vendor-supplied red-team evidence covers their hosted environment, not our retrieval corpus. | validation-plan | model risk team | 2026-06-15 |
| Should a separate model card cover the talking-point summaries vs the recap framing? Architecture is the same but the audience for the limitations differs. | model-card-builder | AI governance | 2026-06-30 |
| Vendor pinning posture is "pinned with floating on minor patches" — is the patch-monitoring instrumented to catch a behavior change in the patch window? | vendor-diligence | vendor management | 2026-07-15 |

##### 13. Twelve-month change plan

- Named owner: head of commercial-banking RM technology
- Scope changes: planned expansion from 30 RMs in two regions to all 240 RMs across all regions in Q3 2026; planned addition of three more business lines' CRM corpora (private banking, treasury management, asset-based lending) in Q4 2026.
- Autonomy uplift: planned addition of a "draft client follow-up email" feature in Q1 2027 (this would change the client-facing posture and triggers re-intake plus pre-prod gate).
- Customer surface expansion: none planned in the twelve-month window for the assistant itself; the planned Q1 2027 follow-up email feature is a customer-surface change and triggers re-intake.
- Vendor changes: vendor-evaluation cycle in Q4 2026 may result in switch to fallback LLM provider; either outcome triggers re-intake.

##### 14. Sector and cross-cutting overlay flags

- Sector overlay applied: banking
- Cross-cutting overlays applied: cyber, privacy
- Overlay-specific notes: banking overlay flags the firm AI inventory entry under the joint interagency Revised Guidance for traditional components and NIST AI RMF for the GenAI use case (the bulletin excludes GenAI per footnote 3), plus CFPB authority on consumer-NPI handling; cyber overlay flags NYDFS Part 500 covered-entity status and the foundation-model supply-chain surface; privacy overlay flags GLBA Safeguards reach and the field-level NPI tagging requirement on the CRM corpus.

##### 15. AI Act overlap

- High-risk overlap likely: no
- Annex III categories flagged: none
- Provider or deployer role: deployer (the firm is a deployer of a vendor-supplied foundation model; not a provider)
- Routed to ai-act-triage: no (US-only footprint; flagged for re-look if EU client base added)

##### 16. Source trace and confidence

| Claim | Source | Evidence reference | Confidence |
|---|---|---|---|
| Foundation-model identity and pinning posture | Vendor contract addendum and vendor system card | Contract §4.2; vendor system card v3.1 | High (firm-controlled contract); medium (vendor-self-attestation on system-card content) |
| RAG corpus scope and refresh | Firm system design document | SDD-2026-CB-014 §3 | High |
| GLBA NPI in CRM | Firm data-classification register | DC-Reg row CRM-CB-001 | High |
| NYDFS Part 500 covered-entity status | Firm regulatory register | Reg-Reg row NY-2023-002 | High |
| Sample-review effective-oversight evidence | Firm-policy-attested sample-review rubric | Rubric SR-2026-014 | High |
| Pilot scope (30 RMs, two regions) | Sponsor brief | Brief SB-2026-014 | High |

#### Reviewer attestation (sketch)

- Reviewer role: AI Governance Lead, model risk function
- Decision: accept with conditions
- Conditions: (a) prompt-injection-risk open question closed before pre-prod gate; (b) NPI-leakage test posture documented in vendor diligence pack before pre-prod gate; (c) re-intake required at any of: scope expansion to additional business lines, autonomy uplift to client-facing email, vendor swap.
- Attestation date: 2026-05-09
- Onward routing: ai-risk-tiering; ai-act-triage (for the deferred re-look flag); model-card-builder; validation-plan; vendor-diligence; prompt-injection-risk

#### Why this scenario matters

- It exercises the GenAI overlay block. Foundation-model identity, pinning posture, RAG corpus naming, and the absence of tools are captured explicitly. NIST AI 600-1 Govern 1.6 / Map 1.1 anchor the GenAI inventory entry.
- It exercises the customer-impact-low + regulatory-medium + privacy-flagged combination. Customer impact is the dominant tier-1 trigger when present; here it is absent and the tier proposal lands at tier-2 because of foundation-model dependence with NPI in the retrieval corpus and NYDFS reach.
- It exercises the autonomy-evidence test. Sample-review at 10% per RM per week, with a structured rubric and aggregate reporting, is what effective-oversight evidence looks like; "the RM edits before use" alone is not.
- It exercises the change-plan field. The planned Q1 2027 follow-up email feature is a known customer-surface change; the change plan flags it as a re-intake trigger rather than letting the use case drift.
- It exercises the open-questions routing discipline. Each question is tagged to a downstream skill with an owner and a due date.

## troubleshooting

### Troubleshooting: ai-use-case-intake

Recurring defects in intake records. The intake is the front-door artefact; defects here propagate into every downstream skill that consumes the record. This file is for second-line reviewers and AI Governance Leads challenging an intake before attestation, and for senior practitioners self-reviewing their own draft.

#### Foundation-model identity is missing or vague

Symptom: the intake records `model_type = foundation_model` but the foundation-model identity block is empty, vague ("vendor LLM"), or missing the version and pinning posture.

Root cause: the model owner submitted the intake without confirming with the build team which foundation model is in use, or the build team treated the foundation model as an implementation detail.

Fix: the foundation-model identity (provider, model name, version, pinning posture) is load-bearing for `ai-risk-tiering`, `model-card-builder`, `validation-plan`, `prompt-injection-risk`, `rag-evaluation-review`, `genai-pre-prod-review`, and `llm-vendor-evidence-review`. Hold the intake at "accept with conditions" until the block is filled. "Pinned with floating on minor patches" is a different posture from "rolling without notice" and the intake distinguishes them.

#### Autonomy level is "human-in-the-loop" but the human review point is rubber-stamp at scale

Symptom: the intake records `autonomy_level = human_in_loop` and the evidence-of-effective-oversight field says "the staff member reviews the output before any use." On inspection, the staff member approves at scale without inspecting (button-push approval; tens of decisions per minute).

Root cause: the intake is recording the existence of a button rather than the evidence that the human review point is effective oversight under NIST Map 3.5 and EU AI Act Article 14.

Fix: surface the autonomy posture as `human_on_loop` or `fully_automated` based on observed behavior, and route an open question to `validation-plan` to test the effective-oversight evidence. Where the evidence is genuinely thin, flag the autonomy level as an open question rather than over-claiming the human-in-the-loop label. The intake is honest about what is observed; the gap is the work product, not a defect to hide.

#### Data sensitivity tagged source-level instead of field-level

Symptom: a data source labelled "CRM extract — internal" turns out to contain regulated NPI fields (account numbers, signatory data, customer financial position) inside an otherwise internal aggregate source.

Root cause: source-level tagging is faster, but it hides exposure inside aggregate sources. The downstream tier reviewer cannot score data sensitivity off a source-level tag alone.

Fix: any data source flagged regulated NPI, regulated PHI, regulated PCI, or biometric requires field-level tagging in the `field_level_tagging` field. Hold the intake until the field-level breakout is supplied for each regulated source. The field-level breakout also feeds the privacy overlay's vendor-flow-down questions.

#### Sponsor has been pushing the tier downward

Symptom: the preliminary-tier proposal is tier-3 or tier-4 on a use case that has customer-binding decisions, regulated NPI, foundation-model dependence, or multi-state DOI reach. The rationale is thin or names "low complexity" or "internal-use only" without engaging with the customer or regulatory dimensions.

Root cause: a low tier reduces validation depth, reduces gate count, and accelerates time-to-deployment. Sponsor pressure runs both directions; downward is the more frequent direction at intake.

Fix: capture the proposal as the sponsor's view; do not edit it down. The formal tier is decided by `ai-risk-tiering` against the intake record, and the dissent line in the tier decision records the disagreement when it stands. Route an open question to `ai-risk-tiering` flagging the contested factors (customer impact, regulatory impact, GenAI block) so the tier reviewer is on notice.

#### GenAI overlay block is empty on a foundation-model intake

Symptom: the intake records `model_type = foundation_model` or `uses_rag = true` or `uses_tools = true`, but the GenAI block (foundation-model identity, RAG corpora and refresh cadence, tool inventory and tool-boundary controls) is sparse or absent.

Root cause: the intake template was filled in linearly without checking whether the architecture flags fired the overlay; the model owner did not know the GenAI block was mandatory once triggered.

Fix: missing the GenAI block on a GenAI intake is what `ai-risk-tiering` flags first when the record lands. Hold the intake at "accept with conditions" until the GenAI block is filled. The block is mandatory once any of the three architecture flags fires.

#### Open-questions list is empty on a non-trivial use case

Symptom: the intake's open-questions table is empty on a tier-2 or tier-1 candidate use case with foundation-model dependence, regulated data, or customer-binding posture.

Root cause: either the use case is genuinely tier-4 with no exposure (rare for any use case worth intaking), or the open questions were sanitised to make the intake look clean. Senior reviewers look for the second case more than the first.

Fix: open questions are not defects; they are the work-in-flight handoff to downstream skills. Surface the questions that actually exist with their downstream-skill routing destinations and owners. A clean intake with an empty open-questions list reads to a senior reviewer as a tell that the conversation has not happened.

#### Vendor dependency block records a vendor without the change-of-version posture

Symptom: a foundation-model vendor or an ECDIS vendor is named with role and criticality, but the change-of-version notice posture and the firm-side fallback are blank.

Root cause: the contract addendum was not consulted; the build team treated the vendor as a black box.

Fix: change-of-version notice is the operative resilience posture for any vendor whose model behaviour can shift outside the firm's change-control loop. Pull the contract clause and record the posture (e.g., "30-day notice on major version; 7-day on minor patches; rolling not allowed"). Where the contract is silent, flag as an open question for `vendor-diligence` and consider holding the intake.

#### EU AI Act Annex III overlap was not flagged

Symptom: the intake is for a US-based credit-decisioning use case, life-insurance underwriting use case, or biometric-identification use case, but the AI Act overlap block reads `high_risk_overlap_likely = false` or is empty.

Root cause: the model owner thought "we don't operate in the EU" was the test for AI Act applicability; in fact the test is whether the use case category is in scope under Article 6 / Annex III, and the routing flag belongs in the intake regardless of EU footprint today.

Fix: the AI Act block in the intake is the routing flag, not the formal classification. The formal classification is owned by `ai-act-triage`. Capture the Annex III category overlap (creditworthiness assessment of natural persons §5(b), risk assessment and pricing in life and health insurance §5(c), biometric identification §1) regardless of EU footprint, and route to `ai-act-triage` for the formal call. The overlap flag also serves as a re-look prompt if EU footprint enters scope.

#### Intake is dated more than a quarter old with no version bump

Symptom: the use case is in active production, has had scope or vendor changes, but the intake record is the v1.0 from six months ago.

Root cause: the intake is being treated as a one-time form rather than a living record; the change plan was either blank or not monitored.

Fix: the intake is a living record. A new version is recorded at any of: scope change, autonomy change, customer-surface change, vendor change, regulatory-environment change, lifecycle stage transition. The change-plan field is what catches drift before the use case grows beyond its intake. Where the intake is stale, hold any downstream re-tier or model-card refresh until the intake is re-versioned.

#### Sector overlay was loaded but the overlay-specific fields are not in the intake

Symptom: the intake records `overlay_flags = ["banking"]` but the banking-specific intake fields (federal regulator, supervisory cycle posture, BSA officer linkage where applicable, sponsor-bank arrangement counterparty, stress-testing pedigree, risk-appetite-statement linkage) are absent.

Root cause: the overlay was loaded as a routing signal for downstream skills, but the overlay's intake-side fields were not consulted at intake time.

Fix: when an overlay is loaded, the overlay's named fields land in the intake. Treating the overlay as background reading is the failure mode. Each sector overlay (`references/sector-overlays.md#<sector>`) lists the sector-specific intake fields; consult the overlay file when filling the intake.

#### Source trace collapses vendor and firm evidence into one line

Symptom: a claim about the foundation model's training-data provenance, fairness evaluation, or safety testing is recorded with `confidence = high` and the source is "vendor".

Root cause: vendor-supplied facts about the vendor's own model carry vendor-self-attestation confidence (typically low to medium); firm-controlled facts carry higher confidence. Collapsing them hides the seam.

Fix: separate vendor-self-attestation evidence from firm-independent evaluation evidence in the source trace. Confidence labels on vendor-supplied facts max at medium absent firm-side independent verification; firm-controlled facts (own contracts, own data classification register, own monitoring rubrics) can be high. The seam between vendor and firm evidence is what `llm-vendor-evidence-review` works against downstream.

#### Intake is being filed on a use case that should re-route to a different skill

Symptom: the intake is being attempted on a use case that has already been intaked and tiered, and the question is the model card or validation plan; or the work is procurement-stage diligence on an AI vendor before any internal use case exists; or the artifact required is the EU AI Act Annex IV technical documentation.

Root cause: the wrong skill was reached for; the intake is the front door but it is not the only door.

Fix: route the work. If the use case is intaked and tiered and the next artifact is the model card, route to `model-card-builder`. If procurement-stage diligence is needed, route to `vendor-diligence` in `third-party-operational-resilience` with the AI-vendor scenario mode. If Annex IV technical documentation is the artifact, route to `ai-act-triage` to scope the deltas the firm carries. The intake skill is for use cases that need the front-door record; do not force-fit it where another skill owns the work.
