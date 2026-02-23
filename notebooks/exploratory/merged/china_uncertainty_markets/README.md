# China Uncertainty & Markets Analysis

## Scope

Phase 2 exploratory analysis of China EPU (`CNEPU`) versus CSI 300 return/volatility dynamics.

## Data used

- Input: `data/processed/cepu_csi300_merged.csv`
- Frequency: Monthly
- Rows: `247` (core complete cases: `246`)
- Features: `17`

## Notebooks

### `01_china_uncertainty_markets_analysis.ipynb`

Academic-style workflow with:
- descriptive diagnostics,
- crisis-aware time-series inspection,
- Pearson/Spearman correlation views,
- lag and rolling-correlation analysis,
- subperiod robustness checks.

### `02_AI_china_uncertainty_markets_analysis.ipynb`

Applied-style workflow with:
- static + scatter correlation blocks,
- quintile and shock regime analysis,
- lagged correlations + Granger tests,
- summary table for modeling guidance.

## Quantitative findings snapshot

From saved notebook outputs:

- Full-sample correlations:
	- `Corr(CNEPU, CSI_Vol) = -0.3214`
	- `Corr(CNEPU, CSI_Vol3m) = -0.2448`
	- `Corr(CNEPU, CSI_Vol6m) = -0.3234`
	- `Corr(ΔCNEPU, CSI_Vol) = 0.0010`

- Best lag (CNEPU → CSI_Vol):
	- `12` months, `r = -0.3911`

- Regime contrast (CNEPU quintiles):
	- mean `CSI_Vol` in Q1: `0.017115`
	- mean `CSI_Vol` in Q5: `0.011184`
	- ratio Q5/Q1: `0.65x`

- Shock-share (applied notebook):
	- `25` months (`10.1%`), with lower volatility than normal months in this sample.

## Interpretation note

In this dataset version, the CNEPU-volatility relationship is predominantly **negative** in static and lagged summaries, so any modeling assumptions of a positive sign should be tested explicitly out-of-sample.

Last updated: 2026-02-23
