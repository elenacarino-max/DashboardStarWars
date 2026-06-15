param(
    [switch]$SkipWorkbook
)

$ErrorActionPreference = "Stop"

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$projectRoot = Split-Path -Parent $scriptDir
Set-Location $projectRoot

function Resolve-PythonCommand {
    $candidates = @()

    $python = Get-Command python -ErrorAction SilentlyContinue
    if ($python) {
        $candidates += ,@($python.Source)
    }

    $py = Get-Command py -ErrorAction SilentlyContinue
    if ($py) {
        $candidates += ,@($py.Source, "-3")
    }

    $bundledPython = Join-Path $env:USERPROFILE ".cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"
    if (Test-Path $bundledPython) {
        $candidates += ,@($bundledPython)
    }

    foreach ($candidate in $candidates) {
        $candidateExe = $candidate[0]
        $candidateArgs = @()
        if ($candidate.Count -gt 1) {
            $candidateArgs = $candidate[1..($candidate.Count - 1)]
        }

        & $candidateExe @candidateArgs -c "import pandas" *> $null
        if ($LASTEXITCODE -eq 0) {
            return ,$candidate
        }
    }

    throw "No se ha encontrado un Python valido con pandas. Instala Python 3.12 con requirements.txt o ejecuta desde Codex con su runtime empaquetado."
}

function Resolve-NodeCommand {
    $bundledNode = Join-Path $env:USERPROFILE ".cache\codex-runtimes\codex-primary-runtime\dependencies\node\bin\node.exe"
    if (Test-Path $bundledNode) {
        return $bundledNode
    }

    $node = Get-Command node -ErrorAction SilentlyContinue
    if ($node) {
        return $node.Source
    }

    throw "No se ha encontrado Node.js para regenerar el workbook."
}

$pythonCommand = Resolve-PythonCommand
$pythonExe = $pythonCommand[0]
$pythonArgs = @()
if ($pythonCommand.Count -gt 1) {
    $pythonArgs = $pythonCommand[1..($pythonCommand.Count - 1)]
}

Write-Host "Regenerando capa estrategica con Python: $($pythonCommand -join ' ')"
& $pythonExe @pythonArgs "scripts\build_rebellion_lab_outputs.py"

if (-not $SkipWorkbook) {
    $nodeExe = Resolve-NodeCommand
    $bundledNodeModules = Join-Path $env:USERPROFILE ".cache\codex-runtimes\codex-primary-runtime\dependencies\node\node_modules"
    if (Test-Path $bundledNodeModules) {
        $env:NODE_PATH = $bundledNodeModules
    }

    Write-Host "Regenerando workbook Power BI con Node: $nodeExe"
    & $nodeExe "scripts\build_powerbi_import_workbook.mjs"
}

Write-Host "Pipeline Rebellion Lab completado."
