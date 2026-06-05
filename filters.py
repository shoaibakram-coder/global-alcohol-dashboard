import streamlit as st

def sidebar_filters(df):

st.sidebar.markdown("""
<style>

section[data-testid="stSidebar"] {

    background: linear-gradient(
        180deg,
        #064E3B 0%,
        #065F46 45%,
        #0F172A 100%
    );

    border-right: 2px solid #10B981;
}

.sidebar-title {

    color: white;

    font-size: 34px;

    font-weight: 800;

    text-align: center;

    line-height: 1.2;

    text-shadow:
        0px 0px 8px rgba(16,185,129,0.7),
        0px 0px 18px rgba(16,185,129,0.5);

    margin-bottom: 10px;
}

.sidebar-subtitle {

    color: #D1FAE5;

    text-align: center;

    font-size: 15px;

    margin-bottom: 25px;
}

label {

    color: white !important;

    font-weight: 600 !important;
}

div[data-baseweb="select"] {

    background-color: #0F172A !important;

    border-radius: 12px !important;
}

.stTextInput input {

    background-color: #0F172A !important;

    color: white !important;

    border-radius: 12px !important;
}

</style>
""", unsafe_allow_html=True)

# SIDEBAR TITLE

st.sidebar.markdown("""
<div class="sidebar-title">
    🌍 Global Alcohol <br>
    Dashboard
</div>

<div class="sidebar-subtitle">
    Professional Analytics
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("---")

# COUNTRY FILTER

country = st.sidebar.multiselect(
    "Select Country",
    df["country"].unique(),
    default=df["country"].unique()
)

# BEER RANGE

beer_range = st.sidebar.slider(
    "Beer Servings",
    int(df["beer_servings"].min()),
    int(df["beer_servings"].max()),
    (
        int(df["beer_servings"].min()),
        int(df["beer_servings"].max())
    )
)

# SEARCH

search = st.sidebar.text_input(
    "Search Country"
)

# EXTRA CHARTS

chart_options = st.sidebar.multiselect(
    "Select Additional Charts",
    [
        "Histogram",
        "Scatter Plot",
        "Box Plot",
        "Heatmap",
        "Area Chart",
        "Count Plot",
        "Violin Plot"
    ]
)

st.session_state["chart_options"] = chart_options

# FILTER DATA

filtered_df = df[
    (df["country"].isin(country))
    &
    (df["beer_servings"] >= beer_range[0])
    &
    (df["beer_servings"] <= beer_range[1])
]

if search:

    filtered_df = filtered_df[
        filtered_df["country"].str.contains(
            search,
            case=False
        )
    ]

return filtered_df
