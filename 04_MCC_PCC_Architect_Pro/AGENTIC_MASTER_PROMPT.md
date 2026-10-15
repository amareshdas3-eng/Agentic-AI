# Product 04: MCC & PCC Architect Pro — Agentic Master Prompt
### Direct Copy-Paste Turnkey Execution Prompt for AI Coding Agents
**Target Environment:** Antigravity IDE / Node.js / Python / Modern Web

---

```markdown
PRODUCT 04 — PROENGINEERING MCC & PCC ARCHITECT PRO
EXECUTION COMMAND: BUILD COMPARTMENTALIZED SWITCHBOARD & MOTOR FEEDER ARCHITECTURE ENGINE

[PERSONA & ROLES]
Act as a Principal Switchboard Applications Engineer, Industrial Motor Control Specialist, and Low-Voltage Assembly Auditor (IEC 61439-1/2 expert).

[TASK DEFINITION]
Develop "MCC & PCC Architect Pro" as a standalone, sellable engineering application and API for ProEngineering.in. The application ingests plant load lists, applies deterministic starter selection logic (DOL, Star-Delta, Soft Starter, VFD), stacks feeders into physically viable panel tiers and columns, generates complete control/automation interface schedules (PLC/DCS I/O), and exports preliminary switchboard Bills of Materials (BOM) and line-up elevation layouts.

[NON-NEGOTIABLE OPERATING RULES]
1. ZERO ARBITRARY STARTER SELECTION:
   Never select a motor starter solely by motor kW! Implement the deterministic decision hierarchy:
   - Check supply transformer kVA and network fault level.
   - <= 5.5 kW (or <= 7.5 kW if grid is stiff): Direct-on-Line (DOL) permissible.
   - 7.5 kW to 30 kW: Star-Delta (reduced starting current to 33% of DOL) or Soft Starter if starting torque is light/medium.
   - > 30 kW to 75 kW: Electronic Soft Starter with internal bypass contactor.
   - Variable flow/pressure applications (Pumps/Fans with modulating process control): Variable Frequency Drive (VFD).
   - High inertia / heavy starting (Crushers, Ball Mills, Conveyors): Heavy-duty Soft Starter or VFD with dynamic braking.
2. PHYSICAL COMPARTMENT & THERMAL FEASIBILITY:
   - Enforce standard switchboard column height (2100mm to 2200mm) and usable functional space (typically 1800mm vertical height divided into standard module units).
   - VFD heat dissipation rule: For any VFD module > 22 kW, flag required forced ventilation or heat heat-pipe ducting (approx. 3% of drive rating dissipated as heat).
   - Maintain minimum 20% equipped spare feeders across all motor kW tiers.
3. STANDARDS COMPLIANCE:
   - Enforce IEC 61439-2 Form 3b or Form 4b internal separation.
   - Motor protection coordination: Type 2 Coordination per IEC 60947-4-1 (requires no damage to overload relay or contactor after short circuit cleared by upstream breaker/fuse).
4. PRELIMINARY BOM DISCLAIMER:
   All generated BOMs and panel line-up layouts must be watermarked:
   "PRELIMINARY ARCHITECTURE PROPOSAL — SUBJECT TO SWITCHBOARD BUILDER DETAILED PRODUCTION ENGINEERING".

[THE 5-AGENT IMPLEMENTATION PIPELINE]

AGENT 1 — LOAD LIST INTAKE & CLASSIFICATION:
- Ingest motor and non-motor load list: Tag, Description, Motor kW, Service Factor, Process Duty (Continuous / Standby), Driven Machine Type (Centrifugal Pump, Blower, Compressor, Agitator, Conveyor), Starting Frequency (starts per hour).
- Group loads by plant area and bus section.

AGENT 2 — STARTER SELECTION & FEEDER SIZING:
- Apply starter decision matrix to choose DOL, Star-Delta, Soft Starter, or VFD.
- Calculate:
  - Motor full load current (FLC).
  - Breaker / MPCB rating: Typically 1.25 to 1.5 x FLC (magnetic instantaneous trip set to 10 to 12 x FLC).
  - Contactor rating (AC-3 duty) sized for continuous motor current.
  - Overload thermal relay range (0.9 to 1.1 x FLC).
  - Minimum cable cross-section (mm²) and feeder terminal size.

AGENT 3 — PHYSICAL COLUMN STACKING & TIER ARCHITECTURE:
- Calculate module heights (e.g., 200mm, 300mm, 400mm, 600mm, full height).
- Stack modules into standard switchboard vertical columns (800mm width for feeders + 300mm cable alley).
- Allocate incoming section (ACB 1000mm to 1200mm width), bus coupler section, and outgoing motor feeder columns.
- Ensure balanced load distribution across Bus Section A and Bus Section B.

AGENT 4 — CONTROL & AUTOMATION INTERFACE REGISTER:
- Generate complete PLC/DCS I/O schedule:
  - Hardwired Signals: Run, Trip, Local/Remote, Emergency Stop, Start, Stop.
  - Analog Signals: Motor current (4-20mA), PT-100 temperature sensors.
  - Communication Protocol: Dual Modbus-TCP / Profinet interface for smart relays.
- Generate Switchboard Elevation Drawing Data (SVG / CAD JSON).

AGENT 5 — QUALITY GATE & BOM EXPORTER:
- Verify total switchboard current does not exceed busbar continuous rating.
- Verify total spare feeder percentage is >= 20%.
- Export complete Preliminary BOM with component catalog references.

[DELIVERABLE ARTIFACTS TO CREATE]
1. `PRODUCT_SPECIFICATION.md`: Functional scope, starter decision rules, physical modularity.
2. `AGENTIC_MASTER_PROMPT.md`: This execution prompt.
3. `STARTER_SELECTION_AND_FEEDER_LOGIC.md`: Decision matrix, Type 2 coordination parameters, contactor AC-3 sizing formulas.
4. `PANEL_ARCHITECTURE_BOM_TEMPLATE.md`: Switchboard line-up layout, compartment schedule, control register, and preliminary BOM template.
5. `COMMERCIAL_PACKAGE.md`: Product page copy, pricing tiers (₹3,999 - ₹7,999 / $79 - $129), and sample output.
```
