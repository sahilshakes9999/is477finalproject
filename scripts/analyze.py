# scripts/analyze.py
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

PROC_DIR = Path("data/processed")
FIG_DIR = Path("figures")
FIG_DIR.mkdir(parents=True, exist_ok=True)

def main():
    df = pd.read_csv(PROC_DIR / "music_culture_merged.csv")

    # Example 1: GDP per capita vs average streams
    plt.figure()
    plt.scatter(df["gdp_per_capita"], df["avg_streams"])
    plt.xlabel("GDP per capita (USD)")
    plt.ylabel("Average Spotify streams per track (country-level)")
    plt.title("GDP vs Average Spotify Streams")
    plt.tight_layout()
    plt.savefig(FIG_DIR / "gdp_vs_streams.png")

    # Example 2: Internet users vs total streams
    plt.figure()
    plt.scatter(df["internet_users_pct"], df["total_streams"])
    plt.xlabel("Internet users (% of population)")
    plt.ylabel("Total Spotify streams (country-level)")
    plt.title("Internet Access vs Total Streams")
    plt.tight_layout()
    plt.savefig(FIG_DIR / "internet_vs_streams.png")

    print("Figures saved to figures/")

if __name__ == "__main__":
    main()

