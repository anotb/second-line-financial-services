# Troubleshooting — evidence-request-builder

Recurring pitfalls. Read before drafting the request list and again before pre-fielding sign-off.

## Request specificity

### "Provide all relevant documents"

The artifact description must be specific enough that a reasonable owner can fulfill it without a follow-up call. If the request needs a phone call to clarify, the spec is wrong. CSV asks name expected columns; per-sample asks reference the sample-ID set; per-period asks name the period boundary rule (extracted-as-of date, originated-during period, action-taken-during period). The schema requires `artifact_description`; populate it with the specific artifact, not a category.

### Asking for the policy as evidence of operating effectiveness

The policy is the criterion (or part of it), not the evidence. Ask for the artifact that shows the policy was followed, not the policy itself. Where the test plan does need the policy as criterion-source evidence, a single criterion-source request is fine; the procedure-evidence requests then ask for the operating evidence (case files, system extracts, attestation packets, reconciliations) that demonstrates the policy in operation.

### Mixing criteria sources without naming them

A single request row names one criterion source: regulator + section, policy + section, or methodology. If the criterion stack is complex (e.g., a control addresses Reg E §1005.11 plus the firm's expedited-error-resolution policy section plus an external NACHA expectation), split the request into multiple rows. Collapsing multiple criteria into one row makes the workpaper's procedure-to-evidence trace ambiguous.

### Letting the artifact description carry the criterion

The artifact description names what is requested; the criterion source names why. A row that says "the production disclosure for Reg DD §1030.4 [verify subsection]" is collapsing the two; the disclosure is the artifact (PDF), Reg DD §1030.4 is the criterion source, and the row populates both fields rather than one.

## Reliance classification

### Skipping the reliance classification

The reliance classification is the workpaper's prompt to apply the right reliability test. Vendor-supplied evidence (AUS configuration, SOC reports, vendor attestations) and management-prepared evidence (data-quality reconciliation logs, schedules, attestations) carry lower reliability than original system output and require completeness-and-accuracy checks at fieldwork. The schema requires `reliance_classification`; populate it.

### Defaulting everything to original-system-output

Reliance defaults to original-system-output only when the artifact actually is an original-system extract. A management-prepared schedule reconciling two system extracts is management-prepared, not original. A vendor-produced report on the firm's behalf is vendor-supplied, not original. The reviewer separates the classes structurally; defaulting hides the seams.

### External-confirmation requests handled as ordinary asks

External-confirmation requests (AU-C 505) carry distinct conventions: the reviewer (not the control owner) controls the request, the response goes to the reviewer (not back through the firm), and the response evidences the recipient's identity. A request flagged `external-confirmation` triggers AU-C 505 conventions in the workpaper; routing the request through the firm's normal PBC process defeats the purpose.

## Sensitivity classification

### Defaulting everything to internal

A request list that defaults every row to `internal` cannot support the firm's privacy program or the workpaper's downstream handling discipline. NPI, PHI, PCI, SAR-adjacent content, customer narratives, regulator correspondence carry confidential or restricted, not internal. Classify at request time.

### Treating SAR content as a normal request

SAR content access is restricted under 31 CFR §1020.320 [verify subsection]. A request for SAR content from a tester without the access posture is a control failure on the request list itself. The standard pattern is to request the case-management file with the BSA officer's sign-off on access posture, or to route SAR-decision testing to a separate cycle with the right access posture; either way, the request list documents the access-control posture rather than restating SAR content.

### Treating customer prompts in AI testing as internal evidence

Customer prompts to AI systems are NPI by default. The request list classifies sensitivity (typically restricted) and asks for the firm's prompt-and-output logging configuration evidence rather than restating customer content; where customer content is requested for sample-level inspection, the request names the de-identification posture and the access-control routing.

## Format and source-of-record discipline

### Accepting screenshots on data-integrity tests

Screenshots are weak evidence on data-integrity tests; they show a screen state at a moment in time without a system-of-record link to replay the data. CSV with named columns from the system of record is the standard for data-integrity testing; specify it in the format and reject screenshots in the format-accepted column. Where a screenshot is the appropriate format (a configuration-screen design-effectiveness procedure), name it explicitly with the timestamp expectation.

### Naming "internal database" as the system of record

Name the system. LAR generation system, loan origination system, IAM (Okta, Azure AD, named platform), HR platform, ticketing system (ServiceNow, Jira), surveillance archive (Smarsh, Global Relay, Bloomberg Vault), claim-management system, BSA case-management system. Generic labels do not survive the workpaper's reliance test or the closure-binder's provenance check. Where the firm pseudonymises systems in artifacts shared externally, the firm-overlay carries the mapping; the request list names the system.

### Test-environment evidence offered for production-control reperformance

Reperformance procedures against production controls (demographic firewall, IAM access in production, encryption-at-rest in production) require production-environment evidence. A request that does not specify production scope risks the firm offering test-environment evidence that does not satisfy the procedure. Specify the environment in the artifact description.

## Population and sample reference

### Requests without a population reference

A request without a sample-ID set or a full-population pointer is not testable. The workpaper later cannot reconcile what was tested against what was asked. The schema does not require `population_reference` (some requests are population-level by design — the SoD exception log for the period, the IAM-system change log for the period — and reference the period only), but the field is the workpaper's bridge from request to sample-level evidence inspection, so populate it where the request is sample-driven.

### Asking for the full population when the procedure tests a sample

A request for "the full LAR" when the procedure tests 60 records is over-asking; the firm fields the larger ask, and the workpaper later inspects only the sampled records. Ask for the sampled records (per the sampling memo) plus the population-level reconciliation evidence (which is a separate, smaller request). Over-asking burns the firm's fielding capacity and trains owners to deprioritise testing requests.

### Asking for the sample when the procedure tests the full population

The inverse: a request for "the 30-record sample" of an exception register when the test is integrity-of-the-register-for-the-period. The full population is the right ask; the procedure inspects the entire register against the firm's exception-log discipline.

## Boundary discipline

### Drafting evidence pulls before reviewer sign-off

Pre-fielding sign-off is the discipline equivalent of pre-fieldwork sign-off on the test plan. Fielding requests before the reviewer signs off the request list is a methodology weakness; the firm receives requests that the reviewer has not approved and the testing program loses the audit trail. The reviewer signs the request list before it is fielded; the schema captures both the preparer date and the reviewer date.

### Treating the request list as a workpaper

The request list documents what was asked and the status. Conclusions on operating effectiveness, design effectiveness, and exceptions live in the workpaper. A request list that carries a "conclusion" column has overstepped; the workpaper consumes the closed request list and writes the conclusion against the inspected evidence.

### Treating the request list as the closure binder

The request list is the operational ask at fieldwork start. The closure binder (`evidence-binder` in `risk-compliance-core`) is the index of artifacts produced at the end of fieldwork, with provenance and sufficiency calls. The two are different artifacts at different lifecycle points. The closed request list flows into the closure binder; the binder is not the request list with status filled in.

### Forgetting the not-applicable section

Without the not-applicable section, the next year's reviewer re-asks for items that were intentionally out of scope and wastes the owner's time. Items out of period, items in another cycle's scope, items at a separate population stratum, items at restricted-access posture — name them with the rationale and the covering test ID where applicable. Closing the loop on what was not asked is as load-bearing as closing the loop on what was asked.

### Inviting the first-line owner to draft the request list

The request list is second-line work product. First-line input is welcome on artifact format and system-of-record naming, but the request list is signed off by the testing reviewer, not the control owner. A request list drafted by the control owner is the methodology equivalent of self-attestation on what evidence the test will see.

## Engagement-scope and overlay loading

### Loading the wrong sector overlay

Institution type and the regulator the control was designed for drive the sector overlay. HMDA controls pull banking; an adviser compliance-program control pulls capital-markets; a sponsor-bank end-customer reconciliation control pulls payments-fintech and banking together (dual-overlay loading is normal for sponsor-bank arrangements). Do not collapse to one overlay when the engagement scope says two.

### Skipping cyber overlay on IAM or Part 500 populations

Cyber overlay is default-on for any control test touching IAM, data-protection, or NYDFS Part 500-mandated areas. Skipping the cyber overlay because the test is "operationally categorised as compliance" misses the §500.7, §500.5, §500.15, and §500.17(b) [verify subsections] frame and the privileged-account sensitivity discipline.

### Skipping privacy overlay on requests touching NPI/PHI/PCI

Privacy overlay loads whenever the request list will pull artifacts containing NPI, PHI, PCI, or other regulated personal data, regardless of how the engagement-scope reads. The overlay drives sensitivity classification, redaction posture, and minimum-necessary discipline at request time.

## Output discipline

### Citing without sections

Every regulator citation in the criterion-source field carries a section reference or a `[verify section]` placeholder. URL alone does not pass the source-anchor depth check. Use `references/source-anchors.md` and the loaded overlays for the canonical citation set; do not restate excerpts in the request list body.

### Marking unsupported claims silently

Use `[evidence needed]` explicitly where a claim (a criterion section, a system-of-record name, a population boundary rule) is not yet evidenced. An inferred claim presented as evidenced is the failure mode that propagates to the workpaper.

### Closing with too much certainty

The confidence label is `high` only when source posture, criteria maturity, firm-policy maturity for the control area, and prior-cycle history line up. `medium` and `low` are normal where the source posture is below evidence-aware, where the firm policy is the only criterion for a specific value (with no external benchmark), or where the control area is new and prior-cycle history is thin. `unknown` is honest where the firm has not yet resourced the planning input.

### Filling the reviewer-questions section with questions the preparer answered

A reviewer question is something the preparer cannot resolve and is asking the named reviewer to decide before sign-off. A question the preparer answers in the request list is not a reviewer question; it is a footnote.

### Rendering the markdown when the deliverable is xlsx

The deliverable is an Excel workbook produced via the `xlsx` skill in `document-skills`. The markdown in `templates/default-output.md` is the content spec, not the artifact. Producing the markdown without rendering the workbook stops short of the deliverable; the xlsx render is the artifact the firm fields.
