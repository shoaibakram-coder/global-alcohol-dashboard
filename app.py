```python
import streamlit as st
import pandas as pd

from charts import *
from filters import *

# PAGE CONFIG

st.set_page_config(
    page_title="Global Alcohol Dashboard",
    layout="wide"
)

# LOAD DATA

df = pd.read_csv("drinks.csv")

# CUSTOM CSS

st.markdown("""
<style>

/* MAIN APP */

.stApp {

    background: linear-gradient(
        135deg,
        #132238 0%,
        #1B2A41 45%,
        #0F766E 100%
    );

    color: white;
}

/* MAIN CONTAINER */

.main .block-container {

    padding-top: 2rem;
    padding-left: 3rem;
    padding-right: 3rem;
}

/* KPI CARDS */

.kpi-card {

    background: rgba(15,23,42,0.75);

    padding: 24px;

    border-radius: 18px;

    border: 1px solid rgba(255,255,255,0.08);

    box-shadow: 0px 4px 20px rgba(0,0,0,0.35);

    text-align: center;
}

/* KPI TITLE */

.kpi-card h4 {

    color: #CBD5E1;

    margin-bottom: 10px;
}

/* KPI VALUE */

.kpi-card h1 {

    color: white;

    font-size: 42px;
}

/* CHART BOX */

.chart-box {

    background: white;

    padding: 20px;

    border-radius: 18px;

    box-shadow: 0px 4px 18px rgba(0,0,0,0.25);

    margin-bottom: 25px;
}

/* HEADINGS */

h1, h2, h3 {

    color: white !important;
}

</style>
""", unsafe_allow_html=True)

# TITLE

st.markdown("""
<h1 style="
font-size:58px;
font-weight:800;
color:white;
">
🌍 Global Alcohol Consumption Dashboard
</h1>
""", unsafe_allow_html=True)

# SUBTITLE

st.markdown("""
<p style="
font-size:22px;
color:#D1D5DB;
margin-bottom:30px;
">
Professional Data Analytics Dashboard
</p>
""", unsafe_allow_html=True)

# FILTERS

df = sidebar_filters(df)

# KPI SECTION

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.markdown(f"""
    <div class="kpi-card">
        <h4>Total Records</h4>
        <h1>{len(df)}</h1>
    </div>
    """, unsafe_allow_html=True)

with col2:

    st.markdown(f"""
    <div class="kpi-card">
        <h4>Total Countries</h4>
        <h1>{df['country'].nunique()}</h1>
    </div>
    """, unsafe_allow_html=True)

with col3:

    st.markdown(f"""
    <div class="kpi-card">
        <h4>Avg Beer</h4>
        <h1>{round(df['beer_servings'].mean(),2)}</h1>
    </div>
    """, unsafe_allow_html=True)

with col4:

    st.markdown(f"""
    <div class="kpi-card">
        <h4>Avg Wine</h4>
        <h1>{round(df['wine_servings'].mean(),2)}</h1>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# DATASET

st.subheader("Dataset Preview")

st.dataframe(
    df,
    use_container_width=True
)

st.markdown("<br>", unsafe_allow_html=True)

# CHARTS

col5, col6 = st.columns(2)

with col5:

    st.markdown('<div class="chart-box">', unsafe_allow_html=True)

    st.subheader("Bar Chart")

    bar_chart(df)

    st.markdown('</div>', unsafe_allow_html=True)

with col6:

    st.markdown('<div class="chart-box">', unsafe_allow_html=True)

    st.subheader("Pie Chart")

    pie_chart(df)

    st.markdown('</div>', unsafe_allow_html=True)

# EXTRA CHARTS

chart_options = st.session_state.get(
    "chart_options",
    []
)

if "Histogram" in chart_options:

    st.markdown('<div class="chart-box">', unsafe_allow_html=True)

    st.subheader("Histogram")

    histogram(df)

    st.markdown('</div>', unsafe_allow_html=True)

if "Scatter Plot" in chart_options:

    st.markdown('<div class="chart-box">', unsafe_allow_html=True)

    st.subheader("Scatter Plot")

    scatter_plot(df)

    st.markdown('</div>', unsafe_allow_html=True)

if "Box Plot" in chart_options:

    st.markdown('<div class="chart-box">', unsafe_allow_html=True)

    st.subheader("Box Plot")

    box_plot(df)

    st.markdown('</div>', unsafe_allow_html=True)

if "Heatmap" in chart_options:

    st.markdown('<div class="chart-box">', unsafe_allow_html=True)

    st.subheader("Heatmap")

    heatmap(df)

    st.markdown('</div>', unsafe_allow_html=True)

if "Area Chart" in chart_options:

    st.markdown('<div class="chart-box">', unsafe_allow_html=True)

    st.subheader("Area Chart")

    area_chart(df)

    st.markdown('</div>', unsafe_allow_html=True)

if "Count Plot" in chart_options:

    st.markdown('<div class="chart-box">', unsafe_allow_html=True)

    st.subheader("Count Plot")

    count_plot(df)

    st.markdown('</div>', unsafe_allow_html=True)

if "Violin Plot" in chart_options:

    st.markdown('<div class="chart-box">', unsafe_allow_html=True)

    st.subheader("Violin Plot")

    violin_plot(df)

    st.markdown('</div>', unsafe_allow_html=True)
```
