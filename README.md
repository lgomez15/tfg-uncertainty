# TFG Uncertainty Analysis

This repository contains the code and data for the Final Degree Project (TFG) focused on uncertainty analysis in financial and economic indicators.

## Project Structure

```text
tfg-uncertainty/
├── data/                       # Project data
│   ├── raw/                    # Original, immutable data (8 datasets)
│   │   └── README.md           # Dataset descriptions and citations
│   └── processed/              # Cleaned and transformed data (2 files)
│       └── README.md           # Processed data dictionary
├── models/                     # Saved trained models (.pkl, .h5, etc.)
├── notebooks/                  # Jupyter notebooks for experimentation
│   ├── exploratory/            # Exploratory Data Analysis (EDA)
│   │   ├── raw/                # Individual dataset explorations (8 notebooks)
│   │   │   └── README.md       # Detailed EDA documentation
│   │   └── merged/             # Cross-dataset analyses (3 themes)
│   │       ├── china_uncertainty_markets/  (2 notebooks)
│   │       │   └── README.md
│   │       ├── us_uncertainty_markets/     (2 notebooks)
│   │       │   └── README.md
│   │       └── geopolitics_monthly/        (planned)
│   │           └── README.md
│   ├── cleaning_and_preparation/  # Data cleaning and merging (2 notebooks)
│   │   └── README.md
│   └── training/               # Model training and evaluation
├── references/                 # Data dictionaries, manuals, and papers
├── src/                        # Modular Python source code
├── .gitignore                  # Git ignore rules
├── requirements.txt            # Project dependencies
└── README.md                   # This file
```

## Datasets

The project analyzes **8 datasets** covering uncertainty indices and market performance:

### Uncertainty Indices
- **US EPU Daily** (1985–present): US Economic Policy Uncertainty Index
- **US-China Tension** (1993–2024): Monthly bilateral tension index
- **CEPU China Mainland** (1949–present): China Economic Policy Uncertainty from newspapers
- **Migration Fear** (1990–present): Quarterly migration-related EPU for UK, Germany, USA, France

### Market Indices & Assets
- **CSI 300 Daily** (2005–present): Chinese stock market index
- **S&P 500 Daily** (2020–present): US stock market index
- **Bitcoin Daily** (2013–present): Cryptocurrency price data
- **Gold Daily** (2005–present): Precious metal price data

📄 **See [`data/raw/README.md`](data/raw/README.md) for detailed dataset descriptions, citations, and sources.**

## Processed Data

Two processed datasets are generated from the Phase 1 cleaning pipelines:

| File | Frequency | Observations | Description |
|------|-----------|--------------|-------------|
| `usepu_assets_daily_features.csv` | Daily | ~2,200 | US EPU + S&P 500 + Gold + Bitcoin (29 cols) |
| `cepu_csi300_merged.csv` | Monthly | ~240 | China EPU + CSI 300 (17 cols) |

📄 **See [`data/processed/README.md`](data/processed/README.md) for feature dictionaries and usage examples.**

## Exploratory Notebooks

### Individual Dataset Explorations (`notebooks/exploratory/raw/`)

1. `01_us_epu_daily_exploration.ipynb` — US Economic Policy Uncertainty
2. `02_csi300_daily_exploration.ipynb` — CSI 300 Stock Index
3. `03_sp500_daily_exploration.ipynb` — S&P 500 Stock Index
4. `04_us_china_tension_exploration.ipynb` — US-China Tension Index
5. `05_cepu_china_mainland_exploration.ipynb` — China EPU (Mainland)
6. `06_migration_fear_exploration.ipynb` — Migration Fear Indices
7. `07_btc_daily_exploration.ipynb` — Bitcoin Price Analysis
8. `08_gold_daily_exploration.ipynb` — Gold Price Analysis

📄 **See [`notebooks/exploratory/raw/README.md`](notebooks/exploratory/raw/README.md) for detailed notebook documentation.**

### Merged Analyses (`notebooks/exploratory/merged/`)

Cross-dataset analyses combining multiple sources by theme. Each theme has **two notebooks** with complementary analytical styles:

#### 1. China Uncertainty & Markets

Combines China EPU and CSI 300 to analyze the relationship between Chinese economic policy uncertainty and market performance.

| Notebook | Style | Key Methods |
|----------|-------|-------------|
| `01_china_uncertainty_markets_analysis.ipynb` | Academic | Pearson+Spearman, crisis lines, subperiod analysis |
| `02_AI_china_uncertainty_markets_analysis.ipynb` | Applied | Scatter+regression, Granger causality, shock analysis |

📄 **See [`notebooks/exploratory/merged/china_uncertainty_markets/README.md`](notebooks/exploratory/merged/china_uncertainty_markets/README.md)**

#### 2. US Uncertainty & Markets

Combines US EPU, S&P 500, Bitcoin, and Gold to study how US economic policy uncertainty affects traditional and alternative assets.

| Notebook | Style | Key Methods |
|----------|-------|-------------|
| `01_us_uncertainty_markets_analysis.ipynb` | Applied | Scatter+regression, Granger causality, shock analysis |
| `02_AI_us_uncertainty_markets_analysis.ipynb` | Academic | Pearson+Spearman, crisis lines, subperiod analysis |

📄 **See [`notebooks/exploratory/merged/us_uncertainty_markets/README.md`](notebooks/exploratory/merged/us_uncertainty_markets/README.md)**

#### 3. Geopolitics Monthly

Monthly-level analysis of geopolitical tensions and their impact on global markets and uncertainty indices.

📄 **See [`notebooks/exploratory/merged/geopolitics_monthly/README.md`](notebooks/exploratory/merged/geopolitics_monthly/README.md)**

## Data Cleaning Pipelines

| Notebook | Input | Output |
|----------|-------|--------|
| `01_us_assets_cleaning_and_preparation.ipynb` | US EPU + S&P 500 + Gold + Bitcoin (raw) | `usepu_assets_daily_features.csv` |
| `02_china_assets_cleaning_and_preparation.ipynb` | China EPU + CSI 300 (raw) | `cepu_csi300_merged.csv` |

📄 **See [`notebooks/cleaning_and_preparation/README.md`](notebooks/cleaning_and_preparation/README.md)**

## Getting Started

### Prerequisites
- Python 3.8+
- Virtual environment (recommended)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/lgomez15/tfg-uncertainty.git
   cd tfg-uncertainty
   ```

2. Create and activate virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Exploratory Data Analysis
```bash
cd notebooks/exploratory/raw
jupyter lab
```

### Data Processing
- **Individual dataset explorations**: `notebooks/exploratory/raw/`
- **Cross-dataset analyses**: `notebooks/exploratory/merged/`
- **Data cleaning and preparation**: `notebooks/cleaning_and_preparation/`
- **Model training**: `notebooks/training/`

## Project Workflow

1. **Data Collection**: Raw datasets stored in `data/raw/` with full citations
2. **Individual Exploration**: Analyze individual datasets in `notebooks/exploratory/raw/` (8 notebooks)
3. **Phase 1 — Data Cleaning**: Merge and clean datasets in `notebooks/cleaning_and_preparation/`
   - US pipeline → `data/processed/usepu_assets_daily_features.csv`
   - China pipeline → `data/processed/cepu_csi300_merged.csv`
4. **Phase 2 — Exploratory Analysis**: Study relationships in `notebooks/exploratory/merged/`
   - Descriptive statistics, correlations (Pearson + Spearman), quantile analysis
   - Lead-lag relationships, Granger causality, rolling correlations
   - Subperiod analysis, shock analysis
   - Output: Modeling recommendations
5. **Phase 3 — Model Training**: Build and evaluate models in `notebooks/training/`
6. **Deployment**: Save models to `models/` directory

## Documentation

| Topic | README |
|-------|--------|
| Dataset Sources | [`data/raw/README.md`](data/raw/README.md) |
| Processed Data | [`data/processed/README.md`](data/processed/README.md) |
| EDA (Individual) | [`notebooks/exploratory/raw/README.md`](notebooks/exploratory/raw/README.md) |
| Cleaning Pipelines | [`notebooks/cleaning_and_preparation/README.md`](notebooks/cleaning_and_preparation/README.md) |
| China Analysis | [`notebooks/exploratory/merged/china_uncertainty_markets/README.md`](notebooks/exploratory/merged/china_uncertainty_markets/README.md) |
| US Analysis | [`notebooks/exploratory/merged/us_uncertainty_markets/README.md`](notebooks/exploratory/merged/us_uncertainty_markets/README.md) |
| Geopolitics | [`notebooks/exploratory/merged/geopolitics_monthly/README.md`](notebooks/exploratory/merged/geopolitics_monthly/README.md) |

## References

Academic papers and documentation are stored in `references/`:
- Análisis de Series Temporales con R
- Pronóstico de Riesgo Financiero
- Economic Policy Uncertainty research papers

## License

This project is part of a Final Degree Project (TFG).
