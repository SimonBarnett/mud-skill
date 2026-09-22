---
name: discworld-city-lancre
description: >
  Discworld MUD city and region guide for Lancre and the Ramtops: location, lore, witch themes. Use for Lancre, Ramtops.
---

# Lancre and Ramtops (city guide)

Companion to `mud-skill` and `discworld-mud`. Surfaces: **city, location, lore** (issue #23).
Public facts only  - link-out [https://discworld.starturtle.net/](https://discworld.starturtle.net/) and [https://www.discworldmud.org/](https://www.discworldmud.org/).
Does not stamp ready for human UAT. No invented host, port, or credentials.

## LOCKED

- Lancre region ties to witch and countryside themes from public Discworld MUD docs.
- Travel between areas follows in-game exits and conveyance shown to the player.
- Human-in-the-loop before long wilderness hunts.

## UNKNOWN

- Exact guildhouses and shop names  - read from game.

## Agent playbook (#26)

1. LOCKED â€” Confirm human intent and connection (`mud-skill`); pay in **local currency** (`discworld-money-currency`).
2. LOCKED â€” Reach lancre using **carriages** or walking exits shown in game (`discworld-travel-transport`).
3. LOCKED â€” `look` each room; log exits â€” no invented ENAMEs.
4. LOCKED â€” Shops and guilds: verify NPC names in room text; see `discworld-shop-*` leaflets.
5. UNKNOWN â€” Live quest gates and NPC positions â€” session-specific.

**Sources:** [https://discworld.starturtle.net/](https://discworld.starturtle.net/), [Travel wiki](https://dwwiki.mooo.com/wiki/Travel)
