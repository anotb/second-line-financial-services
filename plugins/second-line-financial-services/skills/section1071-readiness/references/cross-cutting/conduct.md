# Conduct cross-cutting overlay — section1071-readiness

When the scope flags conduct, load this overlay alongside `references/source-anchors.md`. Section 1071 readiness is a data-collection-and-reporting obligation, but the way it is implemented at the lender carries a lender-conduct dimension: how applicants experience the demographic-collection script, how the firewall is honoured in practice, how vendors and front-line staff are managed against the rule, and how readiness gaps are communicated up the firm. Each of these is a conduct surface, not just a compliance one.

## The lender-conduct dimension of §1071 implementation

§1071 introduces a new applicant interaction (the demographic-data request and refusal-handling) at a sensitive moment in the credit application. The way the firm conducts that interaction is a conduct-risk surface in the same sense that mortgage-application demographic collection has been a conduct-risk surface for HMDA-reporting lenders for decades. The conduct themes specific to §1071:

- **Demographic-collection script integrity**. Front-line staff or the digital application flow must deliver the rule's required disclosures (the request is for compliance with federal law, the applicant may decline, the information will not be used in the credit decision) accurately and consistently. Where staff coach the applicant to decline ("just say no, it's faster"), or where the digital flow buries the request, or where the script is delivered in a way that suggests the answer matters for the credit decision — each is a lender-conduct failure, not just a 1071 compliance gap.
- **Firewall integrity in practice**. The 12 CFR 1002.108 firewall is a control, but it operates through the daily behaviour of underwriters and other personnel in the firm. Where an underwriter sees the demographic data because the customer-360 view exposes it, that's a control gap. Where an underwriter actively seeks the information through informal channels (asking a relationship manager, pulling the application form), that's a conduct issue.
- **Vendor and front-line management**. Vendor staff (LOS support, contact-centre outsource, broker channel) interacting with applicants on the firm's behalf are within the conduct perimeter. Their handling of the demographic-collection interaction reads back to the firm.
- **Readiness gap escalation**. Where readiness gaps are known but not escalated to the named accountable executive, or where the executive sign-off proceeds despite known gaps, the conduct issue is governance and escalation, not only the gap itself.

## Operative conduct anchors that read into §1071 readiness

- **Dodd-Frank §§1031 and 1036 (UDAAP)**. Where the demographic-collection script misleads the applicant about why the data is being requested or how it will be used, the misrepresentation is a UDAAP exposure. The §1071 rule's required disclosures are designed to prevent this; the firm's implementation has to deliver them.
- **CFPB UDAAP Examination Manual** (current edition) [verify edition]. Sets the supervisory expectation for fair-treatment of applicants across the application lifecycle. The §1071 demographic-collection interaction sits inside this expectation.
- **Interagency Fair Lending Examination Procedures** (FFIEC, current edition) [verify edition]. The fair-lending intersection with §1071 is data-driven (the dataset feeds fair-lending testing), but the application-experience dimension is a fair-lending concern in its own right where the demographic-collection interaction itself differs by applicant characteristics in ways the firm has not designed for.
- **Firm code of conduct, sales-practices policy, and complaint-management policy**. The demographic-collection interaction is a sales-and-service touchpoint and reads against the firm's own conduct standards. Front-line incentive design that rewards application-completion speed at the cost of script integrity is a conduct-risk pattern worth surfacing.
- **Conduct committee charter**. Where the firm has a conduct committee or an equivalent forum, §1071 readiness gaps with a conduct dimension belong on the committee's agenda. Routing through the compliance committee alone misses the conduct-governance dimension.

## Where §1071 readiness gaps surface conduct themes

The following gap patterns recur and have a conduct dimension that the readiness memo should name:

- **"Just say no" coaching by the front line**. Reduces collection rates, distorts the demographic dataset, and breaches the script integrity. Surface as a conduct theme; route to the conduct committee.
- **Refusal coded as `null`**. The technical fix is a code-path change. The conduct theme is that the firm tolerated the miscoding because the refusal posture matters less to the front line than the application-completion metric.
- **Customer-360 firewall breach**. The technical fix is access-control redesign. The conduct theme is that the firewall control was designed without regard to how underwriters actually work, and that the daily behaviour reveals what the design did not.
- **Vendor LOS gap unescalated to executive**. The technical fix is to escalate. The conduct theme is governance: the gap was known, the executive was not told, and the readiness memo's sign-off proceeded.
- **Bona-fide-error policy not in place at go-live**. The technical fix is to write the policy. The conduct theme is that the firm went live on a regulated submission without the bona-fide-error governance in place to manage the predictable amendment cycle.
- **Modified data publication blindside**. The technical fix is the privacy-overlay re-identification briefing. The conduct theme is that the firm did not consider its own customer-trust posture before the first modified-data publication.

## Conduct-relevant sections in the readiness output

- **Demographic-collection-mechanics section**: includes a script-integrity check (does the front line deliver the disclosures as written?) and a front-line-incentive review (does the incentive structure pressure the front line away from script integrity?).
- **Firewall section**: includes a firewall-in-practice check (is the firewall working as designed in daily behaviour?) alongside the access-control documentation.
- **Vendor-readiness section**: includes a vendor-staff-conduct row where the vendor is in the applicant interaction.
- **Gap list**: gaps with a conduct dimension are flagged with a `conduct_theme` column or annotation; routing recommendation includes the conduct committee where the firm has one.
- **Reviewer questions**: include a question for the conduct-committee chair where the readiness gaps surface conduct themes.

## Common conduct-overlay pitfalls in §1071 readiness

- Treating §1071 readiness as a compliance-only obligation. The applicant interaction is a conduct surface; the firewall is a conduct surface; the vendor management is a conduct surface; the executive-escalation discipline is a conduct surface.
- Routing readiness gaps to the compliance committee only. Conduct-relevant gaps belong on the conduct committee's agenda.
- Treating front-line coaching of applicants as a training issue. Where it persists despite training, it is an incentive issue and a conduct issue.
- Treating the vendor LOS gap as a vendor-management issue only. Where the firm proceeds toward go-live without escalating, the issue is governance.
- Treating the modified-data publication as a privacy-only issue. The customer-trust dimension is a conduct dimension.
