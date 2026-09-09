"""Scan raw transcripts for Whisper repetition-loop artifacts: a stretch of
consecutive segments dominated by one short phrase repeated over and over.
Checks a rolling window of concatenated segment text (the loop can spread
across many short 1-2s segments, so a per-segment check alone misses it)."""
import json
from collections import Counter
from pathlib import Path

RAW_DIR = Path("evidence/Interviews/_raw")
WINDOW = 10       # segments per window
NGRAM = 4
DOMINANCE = 0.35  # fraction of window's words covered by the top repeated ngram


def dominant_ngram_frac(text: str, ngram=NGRAM):
    words = text.split()
    if len(words) < ngram + 2:
        return 0.0
    ngrams = [" ".join(words[i:i+ngram]) for i in range(len(words) - ngram + 1)]
    c = Counter(ngrams)
    top_count = c.most_common(1)[0][1]
    return (top_count * ngram) / len(words)


for f in sorted(RAW_DIR.glob("*.json")):
    if f.stem.endswith("_labeled"):
        continue
    d = json.load(open(f, encoding="utf-8"))
    segs = d["segments"]
    flagged_ranges = []
    i = 0
    while i < len(segs):
        window = segs[i:i+WINDOW]
        combined = " ".join(s["text"] for s in window)
        frac = dominant_ngram_frac(combined)
        if frac >= DOMINANCE:
            flagged_ranges.append((i, i + len(window) - 1, window[0]["start"], window[-1]["end"], frac))
        i += WINDOW

    print(f"\n=== {f.name} === segments={len(segs)} flagged_windows={len(flagged_ranges)}")
    for a, b, start, end, frac in flagged_ranges:
        print(f"  segs[{a}:{b}]  {start:.1f}-{end:.1f}s  dominance={frac:.2f}")
