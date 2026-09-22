# Build and test plan: mud-skill P0

## BT0 (structure)

- `tools/Validate-MudSkill.ps1` exits 0.
- Required files from functional-spec L1/L3/L8/L9 present.
- No secret-assignment patterns in docs/skills.

## BT1 (install)

- `tools/Install-MudSkill.ps1` copies `mud-skill`, `discworld-mud`, and `harvest-mud-skill` into `~/.grok/skills`.

## BT2 (content bar)

- Umbrella skill lists GATES or procedure for connect/nav/combat at stub level.
- Discworld companion names at least three classes/guilds as UNKNOWN or LOCKED stubs (no invented login).

## DoD

- PR against main with P0 files.
- BT0 green.
- Issue acceptance A1–A6 claimed with evidence in PR body.