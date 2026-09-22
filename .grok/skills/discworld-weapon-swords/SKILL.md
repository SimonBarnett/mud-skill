---
name: discworld-weapon-swords
description: >
  Discworld MUD swords and fencing skills.
  Does not stamp ready for human UAT.
---

# Swords

Companion to `mud-skill` and `discworld-mud`. Surfaces: **weapon, shop, fight** (#23, #26 FIX).
No invented host, port, or credentials.

**Sources (link-out):**

- https://dwwiki.mooo.com/wiki/Swords
- https://discworld.starturtle.net/lpc/playing/documentation.c?path=%2Fhelpdir%2Fjudge

## LOCKED

1. LOCKED — Sword family uses `fighting.melee.sword` / fencing subtree (wiki Swords).
2. LOCKED — Buy from named AM shops in `discworld-shop-weapons` (Tenth Egg, Treacle, Elm).
3. LOCKED — `judge` weapon quality needs `adventuring.evaluating.weapons` 5+ (weapons wiki).
4. LOCKED — Weight affects burden (`discworld-weapon-armour-encumbrance`).

## UNKNOWN

- Best sword per warrior spec — build-specific.

## Do not

- Invent room ENAMEs or login details.
- Stamp ready for human UAT (Bob only).
