import streamlit as st
import time

# Konfigurasi halaman
st.set_page_config(page_title="Ucapan Ulang Tahun untuk Ica", page_icon="🎂", layout="centered")

# Animasi pembuka
st.snow()
st.balloons()

# Judul
st.markdown("<h1 style='text-align: center; color: #ff4b4b;'>🎉 Selamat Ulang Tahun Ica! 🎉</h1>", unsafe_allow_html=True)

# Efek loading sebelum ucapan muncul
with st.spinner("Membuka pesan spesial..."):
    time.sleep(2)

# Ucapan ulang tahun
ucapan = """
<div style='font-size: 18px; text-align: justify; color: #444; line-height: 1.8;'>

Hari ini bukan hari biasa... karena tepat 18 tahun yang lalu, seorang bintang lahir ke dunia ini 🌟<br><br>

Selamat ulang tahun yang ke-18, <b>Ica</b>! 🥳 <br><br>

Di usia yang baru ini, semoga setiap langkahmu dipenuhi keberanian, setiap harapanmu dipenuhi cahaya, dan setiap mimpimu menjadi nyata satu per satu.✨<br><br>

Terima kasih sudah menjadi pribadi yang kuat, manis, dan menginspirasi banyak orang. Dunia lebih indah dengan kehadiranmu 💖<br><br>

<b>Jangan lupa bahagia hari ini, karena kamu pantas mendapatkannya sepenuhnya! 🎁🎈</b><br><br>

Dengan cinta dan doa terbaik selalu 💌

</div>
"""
st.markdown(ucapan, unsafe_allow_html=True)

# Penutup
st.markdown("---")
st.markdown("<p style='text-align: center; font-size:16px; color:gray;'>Dari seseorang yang peduli 🌹</p>", unsafe_allow_html=True)
