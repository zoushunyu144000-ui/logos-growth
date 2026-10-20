"""One command for the whole pipeline: ingest -> audit -> score -> draft -> report.

python run.py            # full run (audit needs open internet)
python run.py --no-audit # offline: ingest, score, draft from search evidence only
"""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
steps = ["ingest", "audit", "score", "draft", "report"]
if "--no-audit" in sys.argv:
    steps.remove("audit")
for s in steps:
    print(f"== {s}")
    subprocess.run([sys.executable, os.path.join(HERE, "leadgen", f"{s}.py")],
                   cwd=os.path.join(HERE, "leadgen"), check=True)
