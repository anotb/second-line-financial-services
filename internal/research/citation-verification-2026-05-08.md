# Citation verification dossier — 2026-05-08

Read-only verification of Codex action-plan claims against official sources. Verdicts are mine, not Codex's. Where the truth is messier than the action-plan, I say so.

---

## P0 launch-blocker currency claims

### 1. OCC Bulletin 2026-13 GenAI/agentic scope

- **Codex claim:** OCC Bulletin 2026-13 explicitly excludes GenAI and agentic AI from scope. The bulletin is the joint interagency Revised Model Risk Management Guidance.
- **Verdict:** CONFIRMED.
- **Official source(s):**
  - https://occ.gov/news-issuances/bulletins/2026/bulletin-2026-13a.pdf (the guidance text PDF, 12 pages)
  - https://www.occ.treas.gov/news-issuances/bulletins/2026/bulletin-2026-13.html (OCC bulletin landing page, dated April 17, 2026)
  - https://www.federalreserve.gov/supervisionreg/srletters/SR2602.htm (FRB SR 26-2 parallel)
  - https://www.fdic.gov/news/financial-institution-letters/2026/agencies-revise-interagency-model-risk-management-guidance (FDIC FIL-15-2026 parallel)
- **Verified text snippet:** Footnote 3 of the joint guidance text: "Generative AI and agentic AI models are novel and rapidly evolving. As such, they are not within the scope of this guidance. Nonetheless, a banking organization's risk management and governance practices should guide the determination of appropriate governance and controls for any tools, processes, or systems not covered in this document. However, the principles described in this guidance apply to traditional statistical and quantitative models and non-generative, non-agentic AI models." Section II further clarifies the guidance "is expected to be most relevant to banking organizations with over $30 billion in total assets" and that "non-compliance with this guidance will not result in supervisory criticism" since it does "not set forth enforceable standards or prescriptive requirements" (Section I, footnote 1 referencing 12 CFR Part 4 Subpart F Appendix A (OCC), 12 CFR Part 262 Appendix A (Board), 12 CFR Part 302 Appendix A (FDIC)).
- **NIST references:** A `grep` of the entire 12-page PDF for "NIST" or "nist" returns ZERO matches. The bulletin does not reference NIST AI RMF, NIST AI 600-1, or any other NIST publication. The model-definition language is the bulletin's own ("a complex quantitative method, system, or approach that applies statistical, economic, or financial theories to process input data into quantitative estimates" — Section II), and explicitly excludes "simple arithmetic calculations, such as those found within spreadsheets, as well as deterministic rule-based processes and software where there are no statistical, economic, or financial theories underpinning their design or use."
- **Recommended cite/text for skills:** "Joint Interagency Revised Guidance on Model Risk Management, OCC Bulletin 2026-13 / FRB SR 26-2 / FDIC FIL-15-2026, dated April 17, 2026, supersedes SR 11-7 (2011) and SR 21-8 (the AML model-risk interagency statement). The guidance is most relevant to banking organizations with total assets over $30 billion and is non-binding (does not set forth enforceable standards). Generative AI and agentic AI models are explicitly out of scope (footnote 3); the guidance principles cover only traditional statistical / quantitative models and non-generative, non-agentic AI models. The bulletin does not reference NIST AI RMF or NIST AI 600-1 — those are separate, voluntary, and non-bank-supervisory frameworks. Where AIS / GenAI governance is the artifact's subject, the guidance must be cited as analogous principle reference, not as the controlling federal model-risk standard."
- **Affected skill files:** widespread; sample from `grep -l "OCC.*2026-13\|Bulletin 2026-13\|SR 11-7"`:
  - `plugins/sector-plugins/banking-risk-compliance/skills/banking-supervision-readiness/SKILL.md`
  - `plugins/sector-plugins/insurance-risk-compliance/skills/life-health-pricing-governance/SKILL.md` (and source-anchors / overlays)
  - `plugins/capability-plugins/ai-governance-model-risk/skills/model-card-builder/SKILL.md`
  - `plugins/capability-plugins/financial-crime-governance/skills/aml-model-monitoring/`
  - many others — see grep at section bottom
- **Notes/caveats:** The supersession of SR 21-8 (AML model-risk) is consequential for AML monitoring skills that previously cited it. The new joint guidance does cover BSA/AML model use under its general principles, but stops short of bank-AML-specific prescription. Treat any prior citation of SR 21-8 as superseded by 2026-13 / SR 26-2 / FIL-15-2026.

---

### 2. FRB SR 26-2 + FDIC FIL-15-2026 parallels

- **Codex claim:** SR 26-2 and FIL-15-2026 are the FRB and FDIC parallels to OCC 2026-13.
- **Verdict:** CONFIRMED. They are not "parallels" in the sense of being separate guidance — they are the SAME joint document issued through each agency's issuance machinery. Same date (April 17, 2026), same text, same signatories.
- **Official source(s):**
  - https://www.federalreserve.gov/supervisionreg/srletters/SR2602.htm
  - https://www.federalreserve.gov/supervisionreg/srletters/SR2602.pdf (full attachment text)
  - https://www.fdic.gov/news/financial-institution-letters/2026/agencies-revise-interagency-model-risk-management-guidance
- **Verified text snippet:** SR 26-2 page: "The Board of Governors of the Federal Reserve System, Office of the Comptroller of the Currency (OCC), and Federal Deposit Insurance Corporation (FDIC) (the 'agencies') are issuing the attached Revised Guidance on Model Risk Management, which supersedes and replaces SR letter 11-7, Guidance on Model Risk Management (issued April 4, 2011) and SR letter 21-8, Interagency Statement on Model Risk Management for Bank Systems Supporting Bank Secrecy Act/Anti-Money Laundering Compliance (issued April 9, 2021)." FDIC FIL-15-2026 confirms FDIC rescinded FIL-22-2017 and FIL-27-2021 in parallel.
- **Recommended cite/text for skills:** Cite all three together in one breath. "Joint interagency Revised Guidance on Model Risk Management (OCC Bulletin 2026-13 / FRB SR 26-2 / FDIC FIL-15-2026, April 17, 2026)." Treat as one document with three bibliographic anchors.
- **Affected skill files:** every file that referenced SR 11-7 or SR 21-8 needs to be updated. Counting via grep, that is most banking-, model-, and AML-touching skills.
- **Notes/caveats:** None. This is the cleanest claim in the action-plan.

---

### 3. FinCEN MSB registration cite — §1022.380 vs §1010.380

- **Codex claim:** FinCEN's current MSB-registration material points to 31 CFR §1022.380, not §1010.380. Distinct from §1010.380, which is the BOI / CTA reporting rule.
- **Verdict:** CONFIRMED.
- **Official source(s):**
  - https://www.fincen.gov/resources/money-services-business-msb-registration (the FinCEN page itself)
  - https://www.ecfr.gov/current/title-31/subtitle-B/chapter-X/part-1022/subpart-D/section-1022.380 (eCFR location)
- **Verified text snippet:** A `grep` of the live FinCEN MSB-registration HTML page returns 9 references to §1022.380 and zero references to §1010.380. The eCFR places MSB registration at 31 CFR §1022.380 and BOI reporting at 31 CFR §1010.380 (different subparts: 1010 Subpart D vs 1022 Subpart D).
- **Recommended cite/text for skills:** "FinCEN MSB rules at 31 CFR Part 1022; MSB registration requirements at 31 CFR §1022.380 (initial registration within 180 days of becoming an MSB, renewal every two years). Note: 31 CFR §1010.380 is the Beneficial Ownership / Corporate Transparency Act reporting rule, a separate obligation with its own legal status." Drop the `[verify section]` flags wherever they occur next to §1010.380 in MSB context — those should be hard-changed to §1022.380.
- **Affected skill files (grep results):**
  - `plugins/sector-plugins/payments-fintech-compliance/skills/payment-operations-incident-review/references/source-anchors.md` (uses §1010.380 for MSB registration — WRONG)
  - `plugins/sector-plugins/payments-fintech-compliance/skills/payments-risk-assessment/references/source-anchors.md` (same)
  - `plugins/sector-plugins/payments-fintech-compliance/skills/payments-risk-assessment/references/sector-overlays/payments-fintech.md` (same)
  - `plugins/sector-plugins/payments-fintech-compliance/skills/payments-risk-assessment/examples/cross-border-remittance-rtp-corridor-add.md` (same)
  - `plugins/sector-plugins/payments-fintech-compliance/skills/fintech-partner-controls/SKILL.md` (same)
  - `plugins/sector-plugins/payments-fintech-compliance/skills/fintech-partner-controls/references/source-anchors.md` (same)
  - `plugins/capability-plugins/third-party-operational-resilience/skills/contract-gap-review/references/source-anchors.md` (uses §1010.380 with `[verify §]`)
  - `plugins/capability-plugins/third-party-operational-resilience/skills/contract-gap-review/references/sector-overlays/payments-fintech.md` (same)
  - `plugins/capability-plugins/third-party-operational-resilience/skills/criticality-assessment/references/sector-overlays/payments-fintech.md` (same)
  - `plugins/capability-plugins/third-party-operational-resilience/skills/concentration-risk-review/references/source-anchors.md` (same)
  - `plugins/capability-plugins/third-party-operational-resilience/skills/concentration-risk-review/references/sector-overlays/payments-fintech.md` (same)
  - `plugins/capability-plugins/financial-crime-governance/skills/sanctions-screening-qa/references/sector-overlays/payments-fintech.md` (same)
  - `plugins/capability-plugins/financial-crime-governance/skills/sar-decision-qa/references/sector-overlays/payments-fintech.md` (same)
  - The vendor-diligence source-anchors file has it RIGHT (§1022.380) and even calls out the BOI distinction — that file is the model.
- **Notes/caveats:** §1010.380 BOI status is volatile (March 26, 2025 IFR exempted US persons; only foreign reporting companies remain in scope as of this date). The repo's BOI-as-of-date posture is correct; just don't accidentally collapse MSB registration into the same paragraph.

---

### 4. CFPB 1071 thresholds + dates (May 1, 2026 final rule)

- **Codex claim:** CFPB issued a final rule on May 1, 2026; covered-financial-institution threshold raised to 1,000 covered credit transactions; effective June 30, 2026; compliance January 1, 2028.
- **Verdict:** CONFIRMED.
- **Official source(s):**
  - https://www.federalregister.gov/documents/2026/05/01/2026-08494/small-business-lending-under-the-equal-credit-opportunity-act-regulation-b
  - https://www.consumerfinance.gov/rules-policy/final-rules/small-business-lending-under-the-equal-credit-opportunity-act-regulation-b-2026/
- **Verified text snippet:** The May 1, 2026 final rule raises the origination threshold to 1,000 covered credit originations (in each of the two preceding calendar years), reduces the small-business definition revenue threshold from $5M to $1M in gross annual revenue, excludes merchant cash advances, agricultural lending, small-dollar business loans of $1,000 or less, and Farm Credit System lenders. Effective June 30, 2026, with a compliance date of January 1, 2028 and a one-year grace period through December 31, 2028.
- **Recommended cite/text for skills:** "CFPB 1071 / Regulation B small-business lending data collection final rule (CFPB, May 1, 2026; effective June 30, 2026; compliance date January 1, 2028 with grace period through December 31, 2028). Covered financial institution threshold is 1,000 covered credit originations in each of the two preceding calendar years; small-business gross annual revenue threshold is $1M; merchant cash advances, agricultural lending, small-dollar business loans ≤$1,000, and Farm Credit System lenders are excluded. Earlier 100-transaction thresholds and litigation-stay-driven compliance dates from the 2023 rule are superseded."
- **Affected skill files:** any skill citing 1071 thresholds — `banking-risk-compliance/skills/credit-risk-governance/SKILL.md` and `references/source-anchors.md`, `consumer-compliance-fair-lending` skills, etc.
- **Notes/caveats:** The pre-2026 Jefferson Bankshares stay timeline and the prior 100-transaction threshold are now historical. Cite the May 2026 final rule, not the 2023 rule.

---

### 5. CFPB May 12, 2025 guidance withdrawal

- **Codex claim:** CFPB withdrew circulars, policy statements, advisory opinions, and the BNPL interpretive rule on May 12, 2025.
- **Verdict:** CONFIRMED. Magnitude: 67 documents.
- **Official source(s):**
  - https://www.federalregister.gov/documents/2025/05/12/2025-08286/interpretive-rules-policy-statements-and-advisory-opinions-withdrawal
  - https://www.consumerfinance.gov/rules-policy/final-rules/use-of-digital-user-accounts-to-access-buy-now-pay-later-loans/ (BNPL interpretive rule landing page)
- **Verified text snippet:** Per the Federal Register notice, withdrawals applicable as of May 12, 2025 cover 8 policy statements, 7 interpretive rules, 13 advisory opinions, and 39 pieces of other guidance (67 total). Coverage spans FCRA, TILA, UDAAP under CFPA, and EFTA. The 2024 BNPL interpretive rule (digital user accounts as Regulation Z card-issuer rule) is among the withdrawn items.
- **Recommended cite/text for skills:** "On May 12, 2025, the CFPB withdrew 67 guidance documents — including 8 policy statements, 7 interpretive rules, 13 advisory opinions, and 39 other guidance items — including the 2024 BNPL Digital User Account interpretive rule. Withdrawn guidance is no longer enforceable as CFPB policy and should not be cited as live obligation. Subject-matter scope of UDAAP, ECOA / Reg B, EFTA, FCRA, TILA, and FDCPA continues to apply through statute and the underlying rules; only the interpretive overlay was withdrawn. The withdrawal Federal Register notice (90 FR 19945, May 12, 2025) is the authoritative list."
- **Affected skill files:** any file citing CFPB advisory opinions, circulars, or the BNPL interpretive rule as live guidance. The `consumer-compliance-fair-lending` skills and any BNPL-touching payments skill will need re-anchoring to the underlying statute / regulation rather than the withdrawn interpretive layer.
- **Notes/caveats:** This is a deregulatory action by the post-January-2025 CFPB. The underlying statutes and Regulation Z, B, V, etc. remain in force; the agency simply removed its interpretive gloss.

---

### 6. CFPB digital payment-app larger-participant rule + Public Law 119-11

- **Codex claim:** Public Law 119-11 nullified the CFPB's December 2024 larger-participant rule for general-use digital consumer payment applications via the Congressional Review Act.
- **Verdict:** CONFIRMED.
- **Official source(s):**
  - https://www.congress.gov/bill/119th-congress/senate-joint-resolution/28 (S.J.Res.28, signed May 9, 2025, P.L. 119-11)
  - https://www.federalregister.gov/documents/2024/12/10/2024-27836/defining-larger-participants-of-a-market-for-general-use-digital-consumer-payment-applications (the original December 2024 rule)
- **Verified text snippet:** S.J.Res.28 of the 119th Congress, signed by the President on May 9, 2025 as Public Law 119-11, disapproved the CFPB's "Defining Larger Participants of a Market for General-Use Digital Consumer Payment Applications" rule (originally effective January 9, 2025). The CRA disapproval has the effect of nullifying the rule and precluding the CFPB from issuing a substantially similar rule unless re-authorized by subsequent legislation.
- **Recommended cite/text for skills:** "The CFPB's December 2024 general-use digital consumer payment applications larger-participant rule (89 FR 99582) was nullified via Congressional Review Act resolution S.J.Res.28, signed as Public Law 119-11 on May 9, 2025. As a result, the rule is not in force and the CFPB is barred from re-promulgating substantially similar designation criteria absent new statutory authority. CFPB direct-supervision posture for digital wallet and digital consumer payment app providers should not be assumed; verify on the analysis date."
- **Affected skill files:** `plugins/sector-plugins/payments-fintech-compliance/skills/fintech-partner-controls/SKILL.md` cites the December 2024 rule — needs CRA-disapproval framing. Search for "larger-participant rule" / "December 2024" / "digital consumer payment applications" across the payments and fintech skills.
- **Notes/caveats:** None significant.

---

### 7. CFPB 1033 status as of October 29, 2025

- **Codex claim:** Compliance dates "stayed"; ANPR / reconsideration posture from August 22, 2025.
- **Verdict:** CONFIRMED, with a precision tweak. The compliance dates were JUDICIALLY STAYED on October 29, 2025 by the court in Forcht Bank, N.A. v. CFPB. The August 22, 2025 ANPR is a separate CFPB-initiated reconsideration. The two are coincident but not the same action.
- **Official source(s):**
  - https://www.consumerfinance.gov/rules-policy/rules-under-development/personal-financial-data-rights-reconsideration/ (ANPR landing page, last modified Aug 22, 2025)
  - https://www.federalregister.gov/documents/2025/08/22/2025-16139/personal-financial-data-rights-reconsideration (ANPR Federal Register notice)
  - https://www.ecfr.gov/current/title-12/chapter-X/part-1033 (codified rule text)
- **Verified text snippet:** CFPB ANPR (August 22, 2025): "The Consumer Financial Protection Bureau (CFPB) is seeking comments and data to inform its consideration of four issues related to implementation of section 1033... [representative scope, fee design, data security, data privacy]." Comment period closed October 21, 2025. Separately, on October 29, 2025, the court in Forcht Bank, N.A., et al. v. Consumer Financial Protection Bureau, et al. stayed the rule's compliance dates pending litigation. As of this date the rule is codified at 12 CFR Part 1033 with phased compliance dates (April 1, 2026 through April 1, 2030 in §1033.121(c)) but those are stayed pending litigation and the CFPB is reconsidering substance via ANPR / forthcoming rulemaking.
- **Recommended cite/text for skills:** "CFPB Personal Financial Data Rights Rule, 12 CFR Part 1033, finalized October 22, 2024. Phased compliance dates at §1033.121(c) (April 1, 2026; April 1, 2027; April 1, 2028; April 1, 2029; April 1, 2030 by data-provider-asset tier) are JUDICIALLY STAYED as of October 29, 2025 in Forcht Bank, N.A. et al. v. CFPB pending litigation. The CFPB issued an Advance Notice of Proposed Rulemaking on Personal Financial Data Rights Reconsideration on August 22, 2025 (90 FR 41099). As of the analysis date the rule is codified but compliance is not enforceable; verify rule-state on the engagement date."
- **Affected skill files:** open-banking, data-rights, payments-fintech and bank-fintech-partnership skills. Any reference to "April 1, 2026 compliance date" needs the stay overlay.
- **Notes/caveats:** Codex's word "stayed" is correct — but it's the COURT staying, not CFPB voluntarily staying. Different posture from the SEC climate situation (#13).

---

### 8. Reg E provisional-credit and investigation-window mechanics

- **Codex claim:** Examples currently use wrong "5 business days / 45/90 business days" patterns. Actual is 10 business days investigation, 45 days extension with provisional credit, 90 days for new-account / POS / foreign-initiated transactions.
- **Verdict:** CONFIRMED. The repo has BOTH right and wrong instances; Codex correctly flags the wrong ones.
- **Official source(s):**
  - https://www.consumerfinance.gov/rules-policy/regulations/1005/11/ (CFPB Reg E codified text)
  - https://www.ecfr.gov/current/title-12/chapter-X/part-1005/subpart-A/section-1005.11 (eCFR)
- **Verified text snippet:** §1005.11(c)(1) "Ten-day period. A financial institution shall investigate promptly and... shall determine whether an error occurred within 10 business days of receiving a notice of error." §1005.11(c)(2) "Forty-five day period. If the financial institution is unable to complete its investigation within 10 business days, the institution may take up to 45 days from receipt of a notice of error to investigate... provided the institution... [provisionally credits within 10 business days...]." §1005.11(c)(3) "Extension of time periods. The applicable time is 20 business days in place of 10 business days... if the notice of error involves an electronic fund transfer to or from the account within 30 days after the first deposit." §1005.11(c)(3)(ii) "The applicable time is 90 days in place of 45 days under paragraph (c)(2) of this section, for completing an investigation, if a notice of error involves an electronic fund transfer that: [POS, foreign-initiated, new-account scenarios]."
- **Critical clarification:** The 10 days and 20 days are explicitly "business days" in the rule. The 45 days and 90 days are NOT "business days" — the rule says "45 days" and "90 days" without the "business" modifier, which means CALENDAR days. This is the most common industry misstatement.
- **Recommended cite/text for skills:** "Regulation E §1005.11(c) error resolution timing: 10 business days to investigate (extended to 20 business days for new-account transactions in §1005.11(c)(3)(i) circumstances). If investigation cannot be completed in 10 business days, the institution may take up to 45 calendar days from receipt of notice provided it provisionally credits the consumer's account within 10 business days. The 45-calendar-day window extends to 90 calendar days for errors involving point-of-sale transactions, foreign-initiated transfers, or transfers to/from accounts that are within 30 days of first deposit (§1005.11(c)(3)(ii)). Provisional-credit clock is 10 business days, NOT 5; the institution must inform the consumer of the provisional credit within 2 business days after the credit is posted (§1005.11(c)(2)(ii)). Final results notification: within 3 business days after investigation is complete."
- **Affected skill files (incorrect timing):**
  - `plugins/sector-plugins/banking-risk-compliance/skills/bank-fintech-partnership-review/references/sector-overlays/banking.md` (uses "5 for provisional credit" — WRONG; should be 10)
  - `plugins/sector-plugins/banking-risk-compliance/skills/bank-fintech-partnership-review/references/source-anchors.md` (uses "5 business days for provisional credit" — WRONG)
  - `plugins/sector-plugins/banking-risk-compliance/skills/bank-fintech-partnership-review/templates/default-output.md` (uses "5 business days for provisional credit" — WRONG)
  - `plugins/capability-plugins/compliance-testing/skills/control-sampling/references/sector-overlays/payments-fintech.md` (`Day-10 / day-5 provisional-credit timing under §1005.11(c) [verify timing]` — wrong; the 10 is the only regulatory clock; the 5 is firm-policy if anywhere)
  - `plugins/capability-plugins/compliance-testing/skills/control-sampling/references/sector-overlays/banking.md` (uses "11-45 business days, beyond 45 days" — should be calendar days)
  - `plugins/capability-plugins/compliance-testing/skills/qa-workpaper/references/sector-overlays/payments-fintech.md` (uses "45 days for completion or 90 days" — correctly omits "business days" but should be explicit)
- **Affected skill files (correct, keep):**
  - `plugins/sector-plugins/banking-risk-compliance/skills/deposit-operations-controls/references/source-anchors.md` (right: "10-business-day investigation window... 45-day full-investigation window (extended to 90 days for POS and foreign-initiated transactions)")
  - `plugins/capability-plugins/risk-compliance-core/skills/control-matrix/references/sector-overlays/payments-fintech.md` (right)
- **Notes/caveats:** The 5-business-day pattern likely originated as a firm-policy floor rather than a regulatory rule. If a skill is documenting a stricter firm policy, that is fine — but the regulatory baseline is 10 business days. Distinguish.

---

### 9. NAIC Model #880 vs #900 + #903

- **Codex claim:** Model #880 should be replaced with Model #900 as the fair-claims-settlement anchor; add Model #903 for life and A&H.
- **Verdict:** PARTIAL — depends on the skill. Codex is right that Model #880 (Unfair Trade Practices Act) is NOT the claims-handling anchor. But Model #880 IS the correct anchor for unfair-discrimination in pricing/rating. The repo uses #880 in BOTH contexts; only the claims-handling uses are wrong.
- **Official source(s):**
  - https://content.naic.org/sites/default/files/model-law-880.pdf (Model #880 — Unfair Trade Practices Act, includes §4(7) unfair discrimination in rates)
  - https://content.naic.org/sites/default/files/model-law-900.pdf (Model #900 — Unfair Claims Settlement Practices Act, separated out by NAIC in June 1990)
  - https://content.naic.org/sites/default/files/model-law-902.pdf (Model #902 — Unfair Property/Casualty Claims Settlement Practices Model REGULATION, July 1997)
  - https://content.naic.org/sites/default/files/model-law-903.pdf (Model #903 — Unfair Life, Accident and Health Claims Settlement Practices Model REGULATION, July 1997)
- **Verified text snippet:** Model #900 prefatory note: "By adopting this model act in June 1990, the NAIC separated issues regarding unfair claims settlement practices into a free-standing act apart from the NAIC Model Unfair Trade Practices Act. This change focuses more attention on unfair claims as a function of market conduct surveillance separate and apart from general unfair trade practices." Models #902 and #903 are the implementing REGULATIONS that operationalize Model #900 for P&C and Life/A&H respectively.
- **Recommended cite/text for skills:**
  - For **claim-handling oversight** (insurance-outsourcing-review delegated-claims context): cite "NAIC Unfair Claims Settlement Practices Act, Model #900 (1990) and the implementing model regulations Model #902 (Unfair Property/Casualty Claims Settlement Practices Model Regulation) for P&C and Model #903 (Unfair Life, Accident and Health Claims Settlement Practices Model Regulation) for life and A&H. State adoption varies; cite both the NAIC model and the state adoption as separate items per the NAIC source-anchors convention."
  - For **unfair-discrimination in pricing / rating** (life-health-pricing-governance): keep "NAIC Unfair Trade Practices Act, Model #880, §4(7) unfair discrimination" as the anchor — that is correct.
- **Affected skill files:**
  - `plugins/sector-plugins/insurance-risk-compliance/skills/insurance-outsourcing-review/SKILL.md` — uses #880 as the claims-handling anchor; WRONG; should be #900 + #902/#903
  - `plugins/sector-plugins/insurance-risk-compliance/skills/insurance-outsourcing-review/TROUBLESHOOTING.md` — line 27 conflates #880 with "unfair-claims-settlement-practices act"; WRONG; should split: #880 is unfair trade practices, #900 (with state-specific equivalents) is unfair claims settlement
  - `plugins/sector-plugins/insurance-risk-compliance/skills/insurance-outsourcing-review/TROUBLESHOOTING.md` — line 35 uses #880 for claims-handling oversight under TPA; WRONG; should be #900
  - `plugins/sector-plugins/insurance-risk-compliance/README.md` line 11 uses #880 where it means #900
  - `plugins/sector-plugins/insurance-risk-compliance/skills/life-health-pricing-governance/*` — KEEP #880 here (correct usage for unfair-discrimination in rating)
- **Notes/caveats:** State adoption matters. Several states adopted #880 in 1972 BEFORE NAIC separated #900 in 1990; some of those states still carry the unfair-claims provisions inside their state UTPA statute despite NAIC's model split. The repo's "name the NAIC model and the state adoption separately" convention from `references-first SKILL.md` design handles this gracefully.

---

### 10. FinCEN/interagency SAR FAQs October 9, 2025

- **Codex claim:** 90-day continuing SAR cadence is optional / firm policy; separate post-SAR continuing reviews not required; no-SAR documentation not required by BSA regulations.
- **Verdict:** CONFIRMED.
- **Official source(s):**
  - https://www.fincen.gov/resources/frequently-asked-questions-regarding-fincen-suspicious-activity-report-sar (FinCEN SAR FAQs page)
  - https://www.fincen.gov/system/files/2025-10/SAR-FAQs-October-2025.pdf (PDF of October 2025 FAQs)
  - https://www.occ.treas.gov/news-issuances/bulletins/2025/bulletin-2025-31a.pdf (OCC interagency parallel)
- **Verified text snippet:** FAQ release of October 9, 2025 (joint FinCEN / Federal Reserve / OCC / FDIC / NCUA): A financial institution is NOT required to conduct a separate review of a customer or account following the filing of a SAR to determine whether suspicious activity has continued. Institutions may rely on risk-based internal policies, procedures, and controls. The 90-day continuing-activity / 120-day deadline cadence (referenced in prior FinCEN guidance) is described as a recommended timing if an institution chooses that approach, NOT a regulatory requirement. No-SAR-decision documentation is not required by BSA regulations; firm policy may dictate it.
- **Recommended cite/text for skills:** "Per the joint FinCEN / federal banking agency SAR FAQs issued October 9, 2025, three clarifications apply: (1) a financial institution is not required to conduct a separate continuing-activity review after filing a SAR; risk-based monitoring policies satisfy the obligation. (2) The 90-day continuing-activity / 120-day filing deadline cadence is a recommended approach, not a regulatory requirement; institutions may rely on their risk-based policies. (3) No-SAR-decision documentation is not required by BSA regulations (31 CFR Part 1020 et seq.); any no-SAR documentation is firm-policy-driven, not regulatory. Where a skill assumes the 90-day cadence as a hard rule or treats no-SAR documentation as a regulatory requirement, the framing is now wrong post-October 9, 2025."
- **Affected skill files:** SAR-related skills under `financial-crime-governance` — `sar-decision-qa`, `cdd-risk-review`, `aml-model-monitoring`, edd-escalation-pack.
- **Notes/caveats:** Existing firm SAR policies that were calibrated to the prior 90-day-mandatory framing may now overshoot the regulatory floor. That is a finding the artifact can name (overcompliance-by-default) without claiming a regulatory rule that no longer exists.

---

### 11. FinCEN CDD updates (2026 exceptive relief, BOI domestic exemption, IA AML delay to Jan 1 2028)

- **Codex claim 11a (2026 CDD exceptive relief):** Real, scope = identification and verification of beneficial owners NOT required at each new account opening for an existing legal entity customer.
- **Verdict 11a:** CONFIRMED.
- **Official source(s):**
  - https://www.fincen.gov/news/news-releases/fincen-issues-exceptive-relief-streamline-customer-due-diligence-requirements (Feb 13, 2026 press release)
  - https://www.fincen.gov/system/files/2026-02/FinCEN-Order-CCDExceptiveRelief.pdf (FIN-2026-R001 order)
- **Verified text snippet:** FinCEN Order FIN-2026-R001, Exceptive Relief from Requirement to Identify and Verify Beneficial Owners at Each Account Opening (February 13, 2026). Excepts covered financial institutions from the 31 CFR §1010.230 requirement to identify and verify beneficial owners of a legal-entity customer each time the customer opens a new account. Verification is required only at first account opening, when the FI has knowledge of facts that would call into question the reliability of prior BOI, or as needed under risk-based ongoing CDD. Voluntary; institutions may continue at-each-opening verification if they choose.
- **Recommended cite/text for skills:** "FinCEN Order FIN-2026-R001 (Exceptive Relief from Requirement to Identify and Verify Beneficial Owners at Each Account Opening, February 13, 2026) excepts covered financial institutions from the requirement to re-verify legal-entity-customer beneficial owners at each new account opening. Verification is required only at (1) first account opening, (2) when the FI has knowledge of facts that call into question previously-obtained BOI, or (3) as needed under the FI's risk-based ongoing CDD. Election is voluntary."

- **Codex claim 11b (BOI domestic exemption March 2025):** Treasury / FinCEN issued an interim final rule in March 2025 effectively exempting US persons from BOI reporting.
- **Verdict 11b:** CONFIRMED.
- **Official source(s):**
  - https://www.fincen.gov/news/news-releases/fincen-removes-beneficial-ownership-reporting-requirements-us-companies-and-us
  - https://www.federalregister.gov/documents/2025/03/26/2025-05199/beneficial-ownership-information-reporting-requirement-revision-and-deadline-extension
  - https://www.fincen.gov/boi/ifr-qa
- **Verified text snippet:** The March 21, 2025 Treasury announcement and March 26, 2025 Federal Register publication of the IFR revise the definition of "reporting company" to include only foreign entities formed under foreign law and registered to do business in the US. All entities formed in the US (previously "domestic reporting companies") are exempt from BOI reporting. US persons are not required to report BOI as beneficial owners of foreign reporting companies that remain in scope.
- **Recommended cite/text for skills:** "FinCEN Interim Final Rule (March 26, 2025; 90 FR 13688) revising the BOI reporting framework: only foreign entities formed under foreign law and registered to do business in any US State or Tribal jurisdiction are 'reporting companies' subject to 31 CFR §1010.380. US-formed entities and US persons are exempt. Foreign entities registered before publication date had 30 days to file; entities registered on or after have 30 calendar days from registration. As of this date the rule is interim final and pending finalization. Verify rule-state on engagement date — the BOI history is volatile."

- **Codex claim 11c (IA AML rule delayed to January 1, 2028):** Real.
- **Verdict 11c:** CONFIRMED.
- **Official source(s):**
  - https://www.fincen.gov/news/news-releases/fincen-issues-final-rule-postpone-effective-date-investment-adviser-rule-2028
  - https://www.federalregister.gov/documents/2026/01/02/2025-24184/delaying-the-effective-date-of-the-anti-money-launderingcountering-the-financing-of-terrorism
- **Verified text snippet:** The IA AML Rule (AML/CFT program and SAR filing requirements for registered investment advisers and exempt reporting advisers, finalized 2024) had an original effective date of January 1, 2026. FinCEN's January 2026 final rule postpones the effective date by two years to January 1, 2028, in coordination with the SEC and pending FinCEN's review of the rule's tailoring to investment-adviser business models.
- **Recommended cite/text for skills:** "FinCEN Investment Adviser AML Rule effective date is January 1, 2028 (delayed from January 1, 2026 by FinCEN final rule, January 2, 2026; 91 FR 14). Until the effective date, AML/CFT program and SAR-filing obligations under the rule are not enforceable against RIAs / ERAs."
- **Affected skill files for #11 broadly:** capital-markets adviser-compliance skills, financial-crime-governance, CDD risk review.

---

### 12. OMB Circular A-4 status

- **Codex claim:** The 2023 revision was revoked and the 2003 version reinstated.
- **Verdict:** CONFIRMED. EO 14192 (January 31, 2025) and OMB Memo M-25-15 (March 2025) carry the action.
- **Official source(s):**
  - https://www.whitehouse.gov/wp-content/uploads/2025/03/M-25-15-Recission-and-Reinstatement-of-Circular-A-4.pdf (the operative OMB memo)
  - Executive Order 14192 (Unleashing Prosperity Through Deregulation), January 31, 2025
- **Verified text snippet:** OMB Memo M-25-15 rescinds the November 2023 revision of OMB Circular A-4 and reinstates the September 17, 2003 version effective immediately. The 2003 version is therefore the operative federal regulatory benefit-cost analysis guidance.
- **Recommended cite/text for skills:** "OMB Circular A-4, Regulatory Analysis (September 17, 2003 version, reinstated by OMB Memo M-25-15 in March 2025 following the rescission of the November 2023 revision pursuant to Executive Order 14192). Use the 2003 version's BCA framework; the 2023 revision is no longer in force. Note that any peer-review obligation for further A-4 changes remains."
- **Affected skill files:** any policy / regulatory-impact / risk-quantification skill that referenced the 2023 A-4 — likely `risk-compliance-core` scoping or risk-reporting skills.
- **Notes/caveats:** The 2003 A-4 and 2023 A-4 differ on, among other things, distributional weighting and global-vs-domestic accounting. Skills that rely on a specific A-4 framing should call out which version they are running against.

---

### 13. SEC climate rule status

- **Codex claim:** Stayed / non-operative.
- **Verdict:** CONFIRMED.
- **Official source(s):**
  - https://www.sec.gov/newsroom/press-releases/2025-58 (SEC Press Release 2025-58, March 27, 2025: SEC Votes to End Defense of Climate Disclosure Rules)
- **Verified text snippet:** The SEC's climate-related disclosure rules (March 2024 final rule) have never gone into effect. They were voluntarily stayed in April 2024 by the Commission pending the Eighth Circuit consolidated litigation. On March 27, 2025, the Commission voted to end its defense of the rules. On April 24, 2025 the Eighth Circuit held the case in abeyance pending SEC status reports; on September 12, 2025 the court continued the abeyance order. SEC has stated it does not intend to review or reconsider the rules. Net: rules remain stayed, SEC not defending, Eighth Circuit case in abeyance.
- **Recommended cite/text for skills:** "SEC Climate-Related Disclosure Rules (89 FR 21668, March 28, 2024) are stayed and non-operative. The Commission voluntarily stayed effectiveness in April 2024 pending Eighth Circuit litigation, voted to end its defense of the rules on March 27, 2025, and as of this date the Eighth Circuit case is held in abeyance. Public companies are not currently obligated to comply with the SEC climate disclosure rules. State-level climate disclosure regimes (California SB 253 / SB 261; New York; etc.) operate independently. Verify status on engagement date."
- **Affected skill files:** `risk-reporting/skills/cyber-disclosure-readiness` (if it touched climate), capital-markets disclosure skills.

---

### 14. SEC capital-markets withdrawals and extensions

- **Codex claim 14a (June 12, 2025 withdrawals — adviser/fund cyber and predictive-data-analytics proposals):** Real.
- **Verdict 14a:** CONFIRMED.
- **Official source(s):** SEC Press Release 2025-58 family; https://www.sec.gov/files/rules/final/2025/33-11377.pdf (the formal withdrawal release covering 14 proposals)
- **Verified text snippet:** On June 12, 2025, the SEC formally withdrew 14 outstanding rule proposals from the prior administration, including the predictive-data-analytics conflicts-of-interest proposal (originally proposed August 9, 2023) and the cybersecurity risk management proposal for broker-dealers and certain other market participants. Any future regulatory action in these areas would require restarting the rulemaking process.

- **Codex claim 14b (Rule 605 compliance extended to August 1, 2026):** Real.
- **Verdict 14b:** CONFIRMED.
- **Official source(s):**
  - https://www.federalregister.gov/documents/2025/10/02/2025-19316/extension-of-compliance-date-for-disclosure-of-order-execution-information
  - https://www.sec.gov/files/rules/final/2025/34-104147.pdf
- **Verified text snippet:** Compliance date for the April 2024 amendments to Rules 600 and 605 of Regulation NMS was extended from December 14, 2025 to August 1, 2026. Reporting entities must collect data starting August 1, 2026; reports for August 2026 data must be public by end of September 2026.

- **Codex claim 14c (Reg S-P compliance dates: Dec 3, 2025 large; June 3, 2026 small):** Real.
- **Verdict 14c:** CONFIRMED.
- **Official source(s):**
  - https://www.finra.org/rules-guidance/guidance/sec-regulation-s-p-compliance-date-reminder-20251114
  - SEC May 16, 2024 final rule release; Small Entity Compliance Guide on sec.gov
- **Verified text snippet:** Reg S-P amendments (May 16, 2024 final rule). Larger covered institutions (registered IAs with $1.5B+ AUM, ICs with $1B+ net assets, all non-small broker-dealers) compliance December 3, 2025. All other covered institutions compliance June 3, 2026.

- **Codex claim 14d (Names Rule extended again in 2026):** Real, but the precise dates Codex cited need this update.
- **Verdict 14d:** CONFIRMED with precise dates.
- **Official source(s):**
  - https://www.sec.gov/newsroom/press-releases/2025-54 (March 14, 2025 extension press release)
  - https://www.sec.gov/files/rules/final/2025/33-11368.pdf (formal release)
- **Verified text snippet:** Names Rule compliance dates extended: large fund groups ($1B+ net assets at most recent fiscal-year end) from December 11, 2025 to **June 11, 2026**. Smaller fund groups (less than $1B net assets) from June 11, 2026 to **December 11, 2026**. (Distinct from Form N-PORT Names Rule reporting compliance dates, which the SEC further extended in February 2026 to November 17, 2027 for large groups and May 18, 2028 for smaller groups — those affect N-PORT reporting only, not the underlying Names Rule itself.)
- **Recommended cite/text for skills:** "SEC Investment Company Names Rule amendments (33-11238, 17 CFR 270.35d-1) compliance dates: large fund groups ($1B+ net assets at most recent fiscal-year end), June 11, 2026; smaller fund groups (less than $1B net assets), December 11, 2026. The Form N-PORT reporting compliance dates for Names Rule data were further extended in February 2026 to November 17, 2027 (large) / May 18, 2028 (smaller); these N-PORT dates affect reporting timing only, not underlying Names Rule compliance."
- **Affected skill files:** capital-markets-asset-management-compliance skills, particularly `fund-board-reporting`.

---

## P1 source-quality claims

### 15. IIA Global Internal Audit Standards effective January 9, 2025

- **Codex claim:** Effective January 9, 2025; replace IIA IPPF / 2017-numbering references.
- **Verdict:** CONFIRMED.
- **Official source(s):** https://www.theiia.org/en/standards/2024-standards/global-internal-audit-standards/ ; https://www.theiia.org/en/content/communications/press-releases/2025/january/the-iia-celebrates-the-effective-date-of-the-global-internal-audit-standards/
- **Verified text snippet:** IIA released the 2024 Global Internal Audit Standards on January 9, 2024 with effective date January 9, 2025. Single 120-page document with 5 domains, 15 principles, 52 standards. Quality assessments under the new Standards are required as of January 9, 2025. The 2017 IPPF Standards numbering and structure (1000-series, 2000-series, etc.) are superseded.
- **Recommended cite/text for skills:** "IIA Global Internal Audit Standards (2024 edition, effective January 9, 2025). Five domains, fifteen guiding principles, fifty-two standards, replacing the 2017 IPPF. Where a skill cites IIA Standards 1000, 2100, 2300 etc. (2017 IPPF numbering), update to the 2024 domain/principle/standard structure or cite the 2024 edition generally with content reference, not the obsolete number."
- **Affected skill files:** any skill referencing IIA / IPPF, particularly third-line-touching skills if any (this repo is second-line-focused, so likely thin).
- **Notes/caveats:** The repo is a second-line repo, so IIA references are mostly in cross-cutting / oversight contexts.

---

### 16. AICPA AU-C / SAS sectional references

- **Codex claim:** Verify current AU-C sections relevant to compliance testing (240, 320, 330, 530, 540).
- **Verdict:** CONFIRMED. The cited AU-C sections are current and accurately titled.
- **Official source(s):**
  - https://www.aicpa-cima.com/resources/download/aicpa-statements-on-auditing-standards-currently-effective
  - https://us.aicpa.org/research/standards/auditattest/clarifiedsas
  - https://downloads.ctfassets.net/rb9cdnjh59cm/6SZYDorUSdWM3sjctjPnOL/d2cb13701145f8699624298a1b875c8a/ps-au-c-sections.pdf (AU-C sections PDF)
- **Verified text snippet:** AU-C 240 Consideration of Fraud in a Financial Statement Audit; AU-C 320 Materiality in Planning and Performing an Audit; AU-C 330 Performing Audit Procedures in Response to Assessed Risks and Evaluating the Audit Evidence Obtained; AU-C 530 Audit Sampling; AU-C 540 Auditing Accounting Estimates, Including Fair Value Accounting Estimates, and Related Disclosures. All five are codified in the AICPA Clarified Statements on Auditing Standards.
- **Recommended cite/text for skills:** Cite as "AU-C 240 / 320 / 330 / 530 / 540 (AICPA Clarified Statements on Auditing Standards, currently effective edition)." For private-company / nonissuer audits these are the operative standards; for issuer audits the analogous PCAOB standards apply (PCAOB AS 2401 for fraud, AS 2105 / 2110 for materiality / risk assessment, AS 2315 for sampling, AS 2501 for accounting estimates).
- **Affected skill files:** `compliance-testing` skills — control-sampling, qa-workpaper, etc.

---

### 17. OCC PPM 5310-3 actual subject

- **Codex claim:** PPM 5310-3 is OCC Bank Enforcement Actions and Related Matters, NOT a general bank-supervision-process anchor.
- **Verdict:** CONFIRMED.
- **Official source(s):**
  - https://www.occ.gov/news-issuances/bulletins/2023/ppm-5310-3.pdf (current 2023 revision)
  - https://www.occ.gov/news-issuances/bulletins/2023/bulletin-2023-16.html (transmittal bulletin)
  - https://www.occ.gov/news-issuances/news-releases/2023/nr-occ-2023-49.html (press release)
- **Verified text snippet:** PPM 5310-3, "Bank Enforcement Actions and Related Matters," sets the OCC's framework for informal and formal enforcement actions against banks. The 2023 revision added Appendix C on heightened-standards-related enforcement. It does NOT govern routine bank-supervision-process activities; for those, the OCC's Comptroller's Handbook series and Bank Supervision Process booklet are the anchors. PPM 5310-3 expressly excludes enforcement actions against institution-affiliated parties or other individuals, civil money penalty actions against individuals, and securities-law-enforcement actions.
- **Recommended cite/text for skills:** "OCC PPM 5310-3, Bank Enforcement Actions and Related Matters (2023 revision; OCC Bulletin 2023-16). Establishes the OCC's bank-enforcement framework: informal-action escalation, formal-action triggers, civil money penalty considerations against banks, and the heightened-standards Appendix C. For routine bank-supervision-process anchors, cite the OCC Comptroller's Handbook (the Bank Supervision Process booklet is the closest analog), not PPM 5310-3."
- **Affected skill files:** any skill that cited PPM 5310-3 as a "bank supervision process" anchor; the bank-supervision-readiness skill is the prime suspect.

---

### 18. SR 08-8 / CA 08-11 October 1, 2025 revision

- **Codex claim:** SR 08-8 / CA 08-11 was revised on October 1, 2025 to remove reputational-risk references.
- **Verdict:** CONFIRMED.
- **Official source(s):** https://www.federalreserve.gov/supervisionreg/srletters/SR0808.htm
- **Verified text snippet:** The FRB SR 08-8 / CA 08-11 page header reads: "Revised October 1, 2025." The revision note says: "On October 1, 2025: This letter was revised to remove references to reputational risk." This aligns with the Federal Reserve Board's June 23, 2025 announcement that reputational risk will no longer be a component of examination programs. The October 7, 2025 OCC / FDIC NPR (Prohibition on Use of Reputation Risk by Regulators) is the parallel, broader codification effort.
- **Recommended cite/text for skills:** "FRB SR 08-8 / CA 08-11, Compliance Risk Management Programs and Oversight at Large Banking Organizations with Complex Compliance Profiles (October 16, 2008; revised October 1, 2025 to remove references to reputational risk). The October 1, 2025 revision aligns with the Federal Reserve Board's June 23, 2025 announcement that reputational risk is no longer a component of examination programs and the parallel OCC / FDIC NPR (October 7, 2025) on reputation risk. The compliance-risk-management framework remains anchored in the letter; the reputational-risk component does not."
- **Affected skill files:** compliance-program / large-bank governance skills citing SR 08-8.

---

### 19. DORA Article 28 internal structure

- **Codex claim:** Article 28 separates register / reporting / prior-notification, termination, and exit-strategy.
- **Verdict:** CONFIRMED with structural precision.
- **Official source(s):**
  - https://eur-lex.europa.eu/eli/reg/2022/2554/oj/eng (DORA Regulation (EU) 2022/2554)
- **Verified text snippet:** Article 28 (General principles for sound management of ICT third-party risk) is the umbrella: 28(1) general management of ICT third-party risk; 28(2) strategy on ICT third-party risk; 28(3) register of information at entity / sub-consolidated / consolidated levels, distinguishing critical-or-important-function-supporting contracts from others, with at-least-yearly reporting to competent authorities; 28(4) prior-notification obligation to competent authorities for new contractual arrangements supporting critical or important functions; 28(5) due-diligence obligations before entry into contracts; 28(6) ongoing monitoring obligations; 28(7) termination triggers; 28(8) exit strategies for ICT services supporting critical or important functions, with documented and tested transition plans.
- **Recommended cite/text for skills:** "DORA Regulation (EU) 2022/2554, Article 28 (General principles for sound management of ICT third-party risk). Structure: 28(1)-(2) management and strategy; 28(3) register of information at entity / sub-consolidated / consolidated levels, separately tracking contracts that support critical or important functions, with at-least-annual reporting to competent authorities; 28(4) prior notification to competent authorities of contractual arrangements supporting critical-or-important functions; 28(5) pre-contractual due diligence; 28(6) ongoing monitoring; 28(7) termination triggers; 28(8) documented and tested exit strategies for ICT services supporting critical or important functions. Applicable from 17 January 2025."
- **Affected skill files:** `third-party-operational-resilience` skills (criticality-assessment, vendor-diligence, exit-plan, contract-gap-review, concentration-risk-review).

---

### 20. DORA Article 30 baseline vs enhanced clauses

- **Codex claim:** Article 30 distinguishes baseline contractual provisions (Art 30(2)) from enhanced provisions for critical / important ICT (Art 30(3)).
- **Verdict:** CONFIRMED.
- **Official source(s):** https://eur-lex.europa.eu/eli/reg/2022/2554/oj/eng (Article 30); https://www.springlex.eu/en/packages/dora/dora-regulation/article-30/ (annotated source)
- **Verified text snippet:** Article 30(2) baseline contractual elements for ALL ICT-services contracts: clear and complete description of functions / ICT services; whether subcontracting is permitted and conditions; locations of contracted/subcontracted services and data processing including storage, with prior-notice obligation on changes; provisions on availability, authenticity, integrity and confidentiality including personal data; data-portability obligations; service-level descriptions and amendments; assistance during ICT incidents at no additional cost or at cost agreed ex ante; cooperation with competent authorities; termination rights and minimum notice periods; participation in awareness / training programs. Article 30(3) enhanced contractual elements for ICT services SUPPORTING CRITICAL OR IMPORTANT FUNCTIONS: full SLDs with quantitative and qualitative performance targets; notice periods and reporting on developments materially impacting the ability to perform; ICT security measures, tools and policies; obligation to participate in TLPT (Article 26); right to monitor performance with unrestricted rights of access, inspection and audit by the financial entity, an appointed third party, or competent authority; exit strategies; participation in cyber awareness / training. Article 30(4)-(5) cover subcontracting and supplementary contractual content.
- **Recommended cite/text for skills:** "DORA Regulation (EU) 2022/2554, Article 30 (Key contractual provisions): Art 30(2) baseline contractual elements apply to ALL ICT-services contracts (function description, location and processing, availability/authenticity/integrity/confidentiality, data portability, SLD, incident assistance, competent-authority cooperation, termination, training). Art 30(3) enhanced contractual elements apply to ICT services SUPPORTING CRITICAL OR IMPORTANT FUNCTIONS (quantitative/qualitative SLDs with performance targets, ICT security measures, TLPT participation under Art 26, unrestricted audit rights for the financial entity / appointed third party / competent authority, exit strategies). Art 30(4) addresses subcontracting; Art 30(5) and following address conditions and supplementary provisions."
- **Affected skill files:** contract-gap-review (DORA overlay), vendor-diligence, criticality-assessment.

---

### 21. Commission Delegated Regulation (EU) 2025/532 (DORA ICT subcontracting RTS)

- **Codex claim:** Real.
- **Verdict:** CONFIRMED.
- **Official source(s):** https://eur-lex.europa.eu/eli/reg_del/2025/532/oj/eng
- **Verified text snippet:** Commission Delegated Regulation (EU) 2025/532 of 24 March 2025 (published in OJ 2 July 2025, applicable from 22 July 2025) supplements DORA with regulatory technical standards specifying the elements financial entities must determine and assess when subcontracting ICT services that support critical or important functions. Covers proportionality and group-wide application, due diligence and risk assessment, subcontracting conditions, and contractual arrangements between financial entities and ICT service providers. (Article 5 of an earlier draft on monitoring of subcontractors was removed at Commission request.)
- **Recommended cite/text for skills:** "Commission Delegated Regulation (EU) 2025/532 of 24 March 2025 (published in OJ 2 July 2025, applicable from 22 July 2025) — RTS on subcontracting of ICT services supporting critical or important functions under DORA. Specifies due diligence, risk assessment, subcontracting conditions, and contractual-arrangement requirements. Applies to all financial entities subject to DORA that rely on ICT subcontracting for critical or important functions."

---

### 22. Commission Delegated Regulation (EU) 2025/1190 (DORA TLPT RTS)

- **Codex claim:** Real.
- **Verdict:** CONFIRMED.
- **Official source(s):** https://eur-lex.europa.eu/eli/reg_del/2025/1190/oj/eng
- **Verified text snippet:** Commission Delegated Regulation (EU) 2025/1190 of 13 February 2025 (published in OJ 18 June 2025, applicable from 8 July 2025) supplements DORA with regulatory technical standards specifying criteria used for identifying financial entities required to perform threat-led penetration testing (TLPT). Entities subject to DORA TLPT requirements must perform TLPT at least once every three years, unless otherwise specified by the national competent authority. Defines red-team / blue-team / control-team roles; covers test planning, execution on live production systems, and reporting.
- **Recommended cite/text for skills:** "Commission Delegated Regulation (EU) 2025/1190 of 13 February 2025 (published in OJ 18 June 2025, applicable from 8 July 2025) — RTS on threat-led penetration testing under DORA Article 26. Specifies criteria for identifying financial entities required to perform TLPT; test cadence (at least every three years unless otherwise specified by competent authority); red-team / control-team / blue-team conventions; live-production testing scope; reporting."
- **Affected skill files (#21 + #22):** `third-party-operational-resilience/skills/resilience-testing-pack`, `vendor-diligence`, DORA-touching capital-markets and banking skills.

---

### 23. PRA SS1/21 + SS2/21 current versions

- **Codex claim:** Verify current versions on bankofengland.co.uk; note any updates since 2021.
- **Verdict:** PARTIAL. Both supervisory statements remain in force, but the regulatory framework around them has evolved significantly: March 31, 2025 was the operational-resilience compliance milestone, and the PRA has since published PS7/26 with SS1/26 and an update to SS2/21 (per multiple secondary sources; verify exact PRA URL on the engagement date as the BoE Bank of England URL conventions shift periodically).
- **Official source(s):**
  - https://www.bankofengland.co.uk/-/media/boe/files/prudential-regulation/supervisory-statement/2021/ss121-march-22.pdf (SS1/21 with March 2022 update)
  - https://www.bankofengland.co.uk/prudential-regulation/publication/2021/march/operational-resilience (SS1/21 landing)
  - PRA Policy Statement 7/26 (PS7/26) — operational incident and third-party reporting
- **Verified text snippet:** SS1/21 ("Operational resilience: Impact tolerances for important business services") sets PRA expectations on operational resilience. SS2/21 ("Outsourcing and third party risk management") sets PRA expectations on outsourcing and TPRM. Both became effective March 31, 2022 with a transitional period to March 31, 2025 for full compliance with operational-resilience expectations (impact tolerances, mapping, scenario testing). PS7/26 (and its accompanying SS1/26) introduce a new UK incident-reporting and material-third-party-arrangement-reporting framework and update SS2/21 expectations.
- **Recommended cite/text for skills:** "PRA SS1/21 (Operational resilience: Impact tolerances for important business services, March 2021; March 2022 update) and PRA SS2/21 (Outsourcing and third party risk management, March 2021). Operational-resilience compliance milestone was 31 March 2025; firms expected to be fully compliant by that date. Note PS7/26 and accompanying SS1/26 introduce new operational-incident and material-third-party-arrangement reporting framework and update SS2/21 expectations; verify current SS2/21 version on engagement date and overlay PS7/26 reporting requirements where applicable."
- **Affected skill files:** UK overlay sections in resilience and outsourcing skills.
- **Notes/caveats:** The PRA / BoE site occasionally re-issues SS documents at the same number with updated effective dates. Always cite the version date.

---

### 24. OCC Appendix D + Regulation YY

- **Codex claim:** Verify the specific subparts for risk-governance / board oversight.
- **Verdict:** CONFIRMED. With one timely caveat: the OCC December 2025 NPR proposes raising the Appendix D applicability threshold from $50B to $700B in average total consolidated assets, which would significantly narrow the population of "covered banks." That NPR is still pending; the existing $50B threshold remains operative until the rule is finalized.
- **Official source(s):**
  - https://www.ecfr.gov/current/title-12/chapter-I/part-30/appendix-Appendix%20D%20to%20Part%2030 (Appendix D current text)
  - https://www.ecfr.gov/current/title-12/chapter-II/subchapter-A/part-252 (Regulation YY)
  - https://www.ecfr.gov/current/title-12/chapter-II/subchapter-A/part-252/subpart-C/section-252.22 (risk-committee requirement at $50B)
  - https://www.occ.gov/news-issuances/bulletins/2025/bulletin-2025-51.html (OCC NPR December 2025)
- **Verified text snippet:** OCC Heightened Standards: 12 CFR Part 30 Appendix D establishes minimum standards for the design and implementation of a covered bank's risk governance framework and minimum standards for the board of directors in providing oversight. Currently applicable to insured national banks, federal savings associations, and federal branches with average total consolidated assets of $50 billion or more (NPR pending to raise to $700B). Regulation YY (12 CFR Part 252): Subpart C — Risk Committee Requirement for BHCs with $50B+ and less than $100B (§252.22 risk-committee composition, scope, CRO requirement); Subpart D — Enhanced Prudential Standards for BHCs with $100B+ (§§252.31-252.36 risk-management and risk-committee, liquidity, stress testing); Subpart O — Foreign Banking Organizations with $100B+ TCA and $100B+ combined US assets.
- **Recommended cite/text for skills:** "OCC Heightened Standards (12 CFR Part 30 Appendix D) currently apply to insured national banks, federal savings associations, and federal branches with average total consolidated assets of $50B or more; OCC NPR December 2025 (OCC Bulletin 2025-51) proposes raising the threshold to $700B and is pending. Regulation YY (12 CFR Part 252): Subpart C §252.22 risk-committee requirement at $50B; Subpart D §§252.31-252.36 enhanced prudential standards including risk-management framework and CRO at $100B; Subpart O for FBOs with $100B+ TCA and $100B+ US assets. Cite the operative subpart that matches the firm's asset tier."
- **Affected skill files:** `risk-committee-pack`, large-bank governance skills.

---

### 25. BCBS January 2026 data-risk themes

- **Codex claim:** Useful as supervisory context, not new binding guidance.
- **Verdict:** CONFIRMED.
- **Official source(s):**
  - https://www.bis.org/bcbs/ (BCBS landing)
  - BCBS Newsletter No. 36 of 6 January 2026 (search-result-confirmed; direct BIS URL not retrieved during this verification but secondary sources are consistent)
- **Verified text snippet:** On 6 January 2026, the Basel Committee issued Newsletter No. 36 summarising key themes and challenges related to banks' risk data aggregation and risk reporting (RDA) practices based on supervisory and industry outreach on BCBS 239 implementation. Identifies governance gaps, fragile data lineage across complex estates, and inconsistent cross-border execution. Emphasizes risk-based data lineage for metrics feeding critical risk and regulatory reports, robust data-quality checks, and time-bounded ad-hoc reporting tests under stress.
- **Recommended cite/text for skills:** "BCBS Newsletter No. 36 (6 January 2026, Basel Committee on Banking Supervision) summarises supervisory themes on RDA / BCBS 239 implementation. Cite as supervisory context, not binding guidance. The binding anchor remains BCBS 239 (Principles for effective risk data aggregation and risk reporting, January 2013, BIS)."
- **Affected skill files:** risk-reporting, RDARR-touching skills.
- **Notes/caveats:** I did not retrieve the direct BIS URL for the newsletter during verification; recommend confirming the exact URL on engagement date. Two independent secondary sources confirmed the newsletter number, date, and substance.

---

### 26. SR 21-19 status as BCBS 239 anchor

- **Codex claim:** Remove SR 21-19 because it's not the BCBS 239 / RDARR anchor.
- **Verdict:** CONFIRMED. SR 21-19 is the wrong cite for BCBS 239.
- **Official source(s):** https://www.federalreserve.gov/supervisionreg/srletters/SR2119.htm
- **Verified text snippet:** SR 21-19 (December 10, 2021; revised January 9, 2026) is titled "The Federal Reserve reminds firms of safe and sound practices for counterparty credit risk management in light of the Archegos Capital Management default." It addresses counterparty credit risk management at firms with large derivatives portfolios and relationships with investment funds, NOT risk-data-aggregation / regulatory-reporting practices.
- **Recommended cite/text for skills:** "Remove SR 21-19 as a BCBS 239 / RDARR anchor — its subject is counterparty credit risk management following Archegos. The proper anchors for BCBS 239 / RDARR in US supervision are: BCBS 239 itself (Principles for effective risk data aggregation and risk reporting, January 2013, BIS), the FRB's CCAR / FR Y-14 instructions for the supervisory expectations on risk data and reporting at large firms, OCC Heightened Standards 12 CFR Part 30 Appendix D §§II.A-II.D for risk-governance documentation, and the BCBS Newsletter No. 36 (6 January 2026) for current supervisory themes."
- **Affected skill files:** any RDARR / data-governance / risk-reporting skill citing SR 21-19.

---

### 27. NIST SP 800-61 Rev. 3 status

- **Codex claim:** Verify NIST publication; SP 800-61 was historically incident-handling guide; Rev. 3 if it exists.
- **Verdict:** CONFIRMED. Rev. 3 exists, finalized April 3, 2025.
- **Official source(s):**
  - https://csrc.nist.gov/pubs/sp/800/61/r3/final
  - https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-61r3.pdf
  - https://www.nist.gov/news-events/news/2025/04/nist-revises-sp-800-61-incident-response-recommendations-and-considerations
- **Verified text snippet:** NIST SP 800-61 Rev. 3, "Incident Response Recommendations and Considerations for Cybersecurity Risk Management: A CSF 2.0 Community Profile," final published April 3, 2025. Supersedes SP 800-61 Rev. 2 (Computer Security Incident Handling Guide). The substantive shift is from a step-by-step incident-handling guide to a CSF 2.0 community profile that maps incident-response activities into the CSF 2.0 functions (Govern, Identify, Protect, Detect, Respond, Recover).
- **Recommended cite/text for skills:** "NIST SP 800-61 Rev. 3, Incident Response Recommendations and Considerations for Cybersecurity Risk Management: A CSF 2.0 Community Profile (April 3, 2025). Supersedes SP 800-61 Rev. 2 (Computer Security Incident Handling Guide). The Rev. 3 framing is CSF 2.0-aligned, not the prior step-by-step lifecycle. Update any skill that cites Rev. 2's "Preparation / Detection and Analysis / Containment / Eradication / Recovery / Post-Incident Activity" lifecycle — that lifecycle is no longer the NIST framing; it has been re-mapped into CSF 2.0 functions in Rev. 3."
- **Affected skill files:** cyber-disclosure-readiness, incident-response-related skills, payment-operations-incident-review.

---

### 28. Reg S-P concrete compliance dates

- **Verdict:** CONFIRMED. See section 14c above for the canonical wording.
- **Recommended cite/text for skills:** "SEC Regulation S-P amendments (May 16, 2024 final rule, 89 FR 47688). Compliance dates: large covered institutions (registered IAs with $1.5B+ AUM, ICs with $1B+ net assets, all non-small broker-dealers as defined in Rule 0-10 of the Exchange Act), December 3, 2025; smaller covered institutions, June 3, 2026. Required: incident response program, customer notification of unauthorized access or use of sensitive customer information, service-provider oversight, recordkeeping."

---

## Summary: counts by verdict

| Verdict | Count | Claims |
|---|---|---|
| CONFIRMED | 23 | 1, 2, 3, 4, 5, 6, 8, 10, 11a, 11b, 11c, 12, 13, 14a, 14b, 14c, 14d, 15, 16, 17, 18, 19, 20, 21, 22, 25, 26, 27, 28 |
| PARTIAL | 2 | 7 (precision tweak: court-stay vs CFPB stay), 9 (right for outsourcing-claims context, wrong for life-health-pricing context where #880 is correct), 23 (PRA SS1/SS2 current — partial because PS7/26 evolution) |
| WRONG | 0 | none |
| UNVERIFIABLE | 0 | none |

(Counts use ranges combined for #11 and #14 sub-claims.)

## Top three surprises

1. **NAIC Model #880 is right where the repo uses it for life/health pricing (unfair-discrimination), and wrong only where it's used for claims-handling (insurance-outsourcing-review).** Codex framed this as a blanket replacement; in fact, the action-plan needs to split: keep #880 for unfair-discrimination in pricing/rating, replace with #900 + #902/#903 only for claims-handling oversight. The two are different statutory frames since NAIC separated them in June 1990.

2. **The OCC 2026-13 PDF contains zero NIST references.** Codex correctly flagged this; downstream skills that bundle "OCC 2026-13 / NIST AI RMF / NIST AI 600-1" as if they were one regulatory package are misrepresenting the OCC's framing. The bulletin builds its model definition from scratch and uses footnote 3 to actively exclude generative and agentic AI from scope. NIST AI RMF is voluntary, separate, and not referenced.

3. **The Reg E "5 business days for provisional credit" pattern in several repo files isn't a typo, it's a pervasive industry mis-cite.** The actual regulatory clock is 10 business days; the 45- and 90-day extensions are calendar days, not business days. Anywhere the repo says "5 business days for provisional credit" or "45 business days for completion" needs to be fixed. The deposit-operations-controls source-anchors file gets it right and is the model.

## Outstanding / deferred items

- **BCBS Newsletter No. 36 direct BIS URL** — I did not retrieve the direct bis.org page during verification (BIS site search returns inconsistent paths for newsletters). Two independent secondary sources confirm the date (6 January 2026) and substance. Recommend confirming exact BIS URL on engagement date and adding it to the source-anchors. Verdict downgraded only to the extent the URL itself is unverified; the publication is real.

- **PRA PS7/26 + SS1/26 + SS2/21 update** — current PRA/Bank of England URL conventions shift periodically. SS1/21 and SS2/21 are confirmed live, but the PS7/26 supplementary framework merits a direct PRA-page check on engagement date before any UK-overlay skill cites it as binding.

- **OCC Appendix D NPR (December 2025)** — pending; the $700B threshold is proposed not final. Skills that cite Appendix D should use current $50B threshold and flag the pending NPR.

- **CFPB 1033 stay litigation** — Forcht Bank docket is active; rule-state may change between this date and engagement date. Treat the stay as the operative posture and verify on the analysis date.

## Note on currency

This dossier is dated 2026-05-08. Several of the verified items (FinCEN orders, SEC withdrawals, court stays, OCC NPRs) are from late 2025 or early 2026 and are subject to change. Skills that cite any of these should retain a `verify on engagement date` posture for the rule-state, even though the cite itself is correct as of this dossier's date.
