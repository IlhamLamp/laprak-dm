import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# membaca dataset
df = pd.read_csv('./data/aqiFIX.csv')
st.title("Charts")


def charts():

    def aqi_mean():
        st.header("Rata-Rata AQI Pada Tiap Bulannya")

        # menghitung rata-rata AQI pada tiap bulan
        df['Month'] = pd.to_datetime(df['Date']).dt.month
        df_mean = df.groupby('Month')['AQI'].mean().reset_index()

        # membuat dictionary untuk mapping bulan ke string
        month_dict = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
                      7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}

        # mapping bulan ke string
        df_mean['Month'] = df_mean['Month'].apply(lambda x: month_dict[x])

        # mengurutkan data berdasarkan bulan
        df_mean = df_mean.sort_values('Month')

        # menampilkan chart
        st.bar_chart(df_mean.set_index('Month'))

    def pie_chart():
        st.header("Rata-Rata Tiap Parameternya")

        # mengambil kolom kecuali City dan Date
        cols = df.columns[2:12]

        # menghitung rata-rata tiap kolom
        means = df.mean()[2:12]

        # mengecek apakah sedang menggunakan dark mode

        # membuat pie chart
        fig, ax = plt.subplots(facecolor='none')
        ax.pie(means, labels=cols, autopct='%1.1f%%')

        # menampilkan plot di dalam Streamlit
        st.pyplot(fig)

    aqi_mean()
    pie_chart()


charts()
