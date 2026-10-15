# LoadFlow & VoltageDrop Pro — Test Benchmarks & Edge Cases
### Hand-Calculated Industrial Benchmarks, Verification Tolerances & Unit Test Suite
**Framework:** ProEngineering Industrial Power Systems Suite

---

## 1. Benchmark Overview & Tolerance Criteria

To guarantee zero hallucination, every software build of `LoadFlow & VoltageDrop Pro` must be verified against these hand-calculated test cases.
- **Maximum Acceptable Tolerance:** $\pm 0.25\%$ variance against manual engineering verification.
- **Test Runner Pass Rule:** 100% of benchmark assertions must pass before code is eligible for the `TESTED PROTOTYPE` or `RELEASE CANDIDATE` stamp.

---

## 2. Benchmark Case 1: Industrial 415V Motor Feeder (3-Phase Radial)

### Input Parameters:
- **Load Type:** Induction Motor (Centrifugal Water Pump)
- **Rated Power ($P$):** $75.0\text{ kW}$
- **System Voltage ($V_{LL}$):** $415\text{ V}$, $50\text{ Hz}$
- **Operating Power Factor ($\cos\varphi$):** $0.85$ lagging ($\sin\varphi = 0.5268$)
- **Motor Efficiency ($\eta$):** $0.93$ ($93\%$)
- **One-Way Cable Route Length ($L$):** $120.0\text{ meters}$
- **Cable Specification:** $3\text{C} \times 95\text{ mm}^2$ Aluminium Conductor, XLPE Insulated
- **Parallel Runs ($N_{runs}$):** $1$
- **Conductor Temperature Base:** $90^\circ\text{C}$ (Max continuous operating for XLPE)

### Step-by-Step Hand Calculation:

1. **Calculate Full Load Current ($I_{FLC}$):**
   $$I_{FLC} = \frac{75.0 \times 1000}{\sqrt{3} \times 415 \times 0.85 \times 0.93} = \frac{75,000}{568.106} = 132.016\text{ Amperes}$$

2. **Lookup Conductor Impedance:**
   - From IEC Table for $95\text{ mm}^2$ Aluminium:
     - $R_{20} = 0.320\text{ }\Omega/\text{km}$
     - $R_{90} = 0.320 \times [1 + 0.00403 \times (90 - 20)] = 0.320 \times 1.2821 = 0.4103\text{ }\Omega/\text{km}$
     - $X_L = 0.0760\text{ }\Omega/\text{km}$

3. **Calculate Effective Specific Resistance-Reactance Term:**
   $$R_{90} \cos\varphi + X_L \sin\varphi = (0.4103 \times 0.85) + (0.0760 \times 0.5268) = 0.34875 + 0.04004 = 0.38879\text{ }\Omega/\text{km}$$

4. **Calculate Voltage Drop ($\Delta V$):**
   $$\Delta V = \frac{\sqrt{3} \times 132.016 \times 120}{1000} \times 0.38879 = 27.439 \times 0.38879 = 10.668\text{ Volts}$$

5. **Calculate Percentage Voltage Drop ($\% \Delta V$):**
   $$\% \Delta V = \frac{10.668}{415} \times 100\% = 2.571\%$$

### Expected Result Summary:
- **Design Current:** $132.02\text{ A}$ ($\pm 0.1\text{ A}$)
- **Voltage Drop (Volts):** $10.67\text{ V}$ ($\pm 0.05\text{ V}$)
- **Voltage Drop (%):** $2.57\%$ ($\pm 0.02\%$)
- **Compliance Status:** **PASS** (Within statutory limit $\le 3.0\%$)

---

## 3. Benchmark Case 2: Heavy LV Incomer from 11kV/433V Transformer

### Input Parameters:
- **Source:** $1600\text{ kVA}$, $11/0.433\text{ kV}$ Distribution Transformer
- **Full Load Capacity ($S$):** $1600\text{ kVA}$ at $433\text{ V}$ ($V_{LL}$)
- **Assumed Operating Power Factor:** $0.90$ ($\sin\varphi = 0.4359$)
- **Feeder Route Length ($L$):** $45.0\text{ meters}$
- **Cable Specification:** Single-Core $630\text{ mm}^2$ Copper, XLPE Insulated
- **Parallel Runs ($N_{runs}$):** $3$ runs per phase (Trefoil formation)

### Step-by-Step Hand Calculation:

1. **Calculate Transformer Rated Secondary Current ($I_{sec}$):**
   $$I_{sec} = \frac{1600 \times 1000}{\sqrt{3} \times 433} = \frac{1,600,000}{750.02} = 2133.28\text{ Amperes}$$
   Current per parallel run: $I_{run} = \frac{2133.28}{3} = 711.09\text{ A}$

2. **Lookup Conductor Impedance for $630\text{ mm}^2$ Copper:**
   - $R_{90} = 0.0402\text{ }\Omega/\text{km}$
   - $X_L = 0.0710\text{ }\Omega/\text{km}$

3. **Calculate Effective Specific Resistance-Reactance Term:**
   $$R_{90} \cos\varphi + X_L \sin\varphi = (0.0402 \times 0.90) + (0.0710 \times 0.4359) = 0.03618 + 0.03095 = 0.06713\text{ }\Omega/\text{km}$$

4. **Calculate Voltage Drop ($\Delta V$):**
   $$\Delta V = \frac{\sqrt{3} \times 2133.28 \times 45}{1000 \times 3} \times 0.06713 = \frac{166.27}{3} \times 0.06713 = 55.423 \times 0.06713 = 3.720\text{ Volts}$$

5. **Calculate Percentage Voltage Drop ($\% \Delta V$):**
   $$\% \Delta V = \frac{3.720}{433} \times 100\% = 0.859\%$$

### Expected Result Summary:
- **Design Current:** $2133.28\text{ A}$
- **Voltage Drop (Volts):** $3.72\text{ V}$
- **Voltage Drop (%):** $0.86\%$
- **Compliance Status:** **PASS** (Excellent margin for main transformer incomer, well below $1.5\%$ allowance).

---

## 4. Benchmark Case 3: Motor Starting Transient Voltage Dip (DOL)

### Input Parameters:
- Same $75\text{ kW}$ motor from Benchmark Case 1.
- **Starting Current Ratio ($I_{st} / I_{fl}$):** $6.0 \times$
- **Starting Power Factor ($\cos\varphi_{st}$):** $0.30$ ($\sin\varphi_{st} = 0.9539$)
- **Starting Current ($I_{start}$):** $6.0 \times 132.016\text{ A} = 792.10\text{ A}$

### Step-by-Step Hand Calculation:
1. **Effective Starting Impedance:**
   $$R_{90} \cos\varphi_{st} + X_L \sin\varphi_{st} = (0.4103 \times 0.30) + (0.0760 \times 0.9539) = 0.12309 + 0.07250 = 0.19559\text{ }\Omega/\text{km}$$

2. **Starting Voltage Drop ($\Delta V_{start}$):**
   $$\Delta V_{start} = \frac{\sqrt{3} \times 792.10 \times 120}{1000} \times 0.19559 = 164.63 \times 0.19559 = 32.20\text{ Volts}$$

3. **Percentage Starting Voltage Dip:**
   $$\% \Delta V_{start} = \frac{32.20}{415} \times 100\% = 7.76\%$$

### Expected Result Summary:
- **Starting Current:** $792.10\text{ A}$
- **Starting Voltage Dip:** $32.20\text{ V}$ ($7.76\%$)
- **Compliance Status:** **PASS** (Within IEEE 141 standard starting dip limit $\le 15.0\%$).

---

## 5. Pathological & Edge Case Tests

| Test ID | Condition | Input Boundary | Expected System Behavior |
|---|---|---|---|
| **EDGE-01** | Zero Cable Length | $L = 0.0\text{ m}$ | Returns $\Delta V = 0.00\text{ V}$, $0.00\%$, status: `COMPLIANT`. Zero division prevented. |
| **EDGE-02** | Unity Power Factor | $\cos\varphi = 1.00$ ($\sin\varphi = 0$) | Reactance term evaluates to zero: $\Delta V \propto R \times 1.0$. |
| **EDGE-03** | Low Leading Power Factor | $\cos\varphi = 0.80$ Leading | Negative sign on reactive term: $R \cos\varphi - X \sin\varphi$. Ferranti effect detected if $\Delta V < 0$. |
| **EDGE-04** | Excessive Overload | $P = 500\text{ kW}$ on $95\text{ mm}^2$ | $\Delta V\% \approx 17.1\%$ $\implies$ Status: `CRITICAL_EXCEEDED`, triggers release block. |
| **EDGE-05** | Invalid Conductor Material | Conductor = `SILVER` | System throws typed validation error: `UNSUPPORTED_CONDUCTOR_MATERIAL`. |
