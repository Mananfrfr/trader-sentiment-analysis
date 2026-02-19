import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

st.set_page_config(page_title="Trader Sentiment Dashboard", layout="wide")

st.title("📊 Trader Performance vs Market Sentiment")

# ============================================================
# LOAD DATA
# ============================================================

@st.cache_data
def load_data():
    trader_df = pd.read_csv("historical_data.csv")
    sentiment_df = pd.read_csv("fear_greed_index.csv")

    trader_df["datetime"] = pd.to_datetime(trader_df["Timestamp"], unit="ms")
    trader_df["date"] = trader_df["datetime"].dt.date
    sentiment_df["date"] = pd.to_datetime(sentiment_df["date"]).dt.date

    def simplify_sentiment(x):
        if "Fear" in x:
            return "Fear"
        elif "Greed" in x:
            return "Greed"
        else:
            return "Neutral"

    sentiment_df["sentiment_bucket"] = sentiment_df["classification"].apply(simplify_sentiment)

    merged_df = trader_df.merge(
        sentiment_df[["date", "sentiment_bucket"]],
        on="date",
        how="inner"
    )

    return merged_df

merged_df = load_data()

st.write("Merged dataset shape:", merged_df.shape)

# ============================================================
# SIDEBAR FILTER
# ============================================================

st.sidebar.header("Filters")

sentiment_filter = st.sidebar.selectbox(
    "Select Sentiment",
    ["All"] + list(merged_df["sentiment_bucket"].unique())
)

if sentiment_filter != "All":
    filtered_df = merged_df[merged_df["sentiment_bucket"] == sentiment_filter]
else:
    filtered_df = merged_df

# ============================================================
# PERFORMANCE SECTION
# ============================================================

st.header("📈 Performance Analysis")

daily_pnl = (
    filtered_df
    .groupby(["date", "Account", "sentiment_bucket"])["Closed PnL"]
    .sum()
    .reset_index()
)

avg_pnl = daily_pnl.groupby("sentiment_bucket")["Closed PnL"].mean()

st.subheader("Average Daily PnL by Sentiment")
st.bar_chart(avg_pnl)

# Win rate
filtered_df["win_flag"] = filtered_df["Closed PnL"] > 0

daily_win = (
    filtered_df
    .groupby(["date", "Account", "sentiment_bucket"])["win_flag"]
    .mean()
    .reset_index()
)

avg_win_rate = daily_win.groupby("sentiment_bucket")["win_flag"].mean()

st.subheader("Average Win Rate by Sentiment")
st.bar_chart(avg_win_rate)

# ============================================================
# BEHAVIOR SECTION
# ============================================================

st.header("⚙️ Behavioral Metrics")

# Trade frequency
daily_trades = (
    filtered_df
    .groupby(["date", "Account"])
    .size()
    .reset_index(name="num_trades")
)

st.subheader("Average Trades per Day")
st.write(daily_trades["num_trades"].mean())

# Position size
st.subheader("Average Position Size")
st.write(filtered_df["Size USD"].mean())

# Long ratio
long_short = (
    filtered_df
    .groupby(["sentiment_bucket", "Side"])
    .size()
    .unstack(fill_value=0)
)

long_short["total"] = long_short.sum(axis=1)
long_short["long_ratio"] = long_short.get("BUY", 0) / long_short["total"]

st.subheader("Long Ratio by Sentiment")
st.bar_chart(long_short["long_ratio"])

# ============================================================
# CLUSTERING SECTION
# ============================================================

st.header("🧠 Trader Archetype Clustering")

trader_features = filtered_df.groupby("Account").agg({
    "Closed PnL": "mean",
    "Size USD": "mean",
    "win_flag": "mean"
}).reset_index()

trader_features.rename(columns={
    "Closed PnL": "avg_pnl",
    "Size USD": "avg_trade_size",
    "win_flag": "avg_win_rate"
}, inplace=True)

if len(trader_features) > 10:
    scaler = StandardScaler()
