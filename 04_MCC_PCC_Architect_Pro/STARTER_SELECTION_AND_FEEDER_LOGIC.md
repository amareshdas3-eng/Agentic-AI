# MCC & PCC Architect Pro — Starter Selection & Feeder Logic (Statutory Edition)
### Switchboard Architecture, Type 2 Coordination & Internal Separation Standards
**Framework:** ProEngineering Industrial Power Systems Suite  
**Statutory Basis:** IEC 61439-1/2:2020, IEC 60947-4-1:2018, IEC TR 61641:2014, IEC 60034-30-1, IS/IEC 61439

---

## 1. Forms of Internal Separation (IEC 61439-2 Clause 8.101)

Internal barriers prevent contact with live adjacent parts and confine internal arcing during maintenance:

| Form of Separation | Busbars Separated From Functional Units | Functional Units Separated From Each Other | Terminals Separated From Functional Units | Terminals Separated From Each Other | Typical Industrial Application |
|---|---|---|---|---|---|
| **Form 1** | NO | NO | NO | NO | Unsegregated lighting panels (non-critical). |
| **Form 2a** | YES | NO | NO (Terminals in same compartment as busbar) | NO | Basic commercial sub-distribution. |
| **Form 2b** | YES | NO | YES (Terminals separate from busbars) | NO | Industrial auxiliary boards. |
| **Form 3a** | YES | YES | NO (Terminals separate from busbars, common with unit) | NO | Standard process MCCs. |
| **Form 3b** | YES | YES | YES (Terminals separate from functional unit) | NO | Heavy industrial MCCs. |
| **Form 4a** | YES | YES | YES (Terminals in same compartment as functional unit) | YES | Process plants with front termination. |
| **Form 4b** | **YES** | **YES** | **YES (Terminals in separate external cable compartment)** | **YES (Individual cable gland/alley for each feeder)** | **Petrochemical, Refinery, Offshore, Power Plants (Maximum Safety)** |

*ProEngineering's standard for critical process plants defaults to **Form 4b Type 7** (individual busbar droppers, functional modules, and cable boxes).*

---

## 2. Clearances and Creepage Distances (IEC 61439-1 Table 1 & Table 2)

For industrial low-voltage switchboards operating in an industrial environment (**Pollution Degree 3**, Overvoltage Category III, Material Group IIIa):

| System Parameter | Rated Value | Statutory Clearance in Air (Table 1) | Statutory Creepage Distance (Table 2) |
|---|---|---|---|
| **Rated Insulation Voltage ($U_i$)** | $1000\text{ V AC}$ | — | **$20.0\text{ mm}$** (Insulating creepage path) |
| **Rated Operating Voltage ($U_e$)** | $415\text{ V / } 690\text{ V AC}$ | — | **$16.0\text{ mm}$** (At 690V) |
| **Impulse Withstand Voltage ($U_{imp}$)** | **$8.0\text{ kV}$** | **$14.0\text{ mm}$** (Inhomogeneous field) | — |
| **Heavy Industrial Substation ($U_{imp}$)** | **$12.0\text{ kV}$** | **$18.0\text{ mm}$** | — |

*Any physical busbar or dropper arrangement with clearance $< 14.0\text{ mm}$ is flagged as a CRITICAL violation.*

---

## 3. Type 2 Coordination (IEC 60947-4-1 Table 11 & Clause 8.2.5.1)

Under short circuit conditions, the motor starter branch (comprising Circuit Breaker/MPCB + Contactor + Overload Relay) must satisfy **Type 2 Coordination**:

```
[Mains 415V Busbar]
        │
        ▼
[MPCB / MCCB: Magnetic Short-Circuit Protection]  ──> Clears bolted fault in < 15ms (I_cu >= 50kA)
        │
        ▼
[Contactor: AC-3 Duty Operational Switching]      ──> Contacts may lightly weld ONLY IF easily separable with screwdriver
        │
        ▼
[Thermal / Electronic Overload Relay]             ──> No damage, no tripping curve drift (retains calibration)
        │
        ▼
[Field Motor Terminal]
```

### 3.1 Coordination Test Sequences per IEC 60947-4-1:
1. **Low Short-Circuit Test Current ($"r"$):**
   - Test current $I_r$ corresponds to prospective current where magnetic trip takes over from thermal overload ($I_r = 10 \times I_{fl}$).
   - The assembly must clear the fault without burning or welding contacts.
2. **High Short-Circuit Test Current ($"q"$):**
   - Full rated prospective breaking capacity ($I_q \ge 50\text{ kA}$ at $415\text{V}$, $\cos\varphi = 0.25$).
   - Overload relay must remain functional and trip within $20\%$ of its nominal time-current curve after the fault.

---

## 4. Starter Selection Decision Hierarchy

```
                                  [Motor Input Data: kW, Application, Duty, Grid Stiffness]
                                                             │
                                   ┌─────────────────────────┴─────────────────────────┐
                                   ▼                                                   ▼
                     [Continuous Variable Flow? (Pumps/Fans)]           [Constant Speed Process Motor]
                                   │                                                   │
                                   ▼                                                   ▼
                    [VARIABLE FREQUENCY DRIVE (VFD)]                    ┌──────────────┴──────────────┐
                    - 0% Inrush current                                 ▼                             ▼
                    - IEC 61800-3 EMC filtering                  [Motor kW <= 5.5 kW]          [Motor kW > 5.5 kW]
                    - Dedicated ventilation ducting                     │                             │
                                                                        ▼                             ▼
                                                             [DIRECT-ON-LINE (DOL)]        ┌──────────┴──────────┐
                                                             - Ist = 6.0 - 7.0 x Ifl       ▼                     ▼
                                                             - High starting torque   [7.5 to 22 kW]     [> 22 kW to 160 kW]
                                                             - Lowest cost                 │                     │
                                                                                           ▼                     ▼
                                                                                   [STAR-DELTA (Y-Δ)]    [SOFT STARTER]
                                                                                   - Ist = 2.0 - 2.5 x   - Ist = 2.5 - 3.5 x
                                                                                   - Low torque loads    - Internal bypass
                                                                                   - 6-core motor cable  - Smooth torque
```

### 4.1 Contactor AC-3 Operational Deratings (IEC 60947-4-1 Table 1):
The line contactor must be rated for **AC-3 Utilization Category** (squirrel-cage induction motors: starting, switching off during run):
- Continuous rated operational current ($I_e$):
  $$I_{e\_AC3} \ge I_{FLC\_motor}$$
- Making capacity: $10 \times I_e$ at $\cos\varphi = 0.35$.
- Breaking capacity: $8 \times I_e$ at $\cos\varphi = 0.35$.
- For frequent jogging or inching duty, the contactor must be up-rated to **AC-4 Utilization Category**.
