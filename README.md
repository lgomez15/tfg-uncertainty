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
| `usepu_assets_daily_features.csv` | Daily | 2227 | 29 | 2014-01-03 to 2023-11-13 |
| `cepu_csi300_merged.csv` | Monthly | 247 | 17 | 2005+ (monthly overlap) |

See [`data/processed/README.md`](data/processed/README.md) for feature definitions.

## Notebook Inventory

### Phase 1 — Cleaning & Preparation
- `notebooks/cleaning_and_preparation/01_us_assets_cleaning_and_preparation.ipynb`
- `notebooks/cleaning_and_preparation/02_china_assets_cleaning_and_preparation.ipynb`

### Phase 2 — Exploratory (Merged)
- US theme: `notebooks/exploratory/merged/us_uncertainty_markets/`
- China theme: `notebooks/exploratory/merged/china_uncertainty_markets/`
- Geopolitics monthly: `notebooks/exploratory/merged/geopolitics_monthly/` (pending notebook implementation)

### Phase 3 — Training
- `notebooks/training/01_us_epu_markets_dd.ipynb`
- `notebooks/training/02_garch_x_modeling_garch.ipynb`

## Snapshot of Main EDA Results

### US EPU vs Assets (daily)
- EPU–Vol30d correlations: S&P 500 `0.625`, Gold `0.545`, Bitcoin `0.025`.
- EPU high-regime effect (Q5/Q1 in Vol30d): S&P 500 `1.93x`, Gold `1.31x`, Bitcoin `1.02x`.
- Strongest lag correlation: S&P 500 lag `0d`, Gold lag `2d`, Bitcoin weak.

### China CNEPU vs CSI 300 (monthly)
- CNEPU–CSI volatility relationship is **negative** in full sample (`-0.321` with `CSI_Vol`).
- Best lag for CNEPU → CSI_Vol appears at `12` months (`r = -0.391`).
- High CNEPU regime (Q5) shows lower mean CSI_Vol than Q1 (Q5/Q1 `0.65x`).

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
