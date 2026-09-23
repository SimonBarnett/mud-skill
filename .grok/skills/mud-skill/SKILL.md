---
name: mud-skill
description: >
  Umbrella agent skill for playing MUDs (connect, navigate, combat, quest,
  economy playbooks). Discworld MUD details live in companion discworld-mud.
  Use when the user says MUD, MUD playbook, telnet mud, DW MUD, Discworld,
  or /mud-skill. Does not stamp ready for human UAT.
---

# MUD skill (umbrella)

Playbooks for agents in text MUDs. Prefer world-specific companions when
the game is named (start with `discworld-mud`; **57+** leaflets under
`.grok/skills/discworld-*` and topic skills — issues #23, #26).

## LOCKED (issue #74)

1. Read https://github.com/SimonBarnett/mud-skill.
2. Try playing Discworld.
3. Any issues or feature request: log on this repo.
4. Harvest learned skills back to the repo as a feature request.

## Topic playbooks (#26)

| Topic | Skill |
|-------|--------|
| Character creation (umbrella) | `mud-character-creation` |
| Discworld char create | `discworld-character-creation` |
| Achaea char create | `achaea-character-creation` |
| Death / corpses | `discworld-death-recovery`, lore: `discworld-lore-death` |
| Money / currency | `discworld-money-currency` |
| Shops (where + workflow) | `discworld-shop-*` |
| Travel | `discworld-travel-transport` |
| Skills / XP | `discworld-skills-experience` |
| Mended Drum main bar | `discworld-location-mended-drum` |

When connected to **Discworld MUD** and room text or the human indicates
**Ankh-Morpork** (AM), load companion **`discworld-ankh-survival`** before
generic navigation — especially for newbies (“dead in 10 minutes” in AM).

## GATES (stub)

| Gate | Status | Entry |
|------|--------|--------|
| connect | LOCKED stub | **Procedure: connect (stub)** below |
| navigate | LOCKED stub | **Procedure: navigate (stub)** below |
| combat | UNKNOWN stub | **Procedure: combat (stub)** below (U4) |

## Procedure: connect (stub)

1. LOCKED — Ask the human which MUD instance and which client or telnet path
   to use; never invent host, port, TLS, or credentials.
2. LOCKED — Connect only with operator-supplied details; do not echo passwords
   into logs, commits, or issue comments.
3. LOCKED — Discworld plain TCP on port 4242 answered (playtest 2026-09-22).
   TLS port 4245 and any fleet wire client stay UNKNOWN.
4. LOCKED — After login, capture prompt/character name from game text; if
   login fails, stop and report verbatim errors (no credential guessing).

### Discworld front door (playtest 2026-09-22)

Source: [Getting Started](https://discworld.starturtle.net/lpc/playing/getting_started.html). Observed on plain TCP `discworld.starturtle.net` port 4242. Banner: `LPmud version : DW OS v1.02 on port 4242.`

1. LOCKED — That page names ports 23 and 4242, and TLS port 4245. This session used 4242 only. Treat 23 and 4245 as cited, not re-tested.
2. LOCKED — The first screen is a menu, not a room:

```
Q - Quit
M - Print this menu again
D - Delete your character
R - Request a temporary password
U - Short list of who is on-line
L - Short list of liaisons on-line
P - Uptime
F - Finger someone
N - New character
G - Guest character
Or, enter your current character's name
Your choice:
```

3. LOCKED — Do not send `look`, `score`, `inventory`, or `quit` until game text shows a room and exits. At the name prompt those words are names. Reply seen: `Sorry the player name look has been banished.` Same for `score` and `inventory`.
4. LOCKED — Guest creation is menu `G`, then the prompt list in `discworld-character-creation`.
5. LOCKED — Terms include `Use of robot scripts or triggers is not permitted.` Show the terms to the human. Simon granted an exception (issue #38, #bobiverse 2026-09-23): this agent may accept and continue. Do not stop at the terms screen.
6. LOCKED — After the terms list the game says it will be back in 30 seconds. Send nothing during that wait.
7. LOCKED — The accept prompt (playtest 2026-09-22, issue #38) is exactly:

```
Enter 'yes' if you agree to the terms or 'no' if you cannot.
By typing 'yes' you signify that you have read, understand and agree to be
bound by these terms and conditions: [yes/no]
```

   With the exception, send `yes`, then follow the post-yes order below. Sending `no` was observed to print `Come back soon!` and close the socket. That is the decline path, not this agent's path.

### After `yes` (playtest 2026-09-22, issues #41 #46)

1. LOCKED — `You have never logged in before.` then `Saving...` twice.
2. LOCKED — ANSI colour is in the stream even when screenreader was answered `no`. Strip ESC sequences before matching text.
3. LOCKED — Rules box: read `help rules`. Ignorance is not a defence.
4. LOCKED — The game prints `>` and `Queued command: look` on its own. Send nothing. That `>` is not a room.
5. LOCKED — `Please set your finger information with "chfn".` Do not run `chfn`. Prompts were not shown.
6. LOCKED — `Inventory regeneration complete.`
7. LOCKED — Chatter before the room (town crier, a one-line guild or work nudge) is not the room and not the result of an agent command.
8. LOCKED — Send the next command only after an `obvious exits` line. On this playtest that room was the Mended Drum (`discworld-location-mended-drum`). Do not describe the room here.
9. LOCKED — When the game says `There are multiple matches` and points at `help parser`, do not send the same noun again. `help parser` was paged with blank lines (same pager rule as item 13 below). It describes ordinals (`1st`, `2nd`) and forms like `blue frog 1`. Do not paste the help page here. Tray gets tested on the Mended Drum brochure: `get 1st colourful brochure from tray` and `get colourful brochure 1 from tray` when `look tray` showed one brochure (`discworld-location-mended-drum`). `get 2nd colourful brochure from tray` with only one brochure on the tray returned `Cannot find "colourful brochure", no match.` Do not claim `2nd` fails when several brochures remain — not retested. `here` was not sent. While holding the brochure, `my` works for `look my brochure`, `open my brochure`, `read my brochure`, and `turn my brochure to page <N>`. If a colourful brochure is also on the floor, bare `brochure` is multiple matches for `open`, `read`, and `turn`; use `my` or another disambiguator. Drop and floor-get lines are in `discworld-location-mended-drum`. Do not paste turn syntax or brochure page text here.
10. LOCKED — A leftover `0;10m` with no ESC can sit inside the room map. It is not an exit and not an object. Strip it before matching.
11. LOCKED — `Queued command: ` is an acknowledgement, not the result. Wait for the real text.
12. LOCKED — If the game prints the sentence below, quote it. Do not send `stop` or `restart`. Those words were not sent.

```
If you are trying to quit and it is queueing things, use "stop" to stop your
commands, and/or "restart" to start your heartbeat.
```

13. LOCKED — Pager line observed: `Read From 1 to 23 of 25 (92%) - return to continue, h for help.` Send a blank line to continue. Do not send another command or `quit` while `return to continue` is the latest prompt. `h` was not sent. Do not describe what `h` prints.
14. LOCKED — Guest `quit` with a clear queue: Greco the Departure Gecko, then `But not saving for guests... sorry.`, then `Do come again!`, then EOF. A `>` in the middle of that speech is not the end. Do not close the socket before `Do come again!`. Do not lock the bird-versus-chimera line. If the link drops before the farewell, a `net dead statue of ` can remain. That outcome is `discworld-death-recovery`.

UNKNOWN — what `h` prints; whether `stop` or `restart` clears a queue; `chfn` prompts; menu `N`; whether `my` works on a get from the tray; `here`.
15. LOCKED — No passwords in logs, commits, or issues.

## Procedure: navigate (stub)

1. LOCKED — Read the current room description and listed exits from game output
   only; do not invent room names or directions.
2. LOCKED — Maintain a short session log: room label (as shown), exits, and
   notable NPCs/items; no passwords.
3. UNKNOWN — Automap or client scripts (U1) — defer until human approves a tool.
4. LOCKED — Before `go`/`enter` into risky or one-way areas, confirm with the
   human when the skill or companion marks the action irreversible.

## Procedure: combat (stub)

1. LOCKED — Confirm with the human whether to engage; default human-in-the-loop
   for lethal or loot-heavy fights (U4).
2. LOCKED — Parse target name and health cues from game text; issue only commands
   the game accepts (e.g. kill/flee) as shown in help or human instruction.
3. UNKNOWN — Optimal rotations, guild combos, and XP grinding routes — harvest
   later; use companion class playbooks when present.
4. LOCKED — Stop and ask before `pkill`, looting unique items, or continuing
   after a death message.

## Do

1. Confirm which MUD (never invent host/port/login).
2. Load the matching companion skill if present (Discworld + AM →
   `discworld-ankh-survival`; other Discworld → `discworld-mud`).
3. Keep a short session log (room, exits, HP/GP if shown) — no passwords.
4. Ask before irreversible actions (pkill, drop unique, guild resign).

## Do not

- Store or commit credentials.
- Stamp ready for human UAT (Bob only).
- Confuse this with `MUD-AI` (separate product).
## CAST IRON harvest (Simon 2026-09-22)

When you learn a MUD / Discworld playbook, load and follow
`harvest-mud-skill` (this repo). Do not leave playbooks only in
`~/.grok/skills`.
