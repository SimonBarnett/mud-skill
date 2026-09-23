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
- Playtest issue #41 (new guest `score`)

## LOCKED — New guest score

Two looks on different guests, both a few seconds old, before any guild join:

- Do not lock one hit-point or guild-point figure. Hit points were 497 (497) and 498 (498). Guild points were 50 (50) and later 6 (50).
- These matched: experience 6, level 0 in the Adventurers' Guild, overall rating 0, died 0, wimpy 20%, unburdened (0%), quite comfortable, neutral, worshipping no god, no special abilities, logged in 1 time.
- Quest points `0 (776)`. Achievement points `0 (1529)`. Social points `50 (50)`.
- The "can die 7 times" clause is owned by `discworld-death-recovery`. Do not restate 7 as a universal cap.
- This is not an `advance` or taskmaster result. Do not spend experience from this section.

UNKNOWN — why guild points were 50 and then 6. Taskmaster on a level 0 guest was not tried.

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
