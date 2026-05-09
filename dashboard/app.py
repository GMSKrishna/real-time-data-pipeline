import streamlit as st
import requests
import pandas as pd
import os

# -----------------------------
# API URL FROM STREAMLIT SECRETS
# -----------------------------

API_URL = os.getenv("API_URL")

# -----------------------------
# PAGE CONFIG
# -----------------------------

st.set_page_config(
    page_title="Real-Time Financial Intelligence Platform",
    layout="wide"
)

st.title("📊 Real-Time Financial Intelligence Dashboard")

st.markdown(
    "Live crypto analytics with ETL pipeline and FastAPI backend"
)

# -----------------------------
# FETCH LATEST DATA
# -----------------------------

latest_response = requests.get(
    f"{API_URL}/latest-data"
)

latest_data = latest_response.json()

latest_df = pd.DataFrame(latest_data)

# -----------------------------
# FETCH TOP MOVERS
# -----------------------------

movers_response = requests.get(
    f"{API_URL}/top-movers"
)

movers_data = movers_response.json()

movers_df = pd.DataFrame(movers_data)

# -----------------------------
# DASHBOARD LAYOUT
# -----------------------------

col1, col2 = st.columns(2)

with col1:

    st.subheader("📈 Latest Market Data")

    st.dataframe(
        latest_df[
            ['symbol', 'price', 'price_change_percent']
        ]
    )

with col2:

    st.subheader("🚀 Top Movers")

    st.dataframe(
        movers_df[
            ['symbol', 'price_change_percent']
        ]
    )

# -----------------------------
# PRICE VISUALIZATION
# -----------------------------

st.subheader("📉 Price Trend Visualization")

chart_df = latest_df.head(20)

st.line_chart(chart_df['price'])

# -----------------------------
# METRICS
# -----------------------------

st.subheader("📌 Platform Metrics")

metric1, metric2, metric3 = st.columns(3)

metric1.metric(
    "Total Records",
    len(latest_df)
)

metric2.metric(
    "Highest Price",
    round(
        latest_df['price'].max(),
        2
    )
)

metric3.metric(
    "Average Change %",
    round(
        latest_df['price_change_percent'].mean(),
        2
    )
)