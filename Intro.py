import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Portafolio Salomé Marín Pérez",
    layout="wide"
)

# ESTILO LIMPIO Y LEGIBLE
st.markdown("""
<style>

/* Fondo suave */
.stApp {
    background: linear-gradient(180deg, #faf7fb, #f3e5f5);
}

/* Título */
h1 {
    text-align: center;
    color: #2d1b3d;
    font-weight: 600;
    margin-bottom: 0;
}

/* Subtítulos */
h3 {
    color: #3e2a52;
    font-weight: 500;
}

/* Texto */
p {
    color: #444;
    font-size: 14px;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #f7f2fa;
}

/* Tarjetas */
.card {
    background-color: white;
    border-radius: 12px;
    padding: 16px;
    margin-bottom: 18px;
    border: 1px solid #eee;
}

/* Botón simple */
.btn {
    display: inline-block;
    margin-top: 8px;
    padding: 6px 10px;
    border-radius: 6px;
    background-color: #6a4c93;
    color: white !important;
    font-size: 13px;
    text-decoration: none;
}

.btn:hover {
    background-color: #5a3e7c;
}

</style>
""", unsafe_allow_html=True)

# Título
st.title("Portafolio Salomé Marín Pérez")
st.write("")

# Sidebar
with st.sidebar:
    st.subheader("Aplicaciones de IA")
    st.write("Colección de aplicaciones desarrolladas con inteligencia artificial.")

# Link general
url_ia = "https://sites.google.com/view/aplicacionesdeia/inicio"
st.markdown(f'<a class="btn" href="{url_ia}" target="_blank">Ver contenido</a>', unsafe_allow_html=True)

st.write("")

# Columnas
col1, col2, col3 = st.columns(3)

# Función para mantener todo alineado
def card(titulo, img, desc, url):
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader(titulo)
    st.image(Image.open(img), use_column_width=True)
    st.write(desc)
    st.markdown(f'<a class="btn" href="{url}" target="_blank">Abrir</a>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

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
