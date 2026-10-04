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

## Presenter stills (avatar / first frame)

The still sets the look of the whole ad, so get it right before spending video credits.

- **Describe what the viewer sees, never how it was filmed.** "Phone propped on a tripod", "selfie", "filming herself" make the model draw the gear into the frame. Write "vertical video still, eye-level medium shot of X talking directly to the viewer" and add: "no camera, phone, tripod, ring light, microphone, laptop, monitor or mirror anywhere in the frame."
- **Plan for Meta's 1:1 and 4:5 crops.** A centered 1:1 crop keeps only the middle ~56% of a 9:16 frame. Ask for a waist-up shot, centered, "top of the head about a quarter of the way down, face near the vertical center, hands in the lower-middle". Keep overlays inside the center square too.
- **Realism comes from specifics:** an ordinary person ("not a model"), real skin detail, everyday clothes, a lived-in room, flat or uneven, slightly underexposed light, "normal lens with no wide-angle distortion, slight sensor noise, true-to-life color". Avoid glossy skin, golden-hour glow, salon hair and posed grins.
- **Give the hands a job** (in the lap, on a counter or armrests). No paper, notepads or screens in shot: models invent fake numbers on them. Numbers go in as editor overlays.
- **Check the client's casting rules** (ethnicity, age, nationality, accent) before generating, and record them in the brand folder.
- **To re-frame a chosen presenter, keep the face** by using a reference-image model (e.g. Higgsfield `flux_3_image` with the still as `image_references`), not outpainting, which keeps the old selfie arm and angle.
- Generate cheap stills first (Soul 2.0 is ~0.12 credits), let the user pick, then animate one 5s test before the full ad.

## Voice delivery: never monotone (standing client feedback)

AI voices default to a flat, even, average delivery: same loudness, same pitch, same pace. Viewers hear that as AI. Fight it in the script, the prompt, the reference and the mix.

**Script**
- Vary sentence length: a two-word punch ("Locked.") next to a longer, running sentence.
- Write in asides, rhetorical questions and reactions: "Honestly?", "Look—", "Here's the thing", "No, really."
- Mark the one word per line that carries the meaning; the prompt will stress it.

**Prompt (per line, not one global "tone")**
- Don't use only "calm, unhurried, not salesy". That produced flat reads. Describe a performance: "animated, like telling a friend surprising news".
- For each line, give at least one of: the **stressed word** ("stress on LOCKED"), a **pitch move** ("rises on the question, drops on the answer"), a **pace change** ("rushes the aside, slows right down on the number"), a **volume change** ("drops to a near-whisper on 'so is the fine print'", "louder, more energy on the hook"), and a **beat** ("short pause and a breath before the number", "small laugh").
- Hook line: the most energy and the widest pitch range in the ad. CTA: warm, a bit quieter and closer, not a flat read-out.
- Keep it human-sized; it's a person talking, not a radio announcer.

**Voice reference**
- A voice reference passes its flatness on. Use an expressive take as the reference, or design one first (Seed Audio / Eleven v4 with lower stability and bracketed cues like [chuckles], [leans in]), then attach it to every clip.

**Mix**
- Don't squash the dynamics. Single-pass `loudnorm` with a low LRA flattens the performance. Use two-pass loudnorm in `linear=true` mode (or plain gain) to hit about -14 LUFS while keeping the natural range.

**QC**
- Listen for variation, not just correct words. Measure loudness range: `ffmpeg -i ad.mp4 -af ebur128 -f null -` and check the LRA. Below about 5 LU on a talking-head ad usually sounds flat; re-generate the flattest clip with stronger per-line direction.

## Output

A scene table (# | setting | action | expression | dialogue | sec), the one-line character description(s), total runtime, and the ad name (`format_avatar_hook_version`) to use when it goes live.
