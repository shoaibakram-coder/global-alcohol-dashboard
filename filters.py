import streamlit as st

def sidebar_filters(df):

    st.sidebar.markdown("""
    <style>

    section[data-testid="stSidebar"]{
        background-color:#111827;
    }

    .sidebar-title{
        color:#7DD3FC;
        font-size:30px;
        font-weight:bold;
        text-align:center;
        text-shadow:0px 0px 10px #38BDF8;
        margin-bottom:10px;
    }

    .sidebar-subtitle{
        color:#CBD5E1;
        text-align:center;
        font-size:14px;
        margin-bottom:20px;
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
    """, unsafe_allow_html=True)

    st.sidebar.markdown("---")

    st.sidebar.header("Dashboard Filters")

    selected_country = st.sidebar.multiselect(
        "Select Country",
        options=df["country"].unique(),
        default=df["country"].unique()
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

