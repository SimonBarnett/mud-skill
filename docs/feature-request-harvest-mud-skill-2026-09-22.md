# Feature request: harvest-mud-skill foundation

**Repo:** `SimonBarnett/mud-skill`  
**Date:** 2026-09-22  
**Source:** CAST IRON harvest (`agentic_build` skill `harvest-agent-skills` + `bob-spec-intake`): every skill product keeps a harvest skill as foundation.

## Intent / critique

| | |
|--|--|
| **Intent** | A dedicated harvest skill in this repo so MUD / Discworld playbooks learned in-session are written back here, not only under `~/.grok/skills`. |
| **Good** | SHA `1e6a497` bolted a CAST IRON paragraph onto `mud-skill` and noted the harvest log. |
| **Bad** | There is no `.grok/skills/harvest-mud-skill/SKILL.md`. Play skill and harvest skill are one file. |
| **Ugly** | `harvest-agent-skills` routes "MUD play / Discworld" to "that repo's harvest skill"; agents will not load a heading inside `mud-skill`. |

## Gap vs current tree

- Missing `.grok/skills/harvest-mud-skill/SKILL.md` (or `harvest-mud-skill` name).
- `Validate-MudSkill.ps1` / `Install-MudSkill.ps1` do not know a harvest skill.
- Not a red MUST on FR #1 (L1–L10 / A1–A6 / BT0–BT2). Adjacent hole.

## Ask (MUST)

1. Add `.grok/skills/harvest-mud-skill/SKILL.md` with YAML `name: harvest-mud-skill` and triggers (`harvest`, CAST IRON, `/harvest-mud-skill`, learn-then-harvest).
2. Procedure: edit `.grok/skills/` in this repo, note `docs/skill-harvest-log.md`, empty harvest = no commit. No secrets.
3. Point `mud-skill` CAST IRON section at this skill (do not duplicate the full harvest ritual).
4. Install copies `harvest-mud-skill` into `~/.grok/skills`. Validator requires the file.

## Out of scope

- Implementing Discworld lore (see Ankh survival FR).
- FR #1 required fixes.

## Acceptance

| ID | Criterion |
|----|-----------|
| H1 | `harvest-mud-skill` SKILL.md exists with triggers and empty-harvest rule. |
| H2 | Install copies it; validator fails if missing. |
| H3 | No `password=` / `XAI_API_KEY=` assignments. |

## Bob-job

Dispatch `bob-job-loop` on this issue after park. Separate worker from FR #1 FIX.
