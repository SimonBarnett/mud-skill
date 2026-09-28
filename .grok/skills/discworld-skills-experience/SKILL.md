---
name: discworld-skills-experience
description: >
  Discworld MUD skills and experience: taskmaster (TM), advance, teach/learn,
  cost, skill tree, hskills. Use when the user says DW XP, advance skill, TM,
  or /discworld-skills-experience.
  Does not stamp ready for human UAT.
---

# Discworld MUD — skills and experience

Companion to `mud-skill`, `discworld-fight-skills-advance`, and guild leaflets.

**Sources (link-out):**

- [Taskmaster](https://discworld.starturtle.net/lpc/playing/documentation.c?path=%2Fconcepts%2Ftaskmaster)
- [Advancing (concepts)](https://discworld.starturtle.net/lpc/playing/documentation.c?path=%2Fconcepts%2Fadvancing)
- [advance command](https://discworld.starturtle.net/lpc/playing/documentation.c?path=%2Fhelpdir%2Fadvance)
- [hskills](https://discworld.starturtle.net/lpc/playing/documentation.c?path=%2Fhelpdir%2Fhskills)
- Playtest issues #41, #65–#68, #78, #88 (new guest `score`)

## LOCKED — New guest score

Guests a few seconds old in the Mended Drum main bar, before any guild join, get, turn, or exit:

- Do not lock one hit-point, guild-point, or **experience** figure. Hit points were 497 (497), 498 (498), 500 (500), and 502 (502). Guild points were 50 (50) and later 6 (50). Experience was 6 on some guests and 15 on another (e.g. Fernkjpn `score` before leaving the bar, ten seconds old). Moteflmg showed experience 138 at 57 seconds old (issue #88). Motewqza: 171 at 36 seconds, 234 at 1 minute 18 seconds, and 401 at 3 minutes 6 seconds (#78). Motevqra: 60 at 41 seconds and 153 at 1 minute 44 seconds (#78). Experience on a new guest is not one constant and does not stay still in the first minutes.
- These matched: level 0 in the Adventurers' Guild, overall rating 0, died 0, wimpy 20%, unburdened (0%), quite comfortable, neutral, worshipping no god, no special abilities, logged in 1 time.
- Quest points `0 (776)`. Achievement points `0 (1529)`. Social points `50 (50)`.
- The "can die 7 times" clause is owned by `discworld-death-recovery`. Do not restate 7 as a universal cap.
- This is not an `advance` or taskmaster result. Do not spend experience from this section.

## LOCKED — New guest `skills` (roots only)

Before any guild, `skills` on Fernkjpn, Motewqza, and Motevqra matched (roots stayed at these zeros while experience rose on Motewqza and Motevqra; no guild join, `advance`, or taskmaster command was sent):

```
covert.............. 0 0
fighting............ 0 0
crafts.............. 0 -
magic............... 0 0
faith............... 0 0
```

The crafts bonus column was `-`, not `0`. Do not invent branches under these roots.

UNKNOWN — why guests of similar age show different experience (including Moteflmg 138 at 57s, Motewqza vs Motevqra). Why the number rises while root skills stay at 0. Why guild points were 50 and then 6. Taskmaster on a level 0 guest was not tried. Moteflmg `skills` was not sent.

## LOCKED — Three advancement paths (public advancing doc)

| Path | How | Agent note |
|------|-----|------------|
| **Taskmaster (TM)** | Practice skills in play — success or fail can grant a free level | TMs often **yellow** on colour terminals; check `hskills` |
| **Advance** | Spend **experience** (+ guild fee) in guild advance rooms | Use `cost` / `cost primaries` before bulk spend |
| **Teach / learn** | Players teach each other | XP cost; `advance` is ~⅔ cheaper than `teach` per player guides — prefer guild advance when in guild |

## LOCKED — Taskmaster behaviour

- Each activity has skill thresholds: below = fail often; above = always succeed;
  **between** = TM chance on attempts (examples: sneak, sword fight, broom flight,
  spells — public taskmaster doc).
- After a TM message, run **`hskills`** or **`hskills brief`** to see which skill moved.

## LOCKED — Advance command (guild rooms)

Works only in **guild advance areas** (obvious in game). Syntax examples from help:

- `advance fighting`
- `advance fighting by 2`
- `advance fighting to 6`
- Partial names expand (`fi.po` → `fighting.points`)

Skills form a **tree** (`fighting.melee.sword` etc.) — `skills` command shows branches.

## LOCKED — Human-in-the-loop

1. Ask before large **`advance`** spends or primaries push.
2. Quest XP rewards are spent via advance — do not grind irrelevant primaries
   without human OK.
3. Adventurers (non-guild) cannot `advance` — teach/learn economy only (public
   footnotes blog); most agents here assume guilded characters.

## UNKNOWN

- Per-guild primary caps and regional currency for advance fees — read guild help.
- Optimal TM grinding routes — character and guild specific.

## Do not

- Invent skill ENAMEs not shown in `skills` output.
- Stamp ready for human UAT.
