# README.md

# Analyzing Global Spotify Popularity Through Socioeconomic and Cultural Indicators

## Summary:

Music streaming platforms such as Spotify have transformed how people access and engage with music across the globe. As listening behavior becomes increasingly digitized, streaming metrics offer a unique lens into cultural preferences and global media consumption patterns. At the same time, country-level socioeconomic factors—such as income, connectivity, and population size—continue to shape how cultural products spread and which genres gain traction across regions.

This project investigates how Spotify track popularity varies across countries in relation to socioeconomic indicators from the World Bank. By integrating two distinct datasets—(1) Spotify Top 50 by Country from Kaggle, and (2) the World Bank Indicators API (GDP per capita, internet users, and population)—the study explores whether countries with different economic conditions exhibit differing patterns in music popularity. This approach aligns with core IS 477 concepts including data acquisition, cleaning, integration, workflow automation, and reproducibility.

The Spotify dataset provides country-level lists of top tracks including metadata such as artists, genres, BPM, and popularity scores. These metrics represent cultural taste signals within each country. The World Bank dataset complements this by providing quantitative socioeconomic context. Together, these sources enable a cross-disciplinary analysis bridging digital culture and macroeconomic conditions.

An end-to-end reproducible workflow was developed that programmatically acquires World Bank data, cleans and standardizes both datasets, aggregates Spotify track popularity by country, and integrates the information into a unified dataset. The project includes data profiling, quality assessment, exploratory analyses, and visualizations capturing relationships between music popularity and socioeconomic indicators.

Preliminary findings indicate a positive correlation between GDP per capita and average Spotify popularity scores, suggesting that higher-income countries may gravitate toward more globally dominant mainstream music. Similarly, countries with higher internet penetration rates tend to exhibit greater popularity levels, reinforcing the idea that digital infrastructure directly shapes cultural accessibility. The results also highlight notable regional contrasts in genre representation, BPM trends, and the concentration of top tracks across countries.

This project demonstrates how openly available datasets can be combined to generate meaningful insights at the intersection of culture and economics. Through structured documentation, metadata, workflow automation, and FAIR principles, the project ensures transparency and reproducibility for future extensions such as genre clustering, cultural distance metrics, or time-series analysis of global listening behavior.

## Data Profile: 

Source : https://www.kaggle.com/datasets/leonardopena/top-50-spotify-songs-by-each-country 
Format : CSV
License : Public dataset hosted on Kaggle

Content:

-Columns include:

* title (renamed to track_name)
* artist
* top genre
* pop (renamed to popularity)
* bpm, dur, year
* country

-Each row represents one track entry from the Top 50 charts of a specific country.

Why this dataset was selected:
It provides a country-by-country snapshot of music consumption, capturing both track-level and cultural metadata. Popularity metrics reflect real user behavior, making the dataset suitable for studying global cultural diffusion.

Transformations applied:

* Column renaming for consistency.
* Standardizing country names and formats.
* Converting numeric fields (bpm, popularity, dur, year) into appropriate types.
* Filtering and aggregating track popularity to country-level means.
* Generating avg_popularity, avg_bpm, and track_count.


## Data Quality Assessment:

Data quality was assessed using profiling scripts (profile_quality.py) and manual inspection.

Spotify Data Quality Findings:

* Completeness: Most numeric fields (BPM, popularity, duration) were fully populated.
* Missingness: Some top_genre entries were empty or overly broad (e.g., “pop”, “latin pop”).
* Inconsistencies: Country names had inconsistent casing; resolved with .str.title().
* Outliers: Popularity values range from 0 to 100; no extreme deviations detected.

World Bank Data Quality Findings: 
* Missing GDP/Internet metrics: A few countries lacked GDP or internet usage data; these were removed.
* Aggregates removed: Entities such as “World” and “OECD members” removed based on non-2-character country codes.
* Numeric coercion: All numeric values converted using to_numeric(errors="coerce").

Merged Dataset Quality:
* Final integrated dataset contained only countries with matching Spotify + World Bank entries for 2022.
* No duplicate entries; join validated.

The cleaning process ensured that analysis results reflect accurate and consistent cross-country comparisons.

Findings:

Two primary relationships were analyzed using scatterplots:

1. GDP per Capita vs. Spotify Popularity

* A moderate positive trend was observed:
* High-GDP countries (e.g., Norway, Switzerland) tended to have higher average Spotify popularity scores.
* Lower-income countries displayed broader variability, possibly due to localized genre preferences or lower streaming adoption rates. This suggests that cultural globalization and mainstream music influence increase with economic development.

2. Internet Users (%) vs. Spotify Popularity

A strong upward relationship emerged:
* Countries with higher internet penetration overwhelmingly exhibited higher Spotify popularity.
* Digital access appears to be a crucial prerequisite for streaming-based cultural consumption. This aligns with prior research linking digital inclusion to global media access.

Interpretation

Taken together, results suggest:
* Economic resources + digital infrastructure → greater access to globally popular music.
* Lower-income countries may maintain more regional music tastes or lack widespread streaming.
These findings support the hypothesis that cultural consumption is shaped by socioeconomic capacity and technological accessibility.

## future work

Several extensions could deepen the cultural and socioeconomic insights identified in this study. First, future research could incorporate genre clustering using unsupervised learning methods such as k-means or hierarchical clustering, enabling countries to be grouped based on their genre distributions. This would provide a richer understanding of how genre preferences relate to broader cultural identity or regional patterns.

Second, the project could be expanded by integrating UNESCO cultural indicators or OECD creative economy metrics, which would allow comparisons between cultural infrastructure (e.g., number of cultural institutions, arts funding) and streaming behaviors. Such expansions would create a more complete model of cultural engagement.

Third, analyzing multiple years of Spotify data would enable a time-series component. This could reveal how global hits spread, how local genres rise or fall over time, and how socioeconomic trends influence cultural convergence or divergence.

More advanced modeling techniques—including regression analysis, principal component analysis (PCA), or neural embeddings—could also improve the explanatory power of the dataset. Finally, results could be deployed through an interactive dashboard using Plotly Dash or Tableau, enabling policymakers, researchers, or marketers to explore global musical trends dynamically.

## reproducing this project 

Reproducing This Project
1. Clone the repository
git clone <your-repo-url>
cd is477finalproject

2. Install dependencies
pip install -r requirements.txt

3. Download Spotify dataset from Kaggle

Save it as:

data/raw/spotify_raw_top50_bycountry.csv

4. Run the full automated workflow

Using Snakemake (recommended):

snakemake --cores 1


Or using the fallback Python script:

python run_all.py

5. Outputs will appear in:

data/processed/music_culture_merged.csv

figures/gdp_vs_popularity.png

figures/internet_vs_popularity.png

reports/summary_stats.md

6. Access final data via Box

(Insert your Box link here.)

Users should download Box files into:

data/final/


# references 
* Kaggle: Spotify Top 50 by Country Dataset, https://www.kaggle.com/datasets/leonardopena/top-50-spotify-songs-by-each-country
* World Bank: _World Development Indicators API_, https://data.worldbank.org/
* pandas documentation: https://pandas.pydata.org/
* snakemake documentation : https://snakemake.readthedocs.io/en/stable/
* matplotlib documentation : https://matplotlib.org/
This project is licensed under the MIT License. See LICENSE for details.

