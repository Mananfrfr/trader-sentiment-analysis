Bitcoin Sentiment–Driven Trader Performance Analysis

A structured quantitative research project analyzing how Bitcoin Fear & Greed sentiment regimes influence trader behavior and profitability on Hyperliquid.

Built with Pandas, NumPy, Scikit-learn, and Streamlit for interactive exploration.

Project Structure
sentiment_analysis/
├── data/
│   ├── trader_data.csv
│   ├── sentiment_data.csv
│   └── processed_data.csv
├── notebooks/
│   └── analysis.ipynb          # Full analysis (charts rendered inside)
├── app.py                      # Streamlit dashboard
├── requirements.txt
└── README.md
Objective

Analyze how Bitcoin market sentiment (Fear vs Greed) impacts:

Trader profitability

Win rate

Trade frequency

Capital exposure

Directional bias

Then extract actionable trading strategy insights.

Methodology
1️⃣ Data Preparation

Converted trade timestamps to daily resolution

Mapped trader activity to daily sentiment regime

Engineered trader-level daily metrics:

Daily PnL

Win rate

Trade frequency

Average trade size

Long/Short ratio

Aggregated metrics by sentiment regime

All charts are displayed directly inside analysis.ipynb.

2️⃣ Performance Analysis

Compared key metrics across regimes:

Metric	Fear Regime	Greed Regime
Average Daily PnL	✓ Higher	Lower
Median PnL	More stable	More volatile
Win Rate	Higher	Lower
Drawdown Proxy	Smaller	Larger

Observation:
Performance improves during Fear periods.

3️⃣ Behavioral Analysis

Examined how trader behavior shifts with sentiment:

Trade frequency

Capital exposure

Directional positioning

Finding:
Traders increase activity and exposure during Fear.
Greed periods show higher downside volatility.

4️⃣ Trader Segmentation

Applied KMeans clustering using:

Average PnL

Average trade size

Average win rate

Identified behavioral archetypes:

High-exposure aggressive traders

Moderate consistent traders

Low-risk low-return traders

These clusters enable risk-adjusted capital allocation.

Key Insights
1️⃣ Regime-Dependent Profitability

Traders perform better during Fear regimes.

2️⃣ Greed Increases Downside Risk

Drawdown proxy significantly higher during Greed periods.

3️⃣ Behavioral Adaptation

Trading intensity increases in Fear regimes.

4️⃣ Structural Trader Differences

Clustering reveals stable behavioral archetypes.

Strategy Recommendations
Strategy 1 — Regime-Based Risk Scaling

Increase capital allocation moderately during Fear

Reduce leverage exposure during Greed

Tighten stop-loss parameters during Greed shifts

Strategy 2 — Segment-Based Allocation

Allocate higher weight to consistent traders

Limit exposure to aggressive traders during Greed

Dynamically rebalance portfolio based on cluster classification

Interactive Dashboard

A Streamlit dashboard allows interactive exploration of:

Sentiment-based performance metrics

Behavioral statistics

Trader cluster visualization

Setup
1. Install Dependencies
pip install -r requirements.txt
2. Run Analysis Notebook

Open:

notebooks/analysis.ipynb

All visualizations are rendered inside the notebook.

3. Run Dashboard
streamlit run app.py
Assumptions

Sentiment data is daily resolution

Traders operate in a single position mode

No transaction cost modeling included

Drawdown approximated via negative PnL distribution

Future Improvements

Add rolling Sharpe ratio per regime

Add regime transition detection (Markov modeling)

Incorporate volatility as control variable

Add risk-adjusted performance metrics (Sortino, Calmar)

Summary

This project demonstrates that:

Sentiment materially impacts trader performance

Risk increases during Greed

Behavioral clustering enables smarter capital allocation

It transforms raw trade data into actionable regime-aware strategy design.
