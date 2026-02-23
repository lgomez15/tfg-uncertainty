# Exploratory Data Analysis — Raw Sources

This folder contains dataset-level exploratory notebooks used to validate and understand each source before merging.

## Notebook list

1. `01_us_epu_daily_exploration.ipynb` — US EPU daily index
2. `02_csi300_daily_exploration.ipynb` — CSI 300 daily market series
3. `03_sp500_daily_exploration.ipynb` — S&P 500 daily market series
4. `04_us_china_tension_exploration.ipynb` — US-China tension monthly index
5. `05_cepu_china_mainland_exploration.ipynb` — CEPU mainland series
6. `06_migration_fear_exploration.ipynb` — migration fear / migrant EPU panel
7. `07_btc_daily_exploration.ipynb` — Bitcoin daily market series
8. `08_gold_daily_exploration.ipynb` — Gold daily market series

## Common analysis flow

All notebooks follow a similar pattern:
- load + cleaning,
- schema/missingness checks,
- descriptive statistics,
- distribution and outlier views,
- time-series plots,
- summary observations.

## File normalization generated here

Two notebooks create CSV exports from original Excel files in `data/raw/`:

| Notebook | Original | Generated CSV |
|----------|----------|---------------|
| `05_cepu_china_mainland_exploration.ipynb` | `cepu-mainland-papers.xlsx` | `cepu-china-mainland.csv` |
| `06_migration_fear_exploration.ipynb` | `migration-fear.xlsx` | `migration-fear.csv` |

## Notes

- Spanish locale numeric parsing is handled for market files where needed.
- These notebooks are the input validation stage for Phase 1 pipelines in `notebooks/cleaning_and_preparation/`.
- Cross-source findings are documented in `notebooks/exploratory/merged/`.

Last updated: 2026-02-23
