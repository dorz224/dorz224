---
name: ugc-results-analysis
description: Read Meta/TikTok ad results for UGC video ads and decide what to make next. Groups results by hook, format and avatar using the format_avatar_hook_version naming convention, diagnoses weak metrics (CTR, hold rate, cost per purchase), and proposes the next 10 ads based only on what is working. Use when the user shares an Ads Manager export/CSV, asks how their ads are doing, which hooks/avatars/formats win, or what creative to make next.
---

# UGC Results Analysis (Step 7)

Run after a few days of spend. Get the data one of three ways:

1. **Live, preferred:** Meta connector (`ads_get_ad_entities` and insights tools) or Windsor.ai (`get_data` with connector `facebook`). Stay read-only.
2. **CSV export** from Ads Manager: run the helper below first.
3. Pasted table.

## Helper script

```bash
python3 .claude/skills/ugc-results-analysis/scripts/group_results.py results.csv --min-spend 20
```

It parses each ad name as `format_avatar_hook_version`, groups by hook, format and avatar, recomputes CTR / hook rate / hold rate (ThruPlays ÷ 3-second plays) / cost per purchase from summed totals, and lists the top ads. Ads not following the naming convention are flagged. If names don't follow it, tell the user and suggest renaming going forward (`ugc-pipeline`).

## The analysis prompt

```text
Here are my ad results. Each row is one ad, with its hook, format, avatar, spend, click through rate, hold rate, and cost per purchase. Tell me: which hooks have the best click through rate, which formats keep people watching longest, which avatars have the lowest cost per purchase, and what the top 5 ads have in common. Then suggest 10 new ads to make next, based only on what's working.
```

## Diagnosing an ad

| Pattern | Meaning | Fix |
|---|---|---|
| Low CTR | The hook isn't working | New hooks on the same body (`ugc-script-writer` step 3) |
| Good CTR, people leave early | The hook promised more than the video delivered | Make the body pay off the hook, or pick a hook that matches the body |
| People watch, few buy | The product shows up too late | Move the product moment earlier |
| Strong everywhere except cost per purchase | Not a creative problem | Fix the offer or the landing page |

## Rules

- Don't call a winner on tiny spend. Flag ads under ~$20 spend or with fewer than ~3 purchases as "too early".
- Next ads come **only** from what's working: winning hook × new avatar, winning body × new hooks, winning format × new angle. On Fridays, the author makes 20 new versions of whatever worked.
- Each suggested ad gets a proposed name in `format_avatar_hook_version` form.
- Pausing ads, changing budgets or launching anything waits for the user.
