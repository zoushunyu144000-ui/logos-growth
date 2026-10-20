"""Shared schema and CSV helpers for the LOGOS lead pipeline (stdlib only)."""
import csv
import os
import re
from datetime import date
from urllib.parse import urlparse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.environ.get("LEADGEN_DATA", os.path.join(ROOT, "leads"))
MASTER = os.path.join(DATA_DIR, "master.csv")

RAW_COLS = ["country", "city", "industry", "business_name", "website", "source_url",
            "evidence", "signals", "has_own_site", "found_via"]
AUDIT_COLS = ["audit_at", "http_status", "final_url", "https", "mobile_viewport",
              "copyright_year", "generator", "load_ms", "page_kb", "has_tel_link",
              "has_form", "has_booking", "title", "meta_desc", "psi_mobile", "audit_notes"]
MASTER_COLS = (["lead_id"] + RAW_COLS + ["domain", "found_at"] + AUDIT_COLS +
               ["score", "tier", "score_reasons", "status", "contact_email",
                "contact_page", "last_action", "notes"])

# Pipeline status values. Nothing moves past "approved" without the owner.
STATUSES = ["new", "audited", "qualified", "draft_ready", "approved", "contacted",
            "replied", "call_booked", "proposal_sent", "won", "lost", "skip"]

SOCIAL_HOSTS = ("facebook.com", "instagram.com", "linktr.ee", "yelp.", "yellowpages",
                "hipages", "truelocal", "yell.com", "checkatrade", "google.com", "bbb.org")


FREE_SUBDOMAINS = ("weebly.com", "wixsite.com", "yolasite.com", "godaddysites.com",
                   "gosite.com", "business.site", "square.site", "webnode.", "site123.me", "jimdosite.com")


def free_subdomain(url):
    d = domain_of(url)
    return next((f for f in FREE_SUBDOMAINS if d.endswith(f) or f in d), "")


def today():
    return date.today().isoformat()


def domain_of(url):
    if not url:
        return ""
    if "://" not in url:
        url = "http://" + url
    host = urlparse(url).netloc.lower().split(":")[0]
    return host[4:] if host.startswith("www.") else host


def is_social_or_directory(url):
    d = domain_of(url)
    return any(h in d for h in SOCIAL_HOSTS)


def norm_key(row):
    """Dedup key: own-site domain if present, else name+city."""
    d = domain_of(row.get("website", ""))
    if d and not is_social_or_directory(row.get("website", "")):
        return "d:" + d
    name = re.sub(r"[^a-z0-9]", "", (row.get("business_name") or "").lower())
    city = re.sub(r"[^a-z0-9]", "", (row.get("city") or "").lower())
    return f"n:{name}|{city}"


def read_csv(path):
    if not os.path.exists(path):
        return []
    with open(path, newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def write_csv(path, rows, cols=MASTER_COLS):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = path + ".tmp"
    with open(tmp, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        for r in rows:
            w.writerow({c: r.get(c, "") for c in cols})
    os.replace(tmp, path)


def signals_of(row):
    return {s.strip() for s in (row.get("signals") or "").split(";") if s.strip()}
