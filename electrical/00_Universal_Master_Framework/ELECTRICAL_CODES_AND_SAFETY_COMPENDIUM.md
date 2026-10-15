# ProEngineering Electrical Codes & Safety Compendium
### Global Statutory Framework, Mathematical Derivations & Safety Standards Directory
**Classification:** Core Engineering Governance Reference  
**Applicability:** India (IS/CEA), International / Middle East (IEC), United Kingdom (BS), North America (IEEE/NFPA/NEC)

---

## 1. Statutory Standards Matrix & Authority Hierarchy

Every derivation, equation, and limit within the **ProEngineering Industrial Power Systems Suite** is anchored to authoritative statutory codes:

| Jurisdiction | Primary Installation Code | Short-Circuit Analysis | Equipment Assemblies | Safety & Earthing Codes |
|---|---|---|---|---|
| **International (IEC)** | **IEC 60364** (Parts 1 to 8) | **IEC 60909-0:2016** & **IEC 60865-1:2011** | **IEC 61439-1/2:2020** & **IEC 62271-200:2021** | **IEC 61936-1:2021**, **IEC 60479-1**, **IEC TR 61641** |
| **India (IS / CEA)** | **IS 732:2019** & **CEA Safety Regs 2023** | **IS 13234:1992 (IEC 60909)** | **IS/IEC 61439-1/2** & **IS 10118** | **IS 3043:2018** (Earthing Code of Practice) |
| **North America (USA)** | **NFPA 70 (NEC 2023)** | **IEEE Std 141 (Red)** & **IEEE Std 399 (Brown)** | **NEMA ICS 2 / NEMA PB2** | **IEEE Std 80:2013**, **NFPA 70E:2024**, **IEEE 1584:2018** |
| **United Kingdom (BS)** | **BS 7671:2018+A2:2022** (18th Edition) | **BS EN 60909-0** | **BS EN 61439-1/2** | **BS 7430:2011+A1:2015** (Earthing) |

---

## 2. Fundamental Safety Derivations & Equations

### 2.1 Touch and Step Voltage Safety Limits (IEEE Std 80:2013 & IS 3043:2018)

When an earth fault occurs in a substation ($V_{LL} \ge 1\text{ kV}$), fault current enters the earth grid, creating a Ground Potential Rise (GPR). Safe limits for human contact are governed by Dalziel's fibrillating current threshold for body weights of $50\text{ kg}$ and $70\text{ kg}$:

$$I_b = \frac{k}{\sqrt{t_s}} \quad (k_{50} = 0.116, \quad k_{70} = 0.157)$$

#### Derivation of Tolerable Touch Voltage ($E_{touch}$):
Human body resistance is standardized at $R_b = 1000\text{ }\Omega$. When a human touches a grounded structure while standing on soil surface covered with crushed rock (surface layer resistivity $\rho_s$, thickness $h_s$):

$$E_{touch} = \left( R_b + 1.5 \cdot C_s \cdot \rho_s \right) \cdot I_b$$

For a $50\text{ kg}$ person with fault duration $t_s$ (seconds):
$$E_{touch\_50} = \frac{1000 + 1.5 \cdot C_s \cdot \rho_s}{\sqrt{t_s}} \times 0.116 \quad [\text{Volts}]$$

#### Derivation of Tolerable Step Voltage ($E_{step}$):
The current path flows from one foot to the other (two feet in series, contact resistance $2 \times 3 \cdot C_s \cdot \rho_s = 6 \cdot C_s \cdot \rho_s$):
$$E_{step\_50} = \frac{1000 + 6.0 \cdot C_s \cdot \rho_s}{\sqrt{t_s}} \times 0.116 \quad [\text{Volts}]$$

Where $C_s$ is the surface layer derating factor:
$$C_s = 1 - \frac{0.09 \cdot \left(1 - \frac{\rho}{\rho_s}\right)}{2 \cdot h_s + 0.09}$$

*Standard Reference: IEEE Std 80:2013 Section 8.3 & IS 3043:2018 Clause 15.3.*

---

### 2.2 Arc Flash Hazard & Incident Energy (IEEE 1584:2018 & NFPA 70E:2024)

Arc-flash incident energy ($E$) in $\text{cal/cm}^2$ determines the required Personal Protective Equipment (PPE) category for personnel working on energized switchgear.

#### IEEE 1584:2018 Arcing Current Model ($I_{arc}$):
For open or box enclosures at voltages $208\text{V} \le V \le 15,000\text{V}$:
$$\log_{10}(I_{arc}) = k_1 + k_2 \log_{10}(I_{bf}) + k_3 \log_{10}(G) + k_4 \left(\frac{I_{bf}}{V}\right)$$
*(where $I_{bf}$ is bolted 3-phase fault current in kA, $G$ is electrode gap in mm, $k_1..k_4$ are enclosure coefficients).*

#### Incident Energy Calculation:
$$E = 4.184 \cdot C_f \cdot E_n \cdot \left(\frac{t}{0.2}\right) \cdot \left(\frac{610^x}{D^x}\right) \quad [\text{J/cm}^2]$$
$$\text{Incident Energy } (\text{cal/cm}^2) = \frac{E}{4.184}$$

Where:
- $t$: Arc clearing time by upstream protective relay/breaker (seconds).
- $D$: Working distance (typically $457\text{ mm}$ for LV switchboards, $914\text{ mm}$ for MV switchgear).
- Arc Flash Boundary ($AFB$): Distance at which incident energy equals $1.2\text{ cal/cm}^2$ (threshold of second-degree burns per NFPA 70E Table 130.5(C)).

---

### 2.3 Protection Disconnection Times for Electric Shock Safety (IEC 60364-4-41:2017)

Under **Automatic Disconnection of Supply (ADS)**, maximum clearing times for final circuits $\le 32\text{A}$ ($230\text{V} / 400\text{V}$ AC):
- **TN Systems:** $t_{max} = 0.4\text{ seconds}$ (Table 41.1)
- **TT Systems:** $t_{max} = 0.2\text{ seconds}$
- **Distribution Feeders & circuits $> 32\text{A}$:** $t_{max} = 5.0\text{ seconds}$

#### Earth Fault Loop Impedance Rule:
$$Z_s \le \frac{U_0}{I_a}$$
Where $U_0$ is nominal phase-to-earth voltage ($230\text{V}$), and $I_a$ is current causing automatic disconnection within time $t_{max}$.

---

### 2.4 Adiabatic Short-Circuit Thermal Limits (IEC 60364-5-54 & IEC 60865-1)

During an electrical short circuit ($t \le 5.0\text{ seconds}$), all heat dissipated by conductor resistance stays within the metallic core:

$$I^2 \cdot R \cdot dt = \gamma \cdot c \cdot A \cdot d\theta$$

Integrating from initial temperature $\theta_i$ to final permissible temperature $\theta_f$:
$$S_{min} = \frac{I_{sc} \cdot \sqrt{t}}{k}$$

Where thermodynamic constant $k$:
$$k = \sqrt{\frac{Q_c \cdot (\beta + 20)}{\rho_{20}} \cdot \ln\left(\frac{\beta + \theta_f}{\beta + \theta_i}\right)}$$

- For **Copper**: Volumetric heat capacity $Q_c = 3.45 \times 10^{-3}\text{ J}/(^\circ\text{C}\cdot\text{mm}^3)$, $\beta = 234.5^\circ\text{C}$, $\rho_{20} = 1.7241 \times 10^{-5}\text{ }\Omega\cdot\text{mm}$.
  - XLPE ($\theta_i = 90^\circ\text{C}, \theta_f = 250^\circ\text{C}$): **$k = 143$**
  - PVC ($\theta_i = 70^\circ\text{C}, \theta_f = 160^\circ\text{C}$): **$k = 115$**
- For **Aluminium**: $Q_c = 2.50 \times 10^{-3}\text{ J}/(^\circ\text{C}\cdot\text{mm}^3)$, $\beta = 228.1^\circ\text{C}$, $\rho_{20} = 2.8264 \times 10^{-5}\text{ }\Omega\cdot\text{mm}$.
  - XLPE ($\theta_i = 90^\circ\text{C}, \theta_f = 250^\circ\text{C}$): **$k = 94$**
  - PVC ($\theta_i = 70^\circ\text{C}, \theta_f = 160^\circ\text{C}$): **$k = 76$**

*Standard Reference: IEC 60364-5-54:2011 Annex A, BS 7671 Regulation 434.5.2, IS 732 Clause 5.4.*

---

### 2.5 Neutral Sizing & Triplen Harmonic Derating (IEC 60364-5-52 Annex E)

In industrial systems with high non-linear loads (VFDs, switched-mode power supplies, LED lighting, rectifiers), third harmonic currents ($150\text{ Hz}$) and odd multiples (triplen harmonics: 3rd, 9th, 15th) add arithmetically in the neutral conductor:

$$I_{neutral} = 3 \cdot I_{3rd}$$

#### Statutory Sizing Rules per IEC 60364-5-52 Table E.52.1:
- **$0\% - 15\%$ Third Harmonic:** Neutral sized equal to phase ($100\%$). No derating required.
- **$> 15\% - 33\%$ Third Harmonic:** Neutral sized equal to phase ($100\%$). Phase cables derated by factor **$0.86$**.
- **$> 33\%$ Third Harmonic:** Neutral carries more current than phase! Sizing **must be based on neutral current**:
  $$I_{design\_phase} = \frac{I_{neutral}}{0.86 \times 3 \cdot h_3}$$
  Neutral conductor cross-section must be equal to or greater than phase conductor ($S_N \ge S_{phase}$), and phase derating factor **$0.86$** is applied.

---

### 2.6 Electrodynamic Peak Short-Circuit Forces on Busbars (IEC 60865-1:2011)

Under peak short-circuit current ($i_p = \kappa \sqrt{2} I_{sc}$), the peak mechanical force between main horizontal busbar conductors of length $l$ and center-to-center spacing $a$:

$$F_{m} = \frac{\mu_0}{2\pi} \cdot \frac{\sqrt{3}}{2} \cdot i_p^2 \cdot \frac{l}{a} = 0.173 \cdot i_p^2 \cdot \frac{l}{a} \quad [\text{Newtons}]$$

#### Bending Stress on Busbar Supports ($\sigma_{tot}$):
$$M_b = \frac{F_m \cdot l}{16} \quad (\text{for continuous multi-span busbars})$$
$$\sigma_m = \frac{M_b}{W_b} \le q \cdot R_{p0.2}$$
*(where $W_b$ is section modulus of busbar, $R_{p0.2}$ is $0.2\%$ proof stress of copper/aluminium, $q$ is plasticity factor per IEC 60865-1).*

---

### 2.7 Internal Arc Fault Classification (IEC TR 61641:2014)

Industrial low-voltage switchboards (MCC/PCC) must be specified for **Internal Arc Classification (IAC)** to protect operating personnel in accordance with IEC TR 61641 criteria 1 through 7:
1. **Criterion 1:** Correctly secured doors, covers, and panels do not open.
2. **Criterion 2:** Parts of the switchboard do not fly off, causing danger to personnel.
3. **Criterion 3:** Arcing does not cause holes in the external enclosure parts.
4. **Criterion 4:** Vertically mounted black cotton indicators do not ignite.
5. **Criterion 5:** The protective circuit (earthing) continues to remain effective.
6. **Criterion 6:** The arc is confined to the original compartment (Form 4b segregation).
7. **Criterion 7:** Emergency operation can be restored after isolating the faulted unit.
