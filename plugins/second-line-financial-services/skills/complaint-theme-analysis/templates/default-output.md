# Complaint-theme analysis

> Status: draft until the named decision forum acts. The skill themes a population of complaints, surfaces red flags, and recommends escalation paths for human decision. It does not approve loans, deny adverse-action notices, finalize UDAAP or fair-lending determinations, or take action on individual complaints.

The delivery is two artifacts. The theme matrix is the structured aggregation rendered as an Excel workbook (via the `xlsx` skill in the `document-skills` plugin). The memo is the narrative analysis rendered as a Word document (via the `docx` skill). The two artifacts emit together; the matrix is the data layer the committee scans, the memo is the analytical layer the committee reads.

## Theme matrix (Excel artifact)

The matrix is one row per theme. Sheet 1 is the headline matrix; supplementary sheets carry the per-theme detail (root-cause hypotheses, regulatory exposure, recommended actions, demographic skew).

### Sheet 1: theme summary

| Column | Type | Notes |
|---|---|---|
| `theme_id` | string | Stable across periods. Example: `THEME-CC-FEE-FX-01`. |
| `theme_label` | string | Human-readable. Plain-language theme name. |
| `definition` | string | Theme inclusion criteria. The coding rule, in one or two sentences. |
| `count` | integer | Period count of unique complaint events coded to this theme as primary. |
| `share` | percentage | Share of total period complaints. |
| `rate_basis` | string | Denominator used for rate (e.g., per 1,000 new accounts; per 1,000 loss-mit-eligible borrowers). Empty where rate not computed. |
| `rate` | float | Per-rate-basis figure where available. |
| `trend` | enum | `up` / `down` / `flat` / `new`. |
| `prior_period_share` | percentage | For comparison. |
| `severity` | enum | `low` / `medium` / `high` / `critical`. |
| `severity_rationale` | string | Brief; full reasoning in supplementary sheet. |
| `regulatory_exposure_summary` | string | Top one or two citations. Full list in supplementary sheet. |
| `conduct_flag` | boolean | Whether theme is a conduct-risk signal. |
| `fair_lending_flag` | boolean | Whether theme suggests protected-class disparity (signal-grade; flag, not finding). |
| `ai_flag` | boolean | Whether theme touches algorithmic decisioning, AI agents, or AI-generated communication. |
| `demographic_skew_summary` | string | Geographic and BISG-derived signals. Empty where not applicable. |
| `cross_references` | string | Named downstream skill(s): `udaap-risk-review`, `fair-lending-test-plan`, `marketing-claim-review`, `adverse-action-review`. |

### Sheet 2: per-theme regulatory exposure

| Column | Type |
|---|---|
| `theme_id` | string |
| `source` | string (e.g., `Reg Z 12 CFR §1026.6(b)(1)`; `Dodd-Frank §1031`; `CFPB Circular 2022-06`) |
| `citation_section` | string |
| `exposure_level` | enum (`primary`, `secondary`, `intersecting`) |
| `notes` | string |

### Sheet 3: per-theme root-cause hypotheses

| Column | Type |
|---|---|
| `theme_id` | string |
| `hypothesis_id` | string |
| `hypothesis_text` | string |
| `tested` | enum (`tested-supported`, `tested-rejected`, `untested`) |
| `evidence` | string |

### Sheet 4: per-theme recommended actions

| Column | Type |
|---|---|
| `theme_id` | string |
| `action_id` | string |
| `action` | string |
| `type` | enum (`control-change`, `policy-change`, `disclosure-change`, `marketing-review`, `udaap-escalation`, `fair-lending-escalation`, `vendor-review`, `monitoring-uplift`, `consumer-redress-consideration`, `training`, `other`) |
| `owner_role` | string |
| `due_date` | date |
| `accountable_forum` | string (e.g., consumer compliance committee, conduct committee, fair-lending committee, product committee, counsel) |
| `named_control` | string (control to be modified or instituted) |

### Sheet 5: per-theme demographic skew (where applicable)

| Column | Type |
|---|---|
| `theme_id` | string |
| `dimension` | enum (`state`, `MSA`, `ZIP3`, `BISG-derived`, `HMDA-aggregate`) |
| `value` | string (e.g., the state code; the MSA name redacted to ZIP3 per firm convention) |
| `share_in_dimension` | percentage |
| `baseline_share` | percentage |
| `concentration_ratio` | float (share / baseline) |
| `signal_grade` | enum (`flag`, `watch-list`, `no-signal`) |
| `notes` | string |

### Sheet 6: source trace

| Column | Type |
|---|---|
| `claim` | string |
| `source` | string (citation; or `references/...` file path) |
| `section` | string |
| `date` | date |
| `url_or_path` | string |

## Memo (Word artifact)

The memo is the narrative analysis. The named sections below are the spine; the practitioner adapts depth and length to the audience and the trigger.

### 1. Scope and population

| Field | Value |
|---|---|
| Analysis ID | `[analysis_id]` |
| As of date | `[YYYY-MM-DD]` |
| Trigger | `quarterly-cycle` / `monthly-cycle` / `pre-exam-readiness` / `regulator-inquiry-triage` / `cluster-trigger` / `peer-enforcement-action` / `post-incident-review` / `other` |
| Period | `[start] to [end]` |
| Comparison period | `[start] to [end]` (for trend) |
| Population sources | `[list of channels reviewed: firm internal, CFPB-portal, CFPB public extract, app-store, social, AG, employee-escalation]` |
| Population total | `[deduplicated unique complaint events]` |
| Sources excluded and why | `[explicit list]` |
| Sector overlay set | `[banking / payments-fintech / capital-markets / insurance]` |
| Cross-cutting overlay set | `conduct (mandatory)` |
| Source posture | `public-only` / `public-plus-firm-policy` / `public-plus-firm-policy-plus-evidence` / `connector-aware` |

### 2. Theming method

- Taxonomy version: `[reference]`
- Active themes plus residual: `[count]`
- Pre-registered coding rules: `[yes / no]` with pointer
- Full-sample application: `[yes / no]`; where partial, the sampling frame is documented
- Coding agreement on dual-read sample: `[percentage; sample size]`
- BISG enrichment applied: `[yes / no; consent-flag handling]`
- Geographic enrichment applied: `[state / MSA / ZIP3]`
- Reproducibility pointer: `[firm-internal path to taxonomy mapping]`

### 3. Top themes

The top themes are listed with the theme ID, theme label, count, share, trend, and severity. Full per-theme detail is in the matrix; the memo carries the analytical narrative for each top theme.

For each top theme, the narrative covers: definition; count and share; trend with prior-period comparison; rate framing where computed; root-cause hypotheses (with which is operative and which are alternative); regulatory exposure; conduct-risk implications; demographic skew where present; recommended actions with owner and forum; cross-skill chain.

### 4. Severity rubric

The rubric used in this period:

- *Critical* — theme matches a public CFPB enforcement focal item directly; material population; ongoing harm; remediation cannot wait for the next committee cycle.
- *High* — theme matches a Supervisory Highlights focal item or a peer enforcement theme; meaningful population; remediation needed within this committee cycle.
- *Medium* — real theme; population bounded or uncertain; remediation enters the controls roadmap.
- *Low* — theme present but population small or driven by isolated process defects.

The rubric is named once in the memo and applied per theme; the per-theme `severity_rationale` carries the reasoning.

### 5. Regulatory exposure mapping

Per theme; full detail in matrix Sheet 2. The memo summarises the operative citations and the intersection patterns (e.g., where a Reg X compliance question and a UDAAP unfairness question are parallel inquiries on the same theme).

### 6. Conduct-risk implications

Per theme; loaded from the conduct cross-cutting overlay. The memo records, per theme: the conduct-risk taxonomy categories the theme touches; the named conduct-accountable manager role; whether the conduct committee receives a read; whether the theme is a conduct-event candidate; the customer-outcome segments affected; the complaint-monitoring loop closure posture.

### 7. Trends and movements

Period-over-period movement per theme. Seasonality treatment named where applicable. Product / campaign / process-change timeline cross-walked against the trend movements; apparent spikes that align with launches are called out.

### 8. Recommended actions

Per theme; full detail in matrix Sheet 4. The memo carries the headline actions, owners, and forums; the matrix carries the structured detail.

### 9. Open questions and dissent

- `[items deferred to counsel]`
- `[items where the second-line view and the first-line view diverge]`
- `[items flagged for the next-period retest]`

### 10. Cross-references

- `udaap-risk-review` `[for themes that warrant element-by-element UDAAP analysis]`
- `fair-lending-test-plan` `[for themes with fair-lending flag set]`
- `marketing-claim-review` `[for themes traced to marketing assets]`
- `adverse-action-review` `[for themes touching AAN content or reason codes]`

### 11. Source trace and confidence

- Material claims cite sources from `references/source-anchors.md` and the loaded sector and conduct overlays by file path.
- Confidence label: `high` / `medium` / `low` per major analytical claim (count-share-and-rate analysis; root-cause hypotheses; demographic-skew read; regulatory-exposure mapping; cross-skill chain).
- Assumptions: `[list]`.

## Decision forum

- Named forum: `[consumer compliance committee / conduct committee / fair-lending committee / counsel / CCO]`
- Decision status: `draft` / `submitted` / `in-review` / `decided` / `deferred`
- Decision date: `[YYYY-MM-DD]`
- Conditions: `[where applicable]`
