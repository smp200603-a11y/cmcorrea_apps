import streamlit as st
from PIL import Image

# Configuración
st.set_page_config(
    page_title="Portafolio Salomé Marín Pérez",
    page_icon="💜",
    layout="wide"
)

# Fondo y estilos reales visibles
st.markdown("""
<style>
.stApp {
    background-color: #fce4ec;
}

.card {
    background-color: #f3e5f5;
    padding: 15px;
    border-radius: 15px;
    margin-bottom: 20px;
    box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
}

h1 {
    color: #6a1b9a;
    text-align: center;
}

h3 {
    color: #8e24aa;
}
</style>
""", unsafe_allow_html=True)

# Título
st.title("💜 Portafolio Salomé Marín Pérez")

# Sidebar
with st.sidebar:
    st.subheader("Aplicaciones con IA")
    st.write(
        "La inteligencia artificial permite mejorar la toma de decisiones, "
        "automatizar tareas y analizar datos en tiempo real."
    )

# Link general
url_ia = "https://sites.google.com/view/aplicacionesdeia/inicio"
st.write(f"[Ir al contenido general]({url_ia})")

# Columnas
col1, col2, col3 = st.columns(3)

# -------- COLUMNA 1 --------
with col1:

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🎤 Texto a Voz")
    st.image(Image.open('txt_to_audio2.png'), width=190)
    st.write("Convierte texto en audio.")
    st.write("[Ir a la app](https://imultimod.streamlit.app/)")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📦 Reconocimiento de Objetos")
    st.image(Image.open('txt_to_audio.png'), width=200)
    st.write("Detecta objetos en imágenes.")
    st.write("[Ir a la app](https://yolov5cmc.streamlit.app/)")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🧠 Entrenamiento de Modelos")
    st.image(Image.open('OIG5.jpg'), width=200)
    st.write("Uso de modelos entrenados.")
    st.write("[Ir a la app](https://xn3pg24ztuv6fdiqon8qn3.streamlit.app/)")
    st.markdown('</div>', unsafe_allow_html=True)


# -------- COLUMNA 2 --------
with col2:

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🗣️ Voz a Texto")
    st.image(Image.open('OIG8.jpg'), width=200)
    st.write("Convierte voz en texto.")
    st.write("[Ir a la app](https://traductorw.streamlit.app/)")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📊 Análisis de Datos")
    st.image(Image.open('data_analisis.png'), width=190)
    st.write("Analiza datos con IA.")
    st.write("[Ir a la app](https://dataagente.streamlit.app/)")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🎧 Transcriptor")
    st.image(Image.open('OIG3.jpg'), width=200)
    st.write("Transcribe audio y video.")
    st.write("[Ir a la app](https://transcript-whisper.streamlit.app/)")
    st.markdown('</div>', unsafe_allow_html=True)


# -------- COLUMNA 3 --------
with col3:

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📄 Chat con PDF")
    st.image(Image.open('Chat_pdf.png'), width=190)
    st.write("Consulta PDFs con IA.")
    st.write("[Ir a la app](https://chatpdf-cc.streamlit.app/)")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🖼️ Análisis de Imagen")
    st.image(Image.open('OIG4.jpg'), width=200)
    st.write("Analiza imágenes.")
    st.write("[Ir a la app](https://vision2-gpt4o.streamlit.app/)")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🤖 Sistema Ciberfísico")
    st.image(Image.open('OIG6.jpg'), width=200)
    st.write("Interacción con el mundo físico.")
    st.write("[Ir a la app](https://vision2-gpt4o.streamlit.app/)")
    st.markdown('</div>', unsafe_allow_html=True)
