---
name: discworld-shop-pawn-trade
description: >
  Discworld MUD pawn, trade, and fencing loot: sell mundane gear, thief fences.
  Use when the user says DW pawn, fence loot, sell sword, or
  /discworld-shop-pawn-trade.
  Does not stamp ready for human UAT.
---

# Pawn and trade

Companion to `mud-skill` and `discworld-guild-thief`.
Surfaces: **shop** (#23, #26).

**Sources (link-out):**

- [Discworld MUD wiki](https://discworld.starturtle.net/) — trade/pawn topics
- Thief guild newbie material (legal fencing themes)
- [Kefka item DB](https://dw.daftjunk.com/items/index.php) — pawn shop entries

## LOCKED — Selling mundane loot

1. Identify **pawn / general trader** NPCs from room text in the current city.
2. `sell` only items the human confirms are **non-quest, non-unique**.
3. Prices vary by city and shop — compare before selling high-value gear.
4. Currency paid is **local**; exchange later if needed (`discworld-money-currency`).

## LOCKED — Thieves' Guild fencing

- Stolen goods and guild rules use **game-identified fences** (public thief
  orientation) — illegal theft from players needs human approval (`mud-skill` combat gate).
- Do not fence items flagged unique in `look` or quest journals.

## LOCKED — Player trade

- Direct `give` / trade with players — human-in-the-loop; no scamming unique items.
- Player shops may host **money changers** with limited float (wiki).

## UNKNOWN

- Best sell price route for a given item — economy shifts; check multiple buyers.

## Do not

- Sell corpses' quest items without human explicit OK.
- Stamp ready for human UAT.
