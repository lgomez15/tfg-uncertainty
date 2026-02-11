# US Uncertainty & Markets Analysis - README

## Overview

This directory contains the **Phase 2 exploratory analysis** of relationships between US Economic Policy Uncertainty (EPU) and asset volatilities (S&P 500, Gold, Bitcoin).

## Notebook

### `01_us_uncertainty_markets_analysis.ipynb`

Comprehensive exploratory analysis with the following sections:

#### 1. Data Loading
- Loads processed data from `data/processed/usepu_assets_daily_features.csv`
- Validates data quality and checks for missing values

#### 2. Descriptive Statistics
- **Summary statistics**: mean, std, min, max, skewness, kurtosis
- **Distribution plots**: Histograms for EPU, ΔEPU, returns, and volatilities
- **Outlier detection**: Boxplots for returns and volatilities

#### 3. Temporal Analysis
- **Time series plots**: EPU and asset volatilities over time
- **Rolling correlations**: 30-day and 90-day windows
- **Co-movement patterns**: Visual identification of correlation regimes

#### 4. Correlation Analysis
- **Static correlation matrix**: Heatmap of all key features
- **Scatter plots with regression**: ΔEPU vs each asset volatility
- **Correlation coefficients**: Quantifies relationship strength

#### 5. Quantile Analysis
- **EPU quintile stratification**: Mean volatility by EPU level (Q1-Q5)
- **ΔEPU quintile stratification**: Mean volatility by EPU change magnitude
- **Shock analysis**: Extreme EPU changes (top 10%) vs normal periods

#### 6. Lead-Lag Analysis
- **Lagged correlations**: EPU and ΔEPU lags 0-7 days vs current volatility
- **Cross-correlation plots**: Identifies optimal lag structure
- **Granger causality tests**: Formal tests for predictive relationships

#### 7. Key Findings Summary
- Comprehensive summary of all analyses
- Quantitative metrics for each finding
- **Modeling recommendations**: Feature selection, target selection, model complexity, temporal dynamics

## Key Insights

### Correlation Patterns
- Static correlations between EPU and asset volatilities
- Time-varying nature of relationships (rolling correlations)
- ΔEPU shows different patterns than EPU level

### Non-Linear Relationships
- Quantile analysis reveals non-linear effects
- Higher EPU quintiles → higher volatility
- Shock periods show amplified volatility

### Predictive Power
- Lagged correlations suggest EPU has predictive value
- Granger causality tests provide formal evidence
- EPU appears to lead volatility changes (not just react)

### Asset-Specific Dynamics
- S&P 500, Gold, and Bitcoin show different EPU relationships
- Bitcoin volatility shows weaker correlation with EPU
- Gold may serve as safe haven during high EPU periods

---

**Created**: 2026-02-10  
**Input**: `data/processed/usepu_assets_daily_features.csv`  
**Status**: Complete and ready for modeling
