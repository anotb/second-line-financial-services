# Examples and troubleshooting

One section per worked example, then troubleshooting. Read only what you need.

## bulk-rescan-bank-portfolio

### Example: bulk re-scan over a community-bank portfolio with a single tier-1 hit

Public-source-derived. No named institution. The shape mirrors a recurring pattern at community banks: an event-driven adverse-media triage on an individual customer following a tier-1 newspaper report on a regional fraud-ring indictment, where the customer's name appears as a co-defendant.

#### Input

- **Institution**: a community bank with a single-state retail and small-business franchise; primary regulator FDIC for this example.
- **Customer**: an individual retail customer holding a checking account, a savings account, and a small consumer-installment loan. CDD file shows occupation, employer, and home address; no business-customer attributes.
- **Triage scope**: `event_driven`. Trigger: a tier-1 regional-newspaper article reporting on a federal indictment in a regional fraud-ring matter; the customer's full name appears in the indictment's named defendant list.
- **Hit set**: a single hit (the regional-newspaper article), surfaced by the firm's daily adverse-media feed and corroborated by an open-source pull that returned the underlying federal-court docket entry.
- **Engagement scope supplied**: institution = community bank; primary regulator = FDIC; persona = second-line negative-news triage reviewer reporting to the BSA officer; source posture = public-plus-firm-policy-plus-system-of-record-evidence; sector overlay = banking; cross-cutting overlays = none initially. The conduct overlay is added to the triage when the underlying indictment surfaces vulnerable-customer-harm patterns (the alleged fraud targeted elder-care patients), per the scope amendment.
- **CDD file evidence available**: customer record, ID verification, account-opening interview note, and the recent transaction-monitoring history (no alerts in the last 24 months).

#### Output sketch

The skill produces a triage memo against the single hit. Headlines:

- **Hit set summary** — 1 total hit. Source-class breakdown: 1 tier-1 (regional-newspaper article naming the federal-court docket entry; corroborated by the underlying docket pull). Publication-date 3 days before the triage; underlying-event-date (indictment filing date) 4 days before the triage.
- **Per-hit assessment**:
  - **`hit_id`: 001**. Headline: tier-1 newspaper coverage of a federal indictment in a regional elder-financial-exploitation-typology fraud-ring matter; the customer is named as a co-defendant.
  - **`identity_confidence`: high**. Identity-rationale: legal name matches; date of birth in the docket entry matches the CDD file; home address (city and state) matches; occupation in the docket-listed defendant profile matches the CDD file's occupation field.
  - **`source_class`: regulator/court** (federal indictment, corroborated by major-outlet coverage). **`source_tier`: tier_1**.
  - **`event_date`: indictment filing date** (4 days before the triage). **`publication_date`: 3 days before the triage**.
  - **`materiality`: material**. **`typology_tags`: [elder financial exploitation, fraud]**. The FinCEN advisory on elder financial exploitation (FIN-2022-A002) provides the typology indicators; the indictment surfaces multiple indicator patterns directly.
  - **`conduct_dimension_tag`: vulnerable-customer overlap** (the alleged victims are elder-care patients). The conduct overlay is loaded for the parallel routing.
  - **`linkage_strength`: direct** (the customer is named as a defendant).
  - **`disposition`: relevant**.
  - **`evidence_pointer`: federal-court docket URL; regional-newspaper article URL**.
- **Aggregated themes** — single hit, so no cross-hit themes. The triage notes the typology specifically because the FinCEN elder-financial-exploitation indicator overlap is direct.
- **Downstream routing**:
  - **`cdd-risk-review` (event-driven refresh)** — the indictment is a material customer-information event; the refresh reads against the four pillars (CIP unchanged, beneficial-ownership not applicable to individual customer, expected-activity now requires re-read against the alleged conduct, ongoing-monitoring scope re-evaluation).
  - **`edd-escalation-pack`** — the customer is not currently on an EDD profile; the indictment with elder-financial-exploitation typology is a candidate for EDD upgrade. Routed for the EDD analyst to open the pack.
  - **`sar-decision-qa` (evidence input)** — no in-flight alert exists, but the triage memo carries forward as evidence input on any future alert that may surface from the post-event monitoring scope re-evaluation. Routing line opened conditionally; not a current SAR-decision input.
  - **`sanctions-screening-qa`** — not implicated; no routing line.
  - **Conduct lane (parallel routing)** — vulnerable-customer overlap surfaced; routing line to the consumer-compliance function for the elder-financial-exploitation framework's parallel discipline (Reg E error-resolution and unauthorized-transfer rules where relevant; CFPB elder-financial-exploitation-related guidance; state adult-protective-services notification framework where the bank's program calls for it). The triage does not initiate APS notification; it routes the artifact to the named decisionmaker.
  - **Relationship-level review gate** — the BSA officer reviews the memo and decides on relationship-level posture (continued monitoring, EDD upgrade, account restriction, exit consideration). The triage does not recommend exit, restriction, or rating change.
- **Open questions and evidence-needed items**:
  - **Co-defendant-relationship inventory**: the indictment names co-defendants; the relationship owner pulls the firm's customer base for matches against co-defendants to surface related-party exposure. Owner: relationship owner. `[evidence needed]`.
  - **Transaction-monitoring scope re-evaluation against typology**: the customer's transaction history did not fire alerts under the in-scope scenarios; the typology indicators in the FinCEN advisory may not all be in the current scenario set. Cross-reference to `aml-model-monitoring`. Owner: AML monitoring team. `[evidence needed]`.
  - **Vulnerable-customer policy applicability**: the customer is named as alleged perpetrator, not as alleged victim, but the firm's vulnerable-customer-protection policy may carry a notification or review obligation when a customer is implicated in an elder-financial-exploitation matter. Owner: consumer-compliance function. `[evidence needed]`.
- **Source trace** — anchors to `references/source-anchors.md` (FFIEC CDD section, FinCEN CDD Final Rule fourth pillar, FinCEN Advisory on Elder Financial Exploitation FIN-2022-A002), `references/sector-overlays.md#banking` (typology-link patterns; bank routing patterns), and `references/cross-cutting.md#conduct` (vulnerable-customer overlap; consumer-compliance parallel routing).
- **Confidence label** — `high`. Identity-confidence is high; source class is tier-1; the typology tag is well-anchored to a named FinCEN advisory; the routing is well-aligned with the FFIEC ongoing-monitoring expectations.

#### Why this scenario matters

- **A single hit can be a complete triage.** Volume is not the work; identity-confidence and typology-tagging are.
- **The FinCEN advisory on elder financial exploitation provides the typology link**; the typology tag is not "negative news" but the named advisory category.
- **The conduct overlay loads for vulnerable-customer overlap** even when the customer is the alleged perpetrator, not the alleged victim; the parallel consumer-compliance routing is the discipline.
- **The triage does not initiate APS notification, recommend exit, file a SAR, or change the rating.** It routes the artifact to the named decisionmaker.
- **Cross-reference to `aml-model-monitoring`** is real: the absence of alerts on a customer implicated in a typology-linked matter is a scope-re-evaluation question, not a clean-bill-of-health.
- **The transaction-monitoring history is read as context**, not as adjudication. The triage notes the no-alert posture and routes the scope re-evaluation rather than asserting a no-typology disposition.

#### Anchors

- FinCEN Customer Due Diligence Final Rule (May 2016, compliance May 11, 2018) — fourth pillar.
- FFIEC BSA/AML Examination Manual — Customer Due Diligence section.
- FinCEN Advisory on Elder Financial Exploitation (FIN-2022-A002, June 15, 2022) [verify date].
- OCC / FRB / FDIC / NCUA Joint Statement on Risk-Focused BSA/AML Supervision (July 22, 2021).

See `references/source-anchors.md` for full citations, `references/sector-overlays.md#banking` for the bank-specific frame, and `references/cross-cutting.md#conduct` for the vulnerable-customer parallel routing.

## principal-civil-fraud-commercial-bank

### Example: principal-level civil fraud (commercial customer at a mid-size US bank)

Public-source-derived. No named institution. The shape mirrors a recurring pattern at mid-size US banks: a periodic adverse-media re-scan on a commercial customer (legal entity) returns a populous hit set dominated by common-name false matches, with a small material subset surfacing principal-level adverse media.

#### Input

- **Institution**: a mid-size US bank with a regional commercial-banking franchise; primary regulator OCC for this example (FRB or FDIC depending on charter).
- **Customer**: a private commercial-services LLC, mid-eight-figure annual revenue, two principals on file (one control-prong individual, one ownership-prong individual at 60%, second principal at 40%).
- **Triage scope**: `periodic_refresh` on the customer's risk-tier cycle (high-risk customer, annual cycle).
- **Hit set (as presented for triage)**: 42 hits across the firm's adverse-media vendor and a supplementary open-source pull. Vendor self-tags 14 hits as "high reliability", 18 as "medium", 10 as "low".
- **Engagement scope supplied**: institution = mid-size US bank; primary regulator = OCC; persona = second-line negative-news triage reviewer reporting to the BSA officer; source posture = public-plus-firm-policy-plus-system-of-record-evidence; sector overlay = banking; cross-cutting overlays = none.
- **CDD file evidence available**: customer record (legal name, formation, EIN, registered address, principal place of business), beneficial-ownership certification (named control-prong and ownership-prong individuals with matchable attributes), expected-activity profile (commercial-services-specific), risk-rating drivers (industry concentration, counterparty geography, transaction velocity), and the most recent CDD refresh memo.

#### Output sketch

The skill produces a triage memo against the hit set. Headlines:

- **Hit set summary** — 42 total. Source-class breakdown: 4 tier-1 (a federal court filing, two regulator press releases, one major-outlet article); 12 tier-2 (trade press and aggregator content); 26 tier-3 (forum, social, unverified aggregator content). Publication-date range covers eight years; underlying-event-date range covers ten years.
- **Per-hit assessment headlines**:
  - **28 hits** (out of 42) **disposition `not_relevant`** on identity grounds. Common-name false matches: the customer's legal name shares a token with three unrelated entities surfaced in the hit set; the matchable-attribute join (jurisdiction, formation date, business activity) eliminates them. The triage names the false-match pattern in `aggregated_themes` rather than dispositioning each individually in the per-hit detail.
  - **8 hits** (tier-3 forum content) **disposition `unverified_pending`** carrying `[evidence needed]` for primary-source corroboration. The triage does not escalate on uncorroborated tier-3 content.
  - **4 hits** (the two regulator press releases and two of the trade-press hits) **disposition `not_relevant`** on entity-disambiguation grounds: the named entity is similar but not the customer (different jurisdiction, different EIN, different beneficial owners).
  - **2 hits** (the federal court filing and the major-outlet article reporting on the same matter) **disposition `relevant`**. Identity confidence high (the filing names one of the customer's principals with corroborating attributes — date of birth, address, prior employment — that match the CDD file's beneficial-ownership record). Tier-1 source class. `event_date` 14 months before the triage; `publication_date` 11 months before. Materiality `material`. Typology tag: `fraud` (civil fraud allegation in a commercial-counterparty matter; not a criminal indictment). Linkage strength: `direct` (the principal is named as a defendant in the civil filing).
- **Aggregated themes**:
  - Common-name false-match pattern dominates the bulk; the firm's vendor query likely needs review for the customer-segment context (a source-posture observation routed to the BSA program, not to per-customer escalation).
  - Principal-level adverse media (the two material hits both bear on one of the two named principals); no entity-level enforcement or court action surfaced.
  - No escalating-timeline pattern; the material subset is a single matter.
- **Downstream routing**:
  - **`cdd-risk-review` (event-driven refresh)** — the principal-level civil fraud allegation is a material-customer-information event under the CDD ongoing-monitoring pillar; the refresh re-reads the principal's role in the entity, the beneficial-ownership inconsistency check, and the expected-activity profile in light of the alleged conduct.
  - **`edd-escalation-pack`** — the principal's other public roles (per the open-question item below) may surface PEP-adjacency or correspondent-banking overlap warranting EDD upgrade. Routed conditionally on the corroboration of the principal's public-role inventory.
  - **`sanctions-screening-qa`** — not implicated by the material subset; no routing line.
  - **`sar-decision-qa`** — not implicated unless an in-flight or recent alert exists; the routing is conditional on the alert-history check.
  - No further action on the 38 non-material hits; next periodic re-scan on cycle.
- **Open questions and evidence-needed items**:
  - **Principal's public-role inventory** (PEP-adjacency check): public-record search for the principal's other directorships, political affiliations, and government-contracting roles. Owner: EDD analyst. `[evidence needed]`.
  - **Civil-matter outcome and counterparty identification**: the filing is 14 months old; the docket may carry an updated status the triage did not pull. Owner: source-corroboration owner. `[evidence needed]`.
  - **Beneficial-ownership inconsistency check**: the alleged conduct in the civil filing implies a counterparty relationship the customer's expected-activity profile does not reflect; the CDD refresh reads against this. Owner: relationship owner. `[evidence needed]`.
- **Source trace** — anchors to `references/source-anchors.md` (FFIEC CDD section, FinCEN CDD Final Rule fourth pillar, joint statement on risk-focused supervision, Wolfsberg adverse-media guidance) and `references/sector-overlays.md#banking` (commercial-customer adverse-media patterns, principal-versus-entity drift, common-name false-match handling).
- **Confidence label** — `medium`. Identity-confidence on the material subset is high; corroboration on the open questions is pending; the source-posture observation on the bulk false-match pattern is the lower-confidence read.

#### Why this scenario matters

- **Identity confidence runs first.** Most of the 42 hits drop out on the identity cut; without it the triage would be 42 misallocated hours and a misleading materiality narrative.
- **Common-name false-match patterns are named at the theme level**, not dispositioned per hit, when the false-match basis is the same. This keeps the per-hit detail readable.
- **Source-tier is anchored to source class**, not to vendor self-tagging; the vendor's "low" reliability tag does not eliminate the obligation to read back to the source class.
- **Principal-versus-entity drift is the load-bearing pattern** in this scenario; the triage names it as a theme and the routing reflects it.
- **The triage does not change the rating, decline the relationship, file a SAR, or escalate to EDD as a closed decision.** It routes the artifact to the named decisionmaker.
- **Open questions carry forward** as `[evidence needed]` rather than being resolved by triage assertion.

#### Anchors

- FinCEN Customer Due Diligence Final Rule (May 2016, compliance May 11, 2018) — fourth pillar (ongoing monitoring) covers material customer-information updates.
- FFIEC BSA/AML Examination Manual — Customer Due Diligence section.
- OCC / FRB / FDIC / NCUA Joint Statement on Risk-Focused BSA/AML Supervision (July 22, 2021).
- Wolfsberg Group guidance on adverse media / negative news (public industry reference).

See `references/source-anchors.md` for full citations and `references/sector-overlays.md#banking` for the bank-specific adverse-media frame.

## troubleshooting

### Troubleshooting: negative-news-triage

Recurring defects in adverse-media triage memos and in the upstream hit sets, and how the skill handles them.

#### Identity confidence asserted on name match alone

**Symptom**: per-hit `identity_confidence` set to `high` because the hit's subject name matches the customer name.

**Why it happens**: bulk re-scan output dominates the work, common-name false matches are the dominant noise category, and the path of least resistance is to disposition on name alone.

**Fix**: identity confidence is rationale-bearing. The per-hit `identity_rationale` field forces the matchable-attribute join (jurisdiction, formation date, beneficial ownership, occupation, employer, prior-address, counterparty pattern). A name match without a matchable-attribute join sits at `low` or `unverified`, not at `high`. The bulk-scan example shows the pattern: 28 of 42 hits drop on the identity cut alone; the triage that skips the identity rationale would have escalated 28 false-positive matters.

#### Source reliability collapsed into vendor self-tagging

**Symptom**: `source_tier` set to whatever the vendor's reliability tag says, with no source-class read.

**Why it happens**: vendors ship reliability tags as part of the product; treating them as authoritative saves time.

**Fix**: vendor self-tagging is a starting hypothesis, not the tier. The triage reads back to the source class (regulator press release, court filing, major outlet with named bylines and editorial accountability versus secondary outlet, trade press, aggregator versus forum, social, unverified aggregator) and tiers from there. A vendor "high reliability" tag on an aggregator-only article is tier-2 or tier-3 in the source-class read, not tier-1.

#### Recency reported as publication date, ignoring underlying event date

**Symptom**: a 2017 event re-published in 2026 reported as a 2026 finding; the materiality read inflates accordingly.

**Why it happens**: vendor exports and aggregator pipelines often surface only the publication date; the underlying event date requires reading the source.

**Fix**: separate `event_date` and `publication_date` fields are required. An old event re-published yesterday is still an old event. The recency dimension feeds the materiality read; conflation is a finding to remove.

#### Materiality assessed against a generic "negative news = bad" frame

**Symptom**: hits flagged material because they are reputationally salient, with no financial-crime typology link.

**Why it happens**: the triage substitutes the reviewer's negative-press reaction for the typology-link discipline.

**Fix**: the per-hit `typology_tags` field forces a named typology link or a "no clear typology" tag. The typology library lives in `references/source-anchors.md` (FinCEN advisories, OFAC guidance, sector-overlay-specific patterns); reputationally salient hits with no typology link sit at `not_material` for the AML lane. When the conduct overlay is loaded, the conduct-dimension tag carries the parallel materiality for conduct-relevant hits even where the AML typology is absent.

#### Aggregated themes skipped

**Symptom**: per-hit triage runs cleanly but the memo carries no aggregated-themes section.

**Why it happens**: the per-hit pass dominates the time budget; the cross-hit synthesis feels redundant.

**Fix**: aggregated themes is the spine the per-hit pass cannot see. Recurring counterparties across independent hits, escalating timelines, jurisdictional clustering, principal-versus-entity drift, and common-name false-match patterns are the patterns that route the triage downstream. A hit set with no themes carries that observation; do not invent a pattern, but do not skip the section either.

#### Common-name false matches dispositioned individually

**Symptom**: 28 separate per-hit dispositions with the same false-match basis bloating the memo.

**Why it happens**: the per-hit template invites per-hit dispositions.

**Fix**: when the false-match basis is the same across many hits, name the pattern in `aggregated_themes` once and disposition the cluster as a group rather than per hit. The per-hit detail in the memo should read the material subset and the unverified-pending subset, not the whole common-name cluster.

#### Routing recommends a closed decision

**Symptom**: the routing block says "rate up to high", "open EDD", "file SAR", "exit relationship".

**Why it happens**: the reviewer has formed a view and writes the view as the recommendation.

**Fix**: the triage routes the artifact to the named decisionmaker; the decisionmaker decides. The routing names the destination (CDD refresh, EDD pack, SAR-decision evidence input, sanctions-screening overlap, conduct-lane parallel routing) and the rationale; it does not propose the rating change, the EDD upgrade, the SAR filing, or the exit. A routing recommendation that proposes the closed decision is itself a finding to remove.

#### Date-as-of missing on the triage memo

**Symptom**: downstream skills consume the triage record without knowing whether it is current.

**Why it happens**: the triage was performed against a hit set generated days or weeks earlier; the as-of date on the memo collapses to "today" or is omitted.

**Fix**: the memo carries both the **triage-performed date** and the **hit-set-as-of date**. Adverse-media findings are perishable on both axes; downstream skills need both dates to assess currency.

#### Source posture on the bulk re-scan unobserved

**Symptom**: the memo flags individual hits but does not surface the bulk pattern (high tier-3 noise, vendor-tag anomalies, identity-evidence thinness).

**Why it happens**: per-hit work crowds out the program-level observation.

**Fix**: a hit set dominated by tier-3 noise is itself a finding about the source posture, not just about the customer. The memo's executive summary carries the source-posture finding when it applies, and the routing surfaces the program-level review (BSA program, source-corroboration owner) rather than letting the noise pollute per-customer escalation.

#### Conduct overlap dropped because no AML typology

**Symptom**: a hit with strong customer-harm content but no AML typology tag dispositioned `not_material`.

**Why it happens**: the AML triage frame does not have a slot for conduct-only material.

**Fix**: when the engagement loads the conduct cross-cutting overlay, the per-hit `conduct_dimension_tag` exists for conduct-only hits. The conduct lane carries the parallel routing (consumer compliance, conduct-risk committee, producer oversight, fair-lending function, adviser supervision); the hit is not dispositioned `not_material` simply because the AML typology is absent.

#### Cyber-typology overlap routed only to AML lane

**Symptom**: a CVC counterparty hit with sanctions-evasion or ransomware linkage routed only to `cdd-risk-review`, missing the sanctions-screening overlap.

**Why it happens**: the cyber typology surfaces in the materiality read but the routing default lands in the CDD lane.

**Fix**: where the typology surfaces sanctions-evasion or ransomware-payment-facilitation linkage, the load-bearing routing line is to `sanctions-screening-qa`. The CDD lane is secondary; do not invert the priority.

#### Beneficial-ownership inconsistency implied by the hit but not surfaced

**Symptom**: a tier-1 hit implies an undisclosed control or counterparty relationship the customer's CDD file does not reflect, and the triage does not name the inconsistency.

**Why it happens**: the per-hit pass focuses on the hit itself, not on the file the hit bears against.

**Fix**: the open-questions block carries beneficial-ownership-inconsistency items as `[evidence needed]` for the relationship owner; the routing line to `cdd-risk-review` carries the rationale. The triage does not re-rate or re-certify beneficial ownership; it surfaces the inconsistency.

#### Vulnerable-customer overlap underread

**Symptom**: an elder-financial-exploitation typology hit dispositioned without the conduct overlay and without the FinCEN advisory citation.

**Why it happens**: the typology library is treated as optional rather than as the named-advisory anchor.

**Fix**: the FinCEN Advisory on Elder Financial Exploitation provides the typology indicators and the named anchor; the conduct overlay carries the vulnerable-customer parallel routing. Both are loaded when the scope and the hit set warrant; neither is optional.
