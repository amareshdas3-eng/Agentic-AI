# LoadFlow & VoltageDrop Pro — Commercial Package & Launch Kit
### Product Page Copy, Pricing Tiers, Sample Deliverables, and FAQ
**Platform:** ProEngineering.in | Flagship Commercial Product #01

---

## 1. High-Converting Product Page Copy

### Hero Headline:
> # Ditch the Buggy Excel Spreadsheets.
> ### Instant, Audit-Ready Industrial Load Schedules & Cable Voltage Drop Calculations — Verified by Dual Mathematical Solvers.

### Sub-Headline:
*The precision engineering software created specifically for electrical design consultants, EPC estimators, and plant facility engineers. Generates rigorous feeder schedules, true impedance voltage drop proofs, and motor starting analysis — formatted for immediate client submittal.*

---

## 2. Why Engineers and Contractors Choose LoadFlow Pro

- **100% Proven Math — Zero Guesswork:**
  Stop worrying whether your junior engineer remembered to temperature-derate the cable resistance or added the inductive reactance term ($X_L$). LoadFlow Pro applies full IEC 60364-5-52 and IEEE 141 physics automatically.
- **Client-Ready Submittal Reports in 60 Seconds:**
  Export beautiful, professional calculation workbooks featuring full mathematical proofs, LaTeX equations, and compliance stamps that pass consultant audits on the first pass.
- **Motor Starting Inrush Analysis Included:**
  Immediately know whether that large direct-on-line (DOL) chiller or pump will cause a nuisance brownout or trip upstream sensitive equipment.
- **Dual-Solver Verification Guarantee:**
  Every calculated feeder is independently checked by our secondary vector node solver before output generation.

---

## 3. Product Pricing Tiers

| Tier | India Price | Global Price | Best For | Features & Inclusions |
|---|---|---|---|---|
| **Pay-Per-Project** | **₹2,499** | **$49** | Independent Electrical Contractors | Up to 30 feeders per project, Excel/CSV load schedule import, PDF calculation report, CSV feeder schedule export. |
| **Consultant Pro** | **₹4,499** | **$79** | MEP Consulting Firms & EPC Engineers | Unlimited feeders, multi-bus radial distribution, motor starting inrush analysis, customizable company logo & title block, Excel workbook export. |
| **Enterprise / Peer-Reviewed** | **₹9,999** | **$179** | Mission-Critical Submittals | Everything in Consultant Pro + **Independent Review Memorandum signed by an accredited Senior Power Systems Engineer (PE/CEng)**. |

---

## 4. Sample Deliverable Excerpt

```markdown
========================================================================================
PROENGINEERING.IN — CABLE VOLTAGE DROP CALCULATION PROOF
Standard: IEC 60364-5-52:2019 / IS 732:2019 | Project: PE-IND-PMP-01
========================================================================================
Feeder Tag:         MCC-01-FDR-08
Load Description:   Cooling Tower Water Circulation Pump Motor #2
Operating Voltage:  415 V (3-Phase, 50 Hz)
Rated Power:        75.0 kW | Power Factor: 0.85 Lagging | Efficiency: 93.0%
Cable Detail:       3C x 95 mm² Aluminium, XLPE Insulated (L = 120.0 m, 1 Run)

STEP 1: DESIGN CURRENT CALCULATION
I_b = P_kW / (sqrt(3) * V_LL * cos(phi) * eta)
    = 75,000 W / (1.73205 * 415 V * 0.85 * 0.93)
    = 132.02 Amperes

STEP 2: CONDUCTOR IMPEDANCE AT OPERATING TEMPERATURE (90°C)
R_90 = R_20 * [1 + 0.00403 * (90 - 20)] = 0.3200 * 1.2821 = 0.4103 Ohm/km
X_L  = 0.0760 Ohm/km
Z_effective = R_90 * cos(phi) + X_L * sin(phi)
            = (0.4103 * 0.85) + (0.0760 * 0.5268) = 0.3888 Ohm/km

STEP 3: VOLTAGE DROP CALCULATION
Delta_V = [sqrt(3) * I_b * L * Z_effective] / 1000
        = [1.73205 * 132.02 A * 120.0 m * 0.3888 Ohm/km] / 1000
        = 10.67 Volts
% Delta_V = (10.67 V / 415 V) * 100% = 2.57%

STATUTORY COMPLIANCE CHECK:
Branch Feeder Limit: 3.00% | Calculated Drop: 2.57% | Margin: +0.43%
STATUS: [PASS — COMPLIANT WITH STATUTORY DESIGN LIMITS]
========================================================================================
```
