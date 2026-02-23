# Raw Datasets

This directory stores source datasets used across cleaning and exploratory notebooks.

## File Inventory (current structure)

### Core source files

| Dataset | File | Frequency | Notes |
|---------|------|-----------|-------|
| US EPU | `us-epu-daily.csv` | Daily | Economic Policy Uncertainty (US) |
| CSI 300 | `csi300-daily.csv` | Daily | Chinese equity index OHLC/volume |
| S&P 500 | `sp500-daily.csv` | Daily | OHLC/volume, Spanish numeric format |
| Bitcoin | `btc-daily.csv` | Daily | OHLC/volume, Spanish numeric format |
| Gold | `gold-daily.csv` | Daily | OHLC/volume, Spanish numeric format |
| US-China Tension | `us-china-tension.csv` | Monthly | Bilateral tension index |
| CEPU Mainland (original) | `cepu-mainland-papers.xlsx` | Monthly | Original Excel source |
| Migration Fear (original) | `migration-fear.xlsx` | Quarterly | Original Excel source |

### Normalized CSV exports (generated from notebooks)

| Generated from | Output file |
|----------------|-------------|
| `cepu-mainland-papers.xlsx` | `cepu-china-mainland.csv` |
| `migration-fear.xlsx` | `migration-fear.csv` |

## Data Handling Notes

### Spanish number/date formatting
Some market files (`sp500-daily.csv`, `btc-daily.csv`, `gold-daily.csv`) contain:
- comma decimal separators,
- dot thousands separators,
- locale-specific date formatting.

Cleaning logic in exploratory and preparation notebooks standardizes these fields before analysis.

### Volume suffix parsing
Market volumes may use suffixes (`K`, `M`, `B`), converted to numeric values during preprocessing.

## Notebook Mapping

Raw-source exploratory notebooks:
1. `notebooks/exploratory/raw/01_us_epu_daily_exploration.ipynb`
2. `notebooks/exploratory/raw/02_csi300_daily_exploration.ipynb`
3. `notebooks/exploratory/raw/03_sp500_daily_exploration.ipynb`
4. `notebooks/exploratory/raw/04_us_china_tension_exploration.ipynb`
5. `notebooks/exploratory/raw/05_cepu_china_mainland_exploration.ipynb`
6. `notebooks/exploratory/raw/06_migration_fear_exploration.ipynb`
7. `notebooks/exploratory/raw/07_btc_daily_exploration.ipynb`
8. `notebooks/exploratory/raw/08_gold_daily_exploration.ipynb`

## References

- Economic Policy Uncertainty project: https://www.policyuncertainty.com/
- Rogers, Sun, and Sun (2024): US-China Tension index
- Davis, Liu, and Sheng (2019): China EPU from mainland newspapers
- Public market data providers (e.g., Investing.com / Yahoo Finance)

Last updated: 2026-02-23
