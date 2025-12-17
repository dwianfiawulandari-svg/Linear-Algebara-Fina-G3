import streamlit as st

# --- Fungsi Pembantu untuk Ekstraksi String Aman ---
# Fungsi ini mencoba mengambil teks di dalam kurung. 
# Jika kurung tidak ada (seperti pada bahasa Inggris), ia akan mengembalikan string kosong.
def extract_parentheses_content(header):
    """Mengekstrak konten di dalam tanda kurung pertama."""
    try:
        # Coba ambil konten antara '(' dan ')'
        return header.split('(')[1].split(')')[0]
    except IndexError:
        # Jika tidak ada '(' atau ')' yang cukup, kembalikan string kosong
        return ""

# Fungsi ini mencoba mengambil kata terakhir sebelum tanda kurung
def extract_last_word_before_paren(header):
    """Mengekstrak kata terakhir sebelum tanda kurung atau kata terakhir string."""
    try:
        # Pisahkan berdasarkan '(', lalu ambil bagian pertama, lalu ambil kata terakhir.
        return header.split('(')[0].strip().split(' ')[-1]
    except IndexError:
        # Jika ada masalah, kembalikan string kosong
        return ""


# --- 1. Definisi Teks Multilingual ---
TEXT = {
    "en": {
        "page_title": "Matrix Transformation Image Processor",
        "app_title": "Matrix Transformation Image Processor",
        "description_header": "🌟 Application Description",
        "description_lead": "Welcome to TransformMatrix! This multipage application is a comprehensive tool for exploring and applying fundamental image processing techniques using *matrix operations* and *convolution*.",
        "description_list": [
            "Visually see how various mathematical operations affect image pixels.",
            "Apply geometric transformations (e.g., rotation, scaling) and convolution filters (e.g., blur, sharpen, edge detection).",
            "Understand the concepts behind kernels and transformation matrices, which are central to modern graphics and computer vision algorithms."
        ],
        "geo_header": "📐 Understanding Matrix Transformations", # Dihilangkan (Geometric)
        "geo_text": "Matrix transformation is a method used to change the position and orientation of every pixel in an image. Each pixel point $P=(x, y)$ is multiplied by a Transformation Matrix $\mathbf{T}$ to get the new position $P'=(x', y')$.",
        "homogeneous_text": "In homogeneous coordinate representation, this is written as:",
        "conv_header": "💡 Matrix Convolution", # Dihilangkan (Convolution)
        "conv_text": "Convolution is a crucial operation for *filtering* and *feature extraction. A small matrix called the **Kernel* (or Filter) is 'slid' across every image pixel. At each position, pixel values under the kernel are multiplied by the corresponding kernel values, and the results are summed to get the new output pixel value. ",
        "sharpen_kernel": "Kernel for Sharpening",
        "edge_kernel": "Kernel for Edge Detection (Laplacian)",
        "cta_header": "🚀 Start Exploring",
        "cta_text_1": "Use the navigation menu on the left (sidebar) to move to the processing pages:",
        "cta_text_2": "* *Geometric Transformations:* To change the position, rotation, and scaling of the image.",
        "cta_text_3": "* *Convolution Filters:* To apply filtering effects like blur, sharpen, and edge detection.",
        "cta_end": "*Happy Experimenting!*",
        "select_lang": "Language / Bahasa",
        "transform_types": {
            "Translation": "Translation (Shifting)",
            "Rotation": "Rotation",
            "Scaling": "Scaling",
            "Shearing": "Shearing"
        },
        "sidebar_success": "Select a page above to start."
    },
    "id": {
        "page_title": "Pemroses Gambar Transformasi Matriks",
        "app_title": "Pemroses Gambar Transformasi Matriks",
        "description_header": "🌟 Deskripsi Aplikasi",
        "description_lead": "Selamat datang di TransformMatrix! Aplikasi multipage ini adalah alat komprehensif untuk eksplorasi dan aplikasi teknik pemrosesan gambar fundamental menggunakan *operasi matriks* dan *konvolusi*.",
        "description_list": [
            "Melihat secara langsung bagaimana berbagai operasi matematika memengaruhi piksel gambar.",
            "Menerapkan transformasi geometris (misalnya, rotasi, skala) dan filter konvolusi (misalnya, blur, sharpen, pendeteksi tepi).",
            "Memahami konsep di balik kernel dan transformation matrix yang menjadi inti dari banyak algoritma grafis dan visi komputer modern."
        ],
        "geo_header": "📐 Pemahaman Transformasi Matriks (Geometric Transformations)",
        "geo_text": "Transformasi matriks adalah metode yang digunakan untuk mengubah posisi dan orientasi setiap piksel dalam gambar (seolah-olah gambar adalah objek dalam ruang 2D). Setiap titik piksel $P=(x, y)$ dikalikan dengan sebuah Transformation Matrix $\mathbf{T}$ untuk mendapatkan posisi baru $P'=(x', y')$. ",
        "homogeneous_text": "Dalam representasi koordinat homogen, ini ditulis sebagai:",
        "conv_header": "💡 Konvolusi Matriks (Convolution)",
        "conv_text": "Konvolusi adalah operasi yang sangat penting untuk *pemfilteran* dan *ekstraksi fitur* gambar. Sebuah matriks kecil yang disebut *Kernel* (atau Filter) 'menggeser' melintasi setiap piksel gambar. Pada setiap posisi, nilai piksel di bawah kernel dikalikan dengan nilai yang sesuai dalam kernel, dan hasilnya dijumlahkan untuk mendapatkan nilai piksel baru pada gambar keluaran. ",
        "sharpen_kernel": "Kernel untuk Sharpening",
        "edge_kernel": "Kernel untuk Edge Detection (Laplacian)",
        "cta_header": "🚀 Mulai Eksplorasi",
        "cta_text_1": "Gunakan menu navigasi di sisi kiri (sidebar) untuk berpindah ke halaman pemrosesan yang Anda inginkan:",
        "cta_text_2": "* *Geometric Transformations:* Untuk mengubah posisi, rotasi, dan skala gambar.",
        "cta_text_3": "* *Convolution Filters:* Untuk menerapkan efek pemfilteran seperti blur, sharpen, dan pendeteksi tepi.",
        "cta_end": "*Selamat Bereksperimen!*",
        "select_lang": "Pilih Bahasa",
        "transform_types": {
            "Translation": "Translasi (Pergeseran)",
            "Rotation": "Rotasi",
            "Scaling": "Penskalaan (Scaling)",
            "Shearing": "Pencerminan (Shearing)"
        },
        "sidebar_success": "Pilih halaman di atas untuk memulai."
    }
}

# --- Style Customization (CSS) ---
st.markdown("""
<style>
/* Style Neon untuk Judul Utama */
.neon-title-h1 {
    color: #00FFD1; /* Warna hijau kebiruan neon */
    font-size: 2.5em;
    font-weight: bold;
    text-shadow: 0 0 5px #00FFD1, 0 0 10px #00FFD1;
    margin-bottom: 0;
}

/* Style Box untuk Teks Lead */
.neon-box {
    background-color: #0D2638; /* Latar belakang gelap */
    border: 1px solid #00FFD1; /* Border neon */
    padding: 15px;
    border-radius: 8px;
    margin-bottom: 20px;
}

/* Mengubah style st.info() untuk transformasi */
div[data-testid="stInfo"] {
    background-color: #0D2638; 
    border-left: 5px solid #00FFD1; 
    padding: 10px;
    border-radius: 5px;
}
</style>
""", unsafe_allow_html=True)


# --- 2. Language Selection and State Management ---
LANG_OPTIONS = {"English": "en", "Bahasa Indonesia": "id"}
lang_choice = st.sidebar.selectbox("Language / Bahasa", list(LANG_OPTIONS.keys()), 
                                 index=list(LANG_OPTIONS.keys()).index('Bahasa Indonesia'))
lang = LANG_OPTIONS[lang_choice]

# Panggil semua teks dengan mudah
T = TEXT[lang]

# --- Konfigurasi Halaman (Harus di awal) ---
st.set_page_config(
    page_title=T['page_title'],
    page_icon="🖼",
    layout="wide"
)

# --- Judul Aplikasi & Lead (Menggunakan custom HTML sesuai permintaan Anda) ---
# Judul Utama (Menggunakan class custom)
st.markdown(f"<h1 style='color:#00ffe1'>{T['app_title']}</h1>", unsafe_allow_html=True)

st.markdown("---")

# --- Deskripsi Aplikasi (Lanjutan) ---
st.header(T['description_header'])

# Menggunakan list dari dictionary T
st.markdown(T['description_lead'])
st.markdown("Berikut yang dapat Anda lakukan:")
for item in T['description_list']:
    st.markdown(f"* {item}")

st.markdown("---")

# --- Bagian 1: Transformasi Matriks (Geometric) ---
st.header(T['geo_header'])
st.markdown(T['geo_text'])


# Persamaan Transformasi
st.latex(r"P' = \mathbf{T} \cdot P")

st.markdown(T['homogeneous_text'])
st.latex(r"""
\begin{pmatrix} x' \\ y' \\ 1 \end{pmatrix}
=
\begin{pmatrix} a & b & t_x \\ c & d & t_y \\ 0 & 0 & 1 \end{pmatrix}
\cdot
\begin{pmatrix} x \\ y \\ 1 \end{pmatrix}
""")

# PERBAIKAN 1: Menggunakan fungsi pembantu untuk menangani header yang berbeda format.
geo_word = extract_last_word_before_paren(T['geo_header'])
geo_word_display = geo_word if geo_word else "Transformasi" # Fallback jika tidak ada kata
st.subheader(f"Contoh-Contoh {geo_word_display} Utama:")


# Menggunakan 4 kolom seperti di contoh
col1, col2, col3, col4 = st.columns(4)

# Menampilkan jenis-jenis transformasi dalam kolom dengan st.info()
with col1:
    st.info(f"{T['transform_types']['Translation']}")
    st.markdown("Memindahkan objek ke posisi baru.")

with col2:
    st.info(f"{T['transform_types']['Rotation']}")
    st.markdown("Memutar objek di sekitar titik tertentu.")

with col3:
    st.info(f"{T['transform_types']['Scaling']}")
    st.markdown("Mengubah ukuran objek.")

with col4:
    st.info(f"{T['transform_types']['Shearing']}")
    st.markdown("Memiringkan objek sepanjang satu sumbu.")


st.markdown("---")

# --- Bagian 2: Konvolusi Matriks (Convolution) ---
st.header(T['conv_header'])
st.markdown(T['conv_text'])

# PERBAIKAN 2: Menggunakan fungsi pembantu untuk menangani header yang berbeda format.
conv_paren_content = extract_parentheses_content(T['conv_header'])

if conv_paren_content:
    # Jika ada konten dalam kurung (Bahasa Indonesia)
    subheader_text = f"Contoh Kernel ({conv_paren_content} Matriks):"
else:
    # Jika tidak ada (Bahasa Inggris), gunakan nama yang sederhana.
    subheader_text = "Contoh Kernel (Convolution Matriks):"

st.subheader(subheader_text)


col_k1, col_k2 = st.columns(2)

with col_k1:
    st.markdown(f"{T['sharpen_kernel']}")
    st.code("""
    [[ 0, -1, 0],
     [-1, 5, -1],
     [ 0, -1, 0]]
    """)

with col_k2:
    st.markdown(f"{T['edge_kernel']}")
    st.code("""
    [[ 0, 1, 0],
     [ 1, -4, 1],
     [ 0, 1, 0]]
    """)

st.markdown("---")

# --- Ajakan Bertindak (Call to Action) ---
st.header(T['cta_header'])
st.markdown(T['cta_text_1'])
st.markdown(T['cta_text_2'])
st.markdown(T['cta_text_3'])
st.markdown(T['cta_end'])

# --- Tambahan untuk pengguna jika ini adalah file utama di struktur multipage ---
if _name_ == '_main_':
    st.sidebar.success(T['sidebar_success'])
