
import os
import streamlit as st
import numpy as np
import pandas as pd

def style_app():
    st.markdown(
        '''
        <style>
        .main {
            background-color: #F5F5F5;
        }
        h1, h2, h3, h4, h5, h6, p, .stMarkdown, .caption, .css-1aumxhk {
            color: #333333;  /* Mengubah warna font menjadi gelap */
        }
        .stButton>button {
            color: #ffffff;
            background-color: #ff6347;
            border: none;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            transition-duration: 0.4s;
            cursor: pointer;
            border-radius: 8px;
        }
        .stButton>button:hover {
            background-color: #e55347;
            color: white;
        }
        </style>
        ''',
        unsafe_allow_html=True
    )

# Tampilan utama aplikasi
def display_main_app():
    st.title("WOYY SELAMAT ULANG TAHUNN ke-18 TAHUN YAAA")
    st.markdown("### HAPPY BISDEYYY!!")


def floating_balloons(character):
    st.markdown(f"""
        <style>
        @keyframes float {{
            0% {{
                transform: translateY(0px);
            }}
            50% {{
                transform: translateY(-20px);
            }}
            100% {{
                transform: translateY(0px);
            }}
        }}
        .balloon {{
            animation: float 6s ease-in-out infinite;
            font-size: 3rem;
        }}
        </style>
        <div class="balloon">{character}{character}{character}{character}{character}{character}{character}{character}{character}{character}</div>
    """, unsafe_allow_html=True)

# Contoh pemanggilan fungsi:
# floating_balloons('🎈')  # Untuk balon
# floating_balloons('❤️')  # Untuk hati
# floating_balloons('🌟')  # Untuk bintang

def blinking_text():
    st.markdown("""
        <style>
        @keyframes blink {
            50% {
                opacity: 0;
            }
        }
        .blinking-text {
            animation: blink 1s linear infinite;
        }
        </style>
        <div class="blinking-text">✨ Teks Berkedip ✨</div>
    """, unsafe_allow_html=True)

def zoom_in_image():
    st.markdown("""
        <style>
        .zoom-in img {
            transition: transform .5s ease;
        }
        .zoom-in img:hover {
            transform: scale(1.1);
        }
        </style>
        <div class="zoom-in">
            <img src="path_to_your_image/dalle.png" width="300"/>
        </div>
    """, unsafe_allow_html=True)


# Panel kosong untuk konten kustom
def custom_content_panels():
    with st.expander("Selamattt!!!"):
        st.write("Selamat ulang tahun, Ica! 🥳✨")
        st.write("Hari ini adalah hari yang spesial, hari di mana seseorang yang luar biasa seperti kamu dilahirkan ke dunia. Terima kasih karena sudah menjadi pribadi yang selalu membawa kebaikan, semangat, dan tawa ke dalam hidup orang-orang di sekitarmu. Setiap senyumanmu, setiap kebaikan kecil yang kamu lakukan, semuanya punya dampak yang jauh lebih besar dari yang mungkin kamu sadari.")
        st.write("Di antara jutaan orang di dunia ini, aku bersyukur sekali bisa mengenal kamu. Bisa menyaksikan setiap versi dirimu tumbuh, menghadapi hari-hari sulit, melewati luka, tapi tetap bertahan. Aku tahu, kamu bukan orang yang selalu cerita banyak hal. Tapi dari caramu tersenyum meski sedang lelah, dari caramu tetap peduli saat dirimu sendiri sedang butuh disemangati, aku tahu kamu kuat, luar biasa kuat.")
        st.write("Ica… mungkin hidup tidak selalu baik padamu. Ada masa-masa kamu merasa sendiri, tidak cukup, atau bahkan lelah menjadi kuat terus-terusan. Tapi hari ini, izinkan aku mengingatkan satu hal penting: kamu sudah jauh melampaui apa yang dulu kamu takutkan. Kamu hebat, meski kamu jarang mengakuinya.")

    with st.expander("Harapann"):
        st.write("Aku harap ulang tahunmu ini bukan sekadar angka baru di kalender, tapi awal dari lembaran hidup yang lebih indah dan lebih damai. Semoga kamu selalu dikelilingi oleh cinta yang tidak membuatmu lelah, oleh orang-orang yang melihatmu apa adanya, dan oleh keberkahan yang datang diam-diam tanpa kamu duga.")
        st.write("Semoga segala luka pelan-pelan berubah jadi pelajaran, segala harapan yang pernah tertunda kini mulai satu per satu datang menghampiri. Semoga kamu nggak pernah kehilangan semangat untuk mencintai hidup, meski hidup tak selalu mudah. Dan semoga… kamu terus diberi alasan untuk tersenyum, tanpa harus berpura-pura.")
        sr.write("Selamat ulang tahun. Terima kasih karena sudah menjadi kamu. Tetap jadi cahaya, meski kadang kamu harus berjalan dalam gelap. Aku doakan kamu selalu bahagia bukan hanya saat difoto, tapi juga saat kamu sendiri, saat kamu berdoa, saat kamu tertawa tanpa alasan. Karena kamu pantas mendapatkan itu semua. 🌷")

def display_image(image_path):
    # Cek apakah file gambar ada di path yang diberikan
    if os.path.exists(image_path):
        st.image(image_path, caption=f'Gambar: {image_path}', use_column_width=True)
    else:
        st.error(f'File gambar {image_path} tidak ditemukan.')

# Main function untuk menjalankan aplikasiS
def main():
    
    style_app()
    display_main_app()
    custom_content_panels()

if __name__ == "__main__":
    main()
