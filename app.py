import streamlit as st
import pandas as pd

from charts import *
from filters import *

st.set_page_config(
    page_title="Global Alcohol Dashboard",
    layout="wide"
)

df = pd.read_csv("drinks.csv")

st.markdown("""
<style>

.stApp{
    background-color:#0F172A;
    color:white;
}

.main-title{
    color:#22c55e;
    font-size:60px;
    font-weight:800;
    text-shadow:
        0px 0px 10px #22c55e,
        0px 0px 20px #22c55e;
}

.kpi-box{
    background:linear-gradient(
        135deg,
        #1E293B,
        #334155
    );

    padding:25px;

    border-radius:18px;

    text-align:center;

    border:1px solid #475569;

    box-shadow:0px 0px 12px rgba(0,0,0,0.3);
}

.kpi-title{
    color:#CBD5E1;
    font-size:18px;
    margin-bottom:10px;
}

.kpi-value{
    color:white;
    font-size:38px;
    font-weight:bold;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<h1 class="main-title">
🌍 Global Alcohol Consumption Dashboard
</h1>
""", unsafe_allow_html=True)

st.write("Professional Data Analytics Dashboard")

df = sidebar_filters(df)

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.markdown(f"""
    <div class="kpi-box">
        <div class="kpi-title">
            Total Records
        </div>

        <div class="kpi-value">
            {len(df)}
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:

    st.markdown(f"""
    <div class="kpi-box">
        <div class="kpi-title">
            Total Countries
        </div>

        <div class="kpi-value">
            {df['country'].nunique()}
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:

    st.markdown(f"""
    <div class="kpi-box">
        <div class="kpi-title">
            Avg Beer
        </div>

        <div class="kpi-value">
            {round(df['beer_servings'].mean(),2)}
        </div>
    </div>
    """, unsafe_allow_html=True)

with col4:

    st.markdown(f"""
    <div class="kpi-box">
        <div class="kpi-title">
            Avg Wine
        </div>

        <div class="kpi-value">
            {round(df['wine_servings'].mean(),2)}
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

st.subheader("Dataset Preview")

st.dataframe(
    df,
    use_container_width=True
)

st.markdown("---")

col5, col6 = st.columns(2)

with col5:

    st.subheader("Bar Chart")

    bar_chart(df)

with col6:

    st.subheader("Pie Chart")

    pie_chart(df)

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

