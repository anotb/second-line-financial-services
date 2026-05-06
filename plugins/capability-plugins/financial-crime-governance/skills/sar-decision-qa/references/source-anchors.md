# Source anchors — sar-decision-qa

The named, dated regulatory sources this skill anchors to. SKILL.md cites this file by path and does not restate excerpts. Sector-specific and cross-cutting anchors live in the corresponding overlay files.

## Primary frame — SAR rules and examination expectations

- **FFIEC BSA/AML Examination Manual — Suspicious Activity Reporting section** [verify section anchor for the current online manual]. The examiner-facing detail on SAR program elements: identification of unusual activity, alert management and case-investigation expectations, decision-to-file documentation, narrative quality, structured-field completeness, continuing-activity reviews, confidentiality, and program-level controls. The manual is the operative read for "what does a defensible SAR decision file look like" in a US examination context. https://bsaaml.ffiec.gov/manual/AssessingComplianceWithBSARegulatoryRequirements/04 .

- **31 USC §5318(g)** — statutory SAR authority, safe-harbor for filers, and the confidentiality / no-notification-of-subject rules with limited exceptions (limited disclosures to the firm's affiliates with consistent SAR programs and to law enforcement and supervisors). The QA's tipping-off lens is anchored here, not in a guidance document.

- **31 CFR §1020.320** — Reports by banks of suspicious transactions [verify section]. The bank SAR rule: dollar thresholds ($5,000 / $25,000 with no suspect identified), filing window (30 days from initial detection of facts that may constitute a basis for filing; 60 days where no suspect is identified), continuing-activity 90-day review expectation as adopted in supervisory practice, confidentiality, supporting-documentation retention. https://www.ecfr.gov/current/title-31/subtitle-B/chapter-X/part-1020/subpart-C/section-1020.320 .

- **31 CFR §1023.320** — Reports by brokers or dealers in securities of suspicious transactions [verify section]. Parallel SAR rule for broker-dealers. https://www.ecfr.gov/current/title-31/subtitle-B/chapter-X/part-1023 .

- **31 CFR §1024.320** — Reports by mutual funds of suspicious transactions [verify section]. https://www.ecfr.gov/current/title-31/subtitle-B/chapter-X/part-1024 .

- **31 CFR §1025.320** — Reports by insurance companies of suspicious transactions [verify section]. Covered products only (permanent life, annuities with cash value, certain other investment-type products). https://www.ecfr.gov/current/title-31/subtitle-B/chapter-X/part-1025 .

- **31 CFR §1026.320** — Reports by futures commission merchants and introducing brokers in commodities of suspicious transactions [verify section]. https://www.ecfr.gov/current/title-31/subtitle-B/chapter-X/part-1026 .

- **31 CFR §1022.320** — Reports by money services businesses of suspicious transactions [verify section]. The MSB SAR rule with the lower $2,000 threshold (and $5,000 for issuers / sellers / redeemers of money orders or traveler's checks identified through a clearance review). https://www.ecfr.gov/current/title-31/subtitle-B/chapter-X/part-1022 .

## FinCEN form, instructions, and filing posture

- **FinCEN SAR (BSA E-Filing) — current form and instructions** [verify section / current form version date]. Operative document for structured-field expectations, narrative guidance, supporting-documentation handling, and continuing-activity filing posture. https://www.fincen.gov/resources/filing-information . The QA reads structured-field completeness against the current form, not a prior version.

- **FinCEN guidance on SAR filing thresholds, timing, and continuing-activity** [verify section / specific FinCEN guidance documents and FAQs current on the date of analysis]. The 30-day / 60-day window posture, the 90-day continuing-activity review expectation (FinCEN guidance reinforces the supervisory expectation), and the structured-field-versus-narrative reconciliation are anchored here. The QA does not fabricate a threshold or a window not in the rule or the guidance.

- **FinCEN advisories and FIN-2020-A series and forward** [verify section / specific advisory by date for the typology under review]. Examples cited in the skill body: convertible-virtual-currency advisories, ransomware advisories, elder-financial-exploitation advisory (FIN-2022-A002) [verify], real-estate advisories. Citing an apt advisory is the floor; citing inapt advisories for window-dressing is itself a finding. Date the advisory in the QA citation. https://www.fincen.gov/resources/advisoriesbulletinsfact-sheets .

## Joint statements

- **OCC / FRB / FDIC Joint Statement on Risk-Focused BSA/AML Supervision** (July 22, 2021) [verify section / URL]. Supervisory framing that risk-focused examination of BSA/AML programs concentrates on areas of higher ML/TF risk; the QA reads decision quality with risk focus, not a uniform-depth pass on every alert. https://www.federalreserve.gov/newsevents/pressreleases/files/bcreg20210722a1.pdf .

- **FinCEN / Federal Banking Agencies Joint Statement on Innovation in BSA/AML Compliance** (December 3, 2018) [verify section]. Acknowledges and supports BSA/AML innovation including technology-driven detection and decision approaches; the QA does not penalise documented, governed innovation in the alert-decision pipeline as long as the decision file evidences the typology, the evidence, and the rationale. https://www.fincen.gov/news/news-releases/treasurys-financial-crimes-enforcement-network-and-federal-banking-agencies .

- **OCC / FRB / FDIC / NCUA / FinCEN Interagency Statement on Model Risk Management for BSA/AML and OFAC Compliance** (April 9, 2021), referenced as SR 21-8 [verify section / URL]. Where the alert was generated by a model (transaction-monitoring scenario or sanctions-screening tool), model-risk governance for that model sits adjacent to the alert-decision QA; this skill does not re-do model-monitoring work (`aml-model-monitoring` does), but the QA notes whether the alert source has model-risk coverage on file. https://www.federalreserve.gov/supervisionreg/srletters/SR2108.htm .

## Confidentiality and tipping-off

- **31 USC §5318(g)(2)** — SAR confidentiality. Disclosure of a SAR or the fact of its existence to the subject is prohibited; limited intra-firm and to-supervisors / law-enforcement disclosures are permitted under specified conditions. The case-specific tipping-off assessment in fraud-recovery, EDD-overlap, dispute, and law-enforcement-liaison cases is anchored here. The program-level tickbox does not satisfy the case-specific assessment.

- **FinCEN guidance and FAQs on SAR confidentiality and sharing** [verify specific FAQs and guidance documents current on the date of analysis]. Sharing within a corporate organisation, sharing with parents and affiliates with consistent SAR programs, sharing with foreign branches, and the 314(b) information-sharing posture (separate authority, but adjacent in practice).

## Plugin-level shared references

Also consult, when present in the plugin:

- `references/source-map.md` — plugin-wide named-source map.
- `references/policy-control-library.md` — plugin-wide policy-and-control library.
- `references/review-gates.md` — named human-review gates and confidence-label definitions.

## Firm overlays

A firm using this skill in production adds firm-specific detail in `references/firm-overlay.md`. The skill consumes that file when present. Firm overlays do not modify the public anchors above.
