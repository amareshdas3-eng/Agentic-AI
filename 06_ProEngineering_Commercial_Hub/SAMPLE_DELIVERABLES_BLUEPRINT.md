# ProEngineering.in — Sample Deliverables Blueprint
### Client Submittal Standards, Lead Magnet Packaging & Sample Artifact Specs
**Target Use:** Free download lead magnets on ProEngineering.in to convert prospective clients into paying customers.

---

## 1. What Makes a Winning Engineering Lead Magnet?

Generic AI tools give users vague bullet points or paragraphs of hallucinated text. ProEngineering converts visitors by showing them **real, mathematically dense, visually stunning engineering deliverables** that look like they were produced by a top-tier global EPC consultancy (e.g., Bechtel, Larsen & Toubro, Jacobs, or Mott MacDonald).

Every sample deliverable packet includes:
1. **Title Block & Metadata:** Document Number, Project Name, Plant Area, Rev Number, Engineering Stage stamp.
2. **Mathematical Step-by-Step Proofs:** Every equation written in standard algebraic notation, followed by substituted variables with physical units, followed by the calculated result.
3. **Statutory Standards Citations:** Specific standard clauses (IEC 60364-5-52 Table B.52.4, IS 732 Clause 5.2, IEEE 141 Section 3.8).
4. **Pass/Fail Compliance Badges:** Clear visual indicators showing design margins.
5. **Human Approval Block:** Signature line for Prepared By, Checked By, and Approved By.

---

## 2. Sample Package 1: 33kV/11kV Substation Single Line Diagram (SVG/PDF Preview)

```
+-------------------------------------------------------------------------------------------------------------+
| PROENGINEERING.IN — ELECTRICAL ENGINEERING DIVISION                                                         |
| Drawing No: PE-E-SLD-001 | Rev: R0 | Date: 15-Oct-2026 | Scale: N.T.S. | System: 33kV/11kV Substation       |
+-------------------------------------------------------------------------------------------------------------+
|                                                                                                             |
|  [33kV GRID LINE 1]                                                     [33kV GRID LINE 2]                  |
|          |                                                                      |                           |
|      [LA 30kV]                                                              [LA 30kV]                       |
|          |                                                                      |                           |
|     [ISOLATOR]                                                             [ISOLATOR]                       |
|          |                                                                      |                           |
|   [VCB 1250A 25kA]                                                       [VCB 1250A 25kA]                   |
|          |                                                                      |                           |
|  +-------+-------------------------+                 +--------------------------+-------+                   |
|  | 33kV BUSBAR SECTION 1 (1250A)   |---[BUS COUPLER]---| 33kV BUSBAR SECTION 2 (1250A)    |                 |
|  +-------+-------------------------+    [VCB 1250A]  +--------------------------+-------+                   |
|          |                                                                      |                           |
|   [VCB 630A 25kA]                                                        [VCB 630A 25kA]                    |
|          |                                                                      |                           |
|   [TR-01: 5MVA 33/11kV]                                                  [TR-02: 5MVA 33/11kV]              |
|   Dyn11, ONAN, Z=7.5%                                                    Dyn11, ONAN, Z=7.5%                |
|          |                                                                      |                           |
|  +-------+-------------------------+                 +--------------------------+-------+                   |
|  | 11kV BUSBAR SECTION A (1250A)   |---[BUS COUPLER]---| 11kV BUSBAR SECTION B (1250A)    |                 |
|  +---+---+---+---+-----------------+    [VCB 1250A]  +--+---+---+---+-------------------+                   |
|      |   |   |   |                                      |   |   |   |                                       |
|     F1  F2  F3  SPARE                                  F4  F5  F6  SPARE                                    |
|                                                                                                             |
+-------------------------------------------------------------------------------------------------------------+
| STATUS: PRELIMINARY DESIGN — AUDITED BY PROENGINEERING DUAL-SOLVER GRAPH ENGINE                             |
| Prepared By: AI Agent (A2) | Checked By: IV&V Agent (A3) | Approved By: Amaresh (Lead PE)                   |
+-------------------------------------------------------------------------------------------------------------+
```

---

## 3. Sample Package 2: Comprehensive Feeder Voltage Drop Workbook Excerpt

```markdown
FEEDER TAG: MCC-01-FDR-12
LOAD: Raw Water Intake Vertical Turbine Pump Motor (110 kW, 415V, 3-Phase, 50Hz)
ROUTE LENGTH: 240.0 Meters | CABLE: 3C x 240 mm² Aluminium XLPE Insulated (Single Run)

1. DESIGN CURRENT COMPUTATION:
   Formula:   I_b = P_kW / (sqrt(3) * V_LL * cos(phi) * eta)
   Inputs:    P_kW = 110.0 kW, V_LL = 415 V, cos(phi) = 0.86, eta = 0.94
   Calculated:I_b = 110,000 / (1.73205 * 415 * 0.86 * 0.94) = 189.26 Amperes

2. CONVERTED CABLE PARAMETERS AT 90°C:
   Reference: IEC 60364-5-52 / IS 7098 Table 1
   R_20:      0.1250 Ohm/km
   R_90:      0.1250 * [1 + 0.00403 * (90 - 20)] = 0.1603 Ohm/km
   X_L:       0.0730 Ohm/km
   cos(phi):  0.8600 | sin(phi) = sqrt(1 - 0.86²) = 0.5103
   Z_eff:     (0.1603 * 0.8600) + (0.0730 * 0.5103) = 0.1378 + 0.0373 = 0.1751 Ohm/km

3. RUNNING VOLTAGE DROP COMPUTATION:
   Delta_V:   [sqrt(3) * 189.26 A * 240 m * 0.1751 Ohm/km] / 1000 = 13.78 Volts
   %Delta_V:  (13.78 V / 415 V) * 100% = 3.32%

4. STATUTORY LIMIT AUDIT:
   Statutory Limit: <= 3.00%
   Calculated Drop: 3.32%
   AUDIT STATUS:    [WARNING — LIMIT EXCEEDED BY 0.32%]
   RECOMMENDATION:  Upsize cable to 3C x 300 mm² Aluminium XLPE to reduce voltage drop to 2.71% (PASS).
```

---

## 4. Distribution Blueprint for Website Visitors

1. Offer this complete 18-page sample document as a free instant download in exchange for a business email and company name:
   `"Download the Complete Industrial Substation Design & Verification Sample Package (PDF)"`
2. Follow up automatically after 24 hours:
   `"Would you like us to run this same dual-solver verification audit on your current electrical project?"`
3. Convert high-intent leads into paid product users or consulting review clients.
