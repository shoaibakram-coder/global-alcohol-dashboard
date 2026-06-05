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

        color:#38BDF8;

        font-size:34px;

        font-weight:800;

        text-align:center;

        line-height:1.2;

        text-shadow:
            0px 0px 8px rgba(56,189,248,0.8),
            0px 0px 18px rgba(56,189,248,0.6);

        margin-bottom:10px;
    }

    .sidebar-subtitle{

        color:#E2E8F0;

        text-align:center;

        font-size:15px;

        margin-bottom:20px;
    }

    h1{
        color:#38BDF8 !important;

        text-shadow:
            0px 0px 8px rgba(56,189,248,0.7),
            0px 0px 18px rgba(56,189,248,0.5);
    }

    label{
        color:#38BDF8 !important;
        font-weight:bold !important;
    }

    span{
        color:#38BDF8 !important;
    }

    div[data-baseweb="select"]{
        background-color:#0F172A !important;
        border-radius:12px !important;
        border:1px solid #38BDF8 !important;
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

