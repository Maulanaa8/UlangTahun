import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Happy Birthday Community", page_icon="🎉", layout="wide")

# ===== CUSTOM CSS =====
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #c3cfe2, #f5c6ec);
}

.hero {
    text-align: center;
    padding: 120px 20px;
    animation: fadeIn 2s ease-in;
}

.title {
    font-size: 60px;
    font-weight: bold;
    color: white;
}

.subtitle {
    font-size: 24px;
    color: #f0f0f0;
}

@keyframes fadeIn {
    from {opacity: 0;}
    to {opacity: 1;}
}

.floating {
    animation: float 4s ease-in-out infinite;
}

@keyframes float {
    0% {transform: translatey(0px);}
    50% {transform: translatey(-20px);}
    100% {transform: translatey(0px);}
}
</style>
""", unsafe_allow_html=True)

# ===== HERO SECTION =====
st.markdown("""
<div class="hero">
    <div class="title">HAPPY BIRTHDAY</div>
    <div class="subtitle">Komunitas Hebat & Inspiratif 🚀</div>
</div>
""", unsafe_allow_html=True)

# ===== COUNTDOWN =====
tanggal_acara = datetime(2026, 3, 10)
sekarang = datetime.now()
selisih = tanggal_acara - sekarang

st.markdown("---")
if selisih.days > 0:
    st.info(f"🎂 {selisih.days} Hari Menuju Perayaan!")
else:
    st.success("🎉 Hari Ini Perayaan Dimulai!")

st.markdown("### 🎈 Gunakan Menu di Sidebar untuk Melihat Halaman Lain")
