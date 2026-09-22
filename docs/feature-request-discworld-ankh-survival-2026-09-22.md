# Feature request: Discworld Ankh survival playbooks

**Repo:** `SimonBarnett/mud-skill`  
**Date:** 2026-09-22  
**Source:** https://github.com/SimonBarnett/mud-skill/issues/3 — agent dies in Ankh-Morpork inside 10 minutes; harvest real play details.

## Intent / critique

| | |
|--|--|
| **Intent** | Give a Discworld-playing agent enough harvested playbooks to stay alive in Ankh-Morpork (streets, NPCs, newbie combat, guild choice) instead of dying in minutes. |
| **Good** | P0 already has `discworld-mud` + four guild name stubs and a three-line newbie path. |
| **Bad** | Stubs are `UNKNOWN — expand P1` only. No Ankh map ritual, no combat loop, no remaining guilds (Priests, Assassins, Fools), no harvested commands. |
| **Ugly** | Issue #3 has no intake doc and no `feature-request` label until this park. |

## Gap vs current tree (SHA 1e6a497 / origin/main P0)

- `.grok/skills/discworld-mud/SKILL.md` names Warrior / Thief / Witch / Wizard only.
- No class playbook with even stub steps (commands, GP, flee).
- No Ankh-Morpork orientation (where you arrive, who kills newbies, what to hold).
- Umbrella `mud-skill` has no connect / nav / combat GATES (that gap is a **Required fix** on FR #1, not this issue).
- U2 still UNKNOWN: lore in-repo vs link-out.

## Ask (MUST)

P1 from `docs/functional-spec.md` (expand class/guild playbooks; connect/nav rituals), scoped to Discworld survival:

1. Harvest operator-approved public sources only (U2). Do not invent host/port/login.
2. Add an Ankh-Morpork newbie survival playbook stub with LOCKED vs UNKNOWN steps.
3. Name all seven working guilds (Warriors, Wizards, Witches, Thieves, Priests, Assassins, Fools) as UNKNOWN or LOCKED stubs.
4. Add at least one class playbook with a stub ritual (commands named only if sourced).
5. Append `docs/skill-harvest-log.md` with what was harvested and from where.

## Out of scope

- Full telnet client (U1).
- Replacing `SimonBarnett/MUD-AI`.
- Real credentials / invented instance URLs.
- FR #1 BT2/L5 required fixes (those stay on the #1 MRB board).

## Acceptance

| ID | Criterion |
|----|-----------|
| S1 | Ankh survival playbook exists in `discworld-mud` (or a companion) with no invented login. |
| S2 | Seven guilds listed as UNKNOWN or LOCKED (no extra invented guilds). |
| S3 | One class playbook has numbered stub steps (not only a table cell). |
| S4 | Harvest log cites sources; no `password=` / API key assignments. |

## Bob-job

Dispatch `bob-job-loop` on the feature-request issue after this park. Do not start from FR #1 FIX work.
