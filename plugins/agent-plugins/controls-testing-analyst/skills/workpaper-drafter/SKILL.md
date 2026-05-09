---
name: workpaper-drafter
description: |
  Drafts the testing workpaper for a single control test cycle once evidence has been inspected and procedures executed. Captures source criteria, walkthrough, evidence inspected, procedures performed, sample-level results, exception aggregation, and a separate design and operating effectiveness conclusion. Output is the standard testing workpaper a QA reviewer, internal audit reviewer, or examiner expects, formatted so each conclusion ties back to evidence.

  Best for:
  - A compliance-testing or internal-audit team has finished evidence inspection and procedure execution and needs the workpaper drafted from those results.
  - A second-line reviewer is documenting a targeted, off-cycle review (regulatory-change triggered, incident-triggered, examiner request) and the workpaper is the artifact.
  - A QA reviewer is rebuilding a workpaper that failed prior QA, working from the same evidence and exception register.

  Not the right tool when:
  - Testing has not been done. Pre-fieldwork scoping is `test-plan-builder`; sample design is `control-sampling`; evidence asks are `evidence-request-builder`.
  - The job is QA on a completed workpaper. That is `qa-workpaper`. Boundary: this skill writes the workpaper from results; `qa-workpaper` reviews the completed workpaper for sufficiency. Sequential, not redundant.
  - Exceptions still need to be classified before the conclusion can land. Run `exception-analysis` first; this skill consumes its register.
  - The work is writing up a confirmed finding for issue tracking. That is `issue-writeup` in `risk-compliance-core`; this skill hands off to it.
argument-hint: "[test plan ID, exception register ID, evidence inspection notes, or pointer to completed fieldwork]"
---

# Workpaper drafter

A testing workpaper is what compliance-testing or internal-audit produces so a QA reviewer, the testing manager, internal-audit lead, or an examiner picking up the file later can see what was tested, what evidence was inspected, what the sample showed, and what the conclusion is. The bar is the AU-C 230 test: an experienced reviewer with no prior connection to the engagement should be able to read this workpaper and understand the work performed and the conclusions reached.

This skill writes the workpaper from completed fieldwork. It does not run the test, classify exceptions, or close findings. It drafts the workpaper against `templates/default-output.md` and emits a structured record conforming to `schemas/workpaper.schema.json` for downstream consumers (QA, issue write-up, internal audit). The skill stops at preparer sign-off; the named reviewer signs separately.

## Ask first

Before drafting, get plain answers. Most cycles answer them in the test plan and exception register; if not, default and flag.

- **Whose workpaper is this for.** QA reviewer, internal audit, the examiner who will read it next quarter, the regulator who may pull it in three years. Audience drives length and how much methodology gets restated. A workpaper drafted for an upcoming exam reads heavier on criteria than the same workpaper drafted for in-cycle QA.
- **Has fieldwork actually finished.** Walkthrough completed, evidence inspected, procedures executed, exceptions classified by `exception-analysis`. Where fieldwork is genuinely complete the workpaper drafts to final. Where fieldwork is in flight (a long cycle with rolling waves of evidence; a vendor delivery still pending; an exception register that is being classified in parallel), draft an *in-flight* workpaper with the sections that are closed populated and the conclusion section blocked: each conclusion field carries `[blocked: pending fieldwork closure]` and the named reviewer cannot sign final until those blocks resolve. The in-flight workpaper is a working document the cycle can iterate on; the final workpaper is what the named reviewer signs after fieldwork closes. Marking the workpaper "draft" without naming the in-flight blocks is the QA defect to avoid.
- **Did the executed procedures match the test plan.** If yes, draft against the plan. If no, document the divergence as a scope change with the named reviewer's pre-fieldwork sign-off, or flag silent drift as a finding the workpaper itself surfaces. Silent drift is a QA finding.
- **What is the exception register saying.** Pull the classified exception register from `exception-analysis`. The conclusion language (effective / partially effective / not effective / inconclusive) flows from the register plus the sample-aggregation read, not from the drafter's intuition.

When `scope` is supplied, consume it: `institution.type` and `institution.primary_regulators` set the citation focus and tone, `sector_overlay_set` selects which `references/sector-overlays/<sector>.md` loads, `cross_cutting_overlay_set` selects the `references/cross-cutting/<topic>.md` files. When it is not supplied, draft against what is on file (the test plan usually carries enough), default to the testing program's standing posture, and note in the workpaper that scope was not formalised separately.

## How the workpaper gets built

The workpaper has the same spine across control types. A senior preparer fills it in roughly in the order fieldwork happened, not in lockstep.

The header pins the workpaper to its test cycle: workpaper ID, test ID (foreign key into `test-plan-builder` output), control ID, obligation ID, period under test, business unit, jurisdiction, preparer role and date, reviewer role and date placeholder, QA placeholder. Reviewer separation is structural, not advisory: the same role cannot both prepare and review. The header is the audit trail when the file is reopened later.

Scope and source posture restates the test plan's scope in two or three sentences and names the source posture the testing operated under (public-only, public-plus-firm-policy, public-plus-firm-policy-plus-evidence, connector-aware). The pointer to the test plan goes here. If the executed procedures diverged from the plan, that goes here as a named scope change with the pre-fieldwork sign-off reference, not buried in the procedures section.

Source criteria names the criteria the test was designed to evaluate. For each criterion the workpaper carries the source (regulator and instrument), the section reference, and either a verbatim excerpt or a paraphrase tight enough that the criterion is unambiguous. This is the regulatory frame; the loaded sector and cross-cutting overlays add sector-specific or topical detail by reference, not restated. Cite by file path into `references/source-anchors.md` and the loaded overlays.

Walkthrough summary captures the design-effectiveness signal: who was interviewed, what was observed, which screens or systems were inspected, and the walkthrough conclusion as a design-effectiveness signal. The walkthrough is not the test; it is the design read that justifies the test plan's procedures. If the walkthrough surfaced a design gap before any sampling happened, that goes here and the conclusion section picks it up.

Evidence inspected lists every evidence item with a stable ID, the system of record it came from, the reliance classification (system-of-record extract, system-generated report, management-prepared schedule, vendor-supplied evidence, third-party assurance), and the request_id that ties back to `evidence-request-builder`. Vendor-supplied and management-prepared evidence carry an explicit reliance test note: completeness check, accuracy check, and what the preparer relied on to accept it. SOC 1 Type II coverage on a vendor system goes here when relied upon, with the CUEC posture noted; reliance on prior-period testing is named with the prior workpaper ID.

Procedures performed restates each procedure from the test plan, gives execution notes (what the preparer actually did, not what the plan said to do), and lands a procedure-level conclusion. If a procedure could not be executed as designed, the workaround procedure and the reviewer's pre-fieldwork sign-off on the workaround sit here. Each procedure ID matches the test plan; new procedures added in fieldwork are flagged as additions with the pre-fieldwork sign-off reference.

Sample-level results is the table the QA reviewer scans first. One row per sample item: sample ID, evidence reviewed (by ID), procedure outcome per procedure ID, exception flag, exception ID where flagged. The exceptions are not classified here; they are surfaced. Classification lives in the exception register from `exception-analysis`.

Exceptions identified pulls the classified exception register from `exception-analysis` (cite by exception_register_id) and summarises by classification and severity: how many design exceptions, how many operating exceptions, how many critical, how many documentation. The summary is read against the test plan's tolerable deviation rate, not invented here.

Aggregation and projection compares observed deviation rate against the tolerable rate set in the test plan, and adds the projection commentary the conclusion will lean on: anomaly versus systemic, concentration in a particular segment or process or region, sample-design implication if the deviation rate suggests the population is not behaving as the sample assumed. Projection commentary is read; it does not invent statistical claims the sample was not designed to support.

Conclusion is two reads, sometimes three. Design effectiveness (effective / partially effective / not effective / inconclusive) reflects the walkthrough plus any design exceptions surfaced in fieldwork; design-not-effective on a test where operating effectiveness was the focus still gets called out, even if the test plan did not nominally cover design. Operating effectiveness (same enum) reflects the sample-level results and the aggregation read against tolerable. A combined conclusion is added when the test plan calls for it. Conclusion language stays in second-line vocabulary: "the control did not operate as designed for the [segment] population during the period," not "the firm violated [Reg X]." Second-line workpapers conclude on control effectiveness; legal violation language is for legal counsel and regulator-led determinations, not for the workpaper.

Issues elevated names every issue handed to `risk-compliance-core/skills/issue-writeup`, with the issue handoff ID and severity. The workpaper does not draft the issue; it elevates and points. The handoff package (criterion, condition, cause, effect, recommendation seed) is built from the exception register's classification fields and is the bridge into issue-writeup.

Reviewer questions captures everything that could not be resolved in fieldwork or that the preparer wants the named reviewer to consider before sign-off. A reviewer question that the preparer answers themselves is not a reviewer question. Cluster questions for the audience that decides them; testing-management questions and internal-audit questions go in the same list when both apply.

Limitations and reliance is the protection paragraph. What the workpaper does not conclude on (a separate control, a separate process, a different period, a different population segment), what reliance was placed on prior testing or vendor SOC 1 / SOC 2 work or management-prepared schedules, and what scope exclusions the test plan had. A workpaper without a limitations section gives a QA reviewer nothing to push back on; absence is itself a defect.

The sign-off block carries preparer, reviewer (separate role), and QA placeholder. Preparer signs with date. Reviewer signs with date. QA placeholder is filled by `qa-workpaper`, not here. Source trace and confidence label close the file: every material claim cites a source with section reference, and the confidence label (high / medium / low / unknown) reflects evidence sufficiency, sample size, source posture, and any reliance on second-hand evidence.

## Quality bar

Holds across every workpaper: every conclusion sentence ties to a procedure result that ties to an evidence item; the AU-C 230 experienced-reviewer test is the bar. Source evidence, management assertion, public-source obligation, generated inference, and open legal or compliance question stay distinguishable. Citations carry section references or `[verify section]` markers; URL alone does not pass. Preparer and reviewer are different roles. Conclusions speak to control effectiveness, not legal violation. The workpaper stops at preparer sign-off; the reviewer signs separately and QA is downstream. No named institutions in the workpaper unless they are public defendants in a finalised enforcement action.

## Adaptation

Workpaper depth and length scale to control complexity, sample size, and exception volume. A clean, low-volume control test with no exceptions reads short; a high-volume test with classified exceptions across multiple severities reads longer with the exception summary clustered for the audience that decides next steps. Sector overlay loading follows scope plus the rule that the regulator the test was designed for drives the sector overlay (HMDA testing pulls banking; an adviser compliance-program test pulls capital-markets; a sponsor-bank end-customer reconciliation test pulls payments-fintech and banking together). Cross-cutting overlay loading: cyber overlay is default-on for any control test touching IAM, data-protection, or NYDFS Part 500-mandated areas; conduct overlay is default-on for any consumer-facing test where customer-harm framing matters separately from technical control conclusion. Privacy overlay loads when GLBA Safeguards or HIPAA touches the population. Audience drives shape: a workpaper for QA reads operationally, a workpaper drafted with an upcoming exam in mind reads heavier on criteria and limitations.

## Pointers

- `references/source-anchors.md` — citations and excerpts for the named anchors.
- `references/sector-overlays/banking.md`, `insurance.md`, `capital-markets.md`, `payments-fintech.md` — sector-specific workpaper conventions loaded per scope.
- `references/cross-cutting/cyber.md`, `conduct.md` — cross-cutting flavour; cyber default-on for IAM and Part 500 controls, conduct default-on for consumer-facing tests.
- `references/firm-overlay.md` — firm-installed methodology, taxonomy, decision checkpoints, and template variants beyond the regulatory baseline; consumed when present.
- `templates/default-output.md` — workpaper template.
- `schemas/workpaper.schema.json` — structured-output contract for downstream consumption.
- `examples/` — HMDA LAR data-integrity workpaper; NYDFS Part 500 access-recertification workpaper.
- `TROUBLESHOOTING.md` — recurring pitfalls (conclusions untied to evidence, mixing inspection with conclusion, legal-violation language, reviewer-separation breaks, silent test-plan drift).

The plugin-level shared references (`references/source-map.md`, `references/policy-control-library.md`, `references/review-gates.md`) sit at the plugin root and are consulted alongside the skill-level files.

## Output

Default to drafting against `templates/default-output.md`. Render as Word, Excel, PowerPoint, or Markdown when the audience or workflow asks for it. Produce the structured record at `schemas/workpaper.schema.json` when downstream automation or a registered consumer needs it. The standard real-world deliverable in most engagements is a Word workpaper with the named sections, often paired with an Excel sample-results tab when the sample is large.

Downstream consumers: `qa-workpaper` reads the full record for sufficiency review; `risk-compliance-core/skills/issue-writeup` reads `issues_elevated` and pulls the handoff packages built from the exception register; internal audit consumes the workpaper as supporting documentation when scoping reliance on second-line testing. The schema is the cross-skill contract; additive changes only. Add fields, do not rename or repurpose them. A breaking change is a versioned migration with the downstream skills told in advance.
