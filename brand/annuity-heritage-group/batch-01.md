# Annuity Heritage Group — UGC batch 01

Built with the ugc-pipeline skills on 2026-10-04.

**Inputs used:** your 6 scripts (`best-scripts.txt`), your 3 live Meta ads, and Fisher Investments' ads (via AdWhispr).
**Claims:** all lawyer-approved (see `claims.md`).
**Still to come:** customer reviews (your team is collecting them). The landing page can't be reached from this sandbox.

---

## 1. What's running now

**Your live ads** (Page ID 666227086575345) (Meta Ad Library, all started ~Sept 22):

| Ad | Headline | Angle |
|---|---|---|
| 28343729718569046 | 7.25%. Locked. Read It Twice | Skeptic + "like a CD" + fine print |
| 1370715968555829 | Fixed Annuities Paying 7.25% | Rate + "we scan 60 carriers" |
| 4172311416400206 | What's the Best Annuity in 2026? | Question + "no fees, doesn't lock up money" |

**Fisher Investments** (the big anti-annuity advertiser): their active annuity ads all run one angle:
> "Does guaranteed income and protection against market downturns sound too good to be true? It probably is. Investors with $1,000,000 or more should read this free report that sheds light on the pitfalls of annuities."

Format: text overlay and lifestyle video. Tone: fear. Offer: free report. Audience: $1M+. Their other evergreen offer is a retirement guide ("When to Retire"). Fisher spends heavily to teach your audience that annuities are a trap. That makes **skepticism the main objection** your ads have to beat, and it's also an opening. Your best ad already plays this ("I read it twice too… read the fine print").


**The rest of the market:** AdWhispr checked which US annuity advertisers are running ads right now.

| Advertiser | Active ads | What their headlines push |
|---|---|---|
| American Retirement Experts | 274 | "See What Your Savings Could Pay You", "Find the Right Annuity for You", "Turn Savings Into Income", "The IRS Loophole for Retirees" |
| Jim Fisher | 161 | Anti-annuity / retirement guide (adjacent) |
| Annuity Explained | 46 | Education |
| RetireWell Annuities | 37 | Annuity matching |
| AnnuityAdvantage | 16 | "Get Our Free Rate Report", "Compare Fixed-Rate Annuities" |
| Annuity Lock | 15 | Rate lock |
| Others seen in the ad library | | Modern Annuity Guru: "Lock In 6.95% Guaranteed"; Bayview Wealth: "Fixed Rates Up to 6.45% APY"; SurePath: "Potentially $8,450/Year Per $100,000" |

**What this tells you:**
- **Volume wins here.** The leader runs 274 ads, and nearly all of them use the same 2 headlines. Their edge is how many ads they test, not what the ads say.
- **Rates are the currency.** Competitors headline 6.45%–6.95%. **Your 7.25% is above every rate seen in competitor headlines**, so put the number up front (S6 below).
- **Some put it in dollars.** SurePath frames it as "$ per year per $100,000". At 7.25%, that's $7,250 a year on $100,000 (S6).
- **The 4 ad IDs you sent:** 1443491304285153 is Fisher Investments (covered above). The other 3 (1571656731350483, 1802550380876329, 2141880286541585) didn't come up in any search. The Meta connector can't look up an ad by its ID, so I can't see them yet. Paste their page names or a screen recording and I'll break them down.

## 2. Angles

No reviews yet, so these come from your scripts and the competitor ads. They get re-ranked once reviews are in.

| # | Angle | Problem | Evidence | Test |
|---|---|---|---|---|
| A1 | **Read it twice** (honest skeptic) | "Sounds too good to be true" | Your winning ad + Fisher's whole campaign | **1st** |
| A2 | **Like a CD, but…** | CD rates dropping, tax bill every year | Your winning ad | 1st (inside A1) |
| A3 | **"Annuities lock up your money" myth** | Fear of losing access | Your Myth script | 2nd |
| A4 | **Your advisor's shelf** (independent vs captive) | Only shown one company's products, hidden fees | Your F3C3 script | 2nd |
| A5 | **The market doesn't care when you retire** | Market drop right before or after retiring | Your 9% script, Fisher's fear tone | 3rd |
| A6 | **The rate gap** (7.25% vs what others advertise) | "Am I getting the best rate?" | Competitor headlines cluster at 6.45–6.95% | **1st** |
| A7 | **9% income guaranteed** (59+) | Income they can't outlive | Your 9% script (approved claim) | 2nd |

| A8 | **Terrified about retirement income** (teachers / public employees) | "terrified about retirement income" | R2 + a competitor targeting retired teachers | **1st** |
| A9 | **Work until 70 → retire at 62** | "I thought I'd have to work until 70" | R5 | 2nd |
| A10 | **Finally sleep** (market volatility) | "protected from market volatility" | R1 + Fisher's fear tone | 2nd (fold into S5) |

**Avatars to test** (now backed by reviews; full profiles in `reviews.md`): a career teacher aged 60–68; a business owner aged 55–62 with no pension; an analytical engineer aged 63–70; a CD holder aged 60–70 whose CD is maturing.

## 3. Scripts

Every script is written as on-screen actions, kept to 40–50s, with 2 small stumbles left in on purpose. Claims are limited to the approved list in `claims.md`.

### S1. Read It Twice v2 (clean rewrite of your winner)
**Name:** `selfie_woman63_readittwice_v2` · ~42s · ~105 words

| # | On screen | She says | s |
|---|---|---|---|
| 1 | Kitchen table, morning light. Woman, 63, reading glasses, holds a printed rate sheet close to her face, eyebrows up | "7.25% locked. Yeah… I read it twice too." | 3 |
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
| 6 | Host B holds up phone showing a ranked comparison | **B:** "We're independent. We compare 40+ carriers and rank the rates for your age and amount side by side. Takes about a minute." | 9 |
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

### S6. The rate gap
**Name:** `selfie_man66_rategap_v1` · ~44s · ~110 words

| # | On screen | He says | s |
|---|---|---|---|
| 1 | Living room recliner, man, 66, scrolling his phone, stops, raises eyebrows | "Every annuity ad I scroll past says six-point-something." | 4 |
| 2 | Turns the phone toward camera, showing a rate comparison | "This one's 7.25%. Locked." | 3 |
| 3 | Sets phone on his knee | "Fixed annuity, set years, set rate, and it's locked for the whole term. Every year, not just year one." | 7 |
| 4 | Grabs a notepad and pen, writes "$100,000 × 7.25%" | "On a hundred grand that's, uh… seventy-two fifty a year. I did the math twice." | 6 |
| 5 | Taps the notepad with the pen | "Tax-deferred too, so no tax bill every year like a CD. You pay when you take it out." | 7 |
| 6 | Picks phone back up | "Annuity Heritage Group's independent. They compare 40+ carriers and rank the top rates for your age and amount, side by side." | 9 |
| 7 | Leans back | "Takes about a minute. Check it before the rate moves. Link's below." | 5 |

### S7. 9% income guaranteed (59+)
**Name:** `selfie_woman61_income9_v1` · ~42s · ~105 words · reuses the approved wording from your "9% Income Guaranteed" script

| # | On screen | She says | s |
|---|---|---|---|
| 1 | Back patio, woman, 61, gardening gloves on, pauses and looks at camera | "Nine percent income, guaranteed, and your principal doesn't go backwards." | 4 |
| 2 | Pulls off a glove, half laugh | "I thought that sounded crazy too." | 2 |
| 3 | Sits on the patio step | "But that's exactly what certain annuities are offering. If you're fifty-nine or older and thinking about retiring… don't ignore this." | 8 |
| 4 | Gestures out at the yard | "The market doesn't care when you plan to retire." | 3 |
| 5 | Counts on fingers | "An annuity can create income you can't outlive, without putting your savings in front of market drops." | 7 |
| 6 | Shrugs, honest | "It isn't for everyone. But for the right person it, um… it changes the whole plan." | 6 |
| 7 | Holds up phone showing the free guide | "There's a free annuity guide below that explains how it works and if it makes sense for you. Or book a call with one of their specialists." | 9 |

### S8. 35 years of teaching (review R2)
**Name:** `selfie_teacher64_terrified_v1` · ~42s · first-person dramatization of Margaret Williams' review
**On screen for the whole ad:** "Dramatization based on a real client review. Individual results vary."

| # | On screen | She says | s |
|---|---|---|---|
| 1 | Woman, 64, cardigan, sitting at a kitchen table with a cardboard box of classroom things (apple mug, name plate) | "After thirty-five years of teaching, I was terrified about one thing." | 4 |
| 2 | Picks up the name plate, sets it down | "Retirement income. Not the pension part. The… the part after." | 5 |
| 3 | Looks at camera, honest | "Every ad I saw either promised the moon or said annuities were a trap." | 5 |
| 4 | Opens laptop, comparison page on screen | "Annuity Heritage Group actually walked me through it. They're independent, so they compared 40+ carriers for my age and amount." | 9 |
| 5 | Taps the screen | "Fixed rate, locked for the term. Principal not in the market." | 5 |
| 6 | Closes laptop, small smile | "Their personalized strategy gave me confidence and a clear path forward. Truly life-changing." | 7 |
| 7 | Picks up the apple mug, to camera | "If you're a teacher about to retire, start with their free guide. Link's below." | 5 |

### S9. Work until 70? (review R5, podcast duo)
**Name:** `podcast_duo_retire62_v1` · ~45s · Host A = host, 50s · Host B = annuity specialist, 40s · the specialist tells the client's story, so nobody impersonates the client
**On screen:** "Based on a real client review. Individual results vary."

| # | On screen | Dialogue | s |
|---|---|---|---|
| 1 | Two-shot, podcast set, Host B holding a printed review card | **B:** "This client told me, 'I thought I'd have to work until seventy.'" | 4 |
| 2 | Host A leans in | **A:** "And?" | 1 |
| 3 | Host B reads from the card | **B:** "'Their annuity strategy helped me retire at sixty-two with complete financial security.'" | 6 |
| 4 | Host A, skeptical face | **A:** "Okay, what's the catch? There's always a catch." | 3 |
| 5 | Host B, calm, counting on fingers | **B:** "Read the fine print. Surrender period, fees, what the rate actually is. That's why we put it all side by side." | 8 |
| 6 | Host B holds up phone with the ranked comparison | **B:** "We're independent. We compare 40+ carriers and rank the top rates for your exact age and amount in about sixty seconds." | 8 |
| 7 | Host A nods | **A:** "So if I'm a small business owner, no pension…" | 3 |
| 8 | Host B to camera | **B:** "That's exactly who should run the numbers. Link's below." | 4 |

## 4. Claims check (against `claims.md`)

| Script | Line | Approved claim | Status |
|---|---|---|---|
| S1 | "7.25% locked… for the whole term… every year" | P1, P2 | ✅ |
| S1, S6 | "Tax-deferred… no tax bill every year like a CD" | P3 | ✅ |
| S1 | "rate, carrier rating and fine print side by side… two minutes" | From the "7.25% Locked" original | ✅ |
| S2 | "part of your money out every year, no penalty" | P5 | ✅ |
| S2, S4, S5 | "principal isn't riding the stock market" | P4 | ✅ |
| S3, S6 | "independent… compare 40+ carriers… rank for your age and amount… about a minute" | C1, C2, C3 | ✅ ("40+" used in every ad so they don't contradict each other) |
| S3 | "the one with no annual fee isn't on their shelf" | P7 + F3C3 original | ✅ |
| S6 | "$7,250 a year on $100,000" | Simple math from P2 | ✅ Lawyer-approved (2026-10-04) |
| S6 | "every annuity ad I scroll past says six-point-something" | Comparison to competitors | ✅ Lawyer-approved (2026-10-04) |
| S7 | Whole script | P6, P8, from the "9% Income Guaranteed" original | ✅ |
| S4 | "the big number might be something else entirely" | General education, no product claim | ✅ |

| S8 | Margaret's review, quoted word for word | R2 (testimonial) | ⚠️ See the testimonial note below |
| S9 | David's review, quoted word for word | R5 (testimonial) | ⚠️ See the testimonial note below |

**Testimonial note (S8, S9):** the claims are true, but these scripts have an AI avatar deliver a real client's story. Before they run, your lawyer should confirm three things. (1) You have the clients' written consent to use their reviews in ads. (2) The on-screen disclosure wording in each script works for you. (3) Results like "retire at 62" need a "results not typical" line under FTC endorsement rules and state insurance advertising rules. S9 avoids the impersonation issue entirely by having the specialist tell the client's story. If your lawyer prefers that, I'll convert S8 to the same format.

## 5. 20 new hooks for your winner (S1, "Read It Twice")

Each one leads into line 2 ("It's a fixed annuity. Set number of years, set rate…").

| # | Hook | Type | Words |
|---|---|---|---|
| 1 | "7.25% locked. Yeah, I read it twice too." | Original | 8 |
| 2 | "My CD renewed at half this. So I looked." | Confession | 9 |
| 3 | "Is 7.25% guaranteed real? I checked the fine print." | Question | 9 |
| 4 | "My bank never mentioned this one." | Confession | 6 |
| 5 | "If your CD matures this year, watch this first." | Mistake | 9 |
| 6 | "7.25%. Every year. Not just the first one." | Number | 8 |
| 7 | "I thought this was a scam. It isn't." | Confession | 8 |
| 8 | "You're probably renewing your CD on autopilot." | Mistake | 7 |
| 9 | "What's the catch with a 7.25% fixed rate?" | Question | 8 |
| 10 | "Three words my CD never said: locked, every year." | Surprise | 9 |
| 11 | "I almost let my CD roll over. Glad I didn't." | Confession | 10 |
| 12 | "Why does this pay more than my bank?" | Question | 8 |
| 13 | "Sixty-three, retired, and I finally read the fine print." | Confession | 9 |
| 14 | "Stop comparing CDs to CDs." | Mistake | 5 |
| 15 | "7.25% locked for the whole term. I asked twice." | Number | 9 |
| 16 | "Nobody told me annuities could work like a CD." | Surprise | 9 |
| 17 | "Before you renew that CD, read this." | Mistake | 7 |
| 18 | "I don't trust big numbers. So I read everything." | Confession | 9 |
| 19 | "How is a fixed rate this high right now?" | Question | 9 |
| 20 | "My husband said 'too good to be true.' He was wrong." | Surprise | 11 |

Test 5–10 of these on the same body, changing only the hook, named `selfie_woman63_<hook>_v1`. Suggested first 6: 2, 3, 5, 7, 14, 20.


**10 more hooks in your customers' own words** (from `reviews.md`):

| # | Hook | Source | Words |
|---|---|---|---|
| 21 | "Thirty-five years of teaching, and I was terrified about one thing." | R2 | 11 |
| 22 | "I thought I'd have to work until 70." | R5 | 8 |
| 23 | "I can finally sleep. Here's why." | R1 | 6 |
| 24 | "I had no idea fixed indexed annuities could do this." | R6 | 10 |
| 25 | "My retirement worries turned into retirement excitement. Seriously." | R4 | 8 |
| 26 | "Retired at 62. I'd planned on 70." | R5 | 7 |
| 27 | "The market used to keep me up at night." | R1 | 9 |
| 28 | "Teachers, nobody explains this part of retirement." | R2 | 7 |
| 29 | "I spent my whole career planning for everyone else." | R4 | 9 |
| 30 | "I sold for thirty years. I still didn't know this." | R6 | 10 |

Hooks 21–30 quote client reviews, so the testimonial note in section 4 applies to them too.

## 6. Text around the video

**On-screen text, first 2 seconds** (works with sound off, under 8 words):
1. 7.25% locked. Every year.
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

1. **You:** have your lawyer check the testimonial note in section 4 (consent, disclosure wording, "results not typical").
2. **You:** for competitor ads 2141880286541585, 1802550380876329 and 1571656731350483, send the page names or screenshots. Facebook is blocked from this sandbox, and the Meta connector can't look up an ad by its ID.
3. **Later:** the full review export (100+). I'll re-mine and re-rank.
4. **Me, once you pick scripts:** build them in Higgsfield (quote before spending) or format them for Infinite UGC.
5. **Live:** ~$20/day per ad, named as above. On Friday, export results and I'll run `ugc-results-analysis`.
