# Troubleshooting: board-ai-risk-pack

Recurring defects observed when this skill is used in practice. Each defect names the failure mode and the corrective pattern.

## The pack reads as a catalogue dump

The committee opens to page nine and reads the inventory list instead of the executive summary. The decision items go missed. The chair leaves the meeting frustrated.

Corrective: the executive summary is up-to-five bullets at most and the rest of the pack is curated, not exhaustive. The inventory list is in `ai-use-case-intake` outputs; this pack carries summary counts and movement, not the catalogue. If the pack runs longer than a quarterly committee can read in a thirty-minute pre-read, the pack has inverted what belongs in the body and what belongs in the appendix.

## Top risks repeats across packs without movement

The same five risks appear pack after pack with "stable" trajectory and no underlying movement. The committee stops engaging with the section because nothing changes. New risks land late because no one wants to retire an existing one to make room.

Corrective: trajectory is a four-value enum (improving, stable, worsening, new) with a required one-line basis on each entry. "Stable" without basis is the wallpaper failure mode. New risks land with `new` flag and `logged_date`. Risks that have been stable for four cycles with no underlying movement are candidates for retirement to the watch list rather than the top-risks section.

## Incidents reported with no near-misses section

The pack lists incidents as resolved. The committee gets a false sense of security. Two cycles later, a near-miss that was not surfaced becomes an incident, and the chair asks why the committee did not see it earlier.

Corrective: near-misses are a separate sub-section under incidents, required every cycle. If the period had no near-misses, state that explicitly with one line on what was checked. An empty near-miss section without statement triggers the standing reviewer question on detection coverage.

## Foundation-model vendor concentration is buried

The committee does not see that the firm has 80% of GenAI use cases on a single foundation-model provider until the provider issues a deprecation notice or has a security incident. The concentration risk lands as a fire drill, not an oversight finding.

Corrective: foundation-model concentration is a required section with a top-three concentration ratio. The firm threshold is named (or the absence of a threshold is itself flagged as a sign-off question). Watch list entries for concentrated providers carry the named concern. The version-change posture is reported by vendor.

## Decisions requested are vague or missing

The decisions section says "note the report" or is empty. The committee meeting closes with no decisions taken. The pack functions as a status update masquerading as a committee instrument.

Corrective: decisions requested entries have options and a recommended motion. "Note the report" is not a decision. If nothing requires committee action this cycle, surface that explicitly so the chair can decide whether to call the meeting; the pack does not pretend a status update is a committee instrument.

## Sector overlay loaded but not reflected in the pack body

The engagement scope flags insurance, the insurance overlay loads, and the pack body is generic. The NAIC AIS Program elements are not addressed. The state DOI inquiry inventory is missing. The reviewer flags the gap on first read.

Corrective: overlays are content that lands in the pack body, not background reading. Insurance overlay implies AIS Program element narrative in the maturity section, state DOI inquiry inventory in the regulator interactions section, NAIC #880 / NYDFS Circular Letter / CO SB 21-169 framing in the top risks section as applicable. Same pattern for banking, capital-markets, payments-fintech.

## Cyber overlay loaded but only AI-enabled threats called out

The cyber overlay treats deepfakes and AI-aided phishing as the cyber-AI section and ignores the firm's own use of AI as cyber surface. Prompt-injection signal is not surfaced. The vendor cyber posture is not reported. The NYDFS October 2024 Industry Letter framing is not reflected.

Corrective: cyber-AI risk is two buckets: AI-enabled threats targeting the firm, and the firm's own use of AI as cyber surface (prompt injection, data exposure through GenAI outputs, vendor concentration on AI providers). Both are reflected in top risks and incidents where elevated. The GenAI program status section carries the prompt-injection signal trend as a standing line.

## Conduct overlay reduces to "fairness testing happened"

The pack reports that fairness testing ran for the quarter and the disparity ratios were within thresholds. The complaint-rate drift is not reported. The adverse-action notice quality posture is not surfaced. The customer-facing GenAI accuracy and harm posture is not addressed.

Corrective: conduct-AI risk is broader than fairness testing. Adverse-action notice posture for credit decisioning AI, complaint-rate drift on AI-touched products, claims-handling AI fairness and accuracy, customer-facing GenAI accuracy and harm are all in scope where the firm has the relevant exposure. The conduct overlay sets which of these surface.

## Inventory state count not reconciled to the inventory of record

The pack reports 47 in-production use cases. The system of record reports 51. The discrepancy is not surfaced. Three months later, an OCC continuous-monitoring letter cites the discrepancy as an inventory completeness finding.

Corrective: inventory reconciliation status is a required field on the inventory state section (reconciled, partial, not-reconciled). If partial or not-reconciled, the data confidence label cannot be high; the gap is named in the AI inventory completeness statement appendix; and the gap routes to the engagement issue log if not already an open MRA.

## "Continuing to monitor the regulatory landscape"

The forward-look section recycles generic regulatory-horizon language pack after pack. The committee learns nothing actionable. The named items the committee can act on are missing.

Corrective: forward look is named, dated, regulator-anchored. Two cycles ahead is the standard horizon. Items: regulator developments expected (rule, date, implication), use cases on the runway for tier escalation or pre-prod gate, GenAI deployments on the runway for production, foundation-model vendor changes expected, validation cycles due, training and capability program milestones. "Continuing to monitor the landscape" fails the section.

## AI governance maturity posture is one paragraph of marketing copy

The maturity section reads like a vendor pitch: "robust governance framework", "comprehensive AI program", "aligned to leading practice". Nothing the committee can challenge. Nothing that names the gaps.

Corrective: maturity narrative is calibrated to the named framework (NIST AI RMF, NAIC AIS Program, ISO/IEC 42001, EU AI Act deployer, firm-bespoke, blended). Each named framework dimension is addressed with current posture and named gaps. For insurers the AIS Program element-by-element narrative is the standing pattern; for federally regulated banks the NIST Govern function plus SR 11-7 §III posture is the standing pattern; for ISO/IEC 42001 firms the §5.1 / §6.2 / §9.3 posture is the standing pattern.

## Pack overlaps with the enterprise risk committee pack

The board AI risk pack and the enterprise risk committee pack both anchor the AI sources, both report the AI inventory state, both list AI top risks. Two committees see two versions of the same content with the same depth. Neither committee gets the right pack for its audience.

Corrective: the board AI risk pack is the AI committee instrument, anchored to AI sources at AI committee depth. The enterprise risk committee pack consumes a brief from this pack for the AI heat-map cell and any AI-driven top-risks entry rather than re-anchoring the AI sources. The AI committee pack does not re-anchor enterprise risk sources (BCBS 239 framing on AI inventory aggregation is the one cross-cutting anchor that lives in both for a different reason).

## Sign-off block names individuals instead of roles

The pack lists named individuals in the sign-off block. The pack ages and the named individuals leave or change roles. The audit trail is degraded.

Corrective: sign-off block names roles, not individuals. The system of record carries the named individual against the role at the time of sign-off. This is the same standing rule as the model card and the enterprise risk committee pack.
