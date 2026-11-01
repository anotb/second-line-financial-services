# Examples and troubleshooting

One section per worked example, then troubleshooting. Read only what you need.

## cash-intensive-llc-community-bank

### Example: cash-intensive LLC (new account at a community bank)

Public-source-derived. No named institution. The shape mirrors a standing pattern at small and mid-sized community banks: a new-account opening for a single-member LLC operating a cash-intensive convenience-store business, with a CDD file that looks complete on the CIP and beneficial-ownership pillars but thin on expected activity and rating-driver evidence.

#### Input

- **Institution**: a community bank with a regional footprint and one primary regulator (FDIC for this example; FRB or OCC depending on charter).
- **Customer**: single-member LLC. Sole 100% beneficial owner is also the control-prong individual. Business: convenience store with food service. State of formation matches state of operations.
- **CDD file (as presented for QA)**:
  - CIP: legal name, formation date, registered agent address, EIN. Verification documentary (state filing extract, EIN letter). Discrepancies: none recorded.
  - Beneficial ownership: certification form on file, dated at account opening. Control prong: named individual. Ownership prong: same named individual at 100%. ID document attached for the named individual. BOI filing status field on the file: blank.
  - Expected activity: documented as "general business banking with cash deposits".
  - Risk rating: "medium". Drivers listed: "small business, cash deposits".
  - Monitoring scope: standard small-business monitoring scenarios; no scenario-specific tuning notes.
  - Refresh cycle: per firm policy, medium-risk small business reviewed every 24 months.
- **Engagement scope supplied**: institution = community bank; primary regulator = FDIC; persona = second-line CDD QA reviewer reporting to the BSA officer; source posture = public-plus-firm-policy-plus-system-of-record-evidence; sector overlay = banking; cross-cutting overlays = none.
- **Review type**: new_account.

#### Output sketch

The skill produces a CDD review memo against the file. Headlines:

- **Customer profile summary** — single-member LLC; convenience store with food service; one US state in play.
- **CIP coverage (Pillar 1)** — `cip_status = sufficient`. Identifying information collected; documentary verification on file; no discrepancies. Retention status meets `§1020.220(a)(3)`.
- **Beneficial ownership (Pillar 2)** — `beneficial_ownership_status = partial`. Certification on file with control prong and ownership prong satisfied by the same individual. ID corroboration on file. **BOI filing status under `31 CFR §1010.380` blank on the file** — reviewer flags `[verify]` with the as-of date and the rule-state read on that date; on most current readings, a single-member LLC formed for active business is a reporting company unless an exemption applies, but the file should evidence the determination.
- **Nature and purpose / expected activity (Pillar 3)** — `expected_activity_status = missing`. The "general business banking with cash deposits" entry is generic boilerplate; the convenience-store business model has typical expected cash deposit volumes, ATM network usage patterns (where the store hosts an ATM), money-order sales activity (where in scope), and lottery / EBT / SNAP redemption patterns that should be specific in the profile to drive monitoring scenario tuning. The QA flags this as a material gap.
- **Risk rating** — current rating "medium"; `rating_reasonableness = borderline`. The drivers listed are labels without evidence linkage. The cash-intensity of the customer's business model is itself the rating's load-bearing driver, and the file does not evidence the cash intensity (no expected-volume figure, no industry-profile note, no customer-stated rationale on cash levels). The QA does not change the rating; it surfaces the misalignment as a finding.
- **Ongoing monitoring (Pillar 4)** — `monitoring_scope_status = partial`. Standard small-business monitoring scenarios are in scope; threshold calibration against an unspecific expected-activity profile cannot be evaluated. The QA flags the cross-reference to `aml-model-monitoring` for threshold tuning consideration once the expected-activity profile is specified.
- **EDD escalation posture** — `edd_status = not_required` on file evidence; cash-intensive label alone does not trigger EDD without elevated additional drivers (geography, structure, jurisdictions of concern, transaction patterns). The QA notes the borderline call and the conditions under which it would re-evaluate.
- **Material gaps**:
  - Quantified expected-cash-deposit profile (pillar = expected_activity; severity = material).
  - Customer-stated rationale for expected cash levels (pillar = expected_activity; severity = moderate).
  - BOI filing status determination with as-of date and rule-state read (pillar = beneficial_ownership; severity = moderate).
  - Rating-driver evidence linkage (pillar = risk_rating; severity = material).
- **Reviewer findings**:
  - `criterion = expected_activity_specificity`, severity material. Boilerplate expected-activity statement cannot drive monitoring scenario tuning on the cash-intensive typology profile.
  - `criterion = rating_driver_evidence`, severity material. Driver labels without evidence linkage.
  - `criterion = boi_filing_grounding`, severity moderate. BOI status field blank.
- **Recommended human-review gates and owner actions** — `recommendation = return_to_first_line_for_evidence`. Conditions: quantified expected-cash-deposit profile, customer-stated rationale for cash levels, BOI determination with as-of date, rating-driver evidence linkage. Schedule monitoring threshold review after the profile is updated; cross-reference to `aml-model-monitoring`. The QA reviewer does not change the rating, decline the account, or set the EDD trigger; the BSA officer and the customer-onboarding compliance lead decide on the routing.
- **Source trace** — anchors to `references/source-anchors.md` (CDD Final Rule, FFIEC CDD section, `§1010.230`, `§1020.220`), `references/sector-overlays.md#banking` (cash-intensive-business risk drivers and the rating-driver-evidence expectation).
- **Confidence label** — `medium`. The CIP and beneficial-ownership pillars are read at high confidence; the expected-activity and rating findings are at high confidence on the file evidence; the BOI status determination is at lower confidence pending the rule-state read.

#### Why this scenario matters

- **The CDD review separates the four pillars**. CIP is complete; that does not make CDD complete. The pillar-by-pillar read is what surfaces the expected-activity and rating-driver gaps.
- **Risk-rating drivers as labels is the dominant defect at small-business onboarding**. The skill's `criterion = rating_driver_evidence` exists for this pattern.
- **Expected-activity specificity is a monitoring-tunability question, not a cosmetic preference**. A profile that cannot drive scenario tuning is a material gap, not an observation.
- **BOI filing status is dated and grounded**. The file should evidence the determination with an as-of date; the QA flags `[verify]` rather than assert without grounding.
- **The QA does not change the rating**. The misalignment is a finding routed to the BSA officer; the firm's risk-rating governance owns the rating.
- **The cross-reference to `aml-model-monitoring` is real**. Threshold tuning is its scope, not the CDD QA's; the QA flags the cross-reference.

#### Anchors

- FinCEN Customer Due Diligence Final Rule (May 2016, compliance May 11, 2018).
- FFIEC BSA/AML Examination Manual — Customer Due Diligence section.
- 31 CFR §1010.230 — beneficial ownership for legal-entity customers.
- 31 CFR §1010.380 — BOI reporting (CTA implementing rule; date the read).
- 31 CFR §1020.220 — bank CIP.

See `references/source-anchors.md` for full citations and `references/sector-overlays.md#banking` for the bank-specific frame.

## periodic-refresh-broker-dealer-hni

### Example: periodic refresh on a high-net-worth individual at a regional broker-dealer

Public-source-derived. No named institution or named natural person. The shape mirrors a standing pattern in capital-markets CDD periodic-refresh work: a long-tenured high-net-worth customer with international wire activity whose source-of-wealth statement is stale and whose expected-activity profile predates a publicly known change in the customer's business circumstances.

#### Input

- **Institution**: a regional broker-dealer; primary regulators FINRA / SEC; the broker-dealer is the institution of record for CIP and the operative SAR rule.
- **Customer**: high-net-worth individual; long-tenured; primary residence in the US; second residence and significant business activity in a non-US jurisdiction.
- **CDD file (as presented for QA)**:
  - CIP under `§1023.220`: complete. Documentary verification on file. ID-document refresh on the file's natural cycle.
  - Beneficial ownership: not applicable (individual customer).
  - Expected activity: documented at original onboarding 11 years ago. Profile: international wire activity to and from the named non-US jurisdiction; private-investment-vehicle holdings; expected wire counterparties named.
  - Source-of-wealth statement: customer-supplied at original onboarding 11 years ago; not refreshed; no independent corroboration on file.
  - Risk rating: "medium-high"; drivers: "international exposure", "high-net-worth", "single-jurisdiction concentration outside US".
  - Refresh cycle: per firm policy, 24 months for medium-high.
  - Monitoring scope: structuring, layering, wire-pattern-anomaly, sanctions-adjacent.
  - Trigger for this refresh: 24-month periodic cycle. Reviewer notes a publicly known change in the customer's business circumstances since the last refresh (acquisition or sale of a named business interest reported in trade press).
- **Engagement scope supplied**: institution = broker-dealer; primary regulator = FINRA / SEC; persona = second-line CDD QA reviewer; source posture = public-plus-firm-policy-plus-system-of-record-evidence; sector overlay = capital-markets; cross-cutting overlays = none.
- **Review type**: periodic_refresh.

#### Output sketch

The skill produces a CDD review memo against the refresh file. Headlines:

- **Customer profile summary** — high-net-worth individual; long-tenured customer; US residence with significant non-US business and asset exposure.
- **CIP coverage (Pillar 1)** — `cip_status = sufficient`. ID-document refresh on the file's cycle; verification corroboration on file; no discrepancies.
- **Beneficial ownership (Pillar 2)** — `beneficial_ownership.applicable = false` (individual customer); pillar not applied.
- **Nature and purpose / expected activity (Pillar 3)** — `expected_activity_status = partial`. The expected-activity profile is specific at the original onboarding level but predates the publicly known change in the customer's business circumstances. The wire-counterparty list and the private-investment-holdings profile may no longer match the customer's current activity. The QA flags this as a material gap and recommends an updated profile.
- **Risk rating** — current "medium-high"; `rating_reasonableness = borderline`. The rating drivers are reasonable on the original profile; the publicly known change in business circumstances introduces possible new drivers (e.g., PEP-adjacent exposure if the change involves a regulated or government-adjacent role; new geographic exposure if the change involves a different jurisdiction). The QA flags the rating for re-evaluation but does not change it.
- **Ongoing monitoring (Pillar 4)** — `monitoring_scope_status = partial`. The monitoring scope is reasonable for the original profile; the threshold calibration may be misaligned if the customer's actual activity has shifted since the last refresh. The QA flags cross-reference to `aml-model-monitoring` for threshold review once the expected-activity profile is updated.
- **EDD escalation posture** — `edd_status = borderline`. The publicly known business change may carry PEP-adjacent or jurisdictional considerations that elevate to EDD. The QA recommends the EDD evaluation route through `edd-escalation-pack` and does not produce the EDD pack itself.
- **Material gaps**:
  - Updated expected-activity profile reflecting the post-change business circumstances (pillar = expected_activity; severity = material).
  - Refreshed source-of-wealth statement with independent corroboration (pillar = expected_activity; severity = material). The 11-year-old self-attestation is not corroboration.
  - Re-evaluation of risk-rating drivers in light of the publicly known change (pillar = risk_rating; severity = material).
  - EDD-trigger evaluation (pillar = edd; severity = moderate; routes to `edd-escalation-pack`).
- **Reviewer findings**:
  - `criterion = expected_activity_specificity`, severity material. Profile predates the publicly known change.
  - `criterion = rating_driver_evidence`, severity material. Drivers do not reflect post-change exposure.
  - `criterion = edd_trigger_application`, severity moderate. Trigger evaluation overdue given the change.
  - `criterion = refresh_cycle_adherence`, severity observation. Cycle was met; the gap is in the depth of the refresh on the source-of-wealth pillar specifically.
- **Recommended human-review gates and owner actions** — `recommendation = escalate_to_edd` with `recommendation_notes`: refresh expected-activity profile and source-of-wealth statement before the EDD pack is built; re-evaluate rating after the EDD evaluation. Cross-reference to `edd-escalation-pack` and `aml-model-monitoring`. The QA reviewer does not change the rating, set the EDD trigger directly, or route the customer to relationship exit; the BSA officer, the AML QA team lead, and the EDD committee decide.
- **Source trace** — anchors to `references/source-anchors.md` (CDD Final Rule, FFIEC CDD section, `§1023.220`), `references/sector-overlays.md#capital-markets` (source-of-wealth corroboration expectation; private-banking-adjacent EDD frame).
- **Confidence label** — `medium`. The findings are at high confidence on the file evidence; the EDD-trigger evaluation requires the EDD-pack work that this skill does not produce.

#### Why this scenario matters

- **Stale source-of-wealth statements at periodic refresh on long-tenured high-net-worth customers** are the dominant defect in capital-markets CDD work. The skill's `criterion = expected_activity_specificity` and `rating_driver_evidence` carry this pattern.
- **Customer self-attestation is not corroboration**. The 11-year-old statement is the customer's claim; the file should evidence independent corroboration where the rating warrants.
- **Publicly known changes in customer circumstances are an event-driven trigger even mid-periodic-cycle**. The QA reads the publicly known change against the file; if the change is material to the rating drivers, the periodic refresh has more to do than the cycle alone implies.
- **The boundary with `edd-escalation-pack` is real**. The CDD QA flags the EDD evaluation; it does not build the EDD pack. The cross-reference is the handoff.
- **The QA does not direct the rating change**. A rating change is a firm-governance decision routed to the BSA officer and the rating-governance forum the firm uses.

#### Anchors

- FinCEN Customer Due Diligence Final Rule (May 2016, compliance May 11, 2018).
- FFIEC BSA/AML Examination Manual — Customer Due Diligence section.
- 31 CFR §1023.220 — broker-dealer CIP.
- 31 CFR §1010.620 — enhanced due diligence for private-banking accounts (consulted for EDD-trigger framing where applicable).

See `references/source-anchors.md` for full citations and `references/sector-overlays.md#capital-markets` for the capital-markets-specific frame.

## troubleshooting

### Troubleshooting: cdd-risk-review

Recurring pitfalls. Read before producing the review memo and again before sign-off.

#### Scope discipline

##### Drifting into the rating decision

The QA produces findings, gaps, and routing recommendations against the CDD file. It does not set or change the customer risk rating, approve onboarding, file a SAR, or exit the relationship. The named decisionmaker is the BSA officer (with the customer-onboarding compliance lead and the EDD committee where the firm uses one). The skill outputs `recommendation`, not `decision`. A QA artifact that says "downgrade the rating to low" or "approve the account" or "exit the relationship" has misread its scope.

##### Reading three pillars instead of four

CIP is identification and verification at onboarding. CDD adds beneficial ownership, nature-and-purpose / expected activity, and ongoing monitoring. A "file looks complete" finding that did not separately read all four pillars has under-read the work. The schema's `cip_coverage`, `beneficial_ownership`, `expected_activity`, and `ongoing_monitoring` fields force the four-pillar read.

##### Treating CIP completeness as CDD completeness

A clean CIP is necessary but not sufficient. The QA marks `cip_status = sufficient` and still reads the next three pillars on their own. A frequent defect: a polished CIP folder masks thin work on expected activity and monitoring scope.

##### Reading the wrong rule for the institution

A bank-flavoured read on a broker-dealer file applies the wrong CIP rule and misframes the EDD posture. Load the sector overlay first; the operative CIP/CDD rule set sits there.

#### Beneficial-ownership discipline

##### Beneficial ownership treated as a one-time form

A legal-entity customer's ownership changes between refresh cycles; the file does not always reflect it. The QA reads the certification date against the latest entity filings, the signatory list, public filings, and any transactional pattern that implies undisclosed control. A certification dated five years ago on an entity with a public ownership change last year is a material gap, not a stylistic observation.

##### Trust, sole-prop, and unincorporated-association customers treated as legal entities under §1010.230

`§1010.230` applies to legal-entity customers as defined. Trusts, sole proprietors, and unincorporated associations are not legal-entity customers under the rule. The QA scopes the rule before applying the pillar; out-of-scope customers get the `not_applicable` status, not a "beneficial ownership missing" finding.

##### Exempt-entity claims accepted as a default

`§1010.230` carries an exemption list (publicly traded companies, certain regulated entities, certain pooled investment vehicles, others). Exemption claims are read against the rule, not assumed. A default exemption status is a finding.

##### BOI filing status asserted on stale ground

`31 CFR §1010.380` (CTA implementing rule) has had live litigation; the entity-class scope and the rule-state have moved through district-court rulings, nationwide injunctions, stays, and FinCEN interim final rulemaking. The QA marks `boi_filing_status` with an as-of date and the rule-state read on that date, and uses the `verify` enum value when the rule-state is unsettled for the customer's entity class. Asserting `required` or `not_required` without grounding is itself a finding.

#### Expected-activity discipline

##### Boilerplate profiles treated as adequate

"General business banking", "personal banking", "active trading" without specifics cannot drive monitoring scenario tuning. The QA flags non-specific expected-activity statements as a material gap, not a stylistic preference. The schema's `specificity = generic` value carries the finding.

##### Quantification missing on customer types where it matters

Cash-intensive businesses, high-velocity retail traders, cross-border-payment customers, MSB customers, and large-premium covered-product customers all benefit from quantified expected-volume figures. Where the firm's monitoring scenarios depend on calibration to an expected baseline, the QA reads whether the baseline exists in the file.

##### Customer self-attestation treated as corroboration

A source-of-wealth statement on a high-net-worth customer, an expected-volume narrative on a small-business customer, and a beneficial-ownership certification are all customer claims. The QA treats them as claims, not as corroboration; corroboration is what other file evidence provides. The schema separates customer self-attestation from corroborated evidence in the source-trace structure.

#### Risk-rating discipline

##### Rating drivers as labels

"Cash-intensive", "international", "PEP-adjacent" without evidence underneath are labels. The QA reads whether each driver ties to file evidence and marks `rating_drivers[].evidence_status = label_only` where it does not. The rating itself stays the firm's call; the QA does not change it.

##### QA changes the rating

The skill does not change the rating. A material misalignment between rating and drivers is a finding routed to the BSA officer and the rating-governance forum the firm uses; the QA frames the finding as a routing recommendation, not a directive.

##### Refresh cycle treated as the only refresh trigger

Refresh is event-driven and time-based on a risk basis. A 24-month cycle was met, but a publicly known change in customer circumstances since the last refresh is itself an event-driven trigger. The QA reads both.

#### Monitoring-scope discipline

##### Re-tuning monitoring scenarios in the CDD QA

Monitoring scenario tuning belongs to `aml-model-monitoring`. The CDD QA surfaces a finding when the monitoring scope or the threshold calibration does not match the customer's risk profile or the expected-activity profile, and cross-references; it does not re-tune the scenarios.

##### Generic monitoring scope on customers that warrant typology-specific tuning

A high-net-worth international customer, a cash-intensive business, a crypto-adjacent fintech customer all carry typology-specific monitoring expectations. A generic "small-business monitoring scenarios" entry on file is a `monitoring_scope_alignment` finding.

#### EDD discipline

##### EDD-trigger application without a sector-overlay read

The foreign-correspondent EDD frame (`§1010.610`) is for accounts maintained for foreign FIs; it is not a generic "international counterparty" rule. The private-banking EDD frame (`§1010.620`) carries a defined account-type scope. The QA scopes the rule before applying it.

##### Building the EDD pack inside the CDD review

EDD escalation routes through `edd-escalation-pack`. The CDD QA marks `edd_status` and cross-references; it does not produce the EDD pack itself. A QA artifact that includes the EDD analysis has stepped into the next skill's scope.

#### Sector-specific pitfalls

##### Applying the bank rule to a broker-dealer or fund

Bank CIP under `§1020.220` is not the same as broker-dealer CIP under `§1023.220` or mutual-fund CIP under `§1024.220`. Load the sector overlay first.

##### Applying the insurance rule to non-covered products

`§1025.210` covers permanent life with cash value, annuities with cash value, and other investment-type products. P&C, term life without cash value, group products, and health are generally outside scope. The QA scopes the product before applying any pillar.

##### Treating an investment-adviser customer as in-scope before the FinCEN adviser rule's compliance date

The FinCEN adviser AML rule (August 2024) phased in compliance dates. The QA dates the read and scopes the rule's effective state on that date for the adviser in question.

##### Reading the fintech onboarding artifact as the sponsor bank's CIP record

In a sponsor-bank model, the bank is the institution of record. The QA reads whether the bank reviewed and accepted the fintech's onboarding work, not whether the fintech's onboarding flow ran.

#### Output discipline

##### Citing without sections

Every regulator citation in the QA carries a section reference or a `[verify section]` placeholder. URL alone fails the source-anchor depth check. Use `references/source-anchors.md` for the canonical citation set; do not restate excerpts in the artifact body.

##### Marking unsupported claims silently

Use `[evidence needed]` explicitly. An inferred claim presented as evidenced is the failure mode the source-trace structure exists to prevent.

##### Closing with too much certainty

The confidence label is `high` only when the source posture, the file evidence, and the QA criteria all line up. `medium` and `low` are normal for early-stage QA work; `unknown` is honest where the firm has not yet resourced the evidence ask. A `high` confidence label on a memo with material gaps across two or three pillars is incoherent.

##### Memo over-extending into the next skill

Each adjacent skill has its own scope: `edd-escalation-pack` builds the EDD pack; `sar-decision-qa` reviews the alert decision; `aml-model-monitoring` re-tunes scenarios; `negative-news-triage` triages adverse media; `sanctions-screening-qa` disposes screening matches. The CDD QA flags cross-references and stops at the cross-reference.
