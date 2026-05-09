# Sector overlay — payments and fintech

Loaded when the scope names payments or fintech (non-bank money transmitter, payment processor, prepaid issuer, neobank operating through a sponsor bank, BNPL provider, PFM, crypto exchange or custodian, remittance provider, P2P platform). The overlay carries non-bank supervision implementation-plan conventions on top of the generic spine.

## CFPB non-bank supervision

For larger participants and non-bank entities under CFPB supervisory authority, the CFPB Supervision and Examination Manual is the framing document. CFPB examinations produce Matters Requiring Attention (the parallel to the federal banking MRA convention) and supervisory letters. Implementation plans triggered by a CFPB MRA mirror the federal banking convention; the plan's effective date is the date the CFPB communicated.

CFPB Supervisory Highlights frames the recurring focus areas; the implementation-plan author tracks the most recent edition for the supervisory pattern that explains the firm's MRA. (Many CFPB Circulars on UDAAP, overdraft, NSF, adverse-action with complex algorithms, and account reopening were **withdrawn May 12, 2025; historical only** — anchor design decisions to the regulatory text rather than the withdrawn circular layer. The CFPB Interpretive Rule on BNPL (May 2024) was separately **nullified by Pub. L. 119-11 (May 9, 2025); historical only.**)

## State money-transmitter remediation

For non-bank money transmitters, state money-transmitter laws and the Money Transmission Modernization Act (MTMA, NMLS-driven) apply. State-by-state remediation cycles can be material when the firm operates in multiple states. The plan tracks state-by-state filings and approvals as separate milestones; the lead state generally drives the substance, with other states adopting in line.

NYDFS, California DFPI, Texas Department of Banking, and the Conference of State Bank Supervisors (CSBS) are common state-side participants in coordinated examinations. The plan names the lead state and the participating states.

## Sponsor-bank-driven remediation

For neobanks and fintechs operating through a sponsor-bank (BaaS) model, the implementation plan is bilateral: the sponsor bank's regulator (OCC, FRB, FDIC) drives expectations through the sponsor, and the fintech absorbs them through the third-party-risk management framework. The plan names the sponsor bank's role in governance, the contractual SLA changes the implementation requires, and the sponsor-bank's review checkpoints.

The June 2023 Interagency Guidance on Third-Party Relationships (OCC, FRB, FDIC) frames the sponsor-bank's expectations on the fintech. The plan reflects the sponsor-bank's diligence, monitoring, and exit-plan posture.

## Cyber and incident-notification overlays

Payments and fintech firms generally face multiple incident-notification regimes simultaneously: state breach-notification laws, NYDFS Part 500 (where applicable), the federal banking 36-hour rule via the sponsor bank where the fintech is a service provider, FTC Safeguards Rule notification (effective 2024), state-specific cybersecurity rules (Colorado, California, Massachusetts). The plan's notification workflow names every applicable regime and the fastest clock.

## Crypto and digital-asset overlays

For crypto-asset firms, the regulatory landscape is fragmented. SEC posture (custody, registration), CFTC posture, state money-transmitter posture, NYDFS BitLicense (Part 200), FinCEN MSB registration, OFAC sanctions screening, and bank-side custody-rule positions all apply differentially. The implementation plan names the regulatory regime each in-scope obligation maps to.

## Workstream shape

Typical payments-fintech workstream pattern:

- policy and procedure updates;
- platform changes (core processing, KYC, fraud, AML transaction monitoring, sanctions screening);
- third-party / sponsor-bank coordination;
- state-by-state filing or notification where applicable;
- consumer-disclosure changes;
- complaint-handling and consumer-redress workflow updates;
- regulatory reporting (state, federal, FinCEN);
- examiner-readiness for the next-cycle exam.

## Governance shape

Generally lighter than bank governance: CCO and CRO function with a compliance committee. Where the firm operates under a consent order or material MRA, governance escalates; for material consent orders, monthly board reporting is the practitioner pattern.

## BAU handoff conventions

The firm's obligation inventory in the GRC platform is the BAU home. The handoff names the CCO or chief risk officer as the obligation owner, the monitoring cadence, and the linkage into ongoing state-by-state filing or sponsor-bank-quarterly-review programmes.

## Sources

Named regulatory anchors for payments and fintech implementation are in `references/source-anchors.md` under the non-bank-supervision and state-banking blocks. Citations include the CFPB Supervision and Examination Manual, the June 2023 Interagency Guidance on Third-Party Relationships, NYDFS Part 200 (virtual currency), state money-transmitter statutes, FinCEN MSB framework (31 CFR Chapter X), OFAC sanctions framework, and the FTC Safeguards Rule.
