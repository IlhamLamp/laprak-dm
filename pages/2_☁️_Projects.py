import streamlit as st
import pickle
import streamlit as st
import pandas as pd
import numpy as np

model = pickle.load(open('./data/aqiOutput.sav', 'rb'))
# df = pd.read_csv('./data/aqiFIX.csv')


def projects():
    st.title('Prediksi indeks kualitas udara')
    st.write("Masukkan nilai parameter berikut untuk menghitung AQI:")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        pm25 = st.number_input("PM2.5")
    with col2:
        pm10 = st.number_input("PM10")
    with col3:
        no = st.number_input("NO")
    with col4:
        no2 = st.number_input("NO2")
    with col1:
        nox = st.number_input("NOx")
    with col2:
        nh3 = st.number_input("NH3")
    with col3:
        co = st.number_input("CO")
    with col4:
        so2 = st.number_input("SO2")
    with col1:
        o3 = st.number_input("O3")
    with col2:
        benzene = st.number_input("Benzene")

    predict = ''

    if st.button('Hitung AQI'):
        predict = model.predict(
            [[pm25, pm10, no, no2, nox, nh3, co, so2, o3, benzene]]
        )

        st.write('AQI saat ini adalah: ', predict)

        if (predict <= 50) and (predict > 0):
            st.success('Kualitas udara Bagus ✅')
        elif (predict <= 100) and (predict > 50):
            st.info('Kualitas udara Sedang')
        elif (predict <= 200) and (predict > 100):
            st.warning('Kualitas udara Buruk ')
        elif (predict <= 300) and (predict > 200):
            st.error('Kualitas udara Tidak Sehat')
        elif (predict <= 400) and (predict > 300):
            st.error('Kualitas udara Berat')
        elif (predict > 400):
            st.error('Kualitas udara Berbahaya ⚠️')
        else:
            st.write('Wrong input')


projects()
