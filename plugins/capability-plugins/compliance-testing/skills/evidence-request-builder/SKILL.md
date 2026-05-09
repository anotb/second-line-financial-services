---
name: evidence-request-builder
description: |
  Drafts the provided-by-client (PBC) evidence request list for a single control test cycle: one numbered row per ask, each carrying the control objective tested, criterion source, artifact requested, format, system of record, owner role, due date, population reference, reliance classification, and status. Produced before fieldwork begins; tracked through fieldwork; closed when every row resolves to received-or-not-applicable. The deliverable is an Excel workbook rendered via the `xlsx` skill in `document-skills`. Downstream, the workpaper consumes the request_id per evidence row and the closure binder consumes the closed list as the index of what was produced.

  Best for:
  - A compliance-testing or internal-audit pod has a signed test plan and is preparing the evidence ask before fieldwork begins.
  - A second-line reviewer is preparing for an upcoming examination and needs to pre-anticipate the regulator's evidence asks against current control coverage.
  - A QA reviewer is building a re-perform request list to redo a workpaper because the original evidence trail was thin.

  Not the right tool when:
  - The test scope and procedures have not been written. Use `test-plan-builder` first; this skill consumes the test plan's procedures and criteria.
  - The sample has not been designed. Use `control-sampling` first where the requests need a sample-ID set; small inline samples can be drafted alongside the request list, large samples sit in a sampling memo this skill references.
  - Evidence is in hand and the work is documenting test results. Use `workpaper-drafter`.
  - The work is QAing a completed workpaper for evidence sufficiency. Use `qa-workpaper`.
  - The work is assembling the evidence index after fieldwork closes. Use `evidence-binder` in `risk-compliance-core` — that skill indexes what was produced; this skill asks for what is needed. The two are different artifacts at different lifecycle points.
argument-hint: "[test plan ID, sampling memo ID, control area, or scenario for the period under test]"
---

# Evidence request builder

A PBC list is the evidence ask the testing pod fields before fieldwork begins. Each row names what is being asked for, of whom, by when, against which criterion, in what format, from which system, and at what reliance class. The named reviewer signs the list before it is fielded; the firm fields the list; rows resolve to received, received-partial, re-asked, closed, not-applicable, or deferred; and the closed list flows into the workpaper as the bridge from procedure to evidence inspected, and into the closure binder as the index of what was produced.

The deliverable is typically an Excel workbook rendered via the `xlsx` skill in `document-skills` because PBC lists live in spreadsheets through fieldwork (statuses updated as rows resolve, pivots run for routing and cadence management). The markdown in `templates/default-output.md` carries the named sections, fields, and the request-row contract; render to xlsx where the firm's workflow consumes a workbook, render to Word or Markdown where the deliverable is a discrete document (a regulator-bound pre-exam letter; a closure-pack appendix; a firm-internal memo where the spreadsheet is overkill). The format choice follows the workflow; the row-level contract is the same either way.

This skill produces that list. It does not run the test, draw the sample, draft the workpaper, classify exceptions, or assemble the closure binder. It produces the request list per `templates/default-output.md` shape, conforms to `schemas/evidence-request.schema.json`, and stops at preparer sign-off. The named reviewer signs separately, before fielding.

## Ask first

Before drafting, get plain answers. Most cycles answer them from the signed test plan plus the sampling memo; if not, default and flag.

- **Whose list is this for fielding to.** First-line control owners typically; in some firms a second-line operations team fields requests on behalf of the control owners. The owner-role column drives routing and the escalation path drives unresponsive-owner handling.
- **Has the test plan been signed off.** A request list before pre-fieldwork sign-off on the test plan is fielding evidence against an unsigned scope, which is a methodology weakness on both artifacts. Stop and route to `test-plan-builder` if not. Where the cycle cannot wait (regulator request with a clock; examiner-prep deadline; in-flight enforcement response), draft a *pro-forma* PBC list that names the unsigned scope explicitly in the cover and limitations sections, marks every row's `criterion_source` with `[scope unsigned — verify on test-plan sign-off]`, and routes the unsigned-scope risk to the named reviewer for explicit acknowledgement. The artifact is still useful (the firm can pre-stage evidence the eventual scope will likely need); the methodology weakness is on the face, not buried.
- **Has the sample been designed.** Where the requests need sample IDs, the sampling memo is the source. For small inline samples, the test plan's `inline_sample_design` is the source. Without a sample, the request list cannot reference the population at the row level for sample-driven procedures.
- **What does the firm already know about the evidence in this control area.** Prior cycle's request list, prior cycle's exceptions on evidence sufficiency, repeat-issue areas, system-of-record changes since last cycle. The previous list is the strongest input; the current list is largely a revision.
- **Has anything material changed since the last cycle.** System migrations, new vendor relationships, policy updates that changed where evidence sits, regulator letters that shifted what evidence the firm should be able to produce. Reusing a prior list without re-reading the system-of-record landscape is the most common drafting failure.

When `scope` is supplied, consume it: `institution.type` and `institution.primary_regulators` set the citation focus and tone, `sector_overlay_set` selects which `references/sector-overlays/<sector>.md` loads, `cross_cutting_overlay_set` selects the `references/cross-cutting/<topic>.md` files. Privacy overlay loads whenever the request list will pull artifacts containing NPI, PHI, PCI, or other regulated personal data, regardless of how the scope reads. When scope is not supplied, draft against what is on file (the test plan usually carries enough), default to the testing program's standing posture, and note in the request list that scope was not formalised separately.

## How the list gets built

The list has the same spine across control types. A senior preparer fills it in roughly in the order a reviewer expects to read it.

The header pins the list to its test cycle: request list ID, test ID (foreign key into `test-plan-builder` output), control ID, obligation IDs, period under test, business unit, jurisdiction, source posture, preparer role and date, reviewer role and date placeholder, escalation path. The header is the audit trail when the cycle is later reopened. Reviewer separation is structural: the same role cannot both prepare and review. The reviewer signs the list before fielding.

The scope statement restates the test plan's scope in two or three sentences and confirms the source posture the requests operate under. The pointer to the test plan goes here. Where the request list addresses a subset of the test plan's procedures (the design-effectiveness procedures only, or the operating-effectiveness procedures only because design was tested in the prior cycle), the scope statement names the subset.

The request rows are the body of the artifact. One row per ask. The contract is fixed: every row carries `request_id`, `control_objective`, `criterion_source`, `artifact_description`, `format_requested`, `system_of_record`, `owner_role`, `due_date`, `reliance_classification`, `sensitivity`, and `status`; sample-driven rows also carry `population_reference`. The schema enforces the contract; populate every required field rather than relying on free-form notes.

A few rules are non-negotiable on the rows:

- **Specificity.** The artifact description is specific enough that a reasonable owner can fulfill it without a follow-up call. CSV asks name expected columns. Per-sample asks reference the sample-ID set in `population_reference`. "Provide all relevant documents" fails the specificity bar.
- **One criterion per row.** The criterion source names a single regulator + section, policy + section, or methodology. If the criterion stack is complex, split the request into multiple rows.
- **Named system of record.** "Internal database" does not pass; name the system. Where the firm pseudonymises systems in artifacts shared externally, the firm-overlay carries the mapping; the request list names the system.
- **Reliance classification.** Original system output, vendor-supplied, management-prepared, third-party-assurance, external-confirmation. Drives the workpaper's reliability assessment. Defaulting everything to original-system-output hides the seams.
- **Honest sensitivity.** NPI, PHI, PCI, SAR-adjacent content, customer narratives, regulator correspondence carry confidential or restricted, not the internal default. Drives downstream handling and routing. Set at request time, not on receipt.
- **Population reference where the procedure is sample-driven.** Without it, the workpaper later cannot reconcile what was tested against what was asked.
- **Format that fits the procedure.** Screenshots are weak evidence on data-integrity tests; CSV with named columns is stronger. Signed-memo is appropriate where the artifact is itself a management-prepared statement. Where a screenshot is the appropriate format (a configuration-screen design-effectiveness procedure), name it explicitly with the timestamp expectation.

The not-applicable section captures items intentionally not requested with rationale. Out-of-period records, items in another cycle's scope, items at a separate population stratum, items at restricted-access posture — name them with the rationale and the covering test ID where applicable. Without the not-applicable section, the next year's reviewer re-asks for items that were intentionally out of scope and wastes the owner's time. Closing the loop on what was not asked is as load-bearing as closing the loop on what was asked.

The limitations section names period coverage, reliance posture (vendor, management-prepared, prior-period), access constraints (SAR, PHI, on-chain), and any other constraint the workpaper will need to reflect. The limitations are the reviewer's protection paragraph: they declare upfront what the request list will not get to so the workpaper does not over-reach later.

The downstream-consumers section names the skills that consume the list (`workpaper-drafter` consuming `request_id` per evidence row; `evidence-binder` consuming the closed list as the index of what was produced). Naming the consumers makes the cycle's lifecycle visible at request-list time.

The reviewer-questions section captures everything that could not be resolved by the preparer and that the preparer wants the named reviewer to consider before pre-fielding sign-off. A question the preparer answers in the list is not a reviewer question. The sign-off block carries preparer (with date) and reviewer (separate role; signs before fielding). Source trace and confidence label close the file: every material claim cites a source with section reference, and the confidence label (high / medium / low / unknown) reflects source posture, criteria maturity, and any open question on the request set.

## Boundary with `evidence-binder`

`evidence-request-builder` is the PBC list at fieldwork start. `evidence-binder` (in `risk-compliance-core`) is the closure pack at the end. The two are different artifacts at different lifecycle points and live in different plugins for that reason.

The request list asks for evidence: numbered, owner-routed, due-dated, status-tracked. The binder indexes evidence: provenance, custodian, sufficiency call, sign-off. The closed request list flows into the binder; the binder is not the request list with status filled in.

When the work is asking for evidence ahead of fieldwork, this skill is the right tool. When the work is indexing evidence after fieldwork closes (for the workpaper of record, the exam-response file, the model-validation pack, the vendor-review file), the binder is the right tool.

## Pointers

- `references/source-anchors.md` — citations and excerpts for the named anchors.
- `references/sector-overlays/banking.md`, `insurance.md`, `capital-markets.md`, `payments-fintech.md` — sector-specific request-list conventions loaded per scope.
- `references/cross-cutting/cyber.md` — cross-cutting flavour; cyber default-on for IAM, data-protection, and Part 500 controls.
- `references/cross-cutting/privacy.md` — cross-cutting flavour; privacy default-on whenever the request list pulls artifacts containing NPI, PHI, PCI, or other regulated personal data.
- `references/firm-overlay.md` — firm-installed PBC-template variants, system-of-record naming map, escalation paths, owner-role conventions; consumed when present.
- `templates/default-output.md` — content spec for the PBC list (named sections, fields, request-row contract). The xlsx render maps the sections to worksheets.
- `schemas/evidence-request.schema.json` — structured-output contract consumed by `workpaper-drafter` (request_id per evidence row) and `evidence-binder` (closed list as index input).
- `examples/` — HMDA LAR data-integrity PBC list; NYDFS Part 500 access-recertification PBC list.
- `TROUBLESHOOTING.md` — recurring pitfalls (under-specific artifact descriptions, mixed criteria per row, default reliance and sensitivity, screenshots on data-integrity tests, generic system-of-record names, fielding before sign-off, request list as workpaper, request list as closure binder, missing not-applicable section).

The plugin-level shared references (`references/source-map.md`, `references/policy-control-library.md`, `references/review-gates.md`) sit at the plugin root and are consulted alongside the skill-level files.

## Output

The skill emits the request list per `templates/default-output.md` shape and a structured record conforming to `schemas/evidence-request.schema.json`. Default render is via the `xlsx` skill in `document-skills` (Worksheet 1 cover and scope; Worksheet 2 request summary; Worksheet 3 evidence request rows, freeze-paned on header row and Request ID column, with status and sensitivity conditional formatting; subsequent worksheets carry not-applicable items, limitations, downstream consumers, reviewer questions, sign-off, and source trace). Where the engagement workflow asks for a Word or Markdown deliverable instead (a pre-exam letter to a regulator; a memo bound into a closure pack; a small request list where the spreadsheet is overkill), render to that format with the same row-level contract.

The structured record is the cross-skill contract: `workpaper-drafter` reads `requests[].request_id` to populate the workpaper's evidence-inspected table per evidence row; `evidence-binder` reads the closed list as the index of what was produced. The schema is additive only — add fields, do not rename or repurpose them. A breaking change is a versioned migration with the downstream skills told in advance.

The skill stops at preparer sign-off; the reviewer signs separately, before fielding.
