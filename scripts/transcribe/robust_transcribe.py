"""
Robust Whisper transcription for one call: splits into small uniform chunks,
transcribes each, and automatically detects + retries any chunk that Whisper
hallucinated into a repetition loop -- instead of manually chasing artifacts
chunk by chunk.

Detection signals (either trips a retry):
  1. Whisper reports segment timestamps that run past the chunk's real audio
     duration (a hallucinating model keeps "inventing" speech past the end of
     real audio -- a very reliable tell).
  2. A short n-gram dominates a large fraction of the chunk's own text (the
     "repeating the same phrase over and over" signature).

On detection, retries the SAME chunk at a higher temperature (breaks the
deterministic decode lock), up to MAX_RETRIES times, keeping the best
(least-repetitive) attempt if none come back fully clean.
"""
import json
import os
import subprocess
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from env_loader import load_env
load_env()
from openai import OpenAI

ROOT = Path(__file__).resolve().parents[2]
AUDIO_DIR = ROOT / "evidence" / "Interviews"
RAW_DIR = AUDIO_DIR / "_raw"

CHUNK_SECONDS = 30
TEMPERATURES = [0.0, 0.5, 0.8]
NGRAM = 4
DOMINANCE_THRESHOLD = 0.30
DURATION_SLACK = 2.0  # seconds a chunk's reported timestamps may exceed real duration before flagging

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])


def dominant_ngram_frac(text: str) -> float:
    words = text.split()
    if len(words) < NGRAM + 2:
        return 0.0
    ngrams = [" ".join(words[i:i+NGRAM]) for i in range(len(words) - NGRAM + 1)]
    top_count = Counter(ngrams).most_common(1)[0][1]
    return (top_count * NGRAM) / len(words)


def is_bad(data: dict, chunk_duration: float) -> tuple[bool, str]:
    segs = data.get("segments", [])
    if not segs:
        return False, ""
    max_end = max(s["end"] for s in segs)
    if max_end > chunk_duration + DURATION_SLACK:
        return True, f"timestamps run to {max_end:.1f}s past {chunk_duration:.1f}s chunk"
    full_text = " ".join(s["text"] for s in segs)
    frac = dominant_ngram_frac(full_text)
    if frac >= DOMINANCE_THRESHOLD:
        return True, f"ngram dominance {frac:.2f}"
    return False, ""


def transcribe_chunk_robust(chunk_path: Path, chunk_duration: float, label: str):
    best = None
    best_frac = 1.0
    for temp in TEMPERATURES:
        with open(chunk_path, "rb") as f:
            resp = client.audio.transcriptions.create(
                model="whisper-1", file=f, language="en",
                response_format="verbose_json", timestamp_granularities=["segment"],
                temperature=temp,
            )
        data = resp.model_dump()
        bad, reason = is_bad(data, chunk_duration)
        if not bad:
            if temp != TEMPERATURES[0]:
                print(f"    [{label}] clean at temperature={temp}")
            return data
        print(f"    [{label}] temperature={temp} REJECTED: {reason} -- retrying")
        segs = data.get("segments", [])
        frac = dominant_ngram_frac(" ".join(s["text"] for s in segs)) if segs else 1.0
        if frac < best_frac:
            best_frac, best = frac, data
    print(f"    [{label}] WARNING: no attempt came back fully clean, keeping least-bad (frac={best_frac:.2f})")
    return best


def transcribe_file(fname: str):
    src = AUDIO_DIR / fname
    out = RAW_DIR / (Path(fname).stem + ".json")
    chunk_dir = RAW_DIR / "_chunks30" / Path(fname).stem
    chunk_dir.mkdir(parents=True, exist_ok=True)

    import subprocess as sp
    probe = sp.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", str(src)],
        check=True, capture_output=True, text=True,
    )
    total_duration = float(probe.stdout.strip())
    n_chunks = int(total_duration // CHUNK_SECONDS) + 1

    all_segments = []
    for i in range(n_chunks):
        start = i * CHUNK_SECONDS
        dur = min(CHUNK_SECONDS, total_duration - start)
        if dur <= 0:
            break
        chunk_path = chunk_dir / f"c_{i:03d}.mp3"
        if not chunk_path.exists():
            subprocess.run(
                ["ffmpeg", "-y", "-ss", str(start), "-t", str(dur), "-i", str(src),
                 "-vn", "-ac", "1", "-ar", "16000", "-b:a", "64k", str(chunk_path)],
                check=True, capture_output=True,
            )
        label = f"{i+1}/{n_chunks} @ {start:.0f}s"
        print(f"  [chunk {label}] {chunk_path.name}")
        data = transcribe_chunk_robust(chunk_path, dur, label)
        for seg in data.get("segments", []):
            seg["start"] += start
            seg["end"] += start
            all_segments.append(seg)

    combined = {
        "language": "english",
        "duration": all_segments[-1]["end"] if all_segments else total_duration,
        "segments": all_segments,
    }
    out.write_text(json.dumps(combined, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[done] {fname} -> {len(all_segments)} segments")


if __name__ == "__main__":
    fname = sys.argv[1]
    transcribe_file(fname)
