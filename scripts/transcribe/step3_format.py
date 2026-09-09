"""
Step 3: Turn labeled segments into one clean, readable transcript file per call —
merged into speaker turns, with exact HH:MM:SS timestamps, saved directly in
evidence/Interviews/.
"""
import json
import re
from datetime import datetime, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
AUDIO_DIR = ROOT / "evidence" / "Interviews"
RAW_DIR = AUDIO_DIR / "_raw"
TRANSCRIPTS_DIR = AUDIO_DIR / "Transcripts"
TRANSCRIPTS_DIR.mkdir(parents=True, exist_ok=True)

FNAME_RE = re.compile(r"^Call (.+?)_(\d{6})_(\d{6})$")


def parse_call_meta(stem: str):
    m = FNAME_RE.match(stem)
    if not m:
        return stem, None
    name, ymd, hms = m.groups()
    dt = datetime.strptime("20" + ymd + hms, "%Y%m%d%H%M%S")
    return name.strip(), dt


def hhmmss(seconds: float) -> str:
    td = timedelta(seconds=round(seconds))
    total = int(td.total_seconds())
    h, rem = divmod(total, 3600)
    m, s = divmod(rem, 60)
    return f"{h:02d}:{m:02d}:{s:02d}"


SPEAKER_DISPLAY = {
    "INTERVIEWER": "INTERVIEWER",
    "RESPONDENT": "RESPONDENT",
    "THIRD_SPEAKER": "THIRD SPEAKER",
    "AUDIO_UNCLEAR": "AUDIO UNCLEAR",
}


def format_file(labeled_json: Path, out_md: Path):
    data = json.loads(labeled_json.read_text(encoding="utf-8"))
    segments = data["segments"]
    stem = labeled_json.stem.replace("_labeled", "")
    call_name, call_dt = parse_call_meta(stem)
    duration = data.get("duration", segments[-1]["end"] if segments else 0)

    # Merge consecutive same-speaker segments into turns
    turns = []
    for s in segments:
        text = s["text"].strip()
        if not text:
            continue
        spk = s.get("speaker", "RESPONDENT")
        if turns and turns[-1]["speaker"] == spk and s["start"] - turns[-1]["end"] < 2.0:
            turns[-1]["end"] = s["end"]
            turns[-1]["text"] += " " + text
        else:
            turns.append({"speaker": spk, "start": s["start"], "end": s["end"], "text": text})

    speakers_present = sorted({t["speaker"] for t in turns})

    lines = []
    lines.append(f"# Interview Transcript — Call {call_name}")
    lines.append("")
    lines.append(f"- **Source audio:** `{stem}.m4a`")
    if call_dt:
        lines.append(f"- **Call date/time:** {call_dt.strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append(f"- **Duration:** {hhmmss(duration)}")
    is_translated = "original_language_chunks" in data
    if is_translated:
        lines.append(f"- **Transcription:** OpenAI Whisper (whisper-1) audio translation, verbatim, "
                      f"segment-level timestamps — original call is Telugu / Telugu+English "
                      f"code-switched; text below is the full English translation")
    else:
        lines.append(f"- **Transcription:** OpenAI Whisper (whisper-1), verbatim, segment-level timestamps")
    lines.append(f"- **Speaker detection:** content/role-based (interviewer vs. respondent vs. third "
                  f"speaker), assigned via GPT-4o against the household interview guide — Whisper "
                  f"does not diarize by voice")
    lines.append(f"- **Speakers identified in this call:** {', '.join(SPEAKER_DISPLAY[s] for s in speakers_present)}")
    lines.append("")
    lines.append("---")
    lines.append("")

    for t in turns:
        ts = hhmmss(t["start"])
        lines.append(f"**[{ts}] {SPEAKER_DISPLAY[t['speaker']]}:** {t['text']}")
        lines.append("")

    out_md.write_text("\n".join(lines), encoding="utf-8")
    print(f"[done] {out_md.name} ({len(turns)} turns)")


if __name__ == "__main__":
    labeled_files = sorted(RAW_DIR.glob("*_labeled.json"))
    for lf in labeled_files:
        stem = lf.stem.replace("_labeled", "")
        out_txt = TRANSCRIPTS_DIR / f"{stem} - Transcript.txt"
        format_file(lf, out_txt)
    print("All transcripts formatted.")
