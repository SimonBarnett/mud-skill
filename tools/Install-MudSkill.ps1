$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $PSScriptRoot
foreach ($name in @("mud-skill", "discworld-mud", "discworld-ankh-survival")) {
  $src = Join-Path $root ".grok\skills\$name"
  $dest = Join-Path $HOME ".grok\skills\$name"
  New-Item -ItemType Directory -Force -Path $dest | Out-Null
  Copy-Item -Force (Join-Path $src "SKILL.md") (Join-Path $dest "SKILL.md")
  Write-Output "Installed $name -> $dest"
}
exit 0