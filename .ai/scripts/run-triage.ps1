param([string[]]$Files, [string]$Prompt)
Write-Host "[Stub] run-triage.ps1 invoked." -ForegroundColor Yellow
if ($Files)  { Write-Host "Files: $($Files -join ', ')" }
if ($Prompt) { Write-Host "Prompt: $Prompt" }
# TODO: Replace with full triage implementation