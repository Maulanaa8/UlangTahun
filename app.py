import streamlit as st
import time

# Konfigurasi halaman
st.set_page_config(page_title="Selamat Ulang Tahun Ica 🎂", page_icon="🎈", layout="centered")

# Animasi pembuka
st.snow()
st.balloons()

# CSS kustom untuk tampilan lebih cantik
st.markdown("""
    <style>
        body {
            background-color: #fff0f5;
        }
        .card {
            background-color: #ffffffcc;
            padding: 30px;
            border-radius: 20px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            max-width: 700px;
            margin: auto;
            font-family: 'Trebuchet MS', sans-serif;
        }
        h1 {
            text-align: center;
            color: #e75480;
            font-size: 3em;
        }
        .subtitle {
            text-align: center;
            font-size: 1.3em;
            color: #666;
            margin-bottom: 20px;
        }
        .content {
            font-size: 18px;
            color: #333;
            line-height: 1.8;
            text-align: justify;
        }
        .footer {
            text-align: center;
            margin-top: 30px;
            font-style: italic;
            color: #888;
        }
    </style>
""", unsafe_allow_html=True)

# Judul dan pembuka
st.markdown("<h1>🎉 Selamat Ulang Tahun Ica! 🎉</h1>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Usia ke-18 adalah awal dari petualangan luar biasa ✨</div>", unsafe_allow_html=True)

# Efek loading seperti membuka surat
with st.spinner("Membuka surat cinta untuk Ica... 💌"):
    time.sleep(2)

# Kartu ucapan
st.markdown("""
<div class='card'>
    <div class='content'>
        Hai <b>Ica</b> tersayang, 🌸<br><br>

        Hari ini adalah hari spesial karena 18 tahun lalu, kamu hadir ke dunia membawa cahaya dan kehangatan untuk orang-orang di sekitarmu.<br><br>

        Di usia ke-18 ini, semoga setiap langkahmu penuh dengan berkah, setiap harapanmu disertai doa, dan setiap mimpimu satu per satu menjadi nyata. 🎀<br><br>

        Jadilah versi terbaik dari dirimu. Tersenyumlah lebih sering, cintailah dirimu sendiri, dan tetap jadi pribadi yang rendah hati dan menginspirasi. 🌷<br><br>

        <b>Selamat ulang tahun, Ica! 🎂🎈 Semoga hari ini seindah hatimu 💖</b><br><br>
    </div>
    <div class='footer'>
        — Dari seseorang yang selalu mendoakan kebahagiaanmu 🌹
    </div>
</div>
""", unsafe_allow_html=True)
