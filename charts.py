import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

def bar_chart(df):

    fig, ax = plt.subplots(figsize=(8,5))

    top10 = df.sort_values(
        by="beer_servings",
        ascending=False
    ).head(10)

    sns.barplot(
        data=top10,
        x="beer_servings",
        y="country",
        ax=ax
    )

    st.pyplot(fig)

def pie_chart(df):

    fig, ax = plt.subplots(figsize=(8,8))

    top5 = df.head(5)

    ax.pie(
        top5["beer_servings"],
        labels=top5["country"],
        autopct="%1.1f%%"
    )

    st.pyplot(fig)

def histogram(df):

    fig, ax = plt.subplots(figsize=(8,5))

    ax.hist(
        df["beer_servings"],
        bins=20
    )

    st.pyplot(fig)

def scatter_plot(df):

    fig, ax = plt.subplots(figsize=(8,5))

    sns.scatterplot(
        data=df,
        x="beer_servings",
        y="wine_servings",
        ax=ax
    )

    st.pyplot(fig)

def box_plot(df):

    fig, ax = plt.subplots(figsize=(8,5))

    sns.boxplot(
        data=df,
        y="beer_servings",
        ax=ax
    )

    st.pyplot(fig)

def heatmap(df):

    fig, ax = plt.subplots(figsize=(10,6))

    sns.heatmap(
        df.select_dtypes(include="number").corr(),
        annot=True,
        cmap="Blues",
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

    fig, ax = plt.subplots(figsize=(8,5))

    sns.countplot(
        x="continent",
        data=df,
        ax=ax
    )

    st.pyplot(fig)

def violin_plot(df):

    fig, ax = plt.subplots(figsize=(8,5))

    sns.violinplot(
        data=df,
        y="beer_servings",
        ax=ax
    )

    st.pyplot(fig)
