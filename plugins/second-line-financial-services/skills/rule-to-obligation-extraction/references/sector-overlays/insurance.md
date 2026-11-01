# Insurance sector overlay — rule-to-obligation-extraction

Load this overlay when the rule under extraction is a NAIC model law or model regulation, a state insurance code section, a state DOI bulletin or industry circular, or a market-conduct examination standard. State insurance regulation is state-by-state; the NAIC model is a starting reference, not binding text. The overlay carries the model-versus-state-adopted distinction and recurring extraction patterns for insurance rules.

## NAIC model-law versus state-adopted version

A NAIC model law is the model text the National Association of Insurance Commissioners adopts and circulates for state consideration. The model is not law in any state until the state adopts it through its legislative or regulatory process. State adoption is frequently with amendments. Extraction must distinguish:

- **Model-as-source**. When the rule under extraction is the NAIC model itself (e.g., reading the Model Law as a source for a national obligation inventory), pin to the model-section number with the model number (`Model 668 §4 Information Security Program`). Note that the model is not binding until adopted.
- **State-adopted version-as-source**. When the rule under extraction is a state-adopted version, pin to the state code section (e.g., `New York Insurance Law §305 Cybersecurity Requirements [verify]`; `Ohio Revised Code §3965.02`). State amendments at adoption are common; the extraction should capture material differences from the model in the open-extraction-questions section, with state-specific tags.
- **State-adoption status**. The NAIC tracks state-by-state adoption status. The extraction's source-trace should record adoption status as of the extraction date for the states in scope.

## Recurrent insurance-rule extraction patterns

- **Programme-and-officer pattern**. State insurance codes typically require licensees to maintain a written programme (cybersecurity programme, anti-fraud plan, complaint-handling plan, MLR-rebate procedures, ORSA process) and to designate an officer (Chief Information Security Officer; Anti-Fraud Officer; Compliance Officer; Chief Risk Officer). The programme decomposes into risk-assessment, life-cycle controls, third-party oversight, periodic review, board-or-board-committee reporting, and incident-response. Each is a row.
- **Notification-and-reporting pattern**. State insurance codes attach notification obligations to specific events (cybersecurity event; data breach; MLR-rebate underpayment; market-conduct examination finding). Extraction captures the trigger, the deadline (often 72 hours for cybersecurity events; state-specific for other triggers), the recipient (Commissioner; Attorney General; affected consumers), and the form of notice.
- **Filing-and-attestation pattern**. State insurance codes require periodic filings (Annual Statement; ORSA Summary Report; corporate governance annual disclosure; MLR rebate filings). Each filing is a row, with frequency `periodic`, action_type `reporting`, and the filing form named (e.g., NAIC Annual Statement; ORSA Summary Report).

## NAIC Insurance Data Security Model Law (Model 668) — worked pattern

Model 668 was adopted by the NAIC in 2017 and has been adopted by the majority of states (state-by-state status tracked at the NAIC). Extraction from the model decomposes into:

- §3 Definitions — the defined-terms section captures: "Cybersecurity Event"; "Information System"; "Licensee"; "Multi-Factor Authentication"; "Nonpublic Information"; "Risk Assessment"; "Third-Party Service Provider".
- §4 Information Security Program — programme, risk-assessment, designated officer, board-oversight rows.
- §5 Investigation of a Cybersecurity Event — incident-response, scope-of-investigation, retention rows.
- §6 Notification of a Cybersecurity Event — Commissioner-notification (within 72 hours of determination); affected-consumer-notification; reinsurer-notification rows.
- §7 Powers of the Commissioner — investigative-power, examination-power rows on the regulator-side; not obligation rows for the licensee.
- §9 Exceptions — exceptions row tied to small-licensee exemption (fewer than 10 employees per the model; state-amended thresholds common).

When extracting a state-adopted version of Model 668, capture the model section number alongside the state code section and flag material amendments (e.g., New York's NYDFS Part 500 was issued before Model 668 and has different definitions and timing; New York is sometimes counted as Model 668-equivalent and sometimes not, depending on the framing; the extraction should pin to the actual state instrument, not to the model when the state operates under its own rule).

## NAIC Risk Management and Own Risk and Solvency Assessment Model Act (Model 505) — worked pattern

Model 505 (adopted 2012, amended periodically) requires insurers above a premium-volume threshold to maintain a risk-management framework and to file an annual ORSA Summary Report with the lead-state regulator. Extraction decomposes into:

- §3 Definitions — "Insurer"; "Insurance Group"; "Lead State"; "ORSA Summary Report".
- §4 Risk Management Framework — programme, board-oversight, risk-appetite rows.
- §5 ORSA Requirements — three-component ORSA (description of risk-management framework; insurer assessment of risk exposure; group risk-capital and prospective solvency assessment).
- §6 ORSA Summary Report — filing rows: annual filing with lead-state regulator; sharing with other domestic regulators on request.
- §8 Confidentiality — regulator-side confidentiality posture; not a licensee obligation row.
- §9 Sanctions — penalty regime; not a substantive obligation row.

## Market-conduct examination standards

The NAIC Market Conduct Examiners Handbook is interpretive guidance for state-DOI market-conduct examinations of insurers. Pin to the handbook chapter when extracting (e.g., "Producer Licensing"; "Marketing and Sales"; "Underwriting and Rating"; "Claims"; "Complaint Handling"). The handbook is not directly binding on insurers; the binding text is the state insurance code provisions the handbook examines against. Extract from the underlying state code where the obligation lives, not from the handbook chapter alone.

## NAIC Corporate Governance Annual Disclosure Model Act (Model 305)

Model 305 requires insurers to file an annual corporate-governance disclosure with the lead-state regulator. Extraction decomposes into the disclosure components (board governance; senior management responsibilities; oversight of audit, risk, and other key functions). State-adoption status varies; pin to the state-adopted version when extracting against a specific state.

## When to escalate

The base SKILL.md is the right tool when the extraction feeds `obligation-mapping` for an insurer. When the extraction supports a state-DOI market-conduct examination readiness sprint, downstream consumers may include sector-specific exam-readiness skills (where they exist). The base skill produces the obligation list the readiness pack reads.
