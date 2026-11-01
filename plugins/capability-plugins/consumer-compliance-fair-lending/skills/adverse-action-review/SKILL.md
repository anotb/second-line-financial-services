---
name: adverse-action-review
description: |
  Reviews a population of adverse-action notices and the underlying credit decisions field-by-field — timing, content, specificity of cited reasons, traceability of those reasons back to the model and data, FCRA risk-score disclosure overlay, and disparate-impact red flags. Produces a Word memo for the consumer compliance second-line, the fair-lending lead, model risk, and counsel; flags non-compliant notices and AI / complex-model accuracy gaps; recommends action without finalizing any customer-facing change.

  Best for:
  - Consumer compliance second-line sampling adverse-action notices on a credit product, testing the population against the notification rule's timing and content obligations.
  - Model risk or fair-lending review of a credit decision model (including AI / ML scorecards) where adverse-action reasons are produced from feature contributions and the reviewer needs to test that the cited reasons are the principal reasons supported by the model.
  - Triage of consent-order remediation or supervisory finding around adverse-action notice deficiencies, where the population needs to be re-tested against the operative rule and the firm's remediation plan.

  Not the right tool when:
  - The question is the underwriting model's predictive performance or stability rather than its adverse-action reason generation (use `ai-governance-model-risk/validation-plan`).
  - The question is the pricing tier or ability-to-repay calculation rather than the notice content (use `compliance-testing` for product-level review).
  - The reviewer needs a final fair-lending determination or a credit decision; this skill surfaces red flags and recommends action for human decision, it does not approve, deny, or finalize.
argument-hint: "[notice population reference, decision data, model output, period, or scope statement]"
---

# Adverse-action review

The artifact is a Word memo that walks an adverse-action notice population field-by-field. Per-notice timing. Per-notice content. Per-notice cited reasons against the model output and feature contributions. FCRA risk-score disclosure overlay where applicable. Population-level disparate-impact red flags with the proxy caveats applied. AI / complex-model findings called out separately. Recommended action is owner-routed; the memo is a draft for human decision and does not approve, deny, finalize, or take any customer-facing action.

The doctrinal frame for this work is the regulatory text, not the bureau's interpretive layer. Reg B §1002.9 sets the timing and the specific-reasons obligation; Comment 9(b)(2)-3 of the Official Staff Commentary requires the cited reasons to "relate to and accurately describe the factors actually considered or scored by a creditor"; FCRA §1681m and Reg V §1022.74 set the risk-score disclosure overlay. The CFPB withdrew Circulars 2022-03 and 2023-03 on May 12, 2025 and the BNPL Interpretive Rule was nullified by Pub. L. 119-11; those shifts do not change what the regulation requires of a creditor. The model-supported-reasons review continues to test against §1002.9(a)(2) and the Staff Commentary on its own terms; a creditor that cannot identify the principal reasons relied on still cannot meet the regulation on its face. The withdrawn items are preserved in `references/source-anchors.md` as historical context.

The skill serves both lenses. A 1.5-line consumer compliance officer inside the business uses it to consolidate a quarter's notice review on a focal product. A 2-line independent reviewer or fair-lending lead uses the same skill to challenge the first-line population review and to surface the seams the first line missed (AI / complex-model accuracy, FCRA overlay, the §1002.2(c) action categories outside the denial subset). The artifact's named-section structure is the seam between the two reviews.

## Ask first

Most of what the review needs is on the table by the time someone reaches for this skill. A few things to settle before drafting; defaults are fine when an answer is missing, and the artifact flags the default.

- What population is in scope. Product, decision type, period, count, sampling basis, and which of the action categories under the notification rule's adverse-action definition are covered. A review covering only outright denials misses counteroffers not accepted, terms-less-favorable actions, and existing-account adverse changes that are also adverse action.
- Whether any AI / ML or complex scoring model drives the in-scope decisions. The answer flips on the model-supported-reasons section, brings in the AI / complex-model regulatory framing, and adds the per-decision feature-contribution evidence ask.
- What evidence the review actually has access to. Notice text, decision system extract, model output, feature contributions, FCRA disclosure content, comparator data — set source posture at what the engagement has, not at what it would prefer.
- Who the audience is and which decision forums apply. Consumer compliance committee, fair-lending committee, model risk committee, CRA officer (where dwelling-secured and assessment-area overlap), privacy team, counsel. Audience drives audit-trail depth and the cross-routing on recommended actions.

When `scope` is supplied, the skill consumes it for institution, persona, source posture, sector overlay set, and cross-cutting overlay set. When it is not, the skill asks the questions above and defaults source posture to public-only with the absence flagged in the memo's decision summary.

## How the memo gets built

The memo has the same named-section spine across product types and triggers. The skill walks the sections in order because per-section evidence builds — the population panel sets the action-category split, the timing panel uses the action category to pick the right clock, the content panel uses the timing posture to test the incomplete-application carve-out, the model-supported-reasons panel uses the population panel to scope the explainability ask, and the disparate-impact and AI-finding panels use the per-decision findings to scope the population-level conclusions.

### 1. Decision summary

The opening panel records review ID, reviewer role, population reviewed (product, decision type, period, count), sampling basis, the action categories in scope under the notification rule's adverse-action definition, source posture, scope record path, and the sector and cross-cutting overlays loaded.

A review that does not name the action categories in scope cannot test the full population; the panel forces the scope on the face of the artifact. Where the scope is "denials only", the artifact says so explicitly with the rationale, and the recommended-action section flags the unreviewed populations.

### 2. Specific reasons cited

Per-notice row of the cited reason text as it appears, normalized, with the sample-form reference where used. This is the input to the model-supported-reasons test; the cited text is the artifact's evidence of what the creditor told the applicant.

### 3. Reasons supported by underlying model and data

Per-decision evidence that the cited reasons are the principal reasons actually relied upon. Each row carries the feature reference, the contribution score, the explainability method used (the bank's named method, vendor-supplied where applicable), and a yes / no / indeterminate verdict per cited reason. Indeterminate rows carry `[evidence needed]` and a named owner for the evidence ask.

The named regulatory anchor for this section is the notification rule's specificity standard and the AI / complex-model framing that turns the standard against creditors who cannot identify the principal reasons relied on; both are loaded from `references/source-anchors.md`. A row marked `no` is a substantive content finding that surfaces in section 7.

### 4. Reg B §1002.9 timing compliance

Per-notice rows recording application-completed-at, notice-sent-at, days elapsed, the §1002.9 subsection that set the deadline, and a yes / no / unverifiable verdict. The clock-applied column is where most defects hide:

- the §1002.9(c) incomplete-application clock applied where the application was actually complete (and the incompleteness notice was never sent),
- the counteroffer clock applied where there was no counteroffer (a soft-decline pattern routed into the counteroffer track without the counteroffer ever offered to the applicant),
- the existing-account clock applied where the action category was actually denial.

### 5. Reg B §1002.9 content compliance

Per-notice rows recording ECOA-notice-text-completeness, the specificity test against the cited reasons, FCRA-overlay applicability, FCRA-overlay content completeness where applicable, the combined-notice version in force at decision time, and a yes / no / partial verdict.

The Staff Commentary on specificity sets the reference standard; the AI / complex-model framing layers on top where any in-scope decision uses a complex model. The combined Reg B / Reg V notice tests against both regimes separately — a notice can pass one and fail the other.

### 6. Disparate-impact red flags

Population-level decline-rate disparity, reason-mix disparity, and BISG-flagged geography signals. BISG is a probabilistic proxy and the panel produces signals, not findings. Every BISG-derived statistic carries the BISG caveat, and finding-grade work routes to `fair-lending-test-plan` rather than producing a disparate-impact conclusion here.

For dwelling-secured products, HMDA self-reported demographics are stronger evidence than BISG and are used directly; for non-dwelling consumer credit, BISG is the working proxy and the limits are stated. The geography panel records CRA assessment-area overlap where relevant; a redlining red flag inside the assessment area routes to the CRA officer alongside the fair-lending committee.

### 7. AI / complex-model specific findings

Findings that turn on the AI / complex-model regulatory framing — the specificity expectation that survives model complexity, the accuracy expectation against sample-form reasons, and the agencies' joint statement that algorithmic discrimination is enforceable under existing authorities. Each finding cites the operative regulatory anchor by file path.

The defect taxonomy in this section is empirical:

- *no-explainability*: creditor cannot produce per-decision feature contributions; the model is treated as a black box.
- *impossible-mapping*: cited reason cannot be true for the product (e.g., collateral cited on unsecured personal loan).
- *sample-form-substitution*: closest sample-form reason cited where the principal reason actually relied on is different.
- *generic-reason-only*: the Staff Commentary specificity standard fails on the face (e.g., "you did not meet our credit standards").
- *model-reason-mismatch*: the cited reason ranks low in the per-decision feature contributions.

### 8. Recommended action

Each recommendation names the action, the owner role (not individual), the named first-line control the recommendation modifies or relies on, the proposed due date, the escalation path, and the cross-routing (CRA officer, privacy team, model risk committee, fair-lending committee, counsel). The memo is a draft; the named owner accepts, pushes back, or rebids the proposed due date. The skill stops at draft and does not direct customer-facing action.

### 9. Open legal / compliance questions

Unresolved questions for counsel — re-issuance scope and language, customer-communication posture, regulator-engagement timing, privilege posture on the artifact itself. Counsel reviews before any external use of the memo.

### 10. Source trace and confidence

Every material claim cites a source from `references/source-anchors.md` (or the loaded overlay) by file path; vendor and firm-internal evidence carry separate confidence labels and are not collapsed into one line. Source-cited facts, management assertions, public-source obligations, generated inferences, and open legal or compliance questions stay distinguishable so the artifact shows the seams.

### Quality bar and adaptation

Quality bar (inline above where they apply, restated once): cite a source for every material claim and mark unsupported items `[evidence needed]`; do not fabricate regulatory facts; no named institutions in narrative outside public defendants in finalized enforcement actions; the memo stops at draft and the named owners sign before any notice re-issuance, model release, or external communication.

Adaptation: audience and depth flex. A working-group memo reads short; a fair-lending committee memo reads structured; a counsel-direction memo reads denser; a regulator-response file reads formal. Sector and cross-cutting overlays load from the scope. Banking is the heaviest overlay on this skill (depository product perimeter, FCRA risk-score disclosure, model-risk fabric, CRA assessment-area overlap, sponsor-bank arrangements). Payments-fintech adds the sponsor-bank vs. fintech-of-record allocation, the BNPL adverse-action posture, and vendor-supplied decisioning. Capital-markets narrows the population to the consumer-purpose subset and excludes margin calls and forced liquidations from §1002.9 scope. Insurance flags the scope boundary at the state-DOI / NAIC perimeter and routes insurance-underwriting questions out.

## Pointers

- `references/source-anchors.md` — citations and excerpts for the named anchors (ECOA / Reg B §1002.9, Staff Commentary, CFPB Circulars 2022-03 and 2023-03, the April 2023 Joint Statement, FHA, FCRA / Reg V §1022.74, third-party guidance, BNPL interpretive rule, SR 11-7, GLBA Safeguards Rule, NAIC Model #880).
- `references/sector-overlays/banking.md` (heaviest overlay), `payments-fintech.md`, `capital-markets.md` (narrow), `insurance.md` (scope boundary) — loaded per `scope.sector_overlay_set`.
- `references/cross-cutting/privacy.md` — GLBA Safeguards Rule on the review's own data handling, state-privacy interaction, BISG-derived attribute treatment; loaded when `scope.cross_cutting_set` includes `privacy`.
- `references/cross-cutting/conduct.md` — UDAAP, FTC §5, April 2023 Joint Statement, CFPB Supervisory Highlights, FCA SMCR / Consumer Duty, NAIC Models #880 / #900 frame on the AAN population: comprehensibility read on cited reasons, sample-form-substitution and reason-suppression at population scale, disclosure-consistency against marketing and front-line representations, conduct-event-candidate flagging on AI / complex-model defects, conduct-framework-cohort signals alongside protected-class disparate-impact; loaded when `scope.cross_cutting_set` includes `conduct`.
- `references/firm-overlay.md` — firm-installed notice-template version, reason-code dictionary, named first-line controls, MRM model-risk inventory paths, and named owners; consumed when present.
- `templates/default-output.md` — content spec for the memo (named sections, per-decision tables, recommended-action routing).
- `examples/xgboost-personal-loan-decline-sample.md`, `examples/mortgage-decline-redlining-flag.md` — public-source-derived worked examples.
- `TROUBLESHOOTING.md` — recurring defects in notice-population scope, timing, content, model-supported reasons, and disparate-impact panels.

## Output

The deliverable is a Word memo. Render via the `docx` skill in the `document-skills` plugin using the named sections from `templates/default-output.md`. The memo is a draft for human decision; the consumer compliance lead, fair-lending lead, model risk lead (where AI / complex models are in scope), CRA officer (where redlining red flags inside the assessment area), and counsel sign before any notice re-issuance, model release, or customer-facing action. This skill does not approve loans, deny adverse-action notices, finalize fair-lending determinations, or take any customer-facing action; it surfaces red flags and recommends action for human decision by qualified compliance, fair-lending, model risk, and legal reviewers.

## Human review and AI disclosure

Open the deliverable with this line, and remove it only after the review below: `AI-assisted draft. Requires review by a qualified person before use.`

A qualified person with authority to change the output reviews it before it is delivered or relied on, and stays accountable for it. Where the output supports advice to an individual or a decision about an individual (credit, insurance underwriting, pricing or claims, employment, legal rights, or similar), that individual must be told AI was used to produce it. This skill does not make final decisions, file with a regulator, notify customers, execute transactions, or move money or other financial assets.
