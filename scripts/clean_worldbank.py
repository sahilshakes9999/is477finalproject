# scripts/clean_worldbank.py
import pandas as pd
from pathlib import Path

RAW_DIR = Path("data/raw")
PROC_DIR = Path("data/processed")
PROC_DIR.mkdir(parents=True, exist_ok=True)

def main():
    wb_path = RAW_DIR / "worldbank_raw.csv"
    df = pd.read_csv(wb_path)

    # Keep only one year to match Spotify snapshot
    target_year = 2022
    df = df[df["year"] == target_year].copy()

    # Remove aggregates like "World", "Europe", etc.
    df = df[df["country_code"].str.len() == 2]

    # Drop rows with missing GDP or internet usage
    df = df.dropna(subset=["gdp_per_capita", "internet_users_pct"])

    # Convert columns to numeric
    numeric_cols = ["gdp_per_capita", "internet_users_pct", "population"]
    df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors="coerce")

    # Final cleaning
    df = df.dropna(subset=numeric_cols)

    out_path = PROC_DIR / "worldbank_clean.csv"
    df.to_csv(out_path, index=False)

    print(f"World Bank cleaned data saved to {out_path}, shape = {df.shape}")

if __name__ == "__main__":
    main()
