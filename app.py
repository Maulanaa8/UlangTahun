import streamlit as st
import time

st.set_page_config(
    page_title="Selamat Ulang Tahun Ica 🎂",
    page_icon="🎀",
    layout="centered"
)

# Tambahkan CSS estetik
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Great+Vibes&family=Quicksand:wght@400;600&display=swap');

body {
    background: linear-gradient(135deg, #ffe4ec 0%, #fcefee 100%);
}

h1 {
    font-family: 'Great Vibes', cursive;
    font-size: 64px;
    color: #e75480;
    text-align: center;
    margin-bottom: 0;
}

.subtitle {
    text-align: center;
    font-size: 22px;
    color: #555;
    font-family: 'Quicksand', sans-serif;
    margin-bottom: 30px;
}

.card {
    background-color: #ffffffdd;
    padding: 40px;
    border-radius: 20px;
    max-width: 700px;
    margin: auto;
    box-shadow: 0 8px 20px rgba(0,0,0,0.08);
    font-family: 'Quicksand', sans-serif;
    font-size: 18px;
    color: #333;
    line-height: 1.8;
    animation: fadeIn 2s ease-in-out;
}

.footer {
    margin-top: 30px;
    text-align: center;
    font-style: italic;
    color: #999;
    font-size: 15px;
}

@keyframes fadeIn {
    0% {opacity: 0;}
    100% {opacity: 1;}
}
</style>
""", unsafe_allow_html=True)

# Efek animasi sederhana
st.balloons()
st.snow()

# Judul dan subjudul
st.markdown("<h1>Selamat Ulang Tahun, Ica!!</h1>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>✨ Happy Eighteen Years ✨</div>", unsafe_allow_html=True)

# Loading simulasi
with st.spinner("Membuka surat ulang tahun dari hati terdalam... 💌"):
    time.sleep(2.5)

# Konten ucapan
st.markdown("""
<div class='card'>

Hari ini adalah hari yang spesial, karena tepat 18 tahun yang lalu, seorang gadis luar biasa seperti kamu terlahir ke dunia. 🌍<br><br>

Semoga di usia barumu ini, kamu menemukan kebahagiaan sejati, tetap ceria seperti biasanya, dan tidak pernah kehilangan semangat untuk bermimpi besar. 🎯<br><br>

Di umur ke-18 ini, kamu bukan hanya tumbuh secara usia, tapi juga sebagai pribadi yang makin kuat, dewasa, dan menginspirasi. Jadilah cahaya, untuk dirimu dan dunia. ✨<br><br>

Teruslah melangkah dengan hati yang tulus, senyum yang hangat, dan cinta yang penuh pada hidupmu sendiri. 💖<br><br>

<b>Happy 18th Birthday, Ica! 🎂 Semoga semua hal indah berpihak padamu hari ini dan selamanya.</b>

</div>

<div class='footer'>— Dengan doa terbaik, dariku 🌹</div>
""", unsafe_allow_html=True)
