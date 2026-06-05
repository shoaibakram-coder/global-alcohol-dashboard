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

    .sidebar-title{
        color:#22c55e;

        font-size:40px;

        font-weight:800;

        text-align:center;

        text-shadow:
            0px 0px 10px #22c55e,
            0px 0px 20px #22c55e;
    }

    .sidebar-subtitle{
        color:#dcfce7;

        text-align:center;

        font-size:16px;

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
            "Area Chart"
        ]
    )

    st.session_state["chart_options"] = chart_options

    filtered_df = df[
        df["country"].isin(selected_country)
    ]

    return filtered_df

