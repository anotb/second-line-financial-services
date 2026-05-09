# Banking sector overlay — exam-brief

When the scope flags banking and the regulator is one of OCC, FRB, FDIC, NCUA, or a state banking department running a non-full-scope engagement (e.g., a CFPB-coordinated exam at a bank, an NYDFS cyber exam at a state-chartered bank, a coordinated trust exam, an IT-focused exam), load this overlay alongside `references/source-anchors.md`. For a full-scope federal banking exam at a bank carrying the Heightened Standards, route to `sector-plugins/banking-risk-compliance/banking-supervision-readiness` instead; the readiness sprint there carries the substantive scaffolding. This overlay carries the engagement playbook for the slice that the generic skill owns.

## Examiner-in-charge convention

The federal banking agencies all run an examiner-in-charge model. The OCC EIC sits inside the assigned supervisory office (Large Bank Supervision, Midsize and Community Bank Supervision, or the Federal Branches and Agencies group); the FRB EIC sits inside the regional Reserve Bank for state-member banks and BHCs; the FDIC EIC sits inside the regional office. The single-point-of-contact relationship matters: the firm's head of regulatory affairs or general counsel runs the day-to-day relationship; the CRO and chief compliance officer run topic-specific contact for their domains. Mapping points of contact to the agency's supervisory team structure (EIC, deputy EIC, subject-matter-expert examiners) avoids the common failure mode of routing every question through one bottleneck.

## Document-handling — bank examination posture

Federal bank examiners enjoy broad statutory examination access (12 USC §484 for the OCC; equivalent for FRB and FDIC). The firm does not negotiate examiner reach the way a non-bank firm might in an SEC adviser exam. Document handling is therefore production-shaped, not negotiation-shaped. Key practitioner notes:

- Privilege exists but is constrained. Bank-examination privilege protects the agency's own examination materials and confidential supervisory information; the firm's own attorney-client and work-product privilege still attach to firm-side documents. Counsel sets the privilege posture for each request line.
- Confidential supervisory information from prior cycles (supervisory letters, MRAs, MRIAs, exam reports) is the agency's, not the firm's. The firm cannot share CSI outside the firm without the agency's written authorisation under 12 CFR Part 4 Subpart C (OCC), Part 261 (FRB), or Part 309 (FDIC). Onward sharing inside the firm is constrained to a need-to-know population; ensure the production log records who has had CSI access.
- Production typically runs through agency-provided portals or examiner laptops on-site. On-site reading rooms remain common for sensitive material (loan files, board minutes, SARs).

## MRA / MRIA / consent-order posture

Federal banking MRAs and MRIAs are the two-tier supervisory finding mechanism shared across OCC, FRB, and FDIC. The convention:

- **MRA (Matter Requiring Attention)** — deficiency the bank must address. Typically resolved through the bank's standard issue-management process with bank-side commitment dates.
- **MRIA (Matter Requiring Immediate Attention)** — deficiency of greater significance requiring immediate management attention; expectations of board or board-committee oversight, faster commitment dates, and more frequent agency progress check-ins.
- **Consent order** — formal enforcement action, public, with specific articles, named compliance committee, monitor designation in some cases. Response posture is shaped by the order's articles and milestones; chains to `implementation-plan` for the milestone build-out.

The brief's response-posture section names: who owns the response (typically head of compliance, CRO, or general counsel for the formal letter); what triggers the response clock (receipt of the supervisory letter, not the exit memo); whether board reporting is required (almost always for MRIAs and consent orders, often for material MRAs); whether outside counsel is engaged for the response.

## Bank-specific anticipated-questions patterns

Examination priorities for federal banking agencies cycle through the year in published statements (semi-annual operating plan from the OCC; annual supervisory priorities communications from FRB; FDIC's published supervisory priorities and FILs). Recent recurring themes that shape anticipated-question lists across OCC, FRB, and FDIC engagements:

- BSA/AML programme effectiveness and 2020 AML Act implementation (priorities cycle).
- Third-party risk management against the June 2023 inter-agency guidance.
- Liquidity and interest-rate risk in the context of recent regional-bank stress.
- Operational resilience and cyber, including incident-notification under the 36-hour rule (12 CFR 53 / 12 CFR 225 / 12 CFR 304).
- Fair lending and CRA where the engagement touches consumer credit.
- Model risk management against SR 11-7 / OCC 2011-12 (and the revised 2026 guidance per OCC Bulletin 2026-13 where applicable [verify bulletin number and current title]).

## Exit-meeting and supervisory-letter response

The federal banking agencies typically hold an exit conference, then issue a supervisory letter or report of examination, then expect a written firm response within an agency-specific window (commonly 30 to 60 days; agency-specific). The brief should record the response window calculation as: clock starts on receipt of the supervisory letter or final report (not the exit memo), unless the agency has stated otherwise in writing. For MRIAs and consent orders, board-level commitment is expected and the response is typically reviewed by the agency before acceptance.

## When to hand off to banking-supervision-readiness

If the engagement is a full-scope OCC, FRB, or FDIC bank examination, the substantive readiness sprint belongs in `sector-plugins/banking-risk-compliance/banking-supervision-readiness`. The generic exam-brief is right when the engagement is:

- A targeted or topic-specific exam at a bank (cyber, IT, BSA-only, model risk, third-party, fair lending, trust).
- A CFPB exam at a depository (CFPB has direct supervisory authority for $10B+ banks and for non-bank consumer-finance providers).
- A state regulator exam (state banking department, NYDFS) that is not the federal full-scope cycle.
- A horizontal review across multiple banks where the bank's piece is one of several.

Where the line is unclear, default to chaining: the generic exam-brief produces the engagement playbook (scope, points of contact, document handling, response posture); the sector-readiness sprint produces the substantive evidence pack.
