import pandas as pd
import numpy as np
import streamlit as st
import os
from sklearn.ensemble import RandomForestClassifier

# load dataset
dir_path = os.path.dirname(os.path.realpath(__file__))
model_path = os.path.join(dir_path, 'data', 'liver_patient.csv')

with open(model_path, 'rb') as f:
    df = pd.read_csv(f)

# Drop missing values
df = df.dropna()

# Convert categorical data to numerical
df['Jenis_Kelamin'] = df['Jenis_Kelamin'].map({'Pria': 1, 'Wanita': 0})

# Define function to make prediction using Random Forest Classifier


def predict_liver_disease(umur, jk, tbil, dbil, alkphos, sgpt, sgot, tp, alb):
    X = df[['Umur', 'Jenis_Kelamin', 'Total_Bilirubin', 'Direct_Bilirubin',
            'Alkaline_Phosphotase', 'Alamine_Aminotransferase', 'Aspartate_Aminotransferase', 'Total_Protiens', 'Albumin']]
    y = df['Dataset']

    # Train the model
    clf = RandomForestClassifier(n_estimators=100, max_depth=5)
    clf.fit(X, y)

    # Make prediction
    prediction = clf.predict(
        [[umur, jk, tbil, dbil, alkphos, sgpt, sgot, tp, alb]])

    return prediction


# Set page title
st.title('Diagnosis Penyakit Liver')

col1, col2, col3, col4 = st.columns(4)

# Create input form
umur = st.slider('Umur', min_value=0, max_value=100, value=50)
with col1:
    jk = st.selectbox('Jenis Kelamin', options=['Pria', 'Wanita'])
with col2:
    tbil = st.number_input('Total Bilirubin', min_value=0.0,
                           max_value=100.0, value=0.7, step=0.1)
with col3:
    dbil = st.number_input('Direct Bilirubin', min_value=0.0,
                           max_value=100.0, value=0.1, step=0.1)
with col4:
    alkphos = st.number_input('Alkaline Phosphotase',
                              min_value=0, max_value=1000, value=187, step=10)
with col1:
    sgpt = st.number_input('Alamine Aminotransferase',
                           min_value=0, max_value=1000, value=25, step=10)
with col2:
    sgot = st.number_input('Aspartate Aminotransferase',
                           min_value=0, max_value=1000, value=35, step=10)
with col3:
    tp = st.number_input('Total Protein', min_value=0.0,
                         max_value=10.0, value=7.6, step=0.1)
with col4:
    alb = st.number_input('Albumin', min_value=0.0,
                          max_value=10.0, value=4.4, step=0.1)

if st.button('Prediksi'):
    jk = 1 if jk == 'Pria' else 0
    prediction = predict_liver_disease(
        umur, jk, tbil, dbil, alkphos, sgpt, sgot, tp, alb)
    if prediction == 1:
        st.error('Pasien didiagnosis menderita penyakit hati. ⚠️')
    else:
        st.success('Pasien tidak didiagnosis dengan penyakit hati. ✅')
