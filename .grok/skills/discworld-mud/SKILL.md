---
name: discworld-mud
description: >
  Discworld MUD playbook companion for mud-skill: classes, guilds, newbie
  path, and game-specific rituals. Use when the user says Discworld MUD,
  DW, Ankh-Morpork, AM, guild, witch, wizard, thief, warrior, or
  /discworld-mud. Does not stamp ready for human UAT.
---

# Discworld MUD

Companion to `mud-skill`. Lore and class notes are stubs until harvested
from operator-approved sources (U2).

## Classes / guilds (stub)

| Guild | Notes |
|-------|-------|
| Warrior | UNKNOWN — expand P1 |
| Thief | UNKNOWN — expand P1 |
| Witch | UNKNOWN — expand P1 |
| Wizard | UNKNOWN — expand P1 |

## Newbie path (stub)

1. Confirm character + connection details from the human (do not invent).
2. If starting in **Ankh-Morpork**, load **`discworld-ankh-survival`** and run
   its first-10-minute ritual (lit streets, no alley wander, flee thieves).
3. Otherwise orient: whoami / score / inventory / exits.
4. Defer guild choice until human confirms.

## Warrior class playbook (stub)

Numbered steps only — expand in P1 after operator-approved harvest (U2).

1. LOCKED — Confirm with the human that the character is (or will be) Warrior
   guild; do not assume from the overview table alone.
2. UNKNOWN — Locate the guild master / training room from in-game directions
   once connected (no invented room names in this stub).
3. LOCKED — Run `skills` / guild-equivalent and record which combat skills are
   listed; ask the human before spending XP or learning new skills.
4. UNKNOWN — Follow companion `mud-skill` **Procedure: combat (stub)** for
   sparring or hunting; Warrior-specific tactics stay UNKNOWN until harvested.
5. LOCKED — Stop and ask the human before guild resign, weapon swap that drops
   a unique item, or any irreversible guild action.

## Do not

- Invent discworld host as LOCKED.
- Commit passwords.
- Stamp ready for human UAT.