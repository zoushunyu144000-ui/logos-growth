"""Print a funnel snapshot: leads by status, tier, country and niche."""
from collections import Counter

from common import MASTER, STATUSES, read_csv


def main():
    rows = read_csv(MASTER)
    print(f"total leads: {len(rows)}")
    st = Counter(r.get("status") or "new" for r in rows)
    print("funnel:", " > ".join(f"{s}:{st[s]}" for s in STATUSES if st[s]))
    print("tier:", dict(Counter(r.get("tier") for r in rows)))
    print("country:", dict(Counter(r.get("country") for r in rows)))
    print("niche:", Counter((r.get("industry") or "").lower() for r in rows).most_common(8))
    contacted = sum(st[s] for s in STATUSES[STATUSES.index("contacted"):] if s not in ("skip",))
    replied = sum(st[s] for s in ("replied", "call_booked", "proposal_sent", "won"))
    if contacted:
        print(f"reply rate: {replied}/{contacted} = {replied / contacted:.0%}; won: {st['won']}")


if __name__ == "__main__":
    main()
