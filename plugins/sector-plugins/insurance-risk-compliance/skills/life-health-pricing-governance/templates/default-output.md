# Life and health pricing governance — memo template

The deliverable is two files. This template carries the Word-memo content spec; the Excel rating-factor map structure is at the end of this file.

**Render the memo via the `docx` skill (in the `document-skills` plugin).** Render the rating-factor map via the `xlsx` skill. Both emit together.

---

## Word memo — named sections

### Cover

**Filing ID**: [internal identifier; SERFF tracking number where issued]
**Product type**: [life | health-individual | health-small-group | health-large-group | annuity | disability | LTC | other]
**States in scope**: [list]
**Change type**: [new-filing | refile | rate-change | factor-change | model-change | accelerated-underwriting-launch | accelerated-underwriting-change]
**Engagement ID**: [pointer to scope record, or "none — scope not formalised"]
**As of**: [date]
**Audience**: [state DOI rate analyst | sponsor / chief pricing actuary | rate-filing committee | board risk committee | ORSA reviewer | internal audit]
**Owner (role)**: [chief pricing actuary | head of compliance | head of model risk | other]
**Approver (role)**: [per firm policy for this change type]
**Source posture**: [public-only | public-plus-firm-policy | public-plus-firm-policy-plus-evidence | connector-aware]
**Confidence label**: [high | medium | low | unknown]

### 1. Rate filing summary

[One page maximum. Product, state(s), filing channel (SERFF tracking number where issued), effective date, rationale for change, prior approval status, named-role owners. The summary is the orientation any state DOI rate analyst reads first.]

### 2. Rating factor map

[The line-by-line factor map is the separate Excel workbook (see structure below). This section narrates the headline observations: count of factors in scope, count of ECDIS-derived factors, count of factors with state-by-state divergence in permitted status, and any factor with an open unfair-discrimination question. Cross-reference the workbook by file name.]

### 3. Unfair discrimination analysis (NAIC Model #880)

[Apply the Model #880 standard factor-by-factor and to the rating plan as a whole. The test is actuarial-justification-driven: differences in rate are permitted where supported by sound actuarial principles applied to credible data; differences not so supported are unfairly discriminatory. Permitted-vs-prohibited rating-factor lists are state-specific and live in the state insurance code, not in the model. Protected classes are state-defined and not coterminous with ECOA / Reg B.

Carry per-factor findings in a table:

| Factor ID | Factor name | Statutory frame (Model #880 + state code) | Actuarial-justification status | Finding | Severity | Source citation |
|---|---|---|---|---|---|---|
| | | | sufficient / partial / insufficient / [evidence needed] | | low / moderate / high / critical | |

Plus a rating-plan-as-a-whole assessment paragraph.]

### 4. Disparate-impact red flags (state DOI guidance)

[Run where state DOI guidance imports a disparate-impact-style monitoring expectation on top of #880. CO regulation, NY DFS Circular Letter (January 2024), CA bulletin. Where ECDIS is in the input set, run the proxy-variable risk check; where the model is ML-driven, run the monitoring-metric check; where consumer recourse is required, name the channel and the SLA.

| Finding ID | State | Source bulletin | Concern | Mitigation in place | Gap | Severity |
|---|---|---|---|---|---|---|
| | CO / NY / CA / other | | proxy-variable risk / monitoring metric / consumer-recourse / disclosure | | | |
]

### 5. AI / ML rating factor and accelerated-underwriting governance — AIS Program cross-walk

[NAIC Bulletin December 2023. Run element-by-element. Vendor-AI is not exempt; the carrier remains accountable.

| AIS Program element | Status | Evidence pointer | Gap | Owner role |
|---|---|---|---|---|
| Governance | in-place / partial / gap / not-applicable | | | |
| Risk management | | | | |
| Testing and validation | | | | |
| Third-party AI accountability | | | | |
| Monitoring | | | | |
| Documentation | | | | |
| Transparency | | | | |
| Fairness (translated to unfair-discrimination terminology for DOI audience) | | | | |

Where the carrier has not yet adopted an AIS Program, the artifact says so and tags the gap to the regulatory-affairs lead.]

### 6. Documentation completeness vs SR 11-7-equivalent expectations

[Cite SR 11-7 / OCC 2026-13 as **analogous** model-risk expectation language, not as binding. Mark `[verify final OCC 2026-13 issuance date and bulletin number]` until confirmed.

| Element | Status | Evidence pointer | Gap |
|---|---|---|---|
| Model documentation (purpose, theory, design, data, assumptions, limitations) | | | |
| Validation evidence (independent validation, conceptual soundness, outcomes analysis, benchmarking) | | | |
| Performance-monitoring plan (metrics, drift detection, threshold-breach response, cadence, owner) | | | |
| Change-management process (revalidation triggers, approval chain, documentation update) | | | |
| Ongoing-monitoring metrics (named metrics with definitions and current values where evidence is available) | | | |
]

### 7. State DOI bulletin alignment

[Per state in the filing footprint. Use the NAIC AI Working Group adoption tracker on the analysis date; do not freeze a state list.

| State | NAIC Model Bulletin adoption status | State-specific bulletin / regulation | Alignment status | Gap | Owner role |
|---|---|---|---|---|---|
| CO | n-a (CO has its own SB 21-169 implementing regulation) | SB 21-169 implementing regulation | | | |
| NY | n-a (NY has its own NY DFS Circular Letter) | NY DFS Circular Letter (January 2024) | | | |
| CA | | CA DOI bulletin on AI use | | | |
| [other in scope] | adopted / pending / not-adopted | | | | |
]

### 8. Privacy and consumer-disclosure posture

[HIPAA Privacy Rule alignment where PHI is in scope; ECDIS consumer-recourse and adverse-information-disclosure posture under CO regulation and NY DFS Circular Letter; state insurance information privacy framework alignment (Model #670 where adopted); state comprehensive privacy law alignment with insurance-licensee carve-out posture.

| Element | Status | Evidence pointer | Gap |
|---|---|---|---|
| HIPAA notice-of-privacy-practices alignment | | | |
| HIPAA authorization posture for non-routine uses | | | |
| HIPAA business-associate-agreement chain for vendor AI | | | |
| Minimum-necessary analysis under §164.502(b) | | | |
| ECDIS consumer-recourse channel (name, SLA, owner, documentation) | | | |
| ECDIS adverse-information-disclosure posture | | | |
| FCRA applicability and adverse-action notice posture | | | |
| State insurance privacy framework alignment (Model #670 where adopted) | | | |
| State comprehensive privacy law applicability and insurance-licensee carve-out posture | | | |
]

### 9. ACA-pricing checks (where individual / small-group health is in scope)

[Bright-line rules under PHSA §2701 and 45 CFR Part 147.

| Check | Status | Evidence pointer | Gap |
|---|---|---|---|
| Permitted rating factors (family size, geography, age 3:1, tobacco 1.5:1) — only these used | | | |
| Prohibited rating factors — none used (health status, gender, occupation, claims history, duration of coverage, other) | | | |
| Geographic rating-area structure under 45 CFR §147.102 | | | |
| Rating-area-vs-zip-code mapping | | | |
| Guaranteed renewability under §147.106 | | | |
]

### 10. Illustration check (where life is in scope and the change touches illustrated values)

[NAIC Model #582.

| Element | Status | Evidence pointer | Gap |
|---|---|---|---|
| Disciplined-current-scale documentation | | | |
| Self-support test (§6 — verify section) | | | |
| Lapse-support test (§7 — verify section) | | | |
| Illustration-actuary annual certification | | | |
| Illustrated-vs-non-illustrated-vs-actual variance reports | | | |
]

### 11. Gaps, issues, and recommended disposition

| Gap ID | Description | Source citation | Severity | Owner role | Target close date |
|---|---|---|---|---|---|
| | | | low / moderate / high / critical | | |

**Recommended disposition**: [approve | approve-with-conditions | remediate-then-re-review | decline-and-rework]

The artifact is a draft. The named approver — chief pricing actuary, CRO, head of compliance, or the rate-filing committee — decides.

### 12. Open items, owners, target dates

| Item | Owner role | Target date |
|---|---|---|
| | | |

### 13. Source citations

| Claim | Source | Section | Retrieval date | URL or file ref | Notes |
|---|---|---|---|---|---|
| | | | | | analogous / model text vs state adoption / [verify section] |

Cite `references/source-anchors.md` for canonical citations. Use `[verify section]` if the section reference is unknown; do not invent.

---

## Excel rating-factor map — workbook structure

Render via the `xlsx` skill. One workbook per filing. Tabs:

### Tab 1 — `factor_map`

One row per rating factor. Columns:

| Column | Type | Notes |
|---|---|---|
| `factor_id` | string | Stable ID across the filing. |
| `factor_name` | string | |
| `category` | enum | `actuarial` / `demographic` / `geographic` / `behavioural` / `medical` / `ECDIS-derived` / `composite-score` / `other` |
| `source_data` | string | System-of-record path or named third-party data source. |
| `ecdis_flag` | enum | `yes` / `no` / `vendor-derived` |
| `ecdis_provider` | string | Where `ecdis_flag` is `yes` or `vendor-derived`. |
| `phi_flag` | enum | `yes` / `no` |
| `fcra_applicability` | enum | `yes` / `no` / `[evidence-needed]` |
| `<state>_status` | enum (one column per state in scope) | `permitted` / `prohibited` / `silent` / `requires-justification` / `[evidence-needed]` |
| `prohibited_basis_interaction` | string | Note on interaction with state-defined protected classes. Per-state notes can be in additional rows or in a separate tab. |
| `actuarial_justification_ref` | string | Memorandum section reference. |
| `unfair_discrimination_finding` | enum | `clear` / `partial` / `insufficient` / `[evidence-needed]` |
| `disparate_impact_red_flag` | enum | `none` / `proxy-variable` / `monitoring-gap` / `consumer-recourse-gap` / `disclosure-gap` |
| `monitoring_metric` | string | Named metric. |
| `monitoring_threshold` | string | Threshold or `[evidence-needed]`. |
| `owner_role` | string | |
| `notes` | string | |

### Tab 2 — `state_status_matrix`

Pivot of factor-by-state status, with one row per factor and one column per state in scope. Conditional formatting: prohibited = red; silent / requires-justification = amber; permitted = green; [evidence-needed] = grey.

### Tab 3 — `ai_ml_components`

One row per AI / ML component in the pricing or underwriting chain. Columns: `component_id`, `tool_name`, `vendor`, `role` (`rating` / `underwriting` / `triage` / `monitoring` / `other`), `training_data_summary`, `monitoring_metrics`, `aip_program_element_status_governance`, `aip_program_element_status_risk_management`, ... (one column per AIS Program element), `bas_in_place` (Y/N for vendor PHI flow), `validation_status`, `documentation_status`, `notes`.

### Tab 4 — `findings`

One row per finding. Columns: `finding_id`, `type` (`unfair_discrimination` / `disparate_impact` / `aip_program` / `documentation` / `state_alignment` / `privacy` / `aca` / `illustration`), `factor_or_component_ref`, `description`, `severity` (`low` / `moderate` / `high` / `critical`), `source_citation`, `owner_role`, `target_close_date`, `status`.

### Tab 5 — `source_citations`

Single source-citations table. Columns: `claim`, `source`, `section`, `retrieval_date`, `url_or_file_ref`, `notes`.

---

*File depth scales to the change type and the audience. A SERFF rate-level refile reads tighter than an AU launch with ECDIS in the input set. A board-risk-committee read-out collapses the rating-factor map to a heat-map appendix. A state-DOI-inquiry response file leads with the bulletin-alignment row for the inquiring state. An ORSA-driven internal review pulls the AIS Program section to the front. The Excel rating-factor map is required for any change touching a rating factor; it can be a single-row delta workbook for a factor change or a full grid for a refile.*
