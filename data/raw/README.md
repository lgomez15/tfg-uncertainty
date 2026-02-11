# Raw Datasets

This directory contains the original, immutable datasets used in the TFG Uncertainty Analysis project. All datasets are publicly available and properly cited below.

## Dataset Inventory

| Dataset | File | Format | Observations | Date Range |
|---------|------|--------|--------------|------------|
| US EPU Daily | `us-epu-daily.csv` | CSV | ~15,000 | 1985-present |
| CSI 300 Daily | `csi300-daily.csv` | CSV | ~5,000 | 2005-present |
| S&P 500 Daily | `sp500-daily.csv` | CSV | ~5,000 | 2020-present |
| US-China Tension | `us-china-tension.csv` | CSV | ~376 | 1993-2024 |
| CEPU China Mainland | `cepu-mainland-papers.xlsx` | Excel | ~900 | 1949-present |
| Migration Fear | `migration-fear.xlsx` | Excel | ~140 | 1990-present |
| Bitcoin Daily | `btc-daily.csv` | CSV | ~4,415 | 2013-present |
| Gold Daily | `gold-daily.csv` | CSV | ~4,966 | 2005-present |

---

## 1. US Economic Policy Uncertainty (EPU) Daily

**File**: `us-epu-daily.csv`

**Description**: Daily index measuring economic policy uncertainty in the United States based on newspaper coverage frequency of policy-related economic uncertainty.

**Variables**:
- Date
- EPU Index

**Source**: [Economic Policy Uncertainty](https://www.policyuncertainty.com/)

**Citation**:
> Baker, S. R., Bloom, N., & Davis, S. J. (2016). Measuring Economic Policy Uncertainty. *The Quarterly Journal of Economics*, 131(4), 1593-1636.

**License**: Publicly available for research purposes

---

## 2. CSI 300 Stock Index Daily

**File**: `csi300-daily.csv`

**Description**: Daily price data for the CSI 300 Index, which tracks the performance of the top 300 stocks traded on the Shanghai and Shenzhen stock exchanges.

**Variables**:
- Date
- Open, High, Low, Close (Price)
- Volume
- Change %

**Source**: Financial market data providers (Investing.com, Yahoo Finance)

**Citation**: Market data is publicly available from multiple financial data providers.

**License**: Publicly available market data

---

## 3. S&P 500 Stock Index Daily

**File**: `sp500-daily.csv`

**Description**: Daily price data for the S&P 500 Index, representing the 500 largest publicly traded companies in the United States.

**Variables**:
- Date (Spanish format: DD.MM.YYYY)
- Open, High, Low, Close (Price)
- Volume
- Change %

**Source**: Financial market data providers (Investing.com, Yahoo Finance)

**Citation**: Market data is publicly available from multiple financial data providers.

**License**: Publicly available market data

**Note**: Data is in Spanish number format (comma as decimal separator)

---

## 4. US-China Tension Index

**File**: `us-china-tension.csv`

**Description**: Monthly index measuring bilateral tension between the United States and China based on news coverage and policy events.

**Variables**:
- Date (Monthly)
- UCT (US-China Tension Index)

**Source**: Research paper by Rogers, Sun, and Sun (2024)

**Citation**:
> Rogers, J., Sun, B., & Sun, C. (2024). U.S.-China Tension. *Working Paper*.

**License**: Academic research data

---

## 5. China Economic Policy Uncertainty (CEPU) - Mainland

**File**: `cepu-mainland-papers.xlsx`

**Description**: Monthly China Economic Policy Uncertainty index constructed from mainland Chinese newspapers, covering the period from 1949 to present.

**Variables**:
- Date (Monthly)
- CEPU Index

**Source**: [Economic Policy Uncertainty - China](https://www.policyuncertainty.com/china_monthly.html)

**Citation**:
> Davis, S. J., Liu, D., & Sheng, X. S. (2019). Economic Policy Uncertainty in China Since 1949: The View from Mainland Newspapers. *Working Paper*.

**License**: Publicly available for research purposes

---

## 6. Migration Fear Index

**File**: `migration-fear.xlsx`

**Description**: Quarterly indices measuring migration-related economic policy uncertainty and fear across multiple countries (UK, Germany, USA, France).

**Variables** (per country):
- Date (Quarterly)
- EPU Migrant Index
- Fear Index

**Countries**: United Kingdom, Germany, United States, France

**Source**: Economic Policy Uncertainty project

**Citation**:
> Baker, S. R., Bloom, N., & Davis, S. J. (2016). Measuring Economic Policy Uncertainty. *The Quarterly Journal of Economics*, 131(4), 1593-1636.

**License**: Publicly available for research purposes

---

## 7. Bitcoin Daily Price

**File**: `btc-daily.csv`

**Description**: Daily Bitcoin (BTC/USD) price data including open, high, low, close, and volume.

**Variables**:
- Date (Spanish format: DD.MM.YYYY)
- Open, High, Low, Close (Price in USD)
- Volume
- Change %

**Source**: Cryptocurrency market data providers (Investing.com, CoinMarketCap)

**Citation**: Publicly available cryptocurrency market data

**License**: Publicly available market data

**Note**: Data is in Spanish number format (comma as decimal separator)

---

## 8. Gold Daily Price

**File**: `gold-daily.csv`

**Description**: Daily gold spot price (USD per troy ounce) including open, high, low, close, and volume.

**Variables**:
- Date (Spanish format: DD.MM.YYYY)
- Open, High, Low, Close (Price in USD per ounce)
- Volume
- Change %

**Source**: Commodity market data providers (Investing.com, Kitco)

**Citation**: Publicly available commodity market data

**License**: Publicly available market data

**Note**: Data is in Spanish number format (comma as decimal separator)

---

## Data Processing Notes

### Spanish Number Format
Several datasets (`sp500-daily.csv`, `btc-daily.csv`, `gold-daily.csv`) use Spanish number formatting:
- **Decimal separator**: Comma (`,`)
- **Thousands separator**: Dot (`.`)
- **Example**: `1.234,56` represents one thousand two hundred thirty-four point five six

All exploratory notebooks include automatic cleaning functions to convert these formats to standard numerical values.

### Excel to CSV Conversion
Some datasets are provided in Excel format (`.xlsx`). The corresponding exploratory notebooks automatically convert these to CSV format for easier processing:
- `cepu-mainland-papers.xlsx` → `cepu-china-mainland.csv`
- `migration-fear.xlsx` → `migration-fear.csv`

### Volume Suffixes
Market data files may include volume values with suffixes:
- **K**: Thousands (×1,000)
- **M**: Millions (×1,000,000)
- **B**: Billions (×1,000,000,000)

Example: `86.69K` = 86,690

---

## Usage

These datasets are used in the exploratory notebooks located in `notebooks/exploratory/raw/`. Each dataset has a corresponding notebook with detailed analysis:

1. `01_us_epu_daily_exploration.ipynb`
2. `02_csi300_daily_exploration.ipynb`
3. `03_sp500_daily_exploration.ipynb`
4. `04_us_china_tension_exploration.ipynb`
5. `05_cepu_china_mainland_exploration.ipynb`
6. `06_migration_fear_exploration.ipynb`
7. `07_btc_daily_exploration.ipynb`
8. `08_gold_daily_exploration.ipynb`

See `notebooks/exploratory/raw/README.md` for detailed documentation.

---

## Data Integrity

All datasets in this directory are:
- **Immutable**: Original files are never modified
- **Version controlled**: Tracked in Git for reproducibility
- **Documented**: Each dataset has clear provenance and citations
- **Validated**: Quality checks performed in exploratory notebooks

---

## References

### Primary Sources

1. **Economic Policy Uncertainty Project**  
   Website: https://www.policyuncertainty.com/  
   Maintained by: Scott Baker, Nick Bloom, and Steven J. Davis

2. **Financial Market Data**  
   Sources: Investing.com, Yahoo Finance, Bloomberg  
   License: Publicly available market data

3. **Academic Research Papers**  
   - Rogers, Sun, and Sun (2024) - US-China Tension Index
   - Davis, Liu, and Sheng (2019) - China EPU from Mainland Newspapers

---

**Last Updated**: 2026-02-11  
**Maintained by**: TFG Uncertainty Analysis Project
