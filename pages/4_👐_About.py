import streamlit as st


def main():

    c = st.container()
    scol1, scol2, scol3 = st.columns(3)
    tcol1, tcol2, tcol3 = st.columns(3)

    # Title Section
    with scol1:
        st.write("")
    with scol2:
        st.title("About Us")
    with scol3:
        st.write("")

    # Hero Section
    st.write(
        "Website sederhana ini dibuat sebagai syarat Tugas Akhir Praktikum Data Mining Semester 6. Nostrud culpa consectetur do incididunt qui est proident adipisicing ea incididunt. Ex non aliquip est ullamco consectetur consectetur nostrud veniam id et sint anim. Magna consectetur excepteur et dolor voluptate nisi veniam nostrud eu id. Culpa et magna deserunt nulla in voluptate ipsum consectetur eiusmod ex nisi laborum ipsum ut. Consequat deserunt ipsum occaecat elit magna.")

    st.header("Anggota Kelompok")

    st.subheader("Orang Pertama")
    st.write("Nama: Aditya Bani Isro")
    st.write("NIM: 312010134")
    st.write("Kelas: TI.20.A1")

    st.subheader("Orang Kedua")
    st.write("Nama: Ilham Nur Utomo")
    st.write("NIM: 312010129")
    st.write("Kelas: TI.20.A1")

    st.subheader("Orang Ketiga")
    st.write("Nama: Muhammad Choerumansyah")
    st.write("NIM: 312010031")
    st.write("Kelas: TI.20.A1")


if __name__ == '__main__':
    main()
