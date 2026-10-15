# Product 04: MCC & PCC Architect Pro — Specification
### Industrial Switchboard Architecture, Motor Feeders, Compartment Sizing & Starter Selection
**Product Family:** ProEngineering Industrial Power Systems Suite  
**Version:** 1.0.0 (Release Candidate Spec)  
**Standard Basis:** IEC 61439-1 / IEC 61439-2 (Low-Voltage Switchgear and Controlgear Assemblies), IS 8623, IEC 60947-4-1, IEEE 841

---

## 1. Product Scope & Capabilities

`MCC & PCC Architect Pro` bridges the critical gap between plant mechanical load lists and electrical switchboard manufacturing. It automatically converts an industrial motor and non-motor load list into an auditable, physically feasible switchboard lineup for:
1. **Power Control Centers (PCC):** High-current main distribution switchboards ($1250\text{A}$ to $6300\text{A}$, $50\text{kA}$ $1.0\text{s}$) housing incoming ACBs, bus couplers, and heavy sub-feeders.
2. **Motor Control Centers (MCC):** Multi-tier compartmentalized motor distribution boards ($400\text{A}$ to $2000\text{A}$) housing DOL, Star-Delta, Soft Starter, and VFD modules.
3. **Intelligent MCCs (iMCC):** Incorporating motor management controllers, fieldbus communications (Modbus-TCP / Profinet), and hardwired safety interlocks.

---

## 2. In-Scope Architectural Features

- **Starter Selection Decision Matrix:**
  Evaluates motor rated kW, starting torque requirement, grid fault level stiffness, and starting frequency to select DOL, Star-Delta, Electronic Soft Starter, or VFD.
- **Physical Compartment & Tier Allocation:**
  - Standard cubicle height ($2100\text{mm} - 2200\text{mm}$) with top/bottom horizontal busbar chamber and cable alley.
  - Multi-tier stacking:
    - Fractional to $7.5\text{ kW}$ motors: 5 to 6 modules per column.
    - $11\text{ kW}$ to $22\text{ kW}$ motors: 3 to 4 modules per column.
    - $30\text{ kW}$ to $55\text{ kW}$ motors: 2 to 3 modules per column.
    - $75\text{ kW}$ to $160\text{ kW}$ motors: 1 module per column.
    - $\ge 200\text{ kW}$ motors / VFDs: Dedicated full-height vertical section.
- **Internal Forms of Separation (IEC 61439-2):**
  - Form 2b (Busbars separated from functional units).
  - Form 3b (Busbars and terminals separated from functional units).
  - Form 4b (Complete individual compartmentalization for busbars, functional units, and outgoing cable terminations).
- **Control & Automation Interface Register:**
  Generates the complete I/O schedule for DCS / PLC integration:
  - Digital Inputs (DI): Run Feedback, Trip Feedback, Local/Remote Status.
  - Digital Outputs (DO): Start Command, Stop Command, Fault Reset.
  - Analog Inputs (AI): Motor Current (4-20mA), Winding Temperature.
  - Analog Outputs (AO): Speed Reference for VFDs (0-10V / 4-20mA).

---

## 3. Explicit Model Exclusions & Safety Limits

- Detailed sheet metal punching and fabrication CAD CAM drawings (DXF nesting).
- Thermal CFD airflow modeling within enclosed non-ventilated cubicles (flags required forced ventilation for VFD enclosures $> 30\text{ kW}$).
- Internal arc containment testing certification (IEC TR 61641) — logged as mandatory factory type-test requirement.
