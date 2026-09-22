---
name: discworld-guild-witch
description: >
  Discworld MUD witch guild: herbs, headology, flying. Use for witch guild, female character join rules.
---

# Witches' Guild

Companion to `mud-skill` and `discworld-mud`. Surfaces: **guild, lore, fight** (issue #23).
Public facts only  - link-out [https://discworld.starturtle.net/](https://discworld.starturtle.net/) and [https://www.discworldmud.org/](https://www.discworldmud.org/).
Does not stamp ready for human UAT. No invented host, port, or credentials.

## LOCKED

- Witch magic is herbs, cursing, flying, headology  - not wizard slots (public witches_guild doc).
- Public guild description: female characters only for join.
- See expanded steps in `discworld-mud` witch playbook.

## UNKNOWN

- Coven and mentor routes  - harvest per character.

## Agent playbook (#26)

1. LOCKED â€” Human confirms guild join; read in-game `/doc/newbie/witch_guild` or equivalent help on [https://discworld.starturtle.net/](https://discworld.starturtle.net/).
2. LOCKED â€” Class playbooks in `discworld-mud` for warrior/witch; others use this leaflet + game teachers.
3. LOCKED â€” Advance skills in guild rooms (`discworld-skills-experience`); ask before large `advance` spends.
4. LOCKED â€” Combat defaults human-in-the-loop (`mud-skill` combat procedure).
5. UNKNOWN â€” Optimal primaries and quest gear â€” character-specific.

**Sources:** [https://discworld.starturtle.net/](https://discworld.starturtle.net/) guild docs, `docs/skill-harvest-log.md`
