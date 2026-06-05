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

h1,h2,h3,h4,h5,h6{
    color:#38BDF8 !important;
}

.kpi-box{
    background:linear-gradient(135deg,#1E293B,#334155);
    padding:25px;
    border-radius:18px;
    text-align:center;
    box-shadow:0px 0px 12px rgba(0,0,0,0.4);
    border:1px solid #334155;
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

</style>
""", unsafe_allow_html=True)

st.sidebar.markdown("""
<h1 style='text-align:center; color:#38BDF8;'>
🌍 Global Alcohol Consumption Dashboard
</h1>
<p style='text-align:center; color:white;'>
Professional Data Analytics Dashboard
</p>
""", unsafe_allow_html=True)

st.title("🌍 Global Alcohol Consumption Dashboard")
st.write("Professional Data Analytics Dashboard")

countries = st.sidebar.multiselect(
    "Select Country",
    df["country"].unique(),
    default=df["country"].unique()[:5]
)

charts = st.sidebar.multiselect(
    "Select Additional Charts",
    ["Heatmap","Scatter Plot","Violin Plot"]
)

if countries:
    df = df[df["country"].isin(countries)]

col1,col2,col3,col4 = st.columns(4)

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
st.dataframe(df)

st.markdown("---")

col1,col2 = st.columns(2)

with col1:

    fig, ax = plt.subplots(figsize=(7,5))

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

    ax.set_title("Top Beer Consuming Countries")
    ax.set_xlabel("Beer Servings")
    ax.set_ylabel("Country")

    st.pyplot(fig)

with col2:

    fig2, ax2 = plt.subplots(figsize=(7,5))

    sns.scatterplot(
        x="beer_servings",
        y="wine_servings",
        data=df,
        color="#38BDF8",
        s=100,
        ax=ax2
    )

    ax2.set_title("Beer vs Wine Consumption")

    st.pyplot(fig2)

if "Heatmap" in charts:

    st.subheader("Correlation Heatmap")

    fig3, ax3 = plt.subplots(figsize=(8,5))

    sns.heatmap(
        df.select_dtypes(include="number").corr(),
        annot=True,
        cmap="Blues",
        ax=ax3
    )

    st.pyplot(fig3)

if "Violin Plot" in charts:

    st.subheader("Violin Plot")

    fig4, ax4 = plt.subplots(figsize=(8,5))

    sns.violinplot(
        y=df["beer_servings"],
        color="#2563EB",
        ax=ax4
    )

    st.pyplot(fig4)

if "Scatter Plot" in charts:

    st.subheader("Scatter Plot")

    fig5, ax5 = plt.subplots(figsize=(8,5))

    sns.scatterplot(
        x="spirit_servings",
        y="total_litres_of_pure_alcohol",
        data=df,
        color="#38BDF8",
        s=100,
        ax=ax5
    )

    st.pyplot(fig5)