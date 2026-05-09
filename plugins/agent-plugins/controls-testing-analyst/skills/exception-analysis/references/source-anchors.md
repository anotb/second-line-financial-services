# Source anchors: exception-analysis

This file holds the named, dated regulatory and professional-standard sources the exception-analysis skill anchors to. The SKILL.md body uses generic workflow language and cites this file by path; named citations live here, not in the activation-tuned description. Firm-specific anchors (severity ladder, named committee gates, policy-floor overrides) belong in `references/firm-overlay.md`.

`[verify section]` placeholders mark anchors where the precise section reference still needs verification against the current edition of the source. They are deliberate, not omissions.

## Internal-audit communication-of-results and root-cause analysis

### IIA International Professional Practices Framework, Global Internal Audit Standards (effective January 2025)

Anchor: Standards covering communication of engagement results and the underlying methodology bar for root-cause analysis. Standard 14 (Communicating Results) and the related conformance requirements on criteria, condition, cause, and effect; the IPPF supplemental guidance on root-cause analysis. [verify section labels under the current 2025 IIA standard set; superseded the prior 2400 / 2410 numbering used in the 2017 IPPF where Standard 2410 set the criteria-for-communicating bar.]

What this skill relies on: the requirement that every finding has a documented criterion, condition, cause, and effect; and that root-cause analysis is part of the engagement methodology rather than an optional follow-up.

Link: https://www.theiia.org/en/standards/

## Audit sampling and evaluation of sample results

### AICPA AU-C 530, Audit Sampling

Anchor: AU-C 530, paragraphs covering the evaluation of sample results, including the projection of misstatements or deviations to the population and the treatment of anomalies. [verify exact paragraph references — .A18 through .A22 in the current edition for the anomaly / systemic distinction.]

What this skill relies on: the methodology bar on projecting deviations to the population (default systemic, downgrade to anomaly only with positive evidence the deviation does not recur) and on distinguishing observed deviation rate from tolerable deviation rate as the read against which classification and severity are measured. Second-line testing borrows the methodology even when the engagement is not a financial-statement audit.

Link: https://us.aicpa.org/research/standards/auditattest/clarifiedsas

## Severity calibration for internal control matters

### AICPA AU-C 265, Communicating Internal Control Related Matters Identified in an Audit

Anchor: AU-C 265 paragraphs framing the deficiency / significant deficiency / material weakness severity hierarchy for internal control matters. [verify paragraph references — .07 through .11 in the current edition cover the severity definitions.]

What this skill relies on: the severity-framing methodology second-line testing borrows when calibrating low / medium / high / critical against the underlying deviation. Not a direct legal standard for second-line testing; the methodology is what carries.

Link: https://us.aicpa.org/research/standards/auditattest/clarifiedsas

## Supervisory expectations on issue identification

### Federal Reserve SR 08-8 / SR 08-8 Attachment — Compliance Risk Management Programs and Oversight at Large Banking Organizations with Complex Compliance Profiles (October 16, 2008)

Anchor: SR 08-8 sections on issue identification, escalation, and tracking expectations within a compliance risk management program. [verify section labels.]

What this skill relies on: program-level expectations that compliance-testing exceptions are identified, classified, escalated, and tracked through to closure; the register this skill produces is the artifact those expectations key off.

Link: https://www.federalreserve.gov/boarddocs/srletters/2008/sr0808.htm

### OCC Comptroller's Handbook on Compliance Management Systems

Anchor: OCC Comptroller's Handbook, Compliance Management Systems booklet. Sections covering exception identification, root-cause analysis, and corrective-action expectations within the CMS framework. [verify booklet edition and section labels; the OCC has revised the CMS-related guidance over time.]

What this skill relies on: the supervisory expectation that exceptions surfaced through compliance-testing are classified by root cause and tracked to corrective action.

Link: https://www.occ.gov/publications-and-resources/publications/comptrollers-handbook/

### CFPB Compliance Management System Review Procedures

Anchor: CFPB CMS Review Procedures, monitoring and corrective-action sections. [verify section labels in the current edition.]

What this skill relies on: the expectation that compliance-testing exceptions are evaluated for root cause and that corrective-action plans address the cause rather than the symptom.

Link: https://files.consumerfinance.gov/f/documents/cfpb_supervision-and-examination-manual.pdf

## Internal control framework

### COSO 2013 Internal Control — Integrated Framework, Principle 17 (Evaluates and Communicates Deficiencies)

Anchor: COSO 2013 Principle 17 framing on the evaluation and communication of internal control deficiencies, including the requirement that deficiencies are communicated to parties responsible for taking corrective action. [verify principle reference.]

What this skill relies on: the framework expectation that classified exceptions feed corrective-action ownership; the register's disposition and handoff fields exist to satisfy this.

Link: https://www.coso.org/internal-control

## IT-audit findings

### FFIEC IT Examination Handbook — Audit Booklet

Anchor: FFIEC IT Examination Handbook, Audit booklet, sections on evaluating audit findings and the classification of findings within IT-audit work. [verify section labels in the edition currently posted.]

What this skill relies on: the IT-audit convention that exceptions in cyber and IT-control testing are classified by control-effectiveness implication rather than by surface symptom; the cyber cross-cutting overlay carries the operational detail.

Link: https://ithandbook.ffiec.gov/

## Heightened-standards severity flavour (large banks)

### 12 CFR Part 30, Appendix D — OCC Heightened Standards for large insured national banks

Anchor: Part 30 Appendix D, sections on the risk-governance framework and the front-line / independent-risk-management / internal-audit three-lines structure. [verify exact appendix and section labels.]

What this skill relies on: the heightened-standards severity flavour large-bank engagements carry; an exception in the front-line that the independent risk function did not catch reads with different severity than the same exception caught earlier in the lifecycle. The banking sector overlay carries the operational detail.

Link: https://www.ecfr.gov/current/title-12/chapter-I/part-30/appendix-Appendix%20D%20to%20Part%2030

## Cyber, privacy, and conduct cross-cutting (when applicable)

When the engagement carries cyber, privacy, or conduct risk lens, the cross-cutting overlays add the relevant anchors:

- Cyber: NIST SP 800-53 control-effectiveness language [verify section labels]; NYDFS 23 NYCRR Part 500 §500.16 (incident response) and §500.11 (third-party security policy) [verify current section labels]; FFIEC IT booklet finding patterns (above).
- Privacy: GLBA Safeguards Rule (16 CFR Part 314), specifically §314.4 on safeguards and incident response [verify section labels]; HIPAA Security Rule where the population includes protected health information.
- Conduct: CFPB UDAAP Examination Manual sections on identifying unfair, deceptive, or abusive practices [verify section labels]; the manual's framing of consumer harm shifts severity calibration when the population is consumer-facing.

These overlays load when the scope's `cross_cutting_overlay_set` includes the corresponding entry.
