# Exploratory Data Analysis - Notebooks

This directory contains exploratory data analysis (EDA) notebooks for all datasets in the `datasets/raw` directory.

## Overview

All notebooks follow a consistent structure:
1. **Data Loading and Cleaning** - Load data and perform necessary preprocessing
2. **Data Overview** - Basic information about the dataset
3. **Missing Values Analysis** - Check for and analyze missing data
4. **Descriptive Statistics** - Statistical summary of the data
5. **Visualizations** - Time series plots, distributions, and patterns
6. **Key Findings** - Summary of insights and important observations

## Notebooks

### 01. US EPU Daily (`01_us_epu_daily_exploration.ipynb`)
- **Dataset**: `us-epu-daily.csv`
- **Description**: Daily US Economic Policy Uncertainty Index from 1985 to present
- **Key Features**:
  - Time series analysis with moving averages
  - Distribution analysis and outlier detection
  - Yearly and monthly patterns
  - ~15,000 daily observations

### 02. CSI 300 Daily (`02_csi300_daily_exploration.ipynb`)
- **Dataset**: `csi300-daily.csv`
- **Description**: Daily CSI 300 stock index data
- **Key Features**:
  - OHLC (Open, High, Low, Close) analysis
  - Daily returns and volatility analysis
  - Volume analysis
  - Moving averages (50-day, 200-day)
  - ~5,000 trading days

### 03. S&P 500 Daily (`03_sp500_daily_exploration.ipynb`)
- **Dataset**: `sp500-daily.csv`
- **Description**: Daily S&P 500 stock index data (Spanish format)
- **Key Features**:
  - Data cleaning for Spanish number format (comma as decimal separator)
  - Price time series with moving averages
  - Returns and volatility analysis
  - ~5,000 trading days

### 04. US-China Tension (`04_us_china_tension_exploration.ipynb`)
- **Dataset**: `us-china-tension.csv`
- **Description**: Monthly US-China Tension Index (1993-2024)
- **Key Features**:
  - Monthly tension index analysis
  - Key events identification (highest/lowest tension periods)
  - Yearly patterns and trends
  - Month-over-month change analysis
  - ~376 monthly observations
- **Citation**: Rogers, Sun, and Sun (2024), U.S.-China Tension, Working paper

### 05. CEPU China Mainland (`05_cepu_china_mainland_exploration.ipynb`)
- **Dataset**: `cepu-china-mainland-paper.xlsx` → **Converts to CSV**
- **Description**: Monthly China Economic Policy Uncertainty from mainland newspapers (1949-present)
- **Key Features**:
  - **Excel to CSV conversion** (saves to `datasets/raw/cepu-china-mainland-paper.csv`)
  - Historical EPU analysis from 1949
  - Decadal analysis
  - Key historical events identification
  - ~900 monthly observations
- **Source**: Economic Policy Uncertainty in China Since 1949: The View from Mainland Newspapers, by Steven J. Davis, Dingqian Liu and Xuguang S. Sheng, 2019

### 06. CNEPU Daily (`06_cnepu_daily_exploration.ipynb`)
- **Dataset**: `cnepu-daily.xlsx` → **Converts to CSV**
- **Description**: Daily China News-based Economic Policy Uncertainty (2000-present)
- **Key Features**:
  - **Excel to CSV conversion** (saves to `datasets/raw/cnepu-daily.csv`)
  - Daily EPU analysis
  - Moving averages (30-day, 365-day)
  - Yearly patterns
  - Key events identification
  - ~9,000 daily observations

### 07. Migration Fear Index (`07_migration_fear_exploration.ipynb`)
- **Dataset**: `migration-fear.xlsx` → **Converts to CSV**
- **Description**: Quarterly migration-related EPU and fear indices for UK, Germany, USA, and France (1990-present)
- **Key Features**:
  - **Excel to CSV conversion** (saves to `datasets/raw/migration-fear.csv`)
  - Multi-country comparative analysis
  - EPU Migrant Index tracking
  - Fear Index tracking
  - Correlation analysis between EPU and Fear
  - Country-by-country analysis
  - ~140 quarterly observations per country

## Excel to CSV Conversions

Three notebooks include automatic conversion from Excel to CSV format:

| Notebook | Excel File | Output CSV File |
|----------|-----------|-----------------|
| 05 | `cepu-china-mainland-paper.xlsx` | `cepu-china-mainland-paper.csv` |
| 06 | `cnepu-daily.xlsx` | `cnepu-daily.csv` |
| 07 | `migration-fear.xlsx` | `migration-fear.csv` |

**Note**: The CSV files are automatically saved to the `datasets/raw` directory when you run the respective notebooks.

## Running the Notebooks

### Prerequisites
```bash
pip install pandas numpy matplotlib seaborn openpyxl
```

### Execution Order
You can run the notebooks in any order. However, if you want to generate CSV files from Excel datasets, run notebooks 05, 06, and 07 first.

### Jupyter Lab/Notebook
```bash
# Navigate to the notebooks directory
cd notebooks/exploratory

# Start Jupyter
jupyter lab
# or
jupyter notebook
```

## Dataset Summary

| Dataset | Format | Frequency | Date Range | Observations | Variables |
|---------|--------|-----------|------------|--------------|-----------|
| US EPU Daily | CSV | Daily | 1985-present | ~15,000 | 1 index |
| CSI 300 Daily | CSV | Daily | 2005-present | ~5,000 | OHLC + Volume |
| S&P 500 Daily | CSV | Daily | 2020-present | ~5,000 | OHLC + Volume |
| US-China Tension | CSV | Monthly | 1993-2024 | ~376 | 1 index |
| CEPU China Mainland | XLSX→CSV | Monthly | 1949-present | ~900 | 1 index |
| CNEPU Daily | XLSX→CSV | Daily | 2000-present | ~9,000 | 1 index |
| Migration Fear | XLSX→CSV | Quarterly | 1990-present | ~140 | 8 indices (4 countries × 2 types) |

## Key Insights

### Uncertainty Indices
- **US EPU**: Captures daily economic policy uncertainty in the United States
- **China EPU (Mainland)**: Historical perspective from 1949, covering major Chinese political and economic events
- **CNEPU**: Daily granularity for modern China (2000+)
- **US-China Tension**: Specific focus on bilateral relationship uncertainty

### Market Indices
- **CSI 300**: Chinese stock market performance
- **S&P 500**: US stock market performance
- Both indices can be correlated with uncertainty measures

### Migration Indices
- **Multi-country comparison**: UK, Germany, USA, France
- **Dual metrics**: EPU Migrant Index and Fear Index
- **Policy relevance**: Migration-related economic policy uncertainty

## Common Analysis Patterns

All notebooks include:
- ✅ Time series visualization
- ✅ Distribution analysis (histograms, box plots)
- ✅ Descriptive statistics
- ✅ Missing values check
- ✅ Trend analysis (moving averages where applicable)
- ✅ Key events/outliers identification
- ✅ Summary of findings

## Next Steps

After exploring the datasets, you can:
1. **Correlation Analysis**: Examine relationships between different uncertainty indices and market performance
2. **Event Studies**: Analyze specific historical events and their impact on uncertainty
3. **Forecasting**: Build predictive models for uncertainty indices
4. **Cross-country Analysis**: Compare uncertainty patterns across countries
5. **Market Impact**: Study how uncertainty affects stock market returns and volatility

## Notes

- All visualizations use consistent styling (seaborn whitegrid theme)
- Figure sizes are optimized for readability (14x6 or 16x6 inches)
- All notebooks include data quality checks
- Spanish format data (S&P 500) is properly cleaned and converted
- Excel files are automatically converted to CSV for easier future use

---

**Created**: 2026-02-03  
**Last Updated**: 2026-02-03  
**Author**: Automated EDA Pipeline
