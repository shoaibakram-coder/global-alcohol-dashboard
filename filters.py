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

        text-shadow:
            0px 0px 8px rgba(16,185,129,0.7),
            0px 0px 18px rgba(16,185,129,0.5);

        margin-bottom: 10px;
    }

    .sidebar-subtitle {

        color: #D1FAE5;

        text-align: center;

        font-size: 16px;

        margin-bottom: 30px;
    }

    .section-title {

        color: white;

        font-size: 28px;

        font-weight: 700;

        margin-top: 25px;

        margin-bottom: 15px;
    }

    label {

        color: white !important;

        font-weight: 600 !important;
    }

    div[data-baseweb="select"] {

        background-color: #0F172A !important;

        border-radius: 14px !important;
    }

    </style>
    """, unsafe_allow_html=True)

    # TITLE

    st.sidebar.markdown("""
    <div class="sidebar-title">
        🔢 Digit Dashboard
    </div>

    <div class="sidebar-subtitle">
        Professional Data Analytics
    </div>
    """, unsafe_allow_html=True)

    st.sidebar.markdown("---")

    # FILTERS TITLE

    st.sidebar.markdown("""
    <div class="section-title">
        🎛 Filters
    </div>
    """, unsafe_allow_html=True)

    # DIGIT FILTER

    selected_digits = st.sidebar.multiselect(
        "Select Digits",
        options=sorted(df["digit"].unique()),
        default=sorted(df["digit"].unique())
    )

    # CHART SELECTION

    chart_options = st.sidebar.multiselect(
        "Choose Charts",
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
        df["digit"].isin(selected_digits)
    ]

    return filtered_df