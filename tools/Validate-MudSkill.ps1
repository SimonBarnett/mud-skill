# BT0 structure check for mud-skill.
$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $PSScriptRoot
function Require-File($rel) {
  $p = Join-Path $root $rel
  if (-not (Test-Path $p)) { Write-Error "Missing: $rel"; exit 1 }
}
Require-File ".grok\skills\mud-skill\SKILL.md"
Require-File ".grok\skills\discworld-mud\SKILL.md"
Require-File "docs\functional-spec.md"
Require-File "docs\feature-request-mud-skill-2026-09-22.md"
Require-File "docs\build-and-test-plan.md"
Require-File "docs\skill-harvest-log.md"
Require-File "tools\Install-MudSkill.ps1"
$mud = Get-Content (Join-Path $root ".grok\skills\mud-skill\SKILL.md") -Raw
foreach ($n in @("name: mud-skill", "ready for human UAT", "Discworld")) {
  if ($mud -notmatch [regex]::Escape($n)) { Write-Error "mud-skill missing: $n"; exit 1 }
}
$dw = Get-Content (Join-Path $root ".grok\skills\discworld-mud\SKILL.md") -Raw
foreach ($n in @("name: discworld-mud", "Warrior", "ready for human UAT")) {
  if ($dw -notmatch [regex]::Escape($n)) { Write-Error "discworld-mud missing: $n"; exit 1 }
}
Write-Output "Validate-MudSkill: OK"
exit 0