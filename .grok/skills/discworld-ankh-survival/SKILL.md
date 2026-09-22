---
name: discworld-ankh-survival
description: >
  First-minutes survival in Ankh-Morpork on Discworld MUD: lit streets, thieves,
  look/score, guild recruiters, when to flee. Use when the user says Ankh,
  Ankh-Morpork, AM streets, newbie DW, dead in 10 minutes, or /ankh-survival.
  Does not stamp ready for human UAT.
---

# Discworld MUD — Ankh survival (first 10 minutes)

Companion to `mud-skill` and `discworld-mud`. Goal: stay alive long enough to
orient and reach a guild recruiter without inventing connection details (L6/U1).

**Public lore depth:** link-out only — e.g. [Discworld MUD wiki](https://discworld.starturtle.net/)
and [discworldmud.org](https://www.discworldmud.org/) newbie material. Do not
paste long lore dumps into chat; cite links when the human wants depth.

## When to load

Load this skill when game text or the human indicates **Ankh-Morpork** (AM),
especially a **new character** in city streets. If the room is not AM, defer to
`discworld-mud` or umbrella `mud-skill` navigate stubs.

## First-10-minute ritual (numbered, fail-closed)

1. **LOCKED — Connection** — Use only operator-supplied host/client/credentials;
   never invent instance URL, port, or player login (U1/L6).
   LOCKED — Do not start this first-10-minute ritual until a human is past the terms screen. The 2026-09-22 playtest stopped at the terms and never saw Ankh-Morpork.
2. **LOCKED — Orient** — `look` (room + exits). Read **exits from game text only**.
   Note whether the room is **lit** and whether NPCs/players are present.
3. **LOCKED — Vitals** — `score` (and `hp` / health cues if the game shows them).
   If HP is low or you are bleeding/poisoned, treat combat as off-limits until healed.
4. **LOCKED — Stay visible** — Prefer **lit, busy streets** (main roads, shops,
   guild-adjacent plazas). Move with a clear exit back toward crowds.
5. **LOCKED — No alley wander** — Do **not** enter alleys, sewers, back passages,
   or unnamed side rooms “to explore” in the first 10 minutes. If an exit looks
   isolated or dark, **skip it** unless the human explicitly orders it.
6. **LOCKED — Thieves and aggro** — In AM, assume **pickpockets and street
   trouble** are common. Do not `kill` or loot in the street without human OK.
   If attacked, **flee** toward lit/busy areas (`flee` / move to known safe exit)
   before re-engaging.
7. **LOCKED — Inventory discipline** — `inventory` after any fight or gift. Do not
   `drop` or `give` unique items. Ask before `sell`/`buy` large purchases.
8. **LOCKED — Guild recruiter** — Goal: find a **guild recruiter** for the class
   the human chose (one of the seven working guilds in `discworld-mud`).
   Use `look` on NPCs; ask locals in-character only if the human approves spam.
   Do not invent recruiter room names — follow signs and game directions.
9. **LOCKED — Pkill / theft** — Stop and ask the human before **player-kill**,
   stealing from players, or illegal acts that risk guards/jail.
10. **LOCKED — Session log** — Keep a short log: room (as shown), exits, HP/GP,
    notable threats. **No passwords** in logs, commits, or issues.

If any step cannot be completed from real game output, **stop and report** what
you see; do not guess room names or commands.

## Do

- Route back to crowds and light when lost or hurt.
- Use umbrella `mud-skill` **Procedure: navigate (stub)** for exit discipline.
- Escalate guild choice to `discworld-mud` once indoors at a recruiter.

## Do not

- Invent host, port, TLS, or credentials.
- Wander alleys or “map the city” in minute 0–10.
- Stamp ready for human UAT (Bob only).
- Commit or echo passwords.
