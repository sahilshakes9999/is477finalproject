# scripts/acquire_worldbank.py
import requests
import pandas as pd
from pathlib import Path
import hashlib

RAW_DIR = Path("data/raw")
RAW_DIR.mkdir(parents=True, exist_ok=True)

# World Bank indicators
INDICATORS = {
    "NY.GDP.PCAP.CD": "gdp_per_capita",
    "IT.NET.USER.ZS": "internet_users_pct",
    "SP.POP.TOTL": "population",
}

# Choose a recent year or small range
START_YEAR = 2018
END_YEAR = 2023

def fetch_indicator(indicator_code: str) -> pd.DataFrame:
    url = (
        f"https://api.worldbank.org/v2/country/all/indicator/"
        f"{indicator_code}?format=json&per_page=20000&date={START_YEAR}:{END_YEAR}"
    )
    r = requests.get(url)
    r.raise_for_status()
    data = r.json()[1]  # first element is metadata, second is data

    rows = []
    for entry in data:
        country = entry["country"]["value"]
        code = entry["country"]["id"]
        year = entry["date"]
        value = entry["value"]
        rows.append({
            "country_name": country,
            "country_code": code,
            "year": int(year),
            indicator_code: value,
        })
    return pd.DataFrame(rows)

def main():
    frames = []
    for ind in INDICATORS.keys():
        df = fetch_indicator(ind)
        frames.append(df)

    # Merge on country_code + year
    from functools import reduce
    df_merged = reduce(
        lambda left, right: pd.merge(
            left, right, on=["country_name", "country_code", "year"], how="outer"
        ),
        frames
    )

    # Rename indicator columns to nicer names
    df_merged = df_merged.rename(columns=INDICATORS)

    out_path = RAW_DIR / "worldbank_raw.csv"
    df_merged.to_csv(out_path, index=False)

    # Compute SHA-256 hash
    sha = hashlib.sha256(out_path.read_bytes()).hexdigest()
    print(f"Saved {out_path} with SHA-256: {sha}")

if __name__ == "__main__":
    main()

