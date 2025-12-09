#!/usr/bin/env python

import pandas as pd
from pathlib import Path
import hashlib

RAW_DIR = Path("data/raw")
RAW_DIR.mkdir(parents=True, exist_ok=True)

# This is the file you downloaded from Kaggle
INPUT_FILE = RAW_DIR / "spotify_raw_top50_bycountry.csv"
OUTPUT_FILE = RAW_DIR / "spotify_raw_checked.csv"


def main():
    if not INPUT_FILE.exists():
        raise FileNotFoundError(
            f"{INPUT_FILE} not found.\n"
            "Download the 'Spotify Top 50 by Country' CSV from Kaggle and "
            "save it as data/raw/spotify_raw_top50_bycountry.csv"
        )

    # Just read and immediately write back to ensure it's a valid CSV
    df = pd.read_csv(INPUT_FILE, encoding="latin1")
    df.to_csv(OUTPUT_FILE, index=False)

    sha = hashlib.sha256(OUTPUT_FILE.read_bytes()).hexdigest()
    print(f"Saved {OUTPUT_FILE} with SHA-256: {sha}")


if __name__ == "__main__":
    main()
