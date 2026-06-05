import streamlit as st
import pandas as pd

from charts import *
from filters import *

# PAGE CONFIG

st.set_page_config(
    page_title="Alcohol Dashboard",
    layout="wide"
)

# CUSTOM THEME

st.markdown("""
<style>

/* MAIN BACKGROUND */

.stApp {
    background-color: #0E1117;
}

/* SIDEBAR */

section[data-testid="stSidebar"] {
    background-color: #161B22;
}

/* KPI CARDS */

div[data-testid="metric-container"] {

    background: linear-gradient(135deg, #00C853, #009624);

    padding: 22px;

    border-radius: 24px;

    border: 4px solid #00E676;

    box-shadow: 0px 0px 20px rgba(0,255,100,0.5);

}

/* KPI LABEL */

div[data-testid="metric-container"] label {

    color: white !important;

    font-size: 24px !important;

    font-weight: bold !important;

}

/* KPI VALUE */

div[data-testid="metric-container"] [data-testid="stMetricValue"] {

    color: white !important;

    font-size: 42px !important;

    font-weight: bold !important;

}

/* SUBHEADINGS */

h2, h3 {

    color: white !important;

}

/* DATAFRAME */

[data-testid="stDataFrame"] {

    border-radius: 15px;

    overflow: hidden;

}

</style>
""", unsafe_allow_html=True)

# LOAD DATA

df = pd.read_csv("drinks.csv")
# TITLE

st.markdown("""
<h1 style='
font-size:60px;
color:#39FF14;
font-weight:bold;
text-shadow: 0px 0px 2px #39FF14;
'>
🌍 Global Alcohol Consumption Dashboard
</h1>
""", unsafe_allow_html=True)

# SUBTITLE

st.markdown("""
<p style='
font-size:25px;
color:#A0AEC0;
'>
Professional Data Visualization Dashboard
</p>
""", unsafe_allow_html=True)

# FILTERS

df = sidebar_filters(df)

# KPI CARDS

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Records",
    len(df)
)

col2.metric(
    "Avg Beer",
    round(df["beer_servings"].mean(),2)
)

col3.metric(
    "Avg Spirit",
    round(df["spirit_servings"].mean(),2)
)

col4.metric(
    "Avg Wine",
    round(df["wine_servings"].mean(),2)
)

st.markdown("---")

# DATASET TABLE

st.subheader("Dataset")

st.dataframe(
    df,
    use_container_width=True
)

st.markdown("---")

# BAR + PIE CHART

col5, col6 = st.columns(2)

with col5:

    st.subheader("Bar Chart")

    bar_chart(df)

with col6:

    st.subheader("Pie Chart")

    pie_chart(df)

st.markdown("---")

# SCATTER + LINE CHART

col7, col8 = st.columns(2)

with col7:

    st.subheader("Scatter Plot")

    scatter_plot(df)

with col8:

    st.subheader("Line Chart")

    line_chart(df)

st.markdown("---")

# MULTI CHART SELECTOR

chart_options = st.sidebar.multiselect(
    "Select Additional Charts",
    [
        "All Charts",
        "Histogram",
        "Box Plot",
        "Heatmap",
        "Area Chart",
        "Count Plot",
        "Violin Plot"
    ]
)

# SHOW ALL CHARTS

if "All Charts" in chart_options:

    chart_options = [
        "Histogram",
        "Box Plot",
        "Heatmap",
        "Area Chart",
        "Count Plot",
        "Violin Plot"
    ]

# DISPLAY CHARTS

for chart in chart_options:

    st.markdown("---")

    if chart == "Histogram":

        st.subheader("Histogram")

        histogram(df)

    elif chart == "Box Plot":

        st.subheader("Box Plot")

        box_plot(df)

    elif chart == "Heatmap":

        st.subheader("Heatmap")

        heatmap(df)

    elif chart == "Area Chart":

        st.subheader("Area Chart")

        area_chart(df)

    elif chart == "Count Plot":

        st.subheader("Count Plot")

        count_plot(df)

    elif chart == "Violin Plot":

        st.subheader("Violin Plot")

        violin_plot(df)