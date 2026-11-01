# cross-cutting

One section per topic. Read only the sections the scope calls for.

## conduct

### Conduct cross-cutting overlay — section1071-readiness

When the scope flags conduct, load this overlay alongside `references/source-anchors.md`. Section 1071 readiness is a data-collection-and-reporting obligation, but the way it is implemented at the lender carries a lender-conduct dimension: how applicants experience the demographic-collection script, how the firewall is honoured in practice, how vendors and front-line staff are managed against the rule, and how readiness gaps are communicated up the firm. Each of these is a conduct surface, not just a compliance one.

#### The lender-conduct dimension of §1071 implementation

§1071 introduces a new applicant interaction (the demographic-data request and refusal-handling) at a sensitive moment in the credit application. The way the firm conducts that interaction is a conduct-risk surface in the same sense that mortgage-application demographic collection has been a conduct-risk surface for HMDA-reporting lenders for decades. The conduct themes specific to §1071:

- **Demographic-collection script integrity**. Front-line staff or the digital application flow must deliver the rule's required disclosures (the request is for compliance with federal law, the applicant may decline, the information will not be used in the credit decision) accurately and consistently. Where staff coach the applicant to decline ("just say no, it's faster"), or where the digital flow buries the request, or where the script is delivered in a way that suggests the answer matters for the credit decision — each is a lender-conduct failure, not just a 1071 compliance gap.
- **Firewall integrity in practice**. The 12 CFR 1002.108 firewall is a control, but it operates through the daily behaviour of underwriters and other personnel in the firm. Where an underwriter sees the demographic data because the customer-360 view exposes it, that's a control gap. Where an underwriter actively seeks the information through informal channels (asking a relationship manager, pulling the application form), that's a conduct issue.
- **Vendor and front-line management**. Vendor staff (LOS support, contact-centre outsource, broker channel) interacting with applicants on the firm's behalf are within the conduct perimeter. Their handling of the demographic-collection interaction reads back to the firm.
- **Readiness gap escalation**. Where readiness gaps are known but not escalated to the named accountable executive, or where the executive sign-off proceeds despite known gaps, the conduct issue is governance and escalation, not only the gap itself.

#### Operative conduct anchors that read into §1071 readiness

- **Dodd-Frank §§1031 and 1036 (UDAAP)**. Where the demographic-collection script misleads the applicant about why the data is being requested or how it will be used, the misrepresentation is a UDAAP exposure. The §1071 rule's required disclosures are designed to prevent this; the firm's implementation has to deliver them.
- **CFPB UDAAP Examination Manual** (current edition) [verify edition]. Sets the supervisory expectation for fair-treatment of applicants across the application lifecycle. The §1071 demographic-collection interaction sits inside this expectation.
- **Interagency Fair Lending Examination Procedures** (FFIEC, current edition) [verify edition]. The fair-lending intersection with §1071 is data-driven (the dataset feeds fair-lending testing), but the application-experience dimension is a fair-lending concern in its own right where the demographic-collection interaction itself differs by applicant characteristics in ways the firm has not designed for.
- **Firm code of conduct, sales-practices policy, and complaint-management policy**. The demographic-collection interaction is a sales-and-service touchpoint and reads against the firm's own conduct standards. Front-line incentive design that rewards application-completion speed at the cost of script integrity is a conduct-risk pattern worth surfacing.
- **Conduct committee charter**. Where the firm has a conduct committee or an equivalent forum, §1071 readiness gaps with a conduct dimension belong on the committee's agenda. Routing through the compliance committee alone misses the conduct-governance dimension.

#### Where §1071 readiness gaps surface conduct themes

The following gap patterns recur and have a conduct dimension that the readiness memo should name:

- **"Just say no" coaching by the front line**. Reduces collection rates, distorts the demographic dataset, and breaches the script integrity. Surface as a conduct theme; route to the conduct committee.
- **Refusal coded as `null`**. The technical fix is a code-path change. The conduct theme is that the firm tolerated the miscoding because the refusal posture matters less to the front line than the application-completion metric.
- **Customer-360 firewall breach**. The technical fix is access-control redesign. The conduct theme is that the firewall control was designed without regard to how underwriters actually work, and that the daily behaviour reveals what the design did not.
- **Vendor LOS gap unescalated to executive**. The technical fix is to escalate. The conduct theme is governance: the gap was known, the executive was not told, and the readiness memo's sign-off proceeded.
- **Bona-fide-error policy not in place at go-live**. The technical fix is to write the policy. The conduct theme is that the firm went live on a regulated submission without the bona-fide-error governance in place to manage the predictable amendment cycle.
- **Modified data publication blindside**. The technical fix is the privacy-overlay re-identification briefing. The conduct theme is that the firm did not consider its own customer-trust posture before the first modified-data publication.

#### Conduct-relevant sections in the readiness output

- **Demographic-collection-mechanics section**: includes a script-integrity check (does the front line deliver the disclosures as written?) and a front-line-incentive review (does the incentive structure pressure the front line away from script integrity?).
- **Firewall section**: includes a firewall-in-practice check (is the firewall working as designed in daily behaviour?) alongside the access-control documentation.
- **Vendor-readiness section**: includes a vendor-staff-conduct row where the vendor is in the applicant interaction.
- **Gap list**: gaps with a conduct dimension are flagged with a `conduct_theme` column or annotation; routing recommendation includes the conduct committee where the firm has one.
- **Reviewer questions**: include a question for the conduct-committee chair where the readiness gaps surface conduct themes.

#### Common conduct-overlay pitfalls in §1071 readiness

- Treating §1071 readiness as a compliance-only obligation. The applicant interaction is a conduct surface; the firewall is a conduct surface; the vendor management is a conduct surface; the executive-escalation discipline is a conduct surface.
- Routing readiness gaps to the compliance committee only. Conduct-relevant gaps belong on the conduct committee's agenda.
- Treating front-line coaching of applicants as a training issue. Where it persists despite training, it is an incentive issue and a conduct issue.
- Treating the vendor LOS gap as a vendor-management issue only. Where the firm proceeds toward go-live without escalating, the issue is governance.
- Treating the modified-data publication as a privacy-only issue. The customer-trust dimension is a conduct dimension.

## privacy

### Privacy cross-cutting overlay — section1071-readiness

When the scope flags privacy, or whenever the readiness assessment touches the demographic-data fields under 12 CFR 1002.107, load this overlay alongside `references/source-anchors.md`. Applicant-demographic data is sensitive customer data; the firewall under 12 CFR 1002.108 is the operative §1071-internal control, and the GLBA Safeguards Rule layers underneath as the broader customer-data-security obligation.

#### GLBA Safeguards Rule on §1071 demographic data

- **GLBA Safeguards Rule, 16 CFR Part 314** (FTC; comparable rules at the prudential regulators for depositories under 12 CFR Parts 30, 208, 364, 568). Sets the financial institution's obligation to maintain a written information-security program for customer information. Applicant-demographic data collected under §1071 is **customer information** under GLBA where the applicant becomes a customer (and **consumer information** in the broader pre-customer phase under FTC guidance). The Safeguards Rule's required elements (designated qualified individual, risk assessment, access controls, encryption, multi-factor authentication, monitoring, vendor oversight, incident response, written program with annual report to the board or senior officer) all apply to the §1071 dataset.
- **Specific Safeguards-relevant elements for §1071 readiness**:
  - **Access controls** (16 CFR 314.4(c)(1) [verify subsection]): the §1071 firewall under 1002.108 sits inside the broader access-control program; the firewall's role-based access design and exception process are the §1071-specific implementation.
  - **Encryption** (16 CFR 314.4(c)(3) [verify subsection]): demographic data at rest and in transit. The LOS, the data warehouse, the customer-360 view, and any vendor-managed environment that holds the §1071 demographic data should meet the encryption standard.
  - **Vendor oversight** (16 CFR 314.4(f) [verify subsection]): vendor LOS, demographic-collection-form provider, FIG-validation utility, submission utility — each is a service provider under the Safeguards Rule and needs the contractual provisions and monitoring.
  - **Incident response and notification**: a breach of the §1071 demographic dataset triggers GLBA notification mechanics (and any state-law notification mechanics that apply); the firm's incident-response plan should name the §1071 dataset explicitly as a regulated dataset.

#### CFPB modified-data publication and re-identification

- **12 CFR 1002.109** provides for the CFPB to publish a modified version of the submitted data. The modification is intended to manage privacy risk (the rule contemplates modification of fields that could enable re-identification), but for **low-volume small-business lending in identifiable geographies** the re-identification risk persists even after the CFPB's modification:
  - A firm with a small number of small-business originations in a sparsely-populated census tract publishes a publicly-readable record where the combination of census tract, NAICS code, gross annual revenue band, time in business, number of workers, and loan amount band may identify the borrower even with demographic fields suppressed.
  - The CFPB's modification methodology is set by the Bureau and applied at submission processing, not by the firm; the firm cannot pre-modify in its submission. But the firm can — and should — surface the re-identification risk in its readiness memo so that the conversation with affected applicants and with internal stakeholders (legal, communications) happens before the first modified-data publication, not after.
- **Operational implication for the readiness work**: the privacy section of the readiness memo includes a re-identification-risk row for low-volume / identifiable-geography portfolios; the gap list rolls up an action to brief the relevant internal stakeholders and consider whether voluntary applicant communication is appropriate.

#### State-privacy applicability

- **State comprehensive privacy laws** (California CCPA / CPRA, Virginia VCDPA, Connecticut CTDPA, Colorado CPA, Utah UCPA, Texas TDPSA, and the growing list) [verify state-specific scope at the time of drafting]. The state laws generally exempt **GLBA-covered financial institutions** or **GLBA-covered data**, but the exemptions are not uniform: some states exempt the entity, some exempt the data, and some carve narrower exemptions that leave certain processing in scope (e.g., employee-data processing, certain marketing uses). The §1071 demographic dataset is GLBA-covered data and typically benefits from the state-law exemptions, but the firm should confirm under its specific state-law applicability matrix.
- **California CMIA** (California Confidential Medical Information Act) and similar state-law regimes targeting specific data classes typically do not reach §1071 demographic data (race, ethnicity, sex, LGBTQI+ status, women-owned status are demographic, not medical) but a careful read is appropriate where the firm operates a data-aggregation environment that crosses categories.
- **Operational implication for the readiness work**: the privacy section includes a state-applicability row marked `[verify state-specific scope]`; the gap list rolls up an action to confirm with privacy counsel for the firm's footprint.

#### Demographic-data-collection mechanics under privacy

- **Voluntary collection**. The §1071 rule requires the firm to **request** the demographic information from the principal owners, but the applicant **may decline**. The collection script must include the rule's required disclosures (the request is for compliance with federal law, the applicant may decline, the information will not be used in the credit decision). The script is itself a privacy-relevant disclosure; treat it as one.
- **Refusal handling**. Refusal is coded with the rule's required value (not `null`); the privacy posture is that the firm does not infer or impute the demographic data from third-party sources where the applicant has declined. Some demographic fields (race / ethnicity / sex) the rule expressly contemplates **firm-observed** capture in narrow circumstances (in-person applications where the principal owner has declined to self-identify) [verify subsection]; the firm-observed pathway is itself a privacy-sensitive process and needs documented procedure.
- **Principal-owner identification**. The rule defines principal owner as a natural person who owns 25% or more of the equity interests of the small business [verify threshold]. Identification of the principal owners (pulling from the application, from KYB / beneficial-ownership data, from public records) is itself a customer-data-processing operation governed by GLBA and applicable state law.

#### Privacy-relevant sections in the readiness output

- **Demographic-collection-mechanics section**: includes the script-disclosure compliance check, the refusal-handling code path, the principal-owner identification logic, and the firm-observed-capture procedure where applicable.
- **Firewall section**: cites 12 CFR 1002.108 as the §1071-specific control and GLBA Safeguards as the broader information-security program.
- **Vendor-readiness section**: includes the vendor's GLBA-Safeguards posture per service provider.
- **A standing privacy-risk row in the gap list**: re-identification risk in modified data publication for low-volume / identifiable-geography portfolios.
- **A standing privacy row in open questions for legal**: state-privacy applicability matrix at the time of drafting.

#### Common privacy-overlay pitfalls in §1071 readiness

- Treating the §1071 firewall as a privacy obligation rather than a §1071-internal access-control under 1002.108 sitting inside the broader GLBA Safeguards program. The firewall is a §1071 control; GLBA Safeguards is the umbrella.
- Coding applicant refusal as `null` rather than the rule's required refusal value. Privacy and FIG-validation both fail.
- Imputing demographic data from third-party sources where the applicant has declined. The rule does not contemplate inference; the firm-observed pathway under the rule is narrowly defined.
- Treating modified data publication as a CFPB problem only. The re-identification risk for low-volume / identifiable-geography portfolios sits with the firm's reputation and applicant relationship; surface it in the readiness memo.
- Missing the state-privacy applicability question on the assumption that GLBA preempts. The GLBA-related state-law exemptions vary; pin per state.
