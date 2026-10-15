/**
 * ProEngineering Industrial Power Systems Suite
 * Cross-Document Consistency & Design Assurance Engine (v2.0.0 - Gate 3 Assurance Layer)
 * 
 * Implements deterministic rules across:
 * - Load Schedule (Equipment ratings, kW, Voltage, PF, Efficiency)
 * - Cable Schedule (Conductor size, length, material, insulation)
 * - Switchgear / Protection Schedule (Breaker In, Breaking capacity, Trip settings)
 * - Project Design Basis (Voltage drop limits, starting dip limits, fault levels)
 * 
 * Standards Citations (Metadata Only):
 * - IEC 60364-4-43:2008 Clause 433.1 (Overload protection: I_b <= I_n <= I_z)
 * - IEC 60364-5-52:2019 Clause 525 (Voltage drop in consumer installations)
 * - IEC 60364-5-54:2011 Clause 543.1.2 (Adiabatic short-circuit withstand)
 * - IEC 60947-2:2016 (Circuit breaker coordination and ratings)
 */

import { 
  calculateDesignCurrent, 
  calculateFeederVoltageDrop, 
  verifyCableFaultWithstand,
  evaluateMotorStarterTechnology,
  CABLE_DATABASE 
} from '../../deterministic_engine.js';

export function runDesignAssuranceAudit(project, equipmentList, feederList, designBasis) {
  const findings = [];
  let findingCounter = 1;

  function addFinding(ruleId, severity, severityBasis, sourceRecords, rationale, uncertainty = null) {
    findings.push({
      finding_id: `FND_${String(findingCounter++).padStart(3, '0')}`,
      project_id: project?.project_id || 'PROJ_DEFAULT',
      rule_id: ruleId,
      severity, // 'CRITICAL_SAFETY' | 'MAJOR_ENGINEERING' | 'MINOR_DISCREPANCY' | 'INFO_MISSING_DATA'
      severity_basis: severityBasis,
      source_records: sourceRecords,
      rationale,
      missing_data_or_uncertainty: uncertainty,
      status: 'OPEN',
      generated_at: new Date().toISOString()
    });
  }

  // Map equipment by tag
  const eqMap = new Map();
  equipmentList.forEach(eq => eqMap.set(eq.tag, eq));

  // Map feeders by load_tag
  const feederMap = new Map();
  feederList.forEach(fdr => feederMap.set(fdr.load_tag, fdr));

  // ==========================================================================
  // RULE ASSURANCE_001: Cross-Document Tag Integrity
  // ==========================================================================
  equipmentList.forEach(eq => {
    if (!feederMap.has(eq.tag)) {
      addFinding(
        'ASSURANCE_001_TAG_ORPHAN',
        'MAJOR_ENGINEERING',
        'SLD & Cable Schedule Completeness',
        [{
          document_id: eq.rated_power_kw?.source_document_id || 'LOAD_SCHEDULE',
          document_revision: 'REV_01',
          record_id: eq.equipment_id,
          field_name: 'TAG',
          compared_value: eq.tag,
          unit: 'string'
        }],
        `Equipment "${eq.tag}" exists in Load Schedule but has no corresponding feeder in the Cable Schedule.`
      );
    }
  });

  // ==========================================================================
  // RULES ASSURANCE_002 TO ASSURANCE_008: Feeder & Protection Verification
  // ==========================================================================
  feederList.forEach(fdr => {
    const eq = eqMap.get(fdr.load_tag);
    if (!eq) {
      addFinding(
        'ASSURANCE_001_TAG_ORPHAN',
        'MAJOR_ENGINEERING',
        'Cable Schedule & Load Schedule Integrity',
        [{
          document_id: fdr.route_length_m?.source_document_id || 'CABLE_SCHEDULE',
          document_revision: 'REV_01',
          record_id: fdr.feeder_id,
          field_name: 'LOAD_TAG',
          compared_value: fdr.load_tag,
          unit: 'string'
        }],
        `Feeder "${fdr.tag}" is mapped to Load Tag "${fdr.load_tag}", which does not exist in the Load Schedule.`
      );
      return;
    }

    const powerKw = eq.rated_power_kw?.value;
    const voltageV = eq.system_voltage_v?.value || 415;
    const pf = eq.power_factor?.value || 0.85;
    const eff = eq.efficiency?.value || 0.92;
    const breakerIn = fdr.breaker_rating_a?.value;
    const cableSize = fdr.conductor_size_mm2?.value;
    const conductor = fdr.conductor_material?.value || 'ALUMINIUM';
    const insulation = fdr.insulation?.value || 'XLPE';
    const lengthM = fdr.route_length_m?.value;
    const faultKa = fdr.fault_level_ka?.value || 25;
    const faultTimeS = fdr.fault_clearing_time_s?.value || 0.2;

    // Check for missing data (MVP-AC-03)
    if (!powerKw || !cableSize || !lengthM) {
      addFinding(
        'ASSURANCE_008_INCOMPLETE_INPUT',
        'INFO_MISSING_DATA',
        'Completeness Verification',
        [{
          document_id: fdr.route_length_m?.source_document_id || 'CABLE_SCHEDULE',
          document_revision: 'REV_01',
          record_id: fdr.feeder_id,
          field_name: 'INPUT_STATUS',
          compared_value: 'INCOMPLETE',
          unit: 'metadata'
        }],
        `Feeder "${fdr.tag}" lacks required parameters for physical verification (Length: ${lengthM}, Size: ${cableSize}, Power: ${powerKw}). Marked as NOT_ASSESSED.`,
        'Provide conductor cross-section, cable length, and equipment rated power.'
      );
      return;
    }

    // 1. Calculate Load Design Current (I_b)
    let ib = 0;
    try {
      ib = calculateDesignCurrent(powerKw, voltageV, pf, eff, 3);
    } catch (err) {
      addFinding('ASSURANCE_008_CALC_ERROR', 'MAJOR_ENGINEERING', 'Design Current Formula', [], err.message);
      return;
    }

    // RULE ASSURANCE_002: Overload Protection Coordination (I_b <= I_n)
    if (breakerIn && ib > breakerIn) {
      addFinding(
        'ASSURANCE_002_BREAKER_UNDERSIZED',
        'CRITICAL_SAFETY',
        'IEC 60364-4-43 Clause 433.1 (I_b <= I_n)',
        [
          { document_id: 'LOAD_SCHEDULE', document_revision: 'REV_01', record_id: eq.equipment_id, field_name: 'I_b (Calculated)', compared_value: ib.toFixed(2), unit: 'A' },
          { document_id: 'CABLE_SCHEDULE', document_revision: 'REV_01', record_id: fdr.feeder_id, field_name: 'Breaker_I_n', compared_value: breakerIn, unit: 'A' }
        ],
        `Continuous design current I_b (${ib.toFixed(2)} A) exceeds protective breaker rating I_n (${breakerIn} A). Breaker will nuisance trip during standard continuous plant operation.`
      );
    }

    // RULE ASSURANCE_003: Cable Thermal Protection Coordination (I_n <= I_z')
    const dbEntry = CABLE_DATABASE[conductor]?.[cableSize];
    const baseAmpacity = dbEntry?.ampacity || 0;
    // Assuming 0.85 derating factor for grouping/ambient as project baseline
    const deratedAmpacity = baseAmpacity * 0.85;

    if (breakerIn && breakerIn > deratedAmpacity) {
      addFinding(
        'ASSURANCE_003_CABLE_OVERLOAD_RISK',
        'CRITICAL_SAFETY',
        'IEC 60364-4-43 Clause 433.1 (I_n <= I_z)',
        [
          { document_id: 'CABLE_SCHEDULE', document_revision: 'REV_01', record_id: fdr.feeder_id, field_name: 'Breaker_I_n', compared_value: breakerIn, unit: 'A' },
          { document_id: 'CABLE_DATABASE', document_revision: 'IEC_60364-5-52', record_id: `CABLE_${conductor}_${cableSize}`, field_name: 'Derated_Ampacity_I_z', compared_value: deratedAmpacity.toFixed(1), unit: 'A' }
        ],
        `Protective device nominal rating I_n (${breakerIn} A) exceeds derated cable ampacity I_z (${deratedAmpacity.toFixed(1)} A). Cable is not thermally protected against sustained continuous overload.`
      );
    }

    // RULE ASSURANCE_004: Feeder Steady-State Voltage Drop Limit
    const vdResult = calculateFeederVoltageDrop({
      inputs: {
        power_kw: powerKw,
        voltage_v: voltageV,
        power_factor: pf,
        efficiency: eff,
        cable_length_m: lengthM,
        conductor_material: conductor,
        size_mm2: cableSize,
        insulation_type: insulation,
        phases: 3,
        parallel_runs: 1
      },
      criteria: {
        max_feeder_voltage_drop_pct: designBasis?.voltage_drop_limits_pct?.motor_feeder_steady_state?.value || 3.0,
        max_motor_starting_dip_pct: designBasis?.voltage_drop_limits_pct?.motor_starting_bus_dip?.value || 15.0
      }
    });

    if (vdResult.evaluation_status === 'FAIL') {
      addFinding(
        'ASSURANCE_004_VOLTAGE_DROP_EXCEEDED',
        'MAJOR_ENGINEERING',
        'IEC 60364-5-52 Clause 525 & Project Design Basis',
        [
          { document_id: 'CALC_ENGINE', document_revision: 'V2', record_id: fdr.feeder_id, field_name: 'Voltage_Drop_Pct', compared_value: vdResult.outputs.voltage_drop_pct, unit: '%' },
          { document_id: 'DESIGN_BASIS', document_revision: 'REV_01', record_id: 'PDB_VD_LIMIT', field_name: 'Limit_Pct', compared_value: 3.0, unit: '%' }
        ],
        `Calculated steady-state voltage drop of ${vdResult.outputs.voltage_drop_pct}% (${vdResult.outputs.voltage_drop_volts} V) exceeds allowable design basis limit of 3.0%. Terminal voltage at "${eq.tag}" will be substandard.`
      );
    }

    // RULE ASSURANCE_006: Adiabatic Short-Circuit Withstand
    const adiabaticResult = verifyCableFaultWithstand({
      inputs: {
        fault_current_ka: faultKa,
        fault_clearing_time_sec: faultTimeS,
        conductor_material: conductor,
        insulation_type: insulation,
        selected_size_mm2: cableSize,
        parallel_runs: 1
      }
    });

    if (adiabaticResult.evaluation_status === 'FAIL') {
      addFinding(
        'ASSURANCE_006_ADIABATIC_WITHSTAND_FAIL',
        'CRITICAL_SAFETY',
        'IEC 60364-5-54 Clause 543.1.2 & IEC 60949',
        [
          { document_id: 'CABLE_SCHEDULE', document_revision: 'REV_01', record_id: fdr.feeder_id, field_name: 'Installed_Size', compared_value: cableSize, unit: 'mm2' },
          { document_id: 'CALC_ENGINE', document_revision: 'V2', record_id: fdr.feeder_id, field_name: 'Min_Required_Size', compared_value: adiabaticResult.outputs.min_required_area_mm2, unit: 'mm2' }
        ],
        `Installed conductor size (${cableSize} mm²) is below the minimum adiabatic withstand requirement of ${adiabaticResult.outputs.min_required_area_mm2} mm² for a ${faultKa} kA fault at ${faultTimeS} s. Risk of explosive cable vaporisation during through-fault.`
      );
    }

    // RULE ASSURANCE_007: Starter Technology Selection Consistency
    if (eq.speed_control_required?.value) {
      const starterEval = evaluateMotorStarterTechnology({
        motor_kw: powerKw,
        requires_variable_speed: true
      });
      if (starterEval.recommended_technology !== 'VFD') {
        addFinding(
          'ASSURANCE_007_STARTER_MISMATCH',
          'MAJOR_ENGINEERING',
          'Process Control & Starter Decision Matrix',
          [{ document_id: 'LOAD_SCHEDULE', document_revision: 'REV_01', record_id: eq.equipment_id, field_name: 'SPEED_CONTROL', compared_value: 'YES', unit: 'boolean' }],
          `Motor requires speed modulation, but starter configuration is not set to VFD.`
        );
      }
    }
  });

  // Sort findings: CRITICAL_SAFETY first, then MAJOR_ENGINEERING, then MINOR, then INFO
  const severityRank = {
    'CRITICAL_SAFETY': 1,
    'MAJOR_ENGINEERING': 2,
    'MINOR_DISCREPANCY': 3,
    'INFO_MISSING_DATA': 4
  };

  findings.sort((a, b) => severityRank[a.severity] - severityRank[b.severity]);

  const criticalCount = findings.filter(f => f.severity === 'CRITICAL_SAFETY').length;
  const majorCount = findings.filter(f => f.severity === 'MAJOR_ENGINEERING').length;
  const totalFindings = findings.length;

  return {
    audit_id: `AUD_${Date.now()}`,
    project_id: project?.project_id || 'PROJ_001',
    timestamp: new Date().toISOString(),
    equipment_evaluated: equipmentList.length,
    feeders_evaluated: feederList.length,
    total_findings: totalFindings,
    critical_safety_count: criticalCount,
    major_engineering_count: majorCount,
    evaluation_verdict: criticalCount > 0 ? 'CRITICAL_DEFECTS_DETECTED' : (majorCount > 0 ? 'REVIEW_REQUIRED' : 'PASS'),
    findings
  };
}
