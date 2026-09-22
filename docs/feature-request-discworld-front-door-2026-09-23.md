# FR: Discworld front door — menu, guest prompts, no-bot terms gate (issue #34)

**Issue:** https://github.com/SimonBarnett/mud-skill/issues/34  
**Playtest:** https://github.com/SimonBarnett/mud-skill/issues/33  
**Harvest paste (same work):** https://github.com/SimonBarnett/mud-skill/issues/35

## Summary

Playtest #33 never got past login. The playbooks do not describe the live
front door. Discworld forbids robot scripts and triggers. Teach the next
agent how to reach the terms screen from published connect details, then
**stop**. Implement by pasting the LOCKED text from issue #35 into the
owner skill files. Do not ship a client or a trigger pack.

## Gap vs main (`d8efa43`)

`mud-skill` Procedure: connect says ask the human and never invent a host.
It does not record the login menu. `discworld-character-creation` starts at
nationality / stats / newbie area. The live guest path is: menu → name →
capitalisation → sex → screenreader → terms + 30s wait. Nationality was
not reached. No LOCKED step says: stop at the terms, show them to the
human, do not accept them from an unattended agent.

## LOCKED (live session 2026-09-22 + public getting-started page)

1. Cite published connect: `discworld.starturtle.net` ports 23 and 4242,
   TLS 4245. Do not invent another host.
2. Document the login menu letters: Q, M, D, R, U, L, P, F, N, G, or an
   existing character name.
3. Document the guest prompt order that was actually shown: name,
   capitalisation, male or female, screenreader `[yes/no/help]`, then the
   terms with a 30 second pause.
4. During that 30 second pause, send nothing.
5. Hard stop: while the terms forbid robot scripts or triggers, an agent
   must not accept them and must not send play commands. The human accepts
   and plays, or the agent stops and reports.
6. The name prompt is not a command prompt. Do not send `look`, `score`,
   `inventory`, or `quit` there. Those words come back banished as player
   names.
7. On `someone is already trying to create a character of that name`, pick
   another name or retry later. Do not hammer the same name.
8. No passwords in git or issue comments.
9. `tools/Validate-MudSkill.ps1` stays green. No UAT stamp.

Paste the exact sections from issue #35 into:

| Fact | Owner skill |
|------|-------------|
| Menu, telnet port that answered, no-bot stop | `mud-skill` |
| Guest prompt order, name banishment, name collision | `discworld-character-creation` |
| Stop before newbie orient if terms forbid scripts | `discworld-mud` |
| Do not start the AM ritual until a human is past terms | `discworld-ankh-survival` |
| Pointer when any MUD forbids scripts | `mud-character-creation` |
| Dated note | `docs/skill-harvest-log.md` |

## UNKNOWN

- Exact yes/no wording of the terms accept prompt. Not observed. Do not invent.
- Whether guest (`G`) and new character (`N`) diverge after the screenreader
  question.
- In-world newbie path, Ankh survival, and guild join. Not reached. Do not
  add city, location, guild, fight, shop, weapon, death, money, or travel
  steps from this playtest.

## Acceptance

- A1: `mud-skill` connect and `discworld-character-creation` contain the
  menu and guest prompt order. Mark LOCKED only for lines observed or cited
  from the public getting-started page.
- A2: A numbered no-bot gate: do not accept Discworld terms, and do not
  automate play, while robot scripts or triggers are forbidden.
- A3: Name-prompt banishment and the name-collision failure are written down.
- A4: No secrets, no invented accept syntax, no UAT stamp.
- A5: BT0 (`tools/Validate-MudSkill.ps1`) still exits 0.
- A6: Issue #35 harvest route is applied (five skills + harvest log). Close
  #33 and #35 when this lands.

## Out of scope

Do not add a MUD client (functional spec N4). Do not paste quest spoilers.
Do not lock an accept command that this playtest did not see.

Workers do not stamp UAT.
