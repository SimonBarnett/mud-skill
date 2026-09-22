---
name: discworld-shop-general
description: >
  Discworld MUD general stores: food, drink, containers, sobriety, AM vs
  regional shops. Use when the user says DW general store, buy food AM, or
  /discworld-shop-general.
  Does not stamp ready for human UAT.
---

# General shops

Companion to `mud-skill` and `discworld-money-currency`.
Surfaces: **shop, location** (#23, #26).

**Sources (link-out):**

- [Discworld MUD wiki](https://discworld.starturtle.net/) — shop indexes
- [Kefka item DB](https://dw.daftjunk.com/items/index.php) — 800+ shops indexed
- Newbie docs on **sobriety** and Greg combat (`discworld-fight-newbie-greg`)

## LOCKED — What general stores sell

- **Food and drink** — restore HP/hunger cues; affect **sobriety** (matters for
  newbie combat training with Greg per public FAQ).
- **Containers** — bags, bottles; weight limits tie to encumbrance.
- **Misc supplies** — rope, lights, mundane tools per room stock (read descriptions).

## LOCKED — Agent workflow

1. Pay in **local currency** only.
2. `buy` quantities the human approves; keep emergency food before wilderness travel
   (`discworld-travel-transport`).
3. Do not `drop` unique containers with quest items inside.

## LOCKED — Finding shops

- No single LOCKED list of every general store name — use in-game exploration,
  wiki shop category, or Kefka DB search by city name.
- **Ankh-Morpork** has dense shop coverage along commercial streets (Tenth Egg,
  Elm, Treacle, etc.) — pair with `discworld-city-ankh-morpork` and
  `discworld-ankh-survival` for safe routing.

## UNKNOWN

- Exact ENAME of each food item — room text only.
- Best sobriety-safe drink before training — experiment or read item desc.

## Do not

- Invent shop names on a street not verified in game.
- Stamp ready for human UAT.
