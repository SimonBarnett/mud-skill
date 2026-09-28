## 2026-09-22 — CAST IRON foundation

Simon: ALL skills harvest like agentic_build. Learn → harvest back to
this repo. Seeded into `mud-skill` SKILL.md.
# Skill harvest log

## 2026-09-22 â€” seed

Simon `#bobiverse`: create mud-skill; harvest MUD + Discworld play skills.
P0 is seed skills + docs (no prior in-repo harvest source yet).
## 2026-09-22 — bob-job

Bob-job loop started on issue #1.

## 2026-09-22 — issue #3 (Ankh survival)

Harvested companion `discworld-ankh-survival` from GitHub issue #3 and public
newbie-oriented material (link-out only, no instance credentials):

- [Discworld MUD wiki](https://discworld.starturtle.net/) — city/guild orientation
- [discworldmud.org](https://www.discworldmud.org/) — official site newbie pointers

Ritual steps are agent procedure (lit streets, no early alley wander, score/HP,
guild recruiter, ask before pkill/theft); not copied verbatim from any one page.

## 2026-09-22 — harvest-mud-skill (issue #4)

Added dedicated `harvest-mud-skill` SKILL.md; `mud-skill` CAST IRON points at it.
Install/validator include the harvest skill (H1–H2).

## 2026-09-22 — issue #12 (seven working guilds)

Extended `discworld-mud` guild table with Priest, Assassin, and Fool as
UNKNOWN P1 stubs (S2 / G1). Warrior / Wizard / Witch / Thief rows unchanged
except table order aligned to public “seven guilds” lists.

Sources (link-out, no credentials):

- [Discworld MUD wiki](https://discworld.starturtle.net/) — guild / class orientation
- GitHub issue #12 — acceptance G1/G2 scope (no extra invented guilds)

## 2026-09-22 — issue #20 (playbook depth)

Expanded `discworld-mud` **Warrior** and **Witch** class playbooks (8–9 numbered
steps each) with LOCKED decision points and explicit UNKNOWN gaps. Harvested from
public newbie documentation only — no credentials or invented hosts.

Sources (link-out):

- [Warriors' Guild newbie doc](https://discworld.starturtle.net/lpc/playing/documentation.c?path=%2Fnewbie%2Fwarriors_guild)
- [Warrior specialisations newbie doc](https://discworld.starturtle.net/lpc/playing/documentation.c?path=%2Fnewbie%2Fwarrior_specialisations)
- [Witches' Guild newbie doc](http://discworld.starturtle.net/lpc/playing/documentation.c?path=%2Fnewbie%2Fwitches_guild)
- [Guide for young warriors](https://dwwiki.mooo.com/wiki/Guide_for_young_warriors) — etiquette pointers only
- [Guide for young witches](https://dwwiki.mooo.com/wiki/Guide_for_young_witches) — early skill themes only
- GitHub issue #20 — acceptance A1–A4 scope

## 2026-09-22 — issue #23 (much deeper skill pack)

Added **46** companion skills under `.grok/skills/discworld-*` (50 total with
seed skills) covering **city**, **location**, **shop**, **lore**, **fight**,
**weapon**, and **guild** surfaces. Facts are public wiki/site orientation
only; each leaflet marks LOCKED vs UNKNOWN. No credentials or invented ENAMEs.

Sources (link-out):

- [Discworld MUD wiki](https://discworld.starturtle.net/)
- [discworldmud.org](https://www.discworldmud.org/)
- GitHub issue #23 — acceptance A1–A5 scope

Harvest routing table extended in `harvest-mud-skill`; `discworld-mud` indexes
the pack. `tools/Install-MudSkill.ps1` installs all leaflets; BT0 checks count >= 50.

## 2026-09-22 — issue #26 (MORE — fill stubs)

Web search + public docs used to fill topic playbooks and expand shop/death/skills
leaflets. Added seven skills; appended `#26` agent playbooks to 38 short
`discworld-*` leaflets via `tools/Expand-Issue26Stubs.ps1`.

New skills:

- `mud-character-creation`, `discworld-character-creation`, `achaea-character-creation`
- `discworld-death-recovery`, `discworld-money-currency`, `discworld-travel-transport`
- `discworld-skills-experience`

Filled / expanded: all `discworld-shop-*`, `discworld-lore-death`,
`discworld-fight-skills-advance`, `discworld-city-ankh-morpork`, `mud-skill` topic
index, `discworld-mud` pack index.

Sources (link-out, no credentials):

- [Nationality](https://discworld.starturtle.net/lpc/playing/documentation.c?path=%2Fconcepts%2Fnationality), [races](https://discworld.starturtle.net/lpc/playing/documentation.c?path=%2Fconcepts%2Fraces), [rearrange](https://discworld.starturtle.net/lpc/playing/documentation.c?path=%2Fhelpdir%2Frearrange)
- [Newbie dying](http://discworld.atuin.net/lpc/playing/documentation.c?path=%2Fnewbie%2Fdying), [corpse](http://discworld.atuin.net/lpc/playing/documentation.c?path=%2Fconcepts%2Fcorpse), [Death wiki](https://dwwiki.mooo.com/wiki/Death)
- [Currency](https://dwwiki.mooo.com/wiki/Currency), [Money changer](https://dwwiki.mooo.com/wiki/Money_changer)
- [Travel](https://discworld.starturtle.net/lpc/playing/documentation.c?path=%2Fconcepts%2Ftravel), [Carriages](https://discworld.starturtle.net/lpc/playing/documentation.c?path=%2Fconcepts%2Fcarriages)
- [Taskmaster](https://discworld.starturtle.net/lpc/playing/documentation.c?path=%2Fconcepts%2Ftaskmaster), [advance](https://discworld.starturtle.net/lpc/playing/documentation.c?path=%2Fhelpdir%2Fadvance)
- [Achaea races](https://www.achaea.com/races), [Achaea newbie guide](https://www.achaea.com/newbie-guide)
- Shop locations: [Kefka DB](https://dw.daftjunk.com/items/index.php), [Elm Street Forge](http://dwmud.pbworks.com/w/page/18434059/Elm%20Street%20Forge)

Workers do not stamp UAT.

## 2026-09-22 — issue #26 FIX (MRB FAIL #29)

Replaced `Expand-Issue26Stubs.ps1` template stamps on **38** `discworld-*` leaflets with
topic-specific harvest via `tools/gen_issue26_mrb29_fix.py` (per-topic starturtle/dwwiki/Kefka
URLs). Filled shop leaflets **general / pawn / magic** with named AM shops + locations.
Removed deprecated expand script.

MRB #29 blockers addressed; re-hand MRB on new SHA. No UAT stamp.

## 2026-09-22 — playtest front door (issues #33 #34)

Live guest login on published Discworld port 4242, stopped at the terms
screen. Harvest is the menu, the four guest prompts, the 30 second wait,
name-banishment, and name-collision. No in-world room was seen, so city,
guild, fight, shop, and travel leaflets were not extended.

Source: https://discworld.starturtle.net/lpc/playing/getting_started.html
plus the session recorded on issue #33.

Workers do not stamp UAT.

## 2026-09-23 — terms exception (issue #38)

Playtest recorded the yes/no prompt. Decline (`no`) prints `Come back soon!` and closes. Simon granted an exception on #bobiverse: the agent sends `yes` and continues. The screen after `yes` was not observed.

Workers do not stamp UAT.

## 2026-09-23 — guest arrival at the Mended Drum (issues #41–#54)

After `yes` on guest `G`, the login `>` is not a room. The game queues `look`. The first room with `obvious exits` is the Mended Drum main bar. Pager `return to continue` takes a blank line. `quit` waits for `Do come again!`. A dropped link can leave a net-dead statue, which is not a corpse. New leaflet `discworld-location-mended-drum`. Purse is moths. New guest score recorded without a single HP or GP lock.

Workers do not stamp UAT.

## 2026-09-23 — Mended Drum brochure, exits, boxes, sign (issues #57–#62)

Playtest on plain TCP port 4242: ordinal `get 1st colourful brochure from tray`, open and page-one read, `look` previews vs bare `look`, north door closed, south entrance and up landing with sign, west preview only, Hibiscus and dart board and both newspaper boxes. Harvest into `discworld-location-mended-drum`, parser multiple-match rule in `mud-skill`, Drum trip limits in `discworld-ankh-survival` and `discworld-mud`. Source: GitHub issues #57–#62.

Workers do not stamp UAT.

## 2026-09-23 — brochure turn pages, floor copies, landing (issues #65–#68)

Playtest on plain TCP port 4242: `syntax turn` and tested turns to pages 2–6, page-7 error, six page reads (page 5 pager), `look my brochure`, drop and floor copies with `my` disambiguation, landing picture and lamp, `get colourful brochure 1` and failed `2nd` on a single tray copy, `ask` lines on urchin and Hibiscus. Harvest into `discworld-location-mended-drum`, parser/`my` rules in `mud-skill` item 9, guest experience variability and root `skills` in `discworld-skills-experience`. Source: GitHub issues #65–#68.

Workers do not stamp UAT.


## 2026-09-23 — parser here/in, one-page turns, rising guest experience

Playtest on plain TCP port 4242. Guests Motewqza, Motevqra, and Motelqbn each reached `Do come again!`. No password. Did not buy. Did not open the north door. Did not enter the west stage. Did not leave the Drum for the street.

Harvest:

- `get 2nd colourful brochure from tray` succeeds when the tray shows two. `my` is not a tray get. `here` matches room objects (`look at menu here`) and does not see a brochure that is on the tray. `look at colourful brochure in tray` sees the tray copy when one is shown. Unnumbered `get colourful brochure from tray` succeeded once after a replenish line when look had shown one; it still multiple-matches when two are already listed.
- `turn a page in my brochure`, `turn 1 page of my brochure`, and `turn to random page in my brochure`.
- Guest experience rose on Motewqza (171, 234, 401) and Motevqra (60, 153) while root `skills` stayed at 0. Hit points on these guests were 502 (502). Empty-handed inventory. `listen` and `smell` in the main bar.

Edited `discworld-location-mended-drum`, `mud-skill` item 9, `discworld-skills-experience`, and `discworld-money-currency`. Source: GitHub issues #78–#83.

Workers do not stamp UAT.

## 2026-09-24 — harvest-agent-skills foundation

Added `.grok/skills/harvest-agent-skills/SKILL.md` (honesty box). Frontmatter
`github:` is `https://github.com/SimonBarnett/mud-skill`. Skills root was
already `.grok/skills/`. Repo-local twin of the fleet foundation; game
leaflets unchanged. `tools/Validate-MudSkill.ps1` requires the foundation
file (`name`, `github:`, `/harvest-agent-skills`). Install already copies
every `SKILL.md`.

Workers do not stamp UAT.

## 2026-09-28 — Moteflmg guest (three tray brochures, XP 138)

Playtest on plain TCP port 4242. Guest Moteflmg reached `Do come again!`
(giant bird). No password. Did not buy. Did not get a brochure. Did not open
the north door. Did not leave the Drum for the street.

Harvest:

- `look tray` showed three colourful brochures. Tray count is not locked to
  one (or two).
- `score`: 500 (500) HP, 50 (50) GP, experience 138 at 57 seconds. Level 0
  Adventurers' Guild.
- Empty-handed inventory: unburdened / empty handed / purse moths.
- `listen` in the main bar: `You listen carefully.` then prompt.
- Front door and first room matched existing `mud-skill` / Mended Drum locks.

Edited `discworld-location-mended-drum`, `discworld-skills-experience`, and
`discworld-money-currency`. Source: GitHub issues #88–#92.

Workers do not stamp UAT.
