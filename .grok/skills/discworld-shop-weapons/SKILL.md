---
name: discworld-shop-weapons
description: >
  Discworld MUD weapon shops: Ankh-Morpork locations (Tenth Egg, Treacle, Elm),
  buying workflow. Use when the user says DW weapon shop, buy sword AM, or
  /discworld-shop-weapons.
  Does not stamp ready for human UAT.
---

# Weapon shops

Companion to `mud-skill`, `discworld-mud`, and `discworld-money-currency`.
Surfaces: **shop, weapon, location** (issues #23, #26).

**Sources (link-out):**

- [Weapons (wiki mechanics)](https://dwwiki.mooo.com/wiki/Weapons)
- [Kefka DB — high quality emporium](https://dw.daftjunk.com/items/index.php?item=691&shop=73)
- [Kefka DB — Kernab's](https://dw.daftjunk.com/items/index.php?item=340&shop=42)
- [Elm Street Forge (pbworks snapshot)](http://dwmud.pbworks.com/w/page/18434059/Elm%20Street%20Forge)
- [Discworld MUD wiki](https://discworld.starturtle.net/)

## LOCKED — Buying ritual

1. Confirm **local currency** (`discworld-money-currency`).
2. `look` shop NPC/sign; buy only items **listed in room** with shown prices.
3. Compare **weight** and skill requirements (`judge` / `vurdere` need evaluating
   skills per wiki).
4. Human OK before expensive or unique weapons (e.g. fine sabre tier).

## LOCKED — Ankh-Morpork examples (public databases)

| Shop (public name) | Location (public text) | Stock notes |
|--------------------|------------------------|-------------|
| High quality weapon emporium | Up from armoury, **west half Tenth Egg Street** | Fixed stock: bastard sword, cutlass, daggers, axes, maces, spears, etc. (A$ and p prices in DB) |
| **Kernab's weaponry store** | **Treacle Street**, west of Dragon's Landing | Adds rapiers, stilettos, two-handed axe/sword, fine sabre (high A$) |
| **Elm Street Forge** | **Elm Street**, west of The Pitts | Mixed weapons + armour (see `discworld-shop-armour`) |

## LOCKED — Other cities

- Weapon vendors exist in other hubs (Lancre, BP, etc.) — **UNKNOWN** per-city list
  here; use in-game `look` or wiki city pages when travelling.

## UNKNOWN

- Live stock counts and sale discounts — room text only.
- Quest-only weapons — wiki quest weapons page; do not spoil steps.

## Do not

- Invent shop ENAMEs or directions not in game output.
- Stamp ready for human UAT.
