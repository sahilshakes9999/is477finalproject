# scripts/profile_quality.py
import pandas as pd
from pathlib import Path

PROC_DIR = Path("data/processed")
REPORTS_DIR = Path("reports")
FIG_DIR = Path("figures")

REPORTS_DIR.mkdir(parents=True, exist_ok=True)
FIG_DIR.mkdir(parents=True, exist_ok=True)

def main():
    df = pd.read_csv(PROC_DIR / "music_culture_merged.csv")

    # Simple stats
    desc = df.describe(include="all")
    desc.to_markdown(REPORTS_DIR / "summary_stats.md")

    # Missingness summary
    missing = df.isna().sum().to_frame("missing_count")
    missing["missing_pct"] = missing["missing_count"] / len(df) * 100
    missing.to_markdown(REPORTS_DIR / "missingness.md")

    # Quick correlation matrix for numeric cols
    numeric = df.select_dtypes(include=["number"])
    corr = numeric.corr()
    corr.to_markdown(REPORTS_DIR / "correlations.md")

    print("Data quality reports written to reports/")

if __name__ == "__main__":
    main()
