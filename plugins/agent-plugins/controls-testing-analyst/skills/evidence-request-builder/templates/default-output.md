# Evidence request list (PBC)

The deliverable is an Excel workbook produced via the `xlsx` skill in `document-skills`. This markdown carries the named sections, fields, and the request-row schema. The renderer maps each section to a worksheet (or to a single workbook with grouped tabs depending on list size). Practitioners edit the structure to match the firm's PBC template variant; the request-row contract is fixed.

## Worksheet 1 — Cover and scope

| Field | Value |
|---|---|
| Request list ID | [stable ID per firm naming convention, e.g., ER-CMP-HMDA-2026-01] |
| Test ID | [foreign key into test-plan-builder output] |
| Control ID | [firm control register ID] |
| Obligation IDs | [firm obligation register IDs; one or more] |
| Engagement ID | [pointer to engagement-scope record, or "none — scope not formalised separately from test plan"] |
| Period under test | [start date — end date] |
| Business unit | [name; role-level, not individual-level] |
| Jurisdiction | [primary; list secondary if multi-jurisdiction] |
| Source posture | [public-only | public-plus-firm-policy | public-plus-firm-policy-plus-evidence | connector-aware] |
| Preparer (role) | [e.g., compliance-testing analyst] |
| Preparer date | [ISO date] |
| Reviewer (role) | [separate role from preparer; e.g., compliance-testing manager] |
| Reviewer pre-fielding sign-off date | [filled at sign-off; precedes fielding date] |
| Escalation path | [role-level; e.g., testing manager, then chief compliance officer] |
| Confidence label | [high | medium | low | unknown] |

### Scope statement

Two to three sentences. What the request list covers, what is in and out of scope, what triggered the cycle.

## Worksheet 2 — Request summary

| Field | Value |
|---|---|
| Request count | [n] |
| Earliest due date | [ISO date] |
| Latest due date | [ISO date] |
| Owner-role count | [n distinct roles fielding requests] |
| Repeat-issue area count | [n requests touching prior-cycle issue areas] |
| Restricted-sensitivity row count | [n] |

## Worksheet 3 — Evidence request rows

The body of the deliverable. One row per request. Render as a single sheet; freeze the header row and the request-ID column.

| Request ID | Control objective | Criterion source | Artifact description | Format | System of record | Owner role | Due date | Population reference | Reliance classification | Sensitivity | Status | Received date | Received evidence ID | Re-ask count | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R001 | | [single named source: regulator + section, policy + section, or methodology] | [specific artifact; not "all relevant documents". CSV asks name expected columns] | [pdf | csv | system-export | screenshot | signed-memo | case-file | report-extract | other] | [named system, not "internal database"] | [role, not individual] | [ISO date] | [sample IDs or full-population pointer] | [original-system-output | vendor-supplied | management-prepared | third-party-assurance | external-confirmation] | [public | internal | confidential | restricted] | [open | received | received-partial | re-asked | closed | not-applicable | deferred] | [filled on receipt] | [stable evidence ID assigned on receipt] | [n] | [free text; clarifications, partial-receipt commentary] |

### Field rules

- **Request ID** — stable; carried into the workpaper's evidence-inspected table and the closure binder. Do not renumber on revision.
- **Control objective** — what the evidence supports. Tied to a procedure in the test plan, not free-form.
- **Criterion source** — single named source per row. If the criterion stack is complex, split the request into multiple rows.
- **Artifact description** — specific enough to be fulfilled without a follow-up call. CSV asks name the expected columns. Per-sample asks reference the sample-ID set in `population_reference`. "Provide all relevant documents" fails the specificity bar.
- **Format** — request the format the workpaper needs. Screenshots are weak evidence on data-integrity tests; CSV with named columns is stronger. Signed-memo is appropriate where the artifact is itself a management-prepared statement.
- **System of record** — name the system or report. "Internal database" does not pass.
- **Owner role** — role-level. Individual names are operational metadata the firm tracks separately, not part of the methodology artifact.
- **Population reference** — sample IDs (from the sampling memo) or a full-population pointer. Without it, the request is not testable.
- **Reliance classification** — drives the workpaper's reliability assessment. Vendor-supplied and management-prepared evidence carry separate completeness-and-accuracy checks at fieldwork.
- **Sensitivity** — set honestly at request time. NPI, PHI, PCI, SAR-adjacent content, customer narratives carry confidential or restricted, not the internal default. Drives downstream handling and routing.
- **Status** — operational. Updated through fieldwork. Closed when received in usable form or formally not-applicable.
- **Received date / Received evidence ID** — filled on receipt; the evidence ID is the bridge into the workpaper's evidence-inspected table.
- **Re-ask count** — high counts surface fielding problems and inform the post-cycle improvement read.

## Worksheet 4 — Not applicable

Items intentionally not requested with rationale. Avoids re-ask in the next cycle and documents the boundary.

| Description | Rationale | Covered by test ID |
|---|---|---|
| | [out of period; separate test; separate population stratum; separate cycle; restricted access] | [test ID where this item is covered, when it sits in another cycle's scope] |

## Worksheet 5 — Limitations and reliance posture

- Period coverage: [the request list addresses only the period named above].
- Reliance posture: [vendor evidence carries reliance test notes per row; management-prepared evidence carries completeness-and-accuracy checks; reliance on prior-period evidence is named with the prior request-list ID and rationale].
- Access constraints: [SAR content access is restricted; PHI access requires HIPAA-trained reviewer; on-chain evidence requires named wallet-address scope].
- Other: [list].

## Worksheet 6 — Downstream consumers

| Consumer skill | Field consumed |
|---|---|
| `workpaper-drafter` | request_id per evidence row in the workpaper's evidence-inspected table |
| `evidence-binder` (in `risk-compliance-core`) | the closed list as the index of what was produced for this cycle |
| `qa-workpaper` | request list reviewed alongside the workpaper for sufficiency |
| `exception-analysis` | requests flagged not-applicable or deferred where rationale informs an exception classification |

## Worksheet 7 — Reviewer questions

- [Question. Names the decision the reviewer is being asked to make before pre-fielding sign-off.]

A question the preparer answers in the request list is not a reviewer question. Cluster questions for the audience that decides them.

## Worksheet 8 — Sign-off

| Role | Name (filled at sign-off; role appears here in the template) | Signature | Date |
|---|---|---|---|
| Preparer | | | |
| Reviewer | | | (precedes fielding date) |

Preparer and reviewer must be different roles. Pre-fielding sign-off is a hard gate; fielding requests before reviewer sign-off is a methodology weakness.

## Worksheet 9 — Source trace

| Claim | Source | Section | Date | URL or file ref |
|---|---|---|---|---|
| | | | | |

Cite `references/source-anchors.md` and the loaded overlays for canonical citations. Use `[verify section]` if the section reference is unknown; do not invent.

---

## Rendering notes

- **Default rendering**: a single workbook, one tab per worksheet above, with the request-rows tab freeze-paned on the header row and the Request ID column.
- **Status colour conditional formatting**: open (yellow), received (green), received-partial (amber), re-asked (red), closed (grey), not-applicable (grey strikethrough), deferred (purple). The `xlsx` skill applies this on render.
- **Sensitivity column conditional formatting**: restricted (red text), confidential (orange text), internal (default), public (grey text).
- **Owner-role pivot**: a separate auto-generated tab pivots requests by owner role for fielding routing.
- **Due-date pivot**: a separate auto-generated tab pivots requests by due date for cadence management.
- **List size scales**: short PBC lists (under 15 requests) often render as a single tab with the cover and summary as a header band; long lists (40+ requests) keep the tab structure for navigability. The `xlsx` skill chooses the layout from the request count.
- **Firm-overlay variants**: where the firm has installed `references/firm-overlay.md` with PBC-template variants, the xlsx skill applies the firm's tab and column conventions; the underlying request-row contract above remains the same.
