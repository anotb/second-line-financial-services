# Troubleshooting: ai-act-triage

Recurring failure modes when an AI Act triage looks finished but is not. The reviewer pass should catch these; the triage pass should preempt them.

## The triage skips the row-by-row Annex III walk and asserts a conclusion

Symptom: the artifact lands at "not high-risk" or "high-risk" with one sentence of reasoning. No row-by-row walk of Annex III. No record of the screen running for rows that did not apply.

Why it happens: the answer feels obvious from the use-case description, so the practitioner skips the audit trail.

Fix: every Annex III row is recorded as applies / does not apply, with one-line reasoning. The artifact is auditable. A reviewer reading the triage in two years should see the screen ran. The Article 5 prohibited-practice screen carries the same expectation: each sub-practice screened on the record, including the ones that obviously do not apply.

## Operator role conflated to a single label

Symptom: the triage says "the firm is the deployer" without naming what the vendor is, or names the firm as "user" without distinguishing provider, deployer, importer, distributor, or authorised representative under Article 3.

Why it happens: the practitioner imports a generic vendor-management vocabulary instead of the AI Act's role definitions.

Fix: enumerate every operator role for every entity in the chain. A US parent with an EU subsidiary deploying a vendor-built system involves at least three actors and frequently picks up multiple roles per entity (e.g., a firm that fine-tunes a vendor model becomes a provider for the fine-tuned variant under Article 25). The schema field `operator_roles` is array-typed for a reason.

## Article 27 FRIA collapsed into the GDPR DPIA

Symptom: the artifact claims FRIA coverage by reference to the existing DPIA, with no FRIA-vs-DPIA reconciliation note.

Why it happens: practitioner pattern-matches "impact assessment" to the most familiar instrument.

Fix: the FRIA covers fundamental-rights elements (impact on affected persons' rights, mitigation measures, governance arrangement, complaints handling) that the DPIA does not. Article 27 is in addition to GDPR, not in lieu of. The triage carries an explicit reconciliation note when both are in scope; legal review on the reconciliation, not just the FRIA.

## Article 50 transparency screened as one obligation

Symptom: the triage records "Article 50 applies" or "Article 50 does not apply" without screening each sub-obligation (50(1) AI-interaction disclosure, 50(2) synthetic-content marking, 50(3) deepfake disclosure, 50(4) public-interest text marking, 50(5) emotion recognition / biometric categorisation disclosure).

Why it happens: Article 50 is treated as a binary rather than as a multi-part screen.

Fix: each sub-obligation is screened individually. A GenAI assistant that drafts customer responses fires 50(1) and 50(2); it does not fire 50(3) or 50(5). Recording each on the record both removes the gap and tells the reviewer what disclosure language is needed where.

## GPAI obligations attached to the deployer

Symptom: the triage attaches Articles 51 to 55 obligations to the deploying firm because the firm uses a vendor LLM.

Why it happens: the practitioner reads "general-purpose AI model" and attaches every related obligation to the firm without distinguishing model-provider obligations from system-provider and deployer obligations.

Fix: GPAI obligations under Articles 51 to 55 attach to the model provider. A firm that deploys a vendor LLM-backed system is the deployer of the system; the deployer's obligations are Article 26 (when the system is high-risk) and Article 50 (when the limited-risk obligations apply), not the GPAI provider obligations. The triage records the vendor's GPAI status as deployer-side evidence (training-data summary per Article 53(1)(d), copyright posture, Code of Practice signature status) without attaching the obligations themselves to the firm. When the firm fine-tunes or substantially modifies the model, Article 25 may flip the firm into a provider role; that is a separate analysis.

## Phasing dates ignored or misread

Symptom: the triage names the classification but not the applicable date, or asserts an obligation as currently binding when the Article 113 phasing places it in the future, or the reverse.

Why it happens: practitioner reads the obligation list and does not consult Article 113.

Fix: every obligation in the obligations summary carries its applicable date per Article 113. The schema field `applicable_date` is required. Common phasing landmarks: prohibited-practices applicable from 2 February 2025; GPAI obligations on providers applicable from 2 August 2025; high-risk and Article 50 transparency obligations applicable from 2 August 2026; the high-risk obligations for AI systems falling under Annex I product-safety legislation applicable from 2 August 2027. Confirm against Article 113 at write time; phasing for member-state implementations and AI Office secondary instruments may shift specific items.

## Article 6(3) derogation invoked without analysis

Symptom: the triage records "Article 6(3) derogation applies" or asserts the system is not high-risk under the derogation, with no analysis of which limb of 6(3) is invoked.

Why it happens: the derogation looks like a release valve from high-risk classification, and the practitioner reaches for it.

Fix: Article 6(3) has four narrow limbs (narrow procedural task, improving previously completed human activity, detecting decision-making patterns or deviations, preparatory task). The triage records which limb is invoked and the basis. For pricing, underwriting, and creditworthiness use cases, the derogation is rarely available because the system materially influences the outcome. Profiling of natural persons disqualifies the derogation under 6(3) regardless of which limb is named. When the derogation is invoked, route to legal for sign-off.

## Member-state implementations skipped

Symptom: the triage cites the Regulation only and does not consider member-state implementing measures, national competent authority designations, or member-state deviations on permitted enforcement.

Why it happens: the Regulation is the headline source; the implementing landscape is patchy and changes by state.

Fix: when the scope names a member state of operation, cross-walk to the implementing measure (where designated and where in force at write time). The triage records the state and the implementation status; where the implementation is in transposition or under consultation, the triage records that posture and routes to legal. Do not assert a member-state-specific obligation without confirming the implementation status.

## Sector overlay loaded but ignored

Symptom: insurance pricing triage reads in generic Annex III(5)(c) reasoning but never names ECDIS provenance, NAIC AIS Program reconciliation, or state DOI bulletins. Banking creditworthiness triage names Annex III(5)(b) but never names CRR/CRD model-risk overlap or the OCC large-bank Heightened Standards reach. Capital-markets vendor-LLM triage cites Article 50 but never names the Marketing Rule reach or books-and-records exposure.

Why it happens: the sector overlay file exists in references/ but the triage author treated it as background.

Fix: when the scope names a sector, the matching `references/sector-overlays/<sector>.md` content lands as named items in the triage artifact. The reviewer challenges any sector-flagged engagement that produces an artifact with no sector content.

## The triage drifts into legal advice

Symptom: the artifact says "the firm must ..." or "the firm is required to ..." in language that reads as a binding legal interpretation rather than as a triage decision routed to legal for confirmation.

Why it happens: practitioner voice slips into legal voice when the conclusion feels clear.

Fix: the triage is a draft for legal and compliance review. Practitioner voice records the classification, the article references, and the obligations the firm picks up at that classification. Final legal interpretation, especially on Article 5 prohibition reach, Article 6(3) derogation, Article 27 FRIA-vs-DPIA reconciliation, and member-state implementing measures, is for legal counsel. The artifact stops at draft; the SKILL.md non-negotiable on the human-review gate carries the practice rigidly.

## Source trace omits AI Office and Code of Practice references

Symptom: the triage cites the Regulation and stops there. AI Office Q&A and the Code of Practice on General-Purpose AI are absent, even where the firm has elected to track them.

Why it happens: practitioner treats only the Regulation as authoritative and ignores soft-law sources.

Fix: AI Office guidance and the Code of Practice are not binding interpretations and the triage should not cite them as such. They are useful for tracking enforcement posture and vendor-evidence framing. The source trace records them with the soft-law label so the reviewer sees the firm's monitoring posture; do not collapse soft-law references into the same line as Regulation citations.

## Re-classification triggers missing

Symptom: the triage lands a classification and stops, with no statement of what would re-open it.

Why it happens: the triage is treated as a one-time decision rather than as a living artifact tied to the use case.

Fix: every triage records re-classification triggers (architecture change, scope change, EU-footprint change, AI Office guidance update, member-state implementation update, vendor change-of-version where relevant). Owner and frequency are named. The triage is owned and refreshed; the spec sheet's `applicable_date` is one anchor for refresh cadence.
