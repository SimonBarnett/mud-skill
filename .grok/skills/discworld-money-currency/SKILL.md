---
name: discworld-money-currency
description: >
  Discworld MUD money: AM dollars, Lancre coins, regional currencies, money
  changers, bank branches. Use when the user says DW currency, exchange AM to
  Lancre, money changer, or /discworld-money-currency.
  Does not stamp ready for human UAT.
---

# Discworld MUD — money and currency

Companion to `mud-skill` and `discworld-mud`. Shops and services use **local
currency** unless the game shows otherwise.

**Sources (link-out):**

- [Currency (wiki)](https://dwwiki.mooo.com/wiki/Currency)
- [Big table of coins](https://dwwiki.mooo.com/wiki/Currency/Big_Table_of_Coins)
- [Money changers (wiki)](https://dwwiki.mooo.com/wiki/Money_changer)
- [Changer rates sample](https://dwwiki.mooo.com/sined/general/changers.htm)
- In-game: `help currency` (public references)

## LOCKED — Major currency families

| Family | Used in (public wiki) | Notes |
|--------|----------------------|--------|
| **Ankh-Morpork (AM)** | AM, Sto Plains | Base unit often cited as **A$1 = 400 brass** (wichit bead scale) |
| **Lancre** | Ramtops, Uberwald (many towns) | **Base-12** coin ladder (farthing → hedgehog) |
| **Djelian** | Djelibeybi and related starts | Nationality doc ties several nations to Djelian |
| **Ephebian** | Ephebe / Il Drim starts | Omnian, Istanzian examples in nationality help |
| **Genuan** | Genua | Own Gc/Gl notation on changers |
| **Agatean (Bes Pelargic)** | Agatean empire | Harder to convert to AM per player guides |

AM coin ladder (wiki): penny, ten-pence, half-dollar, dollar, ten-dollar, royal,
crown (high denominations).

Lancre ladder (wiki): farthing, ha'penny, penny, tuppence, thruppence, sixpence,
shilling, crown, tencrown, sovereign, hedgehog.

## LOCKED — Paying and budgeting

1. Read prices in **room shop text** — compare weight and skill reqs before buy
   (`discworld-shop-*`).
2. Carry correct currency for the **city you are in**; foreign coins are useless
   until exchanged.
3. Ask human before large purchases or selling quest gear (`discworld-shop-pawn-trade`).

## LOCKED — Money changers

- NPC changers in many cities; player shops may host changers with **limited
  stock** of denominations (`list rates on changer`).
- Changers **buy/sell foreign vs local** — syntax varies by location (public
  examples: in AM `buy from lancre with dollars`; in Ohulan Cutash `sell dollars`).
- Wiki tables list AM locations e.g. **Street of Bookkeepers**, **Ankh Bridge**,
  **embassies** (Phedre Rd, Widdershins Broadway), and **Ohulan Cutash Lancre St**
  with sample spread percentages (rates **vary** — verify in game).

## LOCKED — Banks

- Some **bank branches** in different currency regions allow **deposit in one
  currency, withdraw in another** (wiki money changer page) — commission often
  low for AM / Lancre / Djelibeybi per player guides; Agatean/Genuan harder.

## UNKNOWN

- Live exchange spread on a given day — always `list rates` in room.
- Provincial obsolete coins — rare; one AM changer may still accept (pbworks note).

## Do not

- Invent exact A$ prices for items not shown in game text.
- Stamp ready for human UAT.
