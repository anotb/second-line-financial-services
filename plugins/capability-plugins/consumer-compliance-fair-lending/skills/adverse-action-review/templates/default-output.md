# Adverse-action notice review memo

The deliverable is a Word memo. Render via the `docx` skill in the `document-skills` plugin using the named sections below. Section order is fixed; per-decision tables expand to the population reviewed.

Audience: consumer compliance second-line, fair-lending lead, model risk, legal counsel, sponsor first-line for the product. Recommended actions are owner-routed; the memo is a draft for human decision and does not approve, deny, or finalize.

---

## 1. Decision summary

| Field | Value |
|---|---|
| Review ID | |
| Reviewer (role) | |
| Population reviewed | [product, decision type, period, count] |
| Sampling basis | [random / risk-based / focal-cohort + sample size + frame] |
| §1002.2(c) action categories in scope | [denial / counteroffer-not-accepted / terms-less-favorable / incomplete-application / existing-account-action] |
| Source posture | [public-only / public-plus-firm-policy / public-plus-firm-policy-plus-evidence / connector-aware] |
| Engagement scope record | [path or "not formalized — defaults applied"] |
| Sector overlay set loaded | [banking / payments-fintech / capital-markets / insurance] |
| Cross-cutting overlay set loaded | [privacy] |

## 2. Specific reasons cited (per-notice, normalized)

Reasons as they appear on the notice, normalized to a per-decision row with the cited reason text and the §1002.9(a)(2) sample-form reference where used.

| Decision ID | §1002.2(c) action | Reasons cited (verbatim) | Sample-form reference (if any) | Notes |
|---|---|---|---|---|

## 3. Reasons supported by underlying model and data (per-notice)

Per-decision evidence that the cited reasons are the principal reasons actually relied upon. The standard is set by §1002.9(a)(2) and the Staff Commentary; the AI / complex-model framing is set by CFPB Circulars 2022-03 and 2023-03 (loaded from `references/source-anchors.md`).

| Decision ID | Cited reason | Feature reference | Contribution score / evidence | Method (SHAP / LIME / leave-one-out / monotonic / firm-named) | Supported (yes / no / indeterminate) | Gap notes |
|---|---|---|---|---|---|---|

Indeterminate rows carry `[evidence needed]` and a named owner for the evidence ask. A row marked `no` is a substantive Circular 2023-03 finding; the recommended action follows in section 8.

## 4. Reg B §1002.9 timing compliance (per-notice)

| Decision ID | Application completed at | Notice sent at | Days elapsed | §1002.9(a)(1) clock applied | Timing compliant (yes / no / unverifiable) | Evidence path |
|---|---|---|---|---|---|---|

The clock-applied column records which §1002.9 subsection set the deadline (30-day on completed application; 30-day on counteroffer not accepted; 30-day on existing-account action; 90-day under §1002.9(c) for incomplete applications).

## 5. Reg B §1002.9 content compliance (per-notice)

| Decision ID | ECOA notice text complete | Specificity test passed | FCRA overlay applicable | FCRA overlay content complete | Combined notice version | Content compliant (yes / no / partial) | Defects |
|---|---|---|---|---|---|---|---|

The specificity test references the Staff Commentary (Comment 9(b)(2)-3 and -4) and the CFPB Circulars on AI / complex models. FCRA overlay applicability is determined per decision by whether a consumer report or score was used.

## 6. Disparate-impact red flags

Decline-rate disparity, reason-mix disparity, and BISG-flagged geography signals at the population level. BISG is a probabilistic proxy; the panel produces signals, not findings. Findings follow formal fair-lending testing — route to `fair-lending-test-plan` for finding-grade work.

| Cohort / segment | Decline rate | Comparator decline rate | Disparity (pp / multiplier) | Statistical posture (descriptive / threshold / regression) | BISG caveat applied | Red flag (yes / no) | Cross-reference |
|---|---|---|---|---|---|---|---|

Reason-mix disparity panel:

| Cited reason | Cohort share | Comparator share | Disparity | Notes |
|---|---|---|---|---|

Geography panel (where dwelling-secured population in scope):

| MSA / census-tract grouping | Decline rate | Peer / comparator rate | CRA assessment-area overlap | Red flag (yes / no) |
|---|---|---|---|---|

## 7. AI / complex-model specific findings

Findings that turn on the CFPB Circular 2022-03 (specificity is not foreclosed by model complexity) and CFPB Circular 2023-03 (sample-form reasons must reflect the principal reasons actually relied upon) anchors. Joint Statement (April 2023) on enforcement against algorithmic discrimination loaded from `references/source-anchors.md`.

| Finding ID | Model in scope (ID, version) | Decision use | Defect type (no-explainability / impossible-mapping / sample-form-substitution / generic-reason-only / model-reason-mismatch) | Decisions affected | Supporting evidence | Recommended action ref |
|---|---|---|---|---|---|---|

## 8. Recommended action

Each recommendation names: the action, the named owner role (not individual), the named first-line control, the due date proposed, and the escalation path. The memo is a draft for human decision; recommendations route to the named owner for sign-off.

| Action ID | Recommendation | Owner role | Named control | Due date proposed | Escalation path | Cross-routing (CRA officer / privacy team / model risk / fair-lending committee / counsel) |
|---|---|---|---|---|---|---|

## 9. Open legal / compliance questions for counsel

Unresolved questions surfaced by the review. Privilege posture per the engagement; counsel reviews before any external use of the artifact.

- [Question 1, with the §1002.9 / CFPB Circular reference where applicable.]
- [Question 2.]

## 10. Source trace and confidence

Every material claim above traces to a source. Source-cited facts, management assertions, public-source obligations, generated inferences, and open legal or compliance questions carry separate confidence labels.

| Claim ID | Claim | Source (path or external citation) | Evidence type | Confidence (high / medium / low / unknown) |
|---|---|---|---|---|

The memo is a draft. The fair-lending lead, model risk lead, and counsel sign before any notice re-issuance, model release, or external communication.
