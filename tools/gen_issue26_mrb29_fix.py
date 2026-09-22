# Generate topic-specific discworld leaflets for MRB #29 (issue #26 FIX).
# Run from repo root: python tools/gen_issue26_mrb29_fix.py
import os
import re
import textwrap

ROOT = os.path.join(os.path.dirname(__file__), "..")
SKILLS = os.path.join(ROOT, ".grok", "skills")

WIKI = "https://discworld.starturtle.net/"
OFFICIAL = "https://www.discworldmud.org/"


def write_skill(dirname, name, desc, title, surfaces, sources, locked, unknown):
    path = os.path.join(SKILLS, dirname, "SKILL.md")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    src_lines = "\n".join(f"- {s}" for s in sources)
    lock_lines = "\n".join(f"{i+1}. {x}" for i, x in enumerate(locked))
    unk_lines = "\n".join(f"- {x}" for x in unknown)
    body = textwrap.dedent(f"""---
name: {name}
description: >
  {desc}
  Does not stamp ready for human UAT.
---

# {title}

Companion to `mud-skill` and `discworld-mud`. Surfaces: **{surfaces}** (#23, #26 FIX).
No invented host, port, or credentials.

**Sources (link-out):**

{src_lines}

## LOCKED

{lock_lines}

## UNKNOWN

{unk_lines}

## Do not

- Invent room ENAMEs or login details.
- Stamp ready for human UAT (Bob only).
""")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(body)


LEAFLETS = []

# --- cities (9) ---
LEAFLETS.append((
    "discworld-city-bes-pelargic",
    "discworld-city-bes-pelargic",
    "Discworld MUD city guide for Bes Pelargic and Agatean themes.",
    "Bes Pelargic (city guide)",
    "city, location, lore",
    [
        "https://dwwiki.mooo.com/wiki/Bes_Pelargic",
        "https://dwwiki.mooo.com/wiki/Travel",
        "http://dwmud.pbworks.com/w/page/18434040/Currencies",
    ],
    [
        "LOCKED — Bes Pelargic (Agatean Empire port) uses **Agatean currency** (Rh/s notation in public guides); converting to AM dollars is awkward — plan spending or use guild/house payments that accept any currency (pbworks currencies page).",
        "LOCKED — Intercontinental carriage routes link AM to BP-facing stops (wiki Travel table); use coloured stop notes and `enter carriage` (`discworld-travel-transport`).",
        "LOCKED — Morporkian nationality does **not** start here; long ocean/carriage legs need human OK while fragile.",
        "LOCKED — `look` room text for exits; Bes maps on Kefka (`dw.daftjunk.com`) — do not memorise speedwalks as LOCKED.",
    ],
    [
        "Per-street shop catalogue for current BP — Kefka DB searchable by city; no single wiki table copied here (gap: https://dwwiki.mooo.com/wiki/Bes_Pelargic lacks shop list section).",
    ],
))

LEAFLETS.append((
    "discworld-city-djelibeybi",
    "discworld-city-djelibeybi",
    "Discworld MUD city guide for Djelibeybi: desert, Djelian guard, DjToon currency.",
    "Djelibeybi (city guide)",
    "city, location, lore",
    [
        "https://dwwiki.mooo.com/wiki/Djelibeybi",
        "https://discworld.starturtle.net/lpc/playing/documentation.c?path=%2Fnewbie%2Fwarrior_specialisations",
        "https://dwwiki.mooo.com/wiki/Carriages",
    ],
    [
        "LOCKED — Desert kingdom; public warrior docs name **Djelian Guard** specialisation tied to this region.",
        "LOCKED — Nationality help groups Djelian / Klatchian / Tsortian / Howondalandish starts with **Djelian currency** and Djelian language (`discworld-character-creation`).",
        "LOCKED — **Djelibeybi carriage** route on wiki Travel matrix; board at marked stops only.",
        "LOCKED — Heat and NPC law cues from room text; `consider` before combat in desert outskirts.",
    ],
    [
        "Temple and palace room graph — not in harvested wiki summary (https://dwwiki.mooo.com/wiki/Djelibeybi stub); discover in-game.",
    ],
))

LEAFLETS.append((
    "discworld-city-ephebe",
    "discworld-city-ephebe",
    "Discworld MUD city guide for Ephebe: philosophers, Ephebian currency, Il Drim starts.",
    "Ephebe (city guide)",
    "city, location, lore",
    [
        "https://dwwiki.mooo.com/wiki/Ephebe",
        "https://discworld.starturtle.net/lpc/playing/documentation.c?path=%2Fconcepts%2Fnationality",
        "https://dwwiki.mooo.com/wiki/Travel",
    ],
    [
        "LOCKED — Philosopher-city parody; **Istanzian** and **Omnian** nationalities start **Il Drim** with Ephebian money per nationality doc.",
        "LOCKED — Harbour Market and sea routes appear on wiki Travel / carriage tables (e.g. swordfish stall Ephebe in player DB examples).",
        "LOCKED — Money changers quote Ephebian `de` rates vs AM on wiki Money changer tables (`discworld-money-currency`).",
        "LOCKED — Ask human before theft/PvP in foreign cities (public etiquette guides).",
    ],
    [
        "Arena and temple quest NPC coordinates — wiki Ephebe page has no full street shop index (cited gap).",
    ],
))

LEAFLETS.append((
    "discworld-city-genua",
    "discworld-city-genua",
    "Discworld MUD city guide for Genua: carnival, voodoo themes, Genuan currency.",
    "Genua (city guide)",
    "city, location, lore",
    [
        "https://dwwiki.mooo.com/wiki/Genua",
        "https://dwwiki.mooo.com/wiki/Travel",
        "https://dwwiki.mooo.com/sined/general/changers.htm",
    ],
    [
        "LOCKED — Genuan nationality starts with **Genuan currency** and Morporkian fluency (nationality concept doc).",
        "LOCKED — **Coast / Genua carriage** stops listed on wiki Travel; changers sample **Gc/Gl** vs AM (changers.htm).",
        "LOCKED — Carnival and voodoo-themed NPC magic — treat as high risk until `consider` + human OK.",
        "LOCKED — Pair with `discworld-travel-transport` for long routes from AM; carry correct coin before shopping.",
    ],
    [
        "Carnival quest spoiler rooms — intentionally not listed (wiki Genua quest sections omitted).",
    ],
))

LEAFLETS.append((
    "discworld-city-klatch",
    "discworld-city-klatch",
    "Discworld MUD city guide for Klatch and Klatchian areas.",
    "Klatch (city guide)",
    "city, location, lore",
    [
        "https://dwwiki.mooo.com/wiki/Klatch",
        "https://dwwiki.mooo.com/wiki/Travel",
        "https://discworld.starturtle.net/lpc/playing/documentation.c?path=%2Fconcepts%2Fnationality",
    ],
    [
        "LOCKED — Klatchian nationality starts **Djelibeybi area** with Djelian money per nationality help (not a separate Klatch coin at creation).",
        "LOCKED — Wiki Travel marks **Klatch Foreign Legion** and related intercontinental stops — transfer carriages at listed poles.",
        "LOCKED — Desert/coastal themes in Pratchett canon; load `discworld-mud` before cross-continent trips.",
        "LOCKED — Exits from game text only; Klatch city map fragments on dwwiki — verify live.",
    ],
    [
        "Named Klatch city shop list — dwwiki Klatch page has no comprehensive shop table (gap URL above).",
    ],
))

LEAFLETS.append((
    "discworld-city-lancre",
    "discworld-city-lancre",
    "Discworld MUD Lancre and Ramtops: witch country, Lancre currency, carriage route.",
    "Lancre and Ramtops (city guide)",
    "city, location, lore",
    [
        "https://dwwiki.mooo.com/wiki/Lancre",
        "https://dwwiki.mooo.com/wiki/Carriages",
        "https://dwwiki.mooo.com/wiki/Carriages#Lancre_Kingdom",
    ],
    [
        "LOCKED — Lancre Kingdom is a Ramtops monarchy; **Lancre Town** is a key hub (wiki Lancre).",
        "LOCKED — Spend **Lancre coins** (base-12 ladder in `discworld-money-currency`); change AM dollars before Ramtops shopping.",
        "LOCKED — **Lancre Kingdom carriage** loop includes Mad Stoat, Brass Neck, **Bad Ass**, Slippery Hollow, Razorback, Slice, Creel Springs, Mad Wolf, Blackglass, Lancre Town — route allows `leave carriage at <stop>` (wiki Carriages).",
        "LOCKED — Witch guild paths reference Lancre / Bad Ass (`discworld-mud` witch playbook); human OK before wilderness hunts.",
    ],
    [
        "Every Lancre village shop name — Kefka DB has entries but no curated wiki list on https://dwwiki.mooo.com/wiki/Lancre (one-line page only).",
    ],
))

LEAFLETS.append((
    "discworld-city-pseudopolis",
    "discworld-city-pseudopolis",
    "Discworld MUD city guide for Pseudopolis.",
    "Pseudopolis (city guide)",
    "city, location",
    [
        "https://dwwiki.mooo.com/wiki/Pseudopolis",
        "https://discworld.starturtle.net/lpc/playing/documentation.c?path=%2Fconcepts%2Ffaq",
    ],
    [
        "LOCKED — Major Disc city in canon; FAQ and wiki reference Pseudopolis as reachable hub.",
        "LOCKED — Use umbrella navigate procedure; carriage links appear on master Travel chart (check stop notes in-game).",
        "LOCKED — Local currency per room prices — change money at changers when leaving Sto Plains (`discworld-money-currency`).",
        "LOCKED — Log exits; do not invent recruiter or shop ENAMEs.",
    ],
    [
        "Newbie-friendly shop roll call — wiki Pseudopolis page lacks shop table (https://dwwiki.mooo.com/wiki/Pseudopolis).",
    ],
))

LEAFLETS.append((
    "discworld-city-sto-lat",
    "discworld-city-sto-lat",
    "Discworld MUD city guide for Sto Lat on the Sto Plains.",
    "Sto Lat (city guide)",
    "city, location",
    [
        "https://dwwiki.mooo.com/wiki/Sto_Lat",
        "https://dwwiki.mooo.com/wiki/Travel",
    ],
    [
        "LOCKED — Sto Lat sits on Sto Plains near AM; wiki Travel marks **Sto Lat** on several carriage rows (Mail / intercity).",
        "LOCKED — Uses **AM currency** on Sto Plains per currency wiki; short carriage hops from AM possible.",
        "LOCKED — Mid-game errands reference Sto Lat in player guides — confirm quest text before travel.",
        "LOCKED — `discworld-ankh-survival` not required here; still use `wimpy` in unfamiliar plains.",
    ],
    [
        "Complete Sto Lat shop index — not published on dwwiki Sto Lat stub page.",
    ],
))

LEAFLETS.append((
    "discworld-city-uberwald",
    "discworld-city-uberwald",
    "Discworld MUD Uberwald region: Escrow, undead themes, Uberwald carriage.",
    "Uberwald (region guide)",
    "city, location, lore",
    [
        "https://dwwiki.mooo.com/wiki/Uberwald",
        "https://dwwiki.mooo.com/wiki/Carriages",
        "https://discworld.starturtle.net/lpc/playing/documentation.c?path=%2Fconcepts%2Fnationality",
    ],
    [
        "LOCKED — **Uberwaldian** nationality starts **Escrow** with Lancre currency and Uberwaldean (nationality doc).",
        "LOCKED — **Uberwald carriage** / Vieux River / Steppes routes on wiki Carriages (Escrow, Bonk, Koom Gorge, etc.).",
        "LOCKED — Vampire/werewolf themes — night travel and supernatural NPCs warrant caution + human OK for combat.",
        "LOCKED — Lancre money changers buy/sell vs AM at listed spreads (`discworld-money-currency`).",
    ],
    [
        "Castle clan quest lines — spoiler; wiki Uberwald quest section not harvested.",
    ],
))

def guild_leaflet(dirname, guild_slug, title_extra, locked_extra, unknown_extra):
    url = f"https://discworld.starturtle.net/lpc/playing/documentation.c?path=%2Fnewbie%2F{guild_slug}"
    LEAFLETS.append((
        dirname,
        dirname,
        f"Discworld MUD {title_extra} guild playbook leaflet.",
        title_extra,
        "guild, fight, lore",
        [url, WIKI, "https://dwwiki.mooo.com/wiki/Guilds"],
        [
            f"LOCKED — Read in-game `/doc/newbie/{guild_slug}` and guild help before join (starturtle URL above).",
            "LOCKED — Human confirms guild join — resign is painful; load `discworld-mud` class table.",
            "LOCKED — Train via `advance` in guild advance rooms and TM (`discworld-skills-experience`); ask before big XP spends.",
            "LOCKED — Combat and theft default human-in-the-loop (`mud-skill` combat gate).",
        ] + locked_extra,
        unknown_extra,
    ))


guild_leaflet(
    "discworld-guild-assassin",
    "assassins_guild",
    "Assassins'",
    [
        "LOCKED — Assassins' Guild centred in AM; contracts and PvP rules in public assassin docs.",
        "LOCKED — Stealth/poison skills guild-taught; crossbows limited for non-assassins (weapon wiki).",
    ],
    ["Contract board live procedures — in-game help only (assassins_guild doc does not export board room names)."],
)
guild_leaflet(
    "discworld-guild-fool",
    "fools_guild",
    "Fools'",
    [
        "LOCKED — Fool is roleplay/entertainment focused; not a combat progression guild (public fools_guild orientation).",
        "LOCKED — Confirm joke/toxic RP boundaries with human before public channels.",
    ],
    ["Skill progression gags — sparse public wiki; harvest during play."],
)
guild_leaflet(
    "discworld-guild-priest",
    "priests_guild",
    "Priests'",
    [
        "LOCKED — **Patron deity** choice is major — human must pick before join (priests_guild doc).",
        "LOCKED — Faith points, rituals, and `rituals` help govern spells (`discworld-lore-gods-patrons`).",
        "LOCKED — Divine Hand travel for priests (`discworld-travel-transport`).",
    ],
    ["Per-god spell trees — deity-specific in-game help only."],
)
guild_leaflet(
    "discworld-guild-thief",
    "thieves_guild",
    "Thieves'",
    [
        "LOCKED — Legalised theft in AM; `steal`/`fence` guild rules in thieves_guild doc.",
        "LOCKED — Fence via NPC **fence** command — see `/doc/known_command/fence` (starturtle).",
        "LOCKED — Ask human before stealing from players or unique NPCs.",
    ],
    ["Guild quota/licence numbers — read live thief help."],
)
guild_leaflet(
    "discworld-guild-wizard",
    "wizards_guild",
    "Wizards'",
    [
        "LOCKED — Spell slots, libraries, and UU themes (`discworld-location-am-unseen-university`).",
        "LOCKED — Components via `components <spell>` help (`discworld-shop-magic-components`).",
        "LOCKED — JPCT portals — wizard responsibility; `look enter portal` before use.",
    ],
    ["Optimal spell XP path — guild-specific; not in newbie doc summary."],
)
guild_leaflet(
    "discworld-guild-witch",
    "witches_guild",
    "Witches'",
    [
        "LOCKED — Female characters only for join (witches_guild); herbs, headology, broom flight.",
        "LOCKED — Join NPCs Granny Weatherwax / Ogg-San named in newbie doc — follow signs from AM via Gennie Applebottom hint.",
        "LOCKED — Expanded steps in `discworld-mud` witch playbook.",
    ],
    ["Fruitbat / tea recipe economy — player preference."],
)
guild_leaflet(
    "discworld-guild-warrior",
    "warriors_guild",
    "Warriors'",
    [
        "LOCKED — Specialisation chosen at join — read `warrior_specialisations` doc.",
        "LOCKED — Greg newbie combat (`discworld-fight-newbie-greg`); primaries follow spec.",
        "LOCKED — Full numbered playbook in `discworld-mud` warrior section.",
    ],
    ["Optimal weapon pair per spec — character build."],
)

# --- locations (8) ---
LEAFLETS.append((
    "discworld-location-am-docks",
    "discworld-location-am-docks",
    "Discworld MUD Ankh-Morpork docks and sea travel.",
    "AM docks (location)",
    "location, city",
    [
        "https://dwwiki.mooo.com/wiki/Ankh-Morpork",
        "https://dw.daftjunk.com/items/index.php?item=145&shop=724",
    ],
    [
        "LOCKED — **Kedger Street** hosts a seedy dockside shop (Kefka shop 724) selling sailor gear — example waterfront commerce.",
        "LOCKED — Docks tie to sea smuggling themes; human OK before boarding ships or isolated waterfront rooms.",
        "LOCKED — Pair with `discworld-city-ankh-morpork` and `discworld-ankh-survival` when leaving lit streets.",
        "LOCKED — Thieves' fence economy may reference dock loot — guild rules apply.",
    ],
    ["Sailing schedules and captain names — room text only; dwwiki AM page has no schedule table."],
))
LEAFLETS.append((
    "discworld-location-am-guild-quarter",
    "discworld-location-am-guild-quarter",
    "Discworld MUD AM guild quarter and recruiters.",
    "AM guild quarter (location)",
    "location, guild, city",
    [
        "http://discworld.starturtle.net/lpc/playing/documentation.c?path=%2Fconcepts%2Fankh-morpork",
        "https://dwwiki.mooo.com/wiki/Ankh-Morpork",
    ],
    [
        "LOCKED — AM hosts HQs for most working guilds (ankh-morpork concept doc).",
        "LOCKED — Find recruiters via signs/`look` — do not invent room names; use `discworld-guild-*` after human picks class.",
        "LOCKED — Approach via lit routes (`discworld-ankh-survival`) when newbie.",
        "LOCKED — Watch and guild politics (`discworld-lore-guild-politics`).",
    ],
    ["Exact map coordinates — use in-game Alpha to Omega map item per ankh-morpork help."],
))
LEAFLETS.append((
    "discworld-location-am-sewers",
    "discworld-location-am-sewers",
    "Discworld MUD Ankh-Morpork sewers — high risk.",
    "AM sewers (location)",
    "location, city, fight",
    [
        "https://dwwiki.mooo.com/wiki/Ankh-Morpork",
        "https://discworld.starturtle.net/lpc/playing/documentation.c?path=%2Fhelpdir%2Fwimpy",
    ],
    [
        "LOCKED — Sewers are dangerous; **avoid first 10 minutes** in AM (`discworld-ankh-survival`).",
        "LOCKED — Bring light, set `wimpy`, plan flee exits before human orders sewer run.",
        "LOCKED — Corpse recovery hard in isolated tiles — `discworld-death-recovery`.",
        "LOCKED — Monster tiers vary — `consider` each new NPC type.",
    ],
    ["Full sewer graph — not in public wiki summary; discover with human OK."],
))
LEAFLETS.append((
    "discworld-location-am-unseen-university",
    "discworld-location-am-unseen-university",
    "Discworld MUD Unseen University in Ankh-Morpork.",
    "Unseen University (location)",
    "location, city, guild, lore",
    [
        "https://dwwiki.mooo.com/wiki/Unseen_University",
        "https://discworld.starturtle.net/lpc/playing/documentation.c?path=%2Fnewbie%2Fwizards_guild",
    ],
    [
        "LOCKED — UU is wizard cultural centre; non-wizards face access rules from guards/doors (room text).",
        "LOCKED — High Energy Magic Building / library quests referenced on wiki UU page — spoiler-sensitive.",
        "LOCKED — **Magical Emporium, Sator Square** supplies components upstairs (`discworld-shop-magic-components`).",
        "LOCKED — Do not spam combat spells in AM streets without human OK.",
    ],
    ["Library quest permissions — in-game only."],
))
LEAFLETS.append((
    "discworld-location-bad-ass-cottage",
    "discworld-location-bad-ass-cottage",
    "Discworld MUD Bad Ass village and witch cottage lore.",
    "Bad Ass cottage (location)",
    "location, lore",
    [
        "https://dwwiki.mooo.com/wiki/Bad_Ass",
        "https://dwwiki.mooo.com/wiki/Carriages",
    ],
    [
        "LOCKED — Bad Ass is Lancre village from canon; on **Lancre Kingdom carriage** loop (wiki Carriages).",
        "LOCKED — Witch join / cottage play references Granny themes (`discworld-mud` witch playbook).",
        "LOCKED — Treat powerful witch NPCs with respect; human OK for curse-adjacent RP.",
        "LOCKED — Pay in Lancre currency in Ramtops shops.",
    ],
    ["Quest triggers in cottage rooms — not listed on short dwwiki Bad Ass page."],
))
LEAFLETS.append((
    "discworld-location-hub-rose-garden",
    "discworld-location-hub-rose-garden",
    "Discworld MUD rose garden and player meeting hubs.",
    "Hubs and rose garden (location)",
    "location, lore",
    [
        "https://dwwiki.mooo.com/wiki/Rose_garden",
        "https://discworld.starturtle.net/lpc/playing/documentation.c?path=%2Fconcepts%2Ffaq",
    ],
    [
        "LOCKED — Rose garden is a common **player meeting** reference on wiki (orientation, not a shop).",
        "LOCKED — Good place for approved newbie questions — human controls channel spam.",
        "LOCKED — Not a substitute for guild advance rooms or shops.",
        "LOCKED — Log meeting location from game text if helping a corpse recovery (`discworld-death-recovery`).",
    ],
    ["Live player gatherings — session-specific."],
))
LEAFLETS.append((
    "discworld-location-lancre-kaup",
    "discworld-location-lancre-kaup",
    "Discworld MUD Lancre countryside and Kaup.",
    "Lancre countryside (location)",
    "location, city",
    [
        "https://dwwiki.mooo.com/wiki/Lancre",
        "https://dwwiki.mooo.com/wiki/Carriages",
    ],
    [
        "LOCKED — Ramtop countryside farms/forests between villages; weather differs from AM city.",
        "LOCKED — Reach via **Lancre Kingdom carriage** stops or walking with human-approved supplies.",
        "LOCKED — Witch herb gathering may occur outdoors — `gather` help in-game.",
        "LOCKED — Wilderness combat: `wimpy` + `flee` (`discworld-fight-wimpy-flee`).",
    ],
    ["Hidden paths in Kaup — wiki lacks path graph (Lancre page one paragraph)."],
))
LEAFLETS.append((
    "discworld-location-roundworld-connection",
    "discworld-location-roundworld-connection",
    "Discworld MUD Roundworld easter-egg areas.",
    "Roundworld connections (location)",
    "location, lore",
    [
        "https://dwwiki.mooo.com/wiki/Roundworld",
        "https://discworld.starturtle.net/lpc/playing/documentation.c?path=%2Fconcepts%2Ffaq",
    ],
    [
        "LOCKED — Roundworld links are canon easter eggs; wiki Roundworld page describes concept.",
        "LOCKED — Human must opt in before spoiler exploration.",
        "LOCKED — Access often quest-locked — read room messages, do not invent keys.",
        "LOCKED — No credentials or out-of-game URLs in logs.",
    ],
    ["Current quest requirements — wiki Roundworld page marks some areas without walkthrough."],
))

# --- fight (5 except skills-advance) ---
def fight_leaflet(dirname, help_path, title, locked, unknown):
    LEAFLETS.append((
        dirname,
        dirname,
        f"Discworld MUD fighting guide: {title.lower()}.",
        title,
        "fight",
        [
            f"https://discworld.starturtle.net/lpc/playing/documentation.c?path=%2Fhelpdir%2F{help_path}",
            "https://discworld.starturtle.net/lpc/playing/documentation.c?path=%2Fconcepts%2Ftaskmaster",
        ],
        locked,
        unknown,
    ))


fight_leaflet(
    "discworld-fight-combat-basics",
    "kill",
    "Combat basics",
    [
        "LOCKED — Use `kill` only with human OK; parse target names from room text.",
        "LOCKED — Loot only when rules and human allow; quest items need explicit OK.",
        "LOCKED — Illegal acts (guards) — stop when game warns.",
        "LOCKED — Chain with `consider` and `wimpy` sibling leaflets.",
    ],
    ["Damage formulae — not required for playbooks (helpdir kill focuses on syntax)."],
)
fight_leaflet(
    "discworld-fight-consider",
    "consider",
    "Consider",
    [
        "LOCKED — `consider <target>` estimates difficulty vs your skills (helpdir consider).",
        "LOCKED — Re-run after equipment or skill changes.",
        "LOCKED — If output warns of death, get human approval or skip.",
        "LOCKED — Colour/tier wording — read live output.",
    ],
    ["Exact colour code thresholds — terminal-dependent."],
)
fight_leaflet(
    "discworld-fight-wimpy-flee",
    "wimpy",
    "Wimpy and flee",
    [
        "LOCKED — `wimpy` auto-flees at low HP (helpdir wimpy); pair with `flee` toward known exits.",
        "LOCKED — In AM flee toward lit streets (`discworld-ankh-survival`).",
        "LOCKED — Tune threshold with human after near-death experiences.",
        "LOCKED — Stop if guards intervene.",
    ],
    ["Optimal wimpy % per guild — build-specific."],
)
fight_leaflet(
    "discworld-fight-tactics",
    "tactics",
    "Tactics and options",
    [
        "LOCKED — `tactics` and `options combat` adjust attitude (helpdir tactics).",
        "LOCKED — Match tactics to weapon type and guild.",
        "LOCKED — Human OK before aggressive tactics in cities.",
        "LOCKED — Revisit after weapon change.",
    ],
    ["Boss tactic presets — encounter-specific."],
)
LEAFLETS.append((
    "discworld-fight-newbie-greg",
    "discworld-fight-newbie-greg",
    "Discworld MUD newbie combat training with Greg.",
    "Newbie combat (Greg)",
    "fight",
    [
        "https://discworld.starturtle.net/lpc/playing/documentation.c?path=%2Fconcepts%2Ffaq",
        "https://discworld.starturtle.net/lpc/playing/documentation.c?path=%2Fnewbie%2Fwarriors_guild",
    ],
    [
        "LOCKED — FAQ describes **Greg** in newbie combat area for practice fights.",
        "LOCKED — Answer his prompt; **sobriety** matters (buy food/drink discipline — `discworld-shop-general`).",
        "LOCKED — Leave when asked; training rate slows over time.",
        "LOCKED — TM fighting skills while practicing (`discworld-skills-experience`).",
    ],
    ["Path from your spawn to Greg — follow in-game signs; FAQ does not give speedwalk."],
))

# --- weapons (5) ---
LEAFLETS.append((
    "discworld-weapon-swords",
    "discworld-weapon-swords",
    "Discworld MUD swords and fencing skills.",
    "Swords",
    "weapon, shop, fight",
    [
        "https://dwwiki.mooo.com/wiki/Swords",
        "https://discworld.starturtle.net/lpc/playing/documentation.c?path=%2Fhelpdir%2Fjudge",
    ],
    [
        "LOCKED — Sword family uses `fighting.melee.sword` / fencing subtree (wiki Swords).",
        "LOCKED — Buy from named AM shops in `discworld-shop-weapons` (Tenth Egg, Treacle, Elm).",
        "LOCKED — `judge` weapon quality needs `adventuring.evaluating.weapons` 5+ (weapons wiki).",
        "LOCKED — Weight affects burden (`discworld-weapon-armour-encumbrance`).",
    ],
    ["Best sword per warrior spec — build-specific."],
))
LEAFLETS.append((
    "discworld-weapon-axes",
    "discworld-weapon-axes",
    "Discworld MUD axes and heavy blades.",
    "Axes",
    "weapon, fight",
    [
        "https://dwwiki.mooo.com/wiki/Axes",
        "https://dwwiki.mooo.com/wiki/Weapons",
    ],
    [
        "LOCKED — Axe skills under fighting.melee; large axes on sale at Kernab's / Elm Forge (Kefka listings).",
        "LOCKED — Two-handed axes affect shield use and tactics.",
        "LOCKED — Sharp damage type vs armour layers (weapons wiki).",
        "LOCKED — Human OK before expensive two-handed purchase.",
    ],
    ["Named artefact axes — quest spoilers."],
))
LEAFLETS.append((
    "discworld-weapon-polearms",
    "discworld-weapon-polearms",
    "Discworld MUD polearms and spears.",
    "Polearms",
    "weapon, fight",
    [
        "https://dwwiki.mooo.com/wiki/Polearms",
        "https://dwwiki.mooo.com/wiki/Weapons",
    ],
    [
        "LOCKED — Polearms include spears/halberds (wiki Polearms table).",
        "LOCKED — Spears sold at AM weapon emporia (e.g. Tenth Egg list in Kefka).",
        "LOCKED — Reach weapons — tactics interaction per helpdir tactics.",
        "LOCKED — Check skill requirements on item before buy.",
    ],
    ["Shop availability outside AM — confirm via Kefka city filter."],
))
LEAFLETS.append((
    "discworld-weapon-thrown",
    "discworld-weapon-thrown",
    "Discworld MUD thrown weapons.",
    "Thrown and ranged",
    "weapon, fight",
    [
        "https://dwwiki.mooo.com/wiki/Thrown",
        "https://dwwiki.mooo.com/wiki/Weapons",
    ],
    [
        "LOCKED — Thrown skills listed under fighting tree (wiki Thrown).",
        "LOCKED — Ammo retrieval/loot rules from combat messages.",
        "LOCKED — Assassin thrown builds — guild-specific (`discworld-guild-assassin`).",
        "LOCKED — `consider` before ranged hunts.",
    ],
    ["Optimal thrown combo — build-specific."],
))
LEAFLETS.append((
    "discworld-weapon-armour-encumbrance",
    "discworld-weapon-armour-encumbrance",
    "Discworld MUD armour burden and encumbrance.",
    "Armour and encumbrance",
    "weapon, fight, shop",
    [
        "https://dwwiki.mooo.com/wiki/Encumbrance",
        "https://dwwiki.mooo.com/wiki/Armours",
        "https://discworld.starturtle.net/lpc/playing/documentation.c?path=%2Fhelpdir%2Fvurdere",
    ],
    [
        "LOCKED — Heavy armour/weapons increase burden; affects dodge (wiki Encumbrance).",
        "LOCKED — `vurdere` armour; `judge` weapons when skill permits.",
        "LOCKED — Buy armour at Elm Street Forge / Tenth Egg armoury (`discworld-shop-armour`).",
        "LOCKED — Balance weapon skill with defence training.",
    ],
    ["Optimal armour sets — level-dependent."],
))

# --- lore (4 except death) ---
LEAFLETS.append((
    "discworld-lore-races-species",
    "discworld-lore-races-species",
    "Discworld MUD playable species — humans only.",
    "Races and species (lore)",
    "lore",
    [
        "https://discworld.starturtle.net/lpc/playing/documentation.c?path=%2Fconcepts%2Fraces",
        "https://discworld.starturtle.net/lpc/playing/documentation.c?path=%2Fconcepts%2Fnationality",
    ],
    [
        "LOCKED — **Only humans** are playable (races concept doc); nationality replaces species choice.",
        "LOCKED — Nationality sets language, accent, currency, start region (`discworld-character-creation`).",
        "LOCKED — Witch join **gender** rule is guild-specific, not a human race gate — verify guild help.",
        "LOCKED — NPC species lore (elves allergic to iron, etc.) is flavour — not player races.",
    ],
    ["Per-nationality quest arcs — nationality doc lists nations but not every quest."],
))
LEAFLETS.append((
    "discworld-lore-gods-patrons",
    "discworld-lore-gods-patrons",
    "Discworld MUD gods and priest patrons.",
    "Gods and patrons (lore)",
    "lore, guild",
    [
        "https://discworld.starturtle.net/lpc/playing/documentation.c?path=%2Fnewbie%2Fpriests_guild",
        "https://dwwiki.mooo.com/wiki/Gods",
    ],
    [
        "LOCKED — Many Disc gods; priests choose **patron** at join (priests_guild).",
        "LOCKED — Temples are city landmarks — find via game, not invented names.",
        "LOCKED — Rituals consume faith/components per help.",
        "LOCKED — Roleplay respect for divine NPCs.",
    ],
    ["Full god spell trees — in-game help only."],
))
LEAFLETS.append((
    "discworld-lore-books-tiffany",
    "discworld-lore-books-tiffany",
    "Discworld MUD book lore — witches and Tiffany Aching themes.",
    "Book lore (witches and Tiffany)",
    "lore, guild",
    [
        "https://dwwiki.mooo.com/wiki/Tiffany_Aching",
        "https://dwwiki.mooo.com/wiki/Bad_Ass",
    ],
    [
        "LOCKED — Lancre witch play echoes Pratchett witch books at high level (wiki Tiffany Aching).",
        "LOCKED — Use lore for tone, not puzzle solutions.",
        "LOCKED — Bad Ass / young witch themes tie to Ramtops locations.",
        "LOCKED — Spoiler-sensitive book quests — human opts in.",
    ],
    ["Quest text tied to specific novels — not harvested."],
))
LEAFLETS.append((
    "discworld-lore-guild-politics",
    "discworld-lore-guild-politics",
    "Discworld MUD guild politics, Watch, and city law.",
    "Guild politics and law (lore)",
    "lore, guild, city",
    [
        "http://discworld.starturtle.net/lpc/playing/documentation.c?path=%2Fconcepts%2Fankh-morpork",
        "https://dwwiki.mooo.com/wiki/Ankh-Morpork",
    ],
    [
        "LOCKED — AM has Watch and licensed Thieves' Guild in canon; illegal theft risks fines/jail.",
        "LOCKED — Heed guard warnings in game text before continuing crime.",
        "LOCKED — Assassin contracts are lethal PvP — human must approve.",
        "LOCKED — Player org politics are live — not documented in static help.",
    ],
    ["Patrician questline state — session-specific."],
))


def main():
    for row in LEAFLETS:
        write_skill(*row)
    print(f"Wrote {len(LEAFLETS)} leaflets")


if __name__ == "__main__":
    main()
