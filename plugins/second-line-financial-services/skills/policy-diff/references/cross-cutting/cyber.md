# Cross-cutting overlay: cyber

Loaded when the policy in scope is cyber-anchored — information security, cybersecurity, technology risk, third-party security, incident response, cloud-security, data-handling. The overlay does not change the change-log spine; it loads the named-source set and the materiality lens.

## Source-citation patterns specific to cyber diffs

- NYDFS 23 NYCRR Part 500 — cybersecurity requirements for NY-licensed financial-services companies. §500.3 (cybersecurity policy) is the operative anchor for the policy lifecycle; §500.11 (third-party security) ripples into TPRM diffs; §500.17 (notice of cybersecurity event) ripples into incident-response diffs.
- FFIEC IT Examination Handbook, Information Security booklet — used as the federal-banking expectation source for information-security policy diffs.
- SEC cybersecurity rules — Item 106 of Regulation S-K (cybersecurity risk management and governance disclosures), Form 8-K Item 1.05 (material cybersecurity incident disclosure) for SEC-registered issuers.
- SEC Reg S-P (17 CFR §248.30) — safeguards rule and disposal rule for broker-dealers, investment companies, and investment advisers.
- GLBA Safeguards Rule (16 CFR Part 314) — for FTC-regulated financial institutions.
- FedRAMP, NIST SP 800-53, NIST CSF — used as control-framework references where the firm's policy maps to one of them.

## Materiality patterns specific to cyber diffs

- Annual approval is itself a §500.3 obligation for NYDFS-covered entities; the diff supports the annual-approval record and the materiality lens distinguishes substantive change (operative-language, scope, or threshold movement) from cosmetic refresh (formatting, capitalisation).
- New asset-classification, asset-inventory, or data-classification provisions almost always carry material materiality because they introduce binding handling requirements and trigger fresh attestations.
- Incident-response policy changes that move incident-classification thresholds or notification clocks are material; the §500.17 72-hour clock and the SEC Form 8-K four-business-day clock are the operative external deadlines that define the lower bound on internal escalation timing.
- Cloud-security and third-party-security clauses ripple into the TPRM policy and the cloud-control framework; the cross-policy ripple block surfaces these.

## Downstream-impact patterns specific to cyber diffs

- All-staff training is common when data-classification, acceptable-use, or phishing-handling provisions change.
- DLP, IAM, and SIEM configurations are common system-change destinations; the substantive-delta column should name the configuration point where one is identified.
- Incident-response runbook updates flow from policy to runbook to tabletop exercise; the diff feeds the next tabletop's scenario set.
- Vendor-facing communication is common when the policy's third-party security expectation tightens; the communication plan summary clusters by audience accordingly.
