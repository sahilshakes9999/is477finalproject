# ProjectPlan.md
## Project Title
**Global Music Trends and Cultural Indicators: Exploring the Relationship Between Streaming Popularity and Socioeconomic Data**

---

## Overview
Music has become one of the most globally accessible cultural exports in the digital era. Platforms like Spotify and Apple Music have made it possible to quantify listening behavior across countries. 
However, the popularity of certain genres or artists many times reflect deeper cultural and socioeconomic patterns such as economic status, population demographics, or internet accessibility.

This project aims to explore how global music streaming trends correspond to global/country-level cultural and socioeconomic indicators. 
By combining publicly available datasets on global music charts with data from international organizations like the World Bank, the goal is to identify patterns in how cultural and economic contexts shape listening behavior. 
The analysis will of course involve data integration, cleaning, quality assessment, and visualization to reveal cross-country differences and insights into the global diffusion of music culture.

---

## Research Questions
1. How do country-level socioeconomic indicators (e.g., GDP per capita, population, internet usage) correlate with global music streaming trends?
2. Are certain genres or artists more popular in regions with specific cultural or economic characteristics?
3. Can we identify clusters of countries with similar listening patterns based on cultural indicators?
4. What insights can these patterns offer about cultural globalization and digital access?

---

## Team
**Solo project:**  
- **Student:** Sahil Shaik
- **Role:** Responsible for all components of data acquisition, cleaning, analysis, visualization, documentation, and GitHub management.

---

## Datasets that I will use

### 1. **Global Music Chart Dataset**
- **Source:** Kaggle — *“Spotify Top 50 by Country”* or *“Spotify Tracks Dataset”*
- **Format:** CSV
- **Content:** Includes country-level rankings of songs and artists, with variables such as song name, artist, streams, and genre.
- **Justification:** Captures real-world streaming preferences across countries, suitable for analyzing global music popularity trends.

### 2. **World Bank Cultural and Economic Indicators**
- **Source:** World Bank Open Data Portal ([https://data.worldbank.org](https://data.worldbank.org))
- **Format:** CSV download
- **Content:** Country-level indicators such as GDP per capita, population, internet usage, education index, and cultural expenditure.
- **Justification:** Provides measurable socioeconomic context to interpret global music consumption behavior.

### 3. *(Optional, Enrichment Source)*  
**UNESCO or OECD Cultural Statistics** (e.g., number of cultural institutions, creative economy index)  
- Used to provide deeper insights if time allows.

---

## Data Integration Strategy con't
- Use **country name** as the key for joining datasets.
- Normalize country names to ensure matching between sources.
- Conduct data quality assessment (missing values, outliers, standardization).
- Integrate in Python using **Pandas** with join/merge operations.
- Produce integrated dataset stored as a CSV file (`music_culture_merged.csv`).

---

## Storage and Organization strategy
- Data stored in `data/raw` and `data/processed` directories within the GitHub repository.
- Schema documented in a `data_dictionary.md` file.
- File naming conventions will follow a format like:

data/raw/music_charts.csv
data/raw/worldbank_indicators.csv
data/processed/music_culture_merged.csv


---

## Timeline

Week, Task, and Deliverable
|------|------|--------------|


| **Week 6 (Oct 16)** | Finalize datasets and project plan | ProjectPlan.md |


| **Week 7–8** | Acquire and clean datasets | Raw CSVs and cleaning notebook |


| **Week 9** | Integrate datasets using Pandas | Merged dataset |


| **Week 10–11** | Data profiling, quality checks, visualizations | Data quality report |


| **Week 12** | Analyze trends, produce plots and summaries | Jupyter notebook & figures |


| **Week 13 (Nov 11)** | Submit interim status report | StatusReport.md |


| **Week 14–15** | Final analysis, workflow automation, finalize report | README.md, scripts, Box data |


| **Week 16 (Dec 10)** | Final project release on GitHub | Final submission |

---

## Constraints
- **Data availability:** Music chart datasets may not cover every country or have consistent date ranges.
- **Standardization:** Country name variations (i.e: “United States” vs “USA”) could require a need cleaning.
- **Ethical and Legal:** Datasets from Kaggle and World Bank will be verified for public use and proper citation. No personally identifiable information (PII) will be collected.
- **Time constraint:** As a solo project, workload in conjunction with time management and progressive milestones will be crucial for me.

---

## Gaps and Future Needs
- Final dataset selection: Need to confirm which specific Spotify dataset provides the best global/country-level granularity, needs to be to the proper level.
- Visualization tools: Will experiment with Python libraries like Seaborn or Plotly for geographic and trend plots.
- Automation: Will evaluate whether to use Snakemake or a Python script for workflow automation.
- Data quality metrics: Will develop a reproducible quality assessment framework once the integrated dataset is complete.

---

## References
- Spotify Global Charts Dataset (Kaggle)  
- World Bank Open Data Portal  
- UNESCO Institute for Statistics (optional)  
- Python Libraries: Pandas, Matplotlib, Seaborn, Plotly

---

## Expected Outcome
By the end of this project, I expect to produce:
- A reproducible workflow that integrates global music and socioeconomic data
- A cleaned and merged dataset that links global/country-level music preferences with cultural indicators
- Analytical visualizations as well as summary statistics that shows how cultural and economic variables correlate with listening behavior
- Documentation along the way that supports transparency, reproducibility, and ethical use of all data sources without saying

