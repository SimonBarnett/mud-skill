---
name: discworld-fight-wimpy-flee
description: >
  Discworld MUD fighting guide: wimpy, flee, survival in combat.
---

# Wimpy and flee

Companion to `mud-skill` and `discworld-mud`. Surfaces: **fight** (issue #23).
Public facts only  - link-out [https://discworld.starturtle.net/](https://discworld.starturtle.net/) and [https://www.discworldmud.org/](https://www.discworldmud.org/).
Does not stamp ready for human UAT. No invented host, port, or credentials.

## LOCKED

- Set `wimpy` to auto-flee at low HP (public combat help).
- `flee` toward known safe exits; in AM prefer lit streets (`discworld-ankh-survival`).
- Stop combat if game shows illegality (guards, divine smite).

## UNKNOWN

- Optimal wimpy thresholds  - tune per character.

## Agent playbook (#26)

1. LOCKED â€” Human OK before lethal fights; parse targets from game text.
2. LOCKED â€” Use `consider`, `wimpy`, `flee` as appropriate (sibling fight leaflets).
3. LOCKED â€” Improve fighting via TM + guild `advance` (`discworld-skills-experience`).
4. LOCKED â€” Newbie practice: Greg area when relevant (`discworld-fight-newbie-greg`).
5. UNKNOWN â€” Boss tactics â€” encounter-specific.

**Sources:** [https://discworld.starturtle.net/](https://discworld.starturtle.net/) combat help, [taskmaster](https://discworld.starturtle.net/lpc/playing/documentation.c?path=%2Fconcepts%2Ftaskmaster)
