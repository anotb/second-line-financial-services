# Source anchors: complaint-theme-analysis

Cited regulatory sources this skill anchors to. Every primary anchor names the source, the section reference (or `[verify section]` flag), a one-paragraph excerpt or paraphrase of the relevant content, and the link.

The skill cites these by file path. SKILL.md does not restate excerpts.

## CFPB current-status posture (as of memo date)

On May 12, 2025 the CFPB withdrew a substantial portion of its prior advisory guidance (overdraft, NSF representment, AAN-with-algorithms circulars; the April 2023 Abusiveness Policy Statement). The bureau's Supervisory Highlights publication cadence has slowed materially; older issues remain useful as historical signal but the bureau's current focal items have to be confirmed at memo date. The CFPB Complaint Database itself remains operational and continues to publish public complaint extracts.

Theme-grade work is signal-grade, not finding-grade. The withdrawal of CFPB advisory guidance does not change the underlying complaint patterns, the consumer harm hypotheses, or the regulatory-text touchpoints (UDAAP §1031, Reg E §1005.11, Reg X §1024 Subpart C, Reg B §1002.9, FCRA §1681s-2, etc.). State AGs, prudential regulators, and class-action plaintiffs continue to reach the same fact patterns under their own authority. Anchor regulatory-exposure mapping to the statute and regulation; reference the withdrawn CFPB items as historical interpretive context where useful, but do not depend on them as current bureau posture. Use `[verify operative status at memo date]` for any item where the CFPB's enforcement priorities materially affect the read.

## Primary anchors

### 1. CFPB Consumer Complaint Database

- Citation: Consumer Financial Protection Bureau, Consumer Complaint Database (public; updated daily). Field reference includes: complaint ID, date received, product, sub-product, issue, sub-issue, consumer narrative (where consent flag set), company response, company public response, state, ZIP3, tags, consumer-consent-provided indicator, submitted-via, date sent to company, timely response indicator, consumer disputed indicator (legacy field).
- Excerpt-paraphrase: The Database publishes complaints submitted to the CFPB consumer portal and routed to the named company through the bureau's company portal. The bureau's product / sub-product / issue / sub-issue taxonomy is the public coding scheme; firms maintain parallel internal taxonomies. The consumer-narrative field is published only where the consumer consents; ZIP-level geographic data is published at ZIP3 to limit reidentification risk. The Database is the public anchor for company-vs-peer complaint comparison and for industry-wide theme observation.
- Link: https://www.consumerfinance.gov/data-research/consumer-complaints/ — Database landing page; field documentation at the API and download-data sections [verify section]
- Notes: The Database is one channel, not the firm's full complaint surface. Firm-direct channels (call center, web form, branch escalation, executive resolution) typically dwarf the CFPB-portal subset. Theme analysis deduplicates the CFPB-portal subset against the firm's internal records where the consent flag and matching identifiers permit.

### 2. CFPB Compliance Management System examination procedures

- Citation: Consumer Financial Protection Bureau, Supervision and Examination Manual, Compliance Management Review module (current edition) [verify edition date; the bureau periodically refreshes the manual and the CMR module has been updated multiple times since the original 2012 release].
- Excerpt-paraphrase: The CMR module sets the bureau's examination expectations for compliance management systems. Complaint management is one of the named CMS pillars: the module addresses the firm's complaint-intake process, the complaint-handling timeliness and accuracy, the complaint-data analysis and theme identification, the root-cause analysis and corrective-action process, the trending and escalation, and the board / committee reporting. Examiners assess whether the complaint-management program identifies emerging risks and feeds them into the firm's broader compliance and risk-management framework.
- Link: https://www.consumerfinance.gov/compliance/supervision-examinations/ — Supervision and Examination Manual, Compliance Management Review module section [verify section]
- Notes: The module is the operational anchor for what regulators expect from a complaint-theme analysis. Where the manual edition has rotated, cite the operative edition at memo date.

### 3. Dodd-Frank §1031 — Prohibition on unfair, deceptive, or abusive acts or practices

- Citation: Consumer Financial Protection Act, Section 1031, 12 U.S.C. §5531: §5531(a) general powers; §5531(c) standard for unfairness; §5531(d) standard for abusiveness.
- Excerpt-paraphrase: §5531(c) provides the unfairness standard (substantial injury that is not reasonably avoidable and is not outweighed by countervailing benefits). §5531(d) provides the abusiveness standard (material interference with consumer understanding; unreasonable advantage of consumer lack of understanding, inability to protect interests, or reasonable reliance). Complaint themes function as one of the indicators of unfairness, deception, or abusiveness in the bureau's supervisory and enforcement practice; the theme analysis surfaces signal that the cross-skill chain into `udaap-risk-review` carries to element-by-element analysis.
- Link: https://www.law.cornell.edu/uscode/text/12/5531 — §5531(c) unfairness standard and §5531(d) abusiveness standard
- Notes: Theme analysis cites §1031 where complaint themes raise the elements; the theme analysis does not finalise UDAAP determinations.

### 4. Dodd-Frank §1036 — Prohibited acts

- Citation: Consumer Financial Protection Act, Section 1036, 12 U.S.C. §5536: §5536(a)(1)(B) prohibition on UDAAPs.
- Excerpt-paraphrase: §5536(a)(1)(B) makes it unlawful for any covered person or service provider to engage in any unfair, deceptive, or abusive act or practice. Complaint themes that surface a §1031 fact pattern feed the §1036 prohibition through the cross-skill chain.
- Link: https://www.law.cornell.edu/uscode/text/12/5536 — §5536(a)(1)(B) prohibition

### 5. CFPB Supervisory Highlights (recent editions)

- Citation: CFPB Supervisory Highlights, most recent two issues at memo date [verify issue numbers and publication dates]; the bureau publishes Supervisory Highlights periodically (typically twice yearly), each issue covering recent supervisory observations across the consumer financial-services markets.
- Excerpt-paraphrase: Each issue surfaces complaint-driven and complaint-adjacent supervisory observations: unanticipated overdraft fees, surprise representment NSF fees, mortgage-servicing loss-mit conduct, force-placed insurance pricing, credit-card fee disclosure, deferred-interest mechanics, debt-collection conduct, P2P unauthorised-transfer-dispute conduct, and others. The Highlights are not enforcement actions; they are bureau-stated supervisory observations and signal areas of focus that the firm's theme analysis mirrors against firm-internal themes.
- Link: https://www.consumerfinance.gov/data-research/research-reports/supervisory-highlights/ — Supervisory Highlights index page, issue index section; cite the operative two issues at memo date [verify section]
- Notes: The Highlights are the canonical source for "what the bureau is currently looking at". A quarterly or annual theme pack mirrors the bureau's focal items against firm-internal themes; convergence is signal, divergence is also signal.

### 6. Joint Statement on Enforcement of Civil Rights, Fair Lending, Fair Housing, and Consumer Financial Protection Laws (April 2023)

- Citation: Joint Statement issued April 25, 2023 by the Consumer Financial Protection Bureau, the Civil Rights Division of the Department of Justice, the Federal Trade Commission, and the Equal Employment Opportunity Commission, "Joint Statement on Enforcement Efforts Against Discrimination and Bias in Automated Systems".
- Excerpt-paraphrase: The four agencies confirm that existing legal authorities apply to the use of automated systems and innovative new technologies in the consumer financial-services context. The statement is the cross-agency anchor for treating complaint themes that surface algorithmic-discrimination patterns as consequential under existing UDAAP, ECOA, FCRA, and FTC Act §5 authority. Novel technology is not a defence; the same theme-analysis discipline applies whether the firm's surface is human-driven or model-driven.
- Link: https://www.consumerfinance.gov/about-us/newsroom/cfpb-federal-partners-confirm-automated-systems-advanced-technology-not-an-excuse-for-lawbreaking-behavior/ — Joint Statement text, signatories section
- Notes: Cite where complaint themes surface algorithmic decisions, AI agents, AI-generated communications, or dynamic-disclosure surfaces.

### 7. Reg B 12 CFR §1002.9 — Adverse-action notification

- Citation: Equal Credit Opportunity Act, Regulation B, 12 CFR §1002.9 (notifications); §1002.9(a)(2) (statement of specific reasons); §1002.9(b)(2) (form of ECOA notice).
- Excerpt-paraphrase: Regulation B requires creditors to provide adverse-action notices with statements of specific reasons. Complaint themes that touch AAN content (consumers complaining that the reason coding does not match their understanding of the decision; consumers complaining that the AAN does not arrive in the required time) feed the cross-skill chain into `adverse-action-review`. The bureau's framing in CFPB Circular 2022-03 and Circular 2023-03 reaches AAN content where complex algorithms are in path.
- Link: https://www.ecfr.gov/current/title-12/chapter-X/part-1002/section-1002.9 — Reg B §1002.9
- Notes: Cited where complaint themes touch AAN content, reason-code specificity, or the timing of adverse-action notices.

### 8. Reg Z 12 CFR Part 1026 — Truth in Lending

- Citation: Truth in Lending Act, Regulation Z, 12 CFR Part 1026: §1026.6 (account-opening disclosures for open-end credit), §1026.16 (advertising of open-end credit), §1026.17 (general disclosure requirements for closed-end credit), §1026.24 (advertising of closed-end credit), §1026.40 (HELOC disclosures), §1026.41 (mortgage-servicing periodic statements), §1026.52 (limitations on credit-card fees, including the late-fee provisions [verify operative status given litigation history on the March 2024 amendment]), §1026.53 (allocation of payments), §1026.60 (credit-card application disclosures).
- Excerpt-paraphrase: Reg Z anchors the disclosure-related complaint themes across credit products: APR / fee disclosure complaints map to §1026.6, §1026.17, §1026.24, §1026.40, and §1026.60; payment-application complaints map to §1026.53; mortgage-servicing-statement complaints map to §1026.41; late-fee complaints map to §1026.52 and the operative late-fee rule status. The theme analysis cites the operative section per theme.
- Link: https://www.ecfr.gov/current/title-12/chapter-X/part-1026 — Reg Z, 12 CFR Part 1026, sections cited above
- Notes: Cited per theme. Verify §1026.52 operative status at memo date given the 2024 amendment and subsequent litigation.

### 9. CFPB Circular 2022-06 — Unanticipated overdraft fee assessment practices (withdrawn May 12, 2025)

- Citation: CFPB Circular 2022-06 (October 26, 2022), "Unanticipated Overdraft Fee Assessment Practices". **Withdrawn by the CFPB on May 12, 2025**.
- Excerpt-paraphrase: The circular addressed overdraft fees assessed where the consumer could not reasonably anticipate them, including the authorize-positive-settle-negative (APSN) pattern.
- Link: https://www.consumerfinance.gov/compliance/circulars/circular-2022-06-unanticipated-overdraft-fee-assessment-practices/ — Circular sections "Question Presented" and "Response"
- Notes: Withdrawn. Deposit-overdraft themes still anchor regulatory exposure to §1031 unfairness on the statute. State AGs and class-action plaintiffs continue to pursue APSN fact patterns. Banking sector overlay anchor.

### 10. CFPB Circular 2022-04 — Insufficient funds fees on representment (withdrawn May 12, 2025)

- Citation: CFPB Circular 2022-04 (October 26, 2022), "Insufficient funds fees charged on transactions that the consumer's bank has previously declined". **Withdrawn by the CFPB on May 12, 2025**.
- Excerpt-paraphrase: The circular addressed surprise representment NSF fees on previously-declined transactions resubmitted by the merchant.
- Link: https://www.consumerfinance.gov/compliance/circulars/circular-2022-04-insufficient-funds-fees-charged-on-transactions-that-the-consumers-bank-has-previously-declined-on-presentment/ — Circular sections "Question Presented" and "Response"
- Notes: Withdrawn. Surprise-representment themes still anchor to §1031 on the statute. Multiple banks have already paid restitution under interagency consent orders pre-dating the withdrawal; those orders remain in force. Banking sector overlay anchor.

### 11. CFPB Circulars 2022-03 and 2023-03 — Adverse-action notification with complex algorithms (withdrawn May 12, 2025)

- Citation: CFPB Circular 2022-03 (May 26, 2022) and CFPB Circular 2023-03 (September 19, 2023). **Both withdrawn by the CFPB on May 12, 2025**.
- Excerpt-paraphrase: The circulars took the position that complex algorithms do not relieve creditors of the Reg B specificity requirement, and that pretextual or sample-list reasons do not satisfy §1002.9(a)(2).
- Link: https://www.consumerfinance.gov/compliance/circulars/circular-2022-03-adverse-action-notification-requirements-in-connection-with-credit-decisions-based-on-complex-algorithms/ ; https://www.consumerfinance.gov/compliance/circulars/circular-2023-03-adverse-action-notification-requirements-and-the-proper-use-of-the-cfpbs-sample-forms-provided-in-regulation-b/
- Notes: Withdrawn. The substantive Reg B §1002.9 obligation and the Staff Commentary on specificity remain operative; complaint themes on AAN content map to the regulation directly and feed the cross-skill chain into `adverse-action-review`.

### 12. FCRA / Reg V furnisher-conduct authority

- Citation: Fair Credit Reporting Act, 15 U.S.C. §1681s-2 (responsibilities of furnishers of information to consumer reporting agencies); Regulation V, 12 CFR Part 1022; specifically §1022.41–43 (accuracy and integrity guidelines) and §1022.74 (duties of furnishers upon notice of dispute).
- Excerpt-paraphrase: Furnishers of credit-bureau information have accuracy, integrity, and dispute-investigation obligations. Complaint themes in the population that surface furnisher-conduct concerns (consumers complaining that the firm reported information that does not match their record; that the firm did not investigate a dispute properly; that the firm did not correct after dispute) cite §1681s-2 and §1022.74, and feed the cross-skill chain into the firm's FCRA dispute-handling workflow (outside this skill's scope).
- Link: https://www.law.cornell.edu/uscode/text/15/1681s-2 — FCRA §1681s-2; https://www.ecfr.gov/current/title-12/chapter-X/part-1022 — Reg V
- Notes: Cited where complaint themes touch credit-reporting accuracy or dispute conduct.

### 13. Reg E 12 CFR §1005.11 — Error resolution

- Citation: Electronic Fund Transfer Act, 15 U.S.C. §1693f; Regulation E, 12 CFR §1005.11 (procedures for resolving errors); §1005.6 (consumer liability for unauthorised EFT).
- Excerpt-paraphrase: Regulation E §1005.11 sets the error-resolution process for unauthorised electronic fund transfers and other notice-of-error fact patterns; §1005.6 limits consumer liability. Complaint themes in the P2P, instant-payment, and prepaid-card population frequently raise §1005.11 process concerns (timing of provisional credit; depth of investigation; final-determination communication) and the contested §1005.6 boundary on consumer-authorised-but-deceived fact patterns.
- Link: https://www.ecfr.gov/current/title-12/chapter-X/part-1005 — Reg E, sections 1005.6 and 1005.11
- Notes: Payments-fintech sector overlay anchor.

### 14. Reg X 12 CFR Part 1024 Subpart C — Mortgage servicing

- Citation: Real Estate Settlement Procedures Act, Regulation X, 12 CFR Part 1024 Subpart C: §1024.33 (transfer of servicing), §1024.36 (request for information / qualified written request), §1024.37 (force-placed insurance), §1024.39 (early intervention), §1024.40 (continuity of contact), §1024.41 (loss-mitigation procedures).
- Excerpt-paraphrase: Reg X Subpart C sets the operational baseline for mortgage-servicing conduct. Loss-mitigation themes (the repeatedly-lost-application pattern; clock-reset under §1024.41; continuity-of-contact gap under §1024.40); transfer-of-servicing themes; force-placed insurance themes; QWR-handling themes; and early-intervention themes all cite the operative §1024 section. Complaint themes in the mortgage-servicing population are tested against the literal Reg X requirements as a parallel inquiry to the UDAAP analysis.
- Link: https://www.ecfr.gov/current/title-12/chapter-X/part-1024 — Reg X, 12 CFR Part 1024 Subpart C, sections cited above
- Notes: Banking sector overlay anchor.

### 15. CFPB enforcement actions (worked-example anchors)

- Citation: CFPB enforcement actions index (https://www.consumerfinance.gov/enforcement/actions/), enforcement actions section. Cite by case name, docket number, date, and (where issued) consent-order URL.
- Excerpt-paraphrase: Public consent orders set the empirical reference for what the bureau treats as a complaint-theme-driven violation. Many consent orders document complaint volume and theme as part of the factual basis. The theme analysis derives structural patterns from this body without naming the institution unless the institution is a public defendant in a finalised order.
- Link: https://www.consumerfinance.gov/enforcement/actions/ — CFPB enforcement actions index, topic-filter section; filter by topic for the relevant fact pattern
- Notes: Cited where complaint themes echo a recent enforcement-theme parallel.

### 16. State attorney general consumer-finance complaint portals

- Citation: State AG consumer-protection complaint portals (each operative state). Examples include the New York Attorney General Consumer Frauds and Protection Bureau intake; the California Attorney General complaint intake; the Massachusetts Attorney General complaint intake.
- Excerpt-paraphrase: State AG complaint portals capture complaints that the consumer chose to route through a state authority rather than (or in addition to) the CFPB or the firm. State AGs have independent UDAP-equivalent enforcement authority under state consumer-protection statutes. The complaint-theme analysis pulls state AG complaints where the firm operates in those states and where the firm has a routing relationship with the state AG offices.
- Link: (varies by state; see each state AG website)
- Notes: Pulled selectively per the firm's footprint. State-AG-aggregated themes are a meaningful cross-channel signal where the state AG has a focal area.

## Secondary anchors (sector and cross-cutting)

### 17. CFPB BISG methodology

- Citation: Consumer Financial Protection Bureau, "Using publicly available information to proxy for unidentified race and ethnicity: A methodology and assessment", Summer 2014.
- Excerpt-paraphrase: The bureau's BISG (Bayesian Improved Surname Geocoding) methodology combines surname and geographic information to estimate consumer race / ethnicity probabilistically for non-mortgage consumer credit where self-reported demographics are not collected. The paper documents the method, the validation, and the limits (accuracy varies by geography, by surname distribution, by the granularity of the geographic input). Complaint-theme analysis uses BISG as a signal for demographic-skew enrichment; the analysis is explicit that BISG is signal-grade evidence, not finding-grade.
- Link: https://files.consumerfinance.gov/f/201409_cfpb_report_proxy-methodology.pdf — Methodology paper, sections "Proxy Methodology" and "Validation"
- Notes: BISG is signal, not proof. The fair-lending finding-grade analysis runs through `fair-lending-test-plan`, not through this skill.

### 18. Joint OCC, FRB, and FDIC Interagency Guidance on Third-Party Relationships (June 2023)

- Citation: OCC Bulletin 2023-17 / FRB SR 23-4 / FDIC FIL-29-2023, "Interagency Guidance on Third-Party Relationships: Risk Management" (issued June 6, 2023).
- Excerpt-paraphrase: The interagency guidance sets risk-management expectations for banking organizations engaging third parties, including fintech program operators. Where a complaint theme runs through a sponsor-bank-fintech program, the bank retains accountability; the theme analysis names the program-attribution per theme.
- Link: https://www.occ.gov/news-issuances/bulletins/2023/bulletin-2023-17.html — Bulletin 2023-17, sections on third-party risk-management lifecycle
- Notes: Payments-fintech sector overlay anchor.

### 19. FTC Negative Option Rule and dark-patterns themes

- Citation: FTC Negative Option Rule, 16 CFR Part 425; FTC "Bringing Dark Patterns to Light" report (September 2022).
- Excerpt-paraphrase: The FTC has framed dark patterns (deceptive design choices that manipulate consumers into actions they would not otherwise take) as a focal area; the September 2022 report catalogues recurring dark-pattern types (sneaking; urgency; misdirection; social proof; scarcity; obstruction; forced action). The Negative Option Rule (with the FTC's October 2024 amendments [verify operative status given litigation history]) addresses subscription, auto-renewal, and cancellation-difficulty patterns. Complaint themes that match dark-pattern frames cite both anchors and feed the cross-skill chain.
- Link: https://www.ftc.gov/legal-library/browse/rules/negative-option-rule — Negative Option Rule, 16 CFR Part 425, with the FTC's October 2024 amendments [verify operative status given litigation] ; https://www.ftc.gov/system/files/ftc_gov/pdf/P214800%20Dark%20Patterns%20Report%209.14.2022%20-%20FINAL.pdf — Dark Patterns report, sections on recurring dark-pattern types
- Notes: Verify operative status of the Click-to-Cancel amendments at memo date.

### 20. FINRA Rule 4513 / 4530 — Customer complaint records and reporting

- Citation: FINRA Rule 4513 (Records of Written Customer Complaints); FINRA Rule 4530 (Reporting Requirements), particularly Rule 4530(d) (statistical and summary information about written customer complaints).
- Excerpt-paraphrase: FINRA member firms must maintain written customer complaint records (Rule 4513) and report statistical and summary information about written customer complaints quarterly to FINRA (Rule 4530(d)). Capital-markets sector complaint-theme analysis runs the same theming method on retail-brokerage complaints, with regulatory exposure citing the FINRA framework rather than the CFPB authorities.
- Link: https://www.finra.org/rules-guidance/rulebooks/finra-rules/4513 — FINRA Rule 4513, sections on customer-complaint records ; https://www.finra.org/rules-guidance/rulebooks/finra-rules/4530 — FINRA Rule 4530, section (d) statistical reporting
- Notes: Capital-markets sector overlay anchor.

### 21. NAIC Unfair Trade Practices Act (Model #880) and Unfair Claims Settlement Practices Act (Model #900)

- Citation: NAIC Unfair Trade Practices Act (Model #880); NAIC Unfair Claims Settlement Practices Act (Model #900); state-DOI consumer complaint frameworks implementing the models.
- Excerpt-paraphrase: Insurance complaint-handling sits with state insurance departments under the NAIC framework. Model #880 addresses unfair underwriting and marketing practices; Model #900 addresses unfair claims-settlement conduct. Adoption varies by state. Insurance-sector complaint-theme analysis cites the operative state's adoption of the relevant model.
- Link: https://content.naic.org/sites/default/files/MO880.pdf — Model #880 [verify section]; Model #900 NAIC member library [verify section]
- Notes: Insurance sector overlay anchor.

### 22. NAIC Model Bulletin on AI (December 2023)

- Citation: NAIC Model Bulletin on the Use of Artificial Intelligence Systems by Insurers (adopted December 2023) [verify exact title and adoption status by state].
- Excerpt-paraphrase: The bulletin sets state-DOI expectations for insurers' use of AI / ML systems, including governance, validation, monitoring, and consumer-impact documentation. State adoption varies. Where complaint themes touch AI surfaces in insurance underwriting, pricing, claims, or communication, the bulletin and the operative state adoption are the operative anchors.
- Link: https://content.naic.org/sites/default/files/inline-files/2023-12-04%20Model%20Bulletin_Adopted_0.pdf — Model Bulletin, sections on governance, validation, and consumer-impact documentation [verify URL and section]
- Notes: Insurance sector overlay anchor for AI-flagged themes.

### 23. UK FCA Consumer Duty (informal cross-reference for global firms)

- Citation: FCA Principles for Businesses (PRIN), particularly the Consumer Duty (PRIN 2A), in force from July 31, 2023 for new and existing products open to sale.
- Excerpt-paraphrase: For global firms with UK operations, the Consumer Duty (PRIN 2A) sets a customer-outcome framework with the four outcomes (products and services; price and value; consumer understanding; consumer support). Complaint themes for UK-licensed entities can be analysed under the Consumer Duty alongside any US-jurisdictional framework.
- Link: https://www.handbook.fca.org.uk/handbook/PRIN/2A/ — PRIN 2A Consumer Duty, principle 12 and cross-cutting rules section
- Notes: Conduct cross-cutting overlay informal cross-reference for global firms.

## Verification flags

The following items carry `[verify section]` or `[verify ...]` flags and must be confirmed at SKILL.md write time and at memo-write time:

- CFPB Compliance Management Review module of the Supervision and Examination Manual — confirm current edition.
- CFPB Supervisory Highlights — confirm the operative two issues at memo date.
- Reg Z §1026.52 (credit-card late fee provision) — confirm operative status given the March 2024 amendment and litigation history.
- FTC Negative Option Rule (Click-to-Cancel amendments) — confirm operative status given litigation.
- NAIC Models #880 and #900 — confirm current model edition and operative state adoption.
- NAIC Model Bulletin on AI (December 2023) — confirm exact title and operative state adoption.
- Newer (2024 to 2026) CFPB circulars and policy statements — sweep https://www.consumerfinance.gov/compliance/circulars/ at memo date and add any newer items relevant to in-scope themes. Do not invent.
- HUD discriminatory-effects standard at 24 CFR §100.500 — confirm current operative version.

Where verification is incomplete, the SKILL.md cites with the `[verify section]` flag carried forward; do not invent.

## Firm overlay placeholder

A firm using this skill in production overlays its policy, taxonomy, and named owners via `references/firm-overlay.md` (not committed in this repo). The firm overlay does not modify this source-anchors file. An advisory firm shipping a client-specific overlay does the same thing under a separate overlay file.
