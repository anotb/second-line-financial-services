# Examples and troubleshooting

One section per worked example, then troubleshooting. Read only what you need.

## health-small-group-refile-vendor-ml

### Example: small-group health refile with a new geographic-area factor and a vendor-supplied ML risk-adjustment input

**Public-source-derived. No named institutions.**

#### Scenario

A US health insurer is refiling small-group rates in three states. The refile introduces a new geographic-area factor (a redrawn rating-area structure) and a vendor-supplied ML risk-adjustment input. ACA pricing rules apply.

#### Source posture

Public-plus-firm-policy-plus-evidence.

#### What the artifact carries

##### Rate filing summary

Three SERFF filings (small-group ACA-regulated). Refile, not new filing. Effective date next plan year.

##### Rating factor map (Excel workbook)

Five rating factors (four are ACA-permitted: family size, geography, age within 3:1, tobacco within 1.5:1; the ML risk-adjustment input is a sub-component of the geographic factor's actuarial methodology, not an additional rating factor). The artifact names this distinction clearly: the ML input feeds the actuarial methodology under the permitted geographic factor; it is not an additional factor.

##### Unfair discrimination analysis

Per-factor under #880 plus a rating-plan-as-a-whole assessment. All factors carry `clear` actuarial-justification status because they are ACA-permitted on the bright-line list. Plan-as-a-whole assessment carries the methodology question (whether the vendor ML input is being applied consistently within the permitted geographic factor).

##### Disparate-impact red flags

State guidance limited in the three states in scope; no CO, NY, or CA presence in this filing. Standard #880 monitoring expectation only.

##### AI / ML governance: AIS Program cross-walk

Vendor ML input pulls third-party-AI-accountability obligations under the NAIC Bulletin December 2023. Six AIS Program elements `in-place`, three `partial`. The carrier-level monitoring against the vendor's input is the key open item.

##### Documentation completeness vs federal model-risk-equivalent

Vendor-supplied validation evidence; carrier-level validation `partial` (similar to the AU example). Cite the **Joint Interagency Revised Guidance on Model Risk Management (OCC Bulletin 2026-13 / FRB SR 26-2 / FDIC FIL-15-2026, April 17, 2026; supersedes SR 11-7)** as analogous.

##### State DOI bulletin alignment

Three states in scope; standard rate-filing checklist. NAIC Model Bulletin adoption status verified per state on the analysis date.

##### ACA-pricing checks

| Check | Status |
|---|---|
| Permitted rating factors only used | `pass` |
| No prohibited rating factors used | `pass` |
| Geographic rating-area structure under 45 CFR §147.102 | `pass` for two states, `[evidence-needed]` for the third (rating-area-vs-zip-code mapping documentation incomplete) |
| Guaranteed renewability under §147.106 | `pass` |

##### Privacy and consumer-disclosure posture

HIPAA applies (small-group health). Vendor BAA chain on file. Minimum-necessary analysis `pass` (the vendor receives only the inputs needed for the risk-adjustment computation).

##### Recommended disposition

`Approve-with-conditions`. Two conditions: (1) complete the rating-area-vs-zip-code mapping documentation for the third state before SERFF submission; (2) close the carrier-level monitoring gap on the vendor ML input within 90 days of effective date.

#### Public sources used

- ACA pricing rules (45 CFR Part 147).
- NAIC Bulletin on the Use of Artificial Intelligence Systems by Insurers (December 2023).
- NAIC Unfair Trade Practices Act, Model #880.
- HIPAA Privacy Rule, 45 CFR Part 164 Subpart E.
- Joint Interagency Revised Guidance on Model Risk Management (OCC Bulletin 2026-13 / FRB SR 26-2 / FDIC FIL-15-2026, April 17, 2026; supersedes SR 11-7) — cited as analogous model-risk expectation language.

## life-au-launch-co-ny

### Example: life carrier launching accelerated underwriting using ECDIS in Colorado and New York

**Public-source-derived. No named institutions.**

#### Scenario

A US life insurer is launching an accelerated-underwriting (AU) program for term-life products. The AU model uses third-party prescription-history data and a vendor-supplied ML-derived risk score. The program is going live in Colorado and New York first, with a planned national rollout. Second-line wants the pricing-governance file before the SERFF submissions and before AU goes live in either state.

#### Source posture

Public-plus-firm-policy-plus-evidence. The carrier has supplied the actuarial memorandum, the model documentation, the vendor SOC 2, the data-source contracts, the consumer-disclosure draft, and the AIS Program draft.

#### What the artifact carries

##### Rate filing summary

Two SERFF filings (CO and NY). New product (term life) with the AU pathway as a manual-underwriting alternative. Effective date 90 days from filing acceptance.

##### Rating factor map (Excel workbook)

Twelve rating factors. Three are ECDIS-derived (a prescription-history-derived flag, a vendor-supplied composite risk score, a public-records-derived flag). State-status columns for CO and NY show three factors with `requires-justification` posture under #880; the composite score has `requires-justification` in CO under SB 21-169 and `requires-justification` in NY under the Circular Letter.

##### Unfair discrimination analysis

Per-factor under #880 plus a rating-plan-as-a-whole assessment. The composite score is the open question: actuarial-justification status is `partial` because the carrier has the vendor's bias-evaluation evidence but not the carrier-level validation against the carrier's own portfolio. The artifact names this as an open item, not a clearance.

##### Disparate-impact red flags

CO regulation: the proxy-variable risk for the public-records-derived flag surfaces (the flag may correlate with race in some geographies). The carrier has a monitoring-metric plan but not yet baseline data. Open item.

NY DFS Circular Letter: consumer-recourse channel is named (a dedicated AU-decline line with a 10-business-day SLA and manual-underwriting-fallback path) but the disclosure timing for adverse-information is `[evidence-needed]` against the Circular Letter's expectation.

##### AI / ML governance: AIS Program cross-walk

Six AIS Program elements `in-place`, two `partial`, one `gap`. The gap is third-party-AI accountability for the vendor: the contractual clauses are present but the monitoring evidence is not yet flowing.

##### Documentation completeness vs federal model-risk-equivalent

Validation evidence is `partial`; the vendor's validation is documented but the carrier's own outcomes-analysis plan is dated within the last 30 days and has no observation period yet. Cite the **Joint Interagency Revised Guidance on Model Risk Management (OCC Bulletin 2026-13 / FRB SR 26-2 / FDIC FIL-15-2026, April 17, 2026; supersedes SR 11-7)** as analogous.

##### State DOI bulletin alignment

CO: SB 21-169 implementing regulation. Most prescriptive on ECDIS provenance and consumer-recourse for life-insurance underwriting.
NY: NY DFS Insurance Circular Letter (January 2024). Disclosure and consumer-recourse expectations.

##### Privacy and consumer-disclosure posture

HIPAA: the prescription-history data flows through a HIPAA business-associate chain; BAA on file. Minimum-necessary analysis is `partial`; the data set includes therapeutic categories that are not all underwriting-relevant. Open item.

ECDIS: consumer-recourse channel named (above); adverse-information-disclosure posture `[evidence-needed]` (above).

##### Recommended disposition

`Remediate-then-re-review`. Three named gaps: (1) carrier-level outcomes analysis on the vendor composite score; (2) baseline monitoring data on the proxy-variable risk; (3) adverse-information-disclosure posture under NY DFS Circular Letter. AU launch held until remediation.

#### Public sources used

- NAIC Bulletin on the Use of Artificial Intelligence Systems by Insurers (December 2023).
- NAIC Unfair Trade Practices Act, Model #880.
- Colorado SB 21-169 implementing regulation.
- NY DFS Insurance Circular Letter on AI and ECDIS in life-insurance underwriting (January 2024).
- HIPAA Privacy Rule, 45 CFR Part 164 Subpart E.
- Joint Interagency Revised Guidance on Model Risk Management (OCC Bulletin 2026-13 / FRB SR 26-2 / FDIC FIL-15-2026, April 17, 2026; supersedes SR 11-7) — cited as analogous model-risk expectation language.

## troubleshooting

### Troubleshooting: life-health-pricing-governance

Recurring defects in the artifact. Each is a real failure mode observed across draft pricing-governance files; each has a fix and a check the second-line reviewer can run before sign-off.

#### The artifact reads as an ECOA / Reg B fair-lending test plan

**Symptom.** The unfair-discrimination section uses ECOA / Reg B vocabulary: protected classes from the federal list, disparate-treatment-vs-disparate-impact framing, ECOA adverse-action analysis.

**Why it's wrong.** Insurance unfair-discrimination is governed by NAIC Model #880 plus state insurance code, not by ECOA / Reg B. The test is actuarial-justification-driven; the permitted-vs-prohibited rating-factor list is state-specific; the protected classes are state-defined.

**Fix.** Rewrite the section in #880 vocabulary. Where state DOI guidance imports a disparate-impact-style monitoring expectation (CO regulation, NY DFS Circular Letter, CA bulletin), name it as an additional layer on top of #880, not as a substitute.

**Check.** Search the section for "ECOA", "Reg B", and "1691"; remove or replace each with the state insurance code citation. Verify the protected-class list per state in scope.

#### The actuarial memorandum is doing the governance work

**Symptom.** The artifact restates the actuarial justification and recommends `approve` on that basis.

**Why it's wrong.** The actuarial memorandum justifies the rates. The pricing-governance file justifies the governance over the actuaries and the model. They are different artifacts addressing different questions.

**Fix.** The artifact references the actuarial memorandum as input but adds the governance analysis: AIS Program cross-walk; documentation completeness against SR 11-7-equivalent expectations; ECDIS provenance; state-DOI-bulletin alignment; privacy and consumer-disclosure posture.

**Check.** The artifact should read coherently if the actuarial memorandum is removed; the governance findings stand on their own.

#### ECDIS provenance is missing or thin

**Symptom.** Rating factors derived from third-party consumer data (prescription history, motor-vehicle records, public records, credit-bureau attributes, location-based attributes, social-determinants-of-health attributes) are listed without source identification, contractual permitted-use posture, or consumer-recourse channel.

**Why it's wrong.** CO regulation and NY DFS Circular Letter are explicit on ECDIS provenance and consumer-recourse. CA bulletin and other state guidance follow.

**Fix.** For each ECDIS-derived factor, run the full ECDIS layer in the rating-factor map (workbook column `ecdis_provider`) and in the privacy section (consumer-recourse channel name, SLA, owner, documentation posture).

**Check.** Filter the rating-factor map for `ecdis_flag = yes` or `ecdis_flag = vendor-derived`. Every row should have non-empty `ecdis_provider`, `phi_flag`, `fcra_applicability`, and a corresponding entry in the consumer-recourse section.

#### AIS Program elements are restated rather than analysed

**Symptom.** The AIS Program cross-walk section is a generic restatement of the NAIC Bulletin December 2023 element list with no element-by-element status, no evidence pointers, and no gap identification.

**Why it's wrong.** The AIS Program cross-walk is the centre of gravity for any change involving AI / ML. State DOIs are increasingly asking for the AIS Program document by name; the artifact should map findings to its elements with evidence pointers.

**Fix.** Run each AIS Program element with status (`in-place` / `partial` / `gap` / `not-applicable`), evidence pointer, gap description, and owner role. Where the carrier has not yet adopted an AIS Program at all, name the gap and tag it to the regulatory-affairs lead.

**Check.** The AIS Program section should have non-empty status and evidence-pointer columns for all nine elements. Generic restatements with empty columns are the failure pattern.

#### SR 11-7 is cited as binding rather than analogous

**Symptom.** The documentation-completeness section cites SR 11-7 / OCC 2026-13 as the operative standard for the insurance carrier.

**Why it's wrong.** SR 11-7 is federal banking guidance. State DOIs cite it as analogous, not directly applicable. The carrier is not a bank.

**Fix.** Cite SR 11-7 / OCC 2026-13 as **analogous** model-risk expectation language. Use the phrase "state DOIs cite ... as analogous" or equivalent. Mark `[verify final OCC 2026-13 issuance date and bulletin number]` until confirmed.

**Check.** Search the artifact for "SR 11-7" and "OCC 2026-13"; each should be qualified by "analogous" or equivalent. The section heading should read "vs SR 11-7-equivalent expectations", not "vs SR 11-7".

#### ACA bright-lines are missing for individual / small-group health

**Symptom.** The change is for individual or small-group health, but the artifact does not check community rating, age-band, tobacco-surcharge, or geographic-area compliance.

**Why it's wrong.** PHSA §2701 and 45 CFR Part 147 are bright-line rules. A rate filing that misses these will be rejected by HHS / CMS or the state DOI on rate review.

**Fix.** Run the ACA-pricing checks section (template section 9) with status, evidence pointer, and gap for each bright-line rule.

**Check.** For any individual or small-group health change, section 9 should be present and complete. For other product types, section 9 may be omitted.

#### Illustrations are conflated with rate filing

**Symptom.** The change touches life illustrations, but the artifact treats the illustration analysis as part of the rate-filing analysis under #880.

**Why it's wrong.** Illustration governance under Model #582 is a separate test from rate-filing governance under #880. Both can apply on a life pricing change; they are different analyses.

**Fix.** Run section 10 (illustration check) separately. Section 3 (#880 unfair-discrimination analysis) does not subsume the illustration tests.

**Check.** For any life pricing change touching illustrated values, section 10 should be present and complete. Self-support test, lapse-support test, illustration-actuary certification, and disciplined-current-scale documentation should each have a status row.

#### State-by-state divergence collapsed to a federal answer

**Symptom.** The rating-factor map has a single "permitted / prohibited" column rather than one column per state in scope. The unfair-discrimination analysis reads as if it were federal.

**Why it's wrong.** Insurance pricing is state-regulated. The same factor may be permitted in one state and prohibited in another. The artifact must name the divergence.

**Fix.** Build the rating-factor map (Excel workbook) with one `<state>_status` column per state in scope. Build the state-DOI-bulletin-alignment section with one row per state. Run the unfair-discrimination analysis per state where divergence exists.

**Check.** The rating-factor map should have at least one state-status column per state in the filing footprint. The bulletin-alignment section should have one row per state.

#### The artifact reads as a model-validation report

**Symptom.** The artifact dives deep into model architecture, training-data statistics, and validation metrics, treating the model-validation report as the deliverable.

**Why it's wrong.** Model validation is one input to the pricing-governance review. The deliverable is the governance review, not the validation report.

**Fix.** Reference the validation report as input. Add the AIS Program cross-walk, the SR 11-7-equivalent documentation review, the ECDIS provenance check, the state-DOI-bulletin alignment, the privacy and consumer-disclosure posture, and the unfair-discrimination analysis.

**Check.** The artifact should read coherently if the model-validation report is removed; the governance findings stand on their own.

#### HIPAA layer skipped where PHI is in scope

**Symptom.** The change involves life or health AU using prescription-history or medical data, but the privacy section does not run the HIPAA Privacy Rule analysis.

**Why it's wrong.** HIPAA applies wherever the pricing or underwriting model touches PHI. The "underwriting purposes" use under §164.506 has constraints; the GINA carve-out and the minimum-necessary principle apply.

**Fix.** Run the HIPAA-specific check items in the privacy section (template section 8): notice-of-privacy-practices alignment; authorization posture; BAA chain; minimum-necessary analysis; de-identification documentation where applicable; breach-notification posture.

**Check.** For any change involving life or health AU touching prescription-history or medical data, section 8 should include the HIPAA sub-section with non-empty status rows for the seven HIPAA elements.

#### The Excel rating-factor map is missing or stub

**Symptom.** The deliverable is a Word memo only; the rating-factor map is in a markdown table inside the memo or in a stub workbook.

**Why it's wrong.** A state DOI rate analyst reads the rating-factor map line-by-line. The Excel workbook is the artifact a rate analyst will read; the Word memo is the narrative.

**Fix.** Render the workbook via the `xlsx` skill using the structure in `templates/default-output.md` (five tabs: factor_map, state_status_matrix, ai_ml_components, findings, source_citations). The Word memo cross-references the workbook by file name.

**Check.** The deliverable folder should contain a `.docx` and an `.xlsx`. The `.xlsx` should have the five tabs; the factor_map tab should have one row per rating factor with non-empty state-status columns.
