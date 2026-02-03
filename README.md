# TFG Uncertainty Analysis

This repository contains the code and data for the Final Degree Project (TFG) focused on uncertainty analysis in financial and economic indicators.

## Project Structure

```text
├── config/             # Configuration files (YAML, JSON, etc.)
├── data/               # Project data
│   ├── raw/            # Original, immutable data
│   └── processed/      # Cleaned and transformed data
├── logs/               # Application and process logs
├── models/             # Saved trained models (.pkl, .h5, etc.)
├── notebooks/          # Jupyter notebooks for experimentation
│   ├── exploratory/    # EDA and discovery
│   ├── cleaning/       # Data preparation logic
│   └── training/       # Model training and evaluation
├── references/         # Data dictionaries, manuals, and papers
├── src/                # Modular Python source code
├── .gitignore          # Git ignore rules
├── requirements.txt    # Project dependencies
└── README.md           # This file
```

## Getting Started

### Prerequisites
- Python 3.8+
- [Optional] Virtual environment (venv or conda)

### Installation
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
- Explore the datasets in `notebooks/exploratory/`.
- Run data cleaning notebooks in `notebooks/cleaning/`.
- Train models using `notebooks/training/`.
