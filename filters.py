import streamlit as st

def sidebar_filters(df):

    st.sidebar.markdown("""
    <style>

    section[data-testid="stSidebar"]{
        background: linear-gradient(
            180deg,
            #052e16 0%,
            #064e3b 100%
        );
        border-right: 2px solid #22c55e;
    }

    .sidebar-title{
        font-size: 40px;
        font-weight: 800;
        text-align: center;
        margin-bottom: 10px;

        background: linear-gradient(
            90deg,
            #22c55e,
            #4ade80,
            #86efac
        );

        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;

        text-shadow:
            0px 0px 10px rgba(34,197,94,0.9),
            0px 0px 20px rgba(74,222,128,0.8),
            0px 0px 35px rgba(134,239,172,0.7);
    }

    .sidebar-subtitle{
        color: #dcfce7;
        text-align: center;
        font-size: 18px;
        margin-bottom: 25px;
    }

    .filter-title{
        color: #bbf7d0;
        font-size: 26px;
        font-weight: 700;
        margin-top: 20px;
        margin-bottom: 10px;
    }

    label{
        color: white !important;
        font-size: 16px !important;
        font-weight: 600 !important;
    }

    div[data-baseweb="select"]{
        background-color: #022c22 !important;
        border: 1px solid #22c55e !important;
        border-radius: 12px !important;
        box-shadow: 0px 0px 12px rgba(34,197,94,0.4);
    }

    .stMultiSelect div{
        color: white !important;
    }

    </style>
    """, unsafe_allow_html=True)

    st.sidebar.markdown("""
        <div class="sidebar-title">
            🌍 Global Alcohol Dashboard
        </div>

        <div class="sidebar-subtitle">
            Professional Data Analytics
        </div>

        <hr>

        <div class="filter-title">
            Dashboard Filters
        </div>
    """, unsafe_allow_html=True)

    selected_country = st.sidebar.multiselect(
        "Select Country",
        options=sorted(df["country"].unique()),
        default=sorted(df["country"].unique())
    )

    chart_options = st.sidebar.multiselect(
        "Select Additional Charts",
        [
            "Bar Chart",
            "Scatter Plot",
            "Histogram",
            "Box Plot",
            "Heatmap",
            "Area Chart"
        ]
    )

    st.session_state["chart_options"] = chart_options

    filtered_df = df[
        df["country"].isin(selected_country)
    ]

    return filtered_df