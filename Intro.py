import streamlit as st
from PIL import Image

# Configuración
st.set_page_config(
    page_title="Portafolio Salomé Marín Pérez",
    page_icon="💜",
    layout="wide"
)

# Estilos mejorados
st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #f8bbd0, #ce93d8);
}

/* Título */
h1 {
    color: #4a148c;
    text-align: center;
    font-weight: bold;
}

/* Subtítulos */
h3 {
    color: #6a1b9a;
}

/* Texto normal */
p {
    color: #2c2c2c;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #f3e5f5;
}

/* Tarjetas */
.card {
    background-color: white;
    padding: 18px;
    border-radius: 12px;
    margin-bottom: 20px;
    height: 100%;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
}

/* Links */
a {
    color: #8e24aa;
    font-weight: 500;
    text-decoration: none;
}

a:hover {
    text-decoration: underline;
}

</style>
""", unsafe_allow_html=True)

# Título
st.title("Portafolio Salomé Marín Pérez")

# Sidebar
with st.sidebar:
    st.subheader("Aplicaciones con Inteligencia Artificial")
    st.write(
        "La inteligencia artificial permite mejorar la toma de decisiones, "
        "automatizar tareas y analizar datos en tiempo real."
    )

# Link general
url_ia = "https://sites.google.com/view/aplicacionesdeia/inicio"
st.write(f"[Explorar contenido]({url_ia})")

# Columnas
col1, col2, col3 = st.columns(3)

# -------- COLUMNA 1 --------
with col1:

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Conversión de texto a voz")
    st.image(Image.open('txt_to_audio2.png'), use_column_width=True)
    st.write("Convierte texto en audio.")
    st.write("[Ir a la aplicación](https://imultimod.streamlit.app/)")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Reconocimiento de objetos")
    st.image(Image.open('txt_to_audio.png'), use_column_width=True)
    st.write("Detecta objetos en imágenes.")
    st.write("[Ir a la aplicación](https://yolov5cmc.streamlit.app/)")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Entrenamiento de modelos")
    st.image(Image.open('OIG5.jpg'), use_column_width=True)
    st.write("Uso de modelos entrenados.")
    st.write("[Ir a la aplicación](https://xn3pg24ztuv6fdiqon8qn3.streamlit.app/)")
    st.markdown('</div>', unsafe_allow_html=True)


# -------- COLUMNA 2 --------
with col2:

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Conversión de voz a texto")
    st.image(Image.open('OIG8.jpg'), use_column_width=True)
    st.write("Convierte voz en texto.")
    st.write("[Ir a la aplicación](https://traductorw.streamlit.app/)")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Análisis de datos")
    st.image(Image.open('data_analisis.png'), use_column_width=True)
    st.write("Analiza datos con inteligencia artificial.")
    st.write("[Ir a la aplicación](https://dataagente.streamlit.app/)")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Transcriptor de audio y video")
    st.image(Image.open('OIG3.jpg'), use_column_width=True)
    st.write("Transcribe contenido multimedia.")
    st.write("[Ir a la aplicación](https://transcript-whisper.streamlit.app/)")
    st.markdown('</div>', unsafe_allow_html=True)


# -------- COLUMNA 3 --------
with col3:

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Generación en contexto (RAG)")
    st.image(Image.open('Chat_pdf.png'), use_column_width=True)
    st.write("Consulta documentos PDF con IA.")
    st.write("[Ir a la aplicación](https://chatpdf-cc.streamlit.app/)")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Análisis de imagen")
    st.image(Image.open('OIG4.jpg'), use_column_width=True)
    st.write("Análisis inteligente de imágenes.")
    st.write("[Ir a la aplicación](https://vision2-gpt4o.streamlit.app/)")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Sistema ciberfísico")
    st.image(Image.open('OIG6.jpg'), use_column_width=True)
    st.write("Interacción con el mundo físico.")
    st.write("[Ir a la aplicación](https://vision2-gpt4o.streamlit.app/)")
    st.markdown('</div>', unsafe_allow_html=True)
