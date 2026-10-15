# ProEngineering Electrical Intelligence Suite — Architecture Decision Log (ADR)
### Formal Records of System Design Choices, Governance Policies & Risk Remediations
**Author:** Agent 0 (Chief Architect) & Multi-Agent Integration Council  
**Status:** APPROVED (Gate 0 / Gate 1 Baseline)  
**Date:** October 15, 2026

---

## Index of Architecture Decision Records (ADRs)

| ADR ID | Title | Addressed Risk | Status |
|---|---|---|---|
| **ADR-001** | Parameterized Motor Starter Selection vs. Hardcoded kW Cutoffs | **RSK-001** | **ADOPTED** |
| **ADR-002** | Explicit `ProjectDesignBasis` Voltage Drop Criteria vs. Universal 3%/5% | **RSK-002** | **ADOPTED** |
| **ADR-003** | Standards Provenance & Restriction of Complex Arc Flash Claims | **RSK-003** | **ADOPTED** |
| **ADR-004** | Parametric Spare Margins & Thermal Design vs. Hardcoded Rules | **RSK-004** | **ADOPTED** |
| **ADR-005** | Elimination of "Statutory Compliance Certified" in Favor of `EvaluationStatus` | **RSK-005** | **ADOPTED** |
| **ADR-006** | Commercial Claims Reclassification as "Hypotheses for Validation" | **RSK-006** | **ADOPTED** |
| **ADR-007** | Mandatory `TraceableValue<T>` Envelope for All Ingested Data | Architecture | **ADOPTED** |
| **ADR-008** | Pure, Side-Effect-Free Function Contract for Deterministic Engine | Architecture | **ADOPTED** |

---

## ADR-001: Parameterized Motor Starter Selection Matrix
- **Context:** Previous prototypes used fixed, arbitrary motor kW cutoffs (e.g., $\le 5.5\text{ kW}$ DOL, $7.5 - 22\text{ kW}$ Star-Delta, $\ge 30\text{ kW}$ Soft Starter). In industrial practice, starter selection is governed by supply system fault level ($I_{sc}$), permitted transient bus voltage dip ($\le 10\%$ or $\le 15\%$), starting torque profile ($T_L$ vs $T_M$), duty cycle, and process speed regulation needs.
- **Decision:** Remove all hardcoded kW cutoffs. Implement a multi-criteria decision matrix driven by `MotorStartingCriteria` (Maximum allowable starting current ratio, bus voltage dip constraint, driven machine load inertia, process variable speed requirement).
- **Consequence:** The engine accurately models applications where a $15\text{ kW}$ motor on a stiff utility bus starts DOL, or a $5.5\text{ kW}$ pump on a soft generator bus requires a Soft Starter.

---

## ADR-002: Explicit Voltage Drop Criteria & Handling of Missing Deratings
- **Context:** Applying blanket $3.0\%$ or $5.0\%$ voltage drop limits globally ignores the vital distinction between utility point-of-common-coupling (PCC) vs. internal plant distribution, motor running vs. motor starting, and installation conditions (buried vs. tray, grouping, soil resistivity).
- **Decision:** Require explicit `VoltageDropCriteria` passed per circuit from `ProjectDesignBasis`. If cable length, operating temperature, or installation deratings are omitted, the calculation engine MUST NOT assume default values or crash; it MUST return `EvaluationStatus: NOT_ASSESSED` and list the exact missing parameters.
- **Consequence:** Eliminates false-positive compliance claims on incomplete project datasets.

---

## ADR-003: Standards Provenance & Arc Flash MVP Scoping
- **Context:** The preliminary compendium cited empirical arc flash and short-circuit force formulas without explicit parameter validity boundaries or edition metadata (IEEE 1584:2002 vs. 2018).
- **Decision:**
  1. Restrict Arc Flash calculations in the core MVP to verified preliminary screening models clearly marked `REVIEW_REQUIRED`, with mandatory full IEEE 1584:2018 parameter verification.
  2. All standard citations must include exact standard issuer, number, edition year, and clause reference (e.g., IEC 60364-5-52:2019 Table B.52.4).
- **Consequence:** Protects engineering liability and ensures compliance with scientific accuracy principles.

---

## ADR-004: Parametric Margins vs. Hardcoded Rules-of-Thumb
- **Context:** Fixed $20\%$ spare feeders, fixed busbar current density ($1.2\text{ A/mm}^2$), and fixed earth resistance ($< 1\text{ }\Omega$) were presented as universal statutory mandates.
- **Decision:** Move all design margins into versioned `ProjectDesignBasis` fields (`spare_feeder_philosophy_pct`, `transformer_growth_margin_pct`, `target_earth_grid_resistance_ohm`). Switchboard busbars are evaluated primarily on thermal temperature rise equilibrium (IEC 61439-1 Table 6) rather than arbitrary current density.
- **Consequence:** Accommodates diverse client specifications across oil & gas, data centers, and light industrial plants.

---

## ADR-005: Elimination of Blanket "Statutory Compliance Certified" Claims
- **Context:** UI badges and test outputs claimed "100% Statutory Compliance Verified". Legally, compliance can only be certified by a licensed statutory Engineer-of-Record (EOR) on complete, un-redacted construction documentation.
- **Decision:** Strip all "Statutory Compliance Certified" strings from the codebase, UI, and test suites. Replace with four strictly defined states:
  - `PASS` (Meets specified project acceptance criteria)
  - `FAIL` (Violates specified project criteria)
  - `NOT_ASSESSED` (Inputs or criteria missing)
  - `REVIEW_REQUIRED` (Borderline or requires qualified human review)
- **Consequence:** Aligns software output with professional engineering licensing laws and ethics.

---

## ADR-006: Reclassification of Commercial Figures as Validation Hypotheses
- **Context:** Pricing tiers (₹2,499 - ₹14,999 / $49 - $249), margins (95%), and conversion rates were stated as established market facts.
- **Decision:** Prefix all commercial documents with `COMMERCIAL HYPOTHESIS — FOR PILOT VALIDATION`. All client-facing copy must focus on traceable engineering value rather than unsubstantiated ROI claims.
