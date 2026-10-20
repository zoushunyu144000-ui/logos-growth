"""Score leads 0-100 and assign tier (A=contact first, B=nurture, C=low, X=skip).

Weights live in config/scoring.json so they can be tuned from real reply/close data.
"""
import json
import os
from collections import Counter
from datetime import date

from common import MASTER, ROOT, free_subdomain, is_social_or_directory, read_csv, signals_of, write_csv

CFG = json.load(open(os.path.join(ROOT, "config", "scoring.json"), encoding="utf-8"))


def weaknesses(row):
    """Website-weakness tags from search evidence plus objective audit results."""
    w = signals_of(row) & set(CFG["weakness"])
    site = row.get("website", "")
    if not site:
        w.add("no_website")
    if free_subdomain(site):
        w.add("free_subdomain")
    if row.get("audit_at"):
        if not row.get("http_status", "").startswith(("2", "3")):
            w.add("broken_hint")
        if row.get("https") == "no":
            w.add("no_https")
        if row.get("mobile_viewport") == "no":
            w.add("not_mobile_hint")
        y = row.get("copyright_year")
        if y and y.isdigit() and int(y) <= date.today().year - 3:
            w.add("stale_copyright")
    return w


def score(row):
    w = weaknesses(row)
    ranked = sorted(w, key=lambda s: -CFG["weakness"][s])
    pts = CFG["weakness"][ranked[0]] if ranked else 0
    pts += CFG["extra_weakness"] * min(2, max(0, len(ranked) - 1))
    why = list(ranked)
    for s in sorted(signals_of(row) & set(CFG["business"])):
        pts += CFG["business"][s]
        why.append(s)
    if row.get("website") and not is_social_or_directory(row["website"]):
        pts += CFG["reachable_site"]
        why.append("reachable_site")
    psi = row.get("psi_mobile", "")
    if psi.isdigit() and int(psi) < 50:
        pts += 5
        why.append(f"psi{psi}")
    ind = (row.get("industry") or "").lower()
    for key, bonus in CFG["industry_bonus"].items():
        if key in ind:
            pts += bonus
            why.append(f"niche:{key}")
            break
    pts += CFG["country_bonus"].get(row.get("country", ""), 0)
    pts = max(0, min(100, pts))
    t = CFG["tiers"]
    tier = "A" if pts >= t["A"] else "B" if pts >= t["B"] else "C"
    if row.get("status") == "skip":
        tier = "X"
    return pts, tier, " ".join(why)


def main():
    rows = read_csv(MASTER)
    for r in rows:
        s, tier, why = score(r)
        r["score"], r["tier"], r["score_reasons"] = str(s), tier, why
        if r.get("status") in ("", "new", "audited", "qualified"):
            r["status"] = "qualified" if tier == "A" else ("audited" if r.get("audit_at") else "new")
    rows.sort(key=lambda r: -int(r["score"] or 0))
    write_csv(MASTER, rows)
    print("tiers:", dict(Counter(r["tier"] for r in rows)))


if __name__ == "__main__":
    main()
