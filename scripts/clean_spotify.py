#!/usr/bin/env python

import pandas as pd
from pathlib import Path


def main():
    raw_path = Path("data/raw/spotify_global_charts.csv")
    out_dir = Path("data/processed")
    out_dir.mkdir(parents=True, exist_ok=True)

    # latin-1 handles special characters in artist/title names
    df = pd.read_csv(raw_path, encoding="latin1")

    # rename to nicer column names
    df = df.rename(
        columns={
            "title": "track_name",
            "top genre": "top_genre",
            "pop": "popularity",
        }
    )

    # keep only the columns we care about
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
    clean = df[keep_cols].copy()

    # basic cleaning
    clean["country"] = clean["country"].astype(str).str.strip()
    numeric_cols = ["year", "bpm", "dur", "popularity"]
    for col in numeric_cols:
        clean[col] = pd.to_numeric(clean[col], errors="coerce")

    # drop rows with no country
    clean = clean.dropna(subset=["country"])

    out_path = out_dir / "spotify_clean.csv"
    clean.to_csv(out_path, index=False)
    print(f"Saved cleaned Spotify data to {out_path}")


if __name__ == "__main__":
    main()

