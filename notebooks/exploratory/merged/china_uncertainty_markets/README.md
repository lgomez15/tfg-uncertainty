# China Uncertainty & Markets Analysis

## Overview

This directory contains the **Phase 2 exploratory analysis** of relationships between China Economic Policy Uncertainty (CNEPU) and CSI 300 index volatility.

## Data

**Input**: `data/processed/cepu_csi300_merged.csv`  
**Frequency**: Monthly  
**Date Range**: 2005–present (~240 observations)

### Key Variables

| Variable     | Description                           |
| ------------ | ------------------------------------- |
| `CNEPU`      | China EPU index (mainland newspapers) |
| `ΔCNEPU`     | Monthly change in CNEPU               |
| `CNEPU_MA12` | 12-month moving average               |
| `CSI_Return` | CSI 300 monthly return                |
| `CSI_Vol`    | CSI 300 monthly volatility            |
| `CSI_Vol3m`  | 3-month rolling volatility            |
| `CSI_Vol6m`  | 6-month rolling volatility            |

## Notebooks

### `01_china_uncertainty_markets_analysis.ipynb`

**Style**: Academic / China-focused  
Comprehensive monthly EDA with the following sections:

1. **Data Overview** — Structure, missing values, temporal coverage
2. **Time Series Visualisation** — CNEPU and CSI 300 with crisis vertical lines (2008 GFC, 2015 stock crash, COVID-19)
3. **Distributions & Outliers** — Histograms, boxplots, skewness/kurtosis
4. **Correlation Analysis** — Pearson & Spearman side-by-side heatmaps
5. **Quintile Analysis** — CNEPU quintiles vs volatility/return bar plots
6. **Lead-Lag Analysis** — Monthly lags 0–12 with best-lag annotation
7. **Rolling Correlations** — 24-month and 36-month windows
8. **Subperiod Analysis** — Structural robustness across 3 temporal regimes
9. **EDA Conclusions** — Bullet-point synthesis of key patterns

### `02_AI_china_uncertainty_markets_analysis.ipynb`

**Style**: US practical / applied  
Same China monthly data analysed with the US notebook's methodology:

1. **Data Loading** — Quality checks and missing values
2. **Descriptive Statistics** — Summary stats, skewness/kurtosis table, distribution histograms
3. **Temporal Analysis** — Time series plots, rolling correlations (12m/24m)
4. **Correlation Analysis** — Static heatmap, scatter plots with OLS regression lines
5. **Quantile Analysis** — CNEPU/ΔCNEPU quintile stratification, shock analysis (90th percentile)
6. **Lead-Lag Analysis** — Lagged correlations (0–12 months), **Granger causality tests** (up to 6 lags)
7. **Key Findings Summary** — Quantitative summary + modelling recommendations

## Key Insights

- **CNEPU–Volatility association**: Positive correlation between CNEPU and CSI 300 volatility, varying across subperiods
- **Non-linear effects**: Higher CNEPU quintiles show disproportionately elevated volatility
- **Lead-lag structure**: CNEPU may contain leading information for CSI 300 volatility at monthly horizons
- **Regime dependence**: Rolling correlations reveal crisis-driven strengthening of the association

---

**Created**: 2026-02-11  
**Input**: `data/processed/cepu_csi300_merged.csv`  
**Status**: Complete — two complementary EDA perspectives
