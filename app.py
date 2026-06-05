import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="Global Alcohol Dashboard",
    layout="wide"
)

df = pd.read_csv("drinks.csv")

st.markdown("""
<style>

.stApp{
    background-color:#081028;
    color:white;
}

section[data-testid="stSidebar"]{
    background-color:#081028;
}

.main-title{
    color:#38BDF8;
    font-size:58px;
    font-weight:800;
    text-shadow:
        0px 0px 8px rgba(56,189,248,0.8),
        0px 0px 18px rgba(56,189,248,0.6);
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

    border:1px solid #334155;

    box-shadow:0px 0px 12px rgba(0,0,0,0.4);
}

.kpi-title{
    color:#CBD5E1;
    font-size:18px;
    margin-bottom:10px;
    font-weight:bold;
}

.kpi-value{
    color:white;
    font-size:38px;
    font-weight:bold;
}

.sidebar-title{
    color:#38BDF8;
    font-size:32px;
    font-weight:800;
    text-align:center;

    text-shadow:
        0px 0px 8px rgba(56,189,248,0.8),
        0px 0px 18px rgba(56,189,248,0.6);
}

.sidebar-subtitle{
    color:white;
    text-align:center;
    font-size:15px;
}

label{
    color:#38BDF8 !important;
    font-weight:bold !important;
}

div[data-baseweb="tag"]{
    background-color:#2563EB !important;
}

div[data-baseweb="tag"] span{
    color:white !important;
}

.stMultiSelect div[data-baseweb="select"] > div{
    background-color:#0F172A !important;
    border:1px solid #2563EB !important;
}

.chart-box{
    background:#111827;
    padding:20px;
    border-radius:16px;
    margin-bottom:20px;
    box-shadow:0px 0px 10px rgba(0,0,0,0.3);
}

</style>
""", unsafe_allow_html=True)

st.sidebar.markdown("""
<div class="sidebar-title">
🌍 Global Alcohol Consumption Dashboard
</div>

<div class="sidebar-subtitle">
Professional Data Analytics Dashboard
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("---")

countries = st.sidebar.multiselect(
    "Select Country",
    options=sorted(df["country"].unique()),
    default=sorted(df["country"].unique()[:10])
)

chart_options = st.sidebar.multiselect(
    "Select Additional Charts",
    [
        "Histogram",
        "Pie Chart",
        "Scatter Plot",
        "Box Plot",
        "Heatmap",
        "Area Chart",
        "Count Plot",
        "Violin Plot",
        "Line Chart"
    ]
)

if countries:
    df = df[df["country"].isin(countries)]

st.markdown("""
<h1 class="main-title">
🌍 Global Alcohol Consumption Dashboard
</h1>
""", unsafe_allow_html=True)

st.write("Professional Data Analytics Dashboard")

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.markdown(f"""
    <div class="kpi-box">
        <div class="kpi-title">Total Records</div>
        <div class="kpi-value">{len(df)}</div>
    </div>
    """, unsafe_allow_html=True)

with col2:

    st.markdown(f"""
    <div class="kpi-box">
        <div class="kpi-title">Total Countries</div>
        <div class="kpi-value">{df['country'].nunique()}</div>
    </div>
    """, unsafe_allow_html=True)

with col3:

    st.markdown(f"""
    <div class="kpi-box">
        <div class="kpi-title">Avg Beer</div>
        <div class="kpi-value">{round(df['beer_servings'].mean(),2)}</div>
    </div>
    """, unsafe_allow_html=True)

with col4:

    st.markdown(f"""
    <div class="kpi-box">
        <div class="kpi-title">Avg Wine</div>
        <div class="kpi-value">{round(df['wine_servings'].mean(),2)}</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

st.subheader("Dataset Preview")

st.dataframe(df, use_container_width=True)

st.markdown("---")

col5, col6 = st.columns(2)

with col5:

    st.markdown('<div class="chart-box">', unsafe_allow_html=True)

    st.subheader("Bar Chart")

    fig, ax = plt.subplots(figsize=(8,5))

    top_beer = df.sort_values(
        by="beer_servings",
        ascending=False
    ).head(10)

    sns.barplot(
        x="beer_servings",
        y="country",
        data=top_beer,
        palette="Blues_r",
        ax=ax
    )

    st.pyplot(fig)

    st.markdown('</div>', unsafe_allow_html=True)

with col6:

    st.markdown('<div class="chart-box">', unsafe_allow_html=True)

    st.subheader("Scatter Plot")

    fig2, ax2 = plt.subplots(figsize=(8,5))

    sns.scatterplot(
        x="beer_servings",
        y="wine_servings",
        data=df,
        color="#38BDF8",
        s=100,
        ax=ax2
    )

    st.pyplot(fig2)

    st.markdown('</div>', unsafe_allow_html=True)

if "Histogram" in chart_options:

    st.subheader("Histogram")

    fig3, ax3 = plt.subplots(figsize=(8,5))

    ax3.hist(
        df["beer_servings"],
        bins=20,
        color="#2563EB"
    )

    st.pyplot(fig3)

if "Pie Chart" in chart_options:

    st.subheader("Pie Chart")

    fig4, ax4 = plt.subplots(figsize=(8,8))

    df.groupby("continent")["beer_servings"].sum().plot(
        kind="pie",
        autopct="%1.1f%%",
        ax=ax4
    )

    st.pyplot(fig4)

if "Box Plot" in chart_options:

    st.subheader("Box Plot")

    fig5, ax5 = plt.subplots(figsize=(8,5))

    sns.boxplot(
        y=df["beer_servings"],
        color="#38BDF8",
        ax=ax5
    )

    st.pyplot(fig5)

if "Heatmap" in chart_options:

    st.subheader("Heatmap")

    fig6, ax6 = plt.subplots(figsize=(10,6))

    sns.heatmap(
        df.select_dtypes(include="number").corr(),
        annot=True,
        cmap="Blues",
        ax=ax6
    )

    st.pyplot(fig6)

if "Area Chart" in chart_options:

    st.subheader("Area Chart")

    st.area_chart(
        df[
            [
                "beer_servings",
                "wine_servings"
            ]
        ].head(20)
    )

if "Count Plot" in chart_options:

    st.subheader("Count Plot")

    fig7, ax7 = plt.subplots(figsize=(8,5))

    sns.countplot(
        y="country",
        data=df.head(10),
        palette="Blues_r",
        ax=ax7
    )

    st.pyplot(fig7)

if "Violin Plot" in chart_options:

    st.subheader("Violin Plot")

    fig8, ax8 = plt.subplots(figsize=(8,5))

    sns.violinplot(
        y=df["beer_servings"],
        color="#2563EB",
        ax=ax8
    )

    st.pyplot(fig8)

if "Line Chart" in chart_options:

    st.subheader("Line Chart")

    fig9, ax9 = plt.subplots(figsize=(10,5))

    df["beer_servings"].head(20).plot(
        ax=ax9,
        color="#38BDF8"
    )

    st.pyplot(fig9)

