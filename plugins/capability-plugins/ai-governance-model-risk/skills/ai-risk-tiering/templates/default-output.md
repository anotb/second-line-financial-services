# Risk-tier decision record: [use-case ID, version]

Starting structure for a tier decision record. The decision is short on purpose; tiering is judgment, not artifact-padding. The reader is the AI risk committee secretary or the model risk lead, not the model owner.

The record is a draft until the named decider attests.

---

## 1. Use case identity

- Use case ID: [canonical firm ID, links to `ai-use-case-intake`]
- Use case version: [intake record version this tier is decided against]
- Engagement scope ID (if `engagement-scoping` was run): [ID]
- Decision date: [YYYY-MM-DD]
- Decided by: [role, function]

---

## 2. Tier decision

- Tier: [tier-1 / tier-2 / tier-3 / tier-4]
- Tier rationale: [two to four sentences. Names the dominant factors, the regulator constellation, and why the tier is what it is. Reads the way an examiner would read it.]

---

## 3. Factor scoring

Every named factor is scored or marked `n/a` with a reason. Empty factors are not acceptable; an unsupported `n/a` is a tell that the rubric was collapsed to one factor.

| Factor | Score | Weight | Justification | Source |
|---|---|---|---|---|
| customer_impact | [high / medium / low / n/a] | [dominant / contributing / secondary] | [one to three sentences] | [intake field, regulatory citation, firm policy] |
| financial_impact | [...] | [...] | [...] | [...] |
| regulatory_impact | [...] | [...] | [...] | [...] |
| ai_act_category | [...] | [...] | [...] | [...] |
| autonomy_level | [...] | [...] | [...] | [...] |
| data_sensitivity | [...] | [...] | [...] | [...] |
| model_concentration | [...] | [...] | [...] | [...] |
| vendor_dependence | [...] | [...] | [...] | [...] |
| cyber_exposure | [...] | [...] | [...] | [...] |
| conduct_exposure | [...] | [...] | [...] | [...] |
| genai_specific | [...] | [...] | [...] | [...] |
| sector_specific | [...] | [...] | [...] | [...] |

Notes:

- `customer_impact` covers customer-binding decisions, customer-facing surfaces, and indirect customer-outcome effects.
- `financial_impact` covers balance-sheet, capital, liquidity, and material P&L exposure.
- `regulatory_impact` covers named regulator reach (federal, state, foreign), examination posture, and supervisory-letter exposure.
- `ai_act_category` is the routing flag to `ai-act-triage`, not the formal classification.
- `autonomy_level` covers advisory through agentic-with-tool-use through fully-autonomous.
- `data_sensitivity` covers regulated NPI / PHI / PCI, customer-supplied prompt content, biometric data, children's data.
- `model_concentration` covers single-model dominance in a decision flow with no challenger or fallback.
- `vendor_dependence` covers foundation-model vendor, RAG infrastructure vendor, scoring-engine vendor.
- `cyber_exposure` covers prompt-injection surface, training-data poisoning surface, supply-chain dependence, AI-enabled social engineering.
- `conduct_exposure` covers customer-binding decisions, fairness exposure, complaint vector, market integrity.
- `genai_specific` covers foundation-model dependence, RAG corpus drift, hallucination exposure, content-provenance, autonomy-level uplift via tool use.
- `sector_specific` is the elevation from the loaded sector overlay (banking, insurance, capital-markets, payments-fintech).

---

## 4. Triggered gates

| Gate | Owner | Frequency | Stop condition |
|---|---|---|---|
| [Independent validation / pre-prod gate / AI risk committee approval / vendor diligence / monitoring cadence] | [function, never a named individual] | [one-time / annual / quarterly / on-trigger] | [what halts the use case if the gate fails] |

The gates are derived from tier and from sector overlays. The default mapping (firm policy may shift these):

| Tier | Validation depth | Monitoring frequency | Committee route |
|---|---|---|---|
| tier-1 | full | quarterly or continuous | AI risk committee |
| tier-2 | full or targeted | quarterly | model risk committee |
| tier-3 | targeted | semi-annual | model risk team |
| tier-4 | light-touch or monitor-only | annual | model owner with second-line concurrence |

---

## 5. Sector and cross-cutting overlay flags

- Sector overlays applied: [banking / insurance / capital-markets / payments-fintech / none]
- Cross-cutting overlays applied: [cyber / privacy / conduct]
- Notes from each overlay that affect the tier or the gates: [pointers to overlay-specific lines in the per-factor justifications]

---

## 6. AI Act overlap

- High-risk overlap likely: [yes / no]
- Annex III categories flagged: [credit scoring / insurance pricing in life and health / biometric / employment / education / law enforcement / migration / democratic process / critical infrastructure / none]
- Routed to `ai-act-triage`: [yes / no]

The formal classification is owned by `ai-act-triage`. This block is the routing flag.

---

## 7. Re-tiering triggers

Each trigger is a named event with a monitoring owner. Dates without events do not earn a row; "annual review" is a refresh cadence, not a re-tiering trigger.

| Event | Owner | Detection method |
|---|---|---|
| [autonomy-level change / customer-base expansion / scope expansion / vendor swap / RAG corpus scope change / data-sensitivity expansion / regulatory change / performance breach for N consecutive periods / supervisory-letter event] | [function] | [monitoring metric, change-management notice, supervisory letter, regulatory horizon scan] |

---

## 8. Open questions and dissent

Open questions: [items that could move the tier once resolved. Each carries an owner and a due date. Empty list when there are none.]

Dissent: [recorded where the tier disagrees with sponsor or business-line proposal. Empty array when the tier matches the sponsor's. Each dissent names the reviewer role, the position, and the basis. Dissent is signed by the AI risk committee secretary or equivalent at tier-1 and tier-2; tier-3 and tier-4 dissents are signed by the second-line reviewer.]

---

## 9. Source trace and confidence

For every material claim in the decision (factor scores, scope statements, regulatory references, financial-scale figures):

| Claim | Source | Evidence reference | Confidence |
|---|---|---|---|
| [claim] | [intake field, document, system, person, or `[evidence needed]`] | [pointer] | [high / medium / low / evidence-needed] |

`[evidence needed]` items either close before the decision is filed or are accepted with a remediation plan and a re-tiering trigger.

---

## Decider attestation

The record is reviewable when every named factor is scored, every triggered gate has an owner, every re-tiering trigger names an event and a detection path, and the source trace is filled.

- Decider: [role, function]
- Decision date: [YYYY-MM-DD]
- Decision: [accept tier / accept tier with conditions / hold for additional input]
- Conditions (if any): [conditions, owners, dates]
- Onward routing: [model-card-builder / validation-plan / agentic-ai-controls / ai-act-triage / llm-vendor-evidence-review / model inventory of record]

The record is filed only after attestation.
