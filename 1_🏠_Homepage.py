import streamlit as st

st.set_page_config(
    page_title="AQI Prediction",
    page_icon="✍️"
)


def home():
    st.title("Halo Semuanya 😄")
    st.markdown(
        "Project ini berjudul **AQI Prediction**, dimana kami mencoba mengukur indeks kualitas udara sekitar.")
    st.markdown(
        "Dataset diambil dari link [berikut](https://www.kaggle.com/datasets/rohanrao/air-quality-data-in-india), dengan fokus pada kota Mumbai di India pada periode 2019-2020 pertengahan."
    )
    st.write("Metode yang digunakan adalah **Regresi Linier**, dan berikut adalah skala AQI yang kami tetapkan: ")
    st.write("")

    col1, col2 = st.columns(2)

    with col1:
        st.success('**0 - 50 : Kualitas Udara Bagus ✅**')

    with col2:
        st.error('**201 - 300 : Kualitas Udara Tidak Sehat**')

    with col1:
        st.info('**51 - 100 : Kualitas Udara Sedang**')

    with col2:
        st.error('**301 - 400 : Kualitas udara Berat**')

    with col1:
        st.warning('**101 - 200 : Kualitas Udara Buruk**')

    with col2:
        st.error('**> 400 : Kualitas udara Berbahaya ⚠️**')


home()
st.sidebar.success("Select a page above.")
