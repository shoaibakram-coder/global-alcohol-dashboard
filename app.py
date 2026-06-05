import streamlit as st
import pandas as pd

from charts import *
from filters import *

st.set_page_config(
page_title="Global Alcohol Dashboard",
layout="wide"
)

LOAD DATA

df = pd.read_csv("drinks.csv")

CUSTOM CSS

st.markdown("""

""", unsafe_allow_html=True)

TITLE

st.markdown(
"""

🌍 Global Alcohol Consumption Dashboard

""",
unsafe_allow_html=True
)

SUBTITLE

st.markdown(
"""

Professional Data Analytics Dashboard

""",
unsafe_allow_html=True
)

FILTERS

df = sidebar_filters(df)

KPI SECTION

col1, col2, col3, col4 = st.columns(4)

with col1:

st.markdown(
    f"""
    <div class="kpi-card">
        <h4>Total Records</h4>
        <h1>{len(df)}</h1>
    </div>
    """,
    unsafe_allow_html=True
)

with col2:

st.markdown(
    f"""
    <div class="kpi-card">
        <h4>Total Countries</h4>
        <h1>{df['country'].nunique()}</h1>
    </div>
    """,
    unsafe_allow_html=True
)

with col3:

st.markdown(
    f"""
    <div class="kpi-card">
        <h4>Avg Beer</h4>
        <h1>{round(df['beer_servings'].mean(),2)}</h1>
    </div>
    """,
    unsafe_allow_html=True
)

with col4:

st.markdown(
    f"""
    <div class="kpi-card">
        <h4>Avg Wine</h4>
        <h1>{round(df['wine_servings'].mean(),2)}</h1>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("", unsafe_allow_html=True)

DATASET

st.subheader("Dataset Preview")

st.dataframe(
df,
use_container_width=True
)

st.markdown("", unsafe_allow_html=True)

CHARTS

col5, col6 = st.columns(2)

with col5:

st.markdown(
    '<div class="chart-box">',
    unsafe_allow_html=True
)

st.subheader("Bar Chart")

bar_chart(df)

st.markdown(
    '</div>',
    unsafe_allow_html=True
)

with col6:

st.markdown(
    '<div class="chart-box">',
    unsafe_allow_html=True
)

st.subheader("Pie Chart")

pie_chart(df)

st.markdown(
    '</div>',
    unsafe_allow_html=True
)
EXTRA CHARTS

chart_options = st.session_state.get(
"chart_options",
[]
)

if "Histogram" in chart_options:

st.markdown(
    '<div class="chart-box">',
    unsafe_allow_html=True
)

st.subheader("Histogram")

histogram(df)

st.markdown(
    '</div>',
    unsafe_allow_html=True
)

if "Scatter Plot" in chart_options:

st.markdown(
    '<div class="chart-box">',
    unsafe_allow_html=True
)

st.subheader("Scatter Plot")

scatter_plot(df)

st.markdown(
    '</div>',
    unsafe_allow_html=True
)

if "Box Plot" in chart_options:

st.markdown(
    '<div class="chart-box">',
    unsafe_allow_html=True
)

st.subheader("Box Plot")

box_plot(df)

st.markdown(
    '</div>',
    unsafe_allow_html=True
)

if "Heatmap" in chart_options:

st.markdown(
    '<div class="chart-box">',
    unsafe_allow_html=True
)

st.subheader("Heatmap")

heatmap(df)

st.markdown(
    '</div>',
    unsafe_allow_html=True
)

if "Area Chart" in chart_options:

st.markdown(
    '<div class="chart-box">',
    unsafe_allow_html=True
)

st.subheader("Area Chart")

area_chart(df)

st.markdown(
    '</div>',
    unsafe_allow_html=True
)

if "Count Plot" in chart_options:

st.markdown(
    '<div class="chart-box">',
    unsafe_allow_html=True
)

st.subheader("Count Plot")

count_plot(df)

st.markdown(
    '</div>',
    unsafe_allow_html=True
)

if "Violin Plot" in chart_options:

st.markdown(
    '<div class="chart-box">',
    unsafe_allow_html=True
)

st.subheader("Violin Plot")

violin_plot(df)

st.markdown(
    '</div>',
    unsafe_allow_html=True
)