# Annuity Heritage Group — UGC batch 01

Built with the ugc-pipeline skills on 2026-10-04.

**Inputs used:** your 6 scripts (`best-scripts.txt`), your 3 live Meta ads, and Fisher Investments' ads (via AdWhispr).
**Missing:** customer reviews, the landing page (the sandbox can't reach it), competitors 2 and 3 (still loading in AdWhispr), and an approved claims file. Rates appear as `[RATE]` until confirmed. See `claims-draft.md`.

---

## 1. What's running now

**Your live ads** (Meta Ad Library, all started ~Sept 22):

| Ad | Headline | Angle |
|---|---|---|
| 28343729718569046 | 7.25%. Locked. Read It Twice | Skeptic + "like a CD" + fine print |
| 1370715968555829 | Fixed Annuities Paying 7.25% | Rate + "we scan 60 carriers" |
| 4172311416400206 | What's the Best Annuity in 2026? | Question + "no fees, doesn't lock up money" |

**Fisher Investments** (the big anti-annuity advertiser): their active annuity ads all run one angle:
> "Does guaranteed income and protection against market downturns sound too good to be true? It probably is. Investors with $1,000,000 or more should read this free report that sheds light on the pitfalls of annuities."

Format: text overlay and lifestyle video. Tone: fear. Offer: free report. Audience: $1M+. Their other evergreen offer is a retirement guide ("When to Retire"). Fisher spends heavily to teach your audience that annuities are a trap. That makes **skepticism the main objection** your ads have to beat, and it's also an opening. Your best ad already plays this ("I read it twice too… read the fine print").

## 2. Angles

No reviews yet, so these come from your scripts and the competitor ads. They get re-ranked once reviews are in.

| # | Angle | Problem | Evidence | Test |
|---|---|---|---|---|
| A1 | **Read it twice** (honest skeptic) | "Sounds too good to be true" | Your winning ad + Fisher's whole campaign | **1st** |
| A2 | **Like a CD, but…** | CD rates dropping, tax bill every year | Your winning ad | 1st (inside A1) |
| A3 | **"Annuities lock up your money" myth** | Fear of losing access | Your Myth script | 2nd |
| A4 | **Your advisor's shelf** (independent vs captive) | Only shown one company's products, hidden fees | Your F3C3 script | 2nd |
| A5 | **The market doesn't care when you retire** | Market drop right before or after retiring | Your 9% script, Fisher's fear tone | 3rd |

**Avatars to test** (hypotheses until reviews confirm): a CD holder aged 60–70 whose CD is maturing; a 59–64 pre-retiree watching their 401(k); a 65+ retiree who already bought an annuity from a captive agent.

## 3. Scripts

Every script is written as on-screen actions, kept to 40–50s, with 2 small stumbles left in on purpose. Claims are limited to the "until confirmed" list in `claims-draft.md`.

### S1. Read It Twice v2 (clean rewrite of your winner)
**Name:** `selfie_woman63_readittwice_v2` · ~42s · ~105 words

| # | On screen | She says | s |
|---|---|---|---|
| 1 | Kitchen table, morning light. Woman, 63, reading glasses, holds a printed rate sheet close to her face, eyebrows up | "[RATE] locked. Yeah… I read it twice too." | 3 |
| 2 | Puts the sheet down, looks at the phone camera | "It's a fixed annuity. Set number of years, set rate. Kind of like a CD, except it's from an insurance company, not a bank." | 8 |
| 3 | Taps the rate on the page with one finger | "And the rate's locked for the whole term. Not just year one. Every… every year." | 5 |
| 4 | Holds up last year's 1099 from her CD, shakes it slightly | "It's also tax-deferred, so no tax bill every year like my CD. You pay when you take it out." | 8 |
| 5 | Flips the sheet over to the small print, half smile | "The number's real. So is the fine print. Read both." | 5 |
| 6 | Shows her phone screen: comparison page with rate, carrier rating, terms in columns | "Annuity Heritage Group puts today's rate, the carrier's rating and the fine print side by side. Took me, what, two minutes." | 9 |
| 7 | Back to camera, casual | "Do it before the rate moves. Link's below." | 4 |

### S2. The myth my brother-in-law told me
**Name:** `selfie_man64_myth_v1` · ~44s · ~110 words

| # | On screen | He says | s |
|---|---|---|---|
| 1 | Garage workbench, man, 64, flannel shirt, wiping hands on a rag, looking at camera | "My brother-in-law swore annuities lock your money up for ten years." | 4 |
| 2 | Leans on bench, shakes head | "That's why I ignored them. For, like, five years." | 4 |
| 3 | Picks up phone, scrolls | "Turns out some of them let you take part of your money out every year, no penalty." | 6 |
| 4 | Sets phone down, counts on fingers | "And on a fixed one, your principal isn't riding the stock market. A bad year doesn't take a bite out of it." | 8 |
| 5 | Shrugs | "There's still fine print. Surrender periods, all that. So I… I actually read it." | 6 |
| 6 | Holds phone to camera showing the free guide's cover | "Annuity Heritage Group has a free guide that explains it in plain English. Came straight to my email." | 8 |
| 7 | Tosses rag on bench, smiles | "Read it before you listen to your brother-in-law. Link's below." | 5 |

### S3. Your advisor's shelf (two-host podcast)
**Name:** `podcast_duo_shelf_v1` · ~48s · Host A = curious host, 50s · Host B = annuity specialist, 40s, podcast set with two mics

| # | On screen | Dialogue | s |
|---|---|---|---|
| 1 | Two-shot, podcast set, Host A leaning in | **A:** "Same savings, same age. Two annuities. Totally different results. Why?" | 4 |
| 2 | Close on Host B, calm | **B:** "Usually? Fees. And which company your advisor works for." | 4 |
| 3 | Host A frowns, tilts head | **A:** "Wait, they don't show you everything?" | 3 |
| 4 | Host B gestures as if pointing at a shelf | **B:** "Most advisors can only offer what their company carries. If the one with no annual fee isn't on their shelf, you just… never hear about it." | 9 |
| 5 | Host A nods slowly | **A:** "So how do you see the rest?" | 3 |
| 6 | Host B holds up phone showing a ranked comparison | **B:** "We're independent. We compare [40+] carriers and rank the rates for your age and amount side by side. Takes about a minute." | 9 |
| 7 | Host A laughs | **A:** "Make them compete for it." | 3 |
| 8 | Host B to camera | **B:** "Exactly. See what the whole market would pay you. Link's below." | 5 |

### S4. Too good to be true? (answers Fisher's angle)
**Name:** `selfie_man67_toogood_v1` · ~46s · ~115 words

| # | On screen | He says | s |
|---|---|---|---|
| 1 | Porch chair, man, 67, reading glasses on head, coffee mug, squinting at phone | "I keep seeing ads saying guaranteed income 'sounds too good to be true.'" | 4 |
| 2 | Lowers phone, looks at camera | "And honestly? Some annuity pitches are." | 3 |
| 3 | Holds up one finger | "Here's what's real: a fixed annuity gives you a set rate for a set number of years, and the market can't take your principal down." | 9 |
| 4 | Second finger | "Here's what you check: the surrender period, any fees, and whether that big number is the rate you earn or something else entirely." | 9 |
| 5 | Sips coffee, half laugh | "That last one… that's where people get burned." | 4 |
| 6 | Shows phone: side-by-side comparison page | "Annuity Heritage Group lays all of it out side by side, across a bunch of carriers. No pressure, no obligation." | 8 |
| 7 | Sets mug down | "Read it twice. Then decide. Link's below." | 4 |

### S5. The market doesn't care when you retire
**Name:** `selfie_woman60_markettiming_v1` · ~43s · ~105 words

| # | On screen | She says | s |
|---|---|---|---|
| 1 | Couch, woman, 60, looking at a 401(k) app on her phone, lips pressed | "I'm two years from retiring, and the market does not care." | 4 |
| 2 | Puts phone face-down on her lap | "A bad year right before you retire, or right after… that's the one that scares me." | 6 |
| 3 | Leans forward | "So I started looking at fixed annuities for part of it. Not all of it. Part." | 6 |
| 4 | Counts on fingers | "Set rate. Principal isn't exposed to market drops. Grows tax-deferred." | 6 |
| 5 | Shrugs, honest | "It isn't for everyone. There's a surrender period, you have to read the terms." | 5 |
| 6 | Shows the free guide cover on her phone | "Annuity Heritage Group sent me a free guide that walks through whether it fits you. Or you can just talk to a specialist." | 9 |
| 7 | Smiles, picks phone back up | "Worth ten minutes before the next bad year. Link's below." | 4 |

## 4. Claims check

| Script | Line | Issue | Safer version |
|---|---|---|---|
| S1 | "[RATE] locked" | Needs a current, sourced rate, plus term and minimum | Fill from rate sheet; add on-screen "Rate as of [date], [term]-yr, [carrier]" |
| S1 | "Took me two minutes" | Confirm the form length | "Took me a couple of minutes" if true |
| S2 | "part of your money out every year, no penalty" | Product-specific | Keep "some annuities"; free-withdrawal % varies |
| S3 | "[40+] carriers" | Your scripts say 40+, 60+ and "every" | Pick one number for all ads |
| S3 | "no annual fee" | Product-specific | "some have no annual fee" ✅ as written |
| S4 | "the market can't take your principal down" | True for fixed annuities, but subject to surrender charges and carrier strength | Keep; the fine-print line follows it |
| All | (no 9%/9.2% claims) | Left out on purpose | Use only with compliance-approved wording |

Not checked against a compliance reviewer or state rules. Annuity ads need sign-off before they run.

## 5. 20 new hooks for your winner (S1, "Read It Twice")

Each one leads into line 2 ("It's a fixed annuity. Set number of years, set rate…").

| # | Hook | Type | Words |
|---|---|---|---|
| 1 | "[RATE] locked. Yeah, I read it twice too." | Original | 8 |
| 2 | "My CD renewed at half this. So I looked." | Confession | 9 |
| 3 | "Is [RATE] guaranteed real? I checked the fine print." | Question | 9 |
| 4 | "My bank never mentioned this one." | Confession | 6 |
| 5 | "If your CD matures this year, watch this first." | Mistake | 9 |
| 6 | "[RATE]. Every year. Not just the first one." | Number | 8 |
| 7 | "I thought this was a scam. It isn't." | Confession | 8 |
| 8 | "You're probably renewing your CD on autopilot." | Mistake | 7 |
| 9 | "What's the catch with a [RATE] fixed rate?" | Question | 8 |
| 10 | "Three words my CD never said: locked, every year." | Surprise | 9 |
| 11 | "I almost let my CD roll over. Glad I didn't." | Confession | 10 |
| 12 | "Why does this pay more than my bank?" | Question | 8 |
| 13 | "Sixty-three, retired, and I finally read the fine print." | Confession | 9 |
| 14 | "Stop comparing CDs to CDs." | Mistake | 5 |
| 15 | "[RATE] locked for the whole term. I asked twice." | Number | 9 |
| 16 | "Nobody told me annuities could work like a CD." | Surprise | 9 |
| 17 | "Before you renew that CD, read this." | Mistake | 7 |
| 18 | "I don't trust big numbers. So I read everything." | Confession | 9 |
| 19 | "How is a fixed rate this high right now?" | Question | 9 |
| 20 | "My husband said 'too good to be true.' He was wrong." | Surprise | 11 |

Test 5–10 of these on the same body, changing only the hook, named `selfie_woman63_<hook>_v1`. Suggested first 6: 2, 3, 5, 7, 14, 20.

## 6. Text around the video

**On-screen text, first 2 seconds** (works with sound off, under 8 words):
1. [RATE] locked. Every year.
2. I read the fine print twice
3. Your CD vs. a fixed annuity
4. Myth: annuities lock up your money
5. Your advisor's shelf isn't the market
6. Too good to be true?
7. 2 years from retiring. Market doesn't care.
8. Before your CD renews, watch this
9. Same savings. Two very different annuities.
10. Rate, rating, fine print. Side by side.

**Headlines** (under 40 characters, claims from the draft list only):

| # | Headline | Chars |
|---|---|---|
| 1 | Compare Annuity Rates Side by Side | 34 |
| 2 | Your CD vs. a Fixed Annuity | 27 |
| 3 | Read the Fine Print Before You Buy | 34 |
| 4 | Free Annuity Guide, Sent Instantly | 34 |
| 5 | See What 40+ Carriers Would Pay You | 35 |
| 6 | Tax-Deferred. Rate Locked for the Term | 38 |
| 7 | Annuities Without the Sales Pitch | 33 |
| 8 | Independent Annuity Rate Comparison | 35 |
| 9 | Is an Annuity Right for You? | 28 |
| 10 | Fixed Rates for Your Age and Amount | 35 |

**Captions** (casual, no hashtags, each ends with a reason to click):
1. Read it twice before your CD renews. Today's rates and the fine print are one tap away.
2. Annuities aren't all the same, and your advisor probably can't show you all of them. See the full market here.
3. Thought annuities lock up your money for good? Not all of them. The free guide explains it in plain English.
4. Some annuity pitches are too good to be true. Here's how to tell which ones aren't.
5. If the market dropped the year you retired, what's your plan? Free guide below.

## 7. Next steps

1. **You:** confirm or fix `claims-draft.md` (most important: carrier count, current rate + source, 9% wording).
2. **You:** send 100–200 customer reviews (Google, Trustpilot or call notes). I'll re-rank the angles and swap in real customer quotes.
3. **You:** send competitors 2 and 3 as Ad Library links or Page names. Their profile IDs don't match their Page IDs.
4. **Me, once you pick scripts:** build them in Higgsfield (quote before spending) or format them for Infinite UGC.
5. **Live:** ~$20/day per ad, named as above. On Friday, export results and I'll run `ugc-results-analysis`.
