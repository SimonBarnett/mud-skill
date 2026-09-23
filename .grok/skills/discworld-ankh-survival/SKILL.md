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

Load this skill when the room text says Ankh-Morpork or the Mended Drum, after `obvious exits` is on screen. Do not load it on the login `>`. If the room is not AM, defer to `discworld-mud` or umbrella `mud-skill` navigate stubs.

## First-10-minute ritual (numbered, fail-closed)

1. **LOCKED — Connection** — Use only operator-supplied host/client/credentials;
   never invent instance URL, port, or player login (U1/L6).
   LOCKED — Start this ritual only after the terms `[yes/no]` prompt has been answered `yes` (Simon exception, issue #38) and `obvious exits` is on screen. Do not start it on the login `>`.
   LOCKED — First room for guest `G` is the Mended Drum main bar (`discworld-location-mended-drum`). Do not copy the price list here. Do not take up, north, south, or west from this playbook. Alleys and lit streets apply only after the game shows a street.
   LOCKED — `look urchin`: a friendly looking street urchin that looks as if he knows his way around Ankh-Morpork. You could probably ask him how to get somewhere. He will probably give you directions. In good shape, standing, wearing a pair of grey worsted trousers and a ripped shirt. `ask urchin` alone returns `What?`. `ask urchin how to get to the warriors guild` returns `Try something else.` Do not lock an ask sentence.
   LOCKED — Leave with `quit` only as `mud-skill` describes. Do not close before `Do come again!`. A dropped link can leave `the net dead statue of ` in this bar. That is not death.
2. **LOCKED — Orient** — After a street is shown, `look` (room + exits). Read **exits from game text only**.
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
