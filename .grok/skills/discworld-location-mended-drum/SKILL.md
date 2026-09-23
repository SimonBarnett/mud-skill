---
name: discworld-location-mended-drum
description: >
  Discworld MUD main bar of the Mended Drum: guest arrival, Hibiscus, brochure
  tray, menu prices. Use when the user says Mended Drum, brochure, Hibiscus, or
  /discworld-location-mended-drum.
  Does not stamp ready for human UAT.
---

# Mended Drum main bar

Companion to `mud-skill` and `discworld-ankh-survival`. Playtest issue #41. Guest `G` after `yes`.

## LOCKED

1. Guest `G` after `yes` arrives in the main bar of Ankh-Morpork's Mended Drum. Bar along the northeast. Pools of liquid, rubbish, tables, chairs, smoke. A tattered menu hangs above the bar.
2. Exit line: `There are four obvious exits: up, north, south and west.` Do not say where they lead.
3. Hibiscus Dunelm is standing at the bar.
4. Helpful street urchin. `look urchin`: a friendly looking street urchin that looks as if he knows his way around Ankh-Morpork. You could probably ask him how to get somewhere. He will probably give you directions. In good shape, standing, wearing a pair of grey worsted trousers and a ripped shirt. `ask urchin` returns `What?`. `ask urchin how to get to the warriors guild` returns `Try something else.` Do not lock an ask sentence.
5. A peanut tray full of brochures is on the bar. A dart board is on a wall. The Green Slab box and an AM Daily box are beside the bar.
6. `look menu`: it is a menu and appears to have something written on it. `read menu` shows prices. Shown: crisps 20p, a cheap cigarette 20p, boar scratchings 25p, a meat pie 62p, Morporkian Beer 10p, Soggy Mountain Dew 25p, Ankh Water 50p, Peach Corniche A$1, Classic Mead A$1, Fine Ale A$1.75, Brandy A$2.25, Amanita Liquor A$3.50, Ghlen Livid A$4, Ancient Scumble A$5, Ankhian Port A$12.50, Back Burner A$30, a glass of milk 50p. Do not buy. A new guest's purse contains only moths (`discworld-money-currency`).
7. `look tray`: the peanut tray is now a brochure dispenser. Newcomers are told to get a brochure. On the tray: a closed colourful brochure.
8. Command results:

| Command | Result |
|---------|--------|
| `get brochure`, `read brochure`, `look colourful brochure` with nothing in hand | `Cannot find "...", no match.` |
| `get colourful brochure from tray` | Once: `You get a closed colourful brochure from a peanut tray full of brochures.` Staff replenish the tray. |
| same command later | `There are multiple matches for "colourful brochure". See "help parser"...` |
| `read brochure` while holding the closed brochure | `A closed colourful brochure does not have anything written on it.` |

9. A small map and ANSI colour are printed with the room. Strip them before matching the exit line. Map art is not a direction list.

## UNKNOWN

- Where the four exits lead.
- `help parser`. A `get` that works when several brochures match.
- `open` while holding the brochure. What an opened brochure says.
- Hibiscus, the dart board, The Green Slab box, the AM Daily box. Not examined.
- Other people and a cat were sometimes present. Do not name them as targets.

## Do not

- Invent a disambiguator or an open/read sequence past the lines above.
- Stamp ready for human UAT.
