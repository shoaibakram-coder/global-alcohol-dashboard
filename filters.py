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

    font-size:34px;

    font-weight:800;

    text-align:center;

    line-height:1.2;

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

    span{
        color:white !important;
    }

    div[data-baseweb="select"] > div{
        background-color:#0F172A !important;
        border:1px solid #38BDF8 !important;
        border-radius:12px !important;
    }

    div[data-baseweb="tag"]{
        background:#2563EB !important;
        border-radius:8px !important;
        border:none !important;
    }

    div[data-baseweb="tag"] span{
        color:white !important;
        font-weight:bold !important;
    }

    svg{
        color:white !important;
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

