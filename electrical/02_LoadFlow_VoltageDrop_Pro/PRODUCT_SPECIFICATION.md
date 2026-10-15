# Product 02: LoadFlow & VoltageDrop Pro — Specification
### Industrial Load Schedules, Balanced Radial Power Flow & Cable Voltage Drop
**Product Family:** ProEngineering Industrial Power Systems Suite  
**Version:** 1.0.0 (Core Engine Spec)  
**Priority:** #1 Flagship Commercial Launch Product

---

## 1. Executive Product Overview

`LoadFlow & VoltageDrop Pro` is a deterministic calculation engine and professional reporting platform for industrial electrical engineers. It eliminates the rampant formula errors, inconsistent power factor handling, and unverified temperature assumptions found in ad-hoc Excel spreadsheets.

The product calculates:
1. **Connected vs. Operating vs. Peak Demand Power:**
   - Active Power ($P$, kW), Reactive Power ($Q$, kvar), and Apparent Power ($S$, kVA).
   - Accurate application of Demand Factors ($DF$) and Diversity Factors ($DivF$).
2. **Deterministic Feeder Full-Load and Design Currents ($I_b$):**
   - Three-phase balanced circuits ($V_{LL} = 415\text{V}, 6.6\text{kV}, 11\text{kV}, 33\text{kV}$).
   - Single-phase phase-to-neutral ($V_{LN} = 230\text{V}, 240\text{V}, 120\text{V}$) and phase-to-phase circuits.
3. **True Impedance Cable Voltage Drop:**
   - Incorporates AC conductor resistance adjusted for maximum operating temperature ($70^\circ\text{C}$ for PVC, $90^\circ\text{C}$ for XLPE).
   - Incorporates inductive reactance ($X_L$ in $\Omega/\text{km}$) based on cable core formation (trefoil vs. flat spaced).
   - Real and imaginary components of load current: $I_{active} = I \cos\varphi$, $I_{reactive} = I \sin\varphi$.
4. **Motor Starting Voltage Dip:**
   - High inrush current ($I_{start} = 5.5$ to $7.0 \times I_{FLC}$ at low power factor $\cos\varphi \approx 0.25$–$0.35$).
   - Flags if terminal voltage drops below $85\%$ ($15\%$ dip limit per IEC 60034-1 / IEEE 141).

---

## 2. In-Scope Capabilities vs. Model Limitations

### In-Scope:
- Radial distribution networks: Single-source and dual-source (split bus).
- Full load schedule aggregation with continuous, intermittent ($50\%$ duty), and standby ($0\%$ simultaneous) load logic.
- Copper and Aluminium conductors (single-core and multi-core).
- Cable insulation types: XLPE ($90^\circ\text{C}$ max continuous conductor temperature) and PVC ($70^\circ\text{C}$).
- Statutory compliance limit monitoring:
  - Branch Feeder limit: $\le 3.0\%$ (IS 732, NEC 210.19).
  - Overall Main Substation to Final Utilization Load: $\le 5.0\%$ (IEC 60364-5-52).
  - Motor starting transient dip: $\le 15.0\%$ (IEEE 141).

### Explicit Exclusions (Logged in Assumptions Register):
- Meshed, multi-loop transmission load flow requiring Newton-Raphson / Fast Decoupled iteration (future v2.0 roadmap).
- Harmonic distortion and non-linear power factor degradation (IEEE 519 studies).
- Asymmetrical sequence component unbalance in severely unbalanced single-phase loads.

---

## 3. Data Intake Requirements

| Field Name | Type | Mandatory? | Allowed Range / Units | Engineering Description |
|---|---|---|---|---|
| `nominalVoltageV` | Number | Yes | $110\text{V} - 33,000\text{V}$ | Line-to-line RMS system voltage |
| `frequencyHz` | Number | Yes | 50 or 60 Hz | System electrical frequency |
| `feederTag` | String | Yes | Alphanumeric (Unique) | e.g., `MCC-1-FDR-01` |
| `loadDescription` | String | Yes | Text | e.g., `Chilled Water Pump Motor 1` |
| `ratedPowerKw` | Number | Yes | $> 0.1\text{ kW}$ | Shaft output or rated input power |
| `powerFactor` | Number | Yes | $0.50 - 1.00$ (Lagging) | Operating power factor |
| `efficiency` | Number | Yes | $0.70 - 0.99$ | Motor or equipment efficiency |
| `operatingDuty` | Enum | Yes | `CONTINUOUS`, `INTERMITTENT`, `STANDBY` | Operating status |
| `demandFactor` | Number | Yes | $0.10 - 1.00$ | Ratio of maximum demand to rated |
| `cableLengthM` | Number | Yes | $1 - 5,000\text{ m}$ | One-way route length |
| `conductorMaterial` | Enum | Yes | `COPPER`, `ALUMINIUM` | Conductor metallurgy |
| `insulationType` | Enum | Yes | `XLPE`, `PVC` | Maximum operating temperature base |
| `sizeMm2` | Number | Yes | Standard mm² sizes | Conductor cross-sectional area |
| `runsInParallel` | Integer | Yes | $1 - 6$ | Number of parallel cable runs per phase |
