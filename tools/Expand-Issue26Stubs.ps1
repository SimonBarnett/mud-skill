# One-off expansion for issue #26 — append playbook depth to short leaflets.
$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $PSScriptRoot
$wiki = "https://discworld.starturtle.net/"
$official = "https://www.discworldmud.org/"

function Get-AppendBlock($dirName) {
  if ($dirName -match '^discworld-city-') {
    $city = ($dirName -replace '^discworld-city-', '') -replace '-', ' '
    return @"

## Agent playbook (#26)

1. LOCKED — Confirm human intent and connection (``mud-skill``); pay in **local currency** (``discworld-money-currency``).
2. LOCKED — Reach $city using **carriages** or walking exits shown in game (``discworld-travel-transport``).
3. LOCKED — ``look`` each room; log exits — no invented ENAMEs.
4. LOCKED — Shops and guilds: verify NPC names in room text; see ``discworld-shop-*`` leaflets.
5. UNKNOWN — Live quest gates and NPC positions — session-specific.

**Sources:** [$wiki]($wiki), [Travel wiki](https://dwwiki.mooo.com/wiki/Travel)
"@
  }
  if ($dirName -match '^discworld-guild-') {
    $g = ($dirName -replace '^discworld-guild-', '')
    return @"

## Agent playbook (#26)

1. LOCKED — Human confirms guild join; read in-game ``/doc/newbie/${g}_guild`` or equivalent help on [$wiki]($wiki).
2. LOCKED — Class playbooks in ``discworld-mud`` for warrior/witch; others use this leaflet + game teachers.
3. LOCKED — Advance skills in guild rooms (``discworld-skills-experience``); ask before large ``advance`` spends.
4. LOCKED — Combat defaults human-in-the-loop (``mud-skill`` combat procedure).
5. UNKNOWN — Optimal primaries and quest gear — character-specific.

**Sources:** [$wiki]($wiki) guild docs, ``docs/skill-harvest-log.md``
"@
  }
  if ($dirName -match '^discworld-location-') {
    return @"

## Agent playbook (#26)

1. LOCKED — Pair with city leaflet (``discworld-city-*``) and ``discworld-ankh-survival`` if in AM.
2. LOCKED — Navigate by game exits only; note lit vs dark and one-way doors.
3. LOCKED — Before combat here, ``consider`` and set ``wimpy`` (``discworld-fight-*``).
4. LOCKED — Death risk: know corpse recovery (``discworld-death-recovery``).
5. UNKNOWN — Hidden exits and quest locks — discover in play.

**Sources:** [$wiki]($wiki) room/area pages
"@
  }
  if ($dirName -match '^discworld-fight-') {
    return @"

## Agent playbook (#26)

1. LOCKED — Human OK before lethal fights; parse targets from game text.
2. LOCKED — Use ``consider``, ``wimpy``, ``flee`` as appropriate (sibling fight leaflets).
3. LOCKED — Improve fighting via TM + guild ``advance`` (``discworld-skills-experience``).
4. LOCKED — Newbie practice: Greg area when relevant (``discworld-fight-newbie-greg``).
5. UNKNOWN — Boss tactics — encounter-specific.

**Sources:** [$wiki]($wiki) combat help, [taskmaster](https://discworld.starturtle.net/lpc/playing/documentation.c?path=%2Fconcepts%2Ftaskmaster)
"@
  }
  if ($dirName -match '^discworld-weapon-') {
    return @"

## Agent playbook (#26)

1. LOCKED — Buy weapons/armour from named shops (``discworld-shop-weapons``, ``discworld-shop-armour``).
2. LOCKED — Match weapon type to ``skills fighting`` tree; check burden (``discworld-weapon-armour-encumbrance``).
3. LOCKED — ``judge`` / ``vurdere`` when you have evaluating skills (wiki weapons/armour pages).
4. UNKNOWN — Best weapon for your spec — build-specific.

**Sources:** [Weapons wiki](https://dwwiki.mooo.com/wiki/Weapons), [Armours wiki](https://dwwiki.mooo.com/wiki/Armours)
"@
  }
  if ($dirName -match '^discworld-lore-') {
    return @"

## Agent playbook (#26)

1. LOCKED — Use lore for **tone and roleplay**, not invented puzzle solutions.
2. LOCKED — Mechanics (death, gods, races) — cross-check concept docs on [$wiki]($wiki).
3. LOCKED — Character creation facts: ``discworld-character-creation`` + ``discworld-lore-races-species``.
4. UNKNOWN — Quest spoilers — defer to in-game text.

**Sources:** [$wiki]($wiki), [$official]($official)
"@
  }
  return $null
}

$updated = 0
Get-ChildItem (Join-Path $root ".grok\skills\discworld-*\SKILL.md") | ForEach-Object {
  $raw = Get-Content $_.FullName -Raw
  if ($raw -match '## Agent playbook \(#26\)') { return }
  $lines = (Get-Content $_.FullName).Count
  if ($lines -ge 35) { return }
  $block = Get-AppendBlock $_.Directory.Name
  if (-not $block) { return }
  Add-Content -Path $_.FullName -Value $block -Encoding UTF8
  $updated++
}
Write-Output "Expand-Issue26Stubs: appended to $updated files"
