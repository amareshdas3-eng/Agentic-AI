# MCC & PCC Architect Pro — Panel Architecture & BOM Templates
### Switchboard Elevation Structure, Compartment Schedules, Control Registers & Preliminary BOM
**Framework:** ProEngineering Industrial Power Systems Suite  
**Standards:** IEC 61439-1/2 (Form 3b / Form 4b), IS 8623

---

## 1. Switchboard General Arrangement & Elevation Structure

A standard industrial low-voltage Motor Control Center (MCC) or Power Control Center (PCC) is organized into modular vertical sections:
- **Total Height:** $2200\text{ mm}$ (including $100\text{ mm}$ base channel).
- **Depth:** $1000\text{ mm}$ (PCC / Rear accessible) or $600\text{ mm}$ to $800\text{ mm}$ (Front accessible MCC).
- **Usable Module Height:** $1800\text{ mm}$ between horizontal busbar chamber (top) and cable chamber (bottom).
- **Column Structure:**
  - Section 01: Incomer 1 (Drawout ACB, $1000\text{ mm}$ width).
  - Section 02: Outgoing Motor Feeder Column A ($600\text{ mm}$ module + $300\text{ mm}$ cable alley).
  - Section 03: Outgoing Motor Feeder Column B ($600\text{ mm}$ module + $300\text{ mm}$ cable alley).
  - Section 04: Bus Coupler (Drawout ACB, $1000\text{ mm}$ width).
  - Section 05: Outgoing Motor Feeder Column C ($600\text{ mm}$ module + $300\text{ mm}$ cable alley).
  - Section 06: Outgoing Motor Feeder Column D ($600\text{ mm}$ module + $300\text{ mm}$ cable alley).
  - Section 07: Incomer 2 (Drawout ACB, $1000\text{ mm}$ width).

---

## 2. Compartment Stacking & Tier Schedule Template

```markdown
========================================================================================
PROENGINEERING.IN — SWITCHBOARD COMPARTMENT STACKING SCHEDULE
Panel Tag: 04-MCC-01 | Bus Section: A & B | Enclosure: IP54, Form 4b | Fault: 50kA 1s
========================================================================================

COLUMN 02: MOTOR FEEDERS (SECTION A) — WIDTH: 900mm (600mm Unit + 300mm Cable Alley)
+--------------------------------------------------------------------------------------+
| TIER | MODULE HT | FEEDER TAG     | LOAD DESCRIPTION           | KW   | STARTER TYPE |
+--------------------------------------------------------------------------------------+
| T1   | 250 mm    | MCC-01-FDR-01  | Treated Water Pump #1      | 5.5  | DOL          |
| T2   | 250 mm    | MCC-01-FDR-02  | Treated Water Pump #2 (S)  | 5.5  | DOL          |
| T3   | 350 mm    | MCC-01-FDR-03  | Chemical Agitator Motor #1 | 11.0 | Star-Delta   |
| T4   | 350 mm    | MCC-01-FDR-04  | Chemical Agitator Motor #2 | 11.0 | Star-Delta   |
| T5   | 300 mm    | MCC-01-FDR-05  | Dosing Pump Skid Feeder    | 3.7  | DOL          |
| T6   | 300 mm    | MCC-01-SPARE-1 | Equipped Spare Feeder      | 7.5  | DOL / SD     |
+--------------------------------------------------------------------------------------+
Total Functional Height: 1800 mm | Reserve Capacity: 1 Equipped Spare (16.7%)

COLUMN 03: HEAVY MOTOR FEEDERS (SECTION A) — WIDTH: 900mm
+--------------------------------------------------------------------------------------+
| TIER | MODULE HT | FEEDER TAG     | LOAD DESCRIPTION           | KW   | STARTER TYPE |
+--------------------------------------------------------------------------------------+
| T1   | 600 mm    | MCC-01-FDR-06  | Main Air Compressor Motor  | 45.0 | Soft Starter |
| T2   | 600 mm    | MCC-01-FDR-07  | Chilled Water Circ Pump 1  | 75.0 | Soft Starter |
| T3   | 600 mm    | MCC-01-SPARE-2 | Equipped Spare Feeder      | 45.0 | Soft Starter |
+--------------------------------------------------------------------------------------+
Total Functional Height: 1800 mm | Reserve Capacity: 1 Equipped Spare (33.3%)
========================================================================================
```

---

## 3. Control & Automation (PLC/DCS) Interface Register

```csv
Feeder Tag,Equipment Tag,Signal Description,Signal Type,Field Device,Wiring Type,Interlock Logic
MCC-01-FDR-01,PMP-TW-01,Run Indication Feedback,Digital Input (DI),Contactor Aux NO,2C x 1.5 mm²,Permissive to Process Flow
MCC-01-FDR-01,PMP-TW-01,Trip Indication Feedback,Digital Input (DI),MPCB Aux Fault,2C x 1.5 mm²,Alarm on DCS SCADA
MCC-01-FDR-01,PMP-TW-01,Local/Remote Selector,Digital Input (DI),LCS Selector Switch,2C x 1.5 mm²,Inhibits DCS Remote Start
MCC-01-FDR-01,PMP-TW-01,Emergency Stop Status,Digital Input (DI),Field E-Stop Mushroom,2C x 1.5 mm²,Hardwired Break to Contactor Coil
MCC-01-FDR-01,PMP-TW-01,Remote Start Command,Digital Output (DO),PLC Potential-Free Contact,2C x 1.5 mm²,Interlocked with Suction Level OK
MCC-01-FDR-01,PMP-TW-01,Remote Stop Command,Digital Output (DO),PLC Potential-Free Contact,2C x 1.5 mm²,Pulsed De-energize
MCC-01-FDR-07,PMP-CHW-01,Motor Current Output,Analog Input (AI),CT Transducer (4-20mA),2C x 1.5 mm² Shld,Overload Monitoring & Trend
```

---

## 4. Preliminary Bill of Materials (BOM) Excerpt

```markdown
========================================================================================
PROENGINEERING.IN — PRELIMINARY BILL OF MATERIALS (BOM)
Panel: 04-MCC-01 | Revision: 0 | Type: Form 4b Multi-Tier MCC
========================================================================================

1. ENCLOSURE & STRUCTURAL:
   - 06 Vertical Columns: 2200(H) x 900(W) x 800(D) mm, Sheet Steel 2.0mm CRCA, Powder Coated RAL 7035.
   - 01 Incomer Column: 2200(H) x 1000(W) x 1000(D) mm.
   - Internal Separation: Form 4b barriers and terminal shrouds.

2. BUSBAR SYSTEM:
   - Main Horizontal Busbar: 1600A, 50kA 1s, Electrolytic Copper (2 runs of 80 x 10 mm per phase).
   - Vertical Droppers: 400A to 800A Copper flats per column with heat-shrinkable sleeves.

3. SWITCHGEAR & CONTROLGEAR:
   - 02 Nos: 1600A 3P Drawout Air Circuit Breaker (ACB), 50kA, Microprocessor LSIG.
   - 01 No:  1600A 3P Drawout Bus Coupler ACB, 50kA, with Castell key interlock.
   - 08 Nos: Motor Protection Circuit Breakers (MPCB), 50kA, 1.6A to 25A.
   - 06 Nos: Molded Case Circuit Breakers (MCCB), 50kA, 50A to 250A with electronic releases.
   - 14 Nos: 3-Pole AC-3 Contactors, 9A to 150A with 230V AC coils.
   - 03 Nos: Electronic Soft Starters with built-in bypass contactor (45kW, 75kW).
   - 01 Lot: Control accessories (CTs, PTs, Multifunction Meters, Push buttons, Relays).
========================================================================================
```
