---
name: ugc-scene-builder
description: Turn a UGC ad script into a 6–8 scene plan (setting, action, expression, dialogue, duration) with a consistent character, including animated styles (claymation, Pixar-style, skeleton) and two-host podcast formats, then build the video in Infinite UGC or the connected Higgsfield tools. Use when the user wants to break a script into scenes, storyboard a UGC ad, keep an AI avatar consistent across clips, set up a podcast-style two-host ad, or produce/generate the finished UGC video.
---

# UGC Scene Builder (Steps 4 and 6)

Video tools build an ad scene by scene, so the script needs clear scenes. Clear scenes mean the tool's plan comes back right the first time, with fewer fixes. Build the scene plan right the first time.

## Step 4: script → scenes

```text
Split this script into 6 to 8 scenes. For each scene, write: the setting, what the person is doing, their facial expression, what they say, and roughly how many seconds it lasts. Keep the same person and setting across scenes unless the script needs a change.
```

Every scene needs these five fields:

| Field | Question it answers |
|---|---|
| Setting | Where are we? |
| Action | What is happening? |
| Expression | How do they look? |
| Dialogue | What do they say? |
| Duration | How many seconds? |

**Keep it consistent:** same person + same setting across scenes unless the script requires a change. Durations should add up to the script's 40–60s.

**For animation styles** (claymation, Pixar-style, skeleton, mascot), add this to the prompt:

```text
Describe the main character in one line, including their colours, clothing, and one stand-out feature, so they look the same in every scene.
```

Repeat that one-line character description verbatim in every scene's prompt.

**Two-host / podcast format:** tools like Infinite UGC have a Host A / Host B setup (an image per host, dialogue split into "Host A says / Host B responds"). For this format, write the dialogue as alternating lines labelled Host A and Host B, give each host a one-line look description, and keep both in one setting (e.g. a podcast set with mics).

## Step 6: build the ad

What to enter (Infinite UGC terms; same inputs apply elsewhere):

- **Avatar image**: becomes the first frame
- **Product photo**, plus the product name **exactly as written in the script**
- **Tall format** (9:16) for TikTok and Reels
- **The script**, with the scenes from step 4
- **Voice model**: the author picks Seedance 2.0 or Google Omni when the voice matters most

Then:

1. **Check the preview before you spend:** confirm the planned length and the image/clip counts before anything is charged.
2. **Read the scene plan:** check each scene's image before the video builds. When one misses, fix only that scene with a specific instruction, e.g. "scene 3, she's holding the bottle up to the light".
3. **Finish in the editor:** captions, the on-screen hook from `ugc-script-writer`, any b-roll.

### Building with the connected Higgsfield tools

Infinite UGC has no connector here, so either hand the user the scene plan to paste into it, or build with Higgsfield:

- Read `ad-media-prompt-playbook` first for model-specific prompting.
- Follow Higgsfield's server instructions: multi-step videos start with `get_workflow_instructions`; UGC/ads go through `show_marketing_studio_v2`; consistent characters via the character-sheet / AI Influencer workflow; batch generations with the batch tools + `jobs_wait`.
- Quote the cost (e.g. `ads_studio_quote` or the preview the tool gives) and get the user's OK **before** generating anything that spends credits.
- Use 9:16, keep the character description identical across scenes, and regenerate single failed scenes rather than the whole ad.

## Output

A scene table (# | setting | action | expression | dialogue | sec), the one-line character description(s), total runtime, and the ad name (`format_avatar_hook_version`) to use when it goes live.
