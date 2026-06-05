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

""", unsafe_allow_html=True)

st.markdown("""

st.markdown("""

df = sidebar_filters(df)

col1,col2,col3,col4 = st.columns(4)

with col1:
st.markdown(f"""

Total Records
{len(df)}

""", unsafe_allow_html=True)

with col2:
st.markdown(f"""

Total Countries
{df['country'].nunique()}

""", unsafe_allow_html=True)

with col3:
st.markdown(f"""

Avg Beer
{round(df['beer_servings'].mean(),2)}

""", unsafe_allow_html=True)

with col4:
st.markdown(f"""

Avg Wine
{round(df['wine_servings'].mean(),2)}

""", unsafe_allow_html=True)

st.markdown("", unsafe_allow_html=True)

st.subheader("Dataset Preview")

st.dataframe(
df,
use_container_width=True
)

st.markdown("", unsafe_allow_html=True)

col5,col6 = st.columns(2)

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