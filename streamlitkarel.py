# python -m venv .venv --> bikin environment
# .venv\Scripts\activate --> aktivasi environment di Windows
# pip install streamlit --> install streamlit
# jika install langsung dari requirements.txt --> pip install -r requirements.txt
# streamlit run namafile.py --> running

import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st


# Tampilan Page Tab Browser

st.set_page_config(
    page_title="Simple Dashboard", layout="wide")


# Load Source File

url = "https://raw.githubusercontent.com/karelwidjaja1983/dashboard_realestate/refs/heads/main/Real_Estate_Sales_2001-2022_GL.csv"
df = pd.read_csv(url)

# Rename Field
df = df.rename(columns={
    "Date Recorded": "date_recorded",
    "Town": "town",
    "Address": "address",
    "Assessed Value": "assessed_value",
    "Sale Amount": "sale_amount",
    "Property Type": "property_type",
    "Residential Type": "residential_type"
})


# Field untuk filter dan grafik

df["date_recorded"] = pd.to_datetime(df["date_recorded"], errors="coerce")
df["sales_ratio"] = df["assessed_value"] / df["sale_amount"]
df["year"] = df["date_recorded"].dt.year
df["month"] = df["date_recorded"].dt.to_period("M").dt.to_timestamp()


# Sidebar Menu & Filter

st.sidebar.title("Filter")

year = st.sidebar.multiselect(
    "Year",
    sorted(df["year"].dropna().unique()),
    default=sorted(df["year"].dropna().unique())
)

town = st.sidebar.multiselect(
    "Town",
    sorted(df["town"].dropna().unique()),
    default=sorted(df["town"].dropna().unique())
)

property_type = st.sidebar.multiselect(
    "Property Type",
    sorted(df["property_type"].dropna().unique()),
    default=sorted(df["property_type"].dropna().unique())
)

# Filter

filtered = df[
    (df["year"].isin(year)) &
    (df["town"].isin(town)) &
    (df["property_type"].isin(property_type))
]



# Judul Page

st.title("Dashboard real estate")


# Pehitungan Score Card

total_tx = len(filtered)
total_sales = filtered["sale_amount"].sum()
avg_price = filtered["sale_amount"].mean()
avg_ratio = filtered["sales_ratio"].mean()

# Jika data tidak ada maka menjadi 0

total_sales = 0 if pd.isna(total_sales) else int(total_sales)
avg_price = 0 if pd.isna(avg_price) else int(avg_price)
avg_ratio = 0 if pd.isna(avg_ratio) else round(avg_ratio, 2)

# Menampilkan Score Card

c1, c2, c3, c4 = st.columns(4)
c1.metric("Transactions", total_tx)
c2.metric("Total Sales", total_sales)
c3.metric("Average Price", avg_price)
c4.metric("Avg Ratio", avg_ratio)


# Membuat Tab Menu

tab1, tab2 = st.tabs(["Grafik - 1", "Grafik - 2"])


# Tab 1

with tab1:

    st.subheader("Grafik - 1")

    if filtered.empty:
        st.warning("Data kosong setelah filter")
    else:

        col1, col2 = st.columns(2)

        # Scatter Plot
        with col1:
            fig1 = px.scatter(
                filtered,
                x="assessed_value",
                y="sale_amount",
                title="Assessed vs Sale"
            )
            st.plotly_chart(fig1, use_container_width=True)

        # Box Plot
        with col2:
            fig2 = px.box(
                filtered,
                y="sale_amount",
                title="Distribution"
            )
            st.plotly_chart(fig2, use_container_width=True)

        # Histogram
        fig3 = px.histogram(
            filtered,
            x="sale_amount",
            nbins=30,
            title="Histogram"
        )
        st.plotly_chart(fig3, use_container_width=True)


# Tab 2

with tab2:

    st.subheader("Grafik - 2")

    if filtered.empty:
        st.warning("Data kosong setelah filter")
    else:

        # Heatmap
        num_df = filtered.select_dtypes(include=np.number)

        if not num_df.empty:
            corr = num_df.corr()

            fig4 = px.imshow(
                corr,
                text_auto=True,
                title="Correlation Heatmap"
            )
            st.plotly_chart(fig4, use_container_width=True)

        # Trend
        if "month" in filtered.columns:
            trend = filtered.groupby("month").size().reset_index(name="count")

            fig5 = px.line(
                trend,
                x="month",
                y="count",
                title="Transaction Trend"
            )
            st.plotly_chart(fig5, use_container_width=True)
