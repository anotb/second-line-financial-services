---
name: section1071-readiness
description: "Assess Section 1071 small-business lending data readiness under the CFPB's revised rule."
argument-hint: "[CFI determination data, product list, LOS / data extracts, vendor attestations, prior readiness pack, scope statement]"
---

# Section 1071 readiness

Section 1071 added a small-business analogue of HMDA: covered financial institutions must collect, compile, and report data on credit applications from small businesses, with applicant-demographic data captured under a strict firewall that limits underwriting access. The CFPB issued a revised final rule on May 1, 2026 (codified at 12 CFR 1002.101–1002.114) that supersedes the 2023 rule's tier-based compliance schedule and most of the *Texas Bankers Association v. CFPB* litigation posture. Under the revised rule: the covered-financial-institution threshold is 1,000 covered originations to small businesses in each of the two preceding calendar years (up from the 2023 rule's tiered thresholds), the rule is effective June 30, 2026, and the compliance date is January 1, 2028 for all CFIs. There are no longer three tiers with three different effective dates; there is one threshold and one compliance date.

This skill drafts the firm's readiness assessment under the revised rule. It produces two artifacts: a readiness matrix (one row per 12 CFR 1002.107 data point, with system-of-record, capture method, readiness, gap, owner, due date) and a narrative gap memo for the named accountable executive. The matrix is the structured artifact downstream remediation tracking and audit reads from; the memo is what the executive signs off before the firm commits to the January 1, 2028 go-live.

The skill stops at draft. It does not file Section 1071 data, sign off readiness, finalize covered-institution determinations, or take any operational action. The covered financial institution decides; this skill structures the decision.

## When to use

Drafts a Section 1071 small-business lending data readiness assessment under the CFPB's revised final rule (May 1, 2026; effective June 30, 2026; compliance date January 1, 2028). Covers covered-financial-institution determination against the 1,000-covered-transactions threshold, covered-application and covered-credit-transaction scoping, the 12 CFR 1002.107 data-point inventory, applicant-demographic data-collection mechanics, the 12 CFR 1002.108 firewall design, recordkeeping under 12 CFR 1002.110, and reporting-and-filing readiness against the CFPB Filing Instructions Guide. Produces a readiness matrix per data point and a narrative gap memo for the named accountable executive.

Best for:
- Pre-compliance-date readiness check for a covered financial institution against the January 1, 2028 compliance date (now a single compliance date for all CFIs at or above the 1,000-transaction threshold; the prior tier-based schedule is superseded).
- Threshold-determination work for a firm sitting at or near the 1,000 covered-credit-transactions floor in each of the two preceding calendar years.
- Annual operating-state readiness refresh post-go-live, against the firm's first or subsequent submission cycle.
- Vendor or loan-origination-system readiness assessment where 1071 data capture is vendor-supplied (the firm remains the covered financial institution; the vendor is the data-collection agent).

Not the right tool when:
- The question is HMDA / Reg C readiness (different rule, different population — refer the reviewer to a HMDA-specific routine).
- The question is fair-lending testing on the originated 1071 portfolio (use `fair-lending-test-plan`; the 1071 dataset feeds fair-lending testing once it exists).
- The question is the adverse-action notice for a small-business application (use `adverse-action-review`; Reg B 1002.9 applies).
- The question is the firm's overall consumer compliance management system (use `risk-compliance-core` or `compliance-testing`).

## Ask first

Before drafting, settle six things. The matrix is identifier-driven against the 1002.107 list, and getting these wrong upstream costs more than asking once.

- **Covered-financial-institution determination**. Counts of covered originations to small businesses for each of the two preceding calendar years, against the revised 1,000-transaction threshold under 12 CFR 1002.105. The methodology used to count (covered-transaction definition under 1002.106 applied per product) and the source-of-record for the count. If the firm has not done the count, the readiness work begins here; if the firm sits below 1,000 in either of the two preceding calendar years and is not a CFI, the skill says so and stops. There is no tier classification under the revised rule; CFI / not-CFI is the binary.
- **Distance from the threshold**. A firm at 700 originations is in a different posture from a firm at 9,500. The memo names the headroom or the proximity, because near-threshold firms need watch-list monitoring and may flip in or out year-over-year. Far-above-threshold firms are sized for compliance regardless.
- **Product list and per-product covered-credit-transaction mapping**. The firm's product taxonomy (term loans, lines of credit, business credit cards, SBA 7(a), SBA 504, merchant cash advance, sales-based financing, factoring, equipment finance, trade finance, etc.) mapped to the 1002.106 covered-credit-transaction definition with `in / out / edge` classification and rule-cited rationale per product. Skipping this and assuming the procurement product list is the scope is the most common scoping error.
- **System-of-record per data point**. For each 1002.107 data point, the system the data lives in or will live in (LOS, CRM, deposit system, manual capture, vendor-supplied). Multiple systems per data point is normal; pick the canonical source and record the others as feeders.
- **Vendor / LOS posture**. Where the LOS is vendor-supplied, the vendor's readiness is not the firm's readiness. The firm is the covered financial institution. Capture each vendor's role, attestations, change-control identifier for any 1071-driven change, and the contractual responsibility allocation. Sponsor-bank arrangements (a fintech operating under a sponsor bank) require separate treatment: the sponsor bank is the covered financial institution; the fintech is the data-collection agent.
- **Source posture**. Public-only (the rule text and FIG only), public-plus-firm-policy (firm policies, vendor attestations, control documentation), public-plus-firm-policy-plus-evidence (LOS extracts, data dictionaries, system reports), or connector-aware (live LOS access). Set posture to what the engagement actually has, not what it would prefer; the matrix's `readiness` enum reads honestly only when the source posture supports it.

When the scope record is supplied, the skill consumes it for institution type, sector overlay (banking or payments-fintech), persona, source posture, and primary regulators. When it is not supplied, ask the questions above and default to public posture if the practitioner declines.

## How the assessment gets done

The assessment has the same spine across firm types. A senior practitioner walks it in roughly the order the inputs land, not in lockstep. The matrix sorts itself; the memo reads in the order below.

### Covered-financial-institution determination

Open with the 12 CFR 1002.105 threshold count under the revised rule: 1,000 covered originations to small businesses in each of the two preceding calendar years. Carry the year T-1 and year T-2 counts, the methodology (covered-transaction definition per product), and the resulting CFI / not-CFI determination. The compliance date is January 1, 2028 for all CFIs (no tiers); the rule was effective June 30, 2026. Where the firm sits at or near the 1,000-transaction line in either year, surface the sensitivity in a reviewer question and recommend year-over-year monitoring; a near-threshold firm may flip in or out and the readiness posture has to be set up to handle that.

### Covered-application and covered-credit-transaction scoping

Per-product mapping to 12 CFR 1002.104 (covered application) and 12 CFR 1002.106 (covered credit transaction). Each product gets an `in / out / edge` classification with the rule-cited rationale. Edge cases get named open questions for legal: BNPL-for-business, factoring without recourse, trade finance instruments, intra-group lending, agricultural credit at the boundary of small-business definition, deposit-account-secured lending. The firm's procurement taxonomy will not align one-for-one with the rule's covered-transaction definition; the mapping decisions are part of the source trace.

### Data-point readiness against 12 CFR 1002.107

The matrix is the artifact. One row per data point in 12 CFR 1002.107. The 1002.107 list (non-exhaustive — verify completeness against the current rule text) covers: unique identifier, application date, application method, application recipient, credit type (product type, guarantee, loan term), credit purpose, amount applied for, amount approved or originated, action taken, action taken date, denial reasons, pricing information (interest rate; total origination charges; broker fees; initial annual charges; additional cost for merchant cash advance and other sales-based financing; prepayment penalty), census tract (principal address), gross annual revenue, NAICS code, number of workers, time in business, number of principal owners, minority-owned business status, women-owned business status, LGBTQI+-owned business status, and ethnicity / race / sex of principal owners (with firewall-driven access discipline per 1002.108). Each row carries: data point, rule reference (e.g., `1002.107(a)(13)`), system of record, capture method (`applicant_provided` / `firm_inferred` / `vendor_supplied` / `manual_entry` / `not_yet_captured`), readiness (`ready` / `partial` / `gap` / `unverifiable`), gap description, owner, due date.

A few capture-method patterns recur and deserve named treatment. Pricing fields for sales-based financing computed post-funding from settlement data sit as `firm_inferred` rather than `applicant_provided`, with downstream amendment-reporting risk; surface this. Census tract populated from the borrower's mailing address rather than the principal address is a frequent error; flag explicitly. NAICS captured only at SBA-line origination and not at general commercial lending leaves a gap across the rest of the in-scope portfolio. Demographic-data fields populated as `null` for applicant refusal rather than the rule's required refusal value miscode the refusal and break the FIG validation downstream.

### Applicant-demographic data-collection mechanics

Demographic data collection is half the rule; isolating it from underwriting access is the other half. Capture the collection point in the application flow, the script and form text used, the principal-owner identification logic, the refusal-handling code path, and the data-flow diagram from collection to the 1071 dataset. Capture is not enough on its own: where collection happens but the refusal code is wrong, where the principal-owner identification logic captures the wrong individuals, or where the script is missing the rule's required disclosures, the readiness state is not `ready` regardless of whether the field is populated.

### Firewall and data-isolation review per 12 CFR 1002.108

The firewall is a control review, not a UI review. Capture: the system or systems hosting the demographic data, the role-based access controls, the named exceptions (the rule permits specific exceptions where the underwriter cannot avoid access; document each), the firewall-trained personnel design (who has been trained, what training, what cadence), the audit-log posture for access events, and the attestation map per role. The most material 1002.108 gap is usually not in the LOS itself but in customer-360 or relationship-management views that aggregate self-reported demographics from the deposit side and expose them to underwriting; surface this explicitly when it is in the firm's environment.

### Recordkeeping under 12 CFR 1002.110

Three-year retention from the date of submission. Capture: where the records sit, the disposition policy, the link to the firm's broader records-retention schedule, and the recovery posture (can the firm produce the records on regulator request within an examination timeline). Record in the matrix.

### Reporting and filing readiness

FIG conformance. Capture: the FIG edition the firm is building against (mark `[verify current edition]`), file-format readiness, the validation-engine in use (CFPB-provided or vendor-built or in-house), the test-submission plan with named test cycles, and the named owner of the submission. The submission itself is a regulated filing through the CFPB-specified channel; this skill does not file.

### Vendor and LOS readiness

One row per material vendor. Capture: vendor name, role (LOS / demographic-collection-form provider / pricing-data computation / submission utility), attestation status (signed / requested / not yet requested), change-control identifier for the 1071 build, contractual responsibility allocation, and SLA for the data-flow. Where the LOS vendor's product roadmap does not align with the firm's compliance-date go-live, flag in the gap list with severity `high` or `blocking`.

### Fair-lending testing readiness on 1071 data

The 1071 dataset becomes the canonical small-business fair-lending dataset once it exists. Cross-reference `fair-lending-test-plan` for the testing design; this skill's responsibility is to confirm the dataset is fit for that downstream use. Capture: completeness of the demographic-data fields needed for testing, the firewall's compatibility with fair-lending team access (the testing team is one of the rule's permitted exceptions, but access has to be designed in), and the data-pipeline from production 1071 capture to the fair-lending analytics environment.

### Bona-fide-error and safe-harbor approach (12 CFR 1002.112)

Document the firm's bona-fide-error policy before go-live, not after the first submission. Capture: the policy reference, the procedure for amending submitted data, the named owner, and the link to the firm's broader regulatory-reporting-error policy (if one exists). A firm that goes live without a documented bona-fide-error approach is exposed; surface it.

### Gap list, open questions, source trace

Each gap rolls up to a separate gap-list row with severity (`blocking` / `high` / `medium` / `low`), owner, and due date. Open questions for legal and compliance are itemised with the function the question goes to. The source trace cites `references/source-anchors.md` by path for every material claim; uncertain dates and editions are marked `[verify current effectiveness and tier dates]` or `[verify current edition]`.

### Sector and cross-cutting overlay loading

When the scope names a sector, load the matching `references/sector-overlays.md#<sector>`: `references/sector-overlays.md#banking` for depository institutions (the heaviest overlay), `references/sector-overlays.md#payments-fintech` for fintech small-business lenders and sponsor-bank arrangements. `references/sector-overlays.md#capital-markets` and `references/sector-overlays.md#insurance` carry out-of-scope flags so reviewers do not over-extend. Cross-cutting overlays: `privacy.md` for the GLBA Safeguards posture on customer demographic data and the CFPB modified-data publication and re-identification considerations; `conduct.md` for the lender-conduct dimension where 1071 readiness gaps surface conduct themes (data-collection misrepresentation to applicants, firewall failures, vendor mismanagement). Load only the overlays the scope names.

## Quality bar

Holds across every assessment:

- **CFI determination against the 1,000-transaction threshold**. CFI / not-CFI is the binary; the compliance date is January 1, 2028. Date and threshold carried as sourced citations into `references/source-anchors.md`.
- **Per-product covered-transaction mapping with rule citation**. Not the procurement taxonomy.
- **One matrix row per 12 CFR 1002.107 data point**. The list is the contract; partial matrices are not assessments.
- **Firewall as a control review, not a UI question**. 1002.108 is half the rule.
- **Vendor-readiness rows with attestation and change-control identifier**. The vendor is the data-collection agent; the firm is the CFI.
- **Bona-fide-error approach documented before go-live**.
- **Source trace**. Every material claim cites `references/source-anchors.md` by path. Unsupported items go to the engagement issue log, not silently into the memo.
- **The skill does not file**. The matrix and memo carry reviewer questions and named decision checkpoints. The named accountable executive signs off.

## Adaptation

- **Assessment depth scales to source posture and review type**. A pre-compliance-date readiness check at public-plus-firm-policy posture reads narrative-heavy with `unverifiable` rows where evidence has not landed yet; an annual refresh at connector-aware posture reads matrix-heavy with the year-on-year delta as the headline.
- **Audience drives shape**. A pack for the compliance programme lead reads operational. A pack for the named accountable executive leads with the residual gap posture and the sign-off question. A pack for the regulator dialogue reads as a justification of the firm's own readiness posture.
- **Sector overlay loading follows the scope**. A fintech operating under a sponsor bank loads both `banking.md` (sponsor bank's view) and `payments-fintech.md` (fintech's view).
- **Firm-specific policy, taxonomy, named owners, internal-product-to-1002.106 mapping table** sit in plugin-level `references/firm-overlay.md` if installed; consumed when present, never in the memo directly.

## Output

Two artifacts. The readiness matrix is an Excel workbook produced via the `xlsx` skill (in the `document-skills` plugin), with a sheet per ITS-equivalent area: cover, scope and CFI determination, product mapping, data-point matrix (one row per 1002.107 data point), firewall design, vendor readiness, gap list, source trace. The narrative gap memo is a Word document produced via the `docx` skill (in the `document-skills` plugin), using the named sections from `templates/default-output.md`. The memo references the matrix by file name and by sheet; the matrix is the system-of-record for the per-data-point readiness state, the memo is what the named accountable executive reads.

A structured-output schema (`schemas/section1071-readiness.schema.json`) sits alongside the artifacts so a remediation tracker, GRC platform, or audit-workpaper system can ingest the per-data-point readiness state, the gap list, and the firewall and vendor readiness records without re-keying. The schema is additive only.

Downstream consumers: `fair-lending-test-plan` reads the data-point matrix to confirm the 1071 dataset is fit for fair-lending testing; the firm's regulatory-reporting pipeline consumes the FIG-readiness section once go-live approaches; the firm's audit function reads the matrix, memo, and source trace for audit support.

## Pointers

`references/sector-overlays.md` and `references/cross-cutting.md` hold one section per sector or topic, and `examples.md` one per example. Find the heading and read only that section.

- `references/source-anchors.md` — citations for the May 1, 2026 revised final rule, the 1,000-transaction threshold, the June 30, 2026 effective date, the January 1, 2028 compliance date, the 1002.107 data points, the FIG, and the superseded litigation history.
- `references/sector-overlays.md#banking` — depository-institution overlay (heaviest); SBA 7(a) / 504 inclusion, business credit cards, trade finance, CFI tier-classification mechanics for banks.
- `references/sector-overlays.md#payments-fintech` — fintech small-business lending; merchant cash advance and sales-based financing; sponsor-bank attribution; vendor LOS readiness; BNPL-for-business edge cases.
- `references/sector-overlays.md#capital-markets` — out-of-scope flag with the boundary explicitly named so reviewers do not over-extend.
- `references/sector-overlays.md#insurance` — out-of-scope flag with the boundary explicitly named.
- `references/cross-cutting.md#privacy` — GLBA Safeguards (16 CFR Part 314) on customer demographic data; CFPB modified-data publication and re-identification considerations; state-privacy applicability `[verify state-specific scope]`.
- `references/cross-cutting.md#conduct` — lender-conduct dimension; how 1071 readiness gaps (data-collection misrepresentation, firewall failures, vendor mismanagement) surface conduct themes for the conduct committee and the broader risk-and-conduct posture.
- `templates/default-output.md` — content spec for the narrative gap memo (named sections, fields).
- `schemas/section1071-readiness.schema.json` — structured-output contract for the readiness matrix and gap list (downstream remediation-tracker consumption).
- `examples.md#community-bank-pre-go-live`, `examples.md#fintech-mca-sponsor-bank` — anonymised public-source-derived scenarios.
- `examples.md#troubleshooting` — recurring defects in §1071 readiness work.

Plugin-level shared references (`references/source-map.md`, `references/policy-control-library.md`, `references/review-gates.md`) sit at the plugin root and are consulted alongside the skill-level files.

## Human review and AI disclosure

Open the deliverable with this line, and remove it only after the review below: `AI-assisted draft. Requires review by a qualified person before use.`

A qualified person with authority to change the output reviews it before it is delivered or relied on, and stays accountable for it. Where the output supports advice to an individual or a decision about an individual (credit, insurance underwriting, pricing or claims, employment, legal rights, or similar), that individual must be told AI was used to produce it. This skill does not make final decisions, file with a regulator, notify customers, execute transactions, or move money or other financial assets.
