# Source anchors: aml-model-monitoring

Named, dated regulatory and supervisory sources the AML model-monitoring review anchors to. The SKILL.md body uses generic workflow language; specific section references and excerpts live here. Firm-specific anchors (internal model risk policy, AML governance committee charter, scenario inventory taxonomy, refresh-cycle policy) belong in `references/firm-overlay.md`.

`[verify section]` placeholders mark anchors where the precise paragraph or subsection still needs verification against the current edition.

## Model risk supervisory guidance — applied to AML transaction monitoring as a model

### SR 11-7 / OCC Bulletin 2011-12 — Supervisory Guidance on Model Risk Management (Federal Reserve and OCC, April 4, 2011)

Anchor: Section III (Model Development, Implementation, and Use), Section IV (Model Validation), Section V (Governance, Policies, and Controls). [verify subsection labels in the current edition.]

What this skill relies on: that AML transaction-monitoring systems sit inside the model-risk perimeter (the guidance defines a model as a quantitative method that applies statistical, economic, financial, or mathematical theories, techniques, and assumptions to process input data into output — AML scenarios, thresholds, segmentation, and tuning all qualify); that ongoing monitoring, effective challenge, and validation are program-level expectations, not optional; and that governance over scenario change, threshold change, and segmentation refresh requires documented review and challenge.

Link: https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm

### OCC Bulletin 2026-13 — Revised Interagency Model Risk Management Guidance (2026)

Anchor: Sections covering model identification and inventory, validation requirements, ongoing monitoring expectations, and governance. [verify section labels and effective date as repo references mature; this revises the 2011 interagency guidance.]

What this skill relies on: the revised inventory expectation (AML transaction monitoring identified explicitly as a model in the firm's inventory), the expanded ongoing-monitoring expectations on scenario performance and benchmarking, and the strengthened governance over change and effective challenge.

Link: https://www.occ.gov/news-issuances/bulletins/2026/bulletin-2026-13.html

### FDIC Financial Institution Letter — Revised Interagency Model Risk Management Guidance (2026)

Anchor: FDIC FIL adopting the revised interagency MRM guidance. [verify FIL number and section labels.]

What this skill relies on: confirmation that the revised guidance applies to FDIC-supervised institutions on the same terms.

Link: https://www.fdic.gov/news/financial-institution-letters/2026/agencies-revise-interagency-model-risk-management-guidance

## BSA/AML examination expectations on transaction monitoring

### FFIEC BSA/AML Examination Manual — Suspicious Activity Reporting section

Anchor: Examination procedures covering automated transaction monitoring system expectations, rules / scenario coverage, alert generation, investigation, and SAR decisioning. [verify the precise sub-section anchor for transaction-monitoring system expectations within the SAR section of the current online manual edition.]

What this skill relies on: the examiner-facing expectation that the transaction-monitoring system covers products, services, customers, and geographies on a risk basis; that scenarios are designed and calibrated to the institution's risk profile; that the system is documented, validated, and reviewed; and that alert investigations and SAR decisions tie back to monitoring output.

Link: https://bsaaml.ffiec.gov/manual/AssessingComplianceWithBSARegulatoryRequirements/04

### FFIEC BSA/AML Examination Manual — BSA/AML Compliance Program section

Anchor: Risk-based BSA/AML compliance program expectations covering the BSA/AML risk assessment, internal controls, independent testing, BSA officer designation, and training. [verify section anchors.]

What this skill relies on: that the monitoring system's design and tuning flow from the BSA/AML risk assessment, and that independent testing and the BSA officer's program oversight cover the monitoring system.

Link: https://bsaaml.ffiec.gov/manual/

### FFIEC BSA/AML Examination Manual — Customer Due Diligence section

Anchor: CDD expectations including the expected-activity profile that the monitoring scenarios are calibrated against. [verify section anchors.]

What this skill relies on: the linkage between CDD-derived customer segmentation and monitoring scenario calibration; segmentation drift cannot be read in isolation from CDD posture.

Link: https://bsaaml.ffiec.gov/manual/

## Joint statements on innovation and risk-focused supervision

### FinCEN / Federal Banking Agencies Joint Statement on Innovation in BSA/AML Compliance (December 3, 2018)

Anchor: Joint statement issued by FinCEN, OCC, FRB, FDIC, and NCUA on innovative approaches to BSA/AML compliance.

What this skill relies on: the supervisory posture that institutions testing innovative approaches (machine-learning scenarios, network analytics, alternative segmentation) on top of an existing program will not be criticised for self-identified weaknesses surfaced during the test, provided the existing program continues to meet expectations. Relevant when the monitoring memo discusses pilots, parallel runs, or champion-challenger model comparisons.

Link: https://www.fincen.gov/news/news-releases/treasury-and-federal-banking-agencies-issue-joint-statement-encouraging

### OCC, FRB, FDIC, NCUA Joint Statement on Risk-Focused BSA/AML Supervision (July 22, 2021)

Anchor: Joint statement on risk-focused approach to BSA/AML examinations.

What this skill relies on: the supervisory expectation that the institution's BSA/AML risk assessment drives monitoring scope and tuning intensity, and that examination focus follows the institution's risk profile.

Link: https://www.fincen.gov/news/news-releases/agencies-issue-statement-bank-secrecy-actanti-money-laundering

## Adjacent sources used for pattern reference

### FinCEN typology advisories (general)

Anchor: FinCEN advisories documenting active typologies (ransomware, virtual-currency-enabled laundering, BEC, human trafficking, fentanyl, elder fraud, others). [verify specific advisory FIN-references and dates per typology when cited in the memo.]

What this skill relies on: that monitoring scenarios should reflect the typology landscape FinCEN has flagged, and that scenario coverage gaps against active advisories are findings.

Link: https://www.fincen.gov/resources/advisories

### Public AML transaction-monitoring enforcement actions and consent orders

Anchor: Public consent orders and civil-money-penalty assessments addressing transaction-monitoring deficiencies (data integrity, segmentation, scenario coverage, tuning evidence, validation). Used as pattern reference for what regulators have called material; never asserted as binding criteria for any other institution.

What this skill relies on: that recurring enforcement themes (segmentation refresh delays, BTL evidence absent, scenario coverage gaps against the institution's risk profile, change-governance gaps) are the same findings the QA looks for. Examples cited in memo narrative are anonymised; named institutions appear only where they are public defendants in a finalised action with a published consent order.

## Cross-cutting overlay — cyber typologies in transaction monitoring

When the engagement scope flags the cyber cross-cutting overlay, the cross-cutting reference loads the OFAC and FinCEN ransomware advisories, the FinCEN virtual-currency-related guidance, and the relevant typology references. See `references/cross-cutting/cyber.md`.

## Sector overlays

Sector-specific anchors load from the corresponding `references/sector-overlays/<sector>.md` file when the engagement scope names the sector. The banking and payments-fintech overlays carry the heaviest content; capital-markets and insurance carry narrow scope.
