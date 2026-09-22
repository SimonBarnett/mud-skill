# Build/test plan: Discworld terms exception (#38)

1. Read issue #38 + this FR. Simon's IRC exception wins over the issue's
   "send no" ask.
2. Edit the five owner skills + harvest log. LOCK the observed prompt.
   Agent action is `yes` / proceed. Keep `no` → `Come back soon!` as
   decline-only. Do not invent rooms or a client.
3. Run `tools/Validate-MudSkill.ps1` (BT0). Must exit 0.
4. Open PR linking #38. Do not stamp UAT.
