#!/usr/bin/env python

import pandas as pd
from pathlib import Path

RAW_DIR = Path("data/raw")
PROC_DIR = Path("data/processed")


def main():
    in_path = RAW_DIR / "spotify_raw_checked.csv"
    out_dir = PROC_DIR
    out_dir.mkdir(parents=True, exist_ok=True)

    # latin-1 handles artist/title special chars
    df = pd.read_csv(in_path, encoding="latin1")

    # Rename to nicer / consistent names
    df = df.rename(
        columns={
            "title": "track_name",
            "top genre": "top_genre",
            "pop": "popularity",
        }
    )

    # Keep only the columns we care about
    keep_cols = [
        "country",
        "track_name",
        "artist",
        "top_genre",
        "year",
        "bpm",
        "dur",
        "popularity",
    ]
    missing = [c for c in keep_cols if c not in df.columns]
    if missing:
        raise ValueError(
            f"Spotify CSV is missing expected columns: {missing}\n"
            f"Available columns: {list(df.columns)}"
        )

    clean = df[keep_cols].copy()

    # Basic cleaning
    clean["country"] = clean["country"].astype(str).str.strip()
    # Capitalize country names so 'japan' -> 'Japan'
    clean["country_name"] = clean["country"].str.title()

    numeric_cols = ["year", "bpm", "dur", "popularity"]
    for col in numeric_cols:
        clean[col] = pd.to_numeric(clean[col], errors="coerce")

    # Drop rows with no country
    clean = clean.dropna(subset=["country"])

    out_path = out_dir / "spotify_clean.csv"
    clean.to_csv(out_path, index=False)
    print(f"Saved cleaned Spotify data to {out_path}, shape = {clean.shape}")


if __name__ == "__main__":
    main()
