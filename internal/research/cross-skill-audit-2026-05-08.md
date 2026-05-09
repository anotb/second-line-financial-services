# Cross-skill audit — 2026-05-08

Read-only consolidated audit across the 53 capability-plugin skills (post Phase 2 editorial review at commit `5fd4cf6`). Six dimensions: 5A sector overlay coverage, 5B cross-cutting overlay coverage, 5C skill-chain integrity, 5D schema/template alignment, 5E cross-reference integrity, 5F voice spot-check. Sector plugins were checked for cross-references but not audited as a primary surface (per brief — they ARE the sector).

## Executive summary

- **Sector overlay coverage is complete.** Every capability skill that ships sector overlays ships all four (banking, capital-markets, insurance, payments-fintech). No gaps. Differentiation reads strong on the samples drawn (model-card-builder, vendor-diligence, sanctions-screening-qa, test-plan-builder).
- **Cross-cutting overlay coverage is uneven and largely defensible** — most skills load only the cross-cutting domains the SKILL.md actually invokes. A small number of skills look thin in ways that may warrant a second look (see 5B).
- **Three broken cross-skill pointers** — two reference a non-existent `compliance-testing/skills/control-test-workpaper` (the actual skill is `workpaper-drafter`), one references `risk-compliance-core/issue-management` (likely `issue-writeup` or `risk-compliance-core/skills/issue-writeup`), one references `third-party-operational-resilience/skills/important-business-service-mapping` which does not exist.
- **Two real schema field-name drifts** in the controls-test pipeline: producers export `analysis_id` and `request_list_id` as primary keys, but consumer SKILL.md prose and consumer schemas reference them as `exception_register_id` and `evidence_request_list_id`. Mechanical rename, but it touches the cross-skill contract.
- **`risk-compliance-core/README.md` is stale** — lists six v1 skills, the directory has seven (the `scoping` primitive is missing from the skill list). The Phase 1 mid-flight addition of the scoping primitive did not propagate to the README.
- **Voice reads strong overall** — model-card-builder, vendor-diligence, cdd-risk-review, control-sampling, risk-committee-pack, control-matrix all read as senior-practitioner-explaining-the-work. No drafting-scaffolding tells found in samples. The only voice friction is em-dash usage in body prose (the user's voice memo says no em-dashes; the project uses them in two ways — bullet-list separators which are conventional, and prose interruptions which violate the rule. About 485 em-dashes total across SKILL.md, the substantial majority being list separators).

## 5A — Sector overlay coverage and consistency

### Coverage gaps

None. All 53 capability-plugin skills with `references/sector-overlays/` ship all four canonical sector files (`banking.md`, `capital-markets.md`, `insurance.md`, `payments-fintech.md`).

### Consistency drift within sector

Sampled banking overlays across 9 skills for the joint interagency Revised Guidance on Model Risk Management citation pattern (OCC Bulletin 2026-13 / FRB SR 26-2 / FDIC FIL-15-2026, April 17, 2026). Citations are consistent — same date, same parallel-bulletin set, same scope-exclusion footnote (footnote 3 for GenAI/agentic), same $30B threshold qualifier.

The third-party guidance (OCC Bulletin 2023-17 / FRB SR 23-4 / FDIC FIL-29-2023, June 6, 2023) is consistently cited across `vendor-diligence`, `contract-gap-review`, `criticality-assessment`, `exit-plan`, `concentration-risk-review`. The June 2023 → June 2023 wording, the parallel-bulletin set, and the predecessor-bulletin-2013-29-treatment-as-supplemental are all consistent.

No drift findings. Phase 1+2 work did this well.

### Differentiation gaps within skill

Sampled four skills' four-overlay sets:
- `model-card-builder` — banking ↔ capital-markets clearly differentiated (SR 11-7 reach is partial for advisers/BDs; books-and-records under Rule 204-2 / 17a-3/4 is a capital-markets-only addition; Marketing Rule reach is capital-markets-only). Insurance overlay carries NAIC #668, Colorado SB 21-169, NY DFS Circular Letter — distinct from banking. Payments-fintech overlay (not read in detail) is short but skill-appropriate.
- `vendor-diligence` — banking carries Bank Service Company Act §1867(c), Reg O, BaaS joint statement; insurance carries NAIC Models #440/#450/#668/#505/AI Bulletin Dec 2023, ORSA, HIPAA BAA. Materially different operational frames.
- `sanctions-screening-qa` — banking covers correspondent-banking nested-relationships, wire-message field-level reads, trade-finance LC text screening. Payments-fintech covers screening-responsibility allocation between sponsor bank and fintech, real-time card screening, faster-payments rail screening, MSB registration, crypto on-ramp/off-ramp address-level screening. Materially distinct.
- `test-plan-builder` — banking covers CFPB CMS, FFIEC Consumer Compliance Rating System, OCC Comptroller's Handbook CMS, SR 08-8, OCC Heightened Standards, plus per-control-area HMDA/CRA/Reg B/Reg DD/Reg E/Reg Z/BSA conventions. Insurance covers NAIC Market Conduct Examiners Handbook, Model Audit Rule #205, Model #505 ORSA, NAIC AI Bulletin Dec 2023, plus per-control-area underwriting/claims/producer-licensing/data-security/ORSA conventions. Materially distinct.

No "generic boilerplate" findings on the sampled overlays. Differentiation is doing real work.

## 5B — Cross-cutting overlay coverage and consistency

### Coverage inventory

Which cross-cutting overlays each skill ships (47 skills total with `references/cross-cutting/`):

| Skill | Overlays shipped |
| --- | --- |
| agentic-ai-controls | conduct, cyber, privacy |
| ai-act-triage | conduct only |
| ai-risk-tiering | cyber, privacy |
| ai-use-case-intake | conduct, cyber, privacy |
| board-ai-risk-pack | conduct, cyber |
| genai-pre-prod-review | conduct, cyber, privacy |
| llm-vendor-evidence-review | conduct, cyber, privacy |
| model-card-builder | conduct, cyber, privacy |
| prompt-injection-risk | cyber only |
| rag-evaluation-review | conduct, cyber, privacy |
| validation-plan | cyber, privacy |
| control-sampling | conduct, cyber, privacy |
| evidence-request-builder | cyber, privacy |
| exception-analysis | conduct, cyber |
| qa-workpaper | conduct, cyber |
| test-plan-builder | conduct, cyber |
| workpaper-drafter | conduct, cyber |
| adverse-action-review | privacy only |
| complaint-theme-analysis | conduct only |
| fair-lending-test-plan | conduct, privacy |
| marketing-claim-review | conduct, privacy |
| section1071-readiness | conduct, privacy |
| udaap-risk-review | conduct, privacy |
| aml-model-monitoring | cyber only |
| edd-escalation-pack | conduct only |
| negative-news-triage | conduct only |
| sanctions-screening-qa | cyber only |
| sar-decision-qa | cyber only |
| implementation-plan | climate, conduct, cyber, privacy |
| policy-diff | conduct, cyber |
| regulatory-impact-assessment | climate, conduct, cyber, privacy |
| rule-to-obligation-extraction | climate, conduct, cyber, privacy |
| control-matrix | cyber, privacy |
| evidence-binder | privacy only |
| human-review-gates | conduct, cyber |
| issue-writeup | conduct, cyber |
| obligation-mapping | conduct, cyber, privacy |
| policy-gap-review | conduct, cyber, privacy |
| attestation-pack | conduct, cyber, privacy |
| cyber-disclosure-readiness | climate, cyber, privacy |
| kri-commentary | climate, cyber |
| management-response | conduct, cyber, privacy |
| risk-committee-pack | climate, conduct, cyber |
| concentration-risk-review | cyber only |
| contract-gap-review | cyber, privacy |
| dora-register-builder | cyber only |
| exit-plan | cyber, privacy |
| resilience-testing-pack | cyber, privacy |
| vendor-diligence | cyber, privacy |

### Plausible coverage gaps (judgement)

These are skills where one or more cross-cutting overlay seems plausible but is not shipped. Flag for orchestrator decision:

- **`ai-act-triage`** ships only `conduct.md`. The SKILL.md body explicitly references cyber and privacy cross-cutting (lines 80-82) and the Pointers section says "cyber and privacy cross-cutting overlays sit in the broader plugin reference set; load when the engagement scope names them" (line 96) — i.e., the skill consciously delegates to plugin-level overlays that don't exist as plugin-level files. **Either ship the cyber and privacy overlays in this skill, or revise the SKILL.md pointer to point at the actual location** (e.g., the model-card-builder cross-cutting set, or write a plugin-level overlay).
- **`evidence-binder`** ships only `privacy.md`. Cyber is plausibly relevant (binders touch system-of-record, vendor-portal evidence, cyber-incident workpapers). Conduct is plausibly relevant for binders supporting consumer-impact remediation files.
- **`sar-decision-qa`** and **`sanctions-screening-qa`** ship only cyber. Both routinely surface conduct themes (PEP exposure, vulnerable-customer touch, sales-practice exposure layered into AML alerts). Conduct overlay would be defensible.
- **`aml-model-monitoring`** ships only cyber. Plausibly conduct-relevant (segmentation drift can mask conduct themes that the firm's monitoring then misses); plausibly privacy-relevant (transaction-monitoring data is regulated personal data under several frames).
- **`adverse-action-review`** ships only privacy. Conduct overlay is plausibly load-bearing (UDAAP read on adverse-action notice quality, complaint-theme overlap).
- **`complaint-theme-analysis`** ships only conduct. Privacy overlay is plausibly relevant for complaints touching data-handling.
- **`prompt-injection-risk`** ships only cyber. Privacy overlay seems thin to skip — prompt-injection chains have direct privacy leakage paths (training-data extraction, RAG exfiltration of regulated data).
- **`negative-news-triage`** ships only conduct. Privacy overlay is plausibly relevant (the triage handles regulated personal data).

Categorize all of these as "needs editorial decision" — the skills' authors had reasons to scope tight, and adding an overlay is non-trivial.

### Consistency drift within domain

Sampled `cyber.md` across 8 skills (control-matrix, obligation-mapping, resilience-testing-pack, dora-register-builder, vendor-diligence, issue-writeup, human-review-gates, kri-commentary) for source citation consistency.

- NYDFS 23 NYCRR Part 500 (post-Nov 2023 amendment) is the dominant US-side anchor; cited in all the bank/non-DORA-specific cyber overlays. Where the skill is DORA-specific (`dora-register-builder`), DORA Articles 9, 17-23, 24-27 plus NIS2 Directive (EU) 2022/2555 are anchors instead — appropriately. No cross-domain drift.
- SEC cyber rules — 8-K Item 1.05 (Dec 2023), Reg S-K Item 106, Reg S-P (2024 amendment), Reg S-ID — appear consistently across cyber overlays for skills that have a public-registrant audience.
- NIST CSF 2.0 (Feb 2024), NIST SP 800-53 Rev. 5 cited consistently where the skill anchors on it.
- No conflicting citations found.

Loading rules across SKILL.md bodies are consistent: cyber.md loads when `cross_cutting_overlay_set` includes `cyber` (or, in some skills, when the scoped process touches information systems). The phrasing varies stylistically but the trigger semantics align.

### Differentiation gaps within domain

`dora-register-builder/cross-cutting/cyber.md` is much thinner (46 lines) and DORA-specific (zero NYDFS, zero SEC, zero NIST) — that's correct because the skill is EU-specific. Not a gap; differentiation working as intended.

No findings on cross-cutting differentiation worth flagging.

## 5C — Skill-chain integrity

### Flow 1: Engagement bootstrap → vendor-diligence → contract-gap-review → exit-plan → concentration-risk-review

| Producer | Consumer | Producer field (output) | Consumer field (input) | Resolves | Drift |
| --- | --- | --- | --- | --- | --- |
| `scoping` (`scope.schema.json`) | vendor-diligence | `engagement_id`, `institution`, `sector_overlay_set`, `cross_cutting_overlay_set` | "engagement-scope" object | Y | rename pending (background agent: `engagement_scope` → `scope`) |
| criticality-assessment | vendor-diligence | `criticality` field | reads `criticality` | Y | N |
| vendor-diligence | contract-gap-review | structured pack | reads pack | Y | N |
| vendor-diligence | exit-plan | structured pack | reads pack | Y | N |
| vendor-diligence | concentration-risk-review | structured pack | reads pack | Y | N |
| contract-gap-review | exit-plan | clause-gap output | reads clause-gap | Y | N |

The TPRM flow resolves cleanly; the only consistency item is the in-flight `engagement_scope` → `scope` rename, which the orchestrator owns.

### Flow 2: AI lifecycle (intake → tiering → card → validation → genai-pre-prod → llm-vendor-evidence)

| Producer | Consumer | Producer field | Consumer field | Resolves | Drift |
| --- | --- | --- | --- | --- | --- |
| ai-use-case-intake | ai-risk-tiering | `use_case_id` | `use_case_id` | Y | N |
| ai-use-case-intake | ai-act-triage | `use_case_id`, `regulatory_flags`, `ai_act_overlap` | reads same | Y | N |
| ai-risk-tiering | model-card-builder | `tier`, `overlay_flags` | `card_metadata.tier` | Y | N |
| ai-risk-tiering | validation-plan | `tier`, `validation_depth`, `factors` | reads same | Y | N |
| ai-risk-tiering | agentic-ai-controls | `tier`, autonomy-factor | reads same | Y | N |
| ai-risk-tiering | genai-pre-prod-review | `tier`, GenAI factor | reads same | Y | N |
| ai-risk-tiering | board-ai-risk-pack | tier distribution | reads aggregate | Y | N |
| validation-plan | model-card-builder (performance section) | validation outputs | reads same | Y | N |
| ai-act-triage | model-card-builder (Annex IV deltas) | classification + Annex IV deltas | reads classification | Y | N |
| ai-act-triage | genai-pre-prod-review (Article 26 / 50 obligations) | obligations enumeration | reads same | Y | N |
| llm-vendor-evidence-review | genai-pre-prod-review | `eval_evidence_status` | reads same | Y | N |
| board-ai-risk-pack | risk-committee-pack | brief for AI heat-map cell | reads aggregate | Y | N |

Clean. Field names align. Schema descriptions explicitly call out the consumer chain.

### Flow 3: Controls test pipeline (test-plan → sampling → evidence-request → workpaper → exception → qa → issue → management-response)

| Producer | Consumer | Producer field | Consumer field | Resolves | Drift |
| --- | --- | --- | --- | --- | --- |
| test-plan-builder | control-sampling | `test_id` | `test_id` | Y | N |
| control-sampling | test-plan-builder (writes back) | `sampling_id` | `sampling_id` | Y | N |
| test-plan-builder | evidence-request-builder | `test_id`, `criteria`, `procedures` | reads same | Y | N |
| evidence-request-builder | test-plan-builder (writes back) | **`request_list_id`** | **`evidence_request_list_id`** | Y | **DRIFT** |
| test-plan-builder | workpaper-drafter | full plan (`test_id`, `control_id`, etc.) | reads same | Y | N |
| control-sampling | workpaper-drafter | `sampling_id`, population, tolerable rate, sample IDs | reads same | Y | N |
| evidence-request-builder | workpaper-drafter | per-row `request_id` | reads `request_id` per evidence row | Y | N |
| exception-analysis | workpaper-drafter | **`analysis_id`** (schema title `exception-register`) | **`exception_register_id`** | Y | **DRIFT** |
| exception-analysis | issue-writeup | per-exception handoff (`source_exception_id`) | reads `source_exception_id` | Y | N |
| workpaper-drafter | qa-workpaper | full record | reads full record | Y | N |
| workpaper-drafter | issue-writeup | `issues_elevated` | reads same | Y | N |
| issue-writeup | management-response | `issue_id`, `linked_issue_ids` | reads `linked_issue_ids` | Y | N |
| management-response | risk-committee-pack | response posture, owner, target date | reads aggregate | Y | N |

**Two field-name drifts:**
1. `exception-analysis/schemas/exception.schema.json` declares `analysis_id` as the primary-key field (required, top-level). Schema title is `exception-register`. But:
   - `workpaper-drafter/schemas/workpaper.schema.json` declares the foreign key as `exception_register_id` ("Foreign key into exception-analysis output").
   - `exception-analysis/SKILL.md:15` and `:116` both say "this skill produces via `exception_register_id`" / "reads `exception_register_id`".
   - Producer schema and consumer schema use different names for the same identifier.
2. `evidence-request-builder/schemas/evidence-request.schema.json` declares `request_list_id` as primary-key field. But:
   - `test-plan-builder/SKILL.md:92` says "evidence-request-builder reads `criteria` and `procedures` to draft the evidence request list and write back `evidence_request_list_id`".
   - `test-plan-builder/schemas/test-plan.schema.json:326` declares the foreign key as `evidence_request_list_id`.
   - Same drift.

Fix is mechanical: either rename `analysis_id` → `exception_register_id` and `request_list_id` → `evidence_request_list_id` in the producer schemas (most natural — match consumer expectations), or rename consumer references. The first is preferable because the consumer-facing name is more descriptive ("register", "list" are the substantive concepts; "analysis" is the verb).

### Flow 4: Reg-change pipeline (RIA → rule-to-obligation → obligation-mapping → policy-gap-review → control-matrix → implementation-plan → exam-brief)

| Producer | Consumer | Producer field | Consumer field | Resolves | Drift |
| --- | --- | --- | --- | --- | --- |
| regulatory-impact-assessment | rule-to-obligation-extraction | impact assessment scope | reads scope | Y | N |
| regulatory-impact-assessment | policy-diff | policy-impact section | reads section | Y | N |
| regulatory-impact-assessment | implementation-plan | obligation domains, transition window, cost-to-comply | reads same | Y | N |
| rule-to-obligation-extraction | obligation-mapping | `obligations[*].obligation_id` | reads same | Y | N |
| rule-to-obligation-extraction | policy-diff | register | reads same | Y | N |
| rule-to-obligation-extraction | implementation-plan | effective-date and transition table | reads same | Y | N |
| obligation-mapping | control-matrix | `obligations[*].obligation_id` | reads same | Y | N |
| obligation-mapping | policy-gap-review | register vs policy library | reads same | Y | N |
| obligation-mapping | evidence-binder | `obligations[*].evidence_required` | reads same | Y | N |
| policy-gap-review | issue-writeup | `gaps[]` rows | reads same | Y | N |
| control-matrix | compliance-testing | `controls[*].evidence`, `test_method` | reads same | Y | N |
| control-matrix | exam-brief | `controls`, `coverage_gaps` | reads same | Y | N |
| implementation-plan | exam-brief | response posture, MRA/MRIA milestones | reads same | Y | N |

Clean.

### Flow 5: Risk-committee feeders

| Producer | Consumer | Producer field | Consumer field | Resolves | Drift |
| --- | --- | --- | --- | --- | --- |
| kri-commentary | risk-committee-pack | per-KRI commentary block | reads aggregate via `kris` | Y | N |
| management-response | risk-committee-pack | response posture, owner, target date, EoE plan | reads aggregate via `issues_summary` | Y | N |
| bcbs239-gap-assessment | risk-committee-pack | overall rating, top-five priority gaps, data-confidence label | reads via `bcbs239_known_limitations` | Y | N |
| attestation-pack | risk-committee-pack | linked issues, sign-off block | reads aggregate via `issues_summary` | Y | N |
| cyber-disclosure-readiness | risk-committee-pack | brief when elevated | reads aggregate | Y | N |
| board-ai-risk-pack | risk-committee-pack | brief for AI heat-map cell | reads aggregate | Y | N |
| ai-risk-tiering | board-ai-risk-pack | tier mix, factor reads | reads `inventory_state` | Y | N |
| model-card-builder | board-ai-risk-pack | sign-off questions, performance trends | reads `in_flight_reviews`, `model_performance_trends` | Y | N |
| agentic-ai-controls | board-ai-risk-pack | GenAI program status, agentic deployments | reads `genai_program_status` | Y | N |
| vendor-diligence (AI mode) | board-ai-risk-pack | concentration evidence | reads aggregate | Y | N |

**Note (not drift, but worth flagging):** the two parallel pack schemas use different field names for analogous concepts:
- `risk-committee-pack`: `decision_items`, `forward_looking`, `top_risks`, `cro_summary_bullets`
- `board-ai-risk-pack`: `decisions_requested`, `forward_look`, `executive_summary` (no parallel for `top_risks`)

These are not strict drifts because the schemas are independent contracts — but a future practitioner reading both will trip on the inconsistency. Categorize as "editorial decision" — keep for clarity (the AI pack has different structure) or align (e.g., `decisions_requested` → `decision_items`, `forward_look` → `forward_looking`).

## 5D — Schema / template / SKILL.md alignment

Sampled three high-value schemas (test-plan, control-matrix, model-card) for field-template-prose alignment. Default finding is "well-aligned." Misalignments only:

### test-plan-builder

- Schema field `evidence_request_list_id` exists; producer (`evidence-request-builder`) calls the same identifier `request_list_id`. **Same drift as Flow 3 finding above.**

### exception-analysis (`schemas/exception.schema.json`)

- Schema title is `exception-register`; primary-key field is `analysis_id`. SKILL.md prose and downstream consumer schemas refer to `exception_register_id`. **Same drift as Flow 3 finding above.**

### model-card-builder

- Schema's `card_metadata` carries `use_case_id`, `model_id`, `tier`, `lifecycle_stage`, `classification`, `version`, `owner`, `date`, `scope_id`. Template's "Card metadata" section names the same fields in prose. SKILL.md body describes them at line 44. ✓
- Schema's `architecture` carries (need not list every field) — template has matching System description section. ✓

### Banking model-card overlay schema additions
- `banking.md:80-87` proposes additional fields: `card_metadata.heightened_standards_inscope`, `card_metadata.bank_charter_type`, `card_metadata.primary_federal_regulator`, `card_metadata.stress_testing_inscope`, `data[].cra_relevance`. Spot-check shows these are *proposed by the overlay* (additive at sector-overlay load time) rather than declared at the base-schema level. This is intentional — overlays add fields, not strict ones. No fix needed but worth noting that the base `model-card.schema.json` does not declare these enums at the base level; the overlay is the source of truth.

### kri-commentary, management-response, risk-committee-pack alignment

Spot-checked. Top-level fields map to template sections cleanly. No misalignment found.

### Enum prose alignment

- `criticality-assessment.schema.json` enum `["critical", "important", "not-critical", "unknown"]` matches SKILL.md prose at line discussing tier values. ✓
- Sampled `confidence_label` enum (`high | medium | low`) — used consistently across the repo as the source-trace confidence vocabulary. ✓

No type-mismatch findings (no booleans-where-strings or vice versa) found in the sample.

## 5E — Cross-reference + boundary integrity

### Broken pointers

Confirmed unresolved skill-pointers in SKILL.md and reference files:

1. **`risk-compliance-core/skills/issue-writeup/SKILL.md:12`** — `compliance-testing/skills/control-test-workpaper`. The actual skill is `workpaper-drafter`. Mechanical fix.
2. **`risk-reporting/skills/attestation-pack/SKILL.md:15`** — `compliance-testing/skills/control-test-workpaper`. Same broken pointer. Mechanical fix.
3. **`regulatory-change-management/skills/implementation-plan/SKILL.md:17`** — `risk-compliance-core/issue-management`. Plugin-level reference, not a skill. Looking at line 10 ("a self-identified issue or audit finding warrants a programme-level plan with second-line oversight rather than an issue-management ticket") and line 32 ("a self-identified issue routed through issue-management policy"), the SKILL.md uses "issue-management" as a generic term in some places and as a skill pointer in others. Line 17's pointer is the only one that imitates the skill-reference syntax. Recommend either: rename to `risk-compliance-core/skills/issue-writeup`, or de-syntax it (drop the backticks on line 17 to mark it as a generic concept).
4. **`risk-reporting/skills/management-response/references/sector-overlays/banking.md:64`** — `third-party-operational-resilience/skills/important-business-service-mapping`. This skill does not exist. The closest is `criticality-assessment`, which carries the IBS-mapping work in its skill description ("ties it to the firm's important business service"). Fix is to redirect to `criticality-assessment` (or, if IBS mapping is genuinely a missing skill that should exist, flag for build).

Two also-noted but not-strictly-broken:

5. **`consumer-compliance-fair-lending/skills/adverse-action-review/SKILL.md:13`** — `use \`compliance-testing\`` is a vague plugin-pointer rather than a specific skill. Cleaner to point at a skill.
6. **Sector-plugin pointer to non-existent capability skill** — `banking-risk-compliance/skills/bank-fintech-partnership-review/SKILL.md:16` and `payments-fintech-compliance/skills/payments-risk-assessment/SKILL.md:16` reference `aml-risk-assessment` (with "(when present)" caveat) and `risk-compliance-core/risk-assessment` (does not exist). Both are out of audit scope per brief but flagged for the sector-plugin pass.

### Boundary overlaps / orphan use cases

Spot-checked boundaries within plugins:
- **AI plugin (11 skills)**: `ai-use-case-intake` and `ai-risk-tiering` cleanly separated (intake captures, tiering scores). `ai-act-triage` and `ai-risk-tiering` cleanly separated (Act = EU classification; tiering = firm-internal risk score). `model-card-builder` and `validation-plan` cleanly separated (card = firm-side governance artifact; plan = scope contract for testing). `genai-pre-prod-review` is the gate; `agentic-ai-controls` is the agent-specific control review. `prompt-injection-risk` and `rag-evaluation-review` are orthogonal control-level reviews. `llm-vendor-evidence-review` and `model-card-builder` are differentiated (vendor evidence pack vs firm-side card). `board-ai-risk-pack` is the committee-level rollup. No overlaps detected.
- **Compliance-testing (6 skills)**: each owns a discrete artifact in the test cycle. No overlaps.
- **TPRM (7 skills)**: criticality-assessment is upstream of every other skill. vendor-diligence, contract-gap-review, exit-plan, concentration-risk-review, dora-register-builder, resilience-testing-pack are co-equal artifacts. No overlaps.
- **Risk-reporting (6 skills)**: kri-commentary feeds risk-committee-pack; management-response feeds risk-committee-pack and is consumed by attestation-pack indirectly; bcbs239-gap-assessment feeds the data-confidence label; cyber-disclosure-readiness is its own SEC-disclosure file; attestation-pack is the firm-attestation rollup. No overlaps.
- **Reg change (5 skills)**: regulatory-impact-assessment → rule-to-obligation-extraction → policy-diff → implementation-plan → exam-brief is a clean chain. No overlaps.
- **Risk-compliance-core (7 skills)**: scoping is the bootstrap; obligation-mapping, control-matrix, policy-gap-review, evidence-binder, issue-writeup, human-review-gates are the foundational primitives. No overlaps.
- **Financial-crime (6 skills)**: cdd-risk-review and edd-escalation-pack cleanly separated (CDD review vs EDD pack); sanctions-screening-qa and sar-decision-qa cleanly separated (program QA vs decision QA); aml-model-monitoring is the model-risk lens on the AML system; negative-news-triage is the input-relevance triage. No overlaps.
- **Consumer compliance (6 skills)**: each owns a discrete consumer-compliance artifact. No overlaps.

No orphan use cases detected at this level of analysis.

### Plugin README vs skills dir

- **`ai-governance-model-risk/README.md`** — references `claims-ai-controls` and `insurance-ai-act-triage` at lines 55-56, with explanatory note that they were absorbed into `agentic-ai-controls` and `ai-act-triage` respectively. **Documented absences** — not a defect.
- **`compliance-testing/README.md`** — accurate.
- **`consumer-compliance-fair-lending/README.md`** — six skills listed, six skills in dir. Accurate.
- **`financial-crime-governance/README.md`** — six skills listed, six in dir. The `alert-disposition` reference at line 33 is to a *schema* (`alert-disposition.json` planned for Phase 2 / Phase 3), not a skill. The schema is not present in `schemas/`. Flag for orchestrator: either add the schema or revise the README's planned-schemas line.
- **`regulatory-change-management/README.md`** — five skills accurate.
- **`risk-compliance-core/README.md`** — **stale**. Lists six v1 skills (lines 8-13). Directory has seven (`scoping` is missing from the list). Phase 1 added the scoping primitive mid-flight. **Mechanical fix.**
- **`risk-reporting/README.md`** — accurate (six skills listed, six in dir).
- **`third-party-operational-resilience/README.md`** — seven skills listed, seven in dir. Accurate.

## 5F — Voice / style spot-check

### Skills audited

Read full SKILL.md or first 50-80 lines for: `model-card-builder`, `vendor-diligence` (banking overlay), `cdd-risk-review`, `risk-committee-pack`, `control-sampling`, `control-matrix`, `ai-act-triage`.

Verdict on each: **strong senior-practitioner voice.** Descriptions trigger crisply. Bodies read as-if-explaining-the-work, not framework-defining. No drafting-scaffolding tells ("this skill provides guidance on…" / "the framework for…") found in the samples.

### Specific edits flagged

Voice issues that did surface:

- **Em-dash usage in body prose.** The user voice memo says "no em-dashes." 485 em-dashes total across SKILL.md. The bulk are bullet-list separators (`\`file.md\` — description`) which is conventional formatting rather than prose-style em-dashes. But there are prose em-dashes that should be ellipses or parentheses per the rule. Examples flagged for editorial review:
  - `agentic-ai-controls/SKILL.md:73` — "the entity's existing cyber-incident regimes — NYDFS 72-hour notice, the bank 36-hour computer-security incident notification rule, SEC 8-K Item 1.05 …" → use parentheses or replace em-dashes with colon.
  - `prompt-injection-risk/SKILL.md:24` — "carry binding supervisory expectation in their respective scopes — prompt injection is, in those frames, a cybersecurity risk class" → could use a period or "; ".
  - `board-ai-risk-pack/SKILL.md:9-10` (description block) — "Board education session on AI governance — tier mix, top risks, …" → could use a colon.
  - The list-separator usage (e.g., `- \`references/source-anchors.md\` — citations and excerpts`) is repo-wide and conventional. Strict reading of the user voice rule says replace these with periods or colons; pragmatic reading says leave them. Categorize as editorial decision for the orchestrator.
- **Line 34 of `model-card-builder/SKILL.md`** uses `...` for an open-ended list — voice-correct (the rule prefers ellipses).
- **Compliance-testing-related "control-test-workpaper" pointer** (5E above) — also reads as a voice issue: in two SKILL.md descriptions the syntax says use \`control-test-workpaper\` while the actual skill is `workpaper-drafter`. The mismatch reads as drafting-from-an-old-spec rather than from-the-shipped-skill.

No marketing adjectives, fake-precision ranges, or hedge tics surfaced in the spot-check sample. (Worth re-running on a wider random sample if the orchestrator wants more coverage; the seven sampled skills read clean.)

## Categorization for follow-up

### Auto-fixable (mechanical edits, low judgement load)

1. **Broken pointer** `risk-compliance-core/skills/issue-writeup/SKILL.md:12` — `compliance-testing/skills/control-test-workpaper` → `compliance-testing/skills/workpaper-drafter`.
2. **Broken pointer** `risk-reporting/skills/attestation-pack/SKILL.md:15` — same fix.
3. **Broken pointer** `regulatory-change-management/skills/implementation-plan/SKILL.md:17` — `risk-compliance-core/issue-management` → `risk-compliance-core/skills/issue-writeup` (or de-syntax to drop the backticks if the term is meant generically).
4. **Broken pointer** `risk-reporting/skills/management-response/references/sector-overlays/banking.md:64` — `third-party-operational-resilience/skills/important-business-service-mapping` → `third-party-operational-resilience/skills/criticality-assessment`.
5. **Stale README** `risk-compliance-core/README.md` — add `scoping` to the v1 skill list (lines 8-13).
6. **Schema field rename (controls test pipeline drift #1)** — rename `analysis_id` → `exception_register_id` in `compliance-testing/skills/exception-analysis/schemas/exception.schema.json`, plus propagate to `templates/default-output.md` and `examples/`. This is a cross-skill contract change; needs the standard schema-versioning treatment per the SKILL.md rules ("additive changes only between minor versions, never silent renames"). Either bump schema version or do additive (add `exception_register_id` as alias and deprecate `analysis_id`).
7. **Schema field rename (controls test pipeline drift #2)** — rename `request_list_id` → `evidence_request_list_id` in `compliance-testing/skills/evidence-request-builder/schemas/evidence-request.schema.json`. Same versioning consideration.

### Needs editorial decision (not pure mechanical)

8. **`ai-act-triage` cross-cutting overlays** — the SKILL.md says cyber and privacy "sit in the broader plugin reference set" but no plugin-level overlay file exists. Either ship `cross-cutting/cyber.md` and `cross-cutting/privacy.md` in this skill, or revise the SKILL.md pointer to reflect actuality.
9. **Cross-cutting overlay coverage gaps** — should `evidence-binder`, `sar-decision-qa`, `sanctions-screening-qa`, `aml-model-monitoring`, `prompt-injection-risk`, `negative-news-triage`, `complaint-theme-analysis`, `adverse-action-review` add the plausibly-relevant overlays flagged in 5B? Each requires the skill author's call.
10. **Em-dash policy** — user voice memo says no em-dashes. ~485 em-dashes in SKILL.md, mostly as list separators. Strict policy says replace all; pragmatic says replace prose em-dashes only. Orchestrator's call.
11. **`alert-disposition.schema.json`** — `financial-crime-governance/README.md:33` lists this as a Phase 2 schema; it's not in `schemas/`. Either add or remove from README.
12. **Pack schema field-name parallel** — `risk-committee-pack` (`decision_items`, `forward_looking`) vs `board-ai-risk-pack` (`decisions_requested`, `forward_look`). Standardize or document the divergence.
13. **Vague pointer** `consumer-compliance-fair-lending/skills/adverse-action-review/SKILL.md:13` — pointer to `compliance-testing` (the plugin) without naming a skill. Cleaner to name a specific skill.

### Requires verification (external source)

None. Citation verification is in scope of `internal/research/citation-verification-2026-05-08.md` (separate audit). This audit found no new external-verification asks beyond what that file already tracks.

### Out of scope for this audit (but worth flagging to orchestrator)

- The in-flight `engagement-scoping` → `scoping` and `engagement_scope` → `scope` rename has not propagated through SKILL.md prose, schemas, examples, or templates. As of this audit, 55 instances of `engagement-scoping` and 145 instances of `engagement_scope` remain. The orchestrator's brief said the background agent owns this; this audit was tolerant of either name. Once the rename completes, the SKILL.md cross-cutting consistency story will be cleaner.
- Sector-plugin skill content (banking-risk-compliance, capital-markets-asset-management-compliance, insurance-risk-compliance, payments-fintech-compliance) was not deeply audited; the broken-pointer scan caught two within them (`aml-risk-assessment`, `risk-compliance-core/risk-assessment`) which the sector-plugin pass should resolve.
- Agent-plugin SKILL.md content (the six agent plugins) was not audited.
