# TFG Uncertainty Analysis

This repository contains code, data pipelines, and exploratory notebooks for a Final Degree Project (TFG) on uncertainty indicators and financial-market volatility.

## Project Structure

```text
tfg-uncertainty/
├── data/
│   ├── raw/                       # Original files + normalized CSV exports
│   │   └── README.md
│   └── processed/                 # Modeling-ready datasets
│       └── README.md
├── models/                        # Trained models (artifacts)
├── notebooks/
│   ├── cleaning_and_preparation/  # Phase 1 pipelines (2 notebooks)
│   │   └── README.md
│   ├── exploratory/
│   │   ├── raw/                   # Individual-source EDA (8 notebooks)
│   │   │   └── README.md
│   │   └── merged/                # Cross-source EDA by theme
│   │       ├── china_uncertainty_markets/   # 2 notebooks + README
│   │       ├── us_uncertainty_markets/      # 2 notebooks + README
│   │       └── geopolitics_monthly/         # planned, README only
│   └── training/                  # Phase 3 notebooks
├── references/
├── src/
├── fix_path.py
├── requirements.txt
└── README.md
```

## Current Processed Datasets

| File | Frequency | Rows | Columns | Coverage |
|------|-----------|------|---------|----------|
| `panel_usa_mensual.csv` | Monthly | 139 | EPU + vol(SP500,Gold,BTC) | 2014-01 to 2025-07 |
| `panel_china_mensual.csv` | Monthly | 139 | CNEPU + vol(CSI300,Gold,BTC) | 2014-01 to 2025-07 |
| `rendimientos_mensuales.csv` / `rendimientos_diarios.csv` | Monthly / Daily | — | log-returns per asset | 2014 to 2025 |
| `usepu_assets_daily_features.csv` | Daily | 2227 | 29 | 2014-01-03 to 2023-11-13 (legacy) |
| `cepu_csi300_merged.csv` | Monthly | 247 | 17 | 2005+ (legacy) |

The `panel_*` files are the **unified, same-period, same-frequency** datasets used by the TFG
(produced by `notebooks/cleaning_and_preparation/03_unified_panels_2014_2025.ipynb`). The two
`legacy` files come from the earlier (non-comparable) design and are kept for reference only.
See [`data/processed/README.md`](data/processed/README.md) for feature definitions.

## Notebook Inventory

### Phase 1 — Cleaning & Preparation
- `notebooks/cleaning_and_preparation/01_us_assets_cleaning_and_preparation.ipynb`
- `notebooks/cleaning_and_preparation/02_china_assets_cleaning_and_preparation.ipynb`
- `notebooks/cleaning_and_preparation/03_unified_panels_2014_2025.ipynb` — **unified monthly panels** (same period and assets for both countries; current pipeline)

### Phase 2 — Exploratory (Merged)
- US theme: `notebooks/exploratory/merged/us_uncertainty_markets/`
- China theme: `notebooks/exploratory/merged/china_uncertainty_markets/`
- Geopolitics monthly: `notebooks/exploratory/merged/geopolitics_monthly/` (pending notebook implementation)

### Phase 3 — Training / Analysis
- `notebooks/training/01_us_epu_markets_dd.ipynb` (legacy)
- `notebooks/training/02_garch_x_modeling_garch.ipynb` (legacy)
- `notebooks/training/03_analisis_incertidumbre_volatilidad.ipynb` — **current analysis**: four research questions (correlation, quintiles, Granger, GARCH); writes `reports/figures/` and `reports/resultados.json`.

## Snapshot of Main Results (unified 2014–2025, monthly, notebook 03)

Source of truth: `reports/resultados.json` (produced by the analysis notebook). The write-up
(`redaccion/Boceto_TFG.docx`) reads its numbers and figures from there.

### US EPU vs asset volatility
- Pearson EPU–vol: S&P 500 `0.453`, Gold `0.510`, Bitcoin `-0.050`.
- Regime effect (Q5/Q1): S&P 500 `2.077`, Gold `1.443`, Bitcoin `1.124`.
- Granger (EPU → vol): significant only for **Gold** (`F=7.446`, `p=0.007`); not for S&P 500 / BTC.
- GARCH conditional vol vs EPU: S&P 500 `0.510`, Gold `0.717`, BTC `-0.073`.
- Regime change: EPU–S&P 500 corr `0.103` (pre-2020) → `0.407` (since 2020).

### China CNEPU vs asset volatility
- Pearson CNEPU–vol: CSI 300 `-0.197` (negative), Gold `0.237`, Bitcoin `-0.104`.
- Regime effect (Q5/Q1): CSI 300 `0.760` (inverse).

> Earlier daily-frequency numbers (S&P 500 `0.625`, China `-0.321`, etc.) belong to the legacy,
> non-comparable design and are superseded by the unified analysis above.

Detailed per-theme documentation:
- [`notebooks/exploratory/merged/us_uncertainty_markets/README.md`](notebooks/exploratory/merged/us_uncertainty_markets/README.md)
- [`notebooks/exploratory/merged/china_uncertainty_markets/README.md`](notebooks/exploratory/merged/china_uncertainty_markets/README.md)

## Quick Start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
jupyter lab
```

## Documentation Map

- Raw sources and provenance: [`data/raw/README.md`](data/raw/README.md)
- Processed schema and missingness: [`data/processed/README.md`](data/processed/README.md)
- Cleaning pipelines: [`notebooks/cleaning_and_preparation/README.md`](notebooks/cleaning_and_preparation/README.md)
- Raw EDA notebooks: [`notebooks/exploratory/raw/README.md`](notebooks/exploratory/raw/README.md)
- Geopolitics placeholder scope: [`notebooks/exploratory/merged/geopolitics_monthly/README.md`](notebooks/exploratory/merged/geopolitics_monthly/README.md)
