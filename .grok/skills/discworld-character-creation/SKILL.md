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

## LOCKED — Front door (guest, 2026-09-22)

After menu `G` the game showed, in order:

1. `Enter the name you wish to use:`
2. `How would you like your name capitalised? [Name]` — a blank line kept the suggested capitalisation.
3. `Should your character be male or female?` — the word `male` was accepted.
4. `Are you using a screenreader? [yes/no/help]` — `no` was accepted.
5. Terms and conditions, then `Please read the terms and conditions CAREFULLY! (You have time, we'll be back in 30 seconds)`. Send nothing during the wait.
6. After the wait the prompt is exactly: `Enter 'yes' if you agree to the terms or 'no' if you cannot.` then `By typing 'yes' you signify that you have read, understand and agree to be bound by these terms and conditions: [yes/no]`. Simon granted an exception (issue #38): send `yes` and proceed. Do not send `no`. See `mud-skill` front door.
7. If the game says `Sorry, someone is already trying to create a character of that name.` choose a different name or wait. Do not hammer the same name.
8. LOCKED — After `yes`: `You have never logged in before.`, saves, the `help rules` box, then `>` and `Queued command: look` before the room, then `chfn`, then `Inventory regeneration complete.` Do not send a command on that `>`. Follow the `mud-skill` front door. The first room on guest `G` was the main bar of the Mended Drum (`discworld-location-mended-drum`). Nationality was not asked before that room.
9. UNKNOWN — where menu `N` (new character) diverges from `G`. Do not claim every new Discworld character skips nationality.

Guest blurb shown before the name prompt (orientation only, not a command list): trouble goes to liaison domain or any creator; `liaisons` and `finger` are the commands named on that screen.

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
