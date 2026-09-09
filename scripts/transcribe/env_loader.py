"""Tiny .env loader (no external dependency) so the API key never has to be
passed on the command line or hardcoded in a script."""
from pathlib import Path


def load_env(path: str | None = None) -> None:
    import os

    env_path = Path(path) if path else Path(__file__).resolve().parents[2] / ".env"
    if not env_path.exists():
        return
    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        os.environ.setdefault(key.strip(), value.strip())
