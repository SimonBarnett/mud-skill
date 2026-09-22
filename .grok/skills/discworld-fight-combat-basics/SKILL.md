---
name: discworld-fight-combat-basics
description: >
  Discworld MUD fighting guide: combat flow, kill, loot gates. Use for combat basics, fight, kill NPC.
---

# Combat basics

Companion to `mud-skill` and `discworld-mud`. Surfaces: **fight, weapon** (issue #23).
Public facts only  - link-out [https://discworld.starturtle.net/](https://discworld.starturtle.net/) and [https://www.discworldmud.org/](https://www.discworldmud.org/).
Does not stamp ready for human UAT. No invented host, port, or credentials.

## LOCKED

- Use `kill` / combat verbs only with human OK for risky targets.
- Read `consider` output before attacking (see `discworld-fight-consider`).
- Loot only when rules and human allow; no unique quest item drops without OK.

## UNKNOWN

- Exact damage formulae  - not needed for playbooks.

## Agent playbook (#26)

1. LOCKED â€” Human OK before lethal fights; parse targets from game text.
2. LOCKED â€” Use `consider`, `wimpy`, `flee` as appropriate (sibling fight leaflets).
3. LOCKED â€” Improve fighting via TM + guild `advance` (`discworld-skills-experience`).
4. LOCKED â€” Newbie practice: Greg area when relevant (`discworld-fight-newbie-greg`).
5. UNKNOWN â€” Boss tactics â€” encounter-specific.

**Sources:** [https://discworld.starturtle.net/](https://discworld.starturtle.net/) combat help, [taskmaster](https://discworld.starturtle.net/lpc/playing/documentation.c?path=%2Fconcepts%2Ftaskmaster)
