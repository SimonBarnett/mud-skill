---
name: discworld-guild-wizard
description: >
  Discworld MUD Wizards' guild playbook leaflet.
  Does not stamp ready for human UAT.
---

# Wizards'

Companion to `mud-skill` and `discworld-mud`. Surfaces: **guild, fight, lore** (#23, #26 FIX).
No invented host, port, or credentials.

**Sources (link-out):**

- https://discworld.starturtle.net/lpc/playing/documentation.c?path=%2Fnewbie%2Fwizards_guild
- https://discworld.starturtle.net/
- https://dwwiki.mooo.com/wiki/Guilds

## LOCKED

1. LOCKED — Read in-game `/doc/newbie/wizards_guild` and guild help before join (starturtle URL above).
2. LOCKED — Human confirms guild join — resign is painful; load `discworld-mud` class table.
3. LOCKED — Train via `advance` in guild advance rooms and TM (`discworld-skills-experience`); ask before big XP spends.
4. LOCKED — Combat and theft default human-in-the-loop (`mud-skill` combat gate).
5. LOCKED — Spell slots, libraries, and UU themes (`discworld-location-am-unseen-university`).
6. LOCKED — Components via `components <spell>` help (`discworld-shop-magic-components`).
7. LOCKED — JPCT portals — wizard responsibility; `look enter portal` before use.

## UNKNOWN

- Optimal spell XP path — guild-specific; not in newbie doc summary.

## Do not

- Invent room ENAMEs or login details.
- Stamp ready for human UAT (Bob only).
