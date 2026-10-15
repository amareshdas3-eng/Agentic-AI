# Product 02: LoadFlow & VoltageDrop Pro — Agentic Master Prompt
### Direct Copy-Paste Turnkey Execution Prompt for AI Coding Agents
**Target Environment:** Antigravity IDE / Node.js / Python / Modern Web

---

```markdown
PRODUCT 02 — PROENGINEERING LOADFLOW & VOLTAGEDROP PRO
EXECUTION COMMAND: BUILD DETERMINISTIC LOAD FLOW & VOLTAGE DROP CALCULATION ENGINE

[PERSONA & ROLES]
Act as a Principal Power System Studies Engineer (PE/CEng), Senior Electrical Software Mathematician, and Independent QA Verification Specialist.

[TASK DEFINITION]
Develop "LoadFlow & VoltageDrop Pro" as a standalone, sellable engineering application and API for ProEngineering.in. The product accepts industrial plant load schedules, executes rigorous, deterministic balanced radial load flow and cable voltage-drop calculations, cross-checks results using dual-solver methods, and produces audit-ready engineering calculation workbooks and exception registers.

[NON-NEGOTIABLE OPERATING RULES]
1. ZERO LLM ARITHMETIC:
   Under no circumstances may mathematical operations (multiplication, square roots, trigonometric functions, vector sums) be performed via LLM token generation. Implement all calculations in pure TypeScript/JavaScript or Python functions.
2. TEMPERATURE-ADJUSTED RESISTANCE:
   Never use DC resistance at 20°C for operating voltage drop! The calculation engine MUST adjust conductor resistance to maximum operating temperature:
   - For XLPE: T_op = 90°C (or actual operating temperature based on load ratio).
   - For PVC: T_op = 70°C.
   Formula: R_theta = R_20 * [1 + alpha_20 * (theta - 20)]
   Where alpha_20 = 0.00393 for Copper, 0.00403 for Aluminium.
3. TRUE IMPEDANCE VOLTAGE DROP:
   Never use simplified DC formulas (V = 2*I*R) for AC industrial feeders!
   For balanced 3-phase:
   V_drop = sqrt(3) * I_b * L * (R_ac * cos(phi) + X_L * sin(phi)) / 1000
   For single-phase 2-wire:
   V_drop = 2 * I_b * L * (R_ac * cos(phi) + X_L * sin(phi)) / 1000
   Percentage drop: %V_drop = (V_drop / V_nominal) * 100%
4. STATUTORY LIMIT ENFORCEMENT:
   Check each calculated percentage against project limits:
   - Branch Feeder: <= 3.0% (Flag WARNING if > 3.0%).
   - Total Substation to Load: <= 5.0% (Flag VIOLATION if > 5.0%).
   - Motor Starting Dip: <= 15.0% (Flag CRITICAL if > 15.0%).
5. DUAL-SOLVER VERIFICATION GATE:
   The Independent Verification Agent MUST independently calculate the voltage drop using the complex phasor voltage drop formula:
   Delta_V_phasor = |V_source - I_phasor * Z_cable|
   Verify that |V_drop_primary - V_drop_phasor| / V_nominal < 0.1%.

[THE 5-AGENT IMPLEMENTATION WORKFLOW]

AGENT 1 — REQUIREMENTS & LOAD INTAKE:
- Ingest system frequency (50/60 Hz), nominal line voltage (e.g. 415V), and load list.
- Validate each feeder: Tag, Description, kW, Power Factor, Efficiency, Length (m), Conductor, Size (mm²), Parallel Runs.
- Flag any missing parameters or impossible inputs (e.g., PF > 1.0, Efficiency > 100%).

AGENT 2 — DETERMINISTIC CALCULATION SPECIALIST:
- Implement pure functions for:
  - Full load current: I_FLC = P_kW / (sqrt(3) * V_LL * PF * eff)
  - Demand power aggregation: Group by Continuous (100%), Intermittent (50%), Standby (0%).
  - Total Switchboard Active (kW), Reactive (kvar), and Apparent (kVA) demand.
  - Conductor resistance at operating temperature (R_90 or R_70).
  - Effective impedance: Z_eff = (R * cos(phi) + X * sin(phi)) / N_runs.
  - Steady-state running voltage drop (Volts and %).
  - Motor starting transient voltage drop (I_start = 6.0 * I_FLC, cos(phi_start) = 0.30).

AGENT 3 — INDEPENDENT VERIFICATION & BOUNDARY TESTING:
- Re-run all calculations using secondary per-unit / complex node solver.
- Execute edge cases: Zero length, extreme power factor (0.5 lagging), unity power factor (1.0), 150% overload.
- Compare with published hand-calculated benchmarks (Case 1 to Case 5 in `TEST_BENCHMARKS_AND_EDGE_CASES.md`).

AGENT 4 — DOCUMENTATION & EXPORT ENGINE:
- Generate complete Markdown/HTML/PDF calculation sheets with step-by-step mathematical proofs:
  - Formula written in LaTeX notation.
  - Substituted numerical values.
  - Result with SI units and compliance badge (PASS / FAIL).
- Generate downloadable CSV "Feeder Loading & Voltage Drop Schedule".
- Generate Exception Register highlighting limiting feeders.

AGENT 5 — QUALITY GATE & HUMAN SIGN-OFF:
- If any feeder exceeds 5.0% drop, block the "RELEASE CANDIDATE" seal and label output:
  "PRELIMINARY — CONTAINS CODE VIOLATIONS".
- Provide human approval and revision block.

[DELIVERABLE ARTIFACTS TO CREATE]
1. `PRODUCT_SPECIFICATION.md`: Detailed functional scope, standards, and inputs.
2. `AGENTIC_MASTER_PROMPT.md`: This execution prompt.
3. `DETERMINISTIC_CALCULATION_ENGINE.md`: Complete mathematical formulas, AC resistance tables, inductive reactance tables, and TypeScript/Python code implementation.
4. `TEST_BENCHMARKS_AND_EDGE_CASES.md`: 5 hand-calculated test cases with exact expected values and verification tolerances.
5. `COMMERCIAL_PACKAGE.md`: Product page copy, pricing tiers (₹2,499 - ₹4,999 / $49 - $79), and sample calculation workbook.
```
