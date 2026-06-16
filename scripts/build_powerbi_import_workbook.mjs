import fs from "node:fs/promises";
import path from "node:path";
import { pathToFileURL } from "node:url";

// Este script convierte todos los CSV de data/processed en un unico Excel para Power BI.
// Importante: aqui NO se eligen las 12 tablas finales del dashboard; esa seleccion se hace
// en Power BI siguiendo docs/powerbi_montaje_y_medidas_choose_your_side.md.

// El paquete @oai/artifact-tool viene del runtime de Codex. Por eso el runner PowerShell
// configura NODE_PATH antes de ejecutar este script.
const nodeModuleDirs = (process.env.NODE_PATH ?? "")
  .split(path.delimiter)
  .filter(Boolean);
const artifactToolPath = path.join(
  nodeModuleDirs[0] ?? path.join(process.cwd(), "node_modules"),
  "@oai",
  "artifact-tool",
  "dist",
  "artifact_tool.mjs",
);
const { Workbook, SpreadsheetFile } = await import(pathToFileURL(artifactToolPath).href);

const projectRoot = process.cwd();
const processedDir = path.join(projectRoot, "data", "processed");
const outputPath = path.join(projectRoot, "powerbi", "starwars_powerbi_import.xlsx");

// Parser CSV pequeno y local para no depender de librerias externas.
// Respeta comillas dobles, comas dentro de campos y saltos de linea Windows.
function parseCsv(text) {
  const rows = [];
  let row = [];
  let cell = "";
  let inQuotes = false;

  for (let i = 0; i < text.length; i += 1) {
    const char = text[i];
    const next = text[i + 1];

    if (inQuotes) {
      if (char === '"' && next === '"') {
        cell += '"';
        i += 1;
      } else if (char === '"') {
        inQuotes = false;
      } else {
        cell += char;
      }
      continue;
    }

    if (char === '"') {
      inQuotes = true;
    } else if (char === ",") {
      row.push(cell);
      cell = "";
    } else if (char === "\n") {
      row.push(cell);
      rows.push(row);
      row = [];
      cell = "";
    } else if (char !== "\r") {
      cell += char;
    }
  }

  if (cell.length > 0 || row.length > 0) {
    row.push(cell);
    rows.push(row);
  }

  return rows;
}

// Power BI trabaja mejor si los numeros llegan como numeros y los vacios como null.
// Dejamos textos largos como texto para no romper claves o IDs.
function coerceValue(value) {
  if (value === "") return null;
  if (/^-?\d+(\.\d+)?$/.test(value) && value.length < 16) return Number(value);
  return value;
}

// Excel limita los nombres de hoja a 31 caracteres.
// Tambien acortamos prefijos repetitivos para que las hojas sean legibles en Power BI.
function sanitizeSheetName(filename, usedNames) {
  const base = filename
    .replace(/\.csv$/i, "")
    .replace(/^eda_/, "")
    .replace(/^universe_/, "u_")
    .replace(/_clean$/, "")
    .replace(/[^A-Za-z0-9_ ]/g, "_")
    .slice(0, 31);

  let name = base || "table";
  let counter = 2;
  while (usedNames.has(name)) {
    const suffix = `_${counter}`;
    name = `${base.slice(0, 31 - suffix.length)}${suffix}`;
    counter += 1;
  }
  usedNames.add(name);
  return name;
}

// Se incluyen todos los CSV procesados, ordenados alfabeticamente para que el Excel sea estable.
const files = (await fs.readdir(processedDir))
  .filter((file) => file.toLowerCase().endsWith(".csv"))
  .sort((a, b) => a.localeCompare(b));

const workbook = await Workbook.create();

// Primera hoja: indice del workbook. Sirve para saber que hoja viene de que CSV.
const indexSheet = workbook.worksheets.getOrAdd("README", {
  renameFirstIfOnlyNewSpreadsheet: true,
});

const usedNames = new Set(["README"]);
const indexRows = [
  ["Power BI import workbook"],
  ["Generated from", "data/processed"],
  ["CSV count", files.length],
  [],
  ["sheet_name", "source_csv", "rows", "columns"],
];

for (const file of files) {
  const csvPath = path.join(processedDir, file);
  const csvText = await fs.readFile(csvPath, "utf8");
  const parsed = parseCsv(csvText).map((row) => row.map(coerceValue));
  const sheetName = sanitizeSheetName(file, usedNames);
  const sheet = workbook.worksheets.add(sheetName);

  if (parsed.length > 0) {
    // A1 contiene cabeceras. Congelamos esa fila y la ponemos en negrita para navegar mejor.
    const dataRange = sheet.getRange("A1").write(parsed);
    sheet.freezePanes.freezeRows(1);
    sheet.getRange(`A1:${columnName(parsed[0].length)}1`).format.font.bold = true;
    dataRange.format.autofitColumns();
  }

  indexRows.push([sheetName, file, Math.max(parsed.length - 1, 0), parsed[0]?.length ?? 0]);
}

const indexRange = indexSheet.getRange("A1").write(indexRows);
indexSheet.getRange("A1:D5").format.font.bold = true;
indexSheet.freezePanes.freezeRows(5);
indexRange.format.autofitColumns();

// Sobrescribe el workbook de importacion que se usara como fuente en Power BI.
await fs.mkdir(path.dirname(outputPath), { recursive: true });
const output = await SpreadsheetFile.exportXlsx(workbook);
await output.save(outputPath);
await removeInspectArtifact(`${outputPath}.inspect.ndjson`);

console.log(outputPath);

// artifact-tool puede generar un fichero .inspect.ndjson auxiliar. No forma parte de la entrega.
async function removeInspectArtifact(inspectPath) {
  try {
    await fs.unlink(inspectPath);
  } catch (error) {
    if (error.code !== "ENOENT") {
      throw error;
    }
  }
}

// Convierte 1 -> A, 2 -> B, 27 -> AA para poder seleccionar el rango de cabeceras.
function columnName(index) {
  let name = "";
  let n = index;
  while (n > 0) {
    const remainder = (n - 1) % 26;
    name = String.fromCharCode(65 + remainder) + name;
    n = Math.floor((n - 1) / 26);
  }
  return name || "A";
}
