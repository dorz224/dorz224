---
name: ugc-pipeline
description: Entry point for making AI UGC video ads for Meta (Facebook/Instagram Reels) and TikTok, end to end, using the "Claude does the thinking, a video tool does the building" workflow. Use when the user wants to plan or run an AI UGC ad batch, set up a brand Project for ad writing, run their weekly ad routine, name ads for analysis, or automate competitor-ad research. Routes to ugc-angle-mining, ugc-script-writer, ugc-scene-builder and ugc-results-analysis for each stage.
---

# AI UGC Pipeline

Source: @CEO_Vlad's guide on using Claude for AI UGC (a brand doing ~$200k/day where nearly every ad starts as a Claude prompt). The division of labour:

- **Claude**: angles, scripts, hooks, scene breakdowns, reading ad data.
- **Video tool**: turns the scene list into a finished ad (avatar, consistent character, captions). The author uses Infinite UGC (infiniteugc.com). In this workspace, Higgsfield is connected and can do the same job (see ugc-scene-builder).
- **The human**: makes the calls in between (which angles, which ads go live, budgets).

## Stages and which skill runs them

| Step | Stage | Skill |
|---|---|---|
| 0 | Brand context setup | this skill (below) |
| 1 | Find angles (reviews, competitor ads, 1–2★ reviews, buyer profiles) | `ugc-angle-mining` |
| 2 / 2b / 3 / 5 | Scripts, realism, claims check, hooks, on-screen text, captions, headlines | `ugc-script-writer` |
| 4 / 6 | Split script into scenes, build the ad in the video tool | `ugc-scene-builder` |
| 7 | Read ad results, decide what to make next | `ugc-results-analysis` |
| 8 | Automate research and logging | this skill (below) |

Work out where the user is, then load the matching skill. For a full run, go in order and stop for the user's choice after angles and after scripts.

## Step 0: brand context comes first

Every prompt in the pipeline assumes the brand's real information is loaded. Before writing anything, make sure you have (from a claude.ai Project, files in the workspace, or pasted text):

1. **Landing page copy** (copy + offer)
2. **Product file**: ingredients/specs and the **claims you are allowed to make**
3. **Best scripts**: the 10 best-performing scripts so far
4. **Reviews**: 100–200 customer reviews
5. **Brand voice**: a short voice note

If the claims file is missing, ask for it before writing scripts. Every later prompt depends on it, and it is what keeps ads from being rejected.

Project instructions to give the user (for a claude.ai Project), or to follow yourself:

```text
You write scripts for AI UGC ads for [brand]. Only make claims listed in the claims file. Write every scene as something happening on screen. Write in plain, casual language, the way a real customer talks.
```

In a Claude Code workspace, suggest keeping these as files in a `brand/` folder (`landing-page.md`, `claims.md`, `best-scripts.md`, `reviews.txt`, `voice.md`) so every skill can read them.

## Ad naming convention (set this up before anything goes live)

Name every ad `format_avatar_hook_version`, e.g. `podcast_woman40_confession_v3`. Use lowercase, use no underscores inside a part, and use the same vocabulary every week. Then results can be grouped by format, avatar and hook straight from the name (`ugc-results-analysis` does this automatically).

## Weekly routine

| Day | Who | What |
|---|---|---|
| Mon | Claude | Read new competitor ads + reviews, list new angles (`ugc-angle-mining`) |
| Mon | Claude | Write scripts and 20 hooks for each (`ugc-script-writer`) |
| Tue | Claude → human | Split scripts into scenes; build the batch in the video tool (`ugc-scene-builder`) |
| Tue | Human | Everything goes live at ~$20/day per ad |
| Fri | Claude | Read results, say what to make next (`ugc-results-analysis`) |
| Fri | Human + Claude | Make 20 new versions of whatever worked |

Launching ads, setting budgets and spending money always wait for the user's explicit go-ahead.

## Step 8: automate the boring parts (Claude Code)

Useful small tools to build in this repo when the user asks:

- A script that pulls new **long-running** competitor ads every Monday. Use the Meta connector (`ads_library_search`) or AdWhispr (`get_brand_ads` sorted by longevity) rather than scraping.
- A script that downloads and transcribes those ads (the author uses SnapTik for TikToks; transcription via a speech-to-text model such as Whisper).
- A sheet or CSV that logs every ad, its hook, and its results (keyed by the ad name above).

**One rule:** test every automation on 10 items first, then run it on everything.

## Stack (from the guide)

- Claude: angles, scripts, hooks, scene breakdowns, reading ad data
- Infinite UGC (infiniteugc.com): scripts → finished ads, with avatars, animation, editing (author's tool; plans from $77/mo). Higgsfield is the connected alternative here.
- Meta Ad Library (facebook.com/ads/library): competitor ads that have run for months
- SnapTik (snaptik.app): download TikToks to get transcripts
- Meta Ads Manager (adsmanager.facebook.com): export ad results as CSV, or read them live through the Meta / Windsor.ai connectors

## Related skills

`meta-ads-prompt-library` (broader 47-prompt Meta library: static ads, policy, fatigue) and `ad-media-prompt-playbook` (prompting Higgsfield/Seedance etc. for the visuals). Use them alongside this pipeline; don't duplicate their work.
