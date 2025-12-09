# scripts/integrate.py
import pandas as pd
from pathlib import Path

PROC_DIR = Path("data/processed")
PROC_DIR.mkdir(parents=True, exist_ok=True)

def main():
    wb = pd.read_csv(PROC_DIR / "worldbank_clean.csv")
    sp = pd.read_csv(PROC_DIR / "spotify_clean.csv")

    # Simple integration on country_name (you can refine with manual mapping if needed)
    merged = pd.merge(
        sp,
        wb,
        how="inner",
        left_on="country_name",
        right_on="country_name",
    )

    out_path = PROC_DIR / "music_culture_merged.csv"
    merged.to_csv(out_path, index=False)
    print(f"Merged dataset saved to {out_path}, shape: {merged.shape}")

if __name__ == "__main__":
    main()

