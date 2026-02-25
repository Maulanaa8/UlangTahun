import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Happy Birthday", page_icon="🎉", layout="wide")

# ===== CUSTOM CSS =====
st.markdown("""
<style>

html, body, [class*="css"]  {
    scroll-behavior: smooth;
}

section {
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
    flex-direction: column;
    padding: 50px;
}

.hero {
    background: linear-gradient(135deg, #d4c1ec, #fbc2eb);
    color: white;
}

.gallery {
    background: linear-gradient(135deg, #a1c4fd, #c2e9fb);
}

.ucapan {
    background: linear-gradient(135deg, #fddb92, #d1fdff);
}

.title {
    font-size: 70px;
    font-weight: bold;
    animation: fadeIn 2s ease-in-out;
}

.subtitle {
    font-size: 25px;
    margin-top: 20px;
    animation: fadeIn 3s ease-in-out;
}

@keyframes fadeIn {
    from {opacity:0; transform:translateY(30px);}
    to {opacity:1; transform:translateY(0);}
}

.floating {
    animation: float 4s ease-in-out infinite;
}

@keyframes float {
    0% {transform: translateY(0px);}
    50% {transform: translateY(-20px);}
    100% {transform: translateY(0px);}
}

img {
    border-radius: 20px;
}

</style>
""", unsafe_allow_html=True)

# ===== SLIDE 1 - HERO =====
st.markdown("""
<section class="hero">
    <div class="title">HAPPY BIRTHDAY</div>
    <div class="subtitle">Komunitas Hebat & Inspiratif 🚀</div>
    <p style="margin-top:30px;">Scroll ke bawah ⬇</p>
</section>
""", unsafe_allow_html=True)

# ===== SLIDE 2 - GALLERY =====
st.markdown("""
<section class="gallery">
    <h1>📸 Kenangan Indah</h1>
</section>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.image("images/foto1.jpg", use_container_width=True)
with col2:
    st.image("images/foto2.jpg", use_container_width=True)
with col3:
    st.image("images/foto3.jpg", use_container_width=True)

# ===== SLIDE 3 - UCAPAN =====
st.markdown("""
<section class="ucapan">
    <h1>💌 Kirim Ucapan</h1>
</section>
""", unsafe_allow_html=True)

if "ucapan_list" not in st.session_state:
    st.session_state.ucapan_list = []

with st.form("form_ucapan"):
    nama = st.text_input("Nama")
    pesan = st.text_area("Ucapan")
    submit = st.form_submit_button("Kirim 🎉")

    if submit:
        st.session_state.ucapan_list.append((nama, pesan))
        st.success("Ucapan terkirim!")

st.markdown("### ✨ Ucapan Anggota")

for nama, pesan in st.session_state.ucapan_list:
    st.markdown(f"""
        <div style="
            background:white;
            padding:15px;
            border-radius:15px;
            margin-bottom:10px;">
            <b>{nama}</b><br>{pesan}
        </div>
    """, unsafe_allow_html=True)

# ===== CONFETTI OTOMATIS SAAT HARI H =====
tanggal_acara = datetime(2026, 3, 10)
if datetime.now().date() == tanggal_acara.date():
    st.balloons()
