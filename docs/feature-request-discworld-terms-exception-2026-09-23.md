# FR: Discworld terms — exception to proceed (issue #38)

**Issue:** https://github.com/SimonBarnett/mud-skill/issues/38  
**Simon (`#bobiverse` 2026-09-23):** we have to get the agent past this;
we have permission for an exception — the skill should make it clear he
can proceed.

## Summary

Issue #38 harvested the accept prompt that #34 left UNKNOWN. The playtest
body said send `no` and stop. **Simon overrides that:** this fleet has
permission for an exception. The skill must tell the next agent to
**proceed** (send `yes` at the observed prompt), not decline.

Keep the observed prompt text LOCKED. Do not invent a room after `yes`.
Do not ship a client.

## Gap vs main (`7bfbb5b`)

Front door (#34 / PR #36) still says: stop, do not accept, human plays.
That blocks the agent. Simon requires the opposite for this exception.

## LOCKED

1. Prompt text observed on 2026-09-22 (issue #38). After the 30 second
   wait, exactly:

   ```
   Enter 'yes' if you agree to the terms or 'no' if you cannot.
   By typing 'yes' you signify that you have read, understand and agree to be
   bound by these terms and conditions: [yes/no]
   ```

2. Terms still include `Use of robot scripts or triggers is not permitted.`
   Send nothing during the 30 second wait.

3. **Exception (Simon 2026-09-23):** this fleet has permission to proceed.
   The skill must say so in clear numbered steps. At the yes/no prompt the
   agent sends `yes` and continues the existing playbooks. Do not send
   `no`. Do not stop for a human to accept.

4. Observed if someone sends `no`: `Come back soon!` then EOF. Document
   that as the decline outcome only, not the agent action.

5. TLS 4245 banner and telnet-option refusal from #38 may be recorded.
   Port 23 stays cited, not re-tested. No "disable TLS verify" step.

6. No passwords. `tools/Validate-MudSkill.ps1` stays green. No UAT stamp.

## UNKNOWN

- What the game prints after `yes` (rooms, newbie path). Not observed.
  Do not invent.
- Menu `N` versus `G` after the screenreader question.

## Paste / edit

| Fact | Owner skill |
|------|-------------|
| Prompt text; exception: send `yes` and proceed; decline `no` → Come back soon (not our path) | `mud-skill` |
| Same; drop the old "do not accept / hand to human" stop | `discworld-character-creation` |
| After `yes`, continue (do not stop before `look` for terms) | `discworld-mud` |
| Exception pointer: Discworld proceed is allowed for this fleet | `mud-character-creation` |
| Ankh ritual may start after the agent has sent `yes` | `discworld-ankh-survival` |
| Dated note: prompt observed; Simon exception to proceed | `docs/skill-harvest-log.md` |

## Acceptance

- A1: Yes/no prompt text is LOCKED. No invented wording.
- A2: Numbered exception: agent sends `yes` and proceeds. Skill states
  the permission clearly. Agent action is not `no`.
- A3: `no` / `Come back soon!` is documented as decline-only.
- A4: No secrets, no client, no invented post-`yes` rooms, no UAT stamp.
- A5: BT0 exits 0.

Workers do not stamp UAT.
