import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Portafolio Salomé Marín Pérez",
    layout="wide"
)

# Título
st.markdown(
    "<h1 style='text-align:center; color:#4a2c5a;'>Portafolio Salomé Marín Pérez</h1>",
    unsafe_allow_html=True
)

st.write("")

# Sidebar
with st.sidebar:
    st.markdown("### Aplicaciones de IA")
    st.write(
        "Portafolio de aplicaciones desarrolladas con inteligencia artificial."
    )

# Link principal
url_ia = "https://sites.google.com/view/aplicacionesdeia/inicio"
st.markdown(f"[Ver contenido general]({url_ia})")

st.divider()

# Función simple y bonita (sin CSS raro)
def card(titulo, img, desc, url):
    st.subheader(titulo)
    st.image(Image.open(img), use_column_width=True)
    st.write(desc)
    st.markdown(f"[Abrir aplicación]({url})")
    st.write("---")  # separador limpio

# Columnas
col1, col2, col3 = st.columns(3)

# Columna 1
with col1:
    card("Texto a voz", "txt_to_audio2.png",
         "Convierte texto en audio.",
         "https://imultimod.streamlit.app/")

    card("Reconocimiento de objetos", "txt_to_audio.png",
         "Detecta objetos en imágenes.",
         "https://yolov5cmc.streamlit.app/")

    card("Entrenamiento de modelos", "OIG5.jpg",
         "Uso de modelos entrenados.",
         "https://xn3pg24ztuv6fdiqon8qn3.streamlit.app/")

# Columna 2
with col2:
    card("Voz a texto", "OIG8.jpg",
         "Convierte voz en texto.",
         "https://traductorw.streamlit.app/")

    card("Análisis de datos", "data_analisis.png",
         "Análisis con IA.",
         "https://dataagente.streamlit.app/")

    card("Transcriptor", "OIG3.jpg",
         "Transcribe audio y video.",
         "https://transcript-whisper.streamlit.app/")

# Columna 3
with col3:
    card("Chat con PDF", "Chat_pdf.png",
         "Consulta documentos.",
         "https://chatpdf-cc.streamlit.app/")

    card("Análisis de imagen", "OIG4.jpg",
         "Procesa imágenes.",
         "https://vision2-gpt4o.streamlit.app/")

    card("Sistema ciberfísico", "OIG6.jpg",
         "Interacción con el entorno físico.",
         "https://vision2-gpt4o.streamlit.app/")
