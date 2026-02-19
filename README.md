# Primetrade.ai – Data Science Intern Assignment


**NOTE-ALL THE CHARTS ARE SHOW IN THE .ipynb file itself**
**Objective:**

Analyze how Bitcoin market sentiment (Fear vs Greed) influences trader behavior and performance on Hyperliquid. Identify patterns and propose actionable strategy recommendations.

Methodology:

**1️) Data Preparation**

#Converted trade timestamps to daily resolution

#Aligned trader data with daily sentiment regime

#Engineered daily trader-level metrics:

#Daily PnL

#Win rate

#Trade frequency

#Average trade size

#Long/Short ratio

#Aggregated metrics for sentiment-based comparison

**2️). Performance Analysis**

Compared performance metrics under:

#Fear regime

#Greed regime

Metrics analyzed:

#Average daily PnL

#Median PnL

#Win rate

#Drawdown proxy (negative PnL)

**3️). Behavioral Analysis**

Examined regime-based changes in:

#Trade frequency

#Capital exposure

#Directional bias

4️).Trader Segmentation

Applied KMeans clustering using:

#Average PnL

##Average trade size

#Average win rate

Identified behavioral archetypes for risk-adjusted capital allocation.

**Key Insights**

Performance differs by regime
Traders exhibit higher average profitability and win rate during Fear regimes compared to Greed.

Greed increases downside risk
Drawdown proxy is larger during Greed periods, indicating elevated downside volatility.

Behavior adapts to sentiment
Trade frequency and exposure tend to increase during Fear regimes.

Trader archetypes differ structurally
Clustering reveals distinct groups:

High-exposure aggressive traders

Moderate consistent traders

Low-risk low-return traders

 **Strategy Recommendations**

**Strategy 1** — Regime-Based Risk Scaling

Increase capital allocation moderately during Fear regimes.

Reduce leverage exposure during Greed regimes.

Tighten risk controls when sentiment shifts to Greed.

**Strategy 2** — Segment-Based Allocation

Allocate more capital to consistent traders across regimes.

Limit exposure to high-volatility traders during Greed.

Use trader archetype classification for adaptive portfolio weighting.

 **Bonus: Interactive Dashboard**

A Streamlit dashboard (app.py) allows interactive exploration of:

Sentiment-based performance

Behavioral metrics

Trader clustering visualization

****Run locally:

pip install -r requirements.txt

streamlit run app.py****