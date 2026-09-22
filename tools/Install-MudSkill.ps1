$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $PSScriptRoot
$skillsRoot = Join-Path $root ".grok\skills"
foreach ($skillMd in Get-ChildItem (Join-Path $skillsRoot "*\SKILL.md")) {
  $name = $skillMd.Directory.Name
  $dest = Join-Path $HOME ".grok\skills\$name"
  New-Item -ItemType Directory -Force -Path $dest | Out-Null
  Copy-Item -Force $skillMd.FullName (Join-Path $dest "SKILL.md")
  Write-Output "Installed $name -> $dest"
}
exit 0
