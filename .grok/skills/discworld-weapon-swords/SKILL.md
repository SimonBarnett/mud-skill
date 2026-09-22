---
name: discworld-weapon-swords
description: >
  Discworld MUD weapon guide: swords and fencing skills, shops.
---

# Swords

Companion to `mud-skill` and `discworld-mud`. Surfaces: **weapon, shop, fight** (issue #23).
Public facts only  - link-out [https://discworld.starturtle.net/](https://discworld.starturtle.net/) and [https://www.discworldmud.org/](https://www.discworldmud.org/).
Does not stamp ready for human UAT. No invented host, port, or credentials.

## LOCKED

- Sword-family weapons use sword/fencing skills (public weapon help).
- Buy from weapon shops identified in game (`discworld-shop-weapons`).
- Weight affects combat  - check encumbrance (`discworld-weapon-armour-encumbrance`).

## UNKNOWN

- Best sword per spec  - character build.

## Agent playbook (#26)

1. LOCKED â€” Buy weapons/armour from named shops (`discworld-shop-weapons`, `discworld-shop-armour`).
2. LOCKED â€” Match weapon type to `skills fighting` tree; check burden (`discworld-weapon-armour-encumbrance`).
3. LOCKED â€” `judge` / `vurdere` when you have evaluating skills (wiki weapons/armour pages).
4. UNKNOWN â€” Best weapon for your spec â€” build-specific.

**Sources:** [Weapons wiki](https://dwwiki.mooo.com/wiki/Weapons), [Armours wiki](https://dwwiki.mooo.com/wiki/Armours)
