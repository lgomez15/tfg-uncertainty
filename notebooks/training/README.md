# Training Notebooks

This directory contains model-oriented notebooks that extend the exploratory phase using volatility-focused methods.

## Notebooks

### 1) `01_us_epu_markets_dd.ipynb`

**Title:** Advanced Volatility Analysis: Drawdowns and GARCH Modeling

**Purpose:**
- Compute drawdowns for S&P 500, Gold, and Bitcoin.
- Estimate univariate GARCH(1,1) conditional volatility for each asset.
- Compare estimated volatility paths with the US EPU index.

**Input:**
- `data/processed/usepu_assets_daily_features.csv`

**Main outputs inside notebook:**
- Drawdown series (`SP500_Drawdown`, `Gold_Drawdown`, `BTC_Drawdown`)
- GARCH conditional volatility series (`*_GARCH_Vol`)
- Comparative plots vs EPU

---

### 2) `02_garch_x_modeling_garch.ipynb`

**Title:** GARCH Volatility and EPU Co-Movement

**Purpose:**
- Build/verify log returns and standardize EPU.
- Validate ARCH effects (ARCH-LM test).
- Fit GARCH(1,1) with Student's t innovations.
- Run residual diagnostics (Ljung-Box on squared standardized residuals).
- Quantify co-movement via OLS regressions: conditional volatility vs standardized EPU.
- Produce 5-step volatility forecasts.
- Run a hold-out exercise using the last 30 observations.

**Input:**
- `data/processed/usepu_assets_daily_features.csv`

**Main outputs inside notebook:**
- `df_vol` conditional volatility and standardized residuals
- OLS tables by asset
- In-sample dynamic plots (CondVol vs `EPU_Std`)
- 5-step ahead forecasts
- Hold-out visualization block (30-observation split)

---

### 3) `03_analisis_incertidumbre_volatilidad.ipynb` (current analysis)

**Title:** Incertidumbre y volatilidad: cuatro preguntas

**Purpose:**
- Current, definitive analysis on the **unified monthly panels** (2014-2025, both countries, index + gold + Bitcoin).
- Organized around four research questions: (1) correlation EPU-volatility (Pearson/Spearman), (2) uncertainty-regime quintiles, (3) Granger causality, (4) GARCH(1,1) conditional volatility.

**Inputs:**
- `data/processed/panel_usa_mensual.csv`, `panel_china_mensual.csv`, `rendimientos_mensuales.csv`, `rendimientos_diarios.csv`

**Main outputs:**
- Figures in `reports/figures/` and a results summary in `reports/resultados.json`.

> Notebooks `01`/`02` belong to the earlier design (daily, non-comparable periods, with ARCH-LM, drawdowns, etc.). The current TFG uses **notebook 03**, which prunes the analysis to four well-justified techniques.

## Execution Notes

- Recommended order:
  1. `01_us_epu_markets_dd.ipynb`
  2. `02_garch_x_modeling_garch.ipynb`

- Required packages (from project environment):
  - `pandas`, `numpy`, `matplotlib`, `seaborn`
  - `statsmodels`
  - `arch`

Both notebooks include a fallback installation attempt for `arch` when missing.

## Relation to Project Workflow

- These notebooks are **Phase 3 (training/modeling-oriented)** and build on:
  - data engineering outputs from `notebooks/cleaning_and_preparation/`
  - exploratory findings from `notebooks/exploratory/merged/`
- The **current** modeling lives in `03_analisis_incertidumbre_volatilidad.ipynb`, on the unified panels from `03_unified_panels_2014_2025.ipynb`.

Last updated: 2026-06-18
