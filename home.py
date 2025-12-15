import streamlit as st
from PIL import Image, ImageDraw, ImageFilter,ImageOps
import numpy as np
from numpy.lib.stride_tricks import sliding_window_view

# --- Language selection ---
LANG_OPTIONS = {"English": "en", "Bahasa Indonesia": "id"}
lang_choice = st.sidebar.selectbox("Language / Bahasa", list(LANG_OPTIONS.keys()), index=0)
lang = LANG_OPTIONS[lang_choice]

TEXT = {
    "en": {
        "title": "Matrix & Convolution Explorer",
        "lead": "This web application demonstrates basic 2D matrix transformations and convolution filters in image processing.",
        "matrix": "Matrix Transformations (Affine)",
        "matrix_desc": [
            "Rotation",
            "Scaling",
            "Translation",
            "Shear",
            "Flip"
        ],
        "conv": "Convolution",
        "conv_desc": "Convolution applies a kernel (small matrix) to extract features such as blur, edges, or sharpening.",
        "visual": "Visual Examples",
        "tip": "Go to Image Processing Tools to try interactive examples."
    },
    "id": {
        "title": "Matrix & Convolution Explorer",
        "lead": "Aplikasi web ini mendemonstrasikan transformasi matriks 2D dan filter konvolusi pada pengolahan citra.",
        "matrix": "Transformasi Matriks (Affine)",
        "matrix_desc": [
            "Rotasi",
            "Skala",
            "Translasi",
            "Shear",
            "Flip"
        ],
        "conv": "Konvolusi",
        "conv_desc": "Konvolusi menerapkan kernel (matriks kecil) untuk mengekstraksi fitur seperti blur, tepi, atau penajaman.",
        "visual": "Contoh Visual",
        "tip": "Buka halaman Image Processing Tools untuk mencoba contoh interaktif."
    }
}

def generate_demo(size=400):
    img = Image.new("RGB", (size, size), (10, 18, 30))
    draw = ImageDraw.Draw(img)

    step = size // 8
    for i in range(0, size, step):
        draw.line((i, 0, i, size), fill=(40, 60, 90))
        draw.line((0, i, size, i), fill=(40, 60, 90))

    return img

def render():
    t = TEXT[st.session_state.lang]

    st.markdown(f"<h1 style='color:#00ffe1'>{t['title']}</h1>", unsafe_allow_html=True)
    st.markdown(f"<div class='neon-box'>{t['lead']}</div>", unsafe_allow_html=True)

    st.subheader(t["matrix"])
    for item in t["matrix_desc"]:
        st.markdown(f"- {item}")

    st.subheader(t["conv"])
    st.markdown(t["conv_desc"])

    st.subheader(t["visual"])
    demo = generate_demo()
    edges = demo.convert("L").filter(ImageFilter.FIND_EDGES)

    col1, col2 = st.columns(2)
    with col1:
        st.caption("Original")
        st.image(demo, use_column_width=True)
    with col2:
        st.caption("Edge Detection")
        st.image(edges, use_column_width=True)

    st.info(t["tip"])