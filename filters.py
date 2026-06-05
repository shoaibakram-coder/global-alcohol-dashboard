import streamlit as st

def sidebar_filters(df):

    st.sidebar.title(
        "🌍 Dashboard Filters"
    )

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

