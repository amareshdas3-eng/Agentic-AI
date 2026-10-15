# Equipment Sizing Pro — Technical Datasheet & BOM Templates
### Procurement-Ready Engineering Specifications, Comparison Registers & Bill of Materials
**Framework:** ProEngineering Industrial Power Systems Suite

---

## 1. Distribution Transformer Technical Datasheet Template

```markdown
========================================================================================
PROENGINEERING.IN — TECHNICAL SPECIFICATION & DATASHEET: POWER TRANSFORMER
Document No: PE-DS-TR-001 | Revision: 0 | Project: [Project Name]
========================================================================================

1. GENERAL & SERVICE CONDITIONS:
   1.1 Item Tag:                   TR-01
   1.2 Quantity:                   1 Set
   1.3 Installation Location:      Indoor / Substation Transformer Bay
   1.4 Ambient Temperature:        Max: 45°C | Min: 5°C | Design Base: 40°C
   1.5 Altitude:                   < 1000 m above sea level
   1.6 Applicable Standard:        IEC 60076 / IS 2026

2. ELECTRICAL RATINGS:
   2.1 Rated Output (Continuous):  1600 kVA
   2.2 Type of Cooling:            ONAN (Oil Natural Air Natural)
   2.3 Number of Phases:           3-Phase, 50 Hz
   2.4 Nominal Voltage Ratio:      11,000 V / 433 V (No-load)
   2.5 Full Load Primary Current:  83.98 A
   2.6 Full Load Secondary Current:2133.28 A
   2.7 Vector Group:               Dyn11 (Delta High Voltage / Star Earthed Low Voltage)
   2.8 Percent Impedance (%Z):     6.25% at 75°C (Tolerance: ±10% per IEC)

3. TAP CHANGER:
   3.1 Type:                       Off-Circuit Tap Changer (OCTC)
   3.2 Range & Steps:              +5% to -5% in steps of 2.5% (5 Positions)

4. LOSS GUARANTEES & TEMPERATURE RISE:
   4.1 Maximum No-Load Loss (W):   1,850 W
   4.2 Maximum Load Loss at 75°C:  14,200 W
   4.3 Max Winding Temp Rise:      50°C (by resistance over ambient)
   4.4 Max Top Oil Temp Rise:      45°C (by thermometer over ambient)

5. ACCESSORIES & PROTECTION:
   5.1 Buchholz Relay:             Double float with Alarm & Trip contacts
   5.2 Temperature Indicators:     OTI (Oil Temp Indicator) & WTI (Winding Temp Indicator)
   5.3 Pressure Relief Device:     Spring-loaded PRD with trip microswitch
   5.4 Marshalling Box:            IP55 Stainless Steel with terminal strips
========================================================================================
```

---

## 2. Low-Voltage Air Circuit Breaker (ACB) Datasheet Template

```markdown
========================================================================================
PROENGINEERING.IN — TECHNICAL SPECIFICATION & DATASHEET: LOW VOLTAGE ACB
Document No: PE-DS-CB-001 | Revision: 0 | Project: [Project Name]
========================================================================================

1. GENERAL IDENTIFICATION:
   1.1 Equipment Tag:              04-PCC-INC-01 (Main Incomer 1)
   1.2 Duty:                       Main Transformer Incomer Circuit Breaker
   1.3 Standard:                   IEC 60947-2 / IS 13947-2

2. RATINGS & CHARACTERISTICS:
   2.1 Frame Rating (In):          2500 A Frame
   2.2 Rated Continuous Current:   2500 A (Adjustable sensor rated at 2150 A)
   2.3 Number of Poles:            3-Pole / 4-Pole (as specified)
   2.4 Construction:               Drawout Type with Cradle & Position Indicators
   2.5 Rated Operating Voltage:    415 V AC (50 Hz)
   2.6 Rated Insulation Voltage:   1000 V AC
   2.7 Rated Impulse Withstand:    12 kV (Uimp)

3. BREAKING CAPACITY & SHORT CIRCUIT WITHSTAND:
   3.1 Ultimate Breaking (Icu):    50 kA RMS at 415V
   3.2 Service Breaking (Ics):     50 kA RMS (100% of Icu)
   3.3 Short-Time Withstand (Icw): 50 kA RMS for 1.0 Second (Category B Selective)

4. TRIP UNIT & PROTECTION FUNCTIONS:
   4.1 Trip Unit Type:             Microprocessor-based Electronic LSIG Release
   4.2 Long-Time (Overload) Ir:    0.4 to 1.0 x In (Time delay tr = 3s to 30s)
   4.3 Short-Time (Selective) Isd: 1.5 to 10 x Ir (Time delay tsd = 0.1s to 0.4s)
   4.4 Instantaneous (Fault) Ii:   2 to 15 x In (Instantaneous <= 40 ms)
   4.5 Ground Fault (Earth) Ig:    0.2 to 1.0 x In (Time delay tg = 0.1s to 0.4s)
========================================================================================
```

---

## 3. Preliminary Bill of Materials (BOM) Export Format

```csv
Item No,Equipment Tag,Category,Description,Primary Rating,Secondary Rating,Breaking Capacity,Quantity,Unit,Datasheet Ref
01,TR-01,Transformer,"Oil-Cooled Distribution Transformer",11kV,433V,Z=6.25%,1,SET,PE-DS-TR-001
02,TR-02,Transformer,"Oil-Cooled Distribution Transformer",11kV,433V,Z=6.25%,1,SET,PE-DS-TR-001
03,04-PCC-INC-01,Circuit Breaker,"Drawout Air Circuit Breaker (ACB)",2500A,415V,50kA (1s),1,NO,PE-DS-CB-001
04,04-PCC-INC-02,Circuit Breaker,"Drawout Air Circuit Breaker (ACB)",2500A,415V,50kA (1s),1,NO,PE-DS-CB-001
05,04-PCC-BC-01,Circuit Breaker,"Drawout Air Circuit Breaker (ACB)",2500A,415V,50kA (1s),1,NO,PE-DS-CB-001
06,CBL-TR1-PCC,Power Cable,"1C x 630 mm² XLPE Aluminium (3R/Ph)",600/1000V,3 Runs/Ph,Fault = 50kA,540,MTR,PE-DS-CBL-001
07,BB-PCC-415,Busbar Assembly,"Electrolytic High-Conductivity Copper",3200A,415V,50kA (1s),1,LOT,PE-DS-BB-001
```
