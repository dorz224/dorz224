---
name: ugc-script-writer
description: Write AI UGC video ad scripts (40–60s) for Meta Reels / TikTok, written as on-screen actions, plus realism rewrites, claims-compliance checks, 20-hook variations for hook testing, sound-off on-screen text hooks, post captions and sub-40-character headlines. Use when the user asks for UGC scripts, ad scripts, rewriting competitor ads for their product, hooks, ad captions, headlines, or making a script sound less like an ad.
---

# UGC Script Writer (Steps 2, 2b, 3, 5)

Requires the brand context from `ugc-pipeline` step 0: landing page, **claims file**, best scripts, reviews, voice. Use angles and customer quotes from `ugc-angle-mining` when available.

## Ground rules for every script

- **Every scene is an action on screen.** Video tools build what they can see. "She pours the powder into her water bottle at the gym" gives the tool a scene; "this supplement supports energy" leaves it with a person standing still.
- **Only claims in the claims file.**
- **Plain, casual language**, the way a real customer talks.
- **40–60 seconds read aloud.** Estimate at ~2.5 spoken words/second (about 100–150 words) and state the estimate.
- Read it out loud and time it: if a line sounds like an ad, rewrite it; if it runs over 60s, cut it.

## Step 2: write the scripts

**The rewrite prompt** (the one the author uses most):

```text
Here are 10 transcripts from competitor ads that have run for months. For each one, keep the hook, the problem, and the call to action, and rewrite the rest for our product using our landing page and claims file. Write each scene as an action on screen. Keep each script to 40 to 60 seconds when read out loud.
```

**The fresh script prompt:**

```text
Write a 45 second UGC script for [product]. The person on camera is [age, look, situation]. They have [problem, using a real customer quote]. Structure: a hook in the first 3 seconds, the problem in their own words, finding the product, one specific result, and a casual close. Write it as scenes, each with what's happening on screen and what they say.
```

Output format per script: a table of scenes (# | on screen | they say | ~sec), then the total word count and estimated runtime.

## Step 2b: make it sound real, then check it

Polished scripts sound like ads, and viewers scroll past ads.

**Realism prompt:**

```text
Rewrite this script so it sounds like a real person filming on their phone. Add 2 small stumbles, like restarting a sentence or pausing to think. Use short, casual sentences. Keep every claim the same.
```

**Claims check** (run on every script before it gets built, after the realism pass):

```text
Compare this script to our claims file. List any sentence that claims something the file doesn't support, and suggest a safer version.
```

Show the check result even when it is clean ("No unsupported claims").

## Step 3: hooks

The hook is the first 3 seconds and decides whether anyone watches the rest. Once a script works, keep the body and test new hooks on it.

```text
Here is a script that performs well: [script]. Write 20 new opening lines for it. Keep each under 12 words. Use a mix of: a surprising claim, a question, a confession, a mistake the viewer is probably making, and a specific number. Each one must lead naturally into the second line of the script.
```

Return a table: # | hook | type | word count. Testing method: make 5–10 versions of the same ad changing **only the hook**; the winner becomes the new starting point. Suggest the ad names (`format_avatar_hook_version`) for the variants.

## Step 5: the text around the video

**On-screen text hooks:**
```text
Write 10 on-screen text lines for the first 2 seconds of this ad. Each should work with the sound off, and be under 8 words.
```

**Post captions:**
```text
Write 5 short captions for this ad. Casual, no hashtags, and each one ends with a reason to click.
```

**Headlines:**
```text
Write 10 headlines under 40 characters that point at the main result, using our claims file only.
```

Show character/word counts for each so limits are verifiable.

## Hand-off

When the user picks scripts, offer `ugc-scene-builder` to split them into 6–8 scenes for the video tool.
