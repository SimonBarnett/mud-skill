# BT0 structure check for mud-skill.
$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $PSScriptRoot
function Require-File($rel) {
  $p = Join-Path $root $rel
  if (-not (Test-Path $p)) { Write-Error "Missing: $rel"; exit 1 }
}
Require-File ".grok\skills\mud-skill\SKILL.md"
Require-File ".grok\skills\discworld-mud\SKILL.md"
Require-File ".grok\skills\harvest-mud-skill\SKILL.md"
Require-File ".grok\skills\harvest-agent-skills\SKILL.md"
Require-File "docs\functional-spec.md"
Require-File "docs\feature-request-mud-skill-2026-09-22.md"
Require-File "docs\build-and-test-plan.md"
Require-File "docs\feature-request-mud-much-deeper-2026-09-22.md"
Require-File "docs\build-and-test-plan-mud-much-deeper-2026-09-22.md"
Require-File "docs\skill-harvest-log.md"
Require-File "tools\Install-MudSkill.ps1"
$skillFiles = Get-ChildItem (Join-Path $root ".grok\skills\*\SKILL.md")
if ($skillFiles.Count -lt 50) {
  Write-Error "Need at least 50 SKILL.md under .grok/skills (found $($skillFiles.Count))"
  exit 1
}
$surfaceBlob = ($skillFiles | ForEach-Object { Get-Content $_.FullName -Raw }) -join "`n"
foreach ($pat in @("location", "shop", "lore", "fight", "weapon", "guild", "city")) {
  if ($surfaceBlob -notmatch $pat) { Write-Error "Skill pack missing surface keyword: $pat"; exit 1 }
}
Require-File ".grok\skills\discworld-ankh-survival\SKILL.md"
$mud = Get-Content (Join-Path $root ".grok\skills\mud-skill\SKILL.md") -Raw
foreach ($n in @("name: mud-skill", "ready for human UAT", "Discworld")) {
  if ($mud -notmatch [regex]::Escape($n)) { Write-Error "mud-skill missing: $n"; exit 1 }
}
$dw = Get-Content (Join-Path $root ".grok\skills\discworld-mud\SKILL.md") -Raw
foreach ($n in @("name: discworld-mud", "Warrior", "ready for human UAT")) {
  if ($dw -notmatch [regex]::Escape($n)) { Write-Error "discworld-mud missing: $n"; exit 1 }
}
$harvest = Get-Content (Join-Path $root ".grok\skills\harvest-mud-skill\SKILL.md") -Raw
foreach ($n in @("name: harvest-mud-skill", "Empty harvest", "/harvest-mud-skill")) {
  if ($harvest -notmatch [regex]::Escape($n)) { Write-Error "harvest-mud-skill missing: $n"; exit 1 }
}
$foundation = Get-Content (Join-Path $root ".grok\skills\harvest-agent-skills\SKILL.md") -Raw
foreach ($n in @("name: harvest-agent-skills", "github: https://github.com/SimonBarnett/mud-skill", "/harvest-agent-skills")) {
  if ($foundation -notmatch [regex]::Escape($n)) { Write-Error "harvest-agent-skills missing: $n"; exit 1 }
}
Write-Output "Validate-MudSkill: OK"
exit 0
