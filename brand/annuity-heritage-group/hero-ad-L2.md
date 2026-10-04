# Hero ad: "7.25%. Locked." with advisor L2

**Name:** `advisor_man55_readittwice_v1` · 9:16 · ~35s · 720p · Seedance 2.5 with native voice
**Presenter:** L2 (55-year-old Caucasian American advisor, office desk), still `6da9e278-e70a-4056-a4e3-df179f71913b`
**Voice consistency:** every clip uses the hook proof-of-concept clip `dc4faea6-94dc-4aa2-9756-9dadd1e8c681` as a voice-only reference.
**Ad button:** Learn More → book a free call.

## Script (final)

| Clip | Sec | Line |
|---|---|---|
| 1 | 11 | "Seven point two five percent, locked. Yeah… you'll want to read that twice. It's a fixed annuity. You pick the number of years, the rate is set, and it's locked for the whole term." |
| 2a | ~5 | "So on a hundred thousand dollars, that's seven thousand two hundred and fifty dollars a year." |
| 2b | ~8 | "And there's no tax bill every year like with a CD. You only pay when you take your money out. The number's real. So is the fine print." (approved wording from the original "7.25% Locked" script; replaces "tax-deferred", which the model kept slurring) |
| 3 | 11 | "We're independent, so we compare forty-plus carriers side by side for your age and amount. Tap Learn More and book a free call with one of our specialists." |

## Pronunciation lessons (keep for every script)

- **"Read that twice"** is ambiguous: the model said "reed" when we meant past-tense "red". Use "you'll want to read that twice" (present tense, "reed"), or avoid the word.
- **"Seventy-two fifty a year"** is heard as $72.50. Say dollar amounts in full: "seven thousand two hundred and fifty dollars".
- **"Tax-deferred"** came out slurred ("tax-to-first") twice, even with a pronunciation cue. Avoid the word in spoken lines; say "no tax bill every year… you only pay when you take your money out" and put "tax-deferred" in an on-screen overlay if needed.
- Write numbers as words inside the dialogue ("seven point two five percent", "forty-plus").
- QC every clip by transcribing it (faster-whisper in the Higgsfield sandbox). If two models mishear a word, a viewer will too.
- For QC and trim timing use `base.en` with `vad_filter=False, condition_on_previous_text=False`. `small.en` with default settings silently dropped whole sentences, which made the auto-trim cut real speech.

## Clips

| Clip | Job | Status |
|---|---|---|
| 1 | `b9315789-a872-495a-8509-d8be37c25917` | ✅ transcript matches the script |
| 2 (v1) | `478b6118-6111-47ed-bd5a-185f65051d2b` | ❌ "$72.50" ambiguity, "tax-deferred" slurred |
| 2 (v2) | `4f165672-2593-4dfb-a98a-d9ff230d0bc2` | ✅ "$7,250 a year" now clear; "tax-deferred" still slurred, so only the first ~4.8s is used (2a) |
| 2b | `6bfd6014-02eb-4129-b9f3-324147bc7ffe` | ✅ tax line without the word "deferred" |
| 3 | `8307889e-9723-416c-91e4-5337d429ca25` | ✅ transcript matches the script |

## Assembly

Stitched in the Higgsfield sandbox. Each clip is trimmed to 0.12s before the first word and 0.3s after the last word (0.9s on the last clip, to keep the closing smile); hard cuts; 30 fps; loudness normalized to -14 LUFS, true peak -1 dBTP.

## Final deliverables (2026-10-04)

All 34.5s, loudness -14 LUFS, hard cuts. Final transcript verified end to end.

| File | Use | URL |
|---|---|---|
| 9:16 with overlays | Reels, Stories, TikTok | https://d2ol7oe51mr4n9.cloudfront.net/user_3EHQ6Sxu6BlVaZPwEbzGVWsOVqi/ebcf68ca-baf0-418c-a649-87d63fa55a50.mp4 |
| 1:1 with overlays (cropped higher so the head isn't cut) | Facebook/Instagram Feed | https://d2ol7oe51mr4n9.cloudfront.net/user_3EHQ6Sxu6BlVaZPwEbzGVWsOVqi/c251af83-64ce-4d80-ac64-d19917ab6032.mp4 |
| 4:5 with overlays | Feed (alternative to 1:1) | https://d2ol7oe51mr4n9.cloudfront.net/user_3EHQ6Sxu6BlVaZPwEbzGVWsOVqi/deb45ef3-e52f-4566-8b68-8b1296d0deb6.mp4 |
| 9:16 clean (no text) | For your own edit | https://d2ol7oe51mr4n9.cloudfront.net/user_3EHQ6Sxu6BlVaZPwEbzGVWsOVqi/eb5e1689-473d-43c1-8527-9a32471dc8ff.mp4 |

Overlays (Montserrat ExtraBold, white on 62% black, at chest height, inside every crop):
0–4.6s "7.25%. LOCKED." · 10.9–15.7s "$100,000 = $7,250 a year" · 15.7–20.4s "No tax bill every year" · 23.5–29.6s "40+ carriers, side by side" · 30.3–34.4s "Book your free call"

**Meta setup:** CTA button **Learn More** → booking page. Upload the 9:16 for Stories/Reels and the 1:1 (or 4:5) for Feed using placement asset customization, so Meta doesn't auto-crop. Add any lawyer-required disclosure in the primary text or as an extra overlay.

**Cost (from Higgsfield transactions):** 427 credits for the hero ad: hook test 35, clips 1–3 first pass 245 (91 + 77 + 77), clip 2 redo 91, tax-line clip 56. The first clip 2 (91) was discarded.
