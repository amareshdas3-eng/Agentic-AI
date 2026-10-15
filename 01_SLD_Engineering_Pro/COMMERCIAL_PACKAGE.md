# SLD Engineering Pro — Commercial Package & Launch Kit
### Product Page Copy, Pricing Tiers, Sample Deliverables, and FAQ
**Platform:** ProEngineering.in | Industrial Digital Products

---

## 1. High-Converting Product Page Copy

### Hero Headline:
> # Stop Drawing Dumb Lines.
> ### Build Verified, Standards-Compliant Industrial Single Line Diagrams in Minutes — Backed by Topological Graph Logic.

### Sub-Headline:
*The first agentic power systems diagramming tool engineered for substation EPCs, consulting firms, and plant managers. Automatically generates drawing-ready vector SLDs (33kV to 415V), verifies 2-out-of-3 coupler interlocking, detects bus voltage mismatches, and exports switchgear schedules.*

---

## 2. The Core Problem vs. The ProEngineering Solution

| The Traditional Way (AutoCAD / Visio / Excel) | The SLD Engineering Pro Way |
|---|---|
| **Dumb Graphics:** A CAD line has no electrical intelligence; errors in voltage or transformer taps go unnoticed until site commissioning. | **Topological Graph Engine:** Every line is a verified circuit branch with voltage, impedance, and fault withstand properties. |
| **Manual Discrepancies:** Outgoing feeder schedule doesn't match the SLD labels, causing vendor rework and change orders. | **Unified Source of Truth:** Diagrams and schedules are dynamically rendered from the exact same validated JSON database. |
| **Interlocking Blunders:** Parallel grid tie-in or coupler mistakes risk switchgear explosion under fault conditions. | **Automated 2-out-of-3 Interlock Verification:** Mathematical state machines guarantee safe operating configurations. |
| **Hours of Drafting:** Drawing symbols, tagging CTs/PTs, and formatting title blocks takes 15–25 engineering hours per project. | **Instant Vector Delivery:** Generates complete IEC 60617 / IEEE 315 SVG diagrams and schedules in seconds. |

---

## 3. Product Pricing Tiers

| Tier | India Pilot Price | International Pilot Price | Target Customer | Inclusions |
|---|---|---|---|---|
| **Starter (Self-Service)** | **₹2,999** per project | **$59** per project | Electrical Contractors & Panel Estimators | Single-voltage distribution SLDs (up to 20 feeders), SVG diagram, feeder schedule export, basic connectivity audit. |
| **Professional (Substation)** | **₹4,999** per project | **$89** per project | EPC Contractors & Industrial Consultants | Full 33kV/11kV/415V substation hierarchy, dual incomers + bus coupler interlocking, transformer checks, CT/PT schedules, vector SVG + CAD DXF metadata. |
| **Enterprise / Engineer-Reviewed** | **₹12,499** per project | **$219** per project | Critical Infrastructure, Data Centers & Process Plants | Includes everything in Professional + **Independent Senior PE/CEng review & signed design-audit memorandum**. |

---

## 4. Deliverables Checklist Provided to Customer

Upon completing a project in `SLD Engineering Pro`, the customer instantly downloads a `.ZIP` package containing:
1. `SLD_Primary_Substation.svg`: High-resolution, interactive vector diagram with IEC 60617 symbols and color-coded voltage levels.
2. `Switchgear_Incomer_Coupler_Schedule.csv`: Formatted schedule with breaker continuous ratings ($I_n$), breaking capacity ($I_{cu}$), and trip unit parameters.
3. `Outgoing_Feeder_Schedule.csv`: Complete load, cable tag, and protective device register.
4. `Transformer_and_Auxiliary_Register.pdf`: Technical ratings, tap settings, vector group, and cooling summary.
5. `Topological_Verification_Audit_Report.pdf`: 10-point mathematical audit report showing pass/fail status on voltage continuity, interlocking, and loading ratios.

---

## 5. Sample Output Preview

```
========================================================================================
PROENGINEERING.IN — ELECTRICAL DESIGN VERIFICATION CERTIFICATE
Product: SLD Engineering Pro (v1.0.0) | Project ID: PE-SUB-3311-01
========================================================================================
Design Status: VERIFIED TOPOLOGY — ZERO CRITICAL DEFECTS
System Topology: Dual 33kV Transmission Incomers -> 2 x 5MVA 33/11kV Dyn11 Transformers
                 11kV Split-Bus Switchboard (1250A) with Motorized Bus Coupler

TOPOLOGICAL CHECKS:
[PASS] Bus Voltage Continuity: 33kV Switchyard -> 11kV Switchboard -> 415V PCC verified.
[PASS] Bus Coupler Interlock: 2-out-of-3 Castell Scheme mathematically validated.
[PASS] Equipment Tags: 48 unique tags verified (0 duplicates).
[PASS] Transformer Loading: Peak demand = 3,840 kVA (76.8% loading on 5MVA base).
[PASS] Spare Feeders: 4 spare compartments allocated (22.2% reserve capacity).

WATERMARK: PRELIMINARY DESIGN — AUDITED BY PROENGINEERING GRAPH SOLVER
========================================================================================
```
