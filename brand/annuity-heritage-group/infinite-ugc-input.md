# Infinite UGC input: "7.25%. Locked." v3 (36s cut, Starter plan)

Paste each block into the matching Infinite UGC field. The source is `hero-ad-v3.md`.

## 1. Avatar image (becomes the first frame)

**Image Gen** tab. Settings: 9:16 · count **2** (not 4) · **remove the logo upload** · style preset **none** (or Selfie UGC if "none" isn't offered) · pick the most photoreal people model in the model dropdown.

Paste:

```text
Unretouched front-camera phone selfie, frozen from a video call. A 64-year-old American woman, an ordinary retiree, not a model: uneven skin tone, real wrinkles and crow's feet, a few age spots, slightly frizzy grey hair, short and not salon-styled, a little under-eye puffiness, no makeup except faded lipstick. Reading glasses pushed up on top of her head. Faded navy cotton cardigan over a grey t-shirt. She sits at a slightly cluttered kitchen table: a chipped coffee mug and a stack of mail, out of focus. Flat overcast daylight from a window on her left, slightly cool and a bit underexposed. Held at arm's length by an older iPhone, slightly below eye level, tilted a few degrees, wide-angle distortion, visible noise, mild JPEG compression. Mid-sentence, mouth slightly open, eyes on the lens, neutral and friendly, not smiling for a photo. Hands out of frame.
No paper, no documents, no phone, no text, no numbers, no logos anywhere in the image.
Avoid: symmetrical model face, glossy or airbrushed skin, perfect white teeth, salon hair, golden-hour glow, warm orange grade, blurry studio background, staged props, posed grin, perfectly centered framing.
```

Pick the one that looks most like a real person's video call. If both look fake, regenerate with count 1. Don't move on until the face is right.

## 2. Product

- **Product photo:** skip it if the video flow allows. If it's required, upload your **real logo file** (not a screenshot of a generated one). Your real rate comparison screenshot goes in as b-roll over scene 7 in the editor, not into the generation.
- **Product name, exactly as spoken in the script:** `Annuity Heritage Group`

## 3. Format

Tall, **9:16** (TikTok and Reels).

## 4. Script (paste as scenes)

```text
Scene 1 (4s) — Kitchen table, phone at arm's length. She pulls her reading glasses down onto her nose, leans in, eyebrows up, half-laugh.
"7.25%. Locked. Yeah… read that twice."

Scene 2 (5s) — Same. Sits back, talks to camera, matter-of-fact, one small shrug.
"Fixed annuity. Set years, set rate. Like a CD, but from an insurance company."

Scene 3 (3s) — Same. Taps the table once with one finger, firm.
"Locked for the whole term. Every year."

Scene 4 (5s) — Same. Glances up as if doing math in her head, then back to the lens with a small nod.
"On a hundred grand, that's seventy-two fifty a year."

Scene 5 (4s) — Same. Raises one eyebrow, knowing look.
"Tax-deferred, too. No tax bill every year like a CD."

Scene 6 (3s) — Same. Takes her glasses off, half-smile.
"The number's real. So is the fine print."

Scene 7 (7s) — Same. Leans toward the camera, conversational.
"Annuity Heritage Group is independent. We compare 40+ carriers side by side for your age and amount."

Scene 8 (3s) — Same. Points down toward the bottom of the screen, casual.
"Check it before the rate moves. Link's below."
```

**No paper, notepad, tax form or phone screen in any scene.** The AI invents fake numbers on anything with writing on it; your test images showed rate sheets reading 4.50%–6.75% and math reading $4,750 and $5,150, which contradicts your 7.25% ad. Every number goes in as an editor overlay (section 8), where you type it exactly.

## 5. Voice

**Seedance 2.0**, or **Google Omni** if the voice sounds off. Warm, American, mid-60s woman, conversational, not salesy.

## 6. Before you pay: check the preview

- Planned length should be **about 34–36s**. The Starter plan limit is under 40s.
- If it comes back over 38s, cut scene 5 completely (−4s). The tax point is still in the ad copy.
- Check the image and clip counts.

## 7. Check the scene plan

Look at each scene image before it builds. If one is wrong, fix only that scene, for example:
- "scene 4, no paper or notepad, she only looks up and nods"
- "scene 7, same framing as scene 1, nothing in her hands"

## 8. Finish in the editor

Add these as on-screen text overlays (captions on):

| Scene | Overlay |
|---|---|
| 1 | **7.25%. Locked.** |
| 2 | Fixed annuity = set years, set rate |
| 3 | Every year. Not just year one. |
| 4 | $100,000 → $7,250/yr · $250,000 → $18,125/yr · $500,000 → $36,250/yr |
| 5 | Tax-deferred |
| 6 | Read the fine print. We show it. |
| 7 | 40+ carriers · side by side |
| 8 | **See your rate ↓** |

Add your required compliance disclosure text as a footer if your lawyer specifies one.

## 9. Hook variants (same ad, replace only scene 1's line)

Export each one under its own name:

| Export name | Scene 1 line |
|---|---|
| `selfie_woman63_readittwice_v3` | "7.25%. Locked. Yeah… read that twice." |
| `selfie_woman63_cdrenewed_v3` | "Your CD renewed at half this? Read this twice." |
| `selfie_woman63_wallstreet_v3` | "One bad year can wipe out a decade. Not this." |
| `selfie_woman63_beware_v3` | "They say beware of annuities. So read the fine print." |
| `selfie_woman63_dollars_v3` | "Seventy-two fifty a year on a hundred grand. Locked." |
| `selfie_woman63_scam_v3` | "Sounds like a scam? Read it twice." |

Use Infinite UGC's per-clip regenerate (50% off) on scene 1 only, rather than rebuilding the whole ad.

## 10. Launch

- Ad copy: see `hero-ad-v3.md` → Copy.
- ~$20/day per variant, ad names exactly as above.
- After 3–5 days, export results from Ads Manager as CSV and send it to me. I'll run `ugc-results-analysis`.
