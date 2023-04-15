import streamlit as st

st.set_page_config(
    page_title="D'Liver",
    page_icon="💝"
)


def home():
    st.title("Halo Semuanya 😄")
    st.markdown(
        "Project ini berjudul **D'Liver**, dimana kami mencoba mendiagnosa penyakit liver dengan beberapa parameter tertentu.")
    st.markdown(
        "Dataset diambil dari link [berikut](https://www.kaggle.com/code/harisyammnv/liver-disease-prediction). Metode yang digunakan adalah **Regresi Linier**, dan berikut adalah 2 hasil prediksi berdasarkan nilai: "
    )
    st.write("")

    col1, col2 = st.columns(2)

    with col1:
        st.success('**0 : Pasien tidak didiagnosis menderita penyakit hati. ✅**')

    with col2:
        st.error('**1 : Pasien didiagnosis menderita penyakit hati. ⚠️**')


home()
st.sidebar.info("Select a page above.")
