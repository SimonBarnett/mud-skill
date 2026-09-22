---
name: discworld-shop-general
description: >
  Discworld MUD general stores and grocers: food, containers, sobriety.
  Use when the user says DW general store, buy food AM, Grog's Groceries, or
  /discworld-shop-general.
  Does not stamp ready for human UAT.
---

# General shops

Companion to `mud-skill` and `discworld-money-currency`.
Surfaces: **shop, location** (#23, #26 FIX).

**Sources (link-out):**

- [Grog's Groceries (Kefka DB)](https://dw.daftjunk.com/items/index.php?item=162&shop=21)
- [Fresh Fruit on Baker (Kefka DB)](https://dw.daftjunk.com/items/index.php?item=162&shop=21)
- [Corn on the cob — purchase locations](https://dw.daftjunk.com/items/index.php?item=158)
- [Goth mudder AM shop A–Z](http://gothmudders.com/maps/atoz.htm)
- [Making money — general stores](https://dwwiki.mooo.com/wiki/Making_money)

## LOCKED — Named shops (Ankh-Morpork)

| Shop (public name) | Location (public text) | Notes |
|--------------------|------------------------|--------|
| **Grog's Groceries** | **Middle of Fast Lane**, Ankh-Morpork | Groceries: corn, carrots, apples, cabbage, potatoes, cheese, buns, ham (Kefka shop 21 / item location text) |
| **Fresh Fruit on Baker** | **Baker Street**, near God Street intersection | Fruit and veg price list on Kefka (carrots, melons, etc.) |
| **Holbrook's General Shop** | Grid **A7** on public AM map index | Listed under General Shops (atoz.htm) |
| **Elm Street General Shop** | Grid **B6** (atoz.htm) | General store class — verify stock in room |

## LOCKED — Workflow

1. Pay in **AM dollars** (or local currency) shown on price tags.
2. Food/drink affects **sobriety** — relevant before Greg training (`discworld-fight-newbie-greg`).
3. `buy` only what human approves; keep travel rations before carriages (`discworld-travel-transport`).
4. General stores buy loot for less than fences — `discworld-shop-pawn-trade` / Making money wiki.

## UNKNOWN

- Live stock counts — room text only.
- Other cities' general stores — use Kefka city filter; not tabulated here.

## Do not

- Invent shop ENAMEs off-map.
- Stamp ready for human UAT.
