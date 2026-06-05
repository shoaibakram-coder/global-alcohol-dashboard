import streamlit as st

def sidebar_filters(df):

    st.sidebar.markdown("""
    <style>

    section[data-testid="stSidebar"]{
        background:linear-gradient(
            180deg,
            #0B1120 0%,
            #111827 100%
        );
    }

    .sidebar-main-title{
        color:white;
        font-size:26px;
        font-weight:800;
        text-align:center;
        line-height:1.3;
        margin-bottom:10px;
    }

    .sidebar-subtitle{
        color:#E2E8F0;
        text-align:center;
        font-size:15px;
        margin-bottom:20px;
    }

    label{
        color:#38BDF8 !important;
        font-weight:bold !important;
    }

    [data-baseweb="tag"]{
        background-color:#2563EB !important;
        color:white !important;
        border:none !important;
        border-radius:10px !important;
        padding:4px 8px !important;
    }

    [data-baseweb="tag"] span{
        color:white !important;
        font-weight:bold !important;
    }

    [data-baseweb="tag"] svg{
        color:white !important;
    }

    div[data-baseweb="select"] > div{
        background-color:#0F172A !important;
        border:1px solid #38BDF8 !important;
        border-radius:12px !important;
    }

    svg{
        color:white !important;
    }
                        
.stSlider > div > div > div > div {
    background-color:#2563EB !important;
}



    </style>
    """, unsafe_allow_html=True)

    st.sidebar.markdown("""
    <div class="sidebar-main-title">
        🌍 Global Alcohol Consumption Dashboard
    </div>

    <div class="sidebar-subtitle">
        Professional Data Analytics Dashboard
    </div>
    """, unsafe_allow_html=True)

    st.sidebar.markdown("---")

    st.sidebar.header("🎛️ Dashboard Controls")

    beer_range = st.sidebar.slider(
        "Beer Servings Range",
        min_value=int(df["beer_servings"].min()),
        max_value=int(df["beer_servings"].max()),
        value=(
            int(df["beer_servings"].min()),
            int(df["beer_servings"].max())
        )
    )

    df = df[
        (df["beer_servings"] >= beer_range[0]) &
        (df["beer_servings"] <= beer_range[1])
    ]

    st.sidebar.markdown("---")

    st.sidebar.header("Dashboard Filters")

    selected_country = st.sidebar.multiselect(
        "Select Country",
        options=sorted(df["country"].unique()),
        default=sorted(df["country"].unique())
    )

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

    filtered_df = df[
        df["country"].isin(selected_country)
    ]

    return filtered_df
