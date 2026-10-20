"""Discover local businesses from OpenStreetMap (free, open data, ODbL) via Overpass.

Writes leads/raw_osm_<city>_<niche>.csv in the raw schema, ready for ingest.py.
OSM coverage of small businesses is partial, so a missing website tag means
"unknown", never "no website". Run where outbound network is open (laptop or CI).

Usage: python leadgen/discover_osm.py "Brisbane" "Australia" dentist
"""
import json
import os
import sys
import urllib.parse
import urllib.request

from common import DATA_DIR, RAW_COLS, today, write_csv

NICHES = {
    "dentist": '["amenity"="dentist"]',
    "physio": '["healthcare"="physiotherapist"]',
    "chiropractor": '["healthcare"="chiropractor"]',
    "plumber": '["craft"="plumber"]',
    "electrician": '["craft"="electrician"]',
    "builder": '["craft"="builder"]',
    "roofer": '["craft"="roofer"]',
    "gardener": '["craft"="gardener"]',
    "hairdresser": '["shop"="hairdresser"]',
    "beauty": '["shop"="beauty"]',
    "cafe": '["amenity"="cafe"]',
    "accountant": '["office"="accountant"]',
}
ENDPOINT = os.environ.get("OVERPASS_URL", "https://overpass-api.de/api/interpreter")


def query(city, niche):
    sel = NICHES[niche]
    return f"""[out:json][timeout:90];
area["name"="{city}"]["boundary"="administrative"]->.a;
(node{sel}(area.a); way{sel}(area.a););
out tags center 400;"""


def main():
    city, country, niche = sys.argv[1], sys.argv[2], sys.argv[3]
    data = urllib.parse.urlencode({"data": query(city, niche)}).encode()
    req = urllib.request.Request(ENDPOINT, data=data,
                                 headers={"User-Agent": "LogosLeadgen/1.0 (+https://logos144000.com)"})
    with urllib.request.urlopen(req, timeout=120) as r:
        els = json.load(r)["elements"]
    rows = []
    for e in els:
        t = e.get("tags", {})
        name = t.get("name")
        if not name or t.get("brand") or t.get("brand:wikidata"):
            continue  # skip unnamed and chain/franchise outlets
        site = t.get("website") or t.get("contact:website") or ""
        fb = t.get("contact:facebook") or ""
        sig = ["active_business"]
        if not site and fb:
            sig.append("facebook_only")
        if site.startswith("http://"):
            sig.append("no_https")
        rows.append({
            "country": country, "city": city, "industry": niche, "business_name": name,
            "website": site or fb, "source_url": f"https://www.openstreetmap.org/{e['type']}/{e['id']}",
            "evidence": "OSM listing" + ("; no website tag" if not site else ""),
            "signals": ";".join(sig), "has_own_site": "yes" if site else "unknown",
            "found_via": f"osm-overpass {today()}",
        })
    out = os.path.join(DATA_DIR, f"raw_osm_{city.lower().replace(' ', '-')}_{niche}.csv")
    write_csv(out, rows, RAW_COLS)
    print(f"{len(rows)} {niche} in {city} -> {out}")


if __name__ == "__main__":
    main()
