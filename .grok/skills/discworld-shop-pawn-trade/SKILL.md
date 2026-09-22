---
name: discworld-shop-pawn-trade
description: >
  Discworld MUD pawn, reclaim, fences, and selling loot.
  Use when the user says DW pawn, Follatt Biraten, reclaim receipt, or
  /discworld-shop-pawn-trade.
  Does not stamp ready for human UAT.
---

# Pawn and trade

Companion to `mud-skill` and `discworld-guild-thief`.
Surfaces: **shop** (#23, #26 FIX).

**Sources (link-out):**

- [Pawn shop room help](https://discworld.starturtle.net/lpc/playing/documentation.c?path=%2Froom%2Fpawn_shop)
- [Fence command](http://discworld.atuin.net/lpc/playing/documentation.c?path=%2Fknown_command%2Ffence)
- [Making money — fences vs general stores](https://dwwiki.mooo.com/wiki/Making_money)
- [Quow NPC record — Follatt Biraten](https://quow.co.uk/cow.php?a=npc&n=1_Follatt+Biraten&s=Georgio)
- [Player DB example — long sword at Follatt Biraten's pawn shop](https://git.atr0phy.net/binaryatrocity/discworld-tintin/src/branch/master) (item index text)

## LOCKED — Pawn shop (named example)

| Shop | Location | Evidence |
|------|----------|----------|
| **Follatt Biraten's pawn shop** | **Ankh-Morpork** (public DB lists shop name; **street not in Kefka/Quow harvest**) | Quow NPC location string; TinTin DB lists items (e.g. long sword A$3) sold there |

**Pawn workflow** (pawn_shop help):

1. `pawn <item>` — receive cash + **Pawned Item Receipt** (do not lose receipt).
2. `reclaim receipt` at the **same** shop before expiry; pay loan + ~20% fee (shown in shop).
3. Expired stock appears for `list` / `browse` / `buy` — pawn shops do not `sell` buy from players.

## LOCKED — Fences (thief economy)

- NPC **fence** command — better prices than general stores for many items (`/doc/known_command/fence`).
- Some fences publish **wanted items** lists (thief-only visibility per help).
- Human OK before fencing stolen-from-player loot.

## LOCKED — General resale

- **Caveat Emptorium**, **Trotters Lane** — junk/bric-a-brac fixed stock (Kefka shop 728); buy oddments, not a pawn mechanic.
- Compare fence vs general store when not in a hurry (`Making money` wiki).

## UNKNOWN

- **Street address** for Follatt Biraten's — searched Kefka index + Quow; only shop name + city locked (gap cite above).
- Every pawn shop on Disc — pawn_shop help is generic; additional cities not harvested.

## Do not

- Sell quest/unique gear without human check.
- Stamp ready for human UAT.
