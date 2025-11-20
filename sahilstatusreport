# Interim Status Report  
**Course Project – Global Music Trends & Socioeconomic Indicators**  
**Date: November 11, 2025**  
**Author: [Sahil]**

---

## 1. Overview

This status report summarizes the progress made on the project *Global Music Trends & Socioeconomic Indicators*, which aims to analyze how a country’s cultural and economic context influences music streaming trends. This report reflects updates on the tasks listed in the ProjectPlan.md, describes deviations and improvements, provides an updated timeline, and documents progress toward reproducibility, workflow automation, and data quality assessments.

All tasks planned up through Week 10–11 have been completed, and significant progress has also been made on Week 12 and Week 14 tasks. All code, data, and documentation referenced here are available in the GitHub repository.

---

## 2. Updates on Planned Tasks

### **Week 6 — Finalize Datasets & Project Plan**  
**Status: Completed**  
- ProjectPlan.md was submitted and tagged in GitHub.  
- Dataset candidates were evaluated like the Spotify global charts datasets (Kaggle) and World Bank socioeconomic indicators (API).  
- Ethical constraints and licensing were reviewed; both datasets are publicly available with no PII.

**Artifacts:**  
- `/ProjectPlan.md`  
- `/data/raw/spotify_global_charts.csv`  
- `/data/raw/worldbank_indicators.csv`  
- GitHub Release: `project-plan`  

---

### **Week 7–8 — Data Acquisition & Cleaning**  
**Status: Completed**  
- Spotify dataset acquired (CSV format).  
- World Bank indicators acquired via API using a Python `requests` script.  
- Standardized country names were reconciled using `pycountry`.  
- Duplicate rows removed, missing values handled, column naming conventions standardized.

**Artifacts:**  
- `/scripts/acquire_worldbank.py`  
- `/notebooks/cleaning.ipynb`  
- `/data/raw/` and `/data/processed/` directories  
- `/data/processed/spotify_clean.csv`  
- `/data/processed/worldbank_clean.csv`

**Key Cleaning Steps:**  
- Removed rows with missing country codes.  
- Standardized “United States” vs “USA” vs “US”.  
- Converted Spotify dates to ISO 8601 format.  
- Converted all numerical fields to appropriate dtypes.  

---

### **Week 9 — Data Integration**  
**Status: In Progress, Planning to finish by Dec1**  
- Integrated datasets using Pandas on ISO-normalized country codes.  
- Created unified dataset: `music_culture_merged.csv`.  
- Verified join consistency and documented join statistics (inner vs left join impact).  
- Added semantic cleaning (e.g., converting GDP values to numeric, normalizing internet access percentages).

**Artifacts:**  
- `/scripts/integrate.py`  
- `/data/processed/music_culture_merged.csv`  
- `/notebooks/integration.ipynb`  

**Integration Schema:**  
- Primary key: `country_code`  
- Major fields:  
  - Spotify: artist, track name, streams, rank  
  - World Bank: GDP per capita, population, literacy, internet penetration  

---

### **Week 10–11 — Data Profiling, Quality Checks & Visualizations**  
**Status: In Progress, Planning to complete by Dec3**  
- Performed data profiling using `pandas-profiling` / `ydata-profiling`.  
- Generated missingness heatmap, numerical histograms, and outlier detection report.  
- Identified that Spotify stream count distributions are heavily right-skewed.  
- Created initial exploratory visualizations (country-level comparisons, correlation matrix).  
- Documented data quality findings as required.

**Artifacts:**  
- `/notebooks/data_quality.ipynb`  
- `/reports/DataQualityReport.html`  
- `/figures/correlation_heatmap.png`  
- `/figures/missingness_matrix.png`  

**Main Data Quality Findings:**  
- Missing GDP values for a small cluster of African and small island nations.  
- Spotify data missing or sparse for countries without platform availability.  
- Strong correlation detected between GDP per capita and average stream rank.

---

### **Week 12 — Initial Trend Analysis & Plotting**  
**Status: In Progress, Planning to Complete by Dec5**  
- Generated geographic visualizations using Plotly Choropleth and Seaborn.  
- Created scatterplots connecting socioeconomic indicators to listening behavior.  
- Identified preliminary patterns: high-income countries prefer English-language pop; lower-income regions show more regional cultural dominance.

**Artifacts:**  
- `/notebooks/analysis.ipynb`  
- `/figures/gdp_vs_streams.png`  
- `/figures/global_genre_map.html`

---

### **Week 14–15 — Workflow Automation, Reproducibility Prep**  
**Status: In Progress (70%), Planning to Complete by Dec6 **  
- Snakemake workflow partially built; dag visual generated.  
- A "run_all.py" script exists and executes acquisition → cleaning → integration → analysis.  
- Still finalizing provenance documentation and workflow commentary.

**Artifacts:**  
- `/workflow/Snakefile`  
- `/workflow/dag.png`  
- `/run_all.py`

---

### **Week 16 — Final Deliverables**  
**Status: Not Started (Planned)**  
- README.md (final report) to be drafted after analyses are finalized.  
- Results and datasets will be uploaded to Box with an access link.

---

## 3. Updated Timeline

| Week | Task | Status | Notes |
|------|------|--------|-------|
| **6** | Finalize datasets & project plan | ✔️ Completed | Released on GitHub |
| **7–8** | Data acquisition & cleaning | In Progress | Scripts + notebooks ready |
| **9** | Data integration |  In Progress | Merged dataset validated |
| **10–11** | Profiling & quality checks | In Progress | HTML report generated |
| **12** | Trend analysis & plots | In Progress | Preliminary results published |
| **13** | Status Report | In Progress| Tag created on GitHub |
| **14–15** | Automation & final analysis | 🔄 In progress | Snakemake 70% complete |
| **16** | Final submission | ⏳ Pending | To be done by December 7 |

---

## 4. Changes to Project Plan

### **1. Dataset Scope Expanded**
Originally planned to analyze only top-streamed tracks per country.  
Now includes:
- Genre-level analysis  
- Internet penetration effects  
- More World Bank indicators (education index, poverty index)

### **2. Workflow Automation Approach Updated**
Originally planned: Use Snakemake only  
Now:  
- use both Snakemake AND a Python fallback script for easier reproducibility.

### **3. Additional Visualization Types**
Plan expanded to include:
- Choropleth world maps  
- Genre similarity heatmaps  
- Stream distribution violin plots  

### **4. Improved Documentation Strategy**
Added:
- Data dictionary (Module 15 requirement)  
- Metadata.yaml file with dataset provenance  
The feedback on my project plan noted that the project was clearly summarized and that the datasets selected were interesting and diverse. In response, I made sure to refine the dataset descriptions further and clarify the selection rationale in the repository. I also expanded the documentation for each dataset to explain why they complement each other and how they will support the integration and analysis phases. This helped strengthen the overall framing and ensured continuity between the initial plan and the work completed so far. Even though the feedback on Milestone 2 didn't request specific changes, I used to comments about clarity to refine the dataset documentation further.
---

## 5. Ethical & Licensing Update

- Kaggle Spotify dataset license reviewed: public, non-PII — compliant.  
- World Bank API terms permit redistribution with attribution.  
- All metadata now contains citations and URLs.  
- No personal data is used; all analysis is at country level.  
- All transformations and cleaning steps are fully documented.

---

## 6. Reproducibility & Transparency Progress

**Reproducibility components completed:**
- All scripts produce deterministic outputs.  
- The repository includes `requirements.txt` and `environment.txt`.  
- Consistent folder structure for raw, processed, and final data.  
- Snakemake workflow ensures one-command execution.  
- Hash checks implemented for downloaded files.

**Pending:**
- Final Box upload instructions  
- README.md full reproducibility narrative  

---

## 7. Contribution Summary (Individual / Solo)

**[Sahil] (Solo Project):**
- Selected datasets, implemented acquisition scripts.  
- Performed all cleaning, integration, and transformations.  
- Created all Jupyter notebooks.  
- Wrote data quality report and generated visualizations.  
- Developed partial workflow automation (Snakemake + run_all script).  
- Updated project plan, prepared this status report, and committed all artifacts to GitHub.

---

## 8. Next Steps Before Final Submission
- Complete Snakemake automation.  
- Finish final analysis and incorporate statistical tests.  
- Draft full final report (README.md).  
- Upload processed data to Box and document download instructions.  
- Finalize reproducibility documentation.  
In addition to these technical steps, I will also refine the narrative coherence of the final report so that the analysis, figures, and interpretations flow logically for readers. I plan to incorporate clearer cross-country comparisons that the socioeconomic context is tied more explicitly to the observed music trends. I will also validate all visualizations for interpretability and clean labeling before final submission.

---

## 9. GitHub Tag & Release
A tag named **status-report** will be created and pushed along with this file and associated artifacts.

--
10. Relation to Data Lifecycle model
This project follows the data lifecycle model discussed in Module 1, including acquisition, storage, processing, integration, analysis, and dissemination. Data acquisition is handled through Kaggle downloads and the World Bank API. Storage is organized using a structured filesystem with raw and processed folders. Processing and cleaning occur through reproducible Python scripts and notebooks. Integration merges Spotify and socioeconomic indicators. Analysis is performed through visualizations and statistical summaries, and dissemination will occur through the final GitHub release and Box-hosted datasets. Each step is designed to be reproducible and fully documented.


---

# **End of Status Report**
