import streamlit as st
from datetime import datetime
import time

# Konfigurasi halaman
st.set_page_config(
    page_title="Ulang Tahun Komunitas",
    page_icon="🎉",
    layout="centered"
)

# ====== HEADER ======
st.title("🎉 Selamat Ulang Tahun Komunitas Kita 🎉")
st.write("Bersama, Bertumbuh, dan Menginspirasi 🚀")

# ====== COUNTDOWN ======
tanggal_acara = datetime(2026, 3, 10)
sekarang = datetime.now()
selisih = tanggal_acara - sekarang

if selisih.days > 0:
    st.info(f"⏳ Menuju hari spesial: {selisih.days} hari lagi!")
else:
    st.success("🎂 Hari Ini Ulang Tahun Komunitas! 🎂")

st.divider()

# ====== GALERI FOTO ======
st.subheader("📸 Kenangan Perjalanan Komunitas")

col1, col2 = st.columns(2)

with col1:
    st.image("https://picsum.photos/400/300", caption="Kegiatan 1")
    st.image("https://picsum.photos/401/300", caption="Kegiatan 2")

with col2:
    st.image("https://picsum.photos/402/300", caption="Kegiatan 3")
    st.image("https://picsum.photos/403/300", caption="Kegiatan 4")

st.divider()

# ====== FORM UCAPAN ======
st.subheader("💌 Kirim Doa & Harapan")

if "ucapan_list" not in st.session_state:
    st.session_state.ucapan_list = []

with st.form("form_ucapan"):
    nama = st.text_input("Nama")
    pesan = st.text_area("Tulis ucapan terbaikmu...")
    submit = st.form_submit_button("Kirim 🎉")

    if submit:
        if nama and pesan:
            st.session_state.ucapan_list.append({
                "nama": nama,
                "pesan": pesan
            })
            st.success("Ucapan berhasil dikirim 🎉")
        else:
            st.warning("Isi semua field dulu ya!")

# ====== TAMPILKAN UCAPAN ======
st.divider()
st.subheader("✨ Ucapan dari Anggota")

for u in st.session_state.ucapan_list:
    st.markdown(
        f"""
        <div style="
            background-color:#f0f2f6;
            padding:15px;
            border-radius:10px;
            margin-bottom:10px;">
            <b>{u['nama']}</b><br>
            {u['pesan']}
        </div>
        """,
        unsafe_allow_html=True
    )
