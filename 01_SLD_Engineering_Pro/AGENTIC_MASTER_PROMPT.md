# Product 01: SLD Engineering Pro — Agentic Master Prompt
### Direct Copy-Paste Turnkey Execution Prompt for AI Coding Agents
**Target Environment:** Antigravity IDE / Node.js / Python / Modern Web

---

```markdown
PRODUCT 01 — PROENGINEERING SLD ENGINEERING PRO
EXECUTION COMMAND: BUILD STANDALONE SLD GENERATION & VERIFICATION ENGINE

[PERSONA & ROLES]
Act as a Principal Electrical Substation Design Engineer (30+ years in industrial power distribution), Lead Electrical CAD Automation Architect, and Senior Protection Coordination Auditor.

[TASK DEFINITION]
Build "SLD Engineering Pro" as a commercial-grade, standalone engineering application and API for ProEngineering.in. The application converts industrial project inputs into validated, standards-compliant, drawing-ready Single Line Diagrams (SLD), structured electrical topology graphs, equipment schedules, and automated design audit reports.

[NON-NEGOTIABLE OPERATING RULES]
1. ZERO LLM DRAWING HALLUCINATIONS:
   Never generate freehand or unconstrained raster images as an engineering diagram. The SLD MUST be rendered deterministically using a vector SVG layout engine driven by an explicit directed graph model (Nodes: Sources, Transformers, Breakers, Busbars, Outgoing Feeders; Edges: Cables, Busway, Overhead Line).
2. TOPOLOGY INTEGRITY & SANITY CHECKS:
   Enforce rigorous graph verification rules:
   - Zero floating buses or isolated nodes.
   - Dual-incomer interlocking logic: Enforce standard "2-out-of-3" interlock rule (Incomer 1, Incomer 2, Bus Coupler — maximum two closed simultaneously unless automatic momentary paralleling is specifically permitted).
   - Voltage level continuity: Flag any transformer step-up/step-down where secondary nominal voltage does not match connected busbar voltage.
   - Unique equipment tagging: Enforce strict uniqueness for all device tags, feeder IDs, and bus IDs.
3. STANDARDS ADHERENCE:
   - Symbols must comply with IEC 60617 (European/International) with a toggle for IEEE 315 / ANSI (North American).
   - Draw circuit breakers with correct symbol representations: drawout VCB with isolation plugs, fixed/drawout ACB, MCCB with thermal-magnetic or electronic trip units.
   - Mark CT/PT cores with primary/secondary ratios and protection/metering class (e.g., 5P20 for protection, Class 0.2S for tariff metering).
4. DELIVERABLE STATUS LABELS:
   Clearly watermark and mark all generated SVGs, PDFs, and schedules with:
   - "PRELIMINARY DESIGN - NOT FOR CONSTRUCTION" (Default)
   - "VERIFIED TOPOLOGY - PROENGINEERING AUDIT PASSED" (Only when 100% of topological rules pass).

[STEP-BY-STEP SPECIALIST WORKFLOW TO IMPLEMENT]

AGENT 1 — REQUIREMENTS & TOPOLOGY INTAKE:
- Accept project metadata: Project Name, Location, Grid Incomer Voltage (e.g. 33kV), Primary Distribution (11kV), LV Utilization (415V/230V), Frequency (50Hz/60Hz), Fault Level (MVA / kA).
- Accept incoming source specifications: Grid Feeders (1 or 2), Captive Power / DG sets, Solar PV, UPS.
- Accept transformer configurations: Rating (kVA), Ratio (33/11kV, 11/0.433kV), % Impedance, Vector Group (Dyn11, YNd11), Tap Changer (OCTC / OLTC).
- Accept busbar arrangements: Single Bus, Split Bus with Bus Coupler, Ring Main.
- Accept outgoing feeder schedules: Feeder Tag, Load Description, Rated kW, Cable Type, Length, Breaker Type.

AGENT 2 — TOPOLOGY ENGINE & GRAPH BUILDER:
- Build a directed acyclic graph (DAG) representing the power flow hierarchy:
  Grid Incomers -> 33kV Switchyard -> Step-Down Transformers -> 11kV Switchboard -> Distribution Transformers -> 415V PCC -> MCCs -> Sub-Distribution Boards.
- Compute node coordinates dynamically:
  - Calculate grid X/Y positions ensuring no crossing busbars.
  - Position Incomers on Section A (left) and Section B (right) with the Bus Coupler centered.
  - Distribute outgoing feeders symmetrically downwards along busbars.

AGENT 3 — INDEPENDENT ELECTRICAL REVIEW & AUDIT:
- Execute 10 automated graph audit checks:
  1. Isolated Bus Check: Find any bus with 0 incoming or 0 outgoing connections.
  2. Voltage Mismatch Check: Compare transformer secondary rating with downstream bus rating.
  3. Transformer Loading Check: Sum connected continuous kVA on downstream bus and compare against transformer rated capacity.
  4. Coupler Rating Check: Verify bus coupler breaker rating is equal to or greater than the largest incoming breaker rating.
  5. Backfeed & Parallel Grid Risk Check: Flag any closed loop between unsynchronized sources.
  6. Protection Interface Check: Verify presence of Surge Arresters on incoming HV overhead lines and neutral earthing CTs on transformers.
  7. Spare Feeder Allowance: Flag if switchgear has less than 20% installed spare feeders.
  8. Tag Duplicate Check: Flag any non-unique tag.
  9. Cable Size Feasibility: Flag any feeder where cable size is unassigned.
  10. Voltage Drop Propagation: Check that total cascaded voltage drop does not exceed allowable statutory limits.

AGENT 4 — VECTOR SCHEMATIC & SCHEDULE GENERATOR:
- Render high-resolution, interactive SVG diagram:
  - Clean styling: Slate dark `#0f172a` background or white blueprint background `#ffffff`.
  - Crisp vector lines with hover tooltips showing bus voltage, load current, breaker rating, and cable spec.
  - Interactive clickable nodes showing detailed equipment parameters.
- Generate downloadable CSV/Markdown schedules:
  - Switchboard Incomer & Coupler Schedule.
  - Outgoing Feeder Schedule.
  - Transformer & Auxiliary Equipment Register.
  - Design Assumptions & Verification Gaps Log.

AGENT 5 — QUALITY GATE & HUMAN SIGN-OFF:
- Block export of "VERIFIED" status if any critical violation exists.
- Provide a clear Human Approval Block on the final drawing title block:
  "Designed By", "Checked By", "Approved By", "Revision", "Date", "Engineering Disclaimer".

[DELIVERABLE ARTIFACTS TO CREATE]
1. `PRODUCT_SPECIFICATION.md`: Detailed functional requirements, inputs, outputs, and standards.
2. `TOPOLOGY_SCHEMA_AND_SVG_ENGINE.md`: JSON schema for the electrical graph and SVG generation algorithms.
3. `CALCULATION_AND_VERIFICATION_RULES.md`: Mathematical rules for bus continuity, coupler interlocking, and CT/PT sizing.
4. `COMMERCIAL_PACKAGE.md`: Product page copy, pricing tiers (India ₹ / Global $), feature matrix, sample output, and user guide.
```
