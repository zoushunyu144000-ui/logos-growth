"""Merge raw lead CSVs (from research/discovery) into leads/master.csv, deduplicated."""
import glob
import os
import sys

from common import DATA_DIR, MASTER, domain_of, norm_key, read_csv, today, write_csv


COUNTRY = {"UK": "United Kingdom", "GB": "United Kingdom", "US": "United States", "USA": "United States",
           "AU": "Australia", "SG": "Singapore"}


def ingest(paths):
    master = read_csv(MASTER)
    seen = {norm_key(r): r for r in master}
    next_id = 1 + max([int(r["lead_id"][1:]) for r in master if r.get("lead_id")] or [0])
    added = 0
    for p in paths:
        for row in read_csv(p):
            if not (row.get("business_name") or "").strip():
                continue
            k = norm_key(row)
            if k in seen:
                old = seen[k]
                # keep extra evidence/signals from later sources
                for col in ("signals", "evidence", "source_url"):
                    new = (row.get(col) or "").strip()
                    if new and new not in (old.get(col) or ""):
                        sep = ";" if col == "signals" else " | "
                        old[col] = sep.join(x for x in [old.get(col, ""), new] if x)
                continue
            row = {k2: (v or "").strip() for k2, v in row.items()}
            row["country"] = COUNTRY.get(row.get("country", "").upper(), row.get("country", ""))
            row["lead_id"] = f"L{next_id:04d}"
            next_id += 1
            row["domain"] = domain_of(row.get("website", ""))
            row["found_at"] = row.get("found_at") or today()
            row["status"] = "new"
            master.append(row)
            seen[k] = row
            added += 1
    write_csv(MASTER, master)
    print(f"ingested {added} new leads; master now {len(master)} rows -> {MASTER}")


if __name__ == "__main__":
    files = sys.argv[1:] or sorted(glob.glob(os.path.join(DATA_DIR, "raw_*.csv")))
    ingest(files)
