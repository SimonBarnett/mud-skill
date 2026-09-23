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
- Playtest issue #41 (guest purse and Drum menu)

## LOCKED — New guest purse (playtest 2026-09-22)

1. A new guest's inventory says `Your purse contains only moths.` Do not buy. Do not assume starting coins.
2. `read menu` in the Mended Drum main bar priced items in `p` and `A$` together. The full shown list is also in `discworld-location-mended-drum`. Do not add prices that were not printed.
3. Shown list: crisps 20p, a cheap cigarette 20p, boar scratchings 25p, a meat pie 62p, Morporkian Beer 10p, Soggy Mountain Dew 25p, Ankh Water 50p, Peach Corniche A$1, Classic Mead A$1, Fine Ale A$1.75, Brandy A$2.25, Amanita Liquor A$3.50, Ghlen Livid A$4, Ancient Scumble A$5, Ankhian Port A$12.50, Back Burner A$30, a glass of milk 50p.

UNKNOWN — how moths relate to the brass or dollar ladder. Changer use was not tried.

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
