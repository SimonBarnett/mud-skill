---
name: discworld-guild-wizard
description: >
  Discworld MUD wizard guild: spells, magic, university themes. Use for wizard guild, spells, unseen.
---

# Wizards' Guild

Companion to `mud-skill` and `discworld-mud`. Surfaces: **guild, lore, fight** (issue #23).
Public facts only  - link-out [https://discworld.starturtle.net/](https://discworld.starturtle.net/) and [https://www.discworldmud.org/](https://www.discworldmud.org/).
Does not stamp ready for human UAT. No invented host, port, or credentials.

## LOCKED

- Wizards use spell slots and guild libraries per public newbie wizard docs.
- Unseen University themes tie to Ankh-Morpork (`discworld-location-am-unseen-university`).
- Do not spam high-risk spells in city streets without human OK.

## UNKNOWN

- Spell progression costs and quest gates  - in-game.

## Agent playbook (#26)

1. LOCKED â€” Human confirms guild join; read in-game `/doc/newbie/wizard_guild` or equivalent help on [https://discworld.starturtle.net/](https://discworld.starturtle.net/).
2. LOCKED â€” Class playbooks in `discworld-mud` for warrior/witch; others use this leaflet + game teachers.
3. LOCKED â€” Advance skills in guild rooms (`discworld-skills-experience`); ask before large `advance` spends.
4. LOCKED â€” Combat defaults human-in-the-loop (`mud-skill` combat procedure).
5. UNKNOWN â€” Optimal primaries and quest gear â€” character-specific.

**Sources:** [https://discworld.starturtle.net/](https://discworld.starturtle.net/) guild docs, `docs/skill-harvest-log.md`
