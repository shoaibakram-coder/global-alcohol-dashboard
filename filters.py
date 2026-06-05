import streamlit as st

def sidebar_filters(df):

    st.sidebar.markdown("""
    <style>

    section[data-testid="stSidebar"]{
        background:linear-gradient(
            180deg,
            #052e16 0%,
            #064e3b 100%
        );
    }

    .sidebar-main-title{

        color:#22c55e;

        font-size:34px;

        font-weight:800;

        text-align:center;

        line-height:1.2;

        text-shadow:
            0px 0px 10px #22c55e,
            0px 0px 20px #22c55e;

        margin-bottom:10px;
    }

    .sidebar-subtitle{

        color:#dcfce7;

        text-align:center;

        font-size:15px;

        margin-bottom:20px;
    }

    label{
        color:white !important;
        font-weight:bold !important;
    }

    div[data-baseweb="select"]{
        background-color:#0F172A !important;
        border-radius:12px !important;
        border:1px solid #22c55e !important;
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

