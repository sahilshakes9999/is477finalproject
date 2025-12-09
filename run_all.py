#!/usr/bin/env python3

"""
run_all.py

Fallback workflow runner for the IS477 final project.
Runs the entire data pipeline in order without Snakemake.
"""

import subprocess
from pathlib import Path


def run_step(description, command):
    print(f"\n=== {description} ===")
    print(f"Running: {command}\n")
    result = subprocess.run(command, shell=True)
    if result.returncode != 0:
        raise RuntimeError(f"Step failed: {description}")
    print(f"✔ Completed: {description}\n")


def main():

    # Ensure folders exist
    Path("data/raw").mkdir(parents=True, exist_ok=True)
    Path("data/processed").mkdir(parents=True, exist_ok=True)
    Path("figures").mkdir(parents=True, exist_ok=True)
    Path("reports").mkdir(parents=True, exist_ok=True)

    # Run steps
    run_step("Acquire World Bank data",  "python scripts/acquire_worldbank.py")
    run_step("Acquire Spotify data",     "python scripts/acquire_spotify.py")
    run_step("Clean World Bank data",    "python scripts/clean_worldbank.py")
    run_step("Clean Spotify data",       "python scripts/clean_spotify.py")
    run_step("Integrate datasets",       "python scripts/integrate.py")
    run_step("Profile dataset quality",  "python scripts/profile_quality.py")
    run_step("Generate analysis figures", "python scripts/analyze.py")

    print("\n🎉 All steps completed successfully!")
    print("Processed data saved in data/processed/")
    print("Figures saved in figures/")
    print("Quality reports saved in reports/\n")


if __name__ == "__main__":
    main()

