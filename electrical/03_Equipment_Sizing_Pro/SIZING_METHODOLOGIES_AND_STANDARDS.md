# Equipment Sizing Pro — Sizing Methodologies & Standards Basis (Statutory Edition)
### Mathematical Derivations, Adiabatic Fault Physics & Equipment Specification Codes
**Framework:** ProEngineering Industrial Power Systems Suite  
**Statutory Basis:** IEC 60076-1/5, IEC 60364-5-52/54, IEC 60947-2, IEC 60865-1, IS 2026, IS 13947, CEA Safety Regs 2023 Reg 44

---

## 1. Power & Distribution Transformer Sizing Derivations

### 1.1 Capacity Derivation with Environmental & Growth Deratings
- **Statutory Authority:** IEC 60076-1:2011 Clause 4 & IS 2026 (Part 1):2011 Clause 4.
- **Aggregate Diversified Load Equation:**
  $$S_{demand\_kVA} = \left[ \sum_{i=1}^{N_{cont}} \frac{P_{kW\_i}}{\cos\varphi_i \cdot \eta_i} \cdot DF_i + 0.50 \sum_{j=1}^{N_{int}} \frac{P_{kW\_j}}{\cos\varphi_j \cdot \eta_j} \cdot DF_j \right] \times DivF$$
  *(where $DF$ is demand factor, $DivF$ is diversity factor, standby loads are excluded under normal operation).*

#### Altitude Derating Factor ($k_{alt}$) per IEC 60076-2 Clause 4.2:
For installation at an altitude $H > 1000\text{ meters}$ above sea level:
- For naturally cooled (ONAN) oil transformers:
  $$k_{alt} = 1.0 - \left( \frac{H - 1000}{100} \right) \times 0.004$$
- For dry-type transformers (AN):
  $$k_{alt} = 1.0 - \left( \frac{H - 1000}{100} \right) \times 0.005$$

#### Ambient Temperature Derating Factor ($k_{temp}$):
Base rating is standardized at annual average $30^\circ\text{C}$ and peak $40^\circ\text{C}$ ambient air temperature. For maximum ambient temperature $T_{amb} > 40^\circ\text{C}$:
$$k_{temp} = 1.0 - (T_{amb} - 40) \times 0.01$$

#### Minimum Required Transformer Capacity ($S_{min}$):
$$S_{calc} = \frac{S_{demand\_kVA} \times (1 + \alpha_{growth})}{k_{alt} \cdot k_{temp}}$$
The engine maps $S_{calc}$ to the nearest standard commercial rating $S_{std}$ per IEC 60076-1 Table 1.

---

### 1.2 Transformer Short-Circuit Impedance & Prospective Fault Level
- **Statutory Authority:** IEC 60076-5:2006 (Ability to withstand short circuit) & IEC 60909-0:2016.
- The standard impedance voltage $u_k$ ($Z\%$) is evaluated at rated frequency and reference temperature ($75^\circ\text{C}$):
  $$Z_{base} = \frac{V_{LL\_sec}^2}{S_{std\_MVA}} \quad [\Omega]$$
  $$R_{TR} = \frac{P_{load\_loss\_kW} \times 1000}{3 \cdot (I_{rated\_sec})^2} \quad [\Omega]$$
  $$Z_{TR} = \frac{Z\%}{100} \cdot Z_{base} \quad [\Omega]$$
  $$X_{TR} = \sqrt{Z_{TR}^2 - R_{TR}^2} \quad [\Omega]$$

#### Bolted Three-Phase Symmetrical Short-Circuit Current ($I_{sc\_sec}$):
Neglecting infinite grid upstream impedance:
$$I_{sc\_sec} = \frac{I_{rated\_sec}}{Z_{pu}} = \frac{S_{std\_kVA} \times 1000}{\sqrt{3} \cdot V_{LL\_sec} \cdot (Z\% / 100)} \quad [\text{Amperes}]$$

#### Standard Impedance Limits per IEC 60076-5 Table 1:
- $S \le 630\text{ kVA}$: $Z = 4.0\%$ to $4.5\%$ (Tolerance: $\pm 10\%$).
- $631\text{ kVA} \le S \le 1250\text{ kVA}$: $Z = 5.0\%$ (Tolerance: $\pm 10\%$).
- $1251\text{ kVA} \le S \le 2500\text{ kVA}$: $Z = 6.25\%$ (Tolerance: $\pm 7.5\%$).
- $2501\text{ kVA} \le S \le 6300\text{ kVA}$: $Z = 7.15\%$ (Tolerance: $\pm 7.5\%$).
- $6301\text{ kVA} \le S \le 25,000\text{ kVA}$: $Z = 8.0\% - 10.0\%$.

---

## 2. Power Cable Sizing — The 4-Fold Statutory Verification Pipeline

- **Statutory Authority:** IEC 60364-5-52:2019 (Selection and erection of wiring systems), IEC 60364-5-54:2011 Clause 543.1.2 (Adiabatic thermal short-circuit withstand), IS 732:2019 Clause 5.2, BS 7671 Regulations 433 & 434, NEC 2023 Article 310.

A cable is legally verified if and only if **all four tests pass simultaneously**:

```
[Candidate Cable: Conductor Material, Insulation, Size (mm²), Parallel Runs]
                                 │
                 ┌───────────────┴───────────────┐
                 ▼                               ▼
    [TEST 1: CONTINUOUS AMPACITY]    [TEST 2: RUNNING VOLTAGE DROP]
    I_z = I_base · k_total >= I_b    %ΔV_run <= 3.0% (Branch Feeder)
                 │                               │
                 └───────────────┬───────────────┘
                                 │
                 ┌───────────────┴───────────────┐
                 ▼                               ▼
    [TEST 3: MOTOR STARTING DIP]     [TEST 4: ADIABATIC FAULT WITHSTAND]
    %ΔV_start <= 15.0%               S_actual >= (I_sc · √t) / k
                 │                               │
                 └───────────────┬───────────────┘
                                 ▼
                     [STATUTORY CABLE APPROVAL]
```

### Check 1: Continuous Ampacity with Environmental Deratings
$$I_z = I_{base} \cdot \left( k_1 \cdot k_2 \cdot k_3 \cdot k_4 \cdot k_h \right) \ge \frac{I_b}{N_{runs}}$$
Where:
- $k_1$: Ambient air temperature correction factor (IEC 60364-5-52 Table B.52.14).
  - For XLPE ($90^\circ\text{C}$ base $30^\circ\text{C}$): At $45^\circ\text{C}$, $k_1 = \sqrt{\frac{90 - 45}{90 - 30}} = \sqrt{\frac{45}{60}} = 0.866$.
- $k_2$: Cable grouping factor for multiple touching circuits on perforated cable tray (Table B.52.17). (e.g., 3 circuits = $0.82$, 6 circuits = $0.73$).
- $k_3$: Ground thermal resistivity factor for direct-buried runs (Table B.52.16).
- $k_4$: Burial depth factor (Table B.52.18).
- $k_h$: Harmonic neutral current derating factor per Table E.52.1 ($0.86$ if triplen harmonics $> 15\%$).

### Check 2 & 3: Voltage Drop Constraints
$$\% \Delta V_{run} \le 3.0\% \quad \text{and} \quad \% \Delta V_{start} \le 15.0\%$$

### Check 4: Adiabatic Short-Circuit Thermal Withstand
- **Formula:**
  $$S_{min} = \frac{I_{sc\_RMS} \cdot \sqrt{t_{clearing}}}{k}$$
- **Statutory Limits on Final Temperature ($\theta_f$):**
  - Cross-linked Polyethylene (XLPE): Initial $\theta_i = 90^\circ\text{C}$, Final $\theta_f = 250^\circ\text{C}$.
  - Polyvinyl Chloride (PVC): Initial $\theta_i = 70^\circ\text{C}$, Final $\theta_f = 160^\circ\text{C}$ (for $S \le 300\text{ mm}^2$), $140^\circ\text{C}$ (for $S > 300\text{ mm}^2$).
- **Statutory $k$ Factors:**
  - Copper / XLPE: **$k = 143$**
  - Aluminium / XLPE: **$k = 94$**
  - Copper / PVC: **$k = 115$**
  - Aluminium / PVC: **$k = 76$**

---

## 3. Circuit Breaker Selection & Discrimination Derivations

- **Statutory Authority:** IEC 60947-2:2016 (Low-voltage circuit breakers) & CEA Safety Regulations 2023 Regulation 44.

### 3.1 Four-Point Circuit Breaker Verification Equations:
1. **Continuous Current Rating ($I_n$):**
   $$I_n \ge I_b$$
2. **Rated Ultimate Short-Circuit Breaking Capacity ($I_{cu}$):**
   $$I_{cu} \ge I_{sc\_prospective}$$
   *(where breaker must clear short circuit twice under standard test sequence $O - t - CO$, and can suffer performance degradation).*
3. **Rated Service Short-Circuit Breaking Capacity ($I_{cs}$):**
   $$I_{cs} \ge \gamma \cdot I_{cu}$$
   - Industrial standard for critical continuous processes: $\gamma = 1.0$ ($I_{cs} = 100\% \cdot I_{cu}$).
   - Standard commercial requirement: $\gamma \ge 0.50$ to $0.75$.
   *(After clearing fault at $I_{cs}$, the breaker remains fully operational without loss of continuous current rating).*
4. **Short-Time Withstand Current ($I_{cw}$) & Utilization Category:**
   - **Category A:** Instantaneous trip without intentional time delay (e.g., MCCB). No $I_{cw}$ rating required.
   - **Category B:** Selective breakers with intentional short-time delay for downstream discrimination (e.g., Drawout ACB).
     $$I_{cw\_1s} \ge I_{sc\_prospective}$$

---

## 4. Switchboard Copper & Aluminium Busbar Physics

- **Statutory Authority:** IEC 60865-1:2011 Clause 5 & IEC 61439-1:2020 Clause 8.6.

### 4.1 Continuous Thermal Current Rating (Heat Dissipation Equilibrium)
At steady state, $I^2 R$ electrical heat generation equals convective and radiative heat dissipation:
$$I^2 \cdot R_{AC\theta} = h_{conv} \cdot A_{surface} \cdot \Delta T + \varepsilon \cdot \sigma_{SB} \cdot A_{surface} \cdot (T_{bus}^4 - T_{amb}^4)$$
- Permissible temperature rise ($\Delta T$):
  - Bare Copper in air: $\Delta T \le 50\text{ K}$ (Max busbar temp $90^\circ\text{C}$ at $40^\circ\text{C}$ ambient) per IEC 61439-1 Table 6.
  - Silver-plated / Tin-plated joints: $\Delta T \le 65\text{ K}$ (Max temp $105^\circ\text{C}$).
- Maximum Continuous Current Densities (Conservative Engineering Baseline):
  - **Electrolytic Copper (E91E):** $J \le 1.20 - 1.50\text{ A/mm}^2$
  - **Electrical Grade Aluminium (E91E):** $J \le 0.80 - 1.00\text{ A/mm}^2$

### 4.2 Peak Electrodynamic Force & Support Bending Moments
Under three-phase peak short circuit ($i_p$ in kA), the repulsive force per unit length between parallel rectangular busbars spaced distance $a$ (meters) apart:
$$F_m = 0.173 \cdot i_p^2 \cdot \frac{l}{a} \quad [\text{N}]$$

Where peak factor $\kappa$ per IEC 60909-0:
$$\kappa = 1.02 + 0.98 \cdot e^{-3 / (X/R)}$$
$$i_p = \kappa \cdot \sqrt{2} \cdot I_{sc}$$

The maximum bending stress on the insulator supports must satisfy:
$$\sigma_{bending} = \frac{F_m \cdot l_{span}}{16 \cdot W_{insulator}} \le \frac{R_{failure}}{1.5}$$
*(where a minimum mechanical safety factor of $1.5$ is enforced).*
