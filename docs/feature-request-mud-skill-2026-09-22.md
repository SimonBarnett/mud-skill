# Feature request: mud-skill P0 pack

**Repo:** `SimonBarnett/mud-skill`  
**Date:** 2026-09-22  
**Source:** Simon `#bobiverse` — MUD-Skill; harvest MUD + Discworld skills; new public repo; functional spec; bob-job it.

## Intent / critique

| | |
|--|--|
| **Intent** | One skill home so agents can play MUDs, starting with Discworld classes/game rituals. |
| **Good** | Clear separation from `MUD-AI` (game) vs skills (playbooks). |
| **Bad** | Empty tree until P0 — no playbooks yet. |
| **Ugly** | Ad-hoc Discord lore dumps without skill triggers or acceptance. |

## Ask (MUST)

Implement P0 from `docs/functional-spec.md` (L1–L10, A1–A6). Seed:

1. `.grok/skills/mud-skill/SKILL.md` — umbrella MUD play skill.
2. `.grok/skills/discworld-mud/SKILL.md` — Discworld-specific companion (classes/guilds stub ok).
3. `tools/Validate-MudSkill.ps1` + `tools/Install-MudSkill.ps1`.
4. `docs/skill-harvest-log.md` seed entry.
5. Prefer `.github/workflows/bt0.yml`.

## Out of scope

- Full telnet client product (U1).
- Replacing `SimonBarnett/MUD-AI`.
- Real credentials.

## Bob-job

Dispatch `bob-job-loop` / `Start-BobBuildLoop` on this issue after park.