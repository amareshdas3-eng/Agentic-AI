# Product 03: Equipment Sizing Pro — Specification (Statutory Edition)
### Industrial Transformers, Cables, Switchgear & Busbar Sizing Engine
**Product Family:** ProEngineering Industrial Power Systems Suite  
**Version:** 1.0.0 (World-Class Statutory Release Candidate)  
**Governing Codes:** IEC 60076, IEC 60364-5-52/54, IEC 60909, IEC 60947-2, IEC 60865-1, IS 2026, IS 732, CEA Safety Regs 2023 Reg 44

---

## 1. Product Scope & Functional Architecture

`Equipment Sizing Pro` is a modular, deterministic electrical engineering calculation engine that sizes, audits, and generates procurement-ready technical specifications for major industrial electrical plant equipment. Every derivation is anchored to published statutory standards.

### 1.1 Power & Distribution Transformer Sizing Module
- **Statutory Authority:** IEC 60076-1:2011, IEC 60076-2 (Temperature Rise), IEC 60076-5 (Short-Circuit Ability), IS 2026, IEEE C57.12.00, CEA Safety Regulations 2023 Reg 44.
- **Deterministic Derivation:**
  1. Calculates aggregate diversified peak plant load ($S_{demand}$) incorporating continuous, intermittent ($50\%$), and future growth margins ($\alpha_{growth} = 15\% - 25\%$).
  2. Applies altitude derating ($k_{alt}$) for installations $> 1000\text{m}$ ($0.4\%$ capacity reduction per $100\text{m}$ over $1000\text{m}$ per IEC 60076-2 Clause 4.2).
  3. Applies ambient temperature derating ($k_{temp}$) for $T_{amb} > 40^\circ\text{C}$ ($1.0\%$ reduction per $^\circ\text{C}$ over $40^\circ\text{C}$).
  4. Maps calculated kVA to standard commercial ratings per IEC 60076 Table 1:
     `[100, 160, 200, 250, 315, 400, 500, 630, 800, 1000, 1250, 1600, 2000, 2500, 3150, 4000, 5000, 6300, 8000, 10000 kVA]`.
  5. Computes rated secondary current and prospective bolted terminal short-circuit current:
     $$I_{rated\_sec} = \frac{S_{std\_kVA} \times 1000}{\sqrt{3} \cdot V_{LL\_sec}}$$
     $$I_{sc\_sec} = \frac{I_{rated\_sec}}{Z_{pu}} = \frac{I_{rated\_sec} \times 100}{Z_{\%}}$$
  6. Enforces standard impedance limits per IEC 60076-5 Table 1.

---

### 1.2 Power Cable Sizing Module (The 4-Fold Statutory Pipeline)
- **Statutory Authority:** IEC 60364-5-52:2019, IEC 60364-5-54:2011 Clause 543.1.2, IS 732:2019 Clause 5.2/5.4, BS 7671 Regulations 433 & 434, NEC 2023 Article 310.

A cable is verified if and only if **all four independent tests pass simultaneously**:

1. **Continuous Thermal Current (Ampacity) Test:**
   $$I_z = I_{base} \cdot \left( k_1 \cdot k_2 \cdot k_3 \cdot k_4 \cdot k_h \right) \ge \frac{I_b}{N_{runs}}$$
   *(where $k_1$ is ambient air temp derating, $k_2$ is grouping derating, $k_3$ is soil resistivity, $k_4$ is depth, $k_h$ is triplen harmonic derating per Table E.52.1).*
2. **Maximum Permissible Steady-State Voltage Drop:**
   $$\% \Delta V_{run} = \frac{\sqrt{3} \cdot I_b \cdot L \cdot (R_{AC\theta} \cos\varphi + X_L \sin\varphi)}{10 \cdot V_{LL} \cdot N_{runs}} \le 3.0\% \quad (\text{Branch Feeder})$$
3. **Motor Starting Transient Voltage Dip:**
   $$\% \Delta V_{start} = \frac{\sqrt{3} \cdot I_{start} \cdot L \cdot (R_{AC\theta} \cos\varphi_{LR} + X_L \sin\varphi_{LR})}{10 \cdot V_{LL} \cdot N_{runs}} \le 15.0\% \quad (\text{IEEE 141})$$
4. **Adiabatic Short-Circuit Thermal Withstand:**
   $$S_{actual} \ge S_{min} = \frac{I_{sc\_RMS} \cdot \sqrt{t}}{k}$$
   - **Copper / XLPE:** $k = 143$ ($\theta_i = 90^\circ\text{C}, \theta_f = 250^\circ\text{C}$).
   - **Aluminium / XLPE:** $k = 94$ ($\theta_i = 90^\circ\text{C}, \theta_f = 250^\circ\text{C}$).
   - **Copper / PVC:** $k = 115$ ($\theta_i = 70^\circ\text{C}, \theta_f = 160^\circ\text{C}$).
   - **Aluminium / PVC:** $k = 76$ ($\theta_i = 70^\circ\text{C}, \theta_f = 160^\circ\text{C}$).

---

### 1.3 Circuit Breaker & Switchgear Selection Module
- **Statutory Authority:** IEC 60947-2:2016, CEA Safety Regulations 2023 Regulation 44.
- Evaluates:
  1. Rated Continuous Current: $I_n \ge I_b$.
  2. Rated Ultimate Breaking Capacity: $I_{cu} \ge I_{sc\_prospective}$.
  3. Rated Service Breaking Capacity: $I_{cs} \ge 100\% \cdot I_{cu}$ for continuous process facilities.
  4. Rated Short-Time Withstand ($I_{cw}$ for $1.0\text{s}$ or $3.0\text{s}$): Required for Category B selective breakers.
  5. Inrush Ride-Through: Instantaneous trip setting $I_i$ coordinates above transformer inrush ($10 - 12 \times I_{rated}$ for $100\text{ms}$).

---

### 1.4 Switchboard Busbar Module
- **Statutory Authority:** IEC 60865-1:2011 & IEC 61439-1:2020 Clause 8.6.
- Evaluates:
  1. Continuous thermal ampacity: Current density $J \le 1.20 - 1.50\text{ A/mm}^2$ for Copper, $J \le 0.80 - 1.00\text{ A/mm}^2$ for Aluminium.
  2. Peak electrodynamic repulsive force:
     $$F_{peak} = 0.173 \cdot (i_p)^2 \cdot \frac{l_{span}}{a_{spacing}} \quad [\text{Newtons}]$$
  3. Insulator support bending moment safety factor $\ge 1.5$.
