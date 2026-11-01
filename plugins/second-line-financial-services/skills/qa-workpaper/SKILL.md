---
name: qa-workpaper
description: "Quality-review a completed control-test workpaper for scope, evidence, and conclusions."
argument-hint: "[workpaper ID, exception register ID, prior QA note for re-QA, or pointer to a workpaper population for examiner-prep sweep]"
---

# QA workpaper

QA review of a completed control-test workpaper is the last step before workpaper closure and the audit trail an examiner reads when sampling the firm's testing program. The bar is the AICPA AU-C 230 experienced-auditor sufficiency standard plus the firm's methodology floors: an experienced reviewer with no prior connection to the engagement should be able to read the workpaper, follow the evidence to the conclusion, and reach the same call. Where the workpaper does not pass that bar, the QA review note carries the named deficiencies, a decision, and the rework items.

This skill produces the QA review pack as two artifacts: an Excel workbook with QA markup tabs over the workpaper, and a Word QA memo summary. The skill does not run the test, re-classify the original exceptions, or close the workpaper. It produces the markdown content spec in `templates/default-output.md` shape; rendering goes to the `xlsx` and `docx` skills in `document-skills`. The skill stops at QA reviewer sign-off; disagreement between the QA reviewer and the workpaper reviewer escalates per the firm's named escalation path.

## When to use

Reviews a completed control-test workpaper for QA along named dimensions: scope alignment to the test plan, source-criteria sufficiency, evidence reliability, procedure execution rigor, exception classification, conclusion support, severity calibration, reviewer separation, and remediation handoff. Output is a QA review pack — Excel workbook with QA markup tabs over the workpaper plus a Word QA memo summary — that lists deficiencies by severity, a decision (accept, return for rework, conditional accept), and required rework before workpaper closure.

Best for:
- A second-line QA function or independent reviewer is performing the standard QA pass over a completed workpaper before issue closure or examiner sharing.
- An internal-audit director is rolling up workpaper-quality metrics across a testing cycle and needs structured QA notes per workpaper.
- A targeted Federal Reserve, OCC, FDIC, CFPB, NYDFS, or state DOI exam is imminent and the team is doing a self-QA sweep on the workpaper population the examiner will likely sample.
- A workpaper failed prior QA, was reworked, and needs a post-rework re-QA before closure.

Not the right tool when:
- The workpaper has not been drafted. Use `workpaper-drafter`.
- The test plan itself is being reviewed (design-stage review of `test-plan-builder` output, not QA of a completed workpaper).
- Exceptions identified during QA need their own classification. Use `exception-analysis` for the QA-identified deviations from the methodology, not for the original control deviations the workpaper already classified.
- The work is drafting an issue from a confirmed finding. Use `issue-writeup`; this skill's deficiency findings on the workpaper are not the same as control issues on the entity.

## Ask first

Before reviewing, get plain answers. Most reviews answer them in the workpaper header and the QA scope brief; if not, default and flag.

- **What is the QA scope.** Full-review of a single workpaper, targeted re-review on a specific section, post-issue re-QA after rework, examiner-prep sweep on a workpaper population. Scope drives which named dimensions get the heaviest read and what re-perform expectation applies. An examiner-prep sweep produces population-level deficiency themes plus per-workpaper notes; a targeted re-review focuses on the contested section and skips the rest.
- **Who reads the QA pack.** The workpaper reviewer (the immediate audience for the deficiency findings), the testing manager (rolling up workpaper-quality metrics), the head of compliance testing, internal audit (scoping reliance on second-line testing), the head of regulatory affairs (exam preparation). Audience drives memo length and the population-level synthesis depth.
- **Is the QA reviewer independent of the workpaper reviewer.** Reviewer separation is structural, not advisory, but the structural rigour scales to firm size and team posture. At a large firm with a dedicated QA function, preparer / workpaper reviewer / QA reviewer are three distinct roles. At a smaller firm or a thin pod (a community bank's compliance-testing team of three; a fintech's emerging second line), strict three-role separation is not always achievable and forcing it produces fiction. In that case, the QA scope drops to `targeted-re-review` by a different role with the limitation documented on the face; the firm names a compensating control (rotated reviewer pool; cross-pod QA; external QA at audit-cycle close) and the QA review note carries the structural limitation as a named risk for steering. Don't paper over it.
- **What is the firm methodology floor for severity calibration.** Pulled from `references/firm-overlay.md` if installed, else from `references/source-anchors.md` (AICPA AU-C 265 deficiency / significant deficiency / material weakness hierarchy). Severity inflation and severity deflation are both calibration findings; the floor is the discipline that catches both.
- **Does this workpaper carry open issues.** A clean workpaper does not necessarily mean a closeable issue. The QA review note's decision (accept / return / conditional accept) is distinct from the issue closure approval status; both are filled separately at sign-off.

When `scope` (per `scoping`) is supplied, consume it: `institution.type` and `institution.primary_regulators` set the supervisory framing, `sector_overlay_set` selects which `references/sector-overlays.md#<sector>` loads, `cross_cutting_overlay_set` selects the `references/cross-cutting.md#<topic>` files, `persona.role` sets which decision forum the QA pack passes through, `source_posture` constrains what the body can carry. When it is not supplied, draft against what the workpaper carries, default to the testing program's standing posture, and note in the QA review note that scope was not formalised separately.

## How the QA review gets built

The QA review has the same spine across workpaper types. The QA reviewer reads the workpaper end to end first, then walks the named QA dimensions in the order observation surfaces them, not in lockstep.

The header pins the QA review to the workpaper: QA review ID, workpaper ID (foreign key into `workpaper-drafter` output), test ID (foreign key into `test-plan-builder` output), control ID, period under test, preparer role and date (carried from workpaper), workpaper reviewer role and date (carried from workpaper), QA reviewer role and date, QA scope (full-review, targeted-re-review, post-issue-re-qa, examiner-prep-sweep), engagement ID. Reviewer separation is structural: preparer, workpaper reviewer, and QA reviewer must be three distinct roles. The header is the audit trail when QA is later contested in steering, in court, or with a regulator.

QA criteria names the methodology references this review applied. Standing criteria carry the audit-quality methodology (AU-C 220, 230, 265, 530), the IIA QAIP and supervision standards, the firm methodology, and the loaded sector and cross-cutting overlays. The criteria block is the audit trail for what the QA was measured against.

The deficiency register is the load-bearing body. One row per deficiency. For each:

- **Deficiency ID** is stable across the QA cycle.
- **Section affected** names the workpaper section or sample item where the deficiency surfaced.
- **Category** is one of: `scope-alignment` / `criteria-sufficiency` / `evidence-reliability` / `procedure-execution` / `exception-classification` / `conclusion-support` / `severity-calibration` / `reviewer-separation` / `remediation-handoff` / `formatting`. Category is the load-bearing field; it drives the dimension this deficiency belongs to and the rework expectation.
- **Severity** is `critical` (workpaper must be returned), `major` (rework required, can re-issue), or `minor` (note for future cycles), paired with severity rationale that references the firm methodology floor or the experienced-auditor sufficiency standard. Severity assignment always carries human review.
- **Observation** is the dated, scoped, specific statement of what the QA reviewer saw. "Sample S12 procedure P2 shows pass, but evidence ID is missing and exception register did not flag" is an observation. "Evidence is weak" is a conclusion, not an observation.
- **Methodology reference** names the criterion the workpaper failed against, with a section reference and a pointer into `references/source-anchors.md`, the loaded overlays, or the firm overlay. "Firm methodology" without a section reference is not defensible.
- **Required action** is declarative. What the preparer or workpaper reviewer must do. "Reclassify samples S12-S14 as evidence-gap exceptions and re-aggregate deviation rate" passes. "Consider whether the classification is correct" does not.

Sample re-perform is the QA reviewer's discipline that surfaces substantive deficiencies. The QA reviewer selects a small subsample (typically three to seven items, across the workpaper's stratification), re-performs the procedures, and compares QA outcome to the workpaper's recorded outcome. Divergences route into the deficiency register. The re-perform tab carries the comparison; the deficiency register carries the consequences. QA re-perform is the most credible QA dimension; skipping it on high-stakes workpapers (consumer-facing, examiner-prep, post-issue re-QA, large-deviation-rate populations) weakens the QA posture and the deliverable's defensibility.

Severity calibration challenges the workpaper's severity ratings against the firm methodology floors (where they exist) and against analogous prior workpapers. Floor violations are the calibration deficiency type that has the most consequences: severity inflation (rated medium where the floor is high) buries findings that the examiner will surface anyway; severity deflation buries findings the testing program needs to track. Both directions get pushback. Where the firm has not set methodology floors, the AU-C 265 deficiency / significant deficiency / material weakness hierarchy is the borrowed frame.

Conclusion support assesses whether the workpaper's conclusion (design effectiveness, operating effectiveness, combined where applicable) is supported by the evidence and procedures. The assessment is `supported`, `partially-supported`, or `not-supported`, with rationale. Where conclusion language drifts toward legal-violation framing ("the firm violated [Reg X]"), the QA reviewer rewrites to control-effectiveness language and routes the legal question to legal counsel and the head of regulatory affairs separately. Conclusion-language hygiene is a recurring QA intervention on consumer-facing workpapers; the conduct cross-cutting overlay carries the rewrite pattern.

Decision is the QA reviewer's call: `accept` (workpaper passes QA, minor noted carry forward as housekeeping), `conditional-accept` (workpaper passes once specific rework items are addressed; the rework list is the closure gate), or `return-for-rework` (workpaper does not pass; preparer or reviewer must redo named items and re-submit for QA). Critical deficiencies return the workpaper; major deficiencies typically conditional-accept; minor deficiencies typically accept with the items noted. Issue closure approval status is a separate field: `approved`, `not-approved`, or `not-applicable`. A clean workpaper does not necessarily mean a closeable issue; the workpaper carries open issues that have their own remediation lifecycles.

Reviewer questions captures everything that could not be resolved in the QA review or that the QA reviewer wants the workpaper reviewer to consider before re-submission. Cluster questions for the audience that decides them; severity calibration questions and conclusion-language questions go in the same list when both apply.

The sign-off block carries the QA reviewer role and date and the escalation path if disagreement persists between the QA reviewer and the workpaper reviewer. The escalation typically routes to the testing manager, the head of compliance testing, or internal audit lead per the firm's named gate. Source trace and confidence label close the QA review note: every material claim cites a source with section reference, and the confidence label (`high` / `medium` / `low` / `unknown`) reflects evidence sufficiency for the QA review itself (re-perform completeness, methodology depth applied, time available for the review).

### Sector and cross-cutting overlays

The same QA spine carries different conventions across sectors and cross-cutting topics. Load only the overlays the scope flags:

- `references/sector-overlays.md#banking` is the heaviest overlay in the file set. Bank-supervisory expectations on independent QA over the testing program are explicit in the CFPB CMS examination procedures, the OCC Comptroller's Handbook CMS module, and SR 08-8. The overlay carries the population-definition and extract-integrity QA scope items, the consumer-compliance control-area QA notes (HMDA, CRA, Reg B, Reg DD, Reg E, Reg Z, BSA/AML), and the sponsor-bank examiner-prep-sweep posture.
- `references/sector-overlays.md#insurance` carries the Model Audit Rule ICFR documentation review conventions and the state DOI market-conduct workpaper-review conventions.
- `references/sector-overlays.md#capital-markets` carries the FINRA 3120 / 3130 supervisory-controls QA conventions, the Rule 206(4)-7 annual-review QA conventions, and the conclusion-language hygiene posture (especially important in capital-markets QA because of the enforcement environment).
- `references/sector-overlays.md#payments-fintech` carries the sponsor-bank QA conventions, the Reg E error-resolution clock-driven QA dimensions, the NACHA edition-sensitivity conventions, and the end-customer reconciliation responsibility-split conventions.
- `references/cross-cutting.md#cyber` is the most-loaded cross-cutting overlay. Cyber workpapers fail QA on evidence-reliability more often than financial-control workpapers; the overlay carries the vendor-supplied-scan-result reliance pattern, the screenshot-only access-review pattern, the production-versus-test environment evidence pattern, and the privileged-access tolerable-rate-floor pattern.
- `references/cross-cutting.md#conduct` loads when the workpaper sampled a consumer-impact population. The overlay carries the conclusion-language hygiene pattern (rewriting legal-violation framing to control-effectiveness framing), the customer-harm-distinct-from-technical-control-conclusion pattern, and the UDAAP all-three-prongs consideration pattern.

Privacy and climate cross-cutting overlays follow the same pattern; this skill ships cyber and conduct as the cross-cutting files because they are the most frequent triggers for QA deficiencies. Where firm policy or taxonomy applies (severity floors specific to the firm, named QA-committee gates, escalation paths for QA disagreement, template variants), it lives in `references/firm-overlay.md` and is consumed when present.

## Quality bar

Holds across every QA pack:

- Every deficiency cites a methodology reference. Generic references ("firm methodology" alone) do not pass.
- Source evidence, management assertions, public-source obligations, generated inferences, and open legal or compliance questions stay distinguishable in the QA review note. The artifact shows the seams.
- Severity is paired with rationale that references the firm methodology floor or the experienced-auditor sufficiency standard. Severity assignment always carries human review.
- The QA review note concludes on workpaper-quality dimensions and rework requirements, not on legal violation. Where conclusion-language rewrite is required, the legal question routes to legal counsel separately.
- Preparer, workpaper reviewer, and QA reviewer are three distinct roles. Where genuine independence is not achievable, the limitation is documented, not papered over.
- The skill stops at QA reviewer sign-off. Disagreement escalates per the firm's named gate. Issue closure is a separate decision from workpaper QA closure; both are filled at sign-off.
- No named institutions in the QA review note unless they are public defendants in a finalised enforcement action.

## Adaptation

QA depth and length scale to the workpaper depth and the QA scope. A targeted re-review on a single section reads short; a full review of a high-volume workpaper with a high deficiency count reads longer with deficiencies clustered for the workpaper reviewer. An examiner-prep sweep on a portfolio of workpapers reads as a portfolio QA review with population-level themes plus per-workpaper notes. Sector overlay loading follows scope plus the rule that the regulator the test was designed for drives the sector overlay (HMDA testing pulls banking; an adviser compliance-program test pulls capital-markets; a sponsor-bank end-customer reconciliation test pulls payments-fintech and banking together). Cross-cutting overlay loading: cyber overlay is default-on for any workpaper covering IAM, data-protection, or NYDFS Part 500-mandated areas; conduct overlay is default-on for any consumer-facing workpaper where customer-harm framing matters separately from technical control conclusion. Audience drives shape: a QA pack drafted for the testing manager reads operationally, a QA pack drafted with an examiner sweep in mind reads heavier on the population-level themes and methodology-drift findings, a QA pack drafted for internal-audit reliance reads heavier on reviewer-separation evidence and the QA confidence label.

## Pointers

`references/sector-overlays.md` and `references/cross-cutting.md` hold one section per sector or topic, and `examples.md` one per example. Find the heading and read only that section.

- `references/source-anchors.md` — citations and excerpts for the named anchors (AICPA AU-C 220 / 230 / 265 / 530, IIA Standard 1300 and 2340, FFIEC IT Audit booklet, SR 08-8, OCC PPM 5310-3, COSO 2013 Principle 17, PCAOB QC 1000, sector-specific anchors).
- `references/sector-overlays.md#banking`, `insurance.md`, `capital-markets.md`, `payments-fintech.md` — sector-specific QA conventions loaded per scope. Banking is the heaviest overlay.
- `references/cross-cutting.md#cyber`, `conduct.md` — cross-cutting flavour. Cyber default-on for IAM, data-protection, and Part 500-mandated controls; conduct default-on for consumer-facing populations.
- `references/firm-overlay.md` — firm-installed QA methodology, severity floors, named QA-committee gates, escalation paths, and template variants beyond the regulatory baseline; consumed when present.
- `templates/default-output.md` — content spec for both artifacts (Excel QA markup tabs, Word QA memo summary).
- `examples.md` — Reg E error-resolution QA at a regional bank; examiner-prep TPRM sweep at a mid-size bank holding company.
- `examples.md#troubleshooting` — recurring pitfalls (QA as proofreading, QA reviewer is also the workpaper reviewer, severity inflation, skipping sample re-perform, confusing workpaper closure with issue closure, adversarial tone, scope creep into re-running the test, empty methodology references, missed population-level themes, confidence label always high).

The plugin-level shared references (`references/source-map.md`, `references/policy-control-library.md`, `references/review-gates.md`) sit at the plugin root and are consulted alongside the skill-level files.

## Output

Default to drafting against `templates/default-output.md`. Render as Word, Excel, PowerPoint, or Markdown when the audience or workflow asks for it. Produce the structured record at `schemas/qa-workpaper.schema.json` when downstream automation or a registered consumer needs it. QA work is workpaper-natural: the real deliverable is an Excel test-of-design / test-of-effectiveness workbook with QA markup tabs (header, criteria, deficiencies, sample re-perform, severity calibration, conclusion support, source trace, reviewer questions) paired with a Word cover memo (executive summary, QA scope, deficiency findings, sample re-perform results, severity calibration, conclusion support, decision, reviewer questions, sign-off, source trace and confidence label).

Both artifacts emit together; the QA reviewer signs the Word memo, and the Excel workbook is the supporting documentation. Both file against the workpaper ID. The QA review note is consultative input to the workpaper reviewer for re-submission; the firm's testing-program closure machinery picks up the workpaper after QA sign-off.

## Human review and AI disclosure

Open the deliverable with this line, and remove it only after the review below: `AI-assisted draft. Requires review by a qualified person before use.`

A qualified person with authority to change the output reviews it before it is delivered or relied on, and stays accountable for it. Where the output supports advice to an individual or a decision about an individual (credit, insurance underwriting, pricing or claims, employment, legal rights, or similar), that individual must be told AI was used to produce it. This skill does not make final decisions, file with a regulator, notify customers, execute transactions, or move money or other financial assets.
