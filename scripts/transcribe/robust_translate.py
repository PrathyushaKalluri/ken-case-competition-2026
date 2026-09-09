"""
Robust Telugu/English -> English translation-transcription for one call.

For the Telugu and Telugu+English code-switched calls, "transcribe" means:
translate every word into English, with zero information loss, timestamps,
and no repetition/hallucination -- while keeping the original-language
verbatim text too, so nothing is lost in translation and it can be audited.

Same chunked, auto-detect-and-retry approach validated on the 3 English calls
(see robust_transcribe.py), applied twice per chunk:
  1. client.audio.translations.create  -> English text (any source language in,
     English out, in one Whisper pass -- this IS the primary transcript).
  2. client.audio.transcriptions.create (no language forced, so it can follow
     genuine code-switching) -> original-language verbatim text, kept as a
     secondary/audit trail, not shown turn-by-turn (segment boundaries between
     the translate and transcribe passes are not guaranteed to line up 1:1),
     but preserved per 30s chunk so every word that was said is still there
     somewhere in the deliverable.

Both passes go through the same hallucination guard as the English pipeline:
reject + retry at a higher temperature if a chunk's reported timestamps run
past its real duration, or if a short phrase dominates its own text.
"""
import gzip
import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from env_loader import load_env
load_env()
import os
from openai import OpenAI

ROOT = Path(__file__).resolve().parents[2]
AUDIO_DIR = ROOT / "evidence" / "Interviews"
RAW_DIR = AUDIO_DIR / "_raw"

CHUNK_SECONDS = 30
TEMPERATURES = [0.0, 0.5, 0.8]
DURATION_SLACK = 2.0
COMPRESSION_RATIO_THRESHOLD = 2.4  # bytes / gzip(bytes) -- same technique and
    # threshold faster-whisper uses to flag degenerate/repetitive output.
    # Language-agnostic (works on raw bytes, not word-splitting), which matters
    # here: an English word-ngram check produced false positives on legitimate
    # Telugu (different whitespace/morphology), and a fixed-length character
    # n-gram check went too far the other way and missed a real Telugu
    # word-repetition loop. Compression ratio catches both without assuming
    # anything about the script.

# A "domain hint" prompt was tried here to bias vocabulary toward appliance-repair
# terms, but on ambiguous/quiet audio Whisper sometimes echoed the prompt text
# itself back as if it were transcribed speech (a known Whisper prompt-bleed
# quirk) -- e.g. a segment literally read "Telugu with English code-switching
# interview in India, Telugu with English code", lifted straight from the hint.
# That's a hallucination risk of its own, so no prompt is passed at all now.
DOMAIN_PROMPT = None

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])


def compression_ratio(text: str) -> float:
    text = text.strip()
    raw = text.encode("utf-8")
    if len(raw) < 50:
        return 1.0
    compressed = gzip.compress(raw)
    return len(raw) / len(compressed)


def is_bad(data: dict, chunk_duration: float):
    segs = data.get("segments", [])
    if not segs:
        return False, ""
    max_end = max(s["end"] for s in segs)
    if max_end > chunk_duration + DURATION_SLACK:
        return True, f"timestamps run to {max_end:.1f}s past {chunk_duration:.1f}s chunk"

    full_text = " ".join(s["text"] for s in segs)
    ratio = compression_ratio(full_text)
    if ratio >= COMPRESSION_RATIO_THRESHOLD:
        return True, f"compression ratio {ratio:.2f} (repetitive/degenerate text)"

    # A loop confined to ONE segment inside an otherwise-normal chunk gets
    # diluted below threshold when checked only in aggregate (this is exactly
    # how a real "AMC, AMC, AMC, ..." loop slipped through once) -- also check
    # each segment's own text.
    for s in segs:
        seg_ratio = compression_ratio(s["text"])
        if seg_ratio >= COMPRESSION_RATIO_THRESHOLD:
            return True, f"segment [{s['start']:.1f}-{s['end']:.1f}] compression ratio {seg_ratio:.2f}"

    return False, ""


def call_robust(fn, chunk_path: Path, chunk_duration: float, label: str, **kwargs):
    # Escalating temperature only on an actual detected failure (duration overrun
    # or repetition dominance) -- NOT on "this result looks short", which was
    # tried and rejected: temperature>0 sampling is noticeably non-deterministic
    # call to call, so forcing retries on short-but-plausibly-real content just
    # adds random variance (sometimes losing real content that temp=0 got right)
    # without a reliable win, and burns extra calls for no gain.
    best, best_ratio = None, float("inf")
    for temp in TEMPERATURES:
        with open(chunk_path, "rb") as f:
            resp = fn(file=f, model="whisper-1", response_format="verbose_json", temperature=temp, **kwargs)
        data = resp.model_dump()
        bad, reason = is_bad(data, chunk_duration)
        if not bad:
            if temp != TEMPERATURES[0]:
                print(f"    [{label}] clean at temperature={temp}")
            return data
        print(f"    [{label}] temperature={temp} REJECTED: {reason} -- retrying")
        segs = data.get("segments", [])
        ratio = compression_ratio(" ".join(s["text"] for s in segs)) if segs else float("inf")
        if ratio < best_ratio:
            best_ratio, best = ratio, data
    print(f"    [{label}] WARNING: no attempt fully clean, keeping least-bad (ratio={best_ratio:.2f})")
    return best


def translate_file(fname: str):
    src = AUDIO_DIR / fname
    out = RAW_DIR / (Path(fname).stem + ".json")
    chunk_dir = RAW_DIR / "_chunks30" / Path(fname).stem
    chunk_dir.mkdir(parents=True, exist_ok=True)

    probe = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", str(src)],
        check=True, capture_output=True, text=True,
    )
    total_duration = float(probe.stdout.strip())
    n_chunks = int(total_duration // CHUNK_SECONDS) + 1

    all_translated_segments = []
    original_chunks = []

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
        print(f"  [chunk {label}] translating ...")
        tdata = call_robust(client.audio.translations.create, chunk_path, dur, label + " EN")
        for seg in tdata.get("segments", []):
            seg["start"] += start
            seg["end"] += start
            all_translated_segments.append(seg)

        print(f"  [chunk {label}] original-language transcript ...")
        odata = call_robust(client.audio.transcriptions.create, chunk_path, dur, label + " orig",
                             timestamp_granularities=["segment"])
        orig_text = " ".join(s["text"].strip() for s in odata.get("segments", []))
        original_chunks.append({
            "start": start, "end": start + dur,
            "language": odata.get("language"),
            "text": orig_text,
        })

    combined = {
        "language": "english (translated)",
        "duration": all_translated_segments[-1]["end"] if all_translated_segments else total_duration,
        "segments": all_translated_segments,
        "original_language_chunks": original_chunks,
    }
    out.write_text(json.dumps(combined, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[done] {fname} -> {len(all_translated_segments)} English segments, "
          f"{len(original_chunks)} original-language chunks")


if __name__ == "__main__":
    fname = sys.argv[1]
    translate_file(fname)
