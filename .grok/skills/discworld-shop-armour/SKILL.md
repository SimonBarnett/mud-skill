---
name: discworld-shop-armour
description: >
  Discworld MUD armour shops: Elm Street Forge, shields, vurdere, encumbrance.
  Use when the user says DW armour shop, buy breastplate AM, or
  /discworld-shop-armour.
  Does not stamp ready for human UAT.
---

# Armour shops

Companion to `mud-skill` and `discworld-weapon-armour-encumbrance`.
Surfaces: **shop, weapon, location** (#23, #26).

**Sources (link-out):**

- [Armours (wiki)](https://dwwiki.mooo.com/wiki/Armours)
- [Elm Street Forge](http://dwmud.pbworks.com/w/page/18434059/Elm%20Street%20Forge)
- [Tenth Egg armoury chain](https://dw.daftjunk.com/items/index.php?item=691&shop=73) (weapon emporium upstairs)
- [Discworld MUD wiki](https://discworld.starturtle.net/)

## LOCKED — Assessment

- **`vurdere`** assesses armour (wiki); **`judge`** for weapons — need
  `adventuring.evaluating.weapons` at 5+ for judge (wiki).
- Heavy armour increases **burden** — balance with weapon weight (`score`).

## LOCKED — Elm Street Forge (AM example)

Public price snapshot lists on same premises as weapons: metal/large shields,
breastplates (iron/steel), ringmail, bonemail, leather jacket, boots, gauntlets,
helms — prices in AM coin mix (pbworks listing). Location: **Elm Street west of
The Pitts**.

## LOCKED — Workflow

1. Buy armour in **local currency**.
2. `wear` / `equip`; re-`consider` tough targets after gear change.
3. Thieves often want **light** armour — guild help (`discworld-guild-thief`).
4. **Ug Ogg** custom armours (wiki category) — order workflow in-game; UNKNOWN
   pricing here.

## UNKNOWN

- Every shield vendor by city — confirm in destination city.
- Optimal vurdere sets per warrior spec — build-specific.

## Do not

- Stamp ready for human UAT.
