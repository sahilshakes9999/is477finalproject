# scripts/acquire_spotify.py
import pandas as pd
from pathlib import Path
import hashlib

RAW_DIR = Path("data/raw")
RAW_DIR.mkdir(parents=True, exist_ok=True)

INPUT_FILE = RAW_DIR / "spotify_raw.csv"  # you will place this manually
OUTPUT_FILE = RAW_DIR / "spotify_raw_checked.csv"

def main():
    if not INPUT_FILE.exists():
        raise FileNotFoundError(
            f"{INPUT_FILE} not found. "
            "Download your Spotify/Kaggle CSV and save it as data/raw/spotify_raw.csv."
        )

    df = pd.read_csv(INPUT_FILE)
    # You can do light sanity check (e.g., check some required columns)
    required_cols = ["country", "track_name", "artist", "streams"]
    missing = [c for c in required_cols if c not in df.columns]
    if missing:
        raise ValueError(f"Spotify CSV is missing columns: {missing}")

    df.to_csv(OUTPUT_FILE, index=False)
    sha = hashlib.sha256(OUTPUT_FILE.read_bytes()).hexdigest()
    print(f"Saved {OUTPUT_FILE} with SHA-256: {sha}")

if __name__ == "__main__":
    main()
