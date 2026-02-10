# Data Cleaning and Preparation

This directory contains notebooks for **Phase 1: Data Cleaning and Preparation** - merging raw datasets and creating feature-rich processed dataframes for analysis and modeling.

## Notebooks

### `01_us_assets_cleaning_and_preparation.ipynb`

**Purpose**: Merge US EPU, S&P 500, Gold, and Bitcoin datasets into a unified daily dataframe with calculated returns and volatility features.

**Input Datasets**:
- `data/raw/us-epu-daily.csv` - US Economic Policy Uncertainty (1985-present)
- `data/raw/sp500-daily.csv` - S&P 500 Stock Index (2004-present)
- `data/raw/gold-daily.csv` - Gold Prices (2005-present)
- `data/raw/btc-daily.csv` - Bitcoin Prices (2013-present)

**Output**:
- `data/processed/merged_daily_features.csv` - Unified daily dataset with all features

**Processing Steps**:

1. **Load and Clean Individual Datasets**
   - Parse dates (handle Spanish format: DD.MM.YYYY)
   - Clean numeric columns (Spanish format: comma as decimal, dot as thousands)
   - Select relevant columns (Date, OHLC prices)

2. **Calculate EPU Features**
   - `ΔEPU`: Daily change in EPU
   - `EPU_MA30`: 30-day moving average
   - `EPU_Std30`: 30-day rolling standard deviation

3. **Calculate Asset Features**
   - **Log returns**: `log(Close_t / Close_{t-1})`
   - **Rolling volatility**: 7-day, 30-day, 90-day windows (std of returns)

4. **Merge Datasets**
   - Inner join on Date (only dates with all 4 datasets)
   - Sort by date
   - Final date range determined by overlap

5. **Data Quality Checks**
   - Missing value analysis
   - Outlier detection
   - Date continuity verification
   - Negative volatility check

**Features Created**:

| Category | Features | Count |
|----------|----------|-------|
| EPU | `EPU`, `ΔEPU`, `EPU_MA30`, `EPU_Std30` | 4 |
| S&P 500 | `SP500_Close`, `SP500_Open`, `SP500_High`, `SP500_Low`, `SP500_Return`, `SP500_Vol7d`, `SP500_Vol30d`, `SP500_Vol90d` | 8 |
| Gold | `Gold_Close`, `Gold_Open`, `Gold_High`, `Gold_Low`, `Gold_Return`, `Gold_Vol7d`, `Gold_Vol30d`, `Gold_Vol90d` | 8 |
| Bitcoin | `BTC_Close`, `BTC_Open`, `BTC_High`, `BTC_Low`, `BTC_Return`, `BTC_Vol7d`, `BTC_Vol30d`, `BTC_Vol90d` | 8 |
| **Total** | | **29** |

**Missing Values**:
- First 1 row: Returns (lag 1)
- First 7 rows: 7-day volatility
- First 30 rows: 30-day volatility and EPU features
- First 90 rows: 90-day volatility

**Visualizations**:
- EPU and asset volatilities over time
- Correlation heatmap for key features

## Data Dictionary

See [`data/processed/README.md`](../../data/processed/README.md) for detailed feature descriptions, missing value handling, and usage examples.

## Next Steps

After running this notebook:
1. **Phase 2**: Exploratory analysis in `notebooks/exploratory/merged/us_uncertainty_markets/`
2. **Phase 3**: Model training in `notebooks/training/`

---

**Created**: 2026-02-10  
**Status**: Complete and tested
