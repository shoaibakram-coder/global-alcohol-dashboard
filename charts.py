import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set_style("darkgrid")

# BAR CHART

def bar_chart(df):

    fig, ax = plt.subplots(figsize=(10,5))

    top = df.sort_values(
        by="beer_servings",
        ascending=False
    ).head(10)

    sns.barplot(
        data=top,
        x="country",
        y="beer_servings",
        ax=ax
    )

    plt.xticks(rotation=45)

    ax.set_title("Top Beer Consuming Countries")

    st.markdown('<div class="chart-box">', unsafe_allow_html=True)

st.pyplot(fig)

st.markdown('</div>', unsafe_allow_html=True)


# HISTOGRAM

def histogram(df):

    fig, ax = plt.subplots(figsize=(8,5))

    sns.histplot(
        df["total_litres_of_pure_alcohol"],
        kde=True,
        ax=ax
    )

    ax.set_title("Alcohol Distribution")

    st.markdown('<div class="chart-box">', unsafe_allow_html=True)

st.pyplot(fig)

st.markdown('</div>', unsafe_allow_html=True)


# SCATTER PLOT

def scatter_plot(df):

    fig, ax = plt.subplots(figsize=(8,5))

    sns.scatterplot(
        data=df,
        x="beer_servings",
        y="spirit_servings",
        hue="wine_servings",
        ax=ax
    )

    ax.set_title("Beer vs Spirit")

   st.markdown('<div class="chart-box">', unsafe_allow_html=True)

st.pyplot(fig)

st.markdown('</div>', unsafe_allow_html=True)


# BOX PLOT

def box_plot(df):

    fig, ax = plt.subplots(figsize=(8,5))

    sns.boxplot(
        data=df[
            [
                "beer_servings",
                "spirit_servings",
                "wine_servings"
            ]
        ],
        ax=ax
    )

    ax.set_title("Box Plot")

   st.markdown('<div class="chart-box">', unsafe_allow_html=True)

st.pyplot(fig)

st.markdown('</div>', unsafe_allow_html=True)


# HEATMAP

def heatmap(df):

    fig, ax = plt.subplots(figsize=(8,5))

    sns.heatmap(
        df.corr(numeric_only=True),
        annot=True,
        cmap="Greens",
        ax=ax
    )

    ax.set_title("Correlation Heatmap")

    st.markdown('<div class="chart-box">', unsafe_allow_html=True)

st.pyplot(fig)

st.markdown('</div>', unsafe_allow_html=True)


# PIE CHART

def pie_chart(df):

    top = df.head(10)

    fig, ax = plt.subplots(figsize=(8,8))

    ax.pie(
        top["wine_servings"],
        labels=top["country"],
        autopct="%1.1f%%"
    )

    ax.set_title("Wine Consumption Share")

   st.markdown('<div class="chart-box">', unsafe_allow_html=True)

st.pyplot(fig)

st.markdown('</div>', unsafe_allow_html=True)


# LINE CHART

def line_chart(df):

    top = df.sort_values(
        by="total_litres_of_pure_alcohol",
        ascending=False
    ).head(20)

    fig, ax = plt.subplots(figsize=(10,5))

    sns.lineplot(
        data=top,
        x="country",
        y="total_litres_of_pure_alcohol",
        marker="o",
        ax=ax
    )

    plt.xticks(rotation=45)

    ax.set_title("Alcohol Consumption Trend")
st.markdown('<div class="chart-box">', unsafe_allow_html=True)

st.pyplot(fig)

st.markdown('</div>', unsafe_allow_html=True)


# AREA CHART

def area_chart(df):

    top = df.sort_values(
        by="beer_servings",
        ascending=False
    ).head(15)

    fig, ax = plt.subplots(figsize=(10,5))

    ax.fill_between(
        range(len(top)),
        top["beer_servings"],
        alpha=0.5
    )

    plt.xticks(
        range(len(top)),
        top["country"],
        rotation=45
    )

    ax.set_title("Beer Servings Area Chart")

    st.markdown('<div class="chart-box">', unsafe_allow_html=True)

st.pyplot(fig)

st.markdown('</div>', unsafe_allow_html=True)


# COUNT PLOT

def count_plot(df):

    fig, ax = plt.subplots(figsize=(10,5))

    sns.countplot(
        x="beer_servings",
        data=df,
        ax=ax
    )

    ax.set_title("Beer Servings Count Plot")

    st.markdown('<div class="chart-box">', unsafe_allow_html=True)

st.pyplot(fig)

st.markdown('</div>', unsafe_allow_html=True)


# VIOLIN PLOT

def violin_plot(df):

    fig, ax = plt.subplots(figsize=(8,5))

    sns.violinplot(
        data=df[
            [
                "beer_servings",
                "spirit_servings",
                "wine_servings"
            ]
        ],
        ax=ax
    )

    ax.set_title("Violin Plot")

    sst.markdown('<div class="chart-box">', unsafe_allow_html=True)

st.pyplot(fig)

st.markdown('</div>', unsafe_allow_html=True)