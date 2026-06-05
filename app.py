import streamlit as st
import pandas as pd

from charts import *
from filters import *

st.set_page_config(
    page_title="Global Alcohol Dashboard",
    layout="wide"
)

df = pd.read_csv("drinks.csv")

st.title("🌍 Global Alcohol Consumption Dashboard")

st.write("Professional Data Analytics Dashboard")

df = sidebar_filters(df)

col1,col2,col3,col4 = st.columns(4)

col1.metric(
    "Total Records",
    len(df)
)

col2.metric(
    "Total Countries",
    df["country"].nunique()
)

col3.metric(
    "Avg Beer",
    round(df["beer_servings"].mean(),2)
)

col4.metric(
    "Avg Wine",
    round(df["wine_servings"].mean(),2)
)

st.markdown("---")

st.subheader("Dataset Preview")

st.dataframe(
    df,
    use_container_width=True
)

st.markdown("---")

col5,col6 = st.columns(2)

with col5:

    st.subheader("Bar Chart")

    bar_chart(df)

with col6:

    st.subheader("Pie Chart")

    pie_chart(df)

st.markdown("---")

chart_options = st.session_state.get(
    "chart_options",
    []
)

if "Histogram" in chart_options:

    st.subheader("Histogram")

    histogram(df)

if "Scatter Plot" in chart_options:

    st.subheader("Scatter Plot")

    scatter_plot(df)

if "Box Plot" in chart_options:

    st.subheader("Box Plot")

    box_plot(df)

if "Heatmap" in chart_options:

    st.subheader("Heatmap")

    heatmap(df)

if "Area Chart" in chart_options:

    st.subheader("Area Chart")

    area_chart(df)

if "Count Plot" in chart_options:

    st.subheader("Count Plot")

    count_plot(df)

if "Violin Plot" in chart_options:

    st.subheader("Violin Plot")

    violin_plot(df)

