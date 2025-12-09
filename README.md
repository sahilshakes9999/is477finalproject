# Analyzing Global Spotify Popularity Through Socioeconomic and Cultural Indicators

## Contributors
- Sahil Shaik

---

## Summary

Music streaming platforms like Spotify have transformed how people access and engage with music across the globe. As listening behavior becomes increasingly digitized, streaming metrics offer a unique lens into cultural preferences and global media consumption patterns. At the same time, country-level socioeconomic factors such as income, connectivity, and population size continue to shape how cultural products spread and which genres gain traction across regions.

This project investigates how Spotify track popularity varies across countries in relation to socioeconomic indicators from the World Bank. By integrating two distinct datasets (1) **Spotify Top 50 by Country** from Kaggle and (2) **World Bank Indicators API** (GDP per capita, internet users, and population), the study explores whether countries with different economic conditions exhibit differing patterns in music popularity. This approach aligns with core IS 477 concepts including data acquisition, cleaning, integration, workflow automation, and reproducibility.

I developed an end-to-end reproducible workflow that programmatically acquires World Bank data, cleans and standardizes both datasets, aggregates Spotify track popularity by country, and integrates the information into a unified dataset. The project includes data profiling, quality assessment, exploratory analyses, and visualizations capturing relationships between music popularity and socioeconomic indicators.

Preliminary findings indicate a positive correlation between GDP per capita and average Spotify popularity scores, suggesting that higher-income countries may gravitate toward more globally dominant mainstream music. Similarly, countries with higher internet penetration rates tend to exhibit greater popularity levels, reinforcing the idea that digital infrastructure directly shapes cultural accessibility.

---

## Data Profile

### **Spotify Top 50 by Country (Kaggle)**  
- **Source:** https://www.kaggle.com/datasets/leonardopena/top-50-spotify-songs-by-each-country  
- **Format:** CSV  
- **License:** Public dataset (non-PII)

**Columns include:**  
- `title` → renamed to `track_name`  
- `artist`  
- `top genre` → renamed to `top_genre`  
- `pop` → renamed to `popularity`  
- `bpm`, `dur`, `year`  
- `country`

Each row represents one Top-50 track for a country.

**Transformations applied:**  
- Standardized column names  
- Normalized country names (e.g., `.str.title()`)  
- Converted numeric fields to floats/ints  
- Removed missing or invalid rows  
- Aggregated to country-level metrics:
  - `avg_popularity`
  - `avg_bpm`
  - `track_count`

---

### **World Bank Indicators API**  
- **Source:** https://data.worldbank.org  
- **Format:** JSON → CSV  
- **License:** Open Data License (with attribution)

**Indicators used:**  
- `NY.GDP.PCAP.CD` — GDP per capita  
- `IT.NET.USER.ZS` — Internet users (% of population)  
- `SP.POP.TOTL` — Population  

**Transformations applied:**  
- API retrieval using Python `requests`  
- Merging across indicators  
- Filtering for year 2022  
- Removing aggregate regions (“World”, “OECD”, etc.)  
- Converting to numeric types  

---

## Data Quality Assessment

### **Spotify Dataset**
- **Completeness:** Numeric fields mostly complete  
- **Missingness:** Some missing or vague genre labels  
- **Inconsistency:** Country names varied (fixed with `.str.title()`)  
- **Range checks:** Popularity values 0–100, no extreme outliers  

### **World Bank Dataset**
- Some missing GDP or internet-user values  
- Aggregate geopolitical entries removed  
- Coercion to numeric performed cleanly  

### **Merged Dataset**
- Countries appear only if present in *both* datasets  
- No duplicate country entries  
- All numeric columns validated  

This ensures the final analysis reflects accurate cross-country comparisons.

---

## Findings

### **1. GDP per Capita vs. Spotify Popularity**
A moderate positive trend is observed:

- High-GDP countries (Switzerland, Norway, Denmark) tend to have **higher average track popularity**.  
- Low-GDP countries show wider variance and often lower popularity levels.  

This suggests that global, mainstream music tends to permeate countries with stronger economies and greater purchasing power.

---

### **2. Internet Penetration vs. Spotify Popularity**
A clear upward relationship is present:

- Higher internet-access countries show **significantly higher popularity scores**.  
- This confirms digital accessibility as a crucial component of cultural consumption in the streaming era.

---

### **Interpretation**
Together, these trends suggest:

- **Economic resources + digital infrastructure = more globalized music consumption**  
- Lower-income or lower-connectivity countries may retain more localized or regional music preferences  

These findings align with sociocultural theories of digital globalization.

---

## Future Work

Future extensions of this project may include:

1. **Genre clustering** using PCA or k-means to identify cultural similarity groups among countries.  
2. Integration of **UNESCO cultural indicators** to examine the relationship between arts infrastructure and music consumption.  
3. A **multi-year time series analysis** to study how global hits propagate.  
4. Building an **interactive dashboard** in Plotly or Tableau for real-time exploration.  
5. Applying regression or machine learning models to improve predictive power.

---

## Reproducing This Project

1. Clone the repository
   
git clone https://github.com/sahilshakes9999/is477finalproject 
cd is477finalproject

3. Install dependencies
pip install -r requirements.txt

4. Add the Spotify dataset from Kaggle

Save it as:

data/raw/spotify_raw_top50_bycountry.csv

4. Run the full workflow

Using Snakemake:

snakemake --cores 1

Or using fallback script:

python run_all.py

5. Outputs generated

data/processed/music_culture_merged.csv

figures/gdp_vs_popularity.png

figures/internet_vs_popularity.png

reports/summary_stats.md

6. Box Data Archive

Insert link here:
https://app.box.com/...

Place downloaded files into:

data/final/

References

Kaggle. Spotify Top 50 by Country Dataset. https://www.kaggle.com/datasets/leonardopena/top-50-spotify-songs-by-each-country

World Bank. World Development Indicators API. https://data.worldbank.org

Pandas Documentation — https://pandas.pydata.org

Snakemake Documentation — https://snakemake.readthedocs.io

Matplotlib Documentation — https://matplotlib.org

License

This project is licensed under the MIT License.
See the LICENSE file for details.
# test push
