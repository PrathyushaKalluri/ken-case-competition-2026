"""Scan for near-duplicate consecutive segments (same sentence transcribed 2-3x
with overlapping/identical timestamps) -- a milder Whisper artifact distinct
from the full repetition-loop, often appearing right at internal chunk
boundaries (~240s, 480s, 720s, ...)."""
import json
import re
from difflib import SequenceMatcher
from pathlib import Path

RAW_DIR = Path("evidence/Interviews/_raw")


def norm(t: str) -> str:
    return re.sub(r"[^a-z0-9 ]", "", t.lower()).strip()


def similar(a: str, b: str) -> float:
    return SequenceMatcher(None, a, b).ratio()


for f in sorted(RAW_DIR.glob("*.json")):
    if f.stem.endswith("_labeled"):
        continue
    d = json.load(open(f, encoding="utf-8"))
    segs = d["segments"]
    dupes = []
    for i in range(1, len(segs)):
        a, b = norm(segs[i-1]["text"]), norm(segs[i]["text"])
        if not a or not b:
            continue
        overlap = segs[i]["start"] < segs[i-1]["end"] - 0.5
        sim = similar(a, b)
        if sim > 0.6 or (overlap and sim > 0.3):
            dupes.append((i-1, i, segs[i-1]["start"], segs[i]["start"], sim, overlap))
    print(f"\n=== {f.name} === segments={len(segs)} near_dupe_pairs={len(dupes)}")
    for i0, i1, s0, s1, sim, overlap in dupes:
        print(f"  segs[{i0},{i1}]  t={s0:.1f}/{s1:.1f}  sim={sim:.2f}  overlap={overlap}")
