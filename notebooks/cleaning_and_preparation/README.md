# Data Cleaning and Preparation

Phase 1 notebooks that transform raw inputs into the processed datasets used in exploratory analysis and training.

## Notebooks

### `01_us_assets_cleaning_and_preparation.ipynb`

Purpose:
- Build a unified daily dataset joining US EPU, S&P 500, Gold, and Bitcoin.

Inputs:
- `data/raw/us-epu-daily.csv`
- `data/raw/sp500-daily.csv`
- `data/raw/gold-daily.csv`
- `data/raw/btc-daily.csv`

Output:
- `data/processed/usepu_assets_daily_features.csv` (`2227` rows, `29` columns)

Main transformations:
1. locale-aware numeric/date cleaning,
2. EPU features (`ΔEPU`, `EPU_MA30`, `EPU_Std30`),
3. returns and rolling volatilities (`7d`, `30d`, `90d`),
4. date intersection merge across sources.

---

### `02_china_assets_cleaning_and_preparation.ipynb`

Purpose:
- Build a monthly dataset combining CEPU and CSI 300.

Inputs:
- `data/raw/cepu-mainland-papers.xlsx`
- `data/raw/csi300-daily.csv`

Output:
- `data/processed/cepu_csi300_merged.csv` (`247` rows, `17` columns)

Main transformations:
1. CEPU parsing and monthly feature engineering,
2. CSI 300 daily-to-monthly aggregation,
3. monthly return/volatility features (`CSI_Vol`, `CSI_Vol3m`, `CSI_Vol6m`),
4. merged monthly panel aligned on year-month.

## Current outputs

| Pipeline | Output file | Frequency | Rows | Columns |
|----------|-------------|-----------|------|---------|
| US | `usepu_assets_daily_features.csv` | Daily | 2227 | 29 |
| China | `cepu_csi300_merged.csv` | Monthly | 247 | 17 |

Detailed schema: [`data/processed/README.md`](../../data/processed/README.md)

Last updated: 2026-02-23
