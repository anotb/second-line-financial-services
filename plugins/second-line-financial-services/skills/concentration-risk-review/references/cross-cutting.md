# cross-cutting

One section per topic. Read only the sections the scope calls for.

## cyber

### Cyber cross-cutting overlay — concentration-risk-review

When the scope names cyber as a cross-cutting overlay, or when the technology-stack and sub-contractor-chain dimensions surface cyber-risk material to the supervisory read, load this overlay alongside `references/source-anchors.md`.

#### Why cyber sits next to concentration

Concentration shows up as cyber risk in three predictable ways:

1. A single cyber incident at a concentrated vendor removes multiple critical-or-important arrangements at once. The hyperscaler, identity-provider, and shared-utility dimensions all carry this exposure.
2. A shared-utility incident propagates across the firm and its peers, so the firm's own substitutability collapses under sector stress (every peer is shopping for the same alternative at the same time).
3. A sub-contractor-chain compromise at rank 2 or rank 3 reaches the firm through a vendor whose own evidence pack reads clean. Fourth-party visibility is the operative cyber-concentration posture.

The cyber-overlay reading is not a duplicate of `vendor-diligence`'s cyber-evidence read; it is the portfolio-level question of how cyber incidents propagate through the concentration map.

#### Anchors

- **FFIEC Information Technology Examination Handbook — Information Security booklet** [verify current edition and section]. Third-party concentration is read alongside the firm's own information-security posture; concentration nodes are read as third-party attack surface. https://ithandbook.ffiec.gov/ .
- **CISA Information and Communications Technology Supply Chain Risk Management** publications [verify exact title and section of the CISA publication referenced]. Supply-chain concentration is part of the firm's ICT supply-chain risk; named ICT supply-chain risk-management practices apply. https://www.cisa.gov/topics/supply-chain-security .
- **SEC final rule on cybersecurity disclosure** — Item 1.05 Form 8-K and Reg S-K Item 106 (effective 2023) [verify section]. Where the firm is a public registrant, material cyber incidents at a concentrated vendor may be reportable; the concentration view feeds the materiality assessment. https://www.sec.gov/files/rules/final/2023/33-11216.pdf [verify URL].
- **NYDFS 23 NYCRR Part 500.11 — Third-Party Service Provider Security Policy**. §500.11(a) policy elements; §500.11(b) periodic assessment. Reads as part of the firm's own cybersecurity programme; concentration is implicit in the periodic-assessment expectation. https://www.dfs.ny.gov/industry_guidance/cybersecurity .

#### Cyber-driven concentration findings to surface

- Identity-provider concentration where a single identity-and-access-management vendor sits in front of multiple critical-or-important services. Substitutability read names that identity-vendor substitution is operationally invasive.
- Endpoint-detection-and-response or extended-detection-and-response vendor concentration where one vendor supplies the firm's endpoint security posture. Substitutability under stress (the EDR vendor itself being compromised or unavailable) is the operative test.
- Email-security-gateway concentration where one vendor sits in front of all customer-facing and employee email. Substitutability under stress is similar to EDR.
- Certificate-authority and PKI-vendor concentration where one CA underwrites the firm's certificate posture across services.
- Logging-and-SIEM-vendor concentration where the firm's incident-response capability depends on continued vendor availability.
- Cyber-insurance underwriter concentration is a related but separate read; the operational-vendor dimension this overlay covers is the technical-vendor side, not the insurance side.

#### Stressed-substitutability under cyber events

A concentrated cyber-vendor failing during the firm's own incident-response window is a worst-case scenario. The substitutability read in the cyber-overlay rows names whether the firm has rehearsed substitution under those conditions; almost always the answer is "no", and the recommended action chains to `resilience-testing-pack` for a severe-but-plausible scenario test.

#### Output-template additions for cyber

- Identity-provider row in `technology-stack-other` with shared-control-plane considerations.
- EDR/XDR, email-security-gateway, CA/PKI, SIEM rows in the same dimension.
- Stressed-substitutability column populated with explicit attention to the during-incident scenario.
- Reviewer questions clustered for the CISO and the cyber-incident-response forum where the cyber-overlay-driven findings are surfaced.

#### Common pitfalls in cyber-overlay concentration reads

- Reading the cyber-overlay rows as a duplicate of `vendor-diligence`'s cyber-evidence read. They are the portfolio-level question, not the per-arrangement question.
- Missing the during-incident substitutability scenario. Substitutability under benign conditions and substitutability during the firm's own incident-response window are not the same test.
- Treating the SEC cyber-disclosure feed-through as a procurement matter. Where the firm is a public registrant, the concentration view feeds the materiality assessment; legal and disclosure counsel are reviewers, not the head of TPRM alone.
