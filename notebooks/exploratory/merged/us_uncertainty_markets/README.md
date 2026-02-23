# US Uncertainty & Markets Analysis

## Scope

Phase 2 exploratory analysis of US Economic Policy Uncertainty (EPU) versus volatility in S&P 500, Gold, and Bitcoin.

## Data used

- Input: `data/processed/usepu_assets_daily_features.csv`
- Frequency: Daily
- Shape: `2227 x 29`
- Coverage: `2014-01-03` to `2023-11-13`

## Notebooks

### `01_us_uncertainty_markets_analysis.ipynb`

Applied workflow:
1. quality checks,
2. descriptive/distribution analysis,
3. temporal plots + rolling correlations,
4. static/scatter correlations,
5. quintile + shock analysis,
6. lagged correlations + Granger tests,
7. consolidated key findings for modeling.

### `02_AI_us_uncertainty_markets_analysis.ipynb`

Alternative framing of the same data with:
- Pearson/Spearman comparison,
- longer lag scans,
- subperiod checks,
- conclusion table for robust patterns.

## Quantitative findings snapshot

From saved notebook outputs:

- Full-sample correlation with `Vol30d`:
	- EPU ↔ S&P 500: `0.6255`
	- EPU ↔ Gold: `0.5450`
	- EPU ↔ Bitcoin: `0.0254`

- Best lag (EPU → Vol30d):
	- S&P 500: `0d` (`r=0.6255`)
	- Gold: `2d` (`r=0.5460`)
	- Bitcoin: weak (`25d`, `r=-0.0342`)

- EPU regime effect (Q5/Q1 ratio in Vol30d):
	- S&P 500: `1.93x`
	- Gold: `1.31x`
	- Bitcoin: `1.02x`

- Shock-day share in applied notebook: `223` days (`10.0%`).

## Modeling implication (EDA-level)

- EPU level is materially informative for S&P 500 and Gold volatility.
- Bitcoin volatility appears comparatively decoupled from EPU in this sample.
- Lagged EPU features are most justified for Gold and (to a lesser extent) S&P 500.

Last updated: 2026-02-23
