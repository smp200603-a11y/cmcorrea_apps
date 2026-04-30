import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Portafolio Salomé Marín Pérez",
    layout="wide"
)

# ---------- ESTILO FINO ----------
st.markdown("""
<style>

.stApp {
    background-color: #fbf8fc;
}

/* Título */
.main-title {
    text-align: center;
    font-size: 38px;
    font-weight: 600;
    color: #2f1c3f;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    color: #7b5e8e;
    margin-bottom: 30px;
}

/* Tarjetas */
.card {
    background: white;
    border-radius: 14px;
    padding: 16px;
    border: 1px solid #eee;
    margin-bottom: 22px;
    transition: 0.2s;
}

.card:hover {
    border: 1px solid #d1c4e9;
}

/* Botón */
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
st.markdown('<div class="subtitle">Aplicaciones de Inteligencia Artificial</div>', unsafe_allow_html=True)

# ---------- SIDEBAR ----------
with st.sidebar:
    st.markdown("### Información")
    st.write("Colección de aplicaciones desarrolladas con inteligencia artificial.")

# ---------- LINK PRINCIPAL ----------
url_ia = "https://sites.google.com/view/aplicacionesdeia/inicio"
st.markdown(f'<a class="btn" href="{url_ia}" target="_blank">Explorar contenido</a>', unsafe_allow_html=True)

st.write("")

# ---------- FUNCION TARJETA ----------
def card(titulo, img, desc, url):
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown(f"**{titulo}**")
    st.image(Image.open(img), use_column_width=True)
    st.write(desc)
    st.markdown(f'<a class="btn" href="{url}" target="_blank">Ver aplicación</a>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ---------- COLUMNAS ----------
col1, col2, col3 = st.columns(3, gap="large")

# Columna 1
with col1:
    card("Texto a voz", "txt_to_audio2.png", "Convierte texto en audio.", "https://imultimod.streamlit.app/")
    card("Reconocimiento de objetos", "txt_to_audio.png", "Detecta objetos en imágenes.", "https://yolov5cmc.streamlit.app/")
    card("Entrenamiento de modelos", "OIG5.jpg", "Uso de modelos entrenados.", "https://xn3pg24ztuv6fdiqon8qn3.streamlit.app/")

# Columna 2
with col2:
    card("Voz a texto", "OIG8.jpg", "Convierte voz en texto.", "https://traductorw.streamlit.app/")
    card("Análisis de datos", "data_analisis.png", "Análisis con IA.", "https://dataagente.streamlit.app/")
    card("Transcriptor", "OIG3.jpg", "Transcribe audio y video.", "https://transcript-whisper.streamlit.app/")

# Columna 3
with col3:
    card("Chat con PDF", "Chat_pdf.png", "Consulta documentos.", "https://chatpdf-cc.streamlit.app/")
    card("Análisis de imagen", "OIG4.jpg", "Procesa imágenes.", "https://vision2-gpt4o.streamlit.app/")
    card("Sistema ciberfísico", "OIG6.jpg", "Interacción con el entorno físico.", "https://vision2-gpt4o.streamlit.app/")
