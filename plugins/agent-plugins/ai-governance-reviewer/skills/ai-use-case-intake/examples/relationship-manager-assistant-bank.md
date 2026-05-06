# Example: intake for a foundation-model-based RM assistant at a regional bank

Public-source-derived. No named institution. Patterns drawn from NIST AI 600-1 Generative AI Profile (Govern 1.6, Map 1.1), public model and system card precedents from frontier labs as a documentation form factor, and the SR 11-7 / OCC Bulletin 2026-13 model definition and inventory framing.

## Input description

A mid-size US regional bank (commercial banking focus, asset size in the $25-50B band, OCC-supervised national bank) is intaking a foundation-model-based assistant for relationship managers. The assistant ingests internal CRM notes and call summaries plus public earnings transcripts of the RM's coverage portfolio, and produces structured client-meeting prep notes (recent activity recap, talking points, follow-ups). The assistant runs vendor-API foundation model with version pinning, RAG over the firm's CRM corpus and a vendor-supplied earnings-transcript corpus, no tools, no agentic behaviour, advisory-only with the RM editing before any client-facing use. Sponsor (head of commercial-banking RM technology) proposes tier-2.

Engagement scope provided by `engagement-scoping`:
- Institution type: national bank, OCC-supervised, asset size $25-50B band, US-only footprint.
- Persona: AI Governance Lead, second line, reporting to the head of model risk.
- Sector overlay: banking. Cross-cutting overlays: cyber (vendor-hosted foundation model is a supply-chain surface; NYDFS Part 500 reach for the NY footprint of part of the commercial portfolio), privacy (CRM contains GLBA-regulated NPI on commercial customers and on individual signatories).
- Source posture: public-plus-firm-policy-plus-evidence.

## Output sketch

### 1. Identity and sponsor

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

### 2. Business purpose and target outcome

The assistant produces structured client-meeting prep notes from internal CRM notes, call summaries, and public earnings transcripts of each RM's coverage portfolio. Target outcome: reduce RM prep time per client meeting from 45 minutes to 15 minutes while maintaining or improving the quality of the structured talking-points (measured by RM acceptance rate on the talking-point list and by post-meeting client follow-through rate). The assistant does not generate client-facing material; the RM edits before any use, and the bank's existing client-communication review applies to anything the RM emails or files.

### 3. Intended users and decision points

| User role | Decision influenced | Human review point |
|---|---|---|
| Relationship manager | Choice of talking points, follow-up actions, recap framing | RM edits the draft before any internal use; client-communication review applies to any client-facing output |
| RM team lead (sample reviewer) | Quality assurance on assistant output across the team | Weekly sample review; not in the per-meeting flow |

### 4. Decision impact

| Dimension | Score | Basis |
|---|---|---|
| Customer impact | Low | Internal-use only; RM is the user and the editor; no customer-binding decision |
| Financial impact | Low | Productivity tool; no balance-sheet, capital, or fee impact |
| Regulatory impact | Medium | SR 11-7 / OCC 2026-13 inventory entry required; GLBA Safeguards reach via CRM data; NYDFS Part 500 reach for NY-footprint commercial portfolio |
| Operational impact | Low | Failure of the assistant degrades RM productivity but does not break a critical process |

### 5. Autonomy level

- Level: human-in-the-loop
- Evidence of effective oversight: weekly sample-review by RM team lead with a structured rubric (accuracy, talking-point relevance, hallucination flag, source-citation completeness); monthly aggregate report to the AI Governance Lead. Sample size 10% of generated notes per RM per week. The sample-review rubric is firm-policy attested.

### 6. Architecture

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

### 7. Data sources

| Source | Sensitivity | Field-level tagging | Purpose | Lawful basis |
|---|---|---|---|---|
| Firm CRM corpus | regulated NPI | Customer name, signatory name, account numbers, contact information, internal notes referencing customer financial position | retrieval | Firm's existing customer-information processing under GLBA |
| Vendor-supplied earnings-transcript corpus | public | n/a | retrieval | Public information |

### 8. Vendor and third-party dependencies

| Vendor | Role | Criticality | Change-of-version notice | Fallback posture |
|---|---|---|---|---|
| [LLM provider] | foundation_model_provider | important | 30-day notice on major version; 7-day on minor patches; rolling not allowed by contract | Switch to fallback LLM provider already evaluated; the assistant is non-critical so a 2-week pause is tolerable |
| [Earnings-transcript corpus provider] | data_provider | standard | Quarterly refresh; vendor SLA on data freshness | Internal manual transcript collection as backup |

### 9. Regulatory exposure flags

| Flag | Basis | Routes to |
|---|---|---|
| SR_11_7 | Use case is in scope of bank's model definition under §III; inventory entry required | ai-risk-tiering |
| OCC_2026_13 | Bank has migrated to revised guidance; AI/ML inclusion attaches | ai-risk-tiering |
| GLBA_Safeguards | CRM corpus contains regulated NPI; safeguards apply to retrieval and to model serving | ai-risk-tiering, validation-plan |
| NYDFS_Part_500 | NY footprint of commercial portfolio; covered-entity status | ai-risk-tiering |
| NYDFS_AI_letter_2024 | Foundation-model dependence with prompt and retrieval surfaces; covered-entity AI risk | ai-risk-tiering, prompt-injection-risk, genai-pre-prod-review |
| OCC_2023_17_third_party | LLM vendor and transcript-corpus vendor are third parties | vendor-diligence |

### 10. Preliminary tier proposal

- Proposed tier: tier-2
- Rationale: foundation-model dependence with NPI in the retrieval corpus and NYDFS Part 500 covered-entity reach push the tier up from a tier-3 advisory-only baseline. Customer-binding is absent and autonomy is human-in-the-loop with sampled effective-oversight evidence. The formal tier is decided downstream.

### 11. Proposed review gates and human oversight

| Gate | Owner function | Frequency | Stop condition |
|---|---|---|---|
| Independent validation (targeted, focused on hallucination, citation accuracy, NPI handling) | model risk team | Pre-prod and semi-annual | Hallucination rate above firm threshold or NPI leakage detected in output |
| AI risk committee approval | AI risk committee secretary | Pre-prod and on material change | Conditional approval revoked |
| Pre-prod gate | AI Governance Lead | One-time | Pre-prod gate fails |
| Vendor diligence (foundation-model vendor evidence review) | vendor management with AI governance | Annual and on vendor swap | Vendor evidence pack does not meet firm criteria |
| Monitoring cadence | model risk team | Quarterly | Performance breach for two consecutive periods |
| Sample-review by RM team lead | commercial banking | Weekly | Aggregate quality score below firm threshold |

### 12. Open questions for second-line follow-up

| Question | Routes to | Owner | Due date |
|---|---|---|---|
| What is the prompt-injection exposure given that CRM notes contain unstructured customer-supplied content (emails, call notes including customer dictation)? | prompt-injection-risk | AI governance with CISO | 2026-06-15 |
| What is the NPI-leakage test posture in vendor evaluation? Vendor-supplied red-team evidence covers their hosted environment, not our retrieval corpus. | validation-plan | model risk team | 2026-06-15 |
| Should a separate model card cover the talking-point summaries vs the recap framing? Architecture is the same but the audience for the limitations differs. | model-card-builder | AI governance | 2026-06-30 |
| Vendor pinning posture is "pinned with floating on minor patches" — is the patch-monitoring instrumented to catch a behavior change in the patch window? | vendor-diligence | vendor management | 2026-07-15 |

### 13. Twelve-month change plan

- Named owner: head of commercial-banking RM technology
- Scope changes: planned expansion from 30 RMs in two regions to all 240 RMs across all regions in Q3 2026; planned addition of three more business lines' CRM corpora (private banking, treasury management, asset-based lending) in Q4 2026.
- Autonomy uplift: planned addition of a "draft client follow-up email" feature in Q1 2027 (this would change the client-facing posture and triggers re-intake plus pre-prod gate).
- Customer surface expansion: none planned in the twelve-month window for the assistant itself; the planned Q1 2027 follow-up email feature is a customer-surface change and triggers re-intake.
- Vendor changes: vendor-evaluation cycle in Q4 2026 may result in switch to fallback LLM provider; either outcome triggers re-intake.

### 14. Sector and cross-cutting overlay flags

- Sector overlay applied: banking
- Cross-cutting overlays applied: cyber, privacy
- Overlay-specific notes: banking overlay flags SR 11-7 / OCC 2026-13 inventory and CFPB authority on consumer-NPI handling; cyber overlay flags NYDFS Part 500 covered-entity status and the foundation-model supply-chain surface; privacy overlay flags GLBA Safeguards reach and the field-level NPI tagging requirement on the CRM corpus.

### 15. AI Act overlap

- High-risk overlap likely: no
- Annex III categories flagged: none
- Provider or deployer role: deployer (the firm is a deployer of a vendor-supplied foundation model; not a provider)
- Routed to ai-act-triage: no (US-only footprint; flagged for re-look if EU client base added)

### 16. Source trace and confidence

| Claim | Source | Evidence reference | Confidence |
|---|---|---|---|
| Foundation-model identity and pinning posture | Vendor contract addendum and vendor system card | Contract §4.2; vendor system card v3.1 | High (firm-controlled contract); medium (vendor-self-attestation on system-card content) |
| RAG corpus scope and refresh | Firm system design document | SDD-2026-CB-014 §3 | High |
| GLBA NPI in CRM | Firm data-classification register | DC-Reg row CRM-CB-001 | High |
| NYDFS Part 500 covered-entity status | Firm regulatory register | Reg-Reg row NY-2023-002 | High |
| Sample-review effective-oversight evidence | Firm-policy-attested sample-review rubric | Rubric SR-2026-014 | High |
| Pilot scope (30 RMs, two regions) | Sponsor brief | Brief SB-2026-014 | High |

## Reviewer attestation (sketch)

- Reviewer role: AI Governance Lead, model risk function
- Decision: accept with conditions
- Conditions: (a) prompt-injection-risk open question closed before pre-prod gate; (b) NPI-leakage test posture documented in vendor diligence pack before pre-prod gate; (c) re-intake required at any of: scope expansion to additional business lines, autonomy uplift to client-facing email, vendor swap.
- Attestation date: 2026-05-09
- Onward routing: ai-risk-tiering; ai-act-triage (for the deferred re-look flag); model-card-builder; validation-plan; vendor-diligence; prompt-injection-risk

## Why this scenario matters

- It exercises the GenAI overlay block. Foundation-model identity, pinning posture, RAG corpus naming, and the absence of tools are captured explicitly. NIST AI 600-1 Govern 1.6 / Map 1.1 anchor the GenAI inventory entry.
- It exercises the customer-impact-low + regulatory-medium + privacy-flagged combination. Customer impact is the dominant tier-1 trigger when present; here it is absent and the tier proposal lands at tier-2 because of foundation-model dependence with NPI in the retrieval corpus and NYDFS reach.
- It exercises the autonomy-evidence test. Sample-review at 10% per RM per week, with a structured rubric and aggregate reporting, is what effective-oversight evidence looks like; "the RM edits before use" alone is not.
- It exercises the change-plan field. The planned Q1 2027 follow-up email feature is a known customer-surface change; the change plan flags it as a re-intake trigger rather than letting the use case drift.
- It exercises the open-questions routing discipline. Each question is tagged to a downstream skill with an owner and a due date.
