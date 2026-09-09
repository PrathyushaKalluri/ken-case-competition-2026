"""
Step 2: Assign speaker labels (INTERVIEWER / RESPONDENT / THIRD_SPEAKER) to each
timestamped Whisper segment, using GPT-4o with the interview guide as context.

Whisper does not do speaker diarization by voice. Per the task spec, speakers are
identified from conversational structure instead: who is asking the scripted
guide questions vs. who is narrating personal experience vs. any third voice.

Two things this went through before landing here:
  1. A single whole-file pass (given gpt-4o's context window is easily big enough)
     asking for one compact "IRTRIR..." character string. This degenerated into a
     repeating IRTIRTIRT... pattern -- a different flavor of the same kind of
     runaway-repetition failure Whisper hit on long audio, this time in GPT-4o's
     text decoding. Abandoned.
  2. Chunked JSON-list labeling directly on raw Whisper segments. This mostly
     worked but occasionally lost the thread mid-chunk: Whisper often splits one
     spoken sentence into 2-4 tiny fragments, and a sparse one-fragment
     interviewer question buried inside a long respondent answer would get
     mislabeled as more of the respondent's speech.

The fix that actually holds: merge raw segments into full sentences/utterances
first (a short pause + terminal punctuation = utterance boundary), THEN run
chunked JSON-list labeling on those cleaner, more legible units, THEN map each
label back down to every raw segment inside that utterance. Judging a whole
sentence instead of a 2-word fragment is what removes the ambiguity.
"""
import json
import os
import re
import sys
import time
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from env_loader import load_env  # noqa: E402

load_env()

from openai import OpenAI  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
AUDIO_DIR = ROOT / "evidence" / "Interviews"
RAW_DIR = AUDIO_DIR / "_raw"
LABELED_DIR = AUDIO_DIR / "_raw"
GUIDE_PATH = Path(__file__).parent / "core_guide.txt"

MODEL = "gpt-4o"
CHUNK_SIZE = 16
CONTEXT_OVERLAP = 8
MAX_RETRIES = 3
SUSPICIOUS_SAME_SPEAKER_FRAC = 0.9
MAX_GAP_TO_MERGE = 0.4   # seconds of silence still considered "same breath" -- kept tight
                          # because a turn change in natural conversation can happen with
                          # well under 1s of gap, and Whisper doesn't reliably punctuate
                          # sentence ends, so a looser threshold fuses two different
                          # speakers' text into one (wrongly single-labeled) utterance

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
GUIDE_TEXT = GUIDE_PATH.read_text(encoding="utf-8")

TERMINAL_PUNCT = re.compile(r"[.?!]\s*$")


def merge_into_utterances(segments):
    """Group raw Whisper segments into full-sentence utterances. Returns a list
    of {start, end, text, raw_idxs: [...]} -- raw_idxs lets us paint the final
    label back onto every original segment."""
    utterances = []
    cur = None
    for idx, s in enumerate(segments):
        text = s["text"].strip()
        if cur is None:
            cur = {"start": s["start"], "end": s["end"], "text": text, "raw_idxs": [idx]}
            continue
        gap = s["start"] - cur["end"]
        prev_ended = bool(TERMINAL_PUNCT.search(cur["text"]))
        if gap <= MAX_GAP_TO_MERGE and not prev_ended:
            cur["end"] = s["end"]
            cur["text"] = (cur["text"] + " " + text).strip()
            cur["raw_idxs"].append(idx)
        else:
            utterances.append(cur)
            cur = {"start": s["start"], "end": s["end"], "text": text, "raw_idxs": [idx]}
    if cur is not None:
        utterances.append(cur)
    return utterances


SYSTEM_PROMPT = f"""You are labeling speaker turns in a transcribed phone interview conducted by
students researching how Indian households/technicians handle appliance breakdowns and repairs
("Keeping the Machines Running" project). The interview loosely follows the guide below, though
real calls may skip, reorder, or add ad-hoc questions.

Each call has exactly THREE possible speaker roles, used consistently across the whole call:
- INTERVIEWER: asks the scripted/guide-style questions, probes, says "and then what happened",
  explains the study, asks for consent, thanks the respondent, etc.
- RESPONDENT: the main person being interviewed — answers with concrete personal stories, names,
  dates, amounts, specific experiences.
- THIRD_SPEAKER: any other distinct voice that appears — e.g. another household member who joins
  briefly, a person being discussed who then speaks, a call-waiting/interruption, a translator.
  Only use this when a clearly different voice/person is speaking, not just a topic shift.

If a call in fact only has two speakers throughout, it is fine to never use THIRD_SPEAKER — do not
force a third label onto turns that are really the interviewer or respondent.

IMPORTANT — this is a live back-and-forth interview, not a monologue: expect the speaker to change
frequently. A run of many consecutive utterances (say, more than 6-8 in a row) all labeled the same
is unusual and usually means you have lost track — before submitting, re-check any such long run: an
utterance that opens with something like "so...", "okay so like...", "did you...", "was there...",
"how did...", "can you...", "is there anything..." is almost always the INTERVIEWER asking the next
thing. Do not default an ambiguous utterance to RESPONDENT just because the previous one was.

REFERENCE GUIDE (for recognizing the interviewer's scripted questions):
{GUIDE_TEXT}

You will be given a numbered list of full-sentence utterances (some already-labeled ones for
context, then new ones to label). Return STRICT JSON: {{"labels": [{{"i": <utterance index int>,
"speaker": "INTERVIEWER"|"RESPONDENT"|"THIRD_SPEAKER"}}, ...]}} covering exactly the NEW utterance
indices asked for, in order. Do not include the context utterances in your output."""


def build_user_prompt(context_utts, new_utts):
    lines = []
    if context_utts:
        lines.append("CONTEXT (already labeled, for continuity only — do not relabel these):")
        for u in context_utts:
            lines.append(f'  [{u["i"]}] ({u["speaker"]}) {u["text"]}')
        lines.append("")
    lines.append("NEW UTTERANCES TO LABEL:")
    for u in new_utts:
        lines.append(f'  [{u["i"]}] {u["text"]}')
    return "\n".join(lines)


def label_file(json_path: Path, out_path: Path):
    if out_path.exists():
        print(f"[skip] {json_path.name} -> already labeled")
        return

    data = json.loads(json_path.read_text(encoding="utf-8"))
    segments = data["segments"]
    utterances = merge_into_utterances(segments)
    for idx, u in enumerate(utterances):
        u["i"] = idx

    labeled = {}
    i = 0
    while i < len(utterances):
        new_utts = utterances[i:i + CHUNK_SIZE]
        ctx_start = max(0, i - CONTEXT_OVERLAP)
        context_utts = [
            {"i": utterances[j]["i"], "speaker": labeled[j], "text": utterances[j]["text"]}
            for j in range(ctx_start, i) if j in labeled
        ]
        wanted_idxs = {u["i"] for u in new_utts}
        force_note = False

        for attempt in range(1, MAX_RETRIES + 1):
            user_prompt = build_user_prompt(context_utts, [{"i": u["i"], "text": u["text"]} for u in new_utts])
            if force_note:
                user_prompt += (
                    "\n\nNOTE: a previous attempt at labeling these exact utterances collapsed "
                    "almost all of them into one speaker. Look again, utterance by utterance."
                )
            resp = client.chat.completions.create(
                model=MODEL,
                temperature=0.0,
                response_format={"type": "json_object"},
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": user_prompt},
                ],
            )
            try:
                parsed = json.loads(resp.choices[0].message.content)
                got = {int(item["i"]): item["speaker"] for item in parsed["labels"]}
                missing = wanted_idxs - set(got.keys())
                bad_vals = {v for v in got.values() if v not in ("INTERVIEWER", "RESPONDENT", "THIRD_SPEAKER")}
                if missing or bad_vals:
                    raise ValueError(f"missing={missing} bad_vals={bad_vals}")

                if len(new_utts) >= 8:
                    counts = Counter(got.values())
                    top_frac = counts.most_common(1)[0][1] / len(got)
                    if top_frac >= SUSPICIOUS_SAME_SPEAKER_FRAC and attempt < MAX_RETRIES:
                        print(f"  [suspicious] utt chunk at {i}: {top_frac:.0%} one speaker -- re-asking")
                        force_note = True
                        continue

                labeled.update(got)
                break
            except Exception as e:
                print(f"  [retry {attempt}] chunk starting at {i}: {e}")
                if attempt == MAX_RETRIES:
                    for u in new_utts:
                        labeled.setdefault(u["i"], "RESPONDENT")
                    print(f"  [fallback] defaulted unresolved utterances in chunk starting at {i} to RESPONDENT")

        print(f"  labeled utterances {i}..{i+len(new_utts)-1} / {len(utterances)}")
        i += CHUNK_SIZE

    # paint utterance labels back down onto every raw segment inside it
    for u in utterances:
        spk = labeled.get(u["i"], "RESPONDENT")
        for raw_idx in u["raw_idxs"]:
            segments[raw_idx]["speaker"] = spk

    data["segments"] = segments
    out_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[done] {json_path.name} -> {out_path.name} ({len(utterances)} utterances, {len(segments)} raw segments)")


if __name__ == "__main__":
    raw_files = sorted(RAW_DIR.glob("*.json"))
    raw_files = [p for p in raw_files if not p.stem.endswith("_labeled")]
    for p in raw_files:
        out = LABELED_DIR / (p.stem + "_labeled.json")
        t0 = time.time()
        label_file(p, out)
        print(f"  ({time.time()-t0:.1f}s)")
    print("All speaker labeling complete.")
