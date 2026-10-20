"""Write personalised first-touch outreach drafts for tier-A leads.

Drafts only. Every draft lands in outreach/drafts/ with status draft_ready and must be
approved by the owner before anything is sent. Observations come only from the lead's
recorded evidence/audit fields; nothing is invented.
"""
import json
from datetime import date
import os
import re
import sys

from common import MASTER, ROOT, domain_of, free_subdomain, is_social_or_directory, read_csv, signals_of, write_csv

OUT = os.environ.get("LEADGEN_OUTREACH", os.path.join(ROOT, "outreach", "drafts"))
SENDER = json.load(open(os.path.join(ROOT, "config", "sender.json"), encoding="utf-8"))


def observations(r):
    """Plain-English, verifiable observations, most persuasive first."""
    obs = []
    sig = signals_of(r)
    has_site = r.get("website") and not is_social_or_directory(r.get("website", ""))
    if "oneflare" in (r.get("source_url") or "") and not has_site:
        obs.append("now that Oneflare has closed (it shut on 30 June), the profile I found for you there "
                   "can no longer send you enquiries, and I couldn't find a website of your own to take its place")
    elif not has_site:
        if "facebook_only" in sig:
            obs.append("customers searching for you land on a Facebook page rather than your own website")
        else:
            obs.append("I couldn't find a website of your own, only directory listings")
    if has_site and free_subdomain(r["website"]):
        obs.append(f"your website lives on a free builder address ({domain_of(r['website'])}) rather than "
                   "your own domain, which can make an established business look newer than it is")
    if r.get("audit_at"):
        if r.get("http_status") == "0" or r.get("http_status", "").startswith("5"):
            obs.append("your website didn't load when I tried it")
        if r.get("mobile_viewport") == "no":
            obs.append("the site isn't set up for phones, so it shows as a shrunken desktop page on mobile")
        if r.get("https") == "no":
            obs.append("the site has no HTTPS, so Chrome labels it \"Not secure\"")
        y = r.get("copyright_year")
        if y and y.isdigit() and int(y) <= date.today().year - 4:
            obs.append(f"the footer still says {y}, which can make visitors wonder if you're still trading")
        if r.get("has_form") == "no" and r.get("has_booking") == "no":
            obs.append("there's no quick enquiry or booking form")
        if r.get("psi_mobile", "").isdigit() and int(r["psi_mobile"]) < 50:
            obs.append(f"Google's mobile speed test scores it {r['psi_mobile']}/100")
    else:
        if "stale_copyright" in sig:
            obs.append("parts of the site look like they haven't been updated in a few years")
        if "no_https" in sig:
            obs.append("the site doesn't appear to use HTTPS")
        if "old_builder" in sig and not free_subdomain(r.get("website", "")):
            obs.append("the site seems to run on an older builder template")
    return obs[:2]


def draft(r):
    obs = observations(r)
    if not obs:
        return None
    name = re.sub(r"\s*\(.*?\)", "", r["business_name"]).strip()
    has_site = r.get("website") and not is_social_or_directory(r.get("website", ""))
    concept = "a refreshed homepage" if has_site else "a simple website"
    first = obs[0][0].upper() + obs[0][1:]
    extra = f" I also noticed {obs[1]}." if len(obs) > 1 else ""
    city = r.get("city") or "your area"
    subject = f"Quick idea for {name}'s website" if has_site else f"Quick idea for {name}"
    body = f"""Hi {name} team,

I was looking at {(r.get('industry') or 'local').split('/')[0]} businesses in {city} and came across yours. {first}.{extra}

For a local {(r.get('industry') or 'small').split('/')[0]} business, that's usually where new customers decide whether to call or move on.

I run a small web studio and build fast, mobile-first sites for owner-run businesses. If it's useful, I'm happy to mock up a free one-page concept of what {concept} could look like for you, no strings attached.

Would that be worth a look?

{SENDER['name']}
{SENDER['studio']} · {SENDER['website']}
{SENDER['postal_address']}
If you'd rather not hear from me, just reply "no thanks" and I won't contact you again.
"""
    return subject, body


def main():
    """Draft for the top-N qualified leads only, so each batch stays reviewable."""
    top = int(sys.argv[1]) if len(sys.argv) > 1 else 20
    os.makedirs(OUT, exist_ok=True)
    rows = read_csv(MASTER)
    n = 0
    for r in rows:
        if n >= top:
            break
        if r.get("tier") != "A" or r.get("status") not in ("qualified",):
            continue
        d = draft(r)
        if not d:
            continue
        subject, body = d
        path = os.path.join(OUT, f"{r['lead_id']}.md")
        with open(path, "w", encoding="utf-8") as f:
            f.write(f"---\nlead_id: {r['lead_id']}\nbusiness: {r['business_name']}\n"
                    f"country: {r.get('country')}\nchannel: email (contact: {r.get('contact_email') or 'TO FIND on their contact page'})\n"
                    f"status: draft_pending_approval\nevidence: {r.get('evidence','')}\nsource: {r.get('source_url','')}\n---\n\n"
                    f"**Subject:** {subject}\n\n{body}")
        r["status"] = "draft_ready"
        n += 1
    write_csv(MASTER, rows)
    print(f"wrote {n} drafts to {OUT}")


if __name__ == "__main__":
    sys.exit(main())
