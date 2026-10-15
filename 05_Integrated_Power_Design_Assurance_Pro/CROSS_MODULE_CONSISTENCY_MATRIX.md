# Integrated Power Design Assurance Pro — Cross-Module Consistency Matrix (Statutory Edition)
### 40 Deterministic Cross-Document Rules, Statutory Assertions & Severity Classifications
**Framework:** ProEngineering Industrial Power Systems Suite  
**Statutory Basis:** IEC 60364, IEC 60909, IEC 61439, IEC 60076, IEEE 141, IEEE 80, IEEE 1584, NFPA 70E, IS 732, IS 3043, CEA Safety Regs 2023

---

## 1. Complete 40-Rule Statutory Cross-Disciplinary Consistency Matrix

| Rule ID | Checked Electrical Parameter | Source Document A | Source Document B | Statutory Assertion / Physical Formula | Governing Statutory Standard | Severity |
|---|---|---|---|---|---|---|
| **R-01** | Transformer Continuous Rating | SLD Drawing Symbol | Load Schedule & Sizing | $S_{SLD} = S_{Sizing} \ge S_{Peak\_Demand}$ | IEC 60076-1 / IS 2026 | **MAJOR** |
| **R-02** | Transformer Impedance (%Z) | Sizing Sheet & Datasheet | Downstream Switchgear $I_{cu}$ | $I_{cu} \ge \frac{S_{std}}{\sqrt{3} \cdot V_{sec} \cdot (Z\% / 100)}$ | IEC 60076-5 / IEC 60909 | **CRITICAL** |
| **R-03** | Transformer Voltage Ratio | SLD Diagram | Connected Bus Schedule | $V_{sec\_SLD} = V_{bus\_nominal}$ | IEC 61936-1 Cl. 4.2 | **CRITICAL** |
| **R-04** | Feeder Cable Size | Cable Schedule | Voltage Drop Workbook | $\text{Size}_{Schedule} = \text{Size}_{Calc}$ | IEC 60364-5-52 Cl. 525 | **CRITICAL** |
| **R-05** | Cable Route Length | Cable Schedule | Voltage Drop Workbook | $|L_{Schedule} - L_{Calc}| / L_{Calc} \le 5.0\%$ | IS 732:2019 Cl. 5.2 | **MAJOR** |
| **R-06** | Feeder Full Load Current | Voltage Drop Workbook | MCC Feeder Schedule | $|I_{b\_Calc} - I_{b\_MCC}| \le 0.5\text{ A}$ | IEC 60034-1 / IS 12615 | **MAJOR** |
| **R-07** | Motor Shaft Power (kW) | Mechanical Load List | Electrical Load Schedule | $P_{kW\_Mech} = P_{kW\_Elec}$ | ISO 9001 QA Protocol | **MAJOR** |
| **R-08** | Starter Technology Alignment | SLD Feeder Symbol | MCC Feeder Schedule | $\text{Type}_{SLD} = \text{Type}_{MCC}$ (e.g. VFD vs DOL) | IEC 60947-4-1 | **MAJOR** |
| **R-09** | Cable Thermal Protection | Cable Sizing ($I_z$) | Breaker Trip Setting ($I_r$) | $I_r \le I_z = I_{base} \cdot k_{total}$ | IEC 60364-4-43 Cl. 433.1 | **CRITICAL** |
| **R-10** | Cable Fault Thermal Withstand | Cable Sizing ($S_{actual}$) | Bus Fault Level ($I_{sc}$) | $S_{actual} \ge \frac{I_{sc} \cdot \sqrt{t}}{k}$ | IEC 60364-5-54 Cl. 543.1.2 | **CRITICAL** |
| **R-11** | Breaker Breaking Capacity | Switchgear Schedule ($I_{cu}$) | Bus Prospective Fault ($I_{sc}$) | $I_{cu} \ge I_{sc}$ | IEC 60947-2 Cl. 4.3.5 | **CRITICAL** |
| **R-12** | Busbar Continuous Ampacity | Switchboard Sizing ($I_{bus}$) | Incomer Breaker Trip ($I_{inc}$) | $I_{bus} \ge I_{inc}$ | IEC 61439-1 Cl. 8.6 | **MAJOR** |
| **R-13** | Bus Coupler Ampacity | Switchboard Sizing ($I_{cpl}$) | Incomer Breaker ($I_{inc}$) | $I_{cpl} \ge \min(I_{inc1}, I_{inc2})$ | IS 10118 (Part 3) | **MAJOR** |
| **R-14** | Bus Coupler 2-out-of-3 Interlock | SLD Control Narrative | Switchboard Specification | Castell Interlock Verified | CEA Reg 2023 Reg 44(3) | **CRITICAL** |
| **R-15** | Contactor AC-3 Rating | MCC Component Schedule | Motor Full Load Current ($I_{fl}$) | $I_{contactor\_AC3} \ge I_{fl}$ | IEC 60947-4-1 Table 1 | **MAJOR** |
| **R-16** | Overload Relay Setting Range | MCC Component Schedule | Motor Full Load Current ($I_{fl}$) | $I_{fl} \in [I_{relay\_min}, I_{relay\_max}]$ | IEC 60947-4-1 Cl. 8.2 | **MODERATE** |
| **R-17** | Motor Starting Voltage Dip | Voltage Drop Workbook | Statutory Limits ($\le 15.0\%$) | $\Delta V_{start} \le 15.0\%$ | IEEE 141 Section 3.8 | **MAJOR** |
| **R-18** | Running Feeder Voltage Drop | Voltage Drop Workbook | Statutory Limits ($\le 3.0\%$) | $\Delta V_{run} \le 3.0\%$ | IEC 60364-5-52 Cl. 525 | **MAJOR** |
| **R-19** | Spare Feeder Provision | MCC Line-Up Schedule | Project Design Basis | $\text{Spare Modules \%} \ge 20.0\%$ | Industrial Best Practice | **MODERATE** |
| **R-20** | Global Tag Uniqueness | All Project Documents | Canonical Data Store | Count of each Tag $= 1$ (Unique) | IEC 81346 Hierarchy | **CRITICAL** |
| **R-21** | Ambient Temperature Baseline | Transformer Datasheet | Cable Sizing Schedule | $T_{amb\_TR} = T_{amb\_Cable} = T_{amb\_Basis}$ | IEC 60364-5-52 Tab B.52.14 | **MODERATE** |
| **R-22** | Neutral Earthing & Pole Count | SLD Earthing Philosophy | Breaker Poles (3P vs 4P) | TN-S requires switched neutral 4P | IEC 60364-4-41 Cl. 411.3 | **MAJOR** |
| **R-23** | CT Primary Current vs Breaker | SLD Instrument Schedule | Breaker Frame Rating ($I_n$) | $I_{CT\_primary} \ge I_n$ | IEC 61869-2 Cl. 5.2 | **MODERATE** |
| **R-24** | Surge Arrester on HV Line | SLD Incomer Bay | Utility Interface Standards | Gapless ZnO Arrester on Line | IEC 60099-4 / CEA Reg 43 | **MAJOR** |
| **R-25** | Document Revision Sync | Downstream Schedules | Master SLD Drawing | $\text{Rev}_{Schedule} \ge \text{Rev}_{SLD}$ | ISO 9001 QA Protocol | **MODERATE** |
| **R-26** | Arc Flash Incident Energy | Switchgear Schedule | NFPA 70E Safety Limit | $E_{incident} \le 40\text{ cal/cm}^2$ (Max PPE) | IEEE 1584:2018 / NFPA 70E | **CRITICAL** |
| **R-27** | Substation Earth Resistance | Substation Calculation | Statutory Maximum Limit | $R_{ground} \le 1.0\text{ }\Omega$ ($0.5\Omega$ for HV) | IS 3043:2018 / CEA Reg 35 | **CRITICAL** |
| **R-28** | Touch Potential Compliance | Earth Mat Calculation | Tolerable Touch Voltage ($E_{touch}$) | $E_{touch\_actual} \le E_{touch\_tolerable}$ | IEEE Std 80:2013 Cl. 8.3 | **CRITICAL** |
| **R-29** | Step Potential Compliance | Earth Mat Calculation | Tolerable Step Voltage ($E_{step}$) | $E_{step\_actual} \le E_{step\_tolerable}$ | IEEE Std 80:2013 Cl. 8.3 | **CRITICAL** |
| **R-30** | Harmonic Neutral Sizing | Non-Linear Load Schedule | Cable Sizing Module | If 3rd Harm $>33\% \implies S_N \ge S_{ph}$ | IEC 60364-5-52 Annex E | **CRITICAL** |
| **R-31** | Switchgear Air Clearances | Switchboard Fabrication | Statutory Minimum Clearance | Phase-Phase $\ge 14\text{mm}$ ($U_{imp}=8\text{kV}$) | IEC 61439-1 Table 1 | **CRITICAL** |
| **R-32** | Switchgear Creepage Distance | Switchboard Fabrication | Statutory Minimum Creepage | Creepage $\ge 20\text{mm}$ ($U_i=1000\text{V}$) | IEC 61439-1 Table 2 | **CRITICAL** |
| **R-33** | Transformer Inrush Clearance | Breaker Instantaneous ($I_i$) | Transformer Rated Inrush | $I_i \ge 10 - 12 \times I_{rated\_TR}$ for $0.1\text{s}$ | IEEE C57.12.00 / IEEE 242 | **MAJOR** |
| **R-34** | CT Knee-Point Voltage ($V_k$) | Protection Relay Spec | Cable & CT Loop Resistance | $V_k \ge 20 \cdot I_n \cdot (R_{ct} + 2R_L + R_b)$ | IEC 61869-2 Cl. 6.13 | **CRITICAL** |
| **R-35** | Relay Coordination Margin | Upstream Protection Curve | Downstream Protection Curve | $\Delta t \ge 0.20\text{s}$ (Num) / $0.30\text{s}$ (EM) | IEEE Std 242 (Buff Book) | **MAJOR** |
| **R-36** | Disconnector Earth Interlock | Substation SLD Schedule | Switchyard Controls | Mech Interlock: ES Closed $\iff$ DS Open | IEC 62271-102 Cl. 5.104 | **CRITICAL** |
| **R-37** | Motor Protection Coordination | MCC Feeder Schedule | Starter Component Assembly | Verified Type 2 Coordination | IEC 60947-4-1 Cl. 8.2.5 | **MAJOR** |
| **R-38** | Internal Arc Segregation | Switchboard Specification | Operating Environment | Form 3b or Form 4b Mandatory | IEC 61439-2 Cl. 8.101 | **MAJOR** |
| **R-39** | Neutral Busbar Ampacity | Switchboard Busbar Calc | Neutral Harmonic Loading | If Harm $>15\% \implies I_{neutral} = 100\% I_{ph}$ | IEC 61439-1 Cl. 8.6.1 | **MAJOR** |
| **R-40** | Cable Bending Radius Check | Cable Trench / Tray Layout | Cable Outer Diameter ($D$) | Bend Radius $\ge 12 \times D$ (Armored) | IS 1255 / IEC 60502-1 | **MODERATE** |
