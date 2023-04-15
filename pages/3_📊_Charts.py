import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import altair as alt
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
model_path = os.path.join(dir_path, 'data', 'liver_patient.csv')

with open(model_path, 'rb') as f:
    df = pd.read_csv(f)


def charts():

    def bar_charts():
        st.header("Kasus berdasarkan Rentang Usia")
        # Filter data to only include cases of liver disease
        df_liver = df[df['Dataset'] == 1]

        # Create a bar chart of age distribution
        age_counts = df_liver['Umur'].value_counts().sort_index()
        chart = alt.Chart(age_counts.reset_index()).mark_bar().encode(
            x=alt.X('index:Q', title='Age'),
            y=alt.Y('Umur:Q', title='Number of Cases')
        )

        st.altair_chart(chart, use_container_width=True)

    def pie_charts():
        # Pie chart
        st.write("### Kasus berdasarkan Jenis Kelamin")
        plt.style.use('seaborn')
        fig, ax = plt.subplots()
        colors = ['#ff9999', '#66b3ff']
        ax.pie(df['Jenis_Kelamin'].value_counts(), labels=df['Jenis_Kelamin'].value_counts(
        ).index, colors=colors, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')
        st.pyplot(fig)

    # call func
    bar_charts()
    pie_charts()


#
charts()
