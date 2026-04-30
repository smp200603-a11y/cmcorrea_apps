import streamlit as st
from PIL import Image

# Configuración de la página
st.set_page_config(
    page_title="Portafolio Salomé Marín Pérez",
    page_icon="💜",
    layout="wide"
)

# Estilos personalizados (rosado y morado)
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #f8bbd0, #e1bee7);
    }
    h1 {
        color: #6a1b9a;
        text-align: center;
    }
    h2, h3 {
        color: #8e24aa;
    }
    .stSidebar {
        background-color: #f3e5f5;
    }
    </style>
""", unsafe_allow_html=True)

# Título principal
st.title("💜 Portafolio Salomé Marín Pérez")

# Sidebar
with st.sidebar:
    st.subheader("Aplicaciones con Inteligencia Artificial")
    parrafo = (
        "La inteligencia artificial permite mejorar la toma de decisiones con el uso de datos, "
        "automatizar tareas rutinarias y proporcionar análisis avanzados en tiempo real, lo que "
        "resulta en una mayor eficiencia y precisión en diversos campos."
    )
    st.write(parrafo)

# Link general
url_ia = "https://sites.google.com/view/aplicacionesdeia/inicio"
st.subheader("Explora ejercicios y aplicaciones")
st.write(f"[Ir al contenido]({url_ia})")

# Columnas
col1, col2, col3 = st.columns(3)

# ----------- COLUMNA 1 -----------
with col1:

    st.subheader("🎤 Texto a Voz")
    image = Image.open('txt_to_audio2.png')
    st.image(image, width=190)
    st.write("Aplicación de conversión de texto a audio.")
    url = "https://imultimod.streamlit.app/"
    st.write(f"[Ir a la app]({url})")

    st.subheader("📦 Reconocimiento de Objetos")
    image = Image.open('txt_to_audio.png')
    st.image(image, width=200)
    st.write("Detección de objetos en imágenes.")
    url = "https://yolov5cmc.streamlit.app/"
    st.write(f"[Ir a la app]({url})")

    st.subheader("🧠 Entrenamiento de Modelos")
    image = Image.open('OIG5.jpg')
    st.image(image, width=200)
    st.write("Uso de modelos entrenados.")
    url = "https://xn3pg24ztuv6fdiqon8qn3.streamlit.app/"
    st.write(f"[Ir a la app]({url})")


# ----------- COLUMNA 2 -----------
with col2:

    st.subheader("🗣️ Voz a Texto")
    image = Image.open('OIG8.jpg')
    st.image(image, width=200)
    st.write("Conversión de voz a texto.")
    url = "https://traductorw.streamlit.app/"
    st.write(f"[Ir a la app]({url})")

    st.subheader("📊 Análisis de Datos")
    image = Image.open('data_analisis.png')
    st.image(image, width=190)
    st.write("Análisis de datos con IA.")
    url = "https://dataagente.streamlit.app/"
    st.write(f"[Ir a la app]({url})")

    st.subheader("🎧 Transcriptor")
    image = Image.open('OIG3.jpg')
    st.image(image, width=200)
    st.write("Transcripción de audio y video.")
    url = "https://transcript-whisper.streamlit.app/"
    st.write(f"[Ir a la app]({url})")


# ----------- COLUMNA 3 -----------
with col3:

    st.subheader("📄 Chat con PDF (RAG)")
    image = Image.open('Chat_pdf.png')
    st.image(image, width=190)
    st.write("Consulta documentos PDF con IA.")
    url = "https://chatpdf-cc.streamlit.app/"
    st.write(f"[Ir a la app]({url})")

    st.subheader("🖼️ Análisis de Imagen")
    image = Image.open('OIG4.jpg')
    st.image(image, width=200)
    st.write("Análisis inteligente de imágenes.")
    url = "https://vision2-gpt4o.streamlit.app/"
    st.write(f"[Ir a la app]({url})")

    st.subheader("🤖 Sistema Ciberfísico")
    image = Image.open('OIG6.jpg')
    st.image(image, width=200)
    st.write("Interacción con el mundo físico.")
    url = "https://vision2-gpt4o.streamlit.app/"
    st.write(f"[Ir a la app]({url})")
