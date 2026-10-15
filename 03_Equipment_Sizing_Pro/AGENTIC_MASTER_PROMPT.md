# Product 03: Equipment Sizing Pro — Agentic Master Prompt
### Direct Copy-Paste Turnkey Execution Prompt for AI Coding Agents
**Target Environment:** Antigravity IDE / Node.js / Python / Modern Web

---

```markdown
PRODUCT 03 — PROENGINEERING EQUIPMENT SIZING PRO
EXECUTION COMMAND: BUILD MODULAR EQUIPMENT SIZING & SPECIFICATION ENGINE

[PERSONA & ROLES]
Act as a Senior Equipment Procurement & Application Engineer, Power Transformer Specialist, Switchgear Rating Auditor, and Independent Electrical Checker.

[TASK DEFINITION]
Develop "Equipment Sizing Pro" as a standalone, sellable engineering application and API for ProEngineering.in. The product calculates, cross-verifies, and documents optimal ratings for transformers, power cables, low- and medium-voltage circuit breakers, and switchboard busbars. It outputs mathematically justified sizing sheets, equipment comparison tables, and vendor-ready technical datasheets.

[NON-NEGOTIABLE OPERATING RULES]
1. ZERO FABRICATED EQUIPMENT RATINGS:
   Never invent non-standard equipment capacities or catalog values. All selections must map to verified international commercial standards (e.g., standard kVA ratings per IEC 60076, standard frame sizes per IEC 60947-2, standard conductor cross-sections per IEC 60228).
2. ADIABATIC FAULT WITHSTAND IS MANDATORY:
   When sizing cables, never check continuous thermal ampacity alone! You MUST verify the adiabatic short-circuit thermal withstand formula:
   S_min = (I_sc * sqrt(t)) / k
   Where:
   - k = 143 for Copper conductor with XLPE insulation (initial 90°C, final 250°C).
   - k = 94 for Aluminium conductor with XLPE insulation.
   - k = 115 for Copper conductor with PVC insulation (initial 70°C, final 160°C).
   - k = 76 for Aluminium conductor with PVC insulation.
   If S_selected < S_min, the cable is UNACCEPTABLE even if voltage drop and continuous current pass!
3. CIRCUIT BREAKER FOUR-POINT CHECK:
   Every circuit breaker selection must explicitly evaluate:
   - I_n >= I_b (Continuous rated current >= Design load current).
   - I_cu >= I_sc (Ultimate breaking capacity >= Prospective symmetrical short-circuit current).
   - I_cs >= 0.75 * I_cu (Service breaking capacity check; 100% preferred for process plants).
   - I_cw check (Short-time withstand for Category B selective breakers).
4. TRANSFORMER COOLING & ALTITUDE DERATING:
   Account for installation altitude: If altitude > 1000m, apply 0.3% capacity derating per 100m over 1000m per IEC 60076. If ambient temperature > 40°C, apply continuous thermal derating.

[THE 5-AGENT WORKFLOW TO IMPLEMENT]

AGENT 1 — INTAKE & ENVIRONMENTAL AUDIT:
- Ingest design requirements: Total connected load, demand factor, growth margin (%), ambient temperature (°C), installation altitude (m), prospective fault level (kA), fault duration (seconds), system voltage (V).
- Determine combined derating factor (k_total).

AGENT 2 — DETERMINISTIC EQUIPMENT SIZING:
- Module A: Transformer Sizing
  - Calculate required continuous kVA: S_req = S_demand * (1 + Growth%) / k_derating.
  - Select next standard higher rating (S_std).
  - Calculate rated primary and secondary currents: I_pri = S_std / (sqrt(3) * V_pri), I_sec = S_std / (sqrt(3) * V_sec).
  - Estimate full load copper losses (I²R) and transformer short-circuit impedance.
- Module B: Power Cable Sizing (Four-Check Pipeline)
  - Continuous thermal current check: I_z = I_base * k_total >= I_b.
  - Voltage drop check: %Delta_V <= Limit% (3.0%).
  - Motor starting dip check: %Delta_V_start <= 15.0%.
  - Short-circuit withstand check: S_actual >= (I_sc * sqrt(t)) / k.
  - Recommend optimal standard size (mm²) and number of parallel runs.
- Module C: Circuit Breaker & Switchgear Selection
  - Select standard frame size (A) and trip unit rating (A).
  - Select breaking capacity (kA) >= Prospective fault current.
  - Category A (Current limiting) vs. Category B (Time-delayed selective).
- Module D: Busbar Sizing & Peak Force Check
  - Current density check: Typically <= 1.2 to 1.5 A/mm² for Copper, <= 0.8 to 1.0 A/mm² for Aluminium.
  - Adiabatic fault temperature rise check.
  - Electrodynamic peak mechanical stress check: F_peak = 0.2 * (I_peak)² / d (in N/m).

AGENT 3 — INDEPENDENT SIZING VERIFICATION:
- Challenge all selections with boundary stress tests.
- Verify whether breaker downstream of transformer can safely clear secondary terminal bolted short-circuit fault without exceeding breaking capacity.
- Flag any mismatch between transformer rating and cable ampacity.

AGENT 4 — TECHNICAL SPECIFICATION & DATASHEET BUILDER:
- Produce procurement-ready Equipment Datasheets (PDF / Markdown):
  - Transformer Technical Datasheet (Ratings, Losses, Taps, Bushings, Impedance, Accessories).
  - Power Cable Schedule & Datasheet (Voltage grade, conductor, insulation, screen, armor, outer sheath).
  - Circuit Breaker Specification Sheet (Frame, Poles, Breaking Capacity, Protection Functions LSIG).
  - Switchboard Busbar Specification (Material, Conductivity, Cross-section, Phase Spacing, Support Distance).

AGENT 5 — QUALITY GATE & HUMAN SIGN-OFF:
- Verify that every selected equipment rating is backed by deterministic mathematical proofs.
- Apply disclaimer: "EQUIPMENT SIZING RECOMMENDATION — FINAL PROCUREMENT SUBJECT TO DETAILED ENGINEERING AND VENDOR SUBMITTALS".

[DELIVERABLE ARTIFACTS TO CREATE]
1. `PRODUCT_SPECIFICATION.md`: Functional architecture, derating models, standard repositories.
2. `AGENTIC_MASTER_PROMPT.md`: This turnkey prompt.
3. `SIZING_METHODOLOGIES_AND_STANDARDS.md`: Mathematical proofs, adiabatic constants (k), and derating lookup tables.
4. `DATASHEET_AND_BOM_TEMPLATES.md`: Engineering datasheets and bill of materials templates.
5. `COMMERCIAL_PACKAGE.md`: Product page copy, pricing tiers (₹2,999 - ₹5,999 / $59 - $99), and sample output.
```
