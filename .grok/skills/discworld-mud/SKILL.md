---
name: discworld-mud
description: >
  Discworld MUD playbook companion for mud-skill: classes, guilds, newbie
  path, and game-specific rituals. Use when the user says Discworld MUD,
  DW, Ankh-Morpork, AM, guild, witch, wizard, thief, warrior, or
  /discworld-mud. Does not stamp ready for human UAT.
---

# Discworld MUD

Companion to `mud-skill`. Guild tables stay high-level; **class playbooks**
below are P1 depth harvested from public newbie docs (link-out in
`docs/skill-harvest-log.md`). Mark **LOCKED** vs **UNKNOWN**; do not invent
login or instance URLs (L6).

## Skill pack (#23, #26)

LOCKED — Companion leaflets under `.grok/skills/discworld-*` plus filled topic
skills (issue #26). Load the narrowest match:

| Topic | Example skill names |
|-------|---------------------|
| Character creation | `discworld-character-creation`, `mud-character-creation` |
| Death | `discworld-death-recovery`, `discworld-lore-death` |
| Money | `discworld-money-currency` |
| Travel | `discworld-travel-transport` |
| Skills / XP | `discworld-skills-experience`, `discworld-fight-skills-advance` |
| City | `discworld-city-ankh-morpork`, `discworld-city-lancre`, … |
| Location | `discworld-location-mended-drum`, `discworld-location-am-guild-quarter`, … |
| Guild | `discworld-guild-warrior`, `discworld-guild-witch`, … |
| Fight | `discworld-fight-combat-basics`, `discworld-fight-wimpy-flee`, … |
| Weapon | `discworld-weapon-swords`, `discworld-weapon-armour-encumbrance`, … |
| Shop | `discworld-shop-weapons`, `discworld-shop-pawn-trade`, … |
| Lore | `discworld-lore-death`, `discworld-lore-gods-patrons`, … |

Keep deep class steps here; extend a guild leaflet when a fact is guild-specific.

## Classes / guilds

Seven **working** guilds (public FAQ / newbie docs). Leaflets hold guild-specific
facts; warrior and witch **numbered playbooks** below are P1 depth.

| Guild | Leaflet | Playbook depth |
|-------|---------|----------------|
| Warrior | `discworld-guild-warrior` | **LOCKED** — below + specialisations doc |
| Wizard | `discworld-guild-wizard` | P1 leaflet; spells in-game |
| Witch | `discworld-guild-witch` | **LOCKED** — below |
| Thief | `discworld-guild-thief` | P1 leaflet + AM crime context |
| Priest | `discworld-guild-priest` | P1 — patron choice critical |
| Assassin | `discworld-guild-assassin` | P1 — PvP human-in-the-loop |
| Fool | `discworld-guild-fool` | P1 — roleplay-heavy |

## Newbie path

1. LOCKED — Run the Discworld front door in `mud-skill` and `discworld-character-creation`. At the terms `[yes/no]` prompt, send `yes` (Simon exception, issue #38). After `yes`, send nothing until the game has printed an `obvious exits` line. The login `>` and `Queued command: look` are not that line. On this guest the first room was the Mended Drum in Ankh-Morpork. Load `discworld-ankh-survival` and `discworld-location-mended-drum` before leaving the bar. `look` at an exit previews and does not move you. South and up stay inside the Drum and are owned by those two skills. Come back before leaving the pub. Do not open the closed north door. Do not enter the west stage from this step. Do not paste the room text here. Do not invent the host. Confirm the character with the human.
2. LOCKED — If starting in **Ankh-Morpork**, load **`discworld-ankh-survival`**
   and run its first-10-minute ritual before guild shopping.
3. LOCKED — Orient: `look`, `score`, `inventory`, read exits from game text.
4. LOCKED — Human picks guild (or defers); load the matching **class playbook**
   below once the choice is explicit.
5. UNKNOWN — Cross-guild newbie helpers (`helpers`, `newbie` channel) — use
   only when the human approves public-channel questions (wiki etiquette).

## Warrior class playbook

Sources: in-game `/doc/newbie/warriors_guild`, `/doc/newbie/warrior_specialisations`,
and public combat concepts (link-out in harvest log). **Decision-heavy** —
specialisation is chosen at join and cannot be deferred like some other guilds.

1. LOCKED — Confirm Warrior intent with the human. Warriors teach killing,
   maiming, and berserking; default **human-in-the-loop** before lethal hunts.
2. LOCKED — **Pick a specialisation at the guildhouse** — there is no
   “general warrior first, specialise later” path. Read in-game
   `warrior_specialisations` help; examples from public docs include Palace
   Guard and Weapon Masters' Court (Ankh-Morpork), Djelian Guard, Samurai,
   Lancre Highland Regiment, and others by region.
3. LOCKED — Before leaving city safety, run umbrella `mud-skill` **Procedure:
   navigate** and Ankh companion if in AM. Buy a weapon from a **game-shown**
   shop; burden and encumbrance affect combat (check `score` / inventory weight).
4. LOCKED — Newbie combat practice: official FAQ describes **Greg** in the
   newbie combat area — enter the combat room, answer his practice prompt
   (sobriety matters), train weapon/defence skills, leave when asked, repeat
   as needed; training rate slows over time.
5. LOCKED — Combat hygiene from public combat help: `consider` targets before
   attacking; set `wimpy` to flee when badly hurt; use `options combat` and
   `tactics` to adjust attitude; `skills fighting` to read fighting skills.
6. LOCKED — Training in **any** warrior guildhouse is allowed, but primaries
   follow your specialisation. Use guild teachers shown in game text; ask the
   human before large `advance` spends or unique gear changes.
7. UNKNOWN — Optimal weapon skill pairs, quest XP routes, and sub-guild
   equipment lockers vary by specialisation — harvest per character, do not
   paste wiki quest spoilers into public channels.
8. LOCKED — Stop and ask the human before guild resign, pkill, looting unique
   items, or swapping weapons that drop quest gear.

## Witch class playbook

Sources: in-game `/doc/newbie/witches_guild` and public witch guides (link-out).
Witch magic is herbs, cursing, flying, and **headology** — not wizard spell
slots. **Female characters only** for guild join (public guild description).

1. LOCKED — Confirm Witch intent **and** that the character meets the guild's
   public gender rule; if unsure, read in-game witches' guild help and ask the
   human before travelling to a join NPC.
2. LOCKED — Join via **Granny Weatherwax** or **Ogg-San** (public newbie doc).
   Bases include Lancre (cottage) and Bes Pelargic; from Ankh-Morpork, public
   docs name **Gennie Applebottom on Holofernes street** as orientation help
   toward Granny's — follow **in-game directions and signs**, not memorised
   speedwalks from the wiki.
3. LOCKED — If still in AM streets, finish **`discworld-ankh-survival`** first
   (thieves, lit routes). Long-distance travel to Lancre/BP is a human call
   when the character is fragile.
4. LOCKED — After join, use `skills` / guild teachers in **locked advance areas**
   named by the game (e.g. cottage / hut areas with regional currency). Ask
   the human before bulk `advance`; primaries differ from warrior primaries.
5. LOCKED — Early mobility: public guides recommend **broom** skill
   (`magic.items.held.broom`), fuel, and `adventuring.direction`; loot a
   newbie-chest broom only when game text shows one — do not assume chest
   contents.
6. LOCKED — Learn guild commands from teachers (`commands` to see known set).
   Public lists include Brew, Circle, Educe, Fade, Forget, Gaze, Hedgehog,
   Imbue, Mock, Splint, Squint, Tempt, Treat — many unlock via skills or
   NPCs; ask in-game teachers before spamming social commands on players.
7. UNKNOWN — Fruitbat, trick stones, tea recipes, and idle/number chasing —
   player preference; defer to human before pet upkeep or expensive components.
8. LOCKED — Channel etiquette: public guides mention the **Witches talker** —
   use only when the human approves; no quest spoiler sharing on public channels.
9. LOCKED — Stop and ask before curse/PK-adjacent play, stealing, or dropping
   hag stones / imbued items that may be irrecoverable.

## Do not

- Invent discworld host as LOCKED.
- Commit passwords.
- Stamp ready for human UAT.