# ProEngineering Electrical Intelligence Suite — Release Blockers Matrix
### Pre-Release Risk Register & Remediation Tracker (Gate 0 / Gate 1 Baseline)
**Author:** Agent 0 (Integration Lead) & Agent 12 (Release Auditor)  
**Date:** October 15, 2026

---

## Pre-Release Blocker Register

| Risk ID | Affected File(s) | Root Cause & Hazard | Severity | Remediation Action Plan | Status |
|---|---|---|---|---|---|
| **RSK-001** | `04_MCC_PCC_Architect_Pro/STARTER_SELECTION_AND_FEEDER_LOGIC.md` | Fixed motor kW starter cutoffs (DOL $\le 5.5\text{kW}$, etc.) applied universally without considering grid stiffness, voltage dip limit, or torque curves. | **CRITICAL** | Refactored starter selection to a multi-parameter decision matrix based on `starting_dip_limit_pct`, $I_{sc}$, load inertia, and process VFD requirement. | **RESOLVED IN SPEC & ENGINE** |
| **RSK-002** | `02_LoadFlow_VoltageDrop_Pro` & `deterministic_engine.js` | Blanket 3%/5% voltage drop thresholds and simplified derating applied without distinguishing feeder type or installation method; silent defaults when data missing. | **CRITICAL** | Enforced explicit `VoltageDropCriteria` per circuit; emit `NOT_ASSESSED` if conductor length, size, or derating is missing. | **RESOLVED IN ENGINE V2** |
| **RSK-003** | `00_Universal_Master_Framework/ELECTRICAL_CODES_AND_SAFETY_COMPENDIUM.md` | Empirical arc flash and short-circuit equations risked edition mismatch (IEEE 1584:2002 vs 2018) or out-of-bounds application. | **CRITICAL** | Audited all equations for dimensional homogeneity; marked arc flash as `REVIEW_REQUIRED` screening tool; cited exact standard edition metadata. | **RESOLVED IN STANDARDS AUDIT** |
| **RSK-004** | `03_Equipment_Sizing_Pro` & `04_MCC_PCC_Architect_Pro` | Hard-coded 20% spare feeders, fixed current densities ($1.2\text{ A/mm}^2$), and fixed $<1\text{ }\Omega$ earth resistance stated as universal statutory mandates. | **HIGH** | Moved all design margins into versioned `ProjectDesignBasis` fields; busbar sizing evaluated by thermal heat balance (IEC 61439-1 Table 6). | **RESOLVED IN SCHEMA V2** |
| **RSK-005** | `src/test_runner.js` & `demo_dashboard.html` | Self-referential test assertions and blanket "100% Statutory Compliance Verified" UI badges mislead users regarding statutory certification. | **CRITICAL** | Replaced all compliance claims with `EvaluationStatus: PASS | FAIL | NOT_ASSESSED | REVIEW_REQUIRED` citing applied project criteria. | **RESOLVED IN LAB & RUNNER** |
| **RSK-006** | `06_ProEngineering_Commercial_Hub` | Unvalidated pricing tiers, conversion rates, and ROI figures presented as established commercial facts. | **MEDIUM** | Prefixed all commercial documents with `COMMERCIAL HYPOTHESIS — FOR PILOT VALIDATION` and stripped unverified marketing claims. | **RESOLVED IN GTM HUB** |

---

## Gate Transition Criteria
- **Gate 0 -> Gate 1:** Verified baseline files extracted, inventory confirmed, risk register documented, and architectural decisions adopted. (**GATE 0 CLEARED**).
- **Gate 1 -> Gate 2:** Canonical schema v2.0 frozen, independent benchmarks established (15 cases), and pure deterministic calculation engine refactored.
