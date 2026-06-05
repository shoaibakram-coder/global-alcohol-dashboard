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
        #0F172A 0%,
        #132238 40%,
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

/* KPI CARD */

.kpi-card {

    background: rgba(15,23,42,0.80);

    padding: 25px;

    border-radius: 18px;

    border: 1px solid rgba(255,255,255,0.08);

    box-shadow:
        0px 0px 18px rgba(16,185,129,0.15);

    text-align: center;
}

/* KPI TITLE */

.kpi-card h4 {

    color: #CBD5E1;

    font-size: 18px;

    margin-bottom: 12px;
}

/* KPI VALUE */

.kpi-card h1 {

    color: white;

    font-size: 42px;

    margin: 0;
}

/* CHART BOX */

.chart-box {

    background: rgba(255,255,255,0.96);

    padding: 22px;

    border-radius: 20px;

    box-shadow:
        0px 4px 18px rgba(0,0,0,0.25);

    margin-bottom: 25px;
}

/* TITLES */

.main-title {

    font-size: 60px;

    font-weight: 800;

    color: white;

    text-shadow:
        0px 0px 12px rgba(16,185,129,0.35);
}

.sub-title {

    font-size: 22px;

    color: #D1D5DB;

    margin-bottom: 30px;
}

</style>

""", unsafe_allow_html=True)

# TITLE

st.markdown("""

<div class="main-title">
🌍 Global Alcohol Consumption Dashboard
</div>
""", unsafe_allow_html=True)

# SUBTITLE

st.markdown("""

<div class="sub-title">
Professional Data Analytics Dashboard
</div>
""", unsafe_allow_html=True)

# SIDEBAR FILTERS

df = sidebar_filters(df)

# KPI SECTION

col1, col2, col3, col4 = st.columns(4)

with col1:

```
st.markdown(f"""
<div class="kpi-card">
    <h4>Total Records</h4>
    <h1>{len(df)}</h1>
</div>
""", unsafe_allow_html=True)
```

with col2:

```
st.markdown(f"""
<div class="kpi-card">
    <h4>Total Countries</h4>
    <h1>{df['country'].nunique()}</h1>
</div>
""", unsafe_allow_html=True)
```

with col3:

```
st.markdown(f"""
<div class="kpi-card">
    <h4>Avg Beer</h4>
    <h1>{round(df['beer_servings'].mean(),2)}</h1>
</div>
""", unsafe_allow_html=True)
```

with col4:

```
st.markdown(f"""
<div class="kpi-card">
    <h4>Avg Wine</h4>
    <h1>{round(df['wine_servings'].mean(),2)}</h1>
</div>
""", unsafe_allow_html=True)
```

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

```
st.markdown('<div class="chart-box">', unsafe_allow_html=True)

st.subheader("Bar Chart")

bar_chart(df)

st.markdown('</div>', unsafe_allow_html=True)
```

with col6:

```
st.markdown('<div class="chart-box">', unsafe_allow_html=True)

st.subheader("Pie Chart")

pie_chart(df)

st.markdown('</div>', unsafe_allow_html=True)
```

# EXTRA CHARTS

chart_options = st.session_state.get(
"chart_options",
[]
)

if "Histogram" in chart_options:

```
st.markdown('<div class="chart-box">', unsafe_allow_html=True)

st.subheader("Histogram")

histogram(df)

st.markdown('</div>', unsafe_allow_html=True)
```

if "Scatter Plot" in chart_options:

```
st.markdown('<div class="chart-box">', unsafe_allow_html=True)

st.subheader("Scatter Plot")

scatter_plot(df)

st.markdown('</div>', unsafe_allow_html=True)
```

if "Box Plot" in chart_options:

```
st.markdown('<div class="chart-box">', unsafe_allow_html=True)

st.subheader("Box Plot")

box_plot(df)

st.markdown('</div>', unsafe_allow_html=True)
```

if "Heatmap" in chart_options:

```
st.markdown('<div class="chart-box">', unsafe_allow_html=True)

st.subheader("Heatmap")

heatmap(df)

st.markdown('</div>', unsafe_allow_html=True)
```

if "Area Chart" in chart_options:

```
st.markdown('<div class="chart-box">', unsafe_allow_html=True)

st.subheader("Area Chart")

area_chart(df)

st.markdown('</div>', unsafe_allow_html=True)
```

if "Count Plot" in chart_options:

```
st.markdown('<div class="chart-box">', unsafe_allow_html=True)

st.subheader("Count Plot")

count_plot(df)

st.markdown('</div>', unsafe_allow_html=True)
```

if "Violin Plot" in chart_options:

```
st.markdown('<div class="chart-box">', unsafe_allow_html=True)

st.subheader("Violin Plot")

violin_plot(df)

st.markdown('</div>', unsafe_allow_html=True)
```
