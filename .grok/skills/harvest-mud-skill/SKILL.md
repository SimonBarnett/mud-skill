---
name: harvest-mud-skill
description: >
  Promote MUD and Discworld playbooks learned in-session into this repo's
  .grok/skills (SimonBarnett/mud-skill). Use when you learn a repeatable
  procedure while playing or documenting MUD work, or the user says harvest,
  CAST IRON, skill harvest, learn-then-harvest, harvest mud skill, harvest
  Discworld playbook, or /harvest-mud-skill. Does not stamp ready for human UAT.
---

# Harvest mud-skill

Remote: `https://github.com/SimonBarnett/mud-skill` (`origin/main`). Local clone on fleet boxes under `C:\ai\mud-skill*` or operator path.

## CAST IRON (Simon 2026-09-22)

**If you learn something new about MUD play or Discworld, harvest it here.**
Learned playbooks come back to this repo as a feature request.
Do not leave a playbook only in `~/.grok/skills`. Do not wait for an hourly task.

Route facts to the right skill file:

| Playbook | Owner skill |
|----------|-------------|
| Generic connect / navigate / combat gates | `mud-skill` |
| Discworld classes, guilds (overview) | `discworld-mud` |
| Ankh-Morpork survival rituals | `discworld-ankh-survival` |
| City / region travel and hubs | `discworld-city-*` |
| Streets, dungeons, landmarks | `discworld-location-*` |
| Mended Drum main bar | `discworld-location-mended-drum` |
| Guild-specific facts (beyond class playbook here) | `discworld-guild-*` |
| Combat commands and training | `discworld-fight-*` |
| Weapons, armour, burden | `discworld-weapon-*` |
| Buying, selling, components | `discworld-shop-*` |
| Canon and roleplay tone | `discworld-lore-*` |
| Character creation (any MUD) | `mud-character-creation`, `discworld-character-creation`, `achaea-character-creation` |
| Death recovery mechanics | `discworld-death-recovery` |
| Currency and changers | `discworld-money-currency` |
| Carriages, portals, travel | `discworld-travel-transport` |
| Taskmaster, advance, XP | `discworld-skills-experience` |
| Harvest ritual itself | this file |

Fleet-wide CAST IRON routing table: `SimonBarnett/agentic_build` skill `harvest-agent-skills`.

**During the job, not later.** If this session learned a repeatable procedure (trigger, owner skill, hard rule), edit `.grok/skills/*/SKILL.md` in this repo now, append a short dated note to `docs/skill-harvest-log.md`, then commit on a worker branch and open a PR. Do not push `main`. Do not merge.

**Empty harvest: no git commit.** No useful new procedure → stop; do not commit "nothing found".

**Useful harvest:** add or update `SKILL.md`, note in `docs/skill-harvest-log.md`, commit, push the work branch, open PR.

## Scan

1. `~\.grok\skills\mud-skill`, `discworld-mud`, and session notes vs repo `.grok\skills\*`.
2. Recent `docs/*` and uncommitted playbooks in the mud-skill clone.
3. Existing skills — do not duplicate; extend the owner skill or link to it.

A candidate is useful only if it is **repeatable**, has a clear trigger, and is not a single incident report.

## Write

Follow one home per fact (umbrella vs Discworld companion). Frontmatter `name` + `description` with triggers. ASCII in SKILL.md.

After edits, run `tools/Validate-MudSkill.ps1`. Install with `tools/Install-MudSkill.ps1` copies all project skills into `~\.grok\skills`.

Append a short dated section to `docs/skill-harvest-log.md` (what changed and why).

## Do not

- Commit empty harvests or "nothing found".
- Force-push, secrets, or credential assignments in git.
- Invent lore or login details not shown in game text or operator-approved harvest.
- Stamp ready for human UAT (Bob only).
- Confuse this repo with `MUD-AI` (separate product).
