# Privacy cross-cutting overlay — control-sampling

Loaded when `engagement-scope.cross_cutting_overlay_set` includes `privacy`, when the test addresses GLBA Safeguards Rule controls, HIPAA Security Rule controls (where applicable to the entity), or other consumer-financial-information safeguards. Supplements `references/source-anchors.md`.

## Population definition conventions for privacy-relevant sampling

Privacy-relevant sampling carries population conventions that overlap with cyber-control sampling but with distinct emphases:

- **Populations are data-handling events, access events, or safeguards-program tests.** Customer-information access events in the period; data-flow inventory entries during the period; safeguards-program test events run during the period; vendor data-handling assessments completed in the period.
- **Consumer-financial-information populations carry data-classification stratification.** Restricted, confidential, internal, public; or the firm's equivalent classification scheme. Sampling concentrates on the highest-sensitivity classes.
- **Vendor-data-handling populations follow third-party risk management scope.** The population is vendors handling consumer financial information during the period; sampling stratifies by data sensitivity, vendor tier, and assessment recency.

## Privacy-supervisory anchors (load by reference; do not restate)

- **GLBA Safeguards Rule, 16 CFR Part 314 as amended** (FTC, December 2021 amendments effective 2023). §314.4 elements of an information security program, including §314.4(d) regular monitoring and testing of safeguards effectiveness, §314.4(e) implementation of safeguards, §314.4(f) overseeing service providers [verify subsection labels]. https://www.ecfr.gov/current/title-16/chapter-I/subchapter-C/part-314 .
- **GLBA Privacy Rule, 12 CFR Part 1016 (CFPB Reg P)** [verify subsection labels for the privacy-notice and opt-out testing populations]. https://www.ecfr.gov/current/title-12/chapter-X/part-1016 .
- **HIPAA Security Rule (45 CFR Parts 160, 164 Subpart C)** §164.308(a)(8) periodic technical and nontechnical evaluation; §164.312 technical safeguards (access control, audit controls, integrity, transmission security) [verify subsection labels]. Applicable to financial-services entities only when they are a HIPAA Covered Entity or Business Associate (e.g., a health-insurance arm; a benefits-administration affiliate). https://www.hhs.gov/hipaa/for-professionals/security/laws-regulations/index.html .
- **State data-privacy laws (CPRA, VCDPA, CPA, CTDPA, UCPA, etc.)** [verify state-by-state coverage and effective dates]. Applicable when the firm processes resident data above the law's threshold; sampling memos for state-privacy testing populations cite the state statute and the firm's adopted-applicability assessment.
- **FFIEC Information Technology Examination Handbook — Information Security booklet** [verify current edition and section]. The IT-control-testing baseline for federally-supervised banks, including data-protection controls. https://ithandbook.ffiec.gov/it-booklets/information-security.aspx [verify URL].

## Privacy-control-area sampling notes

### Safeguards-program sampling (16 CFR §314.4(d)-relevant)

- Sampling conventions: safeguards-program testing pulls test-events run during the period (penetration tests, vulnerability assessments, continuous-monitoring outputs). The population is the firm's safeguards-program testing inventory; stratification by safeguards-program element (access controls, encryption, monitoring, incident response, training). Annual or periodic-risk-assessment evidence is itself a population for sampling.

### Access-control sampling (privacy frame)

- Sampling conventions: privacy-relevant access-control sampling overlaps with the cyber overlay's IAM sampling but adds data-classification stratification. The population is access events to consumer-financial-information assets; sampling stratifies by data classification and access type (read, write, export, transmit). Audit-control sampling reads logging coverage against the data-classification register.

### Service-provider oversight sampling (16 CFR §314.4(f)-relevant)

- Sampling conventions: vendor-oversight testing pulls vendors handling consumer financial information during the period with stratification by data sensitivity, vendor tier, and assessment recency. The population is vendor relationships in scope; sampling tests due-diligence evidence, contract-clause coverage, and ongoing-monitoring evidence per the firm's TPRM program.

### Privacy-notice and opt-out sampling (Reg P-relevant)

- Sampling conventions: privacy-notice testing samples notice-delivery events with stratification by channel and product. Opt-out testing samples opt-out elections received during the period with stratification by channel and product, and tests opt-out propagation across affiliated systems.

### State-privacy-law sampling (where applicable)

- Sampling conventions: state-privacy-law sampling pulls consumer-rights requests received during the period (right to know, right to delete, right to correct, right to opt-out of sale or sharing) with stratification by request type, requestor state, and resolution status. Per-state stratification matters because state-by-state variance in clocks and exemptions drives the operative criterion.

## Customer-financial-information classification in stratification

When the privacy overlay is loaded, the data-classification scheme drives stratification:

- Population items are mapped to the firm's data-classification scheme; sampling concentrates on restricted-and-confidential classes per firm methodology.
- Where the firm has not formalised a data-classification scheme, the memo names the gap and uses a coarser stratification (consumer-vs-business, PII-handling-vs-not) with the limitation flagged.

## Audience and tone

A sampling memo drafted for the firm's CISO or Chief Privacy Officer reads heavier on the data-classification stratification rationale and the safeguards-program testing inventory. A memo drafted with an upcoming FTC or state-AG inquiry in mind reads heavier on the §314.4 element citations and the vendor-oversight populations. A memo drafted for state-privacy-law compliance reads heavier on per-state stratification and the consumer-rights-request populations.
