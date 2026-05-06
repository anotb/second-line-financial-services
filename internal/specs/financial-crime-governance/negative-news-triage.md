# negative-news-triage — Phase 1 spec sheet

Date: 2026-05-06
Plugin: financial-crime-governance
Phase: 1 (per-skill scoping; no SKILL.md content)

## Activation-tuned description

Triages an adverse-media or negative-news hit set against a specific customer or entity for relevance, identity confidence, source reliability, materiality to financial-crime risk, and downstream action. Produces a structured triage record that downstream artifacts (cdd-risk-review, edd-escalation-pack, sar-decision-qa) can consume. Does not change customer ratings, file SARs, or close customer relationships.

Best for:
- Adverse-media hit triage at onboarding, periodic refresh, or event-driven refresh.
- Bulk triage over a periodic adverse-media re-scan output.
- Pre-EDD triage feeding into an EDD escalation pack.
- Pre-SAR-decision triage where adverse media is part of the alert evidence basis.

Not the right tool when:
- The work is sanctions screening match disposition, not adverse media (use sanctions-screening-qa).
- The hit is already triaged and the next artifact is the EDD pack or SAR decision QA (use the corresponding skill).
- The work is a media-monitoring program design or vendor evaluation (out of scope; use vendor-diligence in third-party-operational-resilience for vendor evaluation).
- The decision is a final risk-rating change, EDD escalation, or SAR filing. Skill produces triage artifacts only; humans decide.

Anchored to: FFIEC BSA/AML Examination Manual, Customer Due Diligence section (covers ongoing CDD and adverse-information escalation expectations) [verify section anchor]; FinCEN CDD Final Rule (May 2016, effective May 11, 2018) — ongoing-monitoring pillar covers material customer-information updates including adverse media; OCC, FRB, FDIC, NCUA Joint Statement on Risk-Focused BSA/AML Supervision (July 22, 2021); Wolfsberg Group guidance on negative news / adverse media (public industry standard reference, dated as-of) [verify].

## Source anchors

- FFIEC BSA/AML Examination Manual — Customer Due Diligence section: https://bsaaml.ffiec.gov/manual/AssessingComplianceWithBSARegulatoryRequirements/02 [verify section anchor for adverse-information handling].
- FFIEC BSA/AML Examination Manual — index and applicable EDD-related sections (PEP, private banking, correspondent) where adverse media is a contextual driver [verify section anchors].
- FinCEN CDD Final Rule (81 FR 29397, May 11, 2016; compliance May 11, 2018) — fourth pillar (ongoing monitoring) implies adverse-information assessment as part of risk-based information updates.
- OCC, FRB, FDIC, NCUA Joint Statement on Risk-Focused BSA/AML Supervision, July 22, 2021.
- Wolfsberg Group guidance on adverse media / negative news (most recent public version) [verify date] — public industry standard, not a regulator anchor.
- Public FinCEN advisories that frame typologies (e.g., elder financial exploitation, human trafficking, real estate, ransomware) — used as typology references when triaging the materiality of a hit [verify advisory dates as cited].

## Sector overlays needed

- `references/sector-overlays/banking.md` — adverse-media drivers for banking (commercial customer fraud allegations, regulatory enforcement against the customer, indictments of customer principals); cash-intensive business linkage.
- `references/sector-overlays/payments-fintech.md` — fintech customer-base adverse-media patterns (payment-processor enforcement, marketplace seller fraud reporting, BIN sponsor exposures).
- `references/sector-overlays/capital-markets.md` — broker-dealer client adverse media (insider-trading allegations, market-manipulation enforcement, microcap promoter exposure).
- `references/sector-overlays/insurance.md` — covered-products customer adverse media (fraud-ring patterns, premium-financing irregularities); narrow scope.

## Cross-cutting overlays

None at v1. Conduct overlap exists for retail-customer harm patterns but is best handled inside the EDD pack rather than at hit-triage stage. Cyber overlap (account-takeover-adjacent adverse media) is captured in typology references, not as a separate cross-cutting overlay.

## Output template named sections

1. Customer / entity identifier and triage scope (onboarding, refresh, event-driven, bulk re-scan)
2. Hit set summary (count by source class, date range, vendor or open-source basis)
3. Per-hit assessment
   a. Hit identifier and headline summary
   b. Identity confidence (subject = customer, with rationale)
   c. Source reliability tier (tier-1 regulator/court/major outlet; tier-2 secondary; tier-3 unverified)
   d. Recency and currency (date of underlying event vs. publication date)
   e. Materiality to financial-crime risk (typology link)
   f. Linkage strength (direct involvement, association, mention only)
   g. Disposition (relevant; not relevant; unverified pending)
4. Aggregated triage findings (themes across hits)
5. Downstream-action recommendations (no further action; route to cdd-risk-review refresh; route to edd-escalation-pack; route to sar-decision-qa support; route to sanctions-screening re-check)
6. Open questions and evidence-needed items
7. Source trace and confidence label (date-as-of)

## Structured output fields

| Field | Type | Purpose |
|---|---|---|
| `subject_id` | string | Customer / entity identifier (placeholder for sample). |
| `triage_scope` | enum | `onboarding`, `periodic_refresh`, `event_driven`, `bulk_rescan`. |
| `hit_set_summary` | object | Sub-fields: total_hits, by_source_class, date_range, vendor_or_open_source. |
| `per_hit` | array of objects | hit_id, headline, identity_confidence (`high`, `medium`, `low`, `unverified`), source_tier (`tier_1`, `tier_2`, `tier_3`), event_date, publication_date, materiality (`material`, `borderline`, `not_material`), linkage_strength (`direct`, `association`, `mention_only`), typology_tags (array), disposition. |
| `aggregated_themes` | array of strings | Cross-hit themes (e.g., recurring counterparty, recurring jurisdiction, escalating timeline). |
| `downstream_actions` | array of objects | Action, target_skill, rationale. |
| `open_questions` | array of strings | Each tagged with target skill or owner. |
| `source_trace` | array of objects | Claim, source, date_as_of, confidence label. |

## Example scenarios (public-source-derived, anonymous)

1. Mid-size US bank, periodic refresh adverse-media re-scan on a commercial customer (legal entity). Hit set returns 42 hits across vendor and open-source feeds. Triage finds: 28 hits are common-name false matches (low identity confidence); 8 hits are tier-3 forum content with no clear sourcing (excluded); 4 hits are tier-1 regulator press releases referencing a different entity with a similar name (excluded after entity-disambiguation against beneficial ownership chain); 2 hits are tier-1 court filings naming a principal of the customer in a civil fraud matter dated within the last 12 months. Anchored to: FFIEC manual CDD section ongoing-monitoring expectations; Wolfsberg adverse-media guidance on identity-confidence and source-reliability tiers. Aggregated themes: principal-level adverse media, civil (not criminal), recent. Downstream actions: route to cdd-risk-review refresh; route to edd-escalation-pack with PEP-adjacency check (principal's other public roles).

2. Community bank, event-driven triage on an individual customer following a tier-1 newspaper report on a regional fraud-ring indictment in which the customer's name appears as a co-defendant. Single hit, tier-1 source, identity confidence high (jurisdiction, age, occupation match against CDD file). Public criteria: FFIEC manual; FinCEN CDD ongoing-monitoring pillar; FinCEN advisory on the typology if applicable [verify advisory if used]. Triage finds: hit is material; linkage direct; typology tag (fraud-ring). Downstream actions: route to sar-decision-qa support for any in-flight or recent alerts on this customer; route to edd-escalation-pack if the customer profile is not already in EDD; flag relationship-level review gate. Skill stops short of recommending exit, rating change, or filing.

## Common pitfalls

1. Identity confidence assumed because the hit's subject name matches the customer name. Common-name false matches dominate bulk re-scan output. Mitigation: per-hit identity_confidence field forces a rationale.
2. Source reliability tier collapsed into "vendor said it is reliable". Mitigation: tier system anchored to source class (regulator/court/major outlet vs. secondary vs. unverified) rather than vendor self-tagging.
3. Recency reported as publication date, ignoring underlying event date. A 2017 event re-published in 2026 is a 2017 event. Mitigation: separate event_date and publication_date fields.
4. Materiality assessed against a generic "negative news = bad" frame rather than financial-crime typology link. Mitigation: typology_tags field forces a typology link or a "no clear typology" tag.
5. Aggregated themes skipped. Per-hit triage misses the pattern across hits (recurring counterparty, escalating timeline). Mitigation: aggregated_themes is a required section.
6. Reviewer drifts toward an exit recommendation or rating change. Skill routes hits to downstream review artifacts; humans decide rating, EDD, SAR, exit.
7. Date-as-of missing on the triage artifact. Adverse-media findings are perishable; downstream skills need the date to assess currency.
