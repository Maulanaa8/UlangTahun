import streamlit as st
import time

st.set_page_config(page_title="Ucapan Ulang Tahun", page_icon="🎉", layout="centered")

# Animasi awal
st.balloons()
st.markdown("<h1 style='text-align: center; color: #FF69B4;'>🎂 Ucapan Ulang Tahun 🎂</h1>", unsafe_allow_html=True)

# Input dari pengguna
nama = st.text_input("Masukkan nama orang yang berulang tahun:", "")
umur = st.number_input("Masukkan usia sekarang:", min_value=1, max_value=150, step=1)

# Jika nama diisi, tampilkan ucapan
if nama:
    st.markdown("---")
    st.markdown(f"### Hai {nama}! 🥳")

    # Efek loading seolah-olah sedang menyiapkan ucapan
    with st.spinner("Menyiapkan ucapan spesial untukmu..."):
        time.sleep(2)

    # Ucapan ulang tahun
    ucapan = f"""
    <div style='font-size: 18px; color: #444;'>
        Hari ini spesial karena dunia diberkati dengan kelahiranmu {umur} tahun yang lalu. 🎈<br><br>

        Semoga di usia yang baru ini, {nama} selalu diberi kebahagiaan, kesehatan, dan kesuksesan tanpa batas. ✨<br><br>

        Teruslah bersinar dan menjadi versi terbaik dari dirimu!<br><br>

        <b>Selamat ulang tahun, {nama}! 🎉🎁</b>
    </div>
    """
    st.markdown(ucapan, unsafe_allow_html=True)

    st.success("Ucapan dikirim dengan cinta 💖")

    # Tambahan: tombol untuk download ucapan sebagai file txt
    if st.button("📥 Download Ucapan"):
        isi = f"Selamat Ulang Tahun, {nama}!\n\nSemoga di usia ke-{umur} ini kamu selalu diberi kebahagiaan, kesehatan, dan kesuksesan.\nTeruslah bersinar dan menjadi pribadi yang luar biasa!\n\n🎂🎉🎁"
        st.download_button("Klik untuk mengunduh ucapan 🎊", data=isi, file_name=f"Ucapan_Ulang_Tahun_{nama}.txt")
