---
name: discworld-guild-priest
description: >
  Discworld MUD Priests' guild playbook leaflet.
  Does not stamp ready for human UAT.
---

# Priests'

Companion to `mud-skill` and `discworld-mud`. Surfaces: **guild, fight, lore** (#23, #26 FIX).
No invented host, port, or credentials.

**Sources (link-out):**

- https://discworld.starturtle.net/lpc/playing/documentation.c?path=%2Fnewbie%2Fpriests_guild
- https://discworld.starturtle.net/
- https://dwwiki.mooo.com/wiki/Guilds

## LOCKED

1. LOCKED — Read in-game `/doc/newbie/priests_guild` and guild help before join (starturtle URL above).
2. LOCKED — Human confirms guild join — resign is painful; load `discworld-mud` class table.
3. LOCKED — Train via `advance` in guild advance rooms and TM (`discworld-skills-experience`); ask before big XP spends.
4. LOCKED — Combat and theft default human-in-the-loop (`mud-skill` combat gate).
5. LOCKED — **Patron deity** choice is major — human must pick before join (priests_guild doc).
6. LOCKED — Faith points, rituals, and `rituals` help govern spells (`discworld-lore-gods-patrons`).
7. LOCKED — Divine Hand travel for priests (`discworld-travel-transport`).

## UNKNOWN

- Per-god spell trees — deity-specific in-game help only.

## Do not

- Invent room ENAMEs or login details.
- Stamp ready for human UAT (Bob only).
