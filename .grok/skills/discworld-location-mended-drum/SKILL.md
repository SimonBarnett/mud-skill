---
name: discworld-location-mended-drum
description: >
  Discworld MUD main bar of the Mended Drum: guest arrival, Hibiscus, brochure
  tray, menu prices, exits, landing sign, newspaper boxes. Use when the user says
  Mended Drum, brochure, Hibiscus, or /discworld-location-mended-drum.
  Does not stamp ready for human UAT.
---

# Mended Drum main bar

Companion to `mud-skill` and `discworld-ankh-survival`. Playtest issues #41, #57–#62, #65–#68. Guest `G` after `yes`.

## LOCKED

1. Guest `G` after `yes` arrives in the main bar of Ankh-Morpork's Mended Drum. Bar along the northeast. Pools of liquid, rubbish, tables, chairs, smoke. A tattered menu hangs above the bar.
2. Exit line: `There are four obvious exits: up, north, south and west.` North, south, west, and up are described below. `look` at an exit previews the next room and does not move you. Confirm with a bare `look` before you treat a preview as the room you are in.
3. Hibiscus Dunelm is standing at the bar. `look hibiscus`: Hibiscus Dunelm, the owner. Wide red face, pale nose. Wearing soft leather shoes, worn cotton trousers, a greasy white apron, and a white short-sleeved cotton shirt. In good shape, standing at the bar. Purse tinkling with coins. `ask hibiscus about the menu` → `What?` Do not lock a working ask.
4. Helpful street urchin. `look urchin`: a friendly looking street urchin that looks as if he knows his way around Ankh-Morpork. You could probably ask him how to get somewhere. He will probably give you directions. In good shape, standing, wearing a pair of grey worsted trousers and a ripped shirt. `ask urchin` returns `What?`. `ask urchin how to get to the warriors guild` returns `Try something else.` `ask urchin about the mended drum` → `That doesn't work.` Do not lock an ask sentence.
5. A peanut tray full of brochures is on the bar. A dart board is on a wall. The Green Slab box and an AM Daily box are beside the bar. `look dart board`: magical board, iconograph of a horrified face, nose as the bullseye, something written on it. `read dart board` prints "Top players by wins" and "Top players by average scores per game". Do not lock names or numbers. `look green slab` and `look am daily` return no match. `look box` is multiple matches. `look green slab box` and `look am daily box` are battered metal boxes with a door you could pull open and small white writing saying 5p, each holding a numbered edition. Do not pull the door. Do not buy. Do not lock the edition number.
6. `look menu`: it is a menu and appears to have something written on it. `read menu` shows prices. Shown: crisps 20p, a cheap cigarette 20p, boar scratchings 25p, a meat pie 62p, Morporkian Beer 10p, Soggy Mountain Dew 25p, Ankh Water 50p, Peach Corniche A$1, Classic Mead A$1, Fine Ale A$1.75, Brandy A$2.25, Amanita Liquor A$3.50, Ghlen Livid A$4, Ancient Scumble A$5, Ankhian Port A$12.50, Back Burner A$30, a glass of milk 50p. Do not buy. A new guest's purse contains only moths (`discworld-money-currency`).
7. `look tray`: the peanut tray is now a brochure dispenser. Newcomers are told to get a brochure. On the tray: a closed colourful brochure.
8. Brochure commands:

| Command | Result |
|---------|--------|
| `get brochure`, `read brochure`, `look colourful brochure` with nothing in hand | `Cannot find "...", no match.` |
| `get colourful brochure from tray` when the tray already holds several | `There are multiple matches for "colourful brochure". See "help parser" for more information on how to be more specific.` |
| `get 1st colourful brochure from tray` | `You get a closed colourful brochure from a peanut tray full of brochures.` Staff may print `A member of staff replenishes the supply of brochures.` |
| `get colourful brochure 1 from tray` when `look tray` shows one brochure | `You get a closed colourful brochure from a peanut tray full of brochures.` Staff may replenish first. |
| `get 2nd colourful brochure from tray` when the tray shows one brochure | `Cannot find "colourful brochure", no match.` Do not claim `2nd` fails when several brochures are still on the tray — that case was not retested. |
| `read brochure` while holding the closed brochure | `A closed colourful brochure does not have anything written on it.` |
| `open brochure` | `You open the colourful brochure to page 1.` |
| `read brochure` on the open brochure | Page one: Guild of Merchants welcome, badly printed, contents pointing at pages 2–6 (As thee Dysk spins (2), Thyngs you should know (3), Oure beutiful Citie (4), Gylds (5), Thee lands about the city (6)). A second `read brochure` stays on page one. |
| `read page 2 of brochure` | `Cannot find "page 2 of brochure", no match.` |

9. `turn brochure` with no page, brochure in hand and no other brochure in the room: `See "syntax turn" for the input patterns.`
10. `syntax turn` lists book forms: `turn <book> to [page] <number>`, `turn to page <number> {of|in} <book>`, `turn <number> pages {of|in} <book>`, `turn [a|1] page {of|in} <book>`, `turn to random page {of|in} <book>`, `turn <book> to random page`, plus turning yourself (`turn <around, [half] right, [half] left, rt, lt>`). Only the two specific-page forms in the table below were sent. Do not claim the other printed forms were used.
11. Tested page turns (brochure in hand, unambiguous):

| Command | Result |
|---------|--------|
| `turn brochure to page 2` | `You turn the colourful brochure to page 2.` |
| `turn my brochure to page 3` | `You turn the colourful brochure to page 3.` |
| `turn my brochure to page 4` | `You turn the colourful brochure to page 4.` |
| `turn my brochure to page 5` | `You turn the colourful brochure to page 5.` |
| `turn to page 6 in my brochure` | `You turn the colourful brochure to page 6.` |
| `turn my brochure to page 7` | `There are only six pages in the open colourful brochure.` then `The open colourful brochure is already open at page 6.` |

12. `read brochure` or `read my brochure` shows the current page and does not advance. Six pages were read. Keep page one as in item 8. Summarize later pages; do not freeze misspellings as match text.
    - Page 2: Great A'Tuin, four elephants, Terry Pratchett.
    - Page 3: ask an urchin for directions; talkers; rooms, objects, and people that provide their own help.
    - Page 4: a mapsmith on Losing Street, or an atlas; an advert for the Mended Drum, Number One Short Street.
    - Page 5: badly printed guild blurbs. Streets named there were not walked. Do not copy them into `discworld-guild-*`.
    - Page 6: the lands outside the city are dangerous. Good luck to wanderers.
13. Page 5 can pager (`return to continue`). Send one blank line. Do not send `h`. Same pager rule as `mud-skill`. Do not lock the `1 to 23 of 38` counts.
14. `look my brochure` while open: a cheerful little brochure, useful if you turn the pages, something written on it, open at the current page.
15. `drop brochure` while open: `You drop an open colourful brochure.` While closed: `You drop a closed colourful brochure.` A later guest can still see it on the floor. Bare `brochure` is then multiple matches for `open`, `read`, and `turn`. One `open brochure` may print the multiple-matches sentence twice; do not require the double print. `open my brochure` still opens the copy in hand. Prefer not to drop it.
16. `get open colourful brochure` → `You get an open colourful brochure from the bar of the Mended Drum.` `get closed colourful brochure` → `You get a closed colourful brochure from the bar of the Mended Drum.` Do not describe the floor line as permanent.
17. North from the main bar: `look north` is `It's just the north door.` / `It is closed.` `peer north` is `You peer around north.` No further text. Do not open the door.
18. South: entrance area of the Mended Drum. Staircase toward the streets. Exits: north, south, and northwest. Stren Withel, Hrun and the splatter were standing there on the preview and on the visit. `south` moves there. `north` returns to the main bar. Do not take south or northwest from the entrance.
19. West: preview only. Stage, shady corner, minor villains, exits southeast, east, and north. A bulletin board with notes (one look said 40). Do not enter it from this leaflet.
20. Up: first-floor landing, lamp, picture, one exit down, wooden sign. `up` moves there. `look sign`: wood, crudely nailed, something written on it. `read sign`: `Rooms no longer to rent due to repeated misuse!` `look picture`: the Broken Drum with its old owner standing outside. The owner does not look happy. `read picture`: `A picture does not have anything written on it.` `look lamp`: hangs from the ceiling on a thin metal chain, gold foil covered brass, old, a large candle, a couple of burnt moths. `down` prints `You carefully descend the stairs.` and returns to the main bar.
21. A small map and ANSI colour are printed with the room. Strip them before matching the exit line. Map art is not a direction list.

## UNKNOWN

- `turn <number> pages {of|in} <book>`, `turn [a|1] page {of|in} <book>`, `turn to random page {of|in} <book>`, `turn <book> to random page`, and turning yourself. Printed by syntax, not sent.
- How long a dropped brochure stays on the floor.
- Page 5 streets as real directions.
- What is beyond the closed north door.
- South and northwest from the entrance.
- The west stage (not entered). The bulletin board text.
- Pulling a newspaper door. Paying 5p.
- `here` on the tray. Whether `my` works on a get from the tray.
- Other people and a cat were sometimes present. Do not name them as targets.

## Do not

- Invent a disambiguator or a page-turn command past the lines above.
- Treat the unnumbered `get colourful brochure from tray` as reliable.
- Stamp ready for human UAT.
