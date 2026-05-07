# Privacy cross-cutting overlay for marketing-rule-evidence

This overlay loads where the advertisement contains a testimonial that discloses (or could disclose) the identity of a client; where account-level details, holdings, or strategy specifics appear in the advertisement at a level that may identify a particular client; or where the advertisement makes claims about the firm's data practices, privacy posture, or use of client information.

Loaded by: `marketing-rule-evidence/SKILL.md` when the advertisement contains a testimonial, an endorsement, a case study identifying a particular client by name or by recognisable description, or any privacy-related claim. The overlay also fires from `engagement_scope.cross_cutting_set` when the scope record names `privacy`.

Cited and section-referenced anchors live in `references/source-anchors.md`.

## What the overlay catches

Marketing Rule disclosure mechanics handle the testimonial and endorsement disclosure clauses (compensation status, client status, material conflicts) and the third-party-rating disclosures. The privacy overlay handles the upstream client-information question: does the firm have the right to use the testimonial in this form, and does the use square with Reg S-P (Regulation S-P, 17 CFR Part 248) and the firm's privacy notice?

The overlay reads three named threads:

- *Client-consent for the testimonial use.* Where a testimonial identifies the client by name, by photograph, by recognisable description, or by reference to specific account facts, the firm's right to use those identifying elements turns on the client-consent posture. The Marketing Rule does not establish the consent posture; the firm's privacy notice and the Reg S-P framework do.
- *Reg S-P treatment of nonpublic personal information appearing in the advertisement.* Where account-level details, portfolio composition, performance attribution to a specific client account, or client-identifying facts appear, the disclosure-of-NPI analysis under Reg S-P §248.10 (limits on disclosure to nonaffiliated third parties) and §248.13 (exceptions) operates. Even where an exception applies, the firm's privacy notice must accurately describe the practice.
- *Privacy-claim accuracy.* Where the advertisement makes a privacy claim ("we will never share your data"; "your information is private to your relationship with us"; "client confidentiality is at the core of how we operate"), the claim must be consistent with the firm's actual practices and with the privacy notice content required under Reg S-P §248.6 (initial notice) and §248.7 (annual notice). A privacy claim that contradicts the privacy notice is a Marketing Rule (b)(1) untrue-statement and (b)(6) materially-misleading finding even where the privacy-program operation is otherwise compliant.

## Reg S-P May 2024 amendments — the breach-notification and incident-response thread

The May 16, 2024 amendments to Reg S-P [verify operative compliance dates by entity size] expanded the rule's scope to require advisers and other covered institutions to adopt incident-response programs and to provide notice to affected individuals following certain unauthorized-access incidents. The overlay reaches the marketing-claim implications:

- Marketing claims about cybersecurity posture, incident-free record, or "industry-leading data protection" are reviewed against the firm's actual incident history and the firm's incident-response program. Claims that are inconsistent with the firm's actual posture (or that overstate the maturity of the program) raise (b)(1) and (b)(6) findings.
- Claims about vendor data-protection practices reviewed for substantiation; the firm's reliance on vendor representations does not substitute for the firm's own substantiation file.

## State-privacy-law interaction

Where the firm's client base or marketing audience includes residents of states with comprehensive privacy laws (CCPA / CPRA in California; VCDPA in Virginia; CTDPA in Connecticut; CPA in Colorado; UCPA in Utah; and the rolling roster of state laws), marketing claims about data practices ("we will not sell your data"; "we will not share your data") must be reconciled with the broader state-law definitions of "sale" and "share" (which include disclosure for cross-context behavioral advertising under CCPA / CPRA) and with the firm's state-privacy-law disclosures. The overlay flags the state-privacy-law cross-check; the operative state list pin sits in `references/source-anchors.md` [verify state list at pack date].

## Privacy-specific pack template additions

The following fields are added where the privacy overlay loads:

- `testimonial.client_consent_obtained` — boolean.
- `testimonial.client_consent_scope` — string; describes the scope of the consent (use of name; use of photograph; use of account-level facts; use across channels; expiration).
- `testimonial.identifying_elements_used[]` — list of identifying elements (name, photograph, recognisable description, account-level fact, performance attribution).
- `advertisement.npi_disclosure_review` — enum (`no-npi-in-advertisement`, `npi-disclosed-with-exception-applicable`, `npi-disclosed-without-exception-applicable`, `npi-status-undetermined-needs-counsel`).
- `advertisement.privacy_notice_consistency` — enum (`consistent`, `inconsistent`, `not-checked`).
- `advertisement.privacy_claim_text[]` — list of privacy claims appearing in the advertisement.
- `advertisement.privacy_claim_substantiation[]` — per-claim substantiation source.
- `advertisement.cyber_posture_claim_substantiation` — string; for claims about cybersecurity posture.
- `advertisement.state_privacy_law_cross_check_state_list[]` — list of state laws checked.

## Common pitfalls in privacy-flagged Marketing-Rule packs

- Treating the testimonial-disclosure clauses as sufficient and missing the upstream client-consent posture. The Marketing Rule disclosures handle the compensation, client-status, and conflict disclosures; the right to use the testimonial in the form presented is a separate question.
- Treating account-level details as substantiation evidence without checking the NPI-disclosure status. Even where the data supports the claim, the disclosure of identifying client facts may itself be a Reg S-P question.
- Treating the firm's privacy notice as a static document. The notice must describe the firm's actual practices; a marketing-claim that contradicts the notice triggers either a Marketing Rule (b)(1) finding (the claim is untrue) or a Reg S-P notice-update obligation (the notice is incomplete).
- Treating cybersecurity claims as marketing flair. Substantiation discipline applies to cyber-posture claims, vendor-protection claims, and incident-record claims on the same basis as performance claims.
- Treating "we will not sell your data" claims as obviously safe. CCPA / CPRA broader sale-and-share definitions reach disclosures for cross-context behavioral advertising; the cross-check is a state-by-state read.
