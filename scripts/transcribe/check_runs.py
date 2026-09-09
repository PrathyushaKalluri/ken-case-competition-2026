import json
from pathlib import Path

RAW_DIR = Path("evidence/Interviews/_raw")

for f in sorted(RAW_DIR.glob("*_labeled.json")):
    d = json.load(open(f, encoding="utf-8"))
    segs = d["segments"]
    runs = []
    cur_spk, cur_start_i, cur_start_t = None, 0, 0
    for i, s in enumerate(segs):
        spk = s.get("speaker")
        if spk != cur_spk:
            if cur_spk is not None:
                runs.append((cur_spk, cur_start_i, i - 1, cur_start_t, segs[i-1]["end"]))
            cur_spk, cur_start_i, cur_start_t = spk, i, s["start"]
    runs.append((cur_spk, cur_start_i, len(segs) - 1, cur_start_t, segs[-1]["end"]))

    long_runs = [r for r in runs if (r[2] - r[1] + 1) >= 10]
    print(f"\n=== {f.name} === total_runs={len(runs)} long_runs(>=10 segs)={len(long_runs)}")
    for spk, i0, i1, t0, t1 in long_runs:
        n = i1 - i0 + 1
        preview = " ".join(s["text"].strip() for s in segs[i0:i0+3])[:150]
        print(f"  {spk} segs[{i0}:{i1}] n={n} t={t0:.0f}-{t1:.0f}s ({t1-t0:.0f}s)  '{preview}...'")
