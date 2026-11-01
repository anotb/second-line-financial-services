# Troubleshooting: ai-risk-tiering

Recurring failure modes when a tier decision looks complete but is not. The decider attestation should catch these; the rubric pass should preempt them.

## The rubric collapses to a single dominant factor

Symptom: every factor scored, but only `customer_impact` carries the rationale. Cyber, conduct, vendor-dependence, and concentration are scored `low` or `n/a` without justification. The tier rationale reads as a one-factor argument.

Why it happens: customer impact is the easiest factor to assess and the loudest. The other factors require pulling on threads (vendor evidence, concentration analysis, NYDFS exposure) that take longer to investigate.

Fix: require all named factors to be scored, with `n/a` justified, not blank. The decider attestation block does not pass when more than one factor is unjustifiably `n/a`. The schema enforces it; the reviewer reads it.

## Tier inflation or deflation by sponsor pressure

Symptom: the sponsor wants a lower tier to skip validation depth, or a higher tier to look serious. The tier matches the sponsor's proposal without dissent recorded; the rationale leans on factors that were not the actual driver.

Why it happens: the tier decision reads as a negotiation instead of a defended judgement. Common when the model risk team and the sponsor sit close together; less common when second-line owns the artefact.

Fix: dissent field is required when tier disagrees with sponsor proposal. AI risk committee secretary signs the dissent line at tier-1 and tier-2; the second-line reviewer signs at tier-3 and tier-4. An empty dissent block is fine; an inflated tier without a defending rationale is not.

## Re-tiering triggers are dates instead of events

Symptom: the re-tiering trigger block reads "annual review" or "Q4 reassessment" as the only entries. The use case grows beyond its tier between review dates without anyone noticing.

Why it happens: annual review feels like the safe default; named events take more thought to enumerate.

Fix: each re-tiering trigger names an event with a monitoring owner and a detection method. Dates are refresh cadences, not triggers. Sector-overlay re-tiering triggers are loaded from the matching overlay file; cross-cutting overlay triggers from the cross-cutting file. Empty or date-only trigger blocks fail the decider attestation.

## GenAI factor block is missing on a GenAI use case

Symptom: tier rubric uses pre-GenAI factor language; foundation-model dependence, RAG corpus drift, prompt-injection exposure, autonomy uplift via tool use are all absent or all `n/a` without justification.

Why it happens: the rubric was built for traditional ML; the GenAI fields look optional and the decider ticks the boxes that exist. Common at first-tier-on-GenAI-use-case stage; less common after the firm has tiered a few.

Fix: when the use case is GenAI (foundation model, RAG, or tools), the GenAI overlay block fires. Reference NIST AI 600-1 Map 1.1 and Measure 2.6 in the rubric explicitly. The schema's `genai_specific` factor is required to be scored; the source trace points at the vendor system card and the firm-side evaluation evidence separately.

## Tier-1 set by reflex for anything customer-facing

Symptom: every customer-facing use case is tier-1; tier-1 becomes the default and loses meaning. Validation depth, monitoring frequency, and committee path get applied uniformly across the inventory; the firm spends tier-1 resources on tier-3 use cases.

Why it happens: tier-1 feels safe; the cost of over-tiering is hidden (everyone's time) while the cost of under-tiering is loud (an exam finding).

Fix: tier-1 is reserved for customer-binding decisions or material financial impact; the rationale names the threshold. Customer-facing alone is not a tier-1 trigger; an internal-use GenAI assistant is not tier-1 even if it interacts with customer-data inputs. The decider attestation challenges any tier-1 designation that does not pass the named-threshold test.

## AI Act overlap is set to true reflexively or missed entirely

Symptom: every use case is routed to `ai-act-triage` regardless of EU footprint, or no use case is routed even when a US adviser serves EU professional clients.

Why it happens: the AI Act is unfamiliar to US-only practitioners, who either over-route as a hedge or under-route from absence of EU client volume.

Fix: the `ai_act_category` factor records the category-by-category Annex III check, not a single yes/no. EU footprint includes EU establishment, EU customer base, EU client base for an adviser, or EU branch reinsurance; the rubric flags the routing trigger when any of those is in scope. Where US-only and no EU exposure, the factor records `n/a` with footprint as the rationale and a re-tiering trigger if footprint changes.

## Sector overlay loaded but ignored

Symptom: insurance pricing model tiered without NAIC #880 unfair-discrimination framing; banking AML model tiered without FFIEC manual exposure; capital-markets surveillance model tiered without Rule 15c3-5 overlap; payments-fintech AI tiered without sponsor-bank reach.

Why it happens: the sector overlay file exists in `references/sector-overlays/` but the decider treated it as background reading.

Fix: when the scope names a sector, the matching overlay's elevation factors and triggered gates land in the tier decision. Sign-off questions probe the sector items. If the overlay is loaded but the tier decision has no overlay-specific content, the loader did not run; rerun with the overlay reference in scope.

## Cross-cutting overlay (cyber, privacy, conduct) is collapsed into the capability rubric

Symptom: cyber exposure scored `low` because "no customer-facing surface", missing the tool-use uplift; privacy scored against training data only, missing the prompt surface; conduct scored only on direct customer impact, missing the indirect path through analyst recommendations or marketing material.

Why it happens: the capability rubric has cyber, data sensitivity, and conduct as named factors; the cross-cutting overlay reads as duplicative.

Fix: the cross-cutting overlay tells the rubric what counts as high, medium, low for the named factor. Cyber, privacy, and conduct are scored once; the overlay is the scoring guide. Where the overlay is loaded but the score reads as if the overlay were absent, the decider re-reads the overlay and re-scores.

## Vendor-dependence scored against contract, not against operational reality

Symptom: vendor-dependence scored `low` because "version pinning is in the contract"; in operational reality the vendor swaps the underlying model with a notice period the firm cannot meet, or pinning applies to the API endpoint but not to the model behaviour.

Why it happens: the contract is the easiest evidence; operational evidence (vendor change-of-version notice posture, pinning verification) requires asking the vendor and reading the notice channel.

Fix: vendor-dependence scoring reads the operational posture, not just the contract. Version pinning in contract without an audited notice channel reads as medium dependence, not low. Vendor-supplied adversarial-test results (vendor self-attestation) read as medium evidence at most; firm-independent evaluation reads as higher confidence. The source trace records both separately.

## Tier and gates do not match firm policy

Symptom: tier-1 with no AI risk committee approval gate; tier-3 with full validation gate; tier-4 with quarterly monitoring. The default tier-to-gate mapping in the template is treated as advisory and overridden without rationale.

Why it happens: the firm's policy defines the mapping; the template's defaults are illustrative and the decider conflated the two.

Fix: where firm policy supplies the tier-to-gate mapping in `references/firm-overlay.md`, the firm policy wins and the template's defaults yield. Where firm policy does not yet exist, the template's defaults are the starting point and any deviation requires rationale in the dissent block. The tier-to-gate mapping is policy, not judgement.

## Source trace omits the regulatory citation

Symptom: tier-1 designation citing "ECOA reach" or "FFIEC manual exposure" without a section reference or link. The decider's reading of the regulation is on the table; the regulatory citation is not.

Why it happens: the citations live in `references/source-anchors.md` and the decider treated the rationale text as self-supporting.

Fix: every regulatory claim in the tier rationale carries a source-anchor pointer. The source trace block enforces the discipline. Where the citation carries `[verify section]`, the flag carries forward into the tier decision; do not invent.

## Re-tiering trigger ownership is left unassigned

Symptom: triggers named with detection methods but no owner; or owner listed as "TBD" or as a named individual.

Why it happens: triggers cross functions (vendor management owns vendor change-of-version notice, regulatory change owns horizon scan, AI governance owns scope changes), and the decider leaves the owner blank rather than chasing across functions.

Fix: each trigger names a function as owner, never a named individual. Where the owner spans functions (vendor management with CISO function, for example), both functions are named. Triggers without owners fail the decider attestation; chasing the owner across functions is part of the work.

## ORSA materiality (insurance) or stress-testing inclusion (banking) is missed

Symptom: insurance use case tiered as tier-2 with ORSA materiality un-checked; banking use case tiered without CCAR/DFAST pedigree where the model is in fact in scope.

Why it happens: ORSA and CCAR/DFAST owners sit elsewhere in the firm; the tier decider does not have the inventory in front of them.

Fix: insurance tier decisions check ORSA-materiality-thresh; banking tier decisions check stress-testing-inscope. Both are sector-overlay-loaded and required to be scored. Where the answer is unknown at tier-decision time, the open-questions block carries the item with a named owner and a due date before pre-prod gate.
