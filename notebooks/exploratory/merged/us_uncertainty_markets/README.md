# US Uncertainty & Markets Analysis

## Overview

This directory contains the **Phase 2 exploratory analysis** of relationships between US Economic Policy Uncertainty (EPU) and asset volatilities (S&P 500, Gold, Bitcoin).

## Data

**Input**: `data/processed/usepu_assets_daily_features.csv`  
**Frequency**: Daily  
**Date Range**: ~2020–present (~2,200 observations)

### Key Variables

| Variable | Description |
|----------|-------------|
| `EPU` | US Economic Policy Uncertainty Index |
| `ΔEPU` | Daily change in EPU |
| `EPU_MA30` | 30-day moving average |
| `SP500_Return` / `Gold_Return` / `BTC_Return` | Daily log returns |
| `SP500_Vol30d` / `Gold_Vol30d` / `BTC_Vol30d` | 30-day rolling volatility |

## Notebooks

### `01_us_uncertainty_markets_analysis.ipynb`

**Style**: US practical / applied  
Comprehensive daily EDA with the following sections:

1. **Data Loading** — Quality checks, missing value analysis
2. **Descriptive Statistics** — Summary stats, distributions, outlier detection (boxplots)
3. **Temporal Analysis** — Time series plots, rolling correlations (30d/90d windows)
4. **Correlation Analysis** — Static heatmap, scatter plots with OLS regression lines
5. **Quantile Analysis** — EPU/ΔEPU quintile stratification, shock analysis (90th percentile)
6. **Lead-Lag Analysis** — Lagged correlations (0–7 days), **Granger causality tests**
7. **Key Findings Summary** — Quantitative summary + modelling recommendations

### `02_AI_us_uncertainty_markets_analysis.ipynb`

**Style**: Academic / China-focused  
Same US daily data analysed with the China notebook's methodology:

1. **Data Overview** — Structure, quality, temporal coverage
2. **Time Series Visualisation** — EPU and volatilities with crisis vertical lines (GFC, COVID-19, Ukraine)
3. **Distributions & Outliers** — Histograms with KDE, boxplots, skewness/kurtosis table
4. **Correlation Analysis** — Pearson & Spearman side-by-side heatmaps + divergence analysis
5. **Quintile Analysis** — EPU/ΔEPU quintiles vs volatility/return bar plots with colour coding
6. **Lead-Lag Analysis** — Daily lags 0–30 with best-lag annotation per asset
7. **Rolling Correlations** — 90-day and 252-day windows with crisis lines
8. **Subperiod Analysis** — Structural robustness across 3 temporal regimes (pre-2013, 2013–2019, 2020+)
9. **EDA Conclusions** — 8-point synthesis of key patterns

## Key Insights

### Correlation Patterns
- Static positive correlation between EPU and asset volatilities (varies by asset)
- Time-varying relationships visible in rolling correlations

### Non-Linear Relationships
- Quantile analysis reveals non-linear effects (Q5 ≫ Q1 volatility)
- Shock periods amplify volatility disproportionately

### Predictive Power
- Lagged correlations suggest EPU has predictive value for volatility
- Granger causality tests provide formal evidence

### Multi-Asset Dynamics
- S&P 500 shows strongest EPU sensitivity; Bitcoin weakest
- Gold may serve as safe haven under elevated uncertainty

---

**Created**: 2026-02-10  
**Updated**: 2026-02-11  
**Input**: `data/processed/usepu_assets_daily_features.csv`  
**Status**: Complete — two complementary EDA perspectives
