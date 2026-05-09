---
name: exception-analysis
description: |
  Classifies the deviations a control test surfaced into design gaps, operating-effectiveness failures, evidence gaps, scope disagreements, data-integrity issues, and anomalies; ranks severity with rationale; names a root-cause hypothesis; sets disposition (elevate to issue, close at exception, re-test, expand sample); and builds the handoff package downstream issue write-up consumes. Output is an exception register that pairs with the testing workpaper and ladders confirmed exceptions into the issue lifecycle.

  Best for:
  - A compliance-testing or internal-audit reviewer has finished sample testing and is sitting on a list of deviations that need to be classified before they become findings.
  - A QA reviewer is challenging a workpaper's exception treatment because the line between evidence gap and control failure was blurred.
  - A repeat-issue review needs to confirm whether deviations across testing cycles are the same root cause or coincidental.
  - A second-line lead is preparing a handoff to issue write-up and wants the criterion, condition, cause, effect, and recommendation seed populated before the writer opens the issue artifact.

  Not the right tool when:
  - The test has not been run yet. Pre-fieldwork scoping is `test-plan-builder`; sample design is `control-sampling`; evidence asks are `evidence-request-builder`.
  - The exception has already been classified and the work is drafting the issue. Use `risk-compliance-core/skills/issue-writeup`; this skill produces the input that issue-writeup consumes via `source_exception_id`.
  - The work is drafting the workpaper end to end. Use `workpaper-drafter`; that skill consumes the exception register this skill produces via `exception_register_id`.
  - The work is QA on a completed workpaper. That is `qa-workpaper`.
argument-hint: "[test plan ID, workpaper ID, raw deviation list, or pointer to completed sample testing]"
---

# Exception analysis

A control test produces deviations. Not every deviation is a finding. Some are evidence gaps the system did the right thing, the file did not record it. Some are anomalies a one-off mistake with positive evidence it does not recur. Some are design gaps the form, the workflow, the rule did not require what the criterion expects. Some are operating failures the design was sound, the operation missed. Some are data-integrity issues the system of record disagrees with the source feed. Some are scope disagreements the tester and the control owner read the criterion differently.

This skill takes the raw deviation list out of fieldwork, classifies each one, ranks severity with rationale, names a root-cause hypothesis, sets a disposition, and builds the handoff package the downstream issue write-up consumes. It drafts the exception register against `templates/default-output.md` and emits a structured record conforming to `schemas/exception.schema.json`. The workpaper drafter consumes that record by ID; the issue write-up consumes the per-exception handoff package via `source_exception_id`. The skill stops at preparer sign-off; the named reviewer signs separately and severity always carries human review.

## Ask first

Before classifying, get plain answers. Most cycles answer them in the test plan and the raw deviation notes; if not, default and flag.

- **Whose register is this for.** The testing manager closing the cycle, the QA reviewer challenging exception treatment, the issue-writeup author opening tracked findings, the internal audit lead deciding reliance, the examiner who reads the file later. Audience drives how heavily the rationale fields read and which dispositions get the most attention.
- **Has fieldwork actually finished.** All sample items inspected, all procedures executed, walkthrough complete. A register built on partial fieldwork mis-projects deviation rate and mis-ranks severity. If fieldwork is open, route back to `workpaper-drafter` and stop.
- **What is the criterion the test was measured against.** Pull it from the test plan and the workpaper's source criteria block. Classification turns on whether the condition deviates from the criterion or from the tester's reading of it; without the criterion in hand, scope-disagreement classifications cannot be defended.
- **Is there a prior cycle with similar deviations.** A repeat-issue flag changes severity calibration and the issue-writeup handoff. Check the issue log for the same control or population before classifying; do not let "looks new" pass when the prior issue is still open.
- **What does the firm's tolerable deviation rate say.** Pulled from the test plan. Aggregation reads against tolerable, not against the preparer's intuition. If the rate is unset, that is a test-plan defect to flag back, not a number to invent here.

When `scope` (per `risk-compliance-core/scoping`) is supplied, consume it: `institution.type` and `institution.primary_regulators` set the supervisory framing for severity rationale and dispositional language, `sector_overlay_set` selects which `references/sector-overlays/<sector>.md` loads, `cross_cutting_overlay_set` selects the `references/cross-cutting/<topic>.md` files, `persona.role` sets which decision forum the register passes through, `source_posture` constrains what the body can carry. When it is not supplied, draft against what the test plan and workpaper carry, default to the testing program's standing posture, and note in the register that scope was not formalised separately.

## How the register gets built

The register has the same spine across control types. A senior preparer fills it in roughly in the order deviations surfaced, not in lockstep.

The header pins the register to its test cycle: exception register ID, test ID (foreign key into `test-plan-builder` output), workpaper ID (foreign key into `workpaper-drafter` output), control ID, obligation IDs, period under test, business unit, jurisdiction, source posture, preparer role and date, reviewer role and date placeholder. Reviewer separation is structural, not advisory: the same role cannot both classify and review classification. The header is the audit trail when classification is later contested in QA, in steering, or with a regulator.

Scope and source posture restates the test plan's scope in two or three sentences. The pointer to the workpaper goes here. If the workpaper noted scope changes from the plan, those carry forward into the classification context.

The exception register itself is the body. One row per deviation. For each:

- **Exception ID** is stable across the engagement and feeds `source_exception_id` on the issue side.
- **Sample ID and population reference** tie the exception back to the workpaper's sample-level results table.
- **Criterion** names the rule, principle, policy section, or methodology the deviation is measured against, with a section reference and a pointer into `references/source-anchors.md` or the loaded overlays. "Per firm policy" without citation is not a criterion.
- **Condition** is the dated, scoped, observable state. What the test actually saw. Specific. "On the 2026-Q1 access-recertification packet for the Production-Admin entitlement group, the per-entitlement attestation column was blank for 14 of 22 entitlements" is a condition. "The control failed" is a conclusion, not a condition.
- **Classification** is one of: `control-failure` (design was sound, operation missed), `design-gap` (the design itself does not require what the criterion expects), `evidence-gap` (the system did the right thing, the file does not record it), `scope-disagreement` (the tester and the control owner read the criterion differently and the disagreement is not yet resolved), `data-integrity` (the system of record disagrees with the source feed or another authoritative system), `anomaly` (with positive evidence it does not recur). Classification is the load-bearing field; it drives severity, disposition, and what the issue-writeup handoff carries.
- **Severity** is low, medium, high, or critical, paired with `severity_rationale`. Rationale references frequency (one-off, intermittent, recurring), customer impact (none, identifiable, quantified harm), regulatory exposure (no exam reference, ongoing exam scope, supervisory-finding-eligible), materiality against the firm's published thresholds where they exist, and any compensating controls. Severity without rationale is a number, not a finding. Severity assignment always carries human review.
- **Root-cause hypothesis** is `people` / `process` / `technology` / `data` / `governance`, with a one-paragraph description naming the specific control attribute that failed. "Human error", "training gap", and "system limitation" are surface labels. The hypothesis names the design or operation weakness underneath. Where root cause is genuinely unknown at register time, the field reads "root cause analysis pending" and the disposition carries an open action; do not invent a cause to fill the field.
- **Repeat-issue flag** and `prior_issue_id`. Check the issue log before flagging false. A repeat exception is a different severity calibration from a first-cycle finding.
- **Disposition** is one of: `elevated-to-issue` (carries handoff package), `closed-at-exception` (with rationale, e.g., evidence re-supplied and reviewed), `re-test-required` (next cycle, with criteria for what closes the re-test), `expanded-sample-required` (with the expanded population and rationale).
- **Issue handoff package** populates when disposition is `elevated-to-issue`. Carries criterion, condition, cause, effect (with unit and time window), and a recommendation seed. The package is the bridge into `risk-compliance-core/skills/issue-writeup`; that skill keys off `source_exception_id` and pulls these fields without re-discovering them.

Aggregation and projection compares observed deviation rate against the tolerable rate set in the test plan. The projection commentary reads anomaly versus systemic, names concentration in a particular segment or process or region or channel, and flags sample-design implications when the deviation rate suggests the population is not behaving as the sample assumed. The default posture is systemic; downgrading to anomaly demands positive evidence the deviation is non-recurring. Stratum-level breakdown belongs here when the sample was stratified.

Disposition summary clusters the register by classification and severity for the audience that decides next steps. How many design exceptions, how many operating, how many critical, how many evidence gaps closed at exception level, how many re-test items, how many elevated. The summary feeds the workpaper's exceptions-identified section directly.

The handoff to issue write-up names every elevated exception with its handoff package populated. Each elevated exception carries criterion, condition, cause, effect, and recommendation seed in the shape `risk-compliance-core/skills/issue-writeup` consumes. Where multiple exceptions roll up into a single issue (same root cause, different sample items), name the rollup grouping.

Reviewer questions captures everything that could not be resolved in classification or that the preparer wants the named reviewer to consider before sign-off. Cluster questions for the audience that decides them; severity calibration questions and root-cause questions go in the same list when both apply.

The sign-off block carries preparer, reviewer (separate role), and a confidence label (high / medium / low / unknown) reflecting evidence sufficiency, sample size, source posture, and any reliance on second-hand evidence. Source trace closes the file: every classification and severity rationale cites the criterion and the firm-overlay or source-anchor file path.

### Sector and cross-cutting overlays

The same classification spine carries different criteria sources, different severity calibrations, and different reviewer machinery across sectors and cross-cutting topics. Load only the overlays the scope flags:

- `references/sector-overlays/banking.md` carries large-bank supervisory-finding terminology context (the firm drafts in the same shape so its records align to examiner vocabulary; the firm does not invent a regulator-issued matter), heightened-standards severity flavour, and the BSA/AML and consumer-compliance exception conventions.
- `references/sector-overlays/insurance.md` carries state DOI market-conduct exception conventions and the model-audit-rule severity framing for ICFR-relevant findings.
- `references/sector-overlays/capital-markets.md` carries supervision-rule exception treatment for broker-dealer and investment-adviser testing, and enforcement-style language hygiene (the register concludes on control effectiveness, not on legal violation).
- `references/sector-overlays/payments-fintech.md` carries sponsor-bank oversight exception conventions and Reg E error-resolution exception treatment.
- `references/cross-cutting/cyber.md` is the most-loaded cross-cutting overlay. Cyber exceptions need careful classification because evidence gaps (no log) often look like control failures; the overlay carries the disambiguation pattern, IAM-recertification exception flavour, and incident-response control-effectiveness language.
- `references/cross-cutting/conduct.md` loads when the test sampled a consumer-impact population. Conduct exceptions need consumer-harm framing distinct from technical control deviation; severity calibration shifts when customer harm is identifiable.

Privacy and climate cross-cutting overlays follow the same pattern; this skill ships cyber and conduct as the v1 cross-cutting files because they are the most frequent triggers for exception classification. Where firm policy or taxonomy applies (severity ladder specific to the firm, named committee gates, policy-floor severity overrides for privileged access or critical data), it lives in `references/firm-overlay.md` and is consumed when present.

## Quality bar

Holds across every register:

- Every material claim cites a source. Mark unsupported items `[evidence needed]`. The register is the audit trail; absence of citation is a defect.
- Source evidence, management assertions, public-source obligations, generated inferences, and open legal or compliance questions stay distinguishable in the register. The artifact shows the seams.
- Classification is the load-bearing field. Default to `control-failure` for a deviation against an operating procedure and to `design-gap` for a deviation against the form or workflow itself; downgrade to `evidence-gap` only when the system shows the right thing happened, and downgrade to `anomaly` only when there is positive evidence the deviation does not recur.
- Severity is paired with rationale. Severity assignment always carries human review.
- The register concludes on control effectiveness and exception classification, not on legal violation. Legal-violation language is for legal counsel and regulator-led determinations.
- Preparer and reviewer are different roles.
- The skill stops at preparer sign-off. The named reviewer signs separately. The handoff to issue write-up is a draft until the reviewer attests and the issue is opened.
- No named institutions in the register unless they are public defendants in a finalised enforcement action.

## Adaptation

Register depth and length scale to deviation volume and severity range. A clean cycle with two evidence-gap exceptions reads short; a cycle with classified exceptions across multiple severities and root-cause categories reads longer with the disposition summary clustered for the audience that decides next steps. Sector overlay loading follows scope plus the rule that the regulator the test was designed for drives the sector overlay. Cross-cutting overlay loading: cyber overlay is default-on for any control test touching IAM, data-protection, or supervisory-rule-mandated security areas; conduct overlay is default-on for any consumer-facing test where customer-harm framing matters separately from technical control conclusion.

## Pointers

- `references/source-anchors.md` — citations and excerpts for the named anchors.
- `references/sector-overlays/banking.md`, `insurance.md`, `capital-markets.md`, `payments-fintech.md` — sector-specific exception conventions loaded per scope.
- `references/cross-cutting/cyber.md`, `conduct.md` — cross-cutting flavour; cyber default-on for IAM, data-protection, and security-rule-mandated controls; conduct default-on for consumer-facing populations.
- `references/firm-overlay.md` — firm-installed methodology, taxonomy, severity ladder, named committee gates, and policy-floor overrides beyond the regulatory baseline; consumed when present.
- `templates/default-output.md` — exception register template.
- `schemas/exception.schema.json` — structured-output contract for downstream consumption.
- `examples/` — Reg E error-resolution exception classification at a regional bank; access-recertification exception classification at an entity under a state security-rule.
- `TROUBLESHOOTING.md` — recurring pitfalls (treating every deviation as a finding, confusing evidence gap with control failure, skipping root cause, projecting anomalies, severity inflation, empty handoff packages).

The plugin-level shared references (`references/source-map.md`, `references/policy-control-library.md`, `references/review-gates.md`) sit at the plugin root and are consulted alongside the skill-level files.

## Output

Default to drafting against `templates/default-output.md`. Render as Word, Excel, PowerPoint, or Markdown when the audience or workflow asks for it. Produce the structured record at `schemas/exception.schema.json` when downstream automation or a registered consumer needs it. Exception work is exception-log-natural: the real deliverable is an Excel root-cause matrix (one row per deviation with classification, severity, rationale, root-cause hypothesis, disposition, and handoff fields) paired with a Word findings memo carrying the disposition summary and the elevated-issue handoffs.

Downstream consumers: `workpaper-drafter` reads `exception_register_id` and pulls the classification summary into the workpaper's exceptions-identified section; `risk-compliance-core/skills/issue-writeup` keys off `source_exception_id` and consumes the per-exception handoff package (criterion, condition, cause, effect, recommendation seed) without re-discovering context; `qa-workpaper` reads the full record when reviewing exception treatment for sufficiency. The schema is the cross-skill contract; additive changes only. Add fields, do not rename or repurpose them. A breaking change is a versioned migration with the downstream skills told in advance.
