# LoadFlow & VoltageDrop Pro — Deterministic Calculation Engine (Statutory Edition)
### Physics Derivations, Standards Reference Formulas & Mathematical Proofs
**Framework:** ProEngineering Industrial Power Systems Suite  
**Statutory Basis:** IEC 60364-5-52:2019, IEC 60287-1-1:2014, IS 732:2019, BS 7671:2018+A2:2022, NEC 2023 Art. 210.19 / 215.2, IEEE 141

---

## 1. Statutory Voltage Drop Limits

| Jurisdiction / Standard | Lighting Feeders | Power & Motor Feeders | Overall Substation to Load Terminal | Motor Starting Transient Dip |
|---|---|---|---|---|
| **IEC 60364-5-52 Section 525** | $\le 3.0\%$ | $\le 5.0\%$ | $\le 5.0\%$ (Public LV) / $\le 8.0\%$ (Private MV/LV) | $\le 15.0\%$ (IEC 60034-1) |
| **IS 732:2019 Clause 5.2.5** | $\le 3.0\%$ | $\le 5.0\%$ | $\le 5.0\%$ | $\le 15.0\%$ |
| **BS 7671:2018+A2:2022 App. 4** | $\le 3.0\%$ | $\le 5.0\%$ | $\le 5.0\%$ | $\le 15.0\%$ |
| **NEC 2023 Art. 210.19 / 215.2** | $\le 3.0\%$ | $\le 3.0\%$ (Branch) | $\le 5.0\%$ (Feeder + Branch Combined) | $\le 15.0\%$ (IEEE 141) |

---

## 2. Rigorous Physical Derivations

### 2.1 Conductor AC Operating Resistance ($R_{AC}$) Derivation
DC resistance at standard calibration temperature ($20^\circ\text{C}$) is given by:
$$R_{DC20} = \frac{\rho_{20} \cdot 1000}{S} \quad [\Omega/\text{km}]$$

Where:
- Standard resistivity at $20^\circ\text{C}$:
  - Copper: $\rho_{20} = 1.7241 \times 10^{-2}\text{ }\Omega\cdot\text{mm}^2/\text{m}$ (100% IACS conductivity).
  - Aluminium: $\rho_{20} = 2.8264 \times 10^{-2}\text{ }\Omega\cdot\text{mm}^2/\text{m}$ (61% IACS conductivity).

#### Step 1: Operating Temperature Correction (Linear Formulation per IEC 60287-1-1)
At maximum continuous rated operating temperature $\theta$ ($70^\circ\text{C}$ for PVC, $90^\circ\text{C}$ for XLPE/EPR):
$$R_{DC\theta} = R_{DC20} \cdot [1 + \alpha_{20} \cdot (\theta - 20)]$$
- Temperature coefficient of resistance ($\alpha_{20}$):
  - Copper: $\alpha_{20} = 0.00393\text{ }^\circ\text{C}^{-1}$
  - Aluminium: $\alpha_{20} = 0.00403\text{ }^\circ\text{C}^{-1}$

#### Step 2: Skin Effect ($y_s$) and Proximity Effect ($y_p$)
For alternating current ($50\text{ Hz} / 60\text{ Hz}$), non-uniform current density across the conductor cross-section increases effective resistance:
$$R_{AC} = R_{DC\theta} \cdot (1 + y_s + y_p)$$

Where skin effect factor $y_s$:
$$x_s^2 = \frac{8\pi f}{R_{DC\theta} \cdot 10^7} \cdot k_s$$
$$y_s = \frac{x_s^4}{192 + 0.8 \cdot x_s^4}$$
*(where $f$ is frequency in Hz, $k_s = 1.0$ for round stranded conductors).*

Where proximity effect factor $y_p$:
$$x_p^2 = \frac{8\pi f}{R_{DC\theta} \cdot 10^7} \cdot k_p$$
$$y_p = \frac{x_p^4}{192 + 0.8 \cdot x_p^4} \cdot \left(\frac{d_c}{s}\right)^2 \cdot 2.9$$
*(where $d_c$ is conductor diameter, $s$ is axial distance between conductors).*

*For conductors $\le 150\text{ mm}^2$ at $50\text{Hz}$, $(y_s + y_p) < 0.01$ and is negligible. For conductors $\ge 240\text{ mm}^2$, $R_{AC}$ increases by $2\% - 8\%$ and MUST be accounted for.*

---

### 2.2 Conductor Inductive Reactance ($X_L$) Derivation
The self-inductance of a multi-core or trefoil cable per phase per kilometer:
$$L = 0.05 + 0.2 \cdot \ln\left(\frac{GMD}{GMR}\right) \quad [\text{mH/km}]$$

Where:
- $GMD$: Geometric Mean Distance between phase conductors ($GMD = \sqrt[3]{d_{12} \cdot d_{23} \cdot d_{31}}$). For trefoil, $GMD = d_{cable}$.
- $GMR$: Geometric Mean Radius of the stranded conductor ($GMR = 0.7788 \cdot r_{conductor}$).

Inductive reactance at frequency $f$:
$$X_L = 2\pi f \cdot L \times 10^{-3} \quad [\Omega/\text{km}]$$
- At $50\text{ Hz}$, $X_L$ ranges from $0.106\text{ }\Omega/\text{km}$ ($2.5\text{ mm}^2$) to $0.071\text{ }\Omega/\text{km}$ ($630\text{ mm}^2$) for multicore XLPE cables.

---

### 2.3 Vector Phasor Voltage Drop Derivation (Balanced Three-Phase)

Consider a balanced three-phase source voltage phasor $\mathbf{V}_S$ feeding a load terminal with voltage $\mathbf{V}_L$ via line impedance $\mathbf{Z} = R + jX$:
$$\mathbf{V}_S = \mathbf{V}_L + \sqrt{3} \cdot \mathbf{I} \cdot \mathbf{Z}$$

Let $\mathbf{V}_L = V_L \angle 0^\circ$ be the reference phasor. For a lagging load current:
$$\mathbf{I} = I \angle (-\varphi) = I (\cos\varphi - j\sin\varphi)$$
$$\mathbf{Z} = R + jX$$

The voltage drop phasor is:
$$\Delta \mathbf{V} = \sqrt{3} \cdot \mathbf{I} \mathbf{Z} = \sqrt{3} \cdot I (\cos\varphi - j\sin\varphi)(R + jX)$$
$$\Delta \mathbf{V} = \sqrt{3} \cdot I \cdot [(R\cos\varphi + X\sin\varphi) + j(X\cos\varphi - R\sin\varphi)]$$

The exact magnitude difference between source and receiving end:
$$V_S = \sqrt{\left(V_L + \sqrt{3} \cdot I(R\cos\varphi + X\sin\varphi)\right)^2 + \left(\sqrt{3} \cdot I(X\cos\varphi - R\sin\varphi)\right)^2}$$

Because the imaginary quadrature drop $\sqrt{3} \cdot I(X\cos\varphi - R\sin\varphi) \ll V_L$ (typically $< 3\%$ of $V_L$), applying Taylor series expansion $\sqrt{1 + u} \approx 1 + \frac{1}{2}u$:
$$\Delta V \approx \sqrt{3} \cdot I \cdot (R \cos\varphi + X \sin\varphi)$$

The exact quadrature correction term per IEC 60364-5-52 Annex G:
$$\Delta V_{exact} = \sqrt{3} \cdot I \cdot (R\cos\varphi + X\sin\varphi) + \frac{3 \cdot I^2 \cdot (X\cos\varphi - R\sin\varphi)^2}{2 \cdot V_L}$$

*ProEngineering's calculation engine evaluates both the standard linear term and the exact non-linear vector difference.*

---

### 2.4 Motor Starting Transient Voltage Dip Derivation (IEEE Std 141 Section 3.8)

During motor direct-on-line (DOL) start, the motor behaves as a locked-rotor impedance:
$$Z_{LR} = \frac{V_{LL}}{\sqrt{3} \cdot I_{start}} \quad \text{with } \cos\varphi_{LR} \approx 0.20 - 0.35$$

The total feeder impedance $\mathbf{Z}_{cable} = (R_{cable} + jX_{cable})$. The transient voltage dip at the motor terminals during starting is:
$$\Delta V_{start} = \frac{\sqrt{3} \cdot I_{start} \cdot L}{1000 \cdot N_{runs}} \cdot (R_{cable} \cos\varphi_{LR} + X_{cable} \sin\varphi_{LR})$$

Where:
- $I_{start} = k_{start} \cdot I_{FLC}$ (typically $k_{start} = 6.0$).
- $\cos\varphi_{LR} = 0.30 \implies \sin\varphi_{LR} = \sqrt{1 - 0.30^2} = 0.9539$.

Because reactive current is dominant ($\sin\varphi_{LR} = 0.9539$), the inductive reactance $X_L$ of the cable contributes **more than 60% of the total starting voltage drop**! Neglecting reactance causes disastrous under-estimation of motor starting dip.
