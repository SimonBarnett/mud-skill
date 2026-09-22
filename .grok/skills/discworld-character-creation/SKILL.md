---
name: discworld-character-creation
description: >
  Discworld MUD character creation: human-only, nationality, regions, stats,
  rearrange, newbie area, seven guilds. Use when the user says DW char create,
  nationality, Morporkian start, or /discworld-character-creation.
  Does not stamp ready for human UAT.
---

# Discworld MUD — character creation

Companion to `mud-skill`, `discworld-mud`, and `mud-character-creation`. Facts
from public docs only; verify live help in-game when rules change.

**Sources (link-out):**

- [Races (humans only)](https://discworld.starturtle.net/lpc/playing/documentation.c?path=%2Fconcepts%2Fraces)
- [Nationality and regions](https://discworld.starturtle.net/lpc/playing/documentation.c?path=%2Fconcepts%2Fnationality)
- [FAQ — guilds and travel overview](https://discworld.starturtle.net/lpc/playing/documentation.c?path=%2Fconcepts%2Ffaq)
- [rearrange (one-time stat edit)](https://discworld.starturtle.net/lpc/playing/documentation.c?path=%2Fhelpdir%2Frearrange)
- [Discworld MUD wiki](https://discworld.starturtle.net/)

## LOCKED — Species

- Playable characters are **human only** (public races doc). Elves and other
  species exist in lore but are not player races.

## LOCKED — Nationality (13 nations)

After the newbie area, everyone chooses a **nationality** (principle unchangeable).
It sets **starting language**, **accent**, **initial currency**, and **where you
enter the Disc**. Nations named in public nationality help include: Agatea,
Djelibeybi, Dreg, Ephebe, Genua, Howondaland, Istanzia, Klatch, Lancre, Morpork,
Omnia, Tsort, and Uberwald.

Each nation has one or more **regions**. Region choice affects **starting
location** (and godmother recall) but not language/money type for that nation.

Examples from public docs (not exhaustive):

| Nationality | Currency (start) | Language (fluent) | Start area pattern |
|-------------|------------------|-------------------|-------------------|
| Morporkian | Morporkian (AM) | Morporkian | Region-dependent (often AM-facing) |
| Lancrastian | Lancre | Morporkian | Region-dependent (Ramtops) |
| Uberwaldian | Lancre | Uberwaldean | Escrow (public doc) |
| Genuan | Genuan | Morporkian | Region-dependent |
| Djelian / Klatchian / Tsortian / Howondalandish | Djelian | Djelian | Djelibeybi area |
| Istanzian / Omnian | Ephebian | Ephebian | Il Drim area |

Human picks nationality with the human before committing — wrong currency region
complicates early shopping (`discworld-money-currency`).

## LOCKED — Stats and rearrange

- Constitution, dexterity, intelligence, strength, and wisdom affect skill
  bonuses; inspect with `score stats` (public newbie material).
- **`rearrange`** — **once per character life** you may set stats in range 8–23
  following in-game prompts. Public help advises playing first, then deciding.
- **Retrophrenologists** (NPCs) can move **one stat point at a time** for a fee
  after the one free rearrange.

## LOCKED — Newbie area → guild

1. Complete newbie orientation (game text). FAQ lists **seven working guilds**:
   warriors, thieves, wizards, witches, priests, assassins, fools.
2. Human confirms guild; load `discworld-guild-*` and class playbooks in
   `discworld-mud`. Witch join has public **female-only** rule — read guild help.
3. If spawn is **Ankh-Morpork**, run `discworld-ankh-survival` before shopping or
   cross-city travel.

## UNKNOWN

- Exact newbie-room command sequence and current guild join NPC rooms — follow
  signs and in-game `doc` / help only.
- Optimal nationality for a given guild build — player preference.

## Do not

- Invent recruiter room names or nationality bypass commands.
- Stamp ready for human UAT.
