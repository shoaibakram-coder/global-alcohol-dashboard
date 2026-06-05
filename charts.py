import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

def bar_chart(df):

    fig, ax = plt.subplots(figsize=(8,5))

    top_beer = df.sort_values(
        by="beer_servings",
        ascending=False
    ).head(10)

    sns.barplot(
        x="beer_servings",
        y="country",
        data=top_beer,
        palette="Blues_r",
        ax=ax
    )

    st.pyplot(fig)

def pie_chart(df):

    fig, ax = plt.subplots(figsize=(8,8))

    df.groupby("country")["beer_servings"].sum().head(10).plot(
        kind="pie",
        autopct="%1.1f%%",
        ax=ax
    )

    st.pyplot(fig)

def histogram(df):

    fig, ax = plt.subplots(figsize=(10,5))

    ax.hist(
        df["beer_servings"],
        bins=20,
        color="#2563EB"
    )

    st.pyplot(fig)

def scatter_plot(df):

    fig, ax = plt.subplots(figsize=(8,5))

    sns.scatterplot(
        data=df,
        x="beer_servings",
        y="wine_servings",
        color="#38BDF8",
        ax=ax
    )

    st.pyplot(fig)

def box_plot(df):

    fig, ax = plt.subplots(figsize=(10,5))

    sns.boxplot(
        y=df["beer_servings"],
        color="#38BDF8",
        ax=ax
    )

    st.pyplot(fig)

def heatmap(df):

    fig, ax = plt.subplots(figsize=(12,8))

    sns.heatmap(
        df.select_dtypes(include="number").corr(),
        cmap="Blues",
        annot=True,
        ax=ax
    )

    st.pyplot(fig)

def area_chart(df):

    st.area_chart(
        df[
            [
                "beer_servings",
                "wine_servings"
            ]
        ].head(20)
    )

def count_plot(df):

    fig, ax = plt.subplots(figsize=(10,5))

    sns.countplot(
        y="country",
        data=df.head(10),
        palette="Blues_r",
        ax=ax
    )

    st.pyplot(fig)

def violin_plot(df):

    fig, ax = plt.subplots(figsize=(10,5))

    sns.violinplot(
        y=df["beer_servings"],
        color="#2563EB",
        ax=ax
    )

    st.pyplot(fig)

