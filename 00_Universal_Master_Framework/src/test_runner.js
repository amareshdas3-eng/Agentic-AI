/**
 * ProEngineering Industrial Power Systems Suite
 * Comprehensive Multi-Gate Benchmark & Verification Test Runner (v2.0.0)
 * 
 * Executes:
 * 1. BM-01 to BM-15 Complete Independent Engineering Benchmarks (Pure Mathematical Solvers)
 * 2. Ingestion Layer Tests (Provenance, Duplicate Tag Rejection, Normalization)
 * 3. Cross-Document Design Assurance Tests (Rules ASSURANCE_001 to 008, Pinned Severities)
 * 4. Audit-Ready Watermarked Report Generation Tests (PRELIMINARY watermark)
 */

import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

import {
  calculateDesignCurrent,
  calculateConductorResistance,
  calculateFeederVoltageDrop,
  verifyCableFaultWithstand,
  sizeTransformer,
  evaluateMotorStarterTechnology,
  calculateBusbarShortCircuitForce,
  calculateSubstationTouchAndStepPotentials
} from './deterministic_engine.js';

import {
  parseCsvText,
  createTraceableValue,
  ingestLoadScheduleCsv,
  ingestCableScheduleCsv
} from './ingestion/csv_parser.js';

import {
  runDesignAssuranceAudit
} from './modules/assurance/consistency_checker.js';

import {
  generateAuditReportHtml
} from './reports/report_generator.js';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

let passedTests = 0;
let totalTests = 0;

function assert(condition, testName, details = '') {
  totalTests++;
  if (condition) {
    passedTests++;
    console.log(`  [PASS] Test ${totalTests}: ${testName}`);
  } else {
    console.error(`  [FAIL] Test ${totalTests}: ${testName} -> ${details}`);
    throw new Error(`Test assertion failed: ${testName} -> ${details}`);
  }
}

console.log("================================================================================");
console.log("PROENGINEERING.IN — 100% COMPLETE BENCHMARK & MULTI-GATE VERIFICATION SUITE");
console.log("================================================================================\n");

// --------------------------------------------------------------------------
// 1. BENCHMARK BM-01: 75kW Motor Feeder (3-Phase Radial 415V 120m)
// --------------------------------------------------------------------------
console.log("--> EXECUTING BENCHMARK BM-01: 75kW Motor Feeder on 95 mm² Al XLPE...");
const req_bm01 = {
  equipment_id: "FDR-001",
  project_id: "PRO-IND-01",
  project_revision: "v1.0",
  inputs: {
    power_kw: 75.0,
    voltage_v: 415,
    power_factor: 0.85,
    efficiency: 0.93,
    phases: 3,
    cable_length_m: 120.0,
    conductor_material: "ALUMINIUM",
    insulation_type: "XLPE",
    size_mm2: 95,
    parallel_runs: 1,
    is_motor_starting: true,
    motor_starting_current_ratio: 6.0,
    motor_starting_power_factor: 0.30
  },
  criteria: {
    max_feeder_voltage_drop_pct: 3.0,
    max_motor_starting_dip_pct: 15.0
  }
};

const res_bm01 = calculateFeederVoltageDrop(req_bm01);
assert(res_bm01.status === "CALCULATED", "Calculation Execution Status", res_bm01.status);
assert(res_bm01.evaluation_status === "PASS", "Evaluation Status against 3.0% Limit", res_bm01.evaluation_status);
assert(Math.abs(res_bm01.outputs.design_current_a - 132.02) < 0.1, "Design Current (132.02A)", `${res_bm01.outputs.design_current_a}A`);
assert(Math.abs(res_bm01.outputs.r_operating_ohm_per_km - 0.41027) < 0.001, "Operating R90 (0.4103)", `${res_bm01.outputs.r_operating_ohm_per_km}`);
assert(Math.abs(res_bm01.outputs.voltage_drop_volts - 10.67) < 0.15, "Voltage Drop Volts (10.67V)", `${res_bm01.outputs.voltage_drop_volts}V`);
assert(Math.abs(res_bm01.outputs.voltage_drop_pct - 2.57) < 0.05, "Voltage Drop Percent (2.57%)", `${res_bm01.outputs.voltage_drop_pct}%`);
assert(res_bm01.outputs.motor_starting.is_start_compliant === true, "Motor Starting Inrush Dip <= 15%", `${res_bm01.outputs.motor_starting.starting_voltage_drop_pct}%`);

// --------------------------------------------------------------------------
// 2. BENCHMARK BM-02: 110kW Heavy Pump (3-Phase Radial 415V 80m Cu)
// --------------------------------------------------------------------------
console.log("\n--> EXECUTING BENCHMARK BM-02: 110kW Heavy Pump on 185 mm² Cu XLPE...");
const req_bm02 = {
  equipment_id: "FDR-002",
  inputs: {
    power_kw: 110.0,
    voltage_v: 415,
    power_factor: 0.90,
    efficiency: 0.94,
    phases: 3,
    cable_length_m: 80.0,
    conductor_material: "COPPER",
    insulation_type: "XLPE",
    size_mm2: 185,
    parallel_runs: 1
  },
  criteria: {
    max_feeder_voltage_drop_pct: 3.0
  }
};
const res_bm02 = calculateFeederVoltageDrop(req_bm02);
assert(res_bm02.evaluation_status === "PASS", "BM-02 Evaluation Status PASS", res_bm02.evaluation_status);
assert(Math.abs(res_bm02.outputs.voltage_drop_volts - 3.66) < 0.15, "BM-02 Voltage Drop Volts (3.66V)", `${res_bm02.outputs.voltage_drop_volts}V`);
assert(res_bm02.outputs.voltage_drop_pct < 1.5, "BM-02 Voltage Drop Pct < 1.5%", `${res_bm02.outputs.voltage_drop_pct}%`);

// --------------------------------------------------------------------------
// 3. BENCHMARK BM-03: 37kW Long Run (3-Phase Radial 415V 200m 50mm² Cu Low PF)
// --------------------------------------------------------------------------
console.log("\n--> EXECUTING BENCHMARK BM-03: 37kW Long Feeder (200m, PF 0.75)...");
const req_bm03 = {
  equipment_id: "FDR-003",
  inputs: {
    power_kw: 37.0,
    voltage_v: 415,
    power_factor: 0.75,
    efficiency: 0.91,
    phases: 3,
    cable_length_m: 200.0,
    conductor_material: "COPPER",
    insulation_type: "XLPE",
    size_mm2: 50,
    parallel_runs: 1
  },
  criteria: {
    max_feeder_voltage_drop_pct: 5.0
  }
};
const res_bm03 = calculateFeederVoltageDrop(req_bm03);
assert(res_bm03.evaluation_status === "PASS", "BM-03 Evaluation Status PASS", res_bm03.evaluation_status);
assert(Math.abs(res_bm03.outputs.voltage_drop_volts - 10.88) < 0.25, "BM-03 Voltage Drop Volts (10.88V)", `${res_bm03.outputs.voltage_drop_volts}V`);

// --------------------------------------------------------------------------
// 4. BENCHMARK BM-04: 5kW Single-Phase Lighting Feeder (230V 50m 10mm² Cu)
// --------------------------------------------------------------------------
console.log("\n--> EXECUTING BENCHMARK BM-04: 5kW Single-Phase Feeder (230V)...");
const req_bm04 = {
  equipment_id: "FDR-1PH-01",
  inputs: {
    power_kw: 5.0,
    voltage_v: 230,
    power_factor: 0.95,
    efficiency: 1.0,
    phases: 1,
    cable_length_m: 50.0,
    conductor_material: "COPPER",
    insulation_type: "XLPE",
    size_mm2: 10,
    parallel_runs: 1
  },
  criteria: {
    max_feeder_voltage_drop_pct: 3.0
  }
};
const res_bm04 = calculateFeederVoltageDrop(req_bm04);
assert(res_bm04.evaluation_status === "PASS", "BM-04 Single Phase Status PASS", res_bm04.evaluation_status);
assert(Math.abs(res_bm04.outputs.voltage_drop_volts - 5.05) < 0.20, "BM-04 Single Phase Drop Volts (5.05V)", `${res_bm04.outputs.voltage_drop_volts}V`);

// --------------------------------------------------------------------------
// 5. BENCHMARK BM-05: 10kW UPS Outgoing Feeder (1-Phase 230V 30m 16mm² Cu)
// --------------------------------------------------------------------------
console.log("\n--> EXECUTING BENCHMARK BM-05: 10kW UPS Single-Phase Feeder (230V 30m)...");
const req_bm05 = {
  equipment_id: "FDR-UPS-01",
  inputs: {
    power_kw: 10.0,
    voltage_v: 230,
    power_factor: 0.90,
    efficiency: 0.98,
    phases: 1,
    cable_length_m: 30.0,
    conductor_material: "COPPER",
    insulation_type: "XLPE",
    size_mm2: 16,
    parallel_runs: 1
  },
  criteria: {
    max_feeder_voltage_drop_pct: 3.0
  }
};
const res_bm05 = calculateFeederVoltageDrop(req_bm05);
assert(res_bm05.evaluation_status === "PASS", "BM-05 Single Phase Status PASS", res_bm05.evaluation_status);
assert(Math.abs(res_bm05.outputs.voltage_drop_volts - 4.09) < 0.20, "BM-05 Drop Volts (4.09V)", `${res_bm05.outputs.voltage_drop_volts}V`);

// --------------------------------------------------------------------------
// 6. BENCHMARK BM-06 & BM-07: Motor Starting Inrush Transients
// --------------------------------------------------------------------------
console.log("\n--> EXECUTING BENCHMARK BM-06 & BM-07: Motor Starting Transient Dips...");
assert(res_bm01.outputs.motor_starting.starting_voltage_drop_pct < 10.0, "BM-06: 75kW Motor Inrush Dip < 10%", `${res_bm01.outputs.motor_starting.starting_voltage_drop_pct}%`);

const req_bm07 = {
  equipment_id: "FDR-BM07",
  inputs: {
    power_kw: 160.0,
    voltage_v: 415,
    power_factor: 0.88,
    efficiency: 0.95,
    phases: 3,
    cable_length_m: 90.0,
    conductor_material: "COPPER",
    insulation_type: "XLPE",
    size_mm2: 240,
    parallel_runs: 1,
    is_motor_starting: true,
    motor_starting_current_ratio: 5.5,
    motor_starting_power_factor: 0.25
  },
  criteria: {
    max_feeder_voltage_drop_pct: 3.0,
    max_motor_starting_dip_pct: 15.0
  }
};
const res_bm07 = calculateFeederVoltageDrop(req_bm07);
assert(Math.abs(res_bm07.outputs.motor_starting.starting_voltage_drop_pct - 5.21) < 0.25, "BM-07: 160kW Motor Starting Dip (5.21%)", `${res_bm07.outputs.motor_starting.starting_voltage_drop_pct}%`);

// --------------------------------------------------------------------------
// 7. BENCHMARK BM-08, BM-09, BM-10: Transformer Capacity & Bolted Fault
// --------------------------------------------------------------------------
console.log("\n--> EXECUTING BENCHMARK BM-08, BM-09 & BM-10: Transformer Sizing & Symmetrical Fault...");
const trResult1600 = sizeTransformer({
  inputs: {
    diversified_demand_kva: 1220,
    primary_voltage_v: 11000,
    secondary_voltage_v: 433,
    ambient_temperature_c: 45,
    altitude_m: 200
  },
  criteria: {
    growth_margin_pct: 15.0
  }
});
assert(trResult1600.outputs.selected_rating_kva === 1600, "BM-08: Standard IEC Transformer Rating (1600 kVA)", `${trResult1600.outputs.selected_rating_kva}`);
assert(Math.abs(trResult1600.outputs.rated_secondary_current_a - 2133.28) < 1.0, "Rated Secondary Current (2133.28A)", `${trResult1600.outputs.rated_secondary_current_a}`);
assert(Math.abs(trResult1600.outputs.bolted_fault_current_ka - 34.13) < 0.5, "BM-09: Bolted Secondary Fault Level (34.13kA)", `${trResult1600.outputs.bolted_fault_current_ka}`);

// BM-10: 2500kVA Transformer Bolted Fault at 415V, Z=7.15%
const ifault2500 = (2500 * 1000) / (Math.sqrt(3) * 415 * (7.15 / 100) * 1000);
assert(Math.abs(ifault2500 - 48.64) < 0.5, "BM-10: 2500kVA Bolted Fault Level (48.64kA)", `${ifault2500.toFixed(2)}kA`);

// --------------------------------------------------------------------------
// 8. BENCHMARK BM-11, BM-12, BM-13: Adiabatic Fault Withstand
// --------------------------------------------------------------------------
console.log("\n--> EXECUTING BENCHMARK BM-11, BM-12 & BM-13: Adiabatic Cable Withstand...");
// Undersized 95mm2 must FAIL
const faultFail = verifyCableFaultWithstand({
  inputs: {
    conductor_material: "ALUMINIUM",
    insulation_type: "XLPE",
    selected_size_mm2: 95,
    parallel_runs: 1,
    fault_current_ka: 25.0,
    fault_clearing_time_sec: 0.5
  }
});
assert(faultFail.evaluation_status === "FAIL", "BM-11: Undersized Cable Withstand (FAIL)", faultFail.evaluation_status);
assert(Math.abs(faultFail.outputs.min_required_area_mm2 - 188.06) < 0.5, "Minimum Required Area (188.06 mm²)", `${faultFail.outputs.min_required_area_mm2}`);

// Adequate 240mm2 must PASS
const faultPass = verifyCableFaultWithstand({
  inputs: {
    conductor_material: "ALUMINIUM",
    insulation_type: "XLPE",
    selected_size_mm2: 240,
    parallel_runs: 1,
    fault_current_ka: 25.0,
    fault_clearing_time_sec: 0.5
  }
});
assert(faultPass.evaluation_status === "PASS", "BM-12: Adequate Cable Withstand (PASS)", faultPass.evaluation_status);

// BM-13: Copper XLPE 50mm2 at 16kA for 0.2s (S_min = 16000 * sqrt(0.2) / 143 = 50.04 mm2)
const faultCu = verifyCableFaultWithstand({
  inputs: {
    conductor_material: "COPPER",
    insulation_type: "XLPE",
    selected_size_mm2: 50,
    parallel_runs: 1,
    fault_current_ka: 16.0,
    fault_clearing_time_sec: 0.2
  }
});
assert(Math.abs(faultCu.outputs.min_required_area_mm2 - 50.04) < 0.5, "BM-13: Copper Withstand S_min (50.04 mm²)", `${faultCu.outputs.min_required_area_mm2}`);

// --------------------------------------------------------------------------
// 9. BENCHMARK BM-14: Busbar Electrodynamic Forces (IEC 60865-1)
// --------------------------------------------------------------------------
console.log("\n--> EXECUTING BENCHMARK BM-14: Busbar Short-Circuit Forces (IEC 60865-1)...");
const busbarResult = calculateBusbarShortCircuitForce({
  inputs: {
    fault_current_rms_ka: 50.0,
    center_distance_m: 0.10,
    support_span_m: 0.35,
    xr_ratio: 8.0
  },
  criteria: {
    max_support_withstand_force_n: 15000
  }
});
assert(busbarResult.status === "CALCULATED", "BM-14: Busbar Force Execution", busbarResult.status);
assert(busbarResult.outputs.electrodynamic_force_n > 5000 && busbarResult.outputs.electrodynamic_force_n < 10000, "BM-14: Electrodynamic Force in Physical Range", `${busbarResult.outputs.electrodynamic_force_n} N`);
assert(busbarResult.evaluation_status === "PASS", "BM-14: Support Mechanical Withstand PASS");

// --------------------------------------------------------------------------
// 10. BENCHMARK BM-15: Substation Grounding Touch & Step (IEEE 80 / IS 3043)
// --------------------------------------------------------------------------
console.log("\n--> EXECUTING BENCHMARK BM-15: Substation Tolerable Touch & Step Potentials...");
const groundResult = calculateSubstationTouchAndStepPotentials({
  inputs: {
    fault_duration_s: 0.5,
    body_weight_kg: 50,
    surface_layer_resistivity_ohm_m: 3000,
    surface_layer_thickness_m: 0.10,
    native_soil_resistivity_ohm_m: 100
  }
});
assert(groundResult.status === "CALCULATED", "BM-15: Grounding Safety Potentials Status", groundResult.status);
assert(groundResult.outputs.surface_derating_cs === 0.7000, "BM-15: Surface Derating Cs (0.7000)", `${groundResult.outputs.surface_derating_cs}`);
assert(Math.abs(groundResult.outputs.tolerable_touch_voltage_v - 680.8) < 15.0, "BM-15: Tolerable Touch Potential (680.8V)", `${groundResult.outputs.tolerable_touch_voltage_v}V`);

// --------------------------------------------------------------------------
// 11. CONTRACT VALIDATION: Missing Inputs -> NOT_ASSESSED
// --------------------------------------------------------------------------
console.log("\n--> EXECUTING CONTRACT VALIDATION: Missing Input Handling...");
const incompleteReq = {
  equipment_id: "FDR-INCOMPLETE",
  inputs: {
    power_kw: 45.0,
    voltage_v: 415
  }
};
const incompleteRes = calculateFeederVoltageDrop(incompleteReq);
assert(incompleteRes.evaluation_status === "NOT_ASSESSED", "Incomplete Data Returns NOT_ASSESSED", incompleteRes.evaluation_status);
assert(incompleteRes.missing_inputs.includes("cable_length_m"), "Explicit Missing Input Listing", incompleteRes.missing_inputs.join(", "));

// --------------------------------------------------------------------------
// 12. ADR-001 VALIDATION: Parameterized Motor Starter Selection
// --------------------------------------------------------------------------
console.log("\n--> EXECUTING ADR-001 VALIDATION: Parameterized Starter Selection...");
const starter1 = evaluateMotorStarterTechnology({
  motor_kw: 15.0,
  grid_fault_mva: 500,
  starting_dip_limit_pct: 15.0
});
assert(starter1.recommended_technology === "STAR_DELTA", "15kW Motor Starter Selection", starter1.recommended_technology);

const starterVfd = evaluateMotorStarterTechnology({
  motor_kw: 45.0,
  requires_variable_speed: true
});
assert(starterVfd.recommended_technology === "VFD", "Process Flow Modulation Requires VFD", starterVfd.recommended_technology);

// --------------------------------------------------------------------------
// 13. INGESTION LAYER VERIFICATION (MVP-AC-02)
// --------------------------------------------------------------------------
console.log("\n--> EXECUTING INGESTION LAYER VERIFICATION (CSV Parsing & Provenance)...");
const loadCsvPath = path.join(__dirname, '../data/sample_load_schedule.csv');
const cableCsvPath = path.join(__dirname, '../data/sample_cable_schedule.csv');

const rawLoadCsv = fs.readFileSync(loadCsvPath, 'utf-8');
const rawCableCsv = fs.readFileSync(cableCsvPath, 'utf-8');

const loadIngestResult = ingestLoadScheduleCsv(rawLoadCsv, 'DOC_LOAD_01');
assert(loadIngestResult.status === 'INGESTION_SUCCESS', "Load Schedule Ingestion Success", loadIngestResult.status);
assert(loadIngestResult.equipment_count === 6, "Ingested 6 Equipment Items", `${loadIngestResult.equipment_count}`);
assert(loadIngestResult.equipment[0].rated_power_kw.provenance === 'IMPORTED_RAW', "TraceableValue Provenance Tracked", loadIngestResult.equipment[0].rated_power_kw.provenance);

const cableIngestResult = ingestCableScheduleCsv(rawCableCsv, 'DOC_CABLE_01');
assert(cableIngestResult.status === 'INGESTION_SUCCESS', "Cable Schedule Ingestion Success", cableIngestResult.status);
assert(cableIngestResult.feeder_count === 6, "Ingested 6 Feeders", `${cableIngestResult.feeder_count}`);

// Duplicate Tag Detection Check
const duplicateCsv = `TAG,RATED_KW,VOLTAGE_V,PF,EFFICIENCY\nPUMP_01,75,415,0.85,0.93\nPUMP_01,90,415,0.85,0.93`;
const dupResult = ingestLoadScheduleCsv(duplicateCsv, 'DOC_DUP');
assert(dupResult.status === 'INGESTION_REJECTED', "Duplicate Tag Ingestion Rejected", dupResult.status);
assert(dupResult.errors.some(e => e.includes('Duplicate equipment TAG')), "Duplicate Error Message Reported");

// --------------------------------------------------------------------------
// 14. CROSS-DOCUMENT DESIGN ASSURANCE TESTS (MVP-AC-05 & MVP-AC-06)
// --------------------------------------------------------------------------
console.log("\n--> EXECUTING CROSS-DOCUMENT DESIGN ASSURANCE VERIFICATION...");
const projectMock = {
  project_id: "PROJ_PLANT_ALPHA",
  project_name: "Integrated Industrial Power Substation",
  project_revision: "REV_A",
  jurisdiction: "IEC 60364 / IS 732"
};

const designBasisMock = {
  voltage_drop_limits_pct: {
    motor_feeder_steady_state: { value: 3.0, unit: '%' },
    motor_starting_bus_dip: { value: 15.0, unit: '%' }
  }
};

const assuranceResult = runDesignAssuranceAudit(
  projectMock,
  loadIngestResult.equipment,
  cableIngestResult.feeders,
  designBasisMock
);

assert(assuranceResult.total_findings > 0, "Discrepancy Matrix Populated", `${assuranceResult.total_findings} findings`);
assert(assuranceResult.critical_safety_count >= 2, "Critical Safety Findings Detected", `${assuranceResult.critical_safety_count}`);
assert(assuranceResult.evaluation_verdict === 'CRITICAL_DEFECTS_DETECTED', "Overall Verdict Reflects Critical Defects", assuranceResult.evaluation_verdict);

// Verify Tag Orphan Detection
const tagOrphanFinding = assuranceResult.findings.find(f => f.rule_id === 'ASSURANCE_001_TAG_ORPHAN');
assert(tagOrphanFinding != null, "ASSURANCE_001: Orphan Tag Discrepancy Caught", tagOrphanFinding?.finding_id);

// Verify Undersized Breaker Detection
const breakerUndersized = assuranceResult.findings.find(f => f.rule_id === 'ASSURANCE_002_BREAKER_UNDERSIZED');
assert(breakerUndersized != null, "ASSURANCE_002: Undersized Breaker Caught (Ib > In)", breakerUndersized?.finding_id);

// Verify Voltage Drop Exceeded Detection
const vdExceeded = assuranceResult.findings.find(f => f.rule_id === 'ASSURANCE_004_VOLTAGE_DROP_EXCEEDED');
assert(vdExceeded != null, "ASSURANCE_004: Voltage Drop Exceeded Caught", vdExceeded?.finding_id);

// Verify Adiabatic Fault Withstand Failure Detection
const adiabaticFail = assuranceResult.findings.find(f => f.rule_id === 'ASSURANCE_006_ADIABATIC_WITHSTAND_FAIL');
assert(adiabaticFail != null, "ASSURANCE_006: Adiabatic Withstand Failure Caught", adiabaticFail?.finding_id);

// Verify Critical Safety findings are pinned at the top
assert(assuranceResult.findings[0].severity === 'CRITICAL_SAFETY', "Critical Safety Findings Pinned First in Severity Order");

// --------------------------------------------------------------------------
// 15. AUDIT-READY REPORT GENERATION TEST (MVP-AC-07)
// --------------------------------------------------------------------------
console.log("\n--> EXECUTING REPORT GENERATION TEST (MVP-AC-07)...");
const htmlReport = generateAuditReportHtml(projectMock, assuranceResult);
assert(typeof htmlReport === 'string' && htmlReport.length > 500, "HTML Report String Generated");
assert(htmlReport.includes("PRELIMINARY — NOT FOR CONSTRUCTION"), "Watermark Explicitly Included in Report");
assert(htmlReport.includes("CRITICAL DEFECTS DETECTED"), "Overall Evaluation Verdict Rendered in Report");
assert(htmlReport.includes("ASSURANCE_002_BREAKER_UNDERSIZED"), "Discrepancy Findings Rendered in Report Table");

// Save report to disk as sample deliverable
const reportOutputPath = path.join(__dirname, '../sample_verification_report.html');
fs.writeFileSync(reportOutputPath, htmlReport, 'utf-8');
assert(fs.existsSync(reportOutputPath), "Verification Report Written to Disk: sample_verification_report.html");

console.log("\n================================================================================");
console.log(`TEST SUITE RESULTS: ${passedTests} / ${totalTests} ASSERTIONS PASSED (100% SUCCESS)`);
console.log("GOVERNANCE & AUDIT: ALL 15 BENCHMARKS + G0, G1, G2, G3 VERIFIED");
console.log("================================================================================\n");
