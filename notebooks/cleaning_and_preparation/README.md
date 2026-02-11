# Data Cleaning and Preparation

This directory contains notebooks for **Phase 1: Data Cleaning and Preparation** — merging raw datasets and creating feature-rich processed dataframes for analysis and modeling.

## Notebooks

### `01_us_assets_cleaning_and_preparation.ipynb`

**Purpose**: Merge US EPU, S&P 500, Gold, and Bitcoin datasets into a unified daily dataframe.

**Input**:
- `data/raw/us-epu-daily.csv` — US EPU (1985–present)
- `data/raw/sp500-daily.csv` — S&P 500 (2004–present)
- `data/raw/gold-daily.csv` — Gold (2005–present)
- `data/raw/btc-daily.csv` — Bitcoin (2013–present)

**Output**: `data/processed/usepu_assets_daily_features.csv` — 29 columns, ~2,200 daily observations

**Processing Steps**:
1. Load and clean individual datasets (handle Spanish date/number formats)
2. Calculate EPU features: `ΔEPU`, `EPU_MA30`, `EPU_Std30`
3. Calculate asset features: log returns, rolling volatility (7d, 30d, 90d)
4. Inner join on Date → unified daily dataframe
5. Data quality validation

---

### `02_china_assets_cleaning_and_preparation.ipynb`

**Purpose**: Merge China EPU (CNEPU) and CSI 300 index data into a monthly dataset.

**Input**:
- `data/raw/cepu-mainland-papers.xlsx` — China EPU (1949–present, monthly)
- `data/raw/csi300-daily.csv` — CSI 300 (2005–present, daily)

**Output**: `data/processed/cepu_csi300_merged.csv` — 17 columns, ~240 monthly observations

**Processing Steps**:
1. Load CEPU from Excel, parse year/month columns
2. Load CSI 300 daily data, aggregate to monthly (average, last, first, max, min)
3. Calculate monthly returns, volatility, rolling volatility (3m, 6m)
4. Calculate CNEPU features: `ΔCNEPU`, `CNEPU_MA12`, `CNEPU_Std12`
5. Merge on year-month → unified monthly dataframe
6. Data quality validation

**Key difference from US pipeline**: CSI 300 daily data is aggregated to monthly frequency to match the CEPU series, which is only available monthly.

---

## Feature Summary

| Pipeline | Output | Frequency | Features | Observations |
|----------|--------|-----------|----------|--------------|
| US (01) | `usepu_assets_daily_features.csv` | Daily | 29 | ~2,200 |
| China (02) | `cepu_csi300_merged.csv` | Monthly | 17 | ~240 |

## Data Dictionary

See [`data/processed/README.md`](../../data/processed/README.md) for detailed feature descriptions, missing value handling, and usage examples.

## Next Steps

After running these notebooks:
1. **Phase 2**: Exploratory analysis in `notebooks/exploratory/merged/`
2. **Phase 3**: Model training in `notebooks/training/`

---

**Created**: 2026-02-10  
**Updated**: 2026-02-11  
**Status**: Both pipelines complete and tested
