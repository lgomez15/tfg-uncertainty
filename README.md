# TFG Uncertainty Analysis

This repository contains the code and data for the Final Degree Project (TFG) focused on uncertainty analysis in financial and economic indicators.

## Project Structure

```text
tfg-uncertainty/
├── config/                 # Configuration files (YAML, JSON, etc.)
├── data/                   # Project data
│   ├── raw/                # Original, immutable data (10 datasets)
│   └── processed/          # Cleaned and transformed data
├── logs/                   # Application and process logs
├── models/                 # Saved trained models (.pkl, .h5, etc.)
├── notebooks/              # Jupyter notebooks for experimentation
│   ├── exploratory/        # Exploratory Data Analysis (EDA)
│   │   ├── raw/            # Individual dataset explorations (8 notebooks)
│   │   └── merged/         # Cross-dataset analyses (3 notebooks)
│   ├── cleaning/           # Data preparation logic
│   └── training/           # Model training and evaluation
├── references/             # Data dictionaries, manuals, and papers
├── src/                    # Modular Python source code
├── .gitignore              # Git ignore rules
├── requirements.txt        # Project dependencies
└── README.md               # This file
```

## Datasets

The project analyzes **10 datasets** covering uncertainty indices and market performance:

### Uncertainty Indices
- **US EPU Daily** (1985-present): US Economic Policy Uncertainty Index
- **CSI 300 Daily** (2005-present): Chinese stock market index
- **S&P 500 Daily** (2020-present): US stock market index
- **US-China Tension** (1993-2024): Monthly bilateral tension index
- **CEPU China Mainland** (1949-present): China Economic Policy Uncertainty from newspapers
- **Migration Fear** (1990-present): Quarterly migration-related EPU for UK, Germany, USA, France

### Market Assets
- **Bitcoin Daily** (2013-present): Cryptocurrency price data
- **Gold Daily** (2005-present): Precious metal price data

All datasets are stored in `data/raw/` and explored in `notebooks/exploratory/raw/`.

## Exploratory Notebooks

### Individual Dataset Explorations (`notebooks/exploratory/raw/`)
1. `01_us_epu_daily_exploration.ipynb` - US Economic Policy Uncertainty
2. `02_csi300_daily_exploration.ipynb` - CSI 300 Stock Index
3. `03_sp500_daily_exploration.ipynb` - S&P 500 Stock Index
4. `04_us_china_tension_exploration.ipynb` - US-China Tension Index
5. `05_cepu_china_mainland_exploration.ipynb` - China EPU (Mainland)
6. `06_migration_fear_exploration.ipynb` - Migration Fear Indices
7. `07_btc_daily_exploration.ipynb` - Bitcoin Price Analysis
8. `08_gold_daily_exploration.ipynb` - Gold Price Analysis

### Merged Analyses (`notebooks/exploratory/merged/`)
Cross-dataset analyses combining multiple sources:
- **China Uncertainty & Markets**: Combines China EPU, CSI 300, and US-China tension
- **US Uncertainty & Markets**: Combines US EPU, S&P 500, Bitcoin, and Gold
- **Geopolitics Monthly**: Monthly-level geopolitical and uncertainty analysis

See `notebooks/exploratory/raw/DOCS.md` for detailed documentation.

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
# Navigate to exploratory notebooks
cd notebooks/exploratory/raw

# Launch Jupyter
jupyter lab
```

### Data Processing
- Individual dataset explorations: `notebooks/exploratory/raw/`
- Cross-dataset analyses: `notebooks/exploratory/merged/`
- Data cleaning: `notebooks/cleaning/`
- Model training: `notebooks/training/`

## Project Workflow

1. **Exploration**: Analyze individual datasets in `notebooks/exploratory/raw/`
2. **Merging**: Combine datasets for cross-analysis in `notebooks/exploratory/merged/`
3. **Cleaning**: Prepare data for modeling in `notebooks/cleaning/`
4. **Training**: Build and evaluate models in `notebooks/training/`
5. **Deployment**: Save models to `models/` directory

## References

Academic papers and documentation are stored in `references/`:
- Análisis de Series Temporales con R
- Pronóstico de Riesgo Financiero
- Economic Policy Uncertainty research papers

## License

This project is part of a Final Degree Project (TFG) at [University Name].
