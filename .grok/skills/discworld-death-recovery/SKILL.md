---
name: discworld-death-recovery
description: >
  Discworld MUD death and corpse recovery: afterlife, raise/resurrect, get all
  from corpse, permit, decay, unloading risk. Use when the user says died on DW,
  corpse loot, resurrect, or /discworld-death-recovery.
  Does not stamp ready for human UAT.
---

# Discworld MUD — death and recovery

Companion to `mud-skill`, `discworld-lore-death` (tone/lore), and
`discworld-mud`. Mechanics from public newbie and concept help.

**Sources (link-out):**

- [Newbie: dying](http://discworld.atuin.net/lpc/playing/documentation.c?path=%2Fnewbie%2Fdying)
- [Corpse concept](http://discworld.atuin.net/lpc/playing/documentation.c?path=%2Fconcepts%2Fcorpse)
- [Faq-O-Matic: items on death](https://discworld.starturtle.net/external/faq/cache/141.html)
- [Death (player wiki)](https://dwwiki.mooo.com/wiki/Death)
- [Unloading rooms](https://dwwiki.mooo.com/wiki/Unloading)

## LOCKED — Immediately after death

1. You are separated from your **inventory** — items stay on your **corpse** at
   the death location (pets may remain in arms per wiki).
2. Read the **afterlife book** and options shown in game text.
3. **Stay near your corpse** when possible — helpers use `find corpse`; empty
   rooms may **unload** and take floor items if the corpse decays with nobody present.
4. Ask for help: `helpers`, newbie channel (if available), `qwho` + `tell`, or
   shrines that **raise** the dead (public newbie dying doc).

## LOCKED — Resurrection → reclaim gear

1. After raise/resurrect, **wait until fully healed** before handling scrolls or
   gear that can damage you (wiki).
2. In the corpse room, recover inventory:

   ```
   get all from corpse
   equip
   ```

   Repeat; `look corpse` for leftovers. Wiki notes up to ~50 items plus money —
   multiple `get all` passes may be needed.

3. **`permit <player>`** — allows another player to take from **your** corpse when
   you cannot reach a dangerous area yourself.
4. **`look corpse`** — inspect contents; looting another player's corpse without
   permission is antisocial (public corpse help).

## LOCKED — Decay and time pressure

- Corpses **decompose over about an hour**, continuing while logged off (faq +
  wiki). When decomposition finishes, items fall to the **floor** — anyone may
  take them; floor items can vanish on **room unload**.
- Do not log out dead and forget — retrieve or get help promptly.

## LOCKED — Other corpse commands (in-game help)

- `drag corpse`, `bury` / `bury corpses`, `recover` variants — situational;
  corpses may not drag through water (public examples in corpse help).
- Playerkillers have special corpse-access rules — **UNKNOWN** detail; read live
  help if flagged PK.

## UNKNOWN

- Exact decay timers per terrain — treat as ~1 hour unless game says otherwise.
- Cost of NPC raise vs player ritual — guild/region specific.

## Do not

- Invent shrine room names or ritual syntax not shown in game output.
- Stamp ready for human UAT.
