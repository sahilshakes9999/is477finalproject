# scripts/analyze.py
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

PROC_DIR = Path("data/processed")
FIG_DIR = Path("figures")
FIG_DIR.mkdir(parents=True, exist_ok=True)


def main():
    df = pd.read_csv(PROC_DIR / "music_culture_merged.csv")

    # GDP vs avg popularity
    plt.figure()
    plt.scatter(df["gdp_per_capita"], df["avg_popularity"])
    plt.xlabel("GDP per capita (USD)")
    plt.ylabel("Average track popularity (Spotify)")
    plt.title("GDP vs Average Spotify Track Popularity")
    plt.tight_layout()
    plt.savefig(FIG_DIR / "gdp_vs_popularity.png")

    # Internet users vs avg popularity
    plt.figure()
    plt.scatter(df["internet_users_pct"], df["avg_popularity"])
    plt.xlabel("Internet users (% of population)")
    plt.ylabel("Average track popularity (Spotify)")
    plt.title("Internet Access vs Spotify Popularity")
    plt.tight_layout()
    plt.savefig(FIG_DIR / "internet_vs_popularity.png")

    print("Figures saved to figures/")


if __name__ == "__main__":
    main()
