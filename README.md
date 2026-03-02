# Bitcoin Sentiment–Driven Trader Performance Analysis

> A quantitative research project analyzing how Bitcoin Fear & Greed sentiment regimes influence trader behavior and profitability on Hyperliquid.

Built with **Pandas**, **NumPy**, **Scikit-learn**, and **Streamlit** for interactive exploration.

---

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Methodology](#methodology)
- [Key Findings](#key-findings)
- [Strategy Recommendations](#strategy-recommendations)
- [Interactive Dashboard](#interactive-dashboard)
- [Setup & Usage](#setup--usage)
- [Assumptions & Limitations](#assumptions--limitations)
- [Future Improvements](#future-improvements)

---

## Overview

This project investigates how Bitcoin market sentiment — measured via the **Fear & Greed Index** — impacts real trader performance on the Hyperliquid perpetuals exchange. By mapping daily sentiment regimes to individual trader activity, the analysis surfaces regime-dependent patterns in profitability, risk-taking, and behavioral archetypes.

**Core questions addressed:**
- Do traders perform better during Fear or Greed regimes?
- How does sentiment shift trade frequency, sizing, and directional bias?
- Can trader behavioral clusters enable smarter, risk-adjusted capital allocation?

---

## Project Structure

```
sentiment_analysis/
├── data/
│   ├── trader_data.csv         # Raw Hyperliquid trade records
│   ├── sentiment_data.csv      # Daily Bitcoin Fear & Greed scores
│   └── processed_data.csv      # Merged, engineered dataset
├── notebooks/
│   └── analysis.ipynb          # Full analysis with inline visualizations
├── app.py                      # Streamlit interactive dashboard
├── requirements.txt
└── README.md
```

---

## Methodology

### 1. Data Preparation

- Converted trade timestamps to **daily resolution**
- Mapped each trader's daily activity to the corresponding **sentiment regime** (Fear / Greed)
- Engineered the following **trader-level daily metrics**:
  - Daily PnL
  - Win rate
  - Trade frequency
  - Average trade size
  - Long/Short ratio
- Aggregated all metrics by sentiment regime for comparison

### 2. Performance Analysis

Compared key performance metrics across Fear and Greed regimes:

| Metric | Fear Regime | Greed Regime |
|---|---|---|
| Average Daily PnL | Higher | Lower |
| Median PnL | More stable | More volatile |
| Win Rate | Higher | Lower |
| Drawdown Proxy | Smaller | Larger |

**Key observation:** Trader performance is materially better during Fear regimes, while Greed periods introduce higher downside volatility.

### 3. Behavioral Analysis

Examined how trader behavior adapts across sentiment regimes:

- **Trade frequency** increases during Fear
- **Capital exposure** rises during Fear
- **Directional positioning** shifts with sentiment
- **Downside volatility** is disproportionately higher during Greed

### 4. Trader Segmentation

Applied **K-Means clustering** on three trader-level features:

- Average PnL
- Average trade size
- Average win rate

This surfaced three distinct behavioral archetypes:

| Cluster | Profile |
|---|---|
| Aggressive | High exposure, high variance traders |
| Consistent | Moderate risk, stable returns |
| Conservative | Low risk, low return, low activity |

These clusters support **risk-adjusted capital allocation** strategies.

---

## Key Findings

1. **Regime-Dependent Profitability** — Traders systematically outperform during Fear regimes compared to Greed.
2. **Greed Amplifies Downside Risk** — The drawdown proxy is significantly elevated during Greed periods, indicating overexposure.
3. **Behavioral Adaptation** — Traders increase both activity and exposure during Fear, suggesting contrarian opportunity awareness.
4. **Stable Trader Archetypes** — Clustering reveals consistent behavioral profiles that persist across market conditions, enabling portfolio-level differentiation.

---

## Strategy Recommendations

### Strategy 1 — Regime-Based Risk Scaling

| Regime | Action |
|---|---|
| Fear | Moderately increase capital allocation |
| Greed | Reduce leverage; tighten stop-loss parameters |
| Regime Transition | Reassess position sizing proactively |

### Strategy 2 — Segment-Based Allocation

- Allocate **higher weight** to Consistent traders as core positions
- **Limit exposure** to Aggressive traders during Greed regimes
- **Dynamically rebalance** the portfolio based on current cluster classification and active sentiment regime

---

## Interactive Dashboard

The Streamlit dashboard provides interactive exploration of:

- Sentiment-segmented performance metrics
- Behavioral statistics by regime
- Trader cluster visualization and filtering

---

## Setup & Usage

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the Analysis Notebook

```bash
jupyter notebook notebooks/analysis.ipynb
```

All charts and visualizations are rendered inline within the notebook.

### 3. Launch the Streamlit Dashboard

```bash
streamlit run app.py
```

---

## Assumptions & Limitations

- Sentiment data is at **daily resolution** — intraday regime shifts are not captured
- Traders are assumed to operate in **single position mode**
- **No transaction cost modeling** is included
- Drawdown is **approximated** via the negative tail of PnL distributions, not tracked at position level

---

## Future Improvements

- [ ] Add **rolling Sharpe ratio** per sentiment regime
- [ ] Implement **regime transition detection** using Markov modeling
- [ ] Incorporate **realized volatility** as a control variable
- [ ] Add **risk-adjusted performance metrics**: Sortino ratio, Calmar ratio
- [ ] Introduce **time-decay weighting** to prioritize recent regime data

---

## Summary

This project demonstrates that Bitcoin market sentiment is a **statistically meaningful signal** for trader performance:

- Fear regimes are associated with higher profitability and lower drawdown
- Greed regimes increase systemic risk across the trader population
- Behavioral clustering enables more precise, regime-aware capital allocation

The result is a framework for transforming raw trade data into **actionable, sentiment-driven strategy design**.
