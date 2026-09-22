# Feature request: Discworld Ankh survival playbooks

**Repo:** `SimonBarnett/mud-skill`  
**Date:** 2026-09-22  
**Issue:** #3  
**Source:** parked from mud-skill #3 — agent is dead inside 10 minutes in Ankh; give a fighting chance; harvest loads of public newbie/Ankh info.

## Intent / critique

| | |
|--|--|
| **Intent** | Companion playbooks so an agent survives the first minutes in Ankh-Morpork (Discworld MUD): streets, thieves, guilds, look/score, when to run. |
| **Good** | Concrete failure mode (dead in 10 minutes) and a harvest-rich world. |
| **Bad** | P0 `discworld-mud` is still a stub; no Ankh survival ritual. |
| **Ugly** | Invented host/login, or a novel-length lore dump with no triggers. |

## Ask (MUST)

1. `.grok/skills/discworld-ankh-survival/SKILL.md` (or equivalent companion) with triggers: Ankh, Ankh-Morpork, newbie DW, dead in 10 minutes, /ankh-survival.
2. Numbered first-10-minute ritual: look/exits, keep to lit/busy streets, do not wander alleys, score/hp, find a guild recruiter, ask before pkill/theft.
3. Harvest **public** Discworld newbie/Ankh facts only. Link-out for long lore. No invented instance URL, port, or player credentials (U1 / L6).
4. Umbrella `mud-skill` points at this companion when the room is Ankh.
5. `docs/skill-harvest-log.md` notes the harvest source (issue #3 + public DW newbie docs).
6. BT0 still exits 0. No secrets. No worker UAT stamp.

## Out of scope

- Implementing #1 L5/BT2 FIX (16948 / PR #7).
- Replacing `MUD-AI`.
- Full telnet client (U1).
- #4 `harvest-mud-skill` foundation (separate FR).

## Acceptance

| ID | Criterion |
|----|-----------|
| A1 | Companion SKILL.md exists with Ankh/newbie triggers. |
| A2 | First-10-minute ritual is numbered and fail-closed (no alley wander, no invented login). |
| A3 | Harvest log cites #3 / public sources (or "seed only"). |
| A4 | Umbrella skill routes Ankh to this companion. |
| A5 | No secrets; BT0 green on the PR. |
