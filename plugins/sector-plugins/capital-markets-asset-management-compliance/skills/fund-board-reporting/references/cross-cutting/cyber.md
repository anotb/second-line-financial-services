# Cyber cross-cutting overlay for fund-board-reporting

When the scope record flags `cyber` for the fund-board pack, this overlay sets the cyber-risk content for the named pack sections. The cyber surface a fund board oversees runs through the Rule 38a-1 service-provider compliance program (the adviser, transfer agent, custodian, fund accountant, distributor, valuation designee, sub-advisers all sit on top of cyber control programs) and through the Reg S-P customer-information safeguards as amended in May 2024.

Loaded by: `fund-board-reporting/SKILL.md` when the scope flags cyber, when a material cyber event affecting the fund or fund shareholders has occurred in the period, or when a service-provider cyber event has reached the §38a-1 material-compliance-matter threshold. Cited and section-referenced anchors live in `references/source-anchors.md`.

## Source basis

- SEC Reg S-P amendments (May 16, 2024): customer-information safeguarding; written incident-response program; 30-day customer notice posture; service-provider oversight in incident response. Compliance dates phased by entity size. [verify current compliance dates]
- SEC Cybersecurity Risk Management Rule for Advisers and Funds (proposed February 9, 2022) — current state must be verified at pack-write time. [verify current state — re-proposed, withdrawn, or pending]
- SEC cyber disclosure rules for public-company issuers (Reg S-K Item 106; Form 8-K Item 1.05) — apply to the fund's adviser parent where the parent is a public-company issuer. Final rule July 26, 2023; compliance dates phased.
- NYDFS 23 NYCRR Part 500 (Second Amendment, effective November 1, 2023) — applies to NYDFS-licensed entities including BDs and IAs licensed in New York; 72-hour cybersecurity event notification under §500.17.
- NIST Cybersecurity Framework 2.0 (February 2024) and FFIEC IT Examination Handbook for substantive control framing.
- ICA Rule 38a-1 — fund and service-provider compliance program; material compliance matters definition (38a-1(e)(2)) reaches cyber events that constitute violations of the federal securities laws or weaknesses in the policies and procedures.

## What changes for cyber-flagged fund-board packs

### 1. Fund-shareholder customer-information events under Reg S-P

Reg S-P (May 2024) covers customer-information events affecting fund shareholders. The pack carries:

- Any customer-information event in the period: nature of the event, affected systems, types of customer information affected (account number, transaction history, taxpayer identification number, beneficiary information), customer count affected, the customer-notice posture and timing (no later than 30 days after becoming aware that unauthorized access has occurred or is reasonably likely to have occurred).
- The fund's incident-response program reference and any program change in the period.
- Service-provider-driven events: the transfer agent, custodian, distributor, or sub-transfer-agent surface holds the bulk of fund-shareholder customer information; an event at the service provider triggers the fund's notice obligation when fund-shareholder customer information was affected. The pack carries the service-provider event detail, the contractual notification posture, and the fund's notice obligation analysis.

Reg S-P customer-notice timing is binding (30 days after becoming aware); the pack reflects whether the fund met the timing and any escalation that occurred.

### 2. Service-provider cyber events feeding the §38a-1 material compliance matter assessment

A cyber event at a service provider may meet the §38a-1 material-compliance-matter threshold if it constitutes a violation of the federal securities laws, a violation of the service provider's compliance policies and procedures, or a weakness in the design or implementation of the policies and procedures. The pack carries:

- Service-provider cyber events in the period meeting the firm's reporting threshold.
- The fund CCO's assessment of whether the event is a §38a-1 material compliance matter for the service provider (and accordingly for the fund).
- The service provider's remediation status and the parent CCO's oversight evidence (testing, third-party reports, attestations supplemented by independent verification).
- Service-provider contract review for incident-notification adequacy: whether the contract requires the service provider to notify the fund or adviser within a defined timeframe, what escalation rights the fund has, and what audit rights the fund retains.

### 3. Public-parent SEC cyber disclosure considerations (Item 1.05, Item 106)

Where the fund's adviser is a subsidiary of a public-company issuer, SEC cyber disclosure rules (Reg S-K Item 106 for annual disclosure, Form 8-K Item 1.05 for material incident disclosure) apply at the public-parent level. The fund-board pack carries:

- Brief reference to any 8-K Item 1.05 disclosure made by the public parent in the period that touches the adviser or the fund.
- Brief reference to the public parent's most recent Item 106 disclosure where it bears on the adviser's program (the disclosure is the public parent's, not the fund's, but the board's oversight context benefits from the reference).
- The disclosure-process referral status for any in-period event that may rise to the Item 1.05 disclosure threshold for the public parent.

The fund board does not make the public-parent disclosure decision; the parent's disclosure committee or equivalent process owns that. The pack flags the event and the disclosure-process referral.

### 4. Cyber as a Rule 38a-1 service-provider program element

The CCO's annual written report under Rule 38a-1(a)(4)(iii) addresses the operation of the fund's compliance program and each service provider's compliance program. Cyber is a program element for every service provider in scope. The pack carries:

- Each service provider's cybersecurity program adequacy as part of the per-service-provider 38a-1 compliance program assessment.
- Material cyber-control changes at each service provider in the period.
- Independent attestation status (SOC 2 Type II reports for the major service-provider categories; third-party penetration test results where shared; incident-response tabletop participation).
- Any cyber-related supervisory finding affecting a service provider (SEC EXAMS finding, NYDFS Part 500 examination finding, FFIEC finding for the bank-affiliated custodian).

### 5. Sub-adviser cyber oversight

Sub-advisers carry their own cyber surface. The pack treats sub-adviser cyber as a sub-adviser-compliance-program element under the parent CCO's 38a-1 oversight:

- Sub-adviser cyber program adequacy assessment evidence.
- Sub-adviser cyber events in the period and any material events.
- Sub-adviser cyber-attestation status (SOC 2, independent assessment, parent-CCO testing where conducted).
- Sub-adviser code of ethics and personal-trading platform cyber posture, given the cyber surface around personal-trading data.

### 6. Cyber-related forward-looking content

The forward-looking commentary's cyber component covers items the trustees should be aware of:

- Reg S-P May 2024 amendments compliance phase-in for the fund and the service-provider population; the fund's program-update status and the service-provider program-update verification status.
- SEC Cybersecurity Risk Management Rule for Advisers and Funds — current state of the proposal and the fund's contingency planning if the rule is finalized.
- NYDFS Part 500 Second Amendment phased compliance dates affecting NY-licensed BDs and IAs in the fund's service-provider population.
- Threat-environment forward view to the extent relevant to the fund or its service providers (sector-specific intelligence, regulator-issued advisories).

### 7. Cross-link to other capability skills and to sector skills

- Adviser-firm cyber slice in the adviser ERM pack: `risk-reporting/skills/risk-committee-pack` with the cyber cross-cutting overlay.
- Public-company cyber disclosure decision and 8-K Item 1.05 trigger analysis for the public parent: `risk-reporting/skills/cyber-disclosure-readiness`.
- Vendor cyber concentration view (the fund's service-provider cyber surface is a concentration question): `third-party-operational-resilience/skills/concentration-risk-review` with capital-markets sector overlay.
- Single-issue write-up for a material cyber event meeting §38a-1 threshold: `risk-compliance-core/skills/issue-writeup`.

## Cyber-specific output content

Added to the fund-board pack content:

- Cyber and operational resilience events section (deck slide and Word annex section): events affecting the fund or fund shareholders in the period; service-provider cyber events meeting the firm reporting threshold; Reg S-P customer-notice posture for any in-period customer-information event; public-parent disclosure-referral status where applicable.
- Service-provider compliance summary: each in-scope service provider's cyber-program adequacy assessment; SOC 2 / independent attestation status; material cyber-program change in the period.
- Forward-looking cyber items: regulatory horizon (Reg S-P phase-in, SEC cyber rule status, NYDFS phased dates) and threat-environment forward view where relevant.

## Common pitfalls in cyber-flagged fund-board packs

- Treating Reg S-P customer-notice timing as a service-provider problem. The fund retains the customer-notice obligation when fund-shareholder customer information was affected, regardless of which party in the chain held the information at the moment of the event.
- Sub-adviser and service-provider cyber attestation accepted without independent verification. The 38a-1 oversight expectation is that the parent CCO reasonably believes the program is adequate; attestation alone does not satisfy this.
- Public-parent 8-K Item 1.05 disclosure decisions reported in the fund-board pack as if they bind the disclosure committee. The disclosure-committee process is separate; the pack flags the event and the disclosure-process referral.
- Cyber rated "stable" in the operational-resilience section while material cyber events occurred in the period, without commentary that explains the apparent inconsistency.
- Service-provider cyber events reported only as a count. The board needs the conflict shape: which service provider, which information surface, the contractual notification posture, the fund's notice obligation analysis, and the remediation status.
- Forward-looking cyber commentary that is generic ("emerging cyber threats remain elevated"). Replace with named items the board can act on: Reg S-P implementation status, SEC cyber rule status with the firm's contingency posture, named threat-environment items where they bear on the fund's service-provider population.
