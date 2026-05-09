# Sector overlay: banking

Loaded when the engagement scope flags `banking` as the sector. The change-log spine is unchanged; what changes is the source citation set, the named approver expectations, and the typical downstream-impact patterns for bank policy diffs.

## Approver routing expectations

For large national banks operating under OCC heightened standards (12 CFR Part 30 Appendix D), material changes to the policies that constitute the written framework default to a routing posture that includes board or board-committee attestation. Specifically:

- Risk-appetite, top-risks, and risk-governance-framework policy changes route to the board risk committee.
- Credit, market, liquidity, and operational risk policy changes route to the board risk committee with named-CRO sign-off.
- Insider-lending (Reg O), affiliate-transactions (Reg W), and savings-and-loan-holding-company policy changes carry both committee and board director attestation depending on the firm's bylaws.
- BSA/AML policy changes route to the BSA Officer and to the board-designated BSA committee where one exists; the FFIEC BSA/AML Examination Manual's program-element expectations frame the materiality call.

For community banks not subject to heightened standards, the routing posture is lighter — typically the relevant committee or function head with board-committee notification — but the lifecycle expectation under OCC Bulletin 2021-36 still applies.

## Source-citation patterns specific to banking diffs

When a banking policy diff cites supervisory letters, the citation carries the SR letter or OCC Bulletin number with section reference where the letter is structured (most are). FRB SR letters and OCC bulletins are the working source set for bank policy diffs along with the underlying CFR.

- 12 CFR Part 30 Appendix D — heightened standards written framework.
- 12 CFR Part 215 (Reg O) — insider lending.
- 12 CFR Part 223 (Reg W) — affiliate transactions.
- 12 CFR Part 252 (Reg YY) — enhanced prudential standards for large bank holding companies.
- Joint interagency Revised Guidance on Model Risk Management (OCC Bulletin 2026-13 / FRB SR 26-2 / FDIC FIL-15-2026, April 17, 2026) — model risk policy. Supersedes SR 11-7 / OCC Bulletin 2011-12 (April 4, 2011) and SR 21-8 (April 9, 2021); GenAI and agentic AI explicitly out of scope.
- Interagency Guidance on Third-Party Relationships (OCC / FRB / FDIC, June 2023) — TPRM policy.
- FFIEC BSA/AML Examination Manual — BSA/AML policy.

## Downstream-impact patterns specific to banking diffs

A few patterns recur in bank policy diffs and the change log carries them as expected fields rather than ad-hoc rationale.

- Material BSA/AML policy changes almost always touch the BSA training program, the suspicious activity reporting workflow, the customer due diligence procedures, and the bank's response to OFAC alerts. The downstream-impact rows enumerate each.
- Material TPRM policy changes touch the master vendor contract templates and the procurement workflow; large banks typically maintain template-by-template change logs that the diff cross-references.
- Material model-risk policy changes touch the model inventory's policy-version field and the validation-cadence schedule; the diff feeds the model risk committee's quarterly review.
- Material capital and liquidity policy changes touch the firm's resolution and recovery plan and may require coordination with the firm's resolution group at the FRB or the FDIC.

## Cross-cutting overlay interaction

Banking policy diffs commonly interact with the cyber cross-cutting overlay (NYDFS Part 500 §500.3 for NY-licensed banks, FFIEC IT booklet for federally regulated banks). Where the policy in scope is information security or third-party security, both the banking sector overlay and `references/cross-cutting/cyber.md` load and the materiality lens picks up both sets of expectations.
