# ProEngineering Electrical Intelligence Suite — Module API Contracts
### Revision: 2.0.0 (Strict Types & Pure Function Contracts)
**Author:** Agent 0 (Integration Lead) & Agent 4 (Calculation Engine Lead)  
**Classification:** Interface Definition Language (TypeScript / JSON-Schema)

---

## 1. Core Foundational Types & Provenance Enums

```typescript
export type ValueProvenance =
  | 'USER_ENTERED'
  | 'IMPORTED_RAW'
  | 'ENGINEER_CONFIRMED'
  | 'PROJECT_DEFAULT'
  | 'CALCULATED_DETERMINISTIC'
  | 'AI_HYPOTHESIS'; // Strictly blocked from calculation engine inputs

export type EvaluationStatus =
  | 'PASS'
  | 'FAIL'
  | 'NOT_ASSESSED'      // Missing required input or missing acceptance criterion
  | 'REVIEW_REQUIRED';  // Boundary condition, engineering exception, or unverified source

export type VerificationStatus =
  | 'VERIFIED'
  | 'NEEDS_AUTHORISED_SOURCE'
  | 'CONFLICTED'
  | 'NOT_APPLICABLE';

export type LifecycleStatus =
  | 'DRAFT'
  | 'PRELIMINARY_NOT_FOR_CONSTRUCTION'
  | 'UNDER_REVIEW'
  | 'APPROVED_FOR_PILOT'
  | 'SUPERSEDED';

export type SeverityTier =
  | 'CRITICAL_SAFETY'    // Life-safety risk, fire hazard, breaking capacity violation -> BLOCKS RELEASE
  | 'MAJOR_ENGINEERING'  // Continuous overload, excessive voltage drop (>5%), wrong starter logic
  | 'MINOR_DISCREPANCY'  // Inconsistent tagging, minor documentation difference
  | 'INFO_MISSING_DATA'; // Unstated ambient temperature, missing spare feeder margin

export interface TraceableValue<T> {
  value: T;
  unit: string; // Explicit SI or recognized engineering unit ('V', 'A', 'kW', 'mm2', 'm', 'Ohm/km', etc.)
  provenance: ValueProvenance;
  source_document_id?: string;
  source_location?: string; // e.g., "Sheet: Load_List, Row: 14, Col: F"
  confirmed_by_user_id?: string;
  confirmed_at?: string; // ISO-8601
}
```

---

## 2. Universal Deterministic Calculation Contract

Every calculation module adheres to the pure, side-effect-free request/response contract:

```typescript
export interface CalculationRequest<TInputs, TCriteria> {
  equipment_id: string;
  project_id: string;
  project_revision: string;
  inputs: TInputs;
  criteria: TCriteria; // ProjectDesignBasis criteria must be passed explicitly; no hidden hardcoded limits
}

export interface CalculationResult<TOutputs> {
  method_id: string;          // e.g., "RADIAL_VD_3PH_IEC_R_X_V2"
  method_version: string;      // e.g., "2.0.0"
  status: 'CALCULATED' | 'INVALID_INPUT' | 'INCOMPLETE_INPUT';
  evaluation_status: EvaluationStatus; // PASS | FAIL | NOT_ASSESSED | REVIEW_REQUIRED
  outputs?: TOutputs;
  intermediate_steps: Array<{
    symbol: string;
    formula_latex: string;
    substituted_values: string;
    value: number;
    unit: string;
  }>;
  assumptions: string[];
  warnings: string[];
  missing_inputs: string[];
  errors: string[];
  executed_at: string; // ISO-8601
}
```

---

## 3. Module 02: LoadFlow & VoltageDrop Pro Contracts

```typescript
export interface VoltageDropInputs {
  power_kw: TraceableValue<number>;
  voltage_v: TraceableValue<number>;
  power_factor: TraceableValue<number>;
  efficiency: TraceableValue<number>;
  phases: TraceableValue<1 | 3>;
  cable_length_m: TraceableValue<number>;
  conductor_material: TraceableValue<'COPPER' | 'ALUMINIUM'>;
  insulation_type: TraceableValue<'XLPE' | 'PVC'>;
  size_mm2: TraceableValue<number>;
  parallel_runs: TraceableValue<number>;
  is_motor_starting?: TraceableValue<boolean>;
  motor_starting_current_ratio?: TraceableValue<number>; // Optional: default 6.0 if motor starting
  motor_starting_power_factor?: TraceableValue<number>;  // Optional: default 0.30 if motor starting
}

export interface VoltageDropCriteria {
  max_feeder_voltage_drop_pct: number;      // e.g., 3.0%
  max_motor_starting_dip_pct: number;       // e.g., 15.0%
  conductor_operating_temp_c?: number;      // e.g., 90°C for XLPE, 70°C for PVC
}

export interface VoltageDropOutputs {
  design_current_a: number;
  r_operating_ohm_per_km: number;
  xl_ohm_per_km: number;
  z_effective_ohm_per_km: number;
  voltage_drop_volts: number;
  voltage_drop_pct: number;
  margin_pct: number; // positive = compliant, negative = violation
  motor_starting?: {
    starting_current_a: number;
    starting_voltage_drop_volts: number;
    starting_voltage_drop_pct: number;
    starting_margin_pct: number;
  };
}
```

---

## 4. Module 03: Equipment Sizing Pro Contracts

```typescript
export interface TransformerSizingInputs {
  diversified_demand_kva: TraceableValue<number>;
  primary_voltage_v: TraceableValue<number>;
  secondary_voltage_v: TraceableValue<number>;
  ambient_temperature_c: TraceableValue<number>;
  altitude_m: TraceableValue<number>;
}

export interface TransformerSizingCriteria {
  growth_margin_pct: number;           // e.g., 15.0%
  max_continuous_loading_pct: number;  // e.g., 80.0% or 100.0%
}

export interface CableFaultWithstandInputs {
  conductor_material: TraceableValue<'COPPER' | 'ALUMINIUM'>;
  insulation_type: TraceableValue<'XLPE' | 'PVC'>;
  selected_size_mm2: TraceableValue<number>;
  parallel_runs: TraceableValue<number>;
  fault_current_ka: TraceableValue<number>;
  fault_clearing_time_sec: TraceableValue<number>;
}

export interface CableFaultWithstandCriteria {
  standard_basis: 'IEC_60364_5_54' | 'IS_732' | 'BS_7671';
}
```

---

## 5. Module 05: Design Assurance Engine Finding Schema

```typescript
export interface Finding {
  finding_id: string;
  project_id: string;
  project_revision: string;
  rule_id: string; // e.g., "ASSURANCE_010_CABLE_FAULT_WITHSTAND"
  rule_description: string;
  severity: SeverityTier;
  source_records: Array<{
    document_id: string;
    document_revision: string;
    record_id: string;
    field_name: string;
    compared_value: string | number;
    unit: string;
  }>;
  rationale: string;
  missing_data_or_uncertainty?: string;
  recommended_remediation: string;
  status: 'OPEN' | 'EXCEPTION_PROPOSED' | 'CLOSED_VERIFIED';
  responsible_owner?: string;
  closure_evidence_id?: string;
  created_at: string;
  closed_at?: string;
}
```
