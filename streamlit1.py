
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
    st.title("SELAMAT ULANG TAHUN WOI WUS WUS WUS WUZZZZZZZZZZZZZ")
    st.markdown("### Aplikasi ini menunjukkan betapa besarnya cinta saya kepada Silvani.")


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
    with st.expander("Alasan Kenapa Aku Sayang Sama Kamu"):
        st.write("1. Kamu merupakan orang pertama yang sangat menyayangi ku dan aku sangat percaya itu karena kamu telah membuktikannya.")
        st.write("2. Kamu menerima aku apa adanya, padahall kamu tau background aku seperti apa, dan hal apa yang aku lakukan di masa lalu")
        st.write("3. Kamu telah memberikan aku pengalaman yang terbaik yang pernah aku rasakan sejak aku pertama kali muncul di bumi ini")
        if st.button("Coba Tekan"):
            floating_balloons('❤️')
            display_image('silvani1.jpeg')
            floating_balloons('❤️')

    with st.expander("Alasan Kenapa Kamu Harus Sayang Sama Aku"):
        st.write("Ajis Iku Setia Tenan: Ayang, kudu ngerti lho, Ajis iku wonge setia banget. Ora gampang mbok larani ati, lan mesthi ngajeni marang sliramu. Ajis kuwi koyo batu karang, teguh lan ora gampang oyak angin. Mula, yakinlah karo setiane Ajis, kaya sliramu yakin karo panase srengenge ing wayah awan.")
        st.write("Ajis Nggawe Ayang Ketawa: Ayang, elinga wektu-wektu Ajis nggawe sliramu ketawa ngakak? Ajis iku pinter nggawe suasana dadi cerah lan ngilangake kesusahanmu. Kaya dene dheweke iku pelawak pribadi kanggo sliramu, selalu ana kanggo nggawe sliramu mesem lan ngguyu seneng.")
        st.write("Ajis Ngerti Carane Ngrawat Ayang kanthi Apik: Paling penting, Ajis ngerti carane ngrawat Ayang kanthi apik tenan. Ora mung masalah materi, nanging uga perhatian lan kasih sayang. Ajis iku kaya kunang-kunang ing bengi, dadi penerang lan pemandu ing wektu petengmu. Dadi, aja lali ngurmati lan njaga wong sing wis ngasih perhatian luwih marang sliramu, Ayang.")
        if st.button("Jangan Lupa Ditekan dek"):
            floating_balloons('🦒')
            display_image('silvani3.jpeg')
            floating_balloons('🦒')

    with st.expander("Doa Untuk Kamu Yang Tersayang"):
        st.write("Keselamatan lan Kabahagiaan: Mugi Gusti Allah paring keselamatan lan kabahagiaan kanggo Silvani. Kayadene lagu saka Bob Marley, 'Don't worry about a thing, cause every little thing gonna be alright', muga saben dina sing dilakoni dadi luwih cerah lan mawa kedamaian hati.")
        st.write("Kekuatan lan Ketabahan: Ning umur 20 taun, mugi Silvani diwenehi kekuatan lan ketabahan kanggo ngadhepi urip. Seperti tembang Bob Marley, 'You never know how strong you are, until being strong is your only choice', muga Silvani dadi wong sing kuat lan tansah ngadhepi masalah kanthi tabah.")
        st.write("Kasucian lan Kecerdasan Hati: Mugi ing taun iki lan taun-taun mendatang, Silvani diberkahi dengan kasucian hati lan kecerdasan kanggo nggawe pilihan sing tepat. Muga kaya pesen Bob Marley, 'The greatness of a man is not in how much wealth he acquires, but in his integrity and his ability to affect those around him positively', Silvani bisa dadi inspirasi kanggo wong-wong sekitare.")

        if st.button("I Love You Soo Much ❤️"):
            floating_balloons('♡')
            display_image('silfani2.jpeg')
            floating_balloons('♡')



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
