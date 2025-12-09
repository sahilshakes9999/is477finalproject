# data dictionary md

## spotify_clean.csv
| Column         | Type    | Description |
|----------------|---------|-------------|
| country        | string  | Raw country name from Spotify dataset |
| country_name   | string  | Standardized country name used for merges |
| track_name     | string  | Title of song |
| artist         | string  | Artist name |
| top_genre      | string  | Genre classification |
| year           | int     | Year track was released |
| bpm            | float   | Beats per minute |
| dur            | float   | Track duration (ms) |
| popularity     | float   | Spotify popularity score |

## worldbank_clean.csv
| Column              | Type   | Description |
|---------------------|--------|-------------|
| country_name        | string | Standardized country identifier |
| country_code        | string | ISO two-letter country code |
| year                | int    | Year of indicator value |
| gdp_per_capita      | float  | GDP per capita (USD) |
| internet_users_pct  | float  | Internet users (% of population) |
| population          | int    | Total population |

## music_culture_merged.csv
| Column            | Type   | Description |
|-------------------|--------|-------------|
| country_name      | string | Merge key |
| avg_popularity    | float  | Mean track popularity for that country |
| avg_bpm           | float  | Mean BPM for top 50 tracks |
| track_count       | int    | Number of unique tracks for that country |
| gdp_per_capita    | float  | GDP per capita |
| internet_users_pct| float  | Internet penetration |
| population        | int    | Population |
