# Privacy cross-cutting overlay — section1071-readiness

When the scope flags privacy, or whenever the readiness assessment touches the demographic-data fields under 12 CFR 1002.107, load this overlay alongside `references/source-anchors.md`. Applicant-demographic data is sensitive customer data; the firewall under 12 CFR 1002.108 is the operative §1071-internal control, and the GLBA Safeguards Rule layers underneath as the broader customer-data-security obligation.

## GLBA Safeguards Rule on §1071 demographic data

- **GLBA Safeguards Rule, 16 CFR Part 314** (FTC; comparable rules at the prudential regulators for depositories under 12 CFR Parts 30, 208, 364, 568). Sets the financial institution's obligation to maintain a written information-security program for customer information. Applicant-demographic data collected under §1071 is **customer information** under GLBA where the applicant becomes a customer (and **consumer information** in the broader pre-customer phase under FTC guidance). The Safeguards Rule's required elements (designated qualified individual, risk assessment, access controls, encryption, multi-factor authentication, monitoring, vendor oversight, incident response, written program with annual report to the board or senior officer) all apply to the §1071 dataset.
- **Specific Safeguards-relevant elements for §1071 readiness**:
  - **Access controls** (16 CFR 314.4(c)(1) [verify subsection]): the §1071 firewall under 1002.108 sits inside the broader access-control program; the firewall's role-based access design and exception process are the §1071-specific implementation.
  - **Encryption** (16 CFR 314.4(c)(3) [verify subsection]): demographic data at rest and in transit. The LOS, the data warehouse, the customer-360 view, and any vendor-managed environment that holds the §1071 demographic data should meet the encryption standard.
  - **Vendor oversight** (16 CFR 314.4(f) [verify subsection]): vendor LOS, demographic-collection-form provider, FIG-validation utility, submission utility — each is a service provider under the Safeguards Rule and needs the contractual provisions and monitoring.
  - **Incident response and notification**: a breach of the §1071 demographic dataset triggers GLBA notification mechanics (and any state-law notification mechanics that apply); the firm's incident-response plan should name the §1071 dataset explicitly as a regulated dataset.

## CFPB modified-data publication and re-identification

- **12 CFR 1002.109** provides for the CFPB to publish a modified version of the submitted data. The modification is intended to manage privacy risk (the rule contemplates modification of fields that could enable re-identification), but for **low-volume small-business lending in identifiable geographies** the re-identification risk persists even after the CFPB's modification:
  - A firm with a small number of small-business originations in a sparsely-populated census tract publishes a publicly-readable record where the combination of census tract, NAICS code, gross annual revenue band, time in business, number of workers, and loan amount band may identify the borrower even with demographic fields suppressed.
  - The CFPB's modification methodology is set by the Bureau and applied at submission processing, not by the firm; the firm cannot pre-modify in its submission. But the firm can — and should — surface the re-identification risk in its readiness memo so that the conversation with affected applicants and with internal stakeholders (legal, communications) happens before the first modified-data publication, not after.
- **Operational implication for the readiness work**: the privacy section of the readiness memo includes a re-identification-risk row for low-volume / identifiable-geography portfolios; the gap list rolls up an action to brief the relevant internal stakeholders and consider whether voluntary applicant communication is appropriate.

## State-privacy applicability

- **State comprehensive privacy laws** (California CCPA / CPRA, Virginia VCDPA, Connecticut CTDPA, Colorado CPA, Utah UCPA, Texas TDPSA, and the growing list) [verify state-specific scope at the time of drafting]. The state laws generally exempt **GLBA-covered financial institutions** or **GLBA-covered data**, but the exemptions are not uniform: some states exempt the entity, some exempt the data, and some carve narrower exemptions that leave certain processing in scope (e.g., employee-data processing, certain marketing uses). The §1071 demographic dataset is GLBA-covered data and typically benefits from the state-law exemptions, but the firm should confirm under its specific state-law applicability matrix.
- **California CMIA** (California Confidential Medical Information Act) and similar state-law regimes targeting specific data classes typically do not reach §1071 demographic data (race, ethnicity, sex, LGBTQI+ status, women-owned status are demographic, not medical) but a careful read is appropriate where the firm operates a data-aggregation environment that crosses categories.
- **Operational implication for the readiness work**: the privacy section includes a state-applicability row marked `[verify state-specific scope]`; the gap list rolls up an action to confirm with privacy counsel for the firm's footprint.

## Demographic-data-collection mechanics under privacy

- **Voluntary collection**. The §1071 rule requires the firm to **request** the demographic information from the principal owners, but the applicant **may decline**. The collection script must include the rule's required disclosures (the request is for compliance with federal law, the applicant may decline, the information will not be used in the credit decision). The script is itself a privacy-relevant disclosure; treat it as one.
- **Refusal handling**. Refusal is coded with the rule's required value (not `null`); the privacy posture is that the firm does not infer or impute the demographic data from third-party sources where the applicant has declined. Some demographic fields (race / ethnicity / sex) the rule expressly contemplates **firm-observed** capture in narrow circumstances (in-person applications where the principal owner has declined to self-identify) [verify subsection]; the firm-observed pathway is itself a privacy-sensitive process and needs documented procedure.
- **Principal-owner identification**. The rule defines principal owner as a natural person who owns 25% or more of the equity interests of the small business [verify threshold]. Identification of the principal owners (pulling from the application, from KYB / beneficial-ownership data, from public records) is itself a customer-data-processing operation governed by GLBA and applicable state law.

## Privacy-relevant sections in the readiness output

- **Demographic-collection-mechanics section**: includes the script-disclosure compliance check, the refusal-handling code path, the principal-owner identification logic, and the firm-observed-capture procedure where applicable.
- **Firewall section**: cites 12 CFR 1002.108 as the §1071-specific control and GLBA Safeguards as the broader information-security program.
- **Vendor-readiness section**: includes the vendor's GLBA-Safeguards posture per service provider.
- **A standing privacy-risk row in the gap list**: re-identification risk in modified data publication for low-volume / identifiable-geography portfolios.
- **A standing privacy row in open questions for legal**: state-privacy applicability matrix at the time of drafting.

## Common privacy-overlay pitfalls in §1071 readiness

- Treating the §1071 firewall as a privacy obligation rather than a §1071-internal access-control under 1002.108 sitting inside the broader GLBA Safeguards program. The firewall is a §1071 control; GLBA Safeguards is the umbrella.
- Coding applicant refusal as `null` rather than the rule's required refusal value. Privacy and FIG-validation both fail.
- Imputing demographic data from third-party sources where the applicant has declined. The rule does not contemplate inference; the firm-observed pathway under the rule is narrowly defined.
- Treating modified data publication as a CFPB problem only. The re-identification risk for low-volume / identifiable-geography portfolios sits with the firm's reputation and applicant relationship; surface it in the readiness memo.
- Missing the state-privacy applicability question on the assumption that GLBA preempts. The GLBA-related state-law exemptions vary; pin per state.
