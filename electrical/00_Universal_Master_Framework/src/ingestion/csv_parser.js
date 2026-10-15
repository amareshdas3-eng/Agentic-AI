/**
 * ProEngineering Industrial Power Systems Suite
 * Traceable CSV / Data Ingestion Parser (v2.0.0 - Gate 2 Ingestion Layer)
 * 
 * Enforces:
 * - MVP-AC-02: Traceable Ingestion with TraceableValue<T> provenance
 * - Duplicate equipment tag detection before commit
 * - Unit validation and normalization
 * - Missing field tagging (IMPORTED_RAW)
 */

/**
 * Parses raw CSV text into an array of objects
 */
export function parseCsvText(csvText) {
  if (!csvText || typeof csvText !== 'string') {
    throw new Error("Invalid CSV text: input must be a non-empty string.");
  }

  const lines = csvText.split(/\r?\n/).filter(line => line.trim().length > 0);
  if (lines.length < 2) {
    throw new Error("Invalid CSV content: header row and at least one data row required.");
  }

  const headers = lines[0].split(',').map(h => h.trim());
  const rows = [];

  for (let i = 1; i < lines.length; i++) {
    const rawCols = lines[i].split(',').map(c => c.trim());
    if (rawCols.length === 0 || (rawCols.length === 1 && rawCols[0] === '')) continue;
    
    const rowObj = { _row_number: i + 1 };
    headers.forEach((h, colIdx) => {
      rowObj[h] = rawCols[colIdx] !== undefined ? rawCols[colIdx] : '';
    });
    rows.push(rowObj);
  }

  return { headers, rows };
}

/**
 * Creates a TraceableValue object with provenance
 */
export function createTraceableValue(value, unit, provenance = 'IMPORTED_RAW', sourceDocId = 'LOAD_SCHEDULE_CSV', location = '') {
  return {
    value,
    unit,
    provenance,
    source_document_id: sourceDocId,
    source_location: location,
    imported_at: new Date().toISOString()
  };
}

/**
 * Ingests a raw Load Schedule CSV and normalizes it to Canonical Equipment objects
 */
export function ingestLoadScheduleCsv(csvText, documentId = 'DOC_LOAD_SCH_01') {
  const { headers, rows } = parseCsvText(csvText);
  const equipmentList = [];
  const tagSet = new Set();
  const errors = [];
  const warnings = [];

  rows.forEach(row => {
    const rowNum = row._row_number;
    const tag = row['TAG'] || row['EQUIPMENT_TAG'] || row['Tag'];

    if (!tag) {
      errors.push(`Row ${rowNum}: Missing equipment TAG identifier.`);
      return;
    }

    if (tagSet.has(tag)) {
      errors.push(`Row ${rowNum}: Duplicate equipment TAG detected: "${tag}". Tags must be unique within a project revision.`);
      return;
    }
    tagSet.add(tag);

    const powerKw = parseFloat(row['RATED_KW'] || row['KW'] || row['Power_kW']);
    const voltageV = parseFloat(row['VOLTAGE_V'] || row['VOLTS'] || row['Voltage_V']);
    const pf = parseFloat(row['PF'] || row['POWER_FACTOR'] || row['Cos_Phi']);
    const eff = parseFloat(row['EFFICIENCY'] || row['EFF'] || row['Eta']);
    const duty = row['DUTY'] || 'CONTINUOUS';
    const equipType = row['TYPE'] || 'MOTOR_LOAD';

    if (isNaN(powerKw) || powerKw <= 0) {
      warnings.push(`Row ${rowNum} (${tag}): Missing or invalid RATED_KW. Received: "${row['RATED_KW']}".`);
    }
    if (isNaN(voltageV) || voltageV <= 0) {
      warnings.push(`Row ${rowNum} (${tag}): Missing or invalid VOLTAGE_V. Received: "${row['VOLTAGE_V']}".`);
    }

    equipmentList.push({
      equipment_id: `EQ_${tag}`,
      tag,
      equipment_type: equipType,
      duty,
      system_voltage_v: createTraceableValue(isNaN(voltageV) ? null : voltageV, 'V', 'IMPORTED_RAW', documentId, `Row ${rowNum}`),
      rated_power_kw: createTraceableValue(isNaN(powerKw) ? null : powerKw, 'kW', 'IMPORTED_RAW', documentId, `Row ${rowNum}`),
      power_factor: createTraceableValue(isNaN(pf) ? null : pf, 'dimensionless', 'IMPORTED_RAW', documentId, `Row ${rowNum}`),
      efficiency: createTraceableValue(isNaN(eff) ? null : eff, 'dimensionless', 'IMPORTED_RAW', documentId, `Row ${rowNum}`),
      duty_cycle: createTraceableValue(duty, 'string', 'IMPORTED_RAW', documentId, `Row ${rowNum}`),
      speed_control_required: createTraceableValue(row['VFD_REQUIRED'] === 'YES' || row['SPEED_CONTROL'] === 'YES', 'boolean', 'IMPORTED_RAW', documentId, `Row ${rowNum}`)
    });
  });

  return {
    document_id: documentId,
    equipment_count: equipmentList.length,
    equipment: equipmentList,
    errors,
    warnings,
    status: errors.length > 0 ? 'INGESTION_REJECTED' : 'INGESTION_SUCCESS'
  };
}

/**
 * Ingests a raw Feeder/Cable Schedule CSV and maps to Canonical Feeder objects
 */
export function ingestCableScheduleCsv(csvText, documentId = 'DOC_CABLE_SCH_01') {
  const { headers, rows } = parseCsvText(csvText);
  const feeders = [];
  const tagSet = new Set();
  const errors = [];
  const warnings = [];

  rows.forEach(row => {
    const rowNum = row._row_number;
    const tag = row['FEEDER_TAG'] || row['TAG'] || row['Feeder_Tag'];

    if (!tag) {
      errors.push(`Row ${rowNum}: Missing FEEDER_TAG identifier.`);
      return;
    }

    if (tagSet.has(tag)) {
      errors.push(`Row ${rowNum}: Duplicate FEEDER_TAG detected: "${tag}".`);
      return;
    }
    tagSet.add(tag);

    const lengthM = parseFloat(row['LENGTH_M'] || row['LENGTH'] || row['Route_Length_m']);
    const sizeMm2 = parseFloat(row['SIZE_MM2'] || row['CONDUCTOR_SIZE'] || row['Size_mm2']);
    const conductor = (row['CONDUCTOR'] || row['MATERIAL'] || 'ALUMINIUM').toUpperCase();
    const insulation = (row['INSULATION'] || 'XLPE').toUpperCase();
    const breakerInA = parseFloat(row['BREAKER_IN_A'] || row['BREAKER_RATING_A'] || row['Breaker_In']);
    const faultCurrentKa = parseFloat(row['FAULT_KA'] || row['SHORT_CIRCUIT_KA']);
    const faultTimeS = parseFloat(row['FAULT_TIME_S'] || row['CLEARING_TIME_S'] || 0.2);

    if (isNaN(lengthM) || lengthM <= 0) {
      warnings.push(`Row ${rowNum} (${tag}): Incomplete feeder length. Received: "${row['LENGTH_M']}".`);
    }

    feeders.push({
      feeder_id: `FDR_${tag}`,
      tag,
      load_tag: row['LOAD_TAG'] || tag, // Handshake link to Equipment
      from_bus: row['FROM_BUS'] || 'MAIN_BUS_415V',
      route_length_m: createTraceableValue(isNaN(lengthM) ? null : lengthM, 'm', 'IMPORTED_RAW', documentId, `Row ${rowNum}`),
      conductor_material: createTraceableValue(conductor, 'string', 'IMPORTED_RAW', documentId, `Row ${rowNum}`),
      conductor_size_mm2: createTraceableValue(isNaN(sizeMm2) ? null : sizeMm2, 'mm2', 'IMPORTED_RAW', documentId, `Row ${rowNum}`),
      insulation: createTraceableValue(insulation, 'string', 'IMPORTED_RAW', documentId, `Row ${rowNum}`),
      breaker_rating_a: createTraceableValue(isNaN(breakerInA) ? null : breakerInA, 'A', 'IMPORTED_RAW', documentId, `Row ${rowNum}`),
      fault_level_ka: createTraceableValue(isNaN(faultCurrentKa) ? null : faultCurrentKa, 'kA', 'IMPORTED_RAW', documentId, `Row ${rowNum}`),
      fault_clearing_time_s: createTraceableValue(faultTimeS, 's', 'IMPORTED_RAW', documentId, `Row ${rowNum}`)
    });
  });

  return {
    document_id: documentId,
    feeder_count: feeders.length,
    feeders,
    errors,
    warnings,
    status: errors.length > 0 ? 'INGESTION_REJECTED' : 'INGESTION_SUCCESS'
  };
}
