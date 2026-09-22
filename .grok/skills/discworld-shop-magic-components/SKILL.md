---
name: discworld-shop-magic-components
description: >
  Discworld MUD magic components: Tarnach's, Alchemists' Guild, components command.
  Use when the user says DW spell components, Tarnach, wizard supplies AM, or
  /discworld-shop-magic-components.
  Does not stamp ready for human UAT.
---

# Magic and component shops

Companion to `discworld-guild-wizard`, `discworld-guild-witch`, and `discworld-mud`.
Surfaces: **shop, guild, lore** (#23, #26 FIX).

**Sources (link-out):**

- [Tarnach's Quality Consumables (wiki)](https://dwwiki.mooo.com/wiki/Tarnach%27s_Quality_Consumables)
- [components command](https://discworld.starturtle.net/lpc/playing/documentation.c?path=%2Fhelpdir%2Fcomponents)
- [Category: Spell components](https://dwwiki.mooo.com/wiki/Components)
- [Alchemists' Guild supply shop (Kefka)](https://dw.daftjunk.com/items/index.php?item=3465&shop=544)
- [Making money — Tarnach job note](https://dwwiki.mooo.com/wiki/Making_money)

## LOCKED — Named shops

| Shop | Location (public text) | Stock notes |
|------|------------------------|-------------|
| **Tarnach's Quality Consumables** | **Magical Emporium**, **Sator Square**, Ankh-Morpork — north-east corner, **second level** (go east, up, northeast from emporium entrance per wiki) | Player-maintained component shop: candles, carrots, feathers, eyes, sap, torches, pebbles, purple mineral powder, etc. (wiki stocked list) |
| **Guild of Alchemists' supply shop** | **Alchemists' Guild**, **Street of Alchemists**, Ankh-Morpork | Sap, sulphur, purple mineral nugget, mandrake jar, lab gear (Kefka shop 544) |

## LOCKED — Casting workflow

1. `components for <spell>` — lists required items (helpdir components); must know spell.
2. Component pouch identification for casting from pouches.
3. Witches use herbs/`gather` plus shops (`discworld-mud` witch playbook) — different economy from wizard slots.
4. Human OK before bulk purchases or illegal reagent farming.

## LOCKED — Ramtops note

- **Magic and Meddlers' Shop** in **House of Magic**, Creel Springs (Lancre) — wiki lists carrots, mineral nuggets, etc.; non-wizards need climbing gear/skills to reach upper shop.

## UNKNOWN

- Live Tarnach player-shop stock — varies with player restocking (wiki warns list is not comprehensive).
- Every herb shop for witches outside AM/Lancre — harvest per trip.

## Do not

- Invent component ENAMEs not shown in `components` output.
- Stamp ready for human UAT.
