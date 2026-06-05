import streamlit as st

def sidebar_filters(df):

    # SIDEBAR TITLE

    st.sidebar.markdown(
    """
    <style>
    .sidebar-title {
        color: #39FF14;
        font-size: 38px;
        font-weight: 800;
        line-height: 1.2;
        text-shadow: 0px 0px 3px #39FF14;
    }
    </style>

    <div class="sidebar-title">
        🌍 Global Alcohol <br>
        Consumption Dashboard
    </div>
    """,
    unsafe_allow_html=True
)

    st.sidebar.markdown("---")

    # FILTER TITLE

    st.sidebar.markdown("""
    <h2 style='
    color:white;
    font-size:28px;
    '>
    Dashboard Filters
    </h2>
    """, unsafe_allow_html=True)

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

    # SEARCH FILTER

    search = st.sidebar.text_input(
        "Search Country"
    )

    # FILTER DATAFRAME

    filtered_df = df[
        (df["country"].isin(country))
        &
        (df["beer_servings"] >= beer_range[0])
        &
        (df["beer_servings"] <= beer_range[1])
    ]

    # SEARCH LOGIC

    if search:

        filtered_df = filtered_df[
            filtered_df["country"].str.contains(
                search,
                case=False
            )
        ]

    return filtered_df