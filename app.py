import os
import streamlit as st
import google.generativeai as genai
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

# ============================================
# KONFIGURASI HALAMAN
# ============================================
st.set_page_config(
    page_title='Bali Fiber AI Assistant',
    page_icon='🤖',
    layout='wide',
    initial_sidebar_state='collapsed'
)

# ============================================
# CUSTOM CSS
# ============================================
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #000000 0%, #0A0A0A 40%, #111111 100%);
    color: white;
}
.block-container { padding-top: 2rem; padding-bottom: 2rem; }
.main-title {
    font-size: 42px; font-weight: 800;
    background: linear-gradient(90deg, #FF8C00, #FFA733, #FFD27A);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    margin-bottom: 5px; text-align: center; letter-spacing: 1px;
}
.subtitle { font-size: 18px; color: #B8C1EC; margin-bottom: 35px; text-align: center; }
.section-title { font-size: 28px; font-weight: 700; margin: 25px 0; color: #FFB347; text-align: center; }
.footer { text-align: center; color: #7F8DB0; margin-top: 50px; font-size: 14px; }
.result-box {
    background: rgba(20,20,20,0.85); backdrop-filter: blur(12px);
    border: 1px solid #FF8C00; box-shadow: 0 8px 25px rgba(0,0,0,0.4);
}
div.stButton > button {
    width: 100%; height: 70px; border-radius: 16px;
    border: 1px solid #FF8C00;
    background: linear-gradient(145deg, #121212, #1C1C1C);
    color: white; font-size: 16px; font-weight: 600;
    box-shadow: 0 4px 15px rgba(255,140,0,0.15); transition: 0.3s;
    margin-bottom: 15px;
}
div.stButton > button:hover {
    background: linear-gradient(145deg, #1F1F1F, #2C2C2C);
    border: 1px solid #FFA733;
    box-shadow: 0 6px 18px rgba(255,140,0,0.35);
    transform: translateY(-2px);
}
.stTextInput > div > div > input {
    background-color: #111111; color: white;
    border: 1px solid #FF8C00; border-radius: 14px;
    padding: 14px; font-size: 16px;
}
.streamlit-expanderHeader { border: 1px solid #FF8C00 !important; border-radius: 10px; }
@media (max-width: 768px) {
    .main-title { font-size: 30px; }
    .subtitle { font-size: 15px; }
    .section-title { font-size: 22px; }
    div.stButton > button { height: 65px; font-size: 14px; }
}
</style>
""", unsafe_allow_html=True)

# ============================================
# HEADER
# ============================================
st.markdown("""
<div class="main-title">Bali Fiber AI Assistant</div>
<div class="subtitle">
    Sistem AI berbasis RAG untuk analisis segmentasi pelanggan
    dan rekomendasi strategi bisnis Bali Fiber.
</div>
""", unsafe_allow_html=True)

# ============================================
# KONFIGURASI API KEY
# FIX: Baca dari environment variable, bukan hardcode
# ============================================
API_KEY = os.environ.get('GEMINI_API_KEY')

if not API_KEY:
    st.error('❌ GEMINI_API_KEY tidak ditemukan. Set environment variable sebelum menjalankan app.')
    st.stop()

genai.configure(api_key=API_KEY)

# ============================================
# MODEL GEMINI
# Menggunakan Gemini 2.5 Flash (stabil dan cepat)
# ============================================
model = genai.GenerativeModel('models/gemini-2.5-flash')

# ============================================
# LOAD EMBEDDING MODEL
# ============================================
@st.cache_resource
def load_embedding():
    return HuggingFaceEmbeddings(
        model_name='sentence-transformers/all-MiniLM-L6-v2'
    )

# ============================================
# LOAD VECTOR DATABASE
# ============================================
@st.cache_resource
def load_vectordb(_embedding_fn):
    return Chroma(
        persist_directory='cluster_db',
        embedding_function=_embedding_fn
    )

embedding_function = load_embedding()
vectordb = load_vectordb(embedding_function)
retriever = vectordb.as_retriever(search_kwargs={'k': 3})

# ============================================
# REKOMENDASI PERTANYAAN
# ============================================
st.markdown('<div class="section-title">💡 Rekomendasi Pertanyaan</div>', unsafe_allow_html=True)

questions = [
    ('📊 Cluster mana yang paling potensial?',      'Cluster mana yang paling potensial?'),
    ('⚠️ Cluster dengan risiko churn tertinggi?',   'Cluster dengan risiko churn tertinggi?'),
    ('👥 Cluster pelanggan aktif terbanyak?',        'Cluster mana yang memiliki pelanggan aktif terbanyak?'),
    ('📌 Apa karakteristik Cluster 0?',              'Apa karakteristik Cluster 0?'),
    ('🚀 Cluster prioritas untuk sales?',            'Cluster mana yang perlu diprioritaskan sales?'),
    ('📈 Cluster dengan performa terbaik?',          'Cluster dengan performa terbaik?'),
]

for i in range(0, len(questions), 2):
    col1, col2 = st.columns(2)
    with col1:
        label1, query1 = questions[i]
        if st.button(label1, key=f'btn_{i}'):
            st.session_state.query = query1
    with col2:
        if i + 1 < len(questions):
            label2, query2 = questions[i + 1]
            if st.button(label2, key=f'btn_{i+1}'):
                st.session_state.query = query2

# ============================================
# INPUT USER
# ============================================
query = st.text_input(
    '💬 Masukkan Pertanyaan:',
    value=st.session_state.get('query', ''),
    placeholder='Contoh: Cluster mana yang paling berisiko churn?'
)

# ============================================
# VALIDASI KATA KUNCI
# ============================================
allowed_keywords = [
    'cluster', 'pelanggan', 'sales', 'segmentasi',
    'churn', 'potensial', 'retensi', 'strategi',
    'aktif', 'bali fiber', 'performa'
]

# ============================================
# PROSES RAG
# ============================================
if query:
    if not any(kw in query.lower() for kw in allowed_keywords):
        st.warning('⚠️ Pertanyaan di luar konteks Business Insight Bali Fiber.')
        st.info('Silakan ajukan pertanyaan terkait cluster pelanggan, strategi bisnis, sales, atau segmentasi.')
    else:
        with st.spinner('🔍 AI sedang menganalisis data cluster...'):
            try:
                docs = retriever.invoke(query)
                context = '\n'.join([doc.page_content for doc in docs])
                prompt = f"""
                Kamu adalah AI Business Analyst Bali Fiber.
                Gunakan context berikut untuk menjawab pertanyaan user.
                Context:
                {context}
                Pertanyaan:
                {query}
                Berikan:
                1. Insight bisnis
                2. Analisis cluster
                3. Rekomendasi strategi
                """
                response = model.generate_content(prompt)
                hasil_ai = response.text
            except Exception as e:
                context = 'Data cluster sementara tidak tersedia.'
                st.warning(f'⚠️ Error: {e}')
                hasil_ai = ''

        if hasil_ai:
            st.markdown('## 📊 Hasil Analisis AI')
            st.write(hasil_ai)
            with st.expander('📁 Lihat Context Retrieval'):
                for i, doc in enumerate(docs):
                    st.markdown(f'### Cluster Retrieval {i+1}')
                    st.write(doc.page_content)

# ============================================
# FOOTER
# ============================================
st.markdown(
    '<div class="footer">Developed using K-Prototypes Clustering + RAG + Gemini LLM</div>',
    unsafe_allow_html=True
)
