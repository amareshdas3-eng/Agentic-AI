# ProEngineering Electrical Intelligence Suite — Standards Governance Policy
### Authoritative Standards Registry, Edition Control & Compliance Claim Protocols
**Author:** Agent 2 (Standards Governance Specialist) & Agent 0 (Integration Lead)  
**Status:** APPROVED (Gate 1 Baseline)  
**Date:** October 15, 2026

---

## 1. Governance Principles & Legal Safe Harbor

1. **Strict Metadata Storage (No Copyright Infringement):**
   The suite stores standard references as metadata pointers (Issuer, Document Number, Edition/Year, Clause Identifier, Scope). Full copyrighted text or tables from standards bodies (IEC, IEEE, BIS, BSI, NFPA) are **never ingested, reproduced, or distributed**.
2. **Prohibition of Autonomous Statutory Certification Claims:**
   The software must NEVER generate outputs containing terms such as "Certified IEC-Compliant", "Statutorily Certified", or "Authority Approved". All outputs are evaluated as:
   - `EvaluationStatus: PASS` — Satisfies specified criteria from the project's authorized `ProjectDesignBasis`.
   - `EvaluationStatus: FAIL` — Violates specified criteria from the project's authorized `ProjectDesignBasis`.
   - `EvaluationStatus: NOT_ASSESSED` — Data or criteria missing; no assessment performed.
   - `EvaluationStatus: REVIEW_REQUIRED` — Requires discretionary engineering review by a licensed Engineer-of-Record (EOR).
3. **Mandatory Disclaimer on Every Output:**
   Every generated diagram, calculation proof, and audit matrix must prominently display:
   > *"This automated calculation and consistency review is an engineering aid for qualified professionals. It does not replace the statutory authority, professional judgment, or required seal of the licensed Engineer-of-Record (EOR)."*

---

## 2. Authorized Standards Edition Registry

| Standard Identifier | Current Edition Status | Verified Clauses | Permitted Usage in Core Suite |
|---|---|---|---|
| **IEC 60364-5-52** | Ed 3.0 (2009) + AMD1:2011 | Clause 525, Annex B, Table E.52.1 | Radial cable voltage drop equations, continuous current rating method, triplen harmonic derating. |
| **IEC 60364-5-54** | Ed 3.0 (2011) | Clause 543.1.2, Table A.54.1 | Adiabatic short-circuit thermal withstand formula ($S_{min} = I_{sc}\sqrt{t}/k$). |
| **IEC 60076-1** | Ed 3.0 (2011) | Clause 4, Table 1 | Standard transformer ratings series, continuous loading criteria. |
| **IEC 60076-5** | Ed 3.0 (2006) | Table 1 | Standard transformer %Z impedance values and short-circuit withstand. |
| **IEC 60947-2** | Ed 5.0 (2016) + AMD1:2019 | Clause 4.3.5, 4.3.6, 4.3.7 | Circuit breaker ratings ($I_n$, $I_{cu}$, $I_{cs}$, $I_{cw}$). |
| **IEC 61439-1/2** | Ed 3.0 (2020) | Clause 8.6, Clause 8.101 | Busbar thermal limits, Forms of Internal Separation (Form 1 to 4b). |
| **IEC 60865-1** | Ed 3.0 (2011) | Clause 5 | Calculation of peak electrodynamic forces on rigid busbars. |
| **IEC 62271-102** | Ed 2.0 (2018) | Clause 5.104 | Mechanical and electrical interlocking for disconnectors and earthing switches. |
| **IEEE Std 141** | Rev 1993 (Red Book) | Section 3.8 | Industrial motor starting transient voltage dip limits ($\le 15\%$). |
| **IEEE Std 80** | Rev 2013 | Section 8.3 | Substation grounding tolerable touch and step voltage limits. |
| **IEEE Std 1584** | Rev 2018 | Section 4 | Arc-flash incident energy screening model (Flagged `REVIEW_REQUIRED`). |
| **IS 732** | Rev 2019 (BIS) | Clause 5.2 | Indian National electrical installation wiring rules. |
| **IS 3043** | Rev 2018 (BIS) | Clause 15.3 | Indian Code of practice for earthing of electrical installations. |
| **CEA Safety Regs** | 2023 Gazette Notification | Reg 35, 43, 44 | Indian statutory safety requirements for earthing, HV supply, and interlocking. |
