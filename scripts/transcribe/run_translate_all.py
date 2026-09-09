import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from robust_translate import translate_file

FILES = [
    "Call Amma_260908_230414.m4a",
    "Call Sarala Aunty_260909_135058.m4a",
    "Call Sarala Aunty_260909_140910.m4a",
    "Technician.m4a",
]

if __name__ == "__main__":
    for fn in FILES:
        print(f"\n===== {fn} =====")
        translate_file(fn)
    print("\nAll 4 Telugu/code-switched files translated.")
