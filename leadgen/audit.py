"""Audit each lead's homepage and record objective website signals.

Stdlib only. Polite: one request per site, 1.5s gap, honest User-Agent.
Optional Google PageSpeed Insights mobile score when PSI_API_KEY is set (free key).

Usage: python leadgen/audit.py [--limit N] [--force] [--offline-html FILE --url URL]
"""
import argparse
import json
import os
import re
import ssl
import sys
import time
import urllib.parse
import urllib.request
from datetime import date

from common import MASTER, is_social_or_directory, read_csv, today, write_csv

UA = "Mozilla/5.0 (compatible; LogosSiteCheck/1.0; +https://logos144000.com)"
BUILDERS = {
    "wix": r"wix\.com|X-Wix|_wixCssImports",
    "weebly": r"weebly\.com|Weebly",
    "squarespace": r"squarespace",
    "godaddy-builder": r"godaddy|img1\.wsimg\.com",
    "joomla": r"Joomla",
    "wordpress": r"wp-content|wp-includes",
    "shopify": r"cdn\.shopify\.com",
    "webflow": r"webflow",
    "jimdo": r"jimdo",
    "frontpage/dreamweaver": r"FrontPage|Dreamweaver",
    "flash": r"\.swf[\"']|shockwave-flash",
}
BOOKING = r"calendly|acuityscheduling|cliniko|fresha|timely|setmore|square\.site|opentable|resdiary|booksy|mindbody|halaxy|nookal"


def analyze_html(html, url, status=200, final_url=None, elapsed_ms=None):
    final_url = final_url or url
    low = html.lower()
    r = {
        "http_status": str(status),
        "final_url": final_url,
        "https": "yes" if final_url.startswith("https://") else "no",
        "mobile_viewport": "yes" if re.search(r'<meta[^>]+name=["\']viewport', low) else "no",
        "page_kb": str(round(len(html.encode("utf-8", "ignore")) / 1024)),
        "load_ms": str(elapsed_ms or ""),
        "has_tel_link": "yes" if 'href="tel:' in low or "href='tel:" in low else "no",
        "has_form": "yes" if "<form" in low else "no",
        "has_booking": "yes" if re.search(BOOKING, low) else "no",
    }
    years = [int(y) for y in re.findall(
        r"(?:©|&copy;|copyright)\s*(?:\d{4}\s*[-–]\s*)?((?:19|20)\d{2})", html, re.I)]
    r["copyright_year"] = str(max(years)) if years else ""
    gen = re.search(r'<meta[^>]+name=["\']generator["\'][^>]+content=["\']([^"\']+)', html, re.I)
    found = [name for name, pat in BUILDERS.items() if re.search(pat, html)]
    r["generator"] = (gen.group(1)[:40] if gen else "") or ",".join(found[:2])
    t = re.search(r"<title[^>]*>(.*?)</title>", html, re.I | re.S)
    r["title"] = re.sub(r"\s+", " ", t.group(1)).strip()[:120] if t else ""
    d = re.search(r'<meta[^>]+name=["\']description["\'][^>]+content=["\']([^"\']*)', html, re.I)
    r["meta_desc"] = d.group(1).strip()[:160] if d else ""
    notes = []
    if r["https"] == "no":
        notes.append("no HTTPS")
    if r["mobile_viewport"] == "no":
        notes.append("no mobile viewport")
    if r["copyright_year"] and int(r["copyright_year"]) <= date.today().year - 3:
        notes.append(f"footer year {r['copyright_year']}")
    if not r["meta_desc"]:
        notes.append("no meta description")
    if r["has_tel_link"] == "no":
        notes.append("phone not tap-to-call")
    if r["has_form"] == "no" and r["has_booking"] == "no":
        notes.append("no enquiry form/booking")
    if "flash" in r["generator"]:
        notes.append("uses Flash")
    if re.search(r"http://[^\"']+\.(?:js|css|png|jpg)", html) and r["https"] == "yes":
        notes.append("mixed content")
    r["audit_notes"] = "; ".join(notes)
    return r


def fetch(url, timeout=20):
    if "://" not in url:
        url = "http://" + url
    ctx = ssl.create_default_context()
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "text/html"})
    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=ctx) as resp:
            body = resp.read(2_000_000).decode(resp.headers.get_content_charset() or "utf-8", "ignore")
            return resp.status, resp.geturl(), body, int((time.time() - t0) * 1000), None
    except ssl.SSLError as e:
        return 0, url, "", None, f"SSL error: {e.__class__.__name__}"
    except urllib.error.HTTPError as e:
        return e.code, url, "", None, f"HTTP {e.code}"
    except Exception as e:  # DNS failure, timeout, refused
        return 0, url, "", None, f"unreachable: {e.__class__.__name__}"


def psi_score(url):
    key = os.environ.get("PSI_API_KEY")
    if not key:
        return ""
    q = urllib.parse.urlencode({"url": url, "strategy": "mobile", "category": "performance", "key": key})
    try:
        with urllib.request.urlopen(
                f"https://www.googleapis.com/pagespeedonline/v5/runPagespeed?{q}", timeout=120) as r:
            data = json.load(r)
        return str(round(data["lighthouseResult"]["categories"]["performance"]["score"] * 100))
    except Exception:
        return ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--offline-html")
    ap.add_argument("--url")
    a = ap.parse_args()
    if a.offline_html:
        print(json.dumps(analyze_html(open(a.offline_html, encoding="utf-8").read(), a.url or ""), indent=2))
        return
    rows = read_csv(MASTER)
    done = 0
    for row in rows:
        site = row.get("website", "")
        if not site or is_social_or_directory(site) or (row.get("audit_at") and not a.force):
            continue
        status, final, body, ms, err = fetch(site)
        res = analyze_html(body, site, status, final, ms) if body else {
            "http_status": str(status), "final_url": final, "audit_notes": err or "empty response"}
        res["psi_mobile"] = psi_score(final) if body else ""
        res["audit_at"] = today()
        row.update(res)
        if row.get("status") in ("", "new"):
            row["status"] = "audited"
        done += 1
        print(f"{row['lead_id']} {site} -> {res.get('audit_notes', '')}", file=sys.stderr)
        if a.limit and done >= a.limit:
            break
        time.sleep(1.5)
    write_csv(MASTER, rows)
    print(f"audited {done} sites")


if __name__ == "__main__":
    main()
