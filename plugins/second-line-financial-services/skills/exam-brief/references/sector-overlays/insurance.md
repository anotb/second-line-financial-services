# Insurance sector overlay — exam-brief

When the scope flags insurance and the regulator is a state department of insurance (state DOI), a coordinated multi-state team led under NAIC framework, the lead-state regulator on a financial exam, or NYDFS for an NY-domiciled or NY-licensed insurer, load this overlay alongside `references/source-anchors.md`. The federal-banking exam-readiness sprint pattern does not apply to insurance; there is no single insurance equivalent to the OCC, FRB, or FDIC examiner-in-charge convention because state DOIs run their own examination programs under their own statutes. The NAIC handbooks set inter-state convention for adoption by state DOIs, but the adopting statute is the operative authority, not the handbook itself.

## Two-track examination model

State DOIs run two distinct examination tracks. The brief carries which track is in scope; running the wrong scaffolding is the most common failure mode.

- **Financial examination** — solvency-focused, conducted on a multi-year cycle (typically every three to five years per state law), led by the lead-state DOI for multi-state coordination. The examiner-in-charge sits inside the lead-state DOI; participating-state examiners may join the team. The output is a public Report of Examination (ROE) filed under state insurance code. Anchored to the NAIC Financial Condition Examiners Handbook structure (planning, risk assessment, examination procedures, reporting, communication of findings).

- **Market conduct examination** — consumer-protection-focused, may run on a triennial cycle, may run for-cause based on complaint patterns or market-conduct annual statement (MCAS) data, may run as a multi-state coordinated examination through the NAIC Market Action Working Group. Anchored to the NAIC Market Conduct Examiners Handbook structure (Chapter 16 standardised data calls; chapter-by-chapter exam standards covering operations and management, complaint handling, marketing and sales, producer licensing, policyholder services, underwriting and rating, claims).

A combined or "comprehensive" exam runs both tracks in parallel; the brief still carries the two scopes separately because the document-handling postures and the finding mechanisms differ.

## Document-handling — insurance examination posture

State DOIs enjoy broad statutory examination access under each state's insurance code (typically modelled on NAIC Model Laws #390 Examiner Handbook Authority and #392 Market Conduct Surveillance). Document handling differs from federal banking on three dimensions:

- The lead-state DOI in a coordinated financial exam has the production relationship; participating states receive the work product through the lead state. The brief names the lead state and the participating-state list; document production runs through the lead.
- Confidential examination materials are protected under each state's confidentiality statute (typically modelled on NAIC Model Law #210 §6 or equivalent) and under NAIC's confidentiality regime for shared work product. The firm's onward sharing of supervisory letters, exam reports, and ROE drafts is constrained; counsel sets the posture per state.
- The examination-by-contractor model is common: state DOIs frequently engage outside accounting and actuarial firms as deputy examiners. The contractor sits inside the agency for examination purposes; the firm's privilege posture treats them as agency.

Production typically runs through agency-provided portals, secure file transfer, or examiner laptops on-site; on-site reading rooms remain common for sensitive material (claim files, complaint files, executive compensation, reinsurance treaties).

## Findings and response posture

Insurance examinations do not use the MRA / MRIA two-tier convention from federal banking. The findings mechanism is:

- **Examiner comment / examination finding** — issue identified during fieldwork, communicated in the examination report draft. The firm responds in writing; the response becomes part of the examination record.
- **Recommendation** — formal recommendation in the examination report; the firm's response posture and remediation plan attach to the public ROE in some states.
- **Order or stipulation** — formal regulatory action, public, with specific articles, often with monetary penalty and required corrective action plan. Response posture is shaped by the order's articles and by state administrative procedure.

The brief's response-posture section names: who owns the response (head of compliance for market-conduct findings; CFO or chief actuary for financial findings; general counsel for any matter heading toward an order); what triggers the response clock (typically receipt of the draft examination report, with an agency-specific window of 30 to 60 days commonly, state-specific); whether board reporting is required (typically yes for any matter that will land in the public ROE); whether outside counsel is engaged.

## Insurance-specific anticipated-questions patterns

Recurring market-conduct themes shaping anticipated-question lists across state DOI engagements:

- Complaint handling and root-cause-analysis quality (driven by NAIC Complaint Database and MCAS data); is the firm's complaint taxonomy aligned with NAIC categories.
- Producer licensing and appointment management; producer training currency; producer compensation conflicts.
- Claims practices, including unfair claims settlement practices under NAIC Model Law #900 and state-specific unfair-claims statutes; timeliness, denial-rationale documentation, claim-file-completeness.
- Underwriting and rating, including filed-form-and-rate compliance, rate-deviation justification, accelerated underwriting and external-data use under NAIC Bulletin and state-specific guidance, AI and predictive-model use under NAIC Model Bulletin on the Use of Artificial Intelligence Systems by Insurers (adopted 2023, state-by-state adoption status varies — [verify state-by-state adoption]).
- Policyholder services, including replacement-and-suitability for life and annuity, free-look handling, premium-handling.
- Privacy and cybersecurity under NAIC Insurance Data Security Model Law (#668), state-by-state adoption status varies; NYDFS Part 500 for NY-licensed entities.

Recurring financial-exam themes:

- Reserves adequacy and actuarial-opinion quality; consistency with the appointed-actuary's report.
- Investment portfolio and SAP-vs-GAAP treatment; affiliate transactions under NAIC Model Law #440.
- Reinsurance, including credit-for-reinsurance and collateral arrangements, under NAIC Model Law #785 / #786.
- ORSA (own risk and solvency assessment) under NAIC Model Law #505; recent ORSA Summary Report quality.
- Holding company filings under NAIC Model Law #440 (Form A, B, D, F as applicable).

## Lead-state coordination for multi-state engagements

For multi-state insurers, the lead-state DOI runs the financial exam under NAIC Financial Condition Examiners Handbook coordination conventions. The brief's scope-window section names: lead state, participating states, NAIC support if any, and the convention for sharing the draft report among participating states before issuance to the firm. Multi-state market-conduct exams run through the NAIC Market Action Working Group (MAWG) where adopted; the brief names the MAWG-coordinated states.

## NYDFS-specific posture

For NYDFS engagements at NY-licensed insurers, layer NYDFS-specific conventions on top of the NAIC scaffolding:

- NYDFS regulates both market conduct and solvency for NY-licensed insurers; the conventions differ from generic state DOI in the formality of the supervisory-letter and consent-order machinery.
- NYDFS Cybersecurity Regulation (23 NYCRR Part 500) applies to most NY-licensed insurers (with limited exemptions); cyber-targeted exam scaffolding applies (cf. cross-cutting `cyber.md` overlay when present in the plugin).
- NYDFS Insurance Regulation 187 (suitability and best interests in life insurance and annuity transactions) drives a distinct examination posture for NY annuity sales.

## When this overlay applies and when it does not

This overlay applies for the engagement playbook on a state DOI examination. There is no separate sector exam-readiness skill for insurance in this plugin set; the substantive readiness work runs against the firm's existing program, with this overlay framing the engagement-side mechanics. If a future `insurance-prudential-conduct/insurance-exam-readiness` skill is added, the substantive readiness sprint moves there and this overlay continues to carry the engagement playbook.
