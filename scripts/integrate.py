#!/usr/bin/env python

import pandas as pd
from pathlib import Path

PROC_DIR = Path("data/processed")
PROC_DIR.mkdir(parents=True, exist_ok=True)


def main():
    sp = pd.read_csv(PROC_DIR / "spotify_clean.csv")
    wb = pd.read_csv(PROC_DIR / "worldbank_clean.csv")

    # Ensure consistent string formatting
    sp["country_name"] = sp["country_name"].astype(str).str.strip()
    wb["country_name"] = wb["country_name"].astype(str).str.strip()

    # Aggregate Spotify to country-level statistics
    agg = sp.groupby("country_name").agg(
        avg_popularity=("popularity", "mean"),
        avg_bpm=("bpm", "mean"),
        track_count=("track_name", "nunique"),
    ).reset_index()

    merged = pd.merge(agg, wb, on="country_name", how="inner")

    out_path = PROC_DIR / "music_culture_merged.csv"
    merged.to_csv(out_path, index=False)
    print(f"Merged dataset saved to {out_path}, shape = {merged.shape}")


if __name__ == "__main__":
    main()
