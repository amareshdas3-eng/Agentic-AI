# SLD Engineering Pro — Calculation & Verification Rules (Statutory Edition)
### Topological Graph Mathematics, Interlocking Logic & Statutory Safety Rules
**Framework:** ProEngineering Industrial Power Systems Suite  
**Statutory Basis:** IEC 61936-1:2021, IEC 62271-200:2021, IEC 62271-102:2018, IS 10118, CEA Safety Regs 2023 Reg 35/43/44, IEEE 141

---

## 1. Statutory Substation Verification Rules

### Rule 01: Voltage Continuity and Transformation Ratio
- **Statutory Authority:** IEC 61936-1:2021 Clause 4.2 & CEA Safety Regulations 2023 Regulation 43(1).
- **Physical Law:** In an alternating-current industrial distribution network, power transformation across winding nodes must satisfy:
  $$|V_{rated\_pri}(T) - V_{nominal}(B_{pri})| = 0$$
  $$|V_{rated\_sec}(T) - V_{nominal}(B_{sec})| \le 5.0\%$$
- **Verification Logic:**
  ```python
  def verify_voltage_continuity(transformer, bus_pri, bus_sec):
      if transformer.rated_primary_voltage != bus_pri.nominal_voltage:
          return Issue(severity="CRITICAL", rule="R-01", 
                       msg=f"Transformer {transformer.tag} primary ({transformer.rated_primary_voltage}V) mismatches primary bus {bus_pri.tag} ({bus_pri.nominal_voltage}V)")
      ratio_err = abs(transformer.rated_secondary_voltage - bus_sec.nominal_voltage) / bus_sec.nominal_voltage
      if ratio_err > 0.05:
          return Issue(severity="CRITICAL", rule="R-01", 
                       msg=f"Transformer {transformer.tag} secondary ({transformer.rated_secondary_voltage}V) exceeds ±5% tolerance on bus {bus_sec.tag} ({bus_sec.nominal_voltage}V)")
      return Issue(severity="PASS", rule="R-01", msg="Voltage continuity validated.")
  ```

---

### Rule 02: Switchyard Disconnector & Earthing Switch Mechanical Interlock
- **Statutory Authority:** IEC 62271-102:2018 Clause 5.104 & CEA Safety Regulations 2023 Regulation 44(2)(a).
- **Mandatory Safety Interlock Requirement:**
  1. The Earthing Switch ($ES$) can be closed **ONLY IF** the Disconnector/Isolator ($DS$) and Circuit Breaker ($CB$) are **OPEN**.
  2. The Disconnector ($DS$) can be closed **ONLY IF** the Earthing Switch ($ES$) is **OPEN**.
  3. The Disconnector ($DS$) cannot break load current; it can be operated **ONLY IF** the Circuit Breaker ($CB$) is **OPEN**.
- **State Logic Formulation:**
  $$\text{State}(ES = \text{CLOSED}) \implies \text{State}(DS = \text{OPEN}) \land \text{State}(CB = \text{OPEN})$$
  $$\text{State}(DS = \text{CLOSED}) \implies \text{State}(ES = \text{OPEN})$$
  $$\Delta \text{State}(DS) \implies \text{State}(CB = \text{OPEN})$$
- **Violation Severity:** **CRITICAL**. An electrical or mechanical failure in this interlock results in closing an earth switch onto an energized 33kV/11kV busbar (3-phase bolted line-to-earth explosion).

---

### Rule 03: Dual-Incomer Bus Coupler 2-out-of-3 Castell Interlocking
- **Statutory Authority:** IS 10118 (Part 3) Clause 6.4, IEEE Std 141-1993 Section 3.3.4, and CEA Safety Regs 2023 Reg 44(3).
- **Operating Constraint:** For dual-incomer switchboards with bus coupler:
  $$\text{State}(CB_{inc1}) + \text{State}(CB_{inc2}) + \text{State}(CB_{coupler}) \le 2$$
  *(where 1 = Closed, 0 = Open).*
- **Fault Level Rationale:** If all three breakers close simultaneously, the fault level doubles ($I_{sc\_total} = I_{sc\_TR1} + I_{sc\_TR2} \approx 2 \times I_{sc}$). Standard switchgear rated for single transformer fault duty ($I_{cu} = 25\text{kA}$ or $50\text{kA}$) will be subjected to $50\text{kA}$ to $100\text{kA}$, violating breaking capacity ($I_{cu} < I_{sc}$) and causing explosive destruction.
- **Exception Rule:** Closed-transition momentary paralleling ($t \le 100\text{ms}$) is permitted **ONLY IF** an automatic sync-check relay (ANSI 25) with high-speed reverse-power tripping is explicitly declared in the protection interface.

---

### Rule 04: Loss of Service Continuity (LSC) & Internal Arc Classification (IAC)
- **Statutory Authority:** IEC 62271-200:2021 Clause 3.106 & Clause 6.106.
- **Specification Check:**
  - For 11kV/33kV indoor industrial switchgear, the topology must declare Loss of Service Continuity category:
    - **LSC2B:** High availability. Cable compartment, busbar compartment, and breaker compartment are segregated. Cable termination can remain live during maintenance of circuit breaker.
    - **LSC2A:** Busbar can remain live during breaker maintenance, but cable must be de-energized.
    - **LSC1:** No service continuity during maintenance. (Prohibited for industrial continuous process plants).
  - Internal Arc Classification: **IAC AFLR** (Personnel protection in Front, Lateral, and Rear for $1.0\text{s}$ at rated fault level $I_{sc}$).

---

### Rule 05: Transformer Winding Protection & Safety Trip Interfaces
- **Statutory Authority:** CEA Safety Regulations 2023 Regulation 44(1) & IEEE Std 242 (Buff Book).
- **Mandatory Trip Matrix for Transformers $\ge 1000\text{ kVA}$:**
  - **Buchholz Relay (ANSI 63):** Double-float gas accumulation (Alarm) and oil surge (Instantaneous Trip to upstream HV Breaker and downstream LV Incomer).
  - **Pressure Relief Device (ANSI 63PRD):** Spring-loaded rapid pressure relief with trip contact.
  - **Winding Temperature Indicator (ANSI 49):** Alarm at $95^\circ\text{C}$, Trip at $105^\circ\text{C}$ (for Class A/O insulation).
  - **Oil Temperature Indicator (ANSI 26):** Alarm at $85^\circ\text{C}$, Trip at $95^\circ\text{C}$.
  - **Restricted Earth Fault (ANSI 64R / 87N):** High-impedance unit protection for star-connected secondary winding.
- **Automated Verification:** The SLD drawing and schedule must include explicit inter-trip cabling connections from transformer marshalling box to upstream and downstream circuit breaker shunt trip coils.

---

### Rule 06: Surge Arrester (Lightning Arrester) Placement
- **Statutory Authority:** IEC 60099-4:2014 & CEA Safety Regulations 2023 Regulation 43(3).
- **Rule:** Gapless Metal-Oxide (ZnO) Surge Arresters (Class 1 or Class 2) must be located:
  1. At the termination point of all incoming 33kV and 11kV overhead transmission lines.
  2. Directly on transformer primary terminal bushings if lead length from line arrester exceeds $10\text{ meters}$.
  3. Continuous operating voltage rating: $U_c \ge 1.05 \times \frac{V_{LL}}{\sqrt{3}}$ for solidly earthed; $U_c \ge V_{LL}$ for unearthed / isolated neutral systems.
