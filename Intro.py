import streamlit as st
from PIL import Image, ImageOps

st.set_page_config(
    page_title="Portafolio Salomé Marín Pérez",
    layout="wide"
)

# ---------- ESTILO ----------
st.markdown("""
<style>
.stApp {
    background-color: #fbf8fc;
}

.main-title {
    text-align: center;
    font-size: 38px;
    font-weight: 600;
    color: #2f1c3f;
}

.subtitle {
    text-align: center;
    color: #7b5e8e;
    margin-bottom: 30px;
}

.card {
    background: white;
    border-radius: 14px;
    padding: 16px;
    border: 1px solid #eee;
    margin-bottom: 22px;
}

.btn {
    display: inline-block;
    margin-top: 10px;
    padding: 7px 14px;
    border-radius: 20px;
    background: #7e57c2;
    color: white !important;
    font-size: 13px;
    text-decoration: none;
}

.btn:hover {
    background: #673ab7;
}
</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown('<div class="main-title">Portafolio Salomé Marín Pérez</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Trabajos de este semestre</div>', unsafe_allow_html=True)

# ---------- FUNCIÓN TARJETA ----------
def card(titulo, img, url):
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.markdown(f"**{titulo}**")

    image = Image.open(img)
    image = ImageOps.fit(image, (350, 250), Image.Resampling.LANCZOS)
    st.image(image)

    st.markdown(f'<a class="btn" href="{url}" target="_blank">Abrir aplicación</a>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# ---------- COLUMNAS ----------
col1, col2, col3 = st.columns(3, gap="large")

# -------- COLUMNA 1 --------
with col1:
    card("App 1", "txt_to_audio2.png", "https://aplicaci-n-de-salome-marin-perez.streamlit.app/")
    card("App 2", "txt_to_audio.png", "https://appsalomemp.streamlit.app/")
    card("App 3", "OIG5.jpg", "https://chatpdf-salo.streamlit.app/")
    card("App 4", "OIG8.jpg", "https://drawrecogsalomarin.streamlit.app/")
    card("App 5", "data_analisis.png", "https://ctrlvoicesalo-axj7kmtf9qtbrfzxbyxsck.streamlit.app/")
    card("App 6", "OIG3.jpg", "https://copiaimm.streamlit.app/")
    card("App 7", "Chat_pdf.png", "https://handwsalome.streamlit.app/")

# -------- COLUMNA 2 --------
with col2:
    card("App 8", "OIG4.jpg", "https://salomemiintroduccion.streamlit.app/")
    card("App 9", "OIG6.jpg", "https://imagentextosalo.streamlit.app/")
    card("App 10", "txt_to_audio2.png", "https://ultimosalo.streamlit.app/")
    card("App 11", "txt_to_audio.png", "https://recepmqtt-salomemarin.streamlit.app/")
    card("App 12", "OIG5.jpg", "https://copiaprofesor.streamlit.app/")
    card("App 13", "OIG8.jpg", "https://copiadelprofe.streamlit.app/")
    card("App 14", "data_analisis.png", "https://tmsalo-afcwbpgkoxc82lahec4b9n.streamlit.app/")

# -------- COLUMNA 3 --------
with col3:
    card("App 15", "OIG3.jpg", "https://djsiwdpcqxpmp45s57qhaa.streamlit.app/")
    card("App 16", "Chat_pdf.png", "https://sentimenta-easycvyxus9ampjgtfufnp.streamlit.app/")
    card("App 17", "OIG4.jpg", "https://sendcmqttsalox-i7hcxcyrjkonzfxgrmdkiw.streamlit.app/")
    card("App 18", "OIG6.jpg", "https://yolov5-rnepyipjc2tj2iywfdwnc6.streamlit.app/")
    card("App 19", "txt_to_audio2.png", "https://wordcloud-dhvplejtnquzsnxzb2fmq7.streamlit.app/")
    card("App 20", "txt_to_audio.png", "https://visionappsalo.streamlit.app/")
    card("App 21", "OIG5.jpg", "https://traductor-salomemarin.streamlit.app/")
