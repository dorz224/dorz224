#!/usr/bin/env python3
"""Group a Meta Ads Manager CSV export by the parts of each ad's name.

Ads are expected to be named format_avatar_hook_version
(e.g. podcast_woman40_confession_v3). Ratios are recomputed from summed
totals, not averaged, so big and small ads are weighted correctly.

Usage: group_results.py results.csv [--min-spend 20] [--top 5]
"""
import argparse
import csv
import sys
from collections import defaultdict

# Lowercased substrings that identify each column in a Meta export.
# The first match wins; a "hold rate"/"ctr" column is used directly only
# when the raw counts needed to recompute it are missing.
COLUMNS = {
    "name": ["ad name"],
    "spend": ["amount spent", "spend"],
    "impressions": ["impressions"],
    "clicks": ["link clicks", "clicks (all)", "clicks"],
    "purchases": ["purchases", "results"],
    "plays3s": ["3-second video plays", "video plays at 3"],
    "thruplays": ["thruplays", "video plays at 100%"],
    "ctr": ["ctr"],
    "hold": ["hold rate"],
}
PARTS = ["format", "avatar", "hook", "version"]


def find_columns(header):
    lower = [h.strip().lower() for h in header]
    found = {}
    for key, needles in COLUMNS.items():
        # Count columns must not pick up derived ones like "CPM (cost per 1,000 impressions)".
        derived = key not in ("ctr", "hold", "name", "spend")
        for needle in needles:
            match = next((header[i] for i, h in enumerate(lower) if needle in h
                          and not (derived and (h.startswith(("cost per", "cpm", "cpc", "ctr")) or "rate" in h))),
                         None)
            if match:
                found[key] = match
                break
    return found


def num(value):
    try:
        return float(str(value).replace(",", "").replace("$", "").replace("%", "").strip())
    except ValueError:
        return 0.0


def load(path, min_spend):
    with open(path, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        cols = find_columns(reader.fieldnames or [])
        if "name" not in cols or "spend" not in cols:
            sys.exit(f"Need at least 'Ad name' and spend columns; found {reader.fieldnames}")
        rows = []
        for raw in reader:
            name = (raw.get(cols["name"]) or "").strip()
            if not name:
                continue
            row = {k: num(raw[c]) for k, c in cols.items() if k != "name"}
            row["name"] = name
            if row["spend"] < min_spend:
                continue
            parts = name.split("_")
            for i, part in enumerate(PARTS):
                row[part] = parts[i] if i < len(parts) and len(parts) >= 3 else "(unnamed)"
            rows.append(row)
        return rows, cols


def summarize(rows):
    total = defaultdict(float)
    for r in rows:
        for k in ("spend", "impressions", "clicks", "purchases", "plays3s", "thruplays"):
            total[k] += r.get(k, 0.0)
    out = {"ads": len(rows), "spend": total["spend"], "purchases": total["purchases"]}
    if total["impressions"] and total["clicks"]:
        out["ctr"] = 100 * total["clicks"] / total["impressions"]
    elif any("ctr" in r for r in rows):
        out["ctr"] = sum(r.get("ctr", 0) for r in rows) / len(rows)
    if total["plays3s"] and total["thruplays"]:
        out["hold"] = 100 * total["thruplays"] / total["plays3s"]
    elif any("hold" in r for r in rows):
        out["hold"] = sum(r.get("hold", 0) for r in rows) / len(rows)
    if total["impressions"] and total["plays3s"]:
        out["hook_rate"] = 100 * total["plays3s"] / total["impressions"]
    out["cpp"] = total["spend"] / total["purchases"] if total["purchases"] else None
    return out


def fmt(v, pct=False, money=False):
    if v is None:
        return "-"
    if money:
        return f"${v:,.2f}"
    return f"{v:.2f}%" if pct else f"{v:,.0f}"


def table(title, groups):
    print(f"\n## By {title}\n")
    print("| value | ads | spend | purchases | CTR | hook rate | hold rate | cost/purchase |")
    print("|---|---|---|---|---|---|---|---|")
    stats = sorted(((k, summarize(v)) for k, v in groups.items()),
                   key=lambda kv: (kv[1]["cpp"] is None, kv[1]["cpp"] or 0))
    for key, s in stats:
        print(f"| {key} | {s['ads']} | {fmt(s['spend'], money=True)} | {fmt(s['purchases'])} | "
              f"{fmt(s.get('ctr'), pct=True)} | {fmt(s.get('hook_rate'), pct=True)} | "
              f"{fmt(s.get('hold'), pct=True)} | {fmt(s['cpp'], money=True)} |")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("csv")
    ap.add_argument("--min-spend", type=float, default=0.0, help="skip ads below this spend")
    ap.add_argument("--top", type=int, default=5)
    args = ap.parse_args()

    rows, cols = load(args.csv, args.min_spend)
    print(f"# Ad results: {len(rows)} ads, columns used: "
          + ", ".join(f"{k}='{v}'" for k, v in cols.items()))
    unnamed = sum(1 for r in rows if r["format"] == "(unnamed)")
    if unnamed:
        print(f"\nNote: {unnamed} ads don't follow format_avatar_hook_version and are grouped as (unnamed).")

    for part in ("hook", "format", "avatar"):
        groups = defaultdict(list)
        for r in rows:
            groups[r[part]].append(r)
        table(part, groups)

    print(f"\n## Top {args.top} ads by cost per purchase\n")
    print("| ad | spend | purchases | CTR | hold rate | cost/purchase |")
    print("|---|---|---|---|---|---|")
    ranked = sorted((r for r in rows if r.get("purchases")),
                    key=lambda r: r["spend"] / r["purchases"])
    for r in ranked[: args.top]:
        s = summarize([r])
        print(f"| {r['name']} | {fmt(s['spend'], money=True)} | {fmt(s['purchases'])} | "
              f"{fmt(s.get('ctr'), pct=True)} | {fmt(s.get('hold'), pct=True)} | {fmt(s['cpp'], money=True)} |")


if __name__ == "__main__":
    main()
