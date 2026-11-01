# AI use case intake record: [use-case ID, version]

Starting structure for an AI use case intake record. The intake is short on purpose; it captures judgment-shaped facts about scope, exposure, and dependencies so downstream tier, AI Act triage, model card, and validation can run against a record an examiner can read. Validation evidence and controls inventory come downstream; the intake is the front door.

The record is a draft until the AI Governance Lead (or named equivalent) attests.

---

## 1. Identity and sponsor

- Use case ID: [canonical firm ID, stable across versions]
- Use case version: [v1.0 / v1.1 / etc; intake is a living record]
- Use case name: [short human-readable; plain English, no marketing language]
- Engagement scope ID (if `scoping` was run): [ID]
- Intake date: [YYYY-MM-DD]
- Next review due: [YYYY-MM-DD]
- Sponsor business unit: [unit]
- Accountable first-line owner: [role / function, never a named individual]
- AI Governance Lead reviewer: [role / function]
- Lifecycle stage: [idea / POC / limited production / full production / retirement]

---

## 2. Business purpose and target outcome

[One paragraph in plain language. What the use case does, what business outcome it supports, why this approach over the alternative. Target outcome is what success looks like, in terms a reviewer can sample against.]

---

## 3. Intended users and decision points

| User role | Decision influenced | Human review point |
|---|---|---|
| [internal staff role / customer segment / third-party role / agentic caller] | [what the use case influences for this user role] | [where the human review point sits in the flow, or "no human review point" if absent] |

---

## 4. Decision impact

| Dimension | Score | Basis |
|---|---|---|
| Customer impact | [none / low / medium / high] | [one-line basis] |
| Financial impact | [...] | [...] |
| Regulatory impact | [...] | [...] |
| Operational impact | [...] | [...] |

Notes:

- Customer impact covers customer-binding decisions, customer-facing surfaces, and indirect customer-outcome effects.
- Financial impact covers balance-sheet, capital, liquidity, material P&L exposure.
- Regulatory impact covers named regulator reach.
- Operational impact covers process criticality and operational-resilience exposure if the use case fails.

---

## 5. Autonomy level

- Level: [human-in-the-loop / human-on-the-loop / fully automated / agentic with tool use]
- Evidence of effective oversight (NIST Map 3.5 / EU AI Act Article 14): [evidence the human review point is effective oversight, not rubber-stamp at scale; or `[evidence needed]` flagged as an open question]

---

## 6. Architecture

- Model type: [traditional statistical / ML / foundation model / agentic]
- Deployment posture: [in-house / vendor API / on-prem vendor / hybrid]
- Foundation-model identity (when applicable):
  - Provider: [provider]
  - Model name: [model name]
  - Version: [version]
  - Pinning posture: [pinned / floating with notice / rolling without notice]
- RAG architecture (when applicable):
  - Corpora: [corpus name(s) with retrieval scoping rules and refresh cadence]
  - Provenance: [firm-controlled / vendor-supplied / hybrid]
- Tool inventory (when applicable):
  - Tool name and actions: [each tool with the actions it can take]
  - Tool-boundary controls: [controls limiting tool action scope]

The GenAI block (foundation-model identity, RAG corpora, tool inventory) is mandatory when `model_type = foundation_model` or `uses_rag = true` or `uses_tools = true`. Missing the foundation-model identity, RAG corpus inventory, or tool inventory on a GenAI intake is what `ai-risk-tiering` flags first.

---

## 7. Data sources

| Source | Sensitivity | Field-level tagging (if regulated) | Purpose | Lawful basis |
|---|---|---|---|---|
| [source name] | [public / internal / confidential / regulated NPI / regulated PHI / regulated PCI / biometric / customer-supplied prompt content / children's data] | [field-level categories within the source; required for any regulated source] | [training / fine-tuning / retrieval / evaluation / monitoring / reference] | [lawful basis or consent posture where applicable] |

---

## 8. Vendor and third-party dependencies

| Vendor | Role | Criticality | Change-of-version notice | Fallback posture |
|---|---|---|---|---|
| [vendor] | [foundation-model provider / model-serving infrastructure / RAG infrastructure / evaluation provider / data provider / sponsor bank / processor / other] | [critical / important / standard] | [contractual posture for change-of-version notice] | [firm-side fallback if the vendor exits or fails] |

---

## 9. Regulatory exposure flags

| Flag | Basis | Routes to |
|---|---|---|
| [SR_11_7 / OCC_2026_13 / EU_AI_Act_Annex_III_5b / EU_AI_Act_Article_17 / NYDFS_Part_500 / NYDFS_AI_letter_2024 / CFPB_Circular_2022_03 / NAIC_Bulletin_AI_2023 / CO_SB_21_169 / NY_DFS_Circular_AI_2024 / SEC_Marketing_Rule / SEC_204_2_books_records / FFIEC_BSA_AML / GLBA_Safeguards / HIPAA / OCC_2023_17_third_party / July_2024_bank_fintech] | [one-line basis] | [downstream skill that picks up the flag] |

---

## 10. Preliminary tier proposal

- Proposed tier: [tier-1 / tier-2 / tier-3 / tier-4 / unclassified]
- Rationale: [one paragraph; what the model owner thinks. The formal tier is decided downstream by `ai-risk-tiering`.]

---

## 11. Proposed review gates and human oversight

| Gate | Owner function | Frequency | Stop condition |
|---|---|---|---|
| [independent validation / AI risk committee approval / pre-prod gate / vendor diligence / monitoring cadence / complaint surveillance] | [function, never a named individual] | [one-time / annual / quarterly / on-trigger] | [what halts the use case if the gate fails] |

---

## 12. Open questions for second-line follow-up

| Question | Routes to | Owner | Due date |
|---|---|---|---|
| [question] | [ai-risk-tiering / ai-act-triage / model-card-builder / validation-plan / agentic-ai-controls / vendor-diligence / prompt-injection-risk / rag-evaluation-review / genai-pre-prod-review / llm-vendor-evidence-review] | [function] | [YYYY-MM-DD] |

A clean intake with an empty open-questions list is either tier-4 with no exposure, or had its open questions sanitised. Senior reviewers look for the second case more than the first.

---

## 13. Twelve-month change plan

- Named owner: [function]
- Scope changes: [planned scope changes]
- Autonomy uplift: [planned autonomy changes (e.g., adding tool use, reducing human-in-the-loop)]
- Customer surface expansion: [planned customer-surface expansion]
- Vendor changes: [planned vendor changes]

A blank field with a recent intake date and an active use case is a tell that the conversation has not happened. Tier and gates set on a snapshot drift within a quarter.

---

## 14. Sector and cross-cutting overlay flags

- Sector overlay applied: [banking / insurance / capital-markets / payments-fintech / none]
- Cross-cutting overlays applied: [cyber / privacy / conduct / none]
- Overlay-specific notes: [pointers to overlay-specific lines in the intake]

---

## 15. AI Act overlap

- High-risk overlap likely: [yes / no]
- Annex III categories flagged: [creditworthiness assessment of natural persons §5(b) / risk assessment and pricing in life and health insurance §5(c) / biometric identification §1 / employment §4 / education §3 / law enforcement §6 / migration §7 / democratic process §8 / critical infrastructure §2 / none]
- Provider or deployer role: [provider / deployer / both / unknown]
- Routed to `ai-act-triage`: [yes / no]

The formal AI Act classification is owned by `ai-act-triage`. This block is the routing flag.

---

## 16. Source trace and confidence

For every material claim in the intake (use case scope, autonomy posture, architecture, data source sensitivity, vendor dependencies, regulatory flags, decision impact):

| Claim | Source | Evidence reference | Confidence |
|---|---|---|---|
| [claim] | [intake conversation / sponsor memo / vendor proposal / system design document / vendor system card / prior intake version / `[evidence needed]`] | [pointer] | [high / medium / low / evidence-needed] |

`[evidence needed]` items either close before the intake is filed or route to the open-questions list with an owner and a due date.

---

## Reviewer attestation

The record is reviewable when the architecture is named, the data sources are tagged, the regulatory flags are set with their routing destinations, the open questions are routed to downstream skills, and the source trace is filled.

- Reviewer role: [AI Governance Lead, function]
- Decision: [accept intake / accept with conditions / hold for input]
- Conditions (if any): [conditions, owners, dates]
- Attestation date: [YYYY-MM-DD]
- Onward routing: [ai-risk-tiering / ai-act-triage / model-card-builder / validation-plan / agentic-ai-controls / vendor-diligence / llm-vendor-evidence-review / AI inventory of record]

The record is filed only after attestation.
