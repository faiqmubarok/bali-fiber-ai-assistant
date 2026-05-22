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
    page_icon='🔷',
    layout='wide',
    initial_sidebar_state='collapsed'
)

# ============================================
# CUSTOM CSS - MODERN AI SAAS DESIGN
# ============================================
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Global Styles */
    * {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    /* Main App Background */
    .stApp {
        background: linear-gradient(135deg, #0f0f1e 0%, #1a1a2e 50%, #16213e 100%);
    }
    
    /* Hide Streamlit Branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Main Container */
    .block-container {
        padding: 2rem 3rem 3rem 3rem;
        max-width: 1400px;
    }
    
    /* Hero Section */
    .hero-section {
        text-align: center;
        padding: 3rem 0 2rem 0;
        margin-bottom: 2rem;
    }
    
    .hero-title {
        font-size: 2.75rem;
        font-weight: 700;
        background: linear-gradient(135deg, #ff6b35 0%, #f7931e 50%, #fbb034 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 0.5rem;
        letter-spacing: -0.02em;
    }
    
    .hero-subtitle {
        font-size: 1.125rem;
        color: #a0aec0;
        font-weight: 400;
        line-height: 1.6;
        max-width: 700px;
        margin: 0 auto;
    }
    
    /* Section Headers */
    .section-header {
        font-size: 1.25rem;
        font-weight: 600;
        color: #e2e8f0;
        margin: 2rem 0 1rem 0;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    /* Card Styles */
    .card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 16px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        transition: all 0.3s ease;
    }
    
    .card:hover {
        background: rgba(255, 255, 255, 0.05);
        border-color: rgba(255, 107, 53, 0.3);
        transform: translateY(-2px);
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.2);
    }
    
    /* Button Styles */
    .stButton > button {
        width: 100%;
        height: 3.5rem;
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        color: #e2e8f0;
        font-size: 0.95rem;
        font-weight: 500;
        transition: all 0.3s ease;
        cursor: pointer;
        margin-bottom: 0.75rem;
    }
    
    .stButton > button:hover {
        background: rgba(255, 107, 53, 0.15);
        border-color: rgba(255, 107, 53, 0.4);
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(255, 107, 53, 0.25);
    }
    
    .stButton > button:active {
        transform: translateY(0);
    }
    
    /* Input Styles */
    .stTextInput > div > div > input {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        color: #e2e8f0;
        font-size: 0.95rem;
        padding: 0.875rem 1rem;
        transition: all 0.3s ease;
    }
    
    .stTextInput > div > div > input:focus {
        background: rgba(255, 255, 255, 0.08);
        border-color: rgba(255, 107, 53, 0.5);
        box-shadow: 0 0 0 3px rgba(255, 107, 53, 0.1);
    }
    
    .stTextInput > div > div > input::placeholder {
        color: #718096;
    }
    
    .stTextInput > label {
        color: #cbd5e0;
        font-weight: 500;
        font-size: 0.875rem;
        margin-bottom: 0.5rem;
    }
    
    /* Result Card */
    .result-card {
        background: linear-gradient(135deg, rgba(255, 107, 53, 0.1) 0%, rgba(247, 147, 30, 0.1) 100%);
        border: 1px solid rgba(255, 107, 53, 0.25);
        border-radius: 16px;
        padding: 2rem;
        margin: 2rem 0;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
    }
    
    .result-title {
        font-size: 1.5rem;
        font-weight: 600;
        color: #e2e8f0;
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
        gap: 0.75rem;
    }
    
    .result-content {
        color: #cbd5e0;
        line-height: 1.8;
        font-size: 1rem;
    }
    
    /* Expander Styles */
    .streamlit-expanderHeader {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 12px;
        color: #cbd5e0;
        font-weight: 500;
        padding: 1rem;
    }
    
    .streamlit-expanderHeader:hover {
        background: rgba(255, 255, 255, 0.05);
        border-color: rgba(255, 107, 53, 0.3);
    }
    
    .streamlit-expanderContent {
        background: rgba(255, 255, 255, 0.02);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-top: none;
        border-radius: 0 0 12px 12px;
        padding: 1.5rem;
    }
    
    /* Alert Styles */
    .stAlert {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        padding: 1rem 1.25rem;
        color: #cbd5e0;
    }
    
    /* Warning */
    div[data-baseweb="notification"] {
        background: rgba(251, 191, 36, 0.1);
        border: 1px solid rgba(251, 191, 36, 0.3);
        border-radius: 12px;
    }
    
    /* Info */
    .stInfo {
        background: rgba(59, 130, 246, 0.1);
        border: 1px solid rgba(59, 130, 246, 0.3);
    }
    
    /* Error */
    .stError {
        background: rgba(239, 68, 68, 0.1);
        border: 1px solid rgba(239, 68, 68, 0.3);
    }
    
    /* Success */
    .stSuccess {
        background: rgba(34, 197, 94, 0.1);
        border: 1px solid rgba(34, 197, 94, 0.3);
    }
    
    /* Spinner */
    .stSpinner > div {
        border-color: rgba(255, 107, 53, 0.3);
        border-top-color: #ff6b35;
    }
    
    /* Grid Layout for Buttons */
    .button-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 1rem;
        margin: 1.5rem 0;
    }
    
    /* Markdown Content */
    .markdown-text-container {
        color: #cbd5e0;
        line-height: 1.8;
    }
    
    /* Scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
        height: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: rgba(255, 255, 255, 0.02);
    }
    
    ::-webkit-scrollbar-thumb {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: rgba(255, 255, 255, 0.15);
    }
    
    /* Footer */
    .footer {
        text-align: center;
        color: #718096;
        font-size: 0.875rem;
        margin-top: 4rem;
        padding-top: 2rem;
        border-top: 1px solid rgba(255, 255, 255, 0.05);
    }
    
    /* Responsive Design */
    @media (max-width: 768px) {
        .hero-title {
            font-size: 2rem;
        }
        
        .hero-subtitle {
            font-size: 1rem;
        }
        
        .block-container {
            padding: 1.5rem 1rem;
        }
        
        .stButton > button {
            height: 3rem;
            font-size: 0.875rem;
        }
        
        .button-grid {
            grid-template-columns: 1fr;
        }
    }
</style>
""", unsafe_allow_html=True)

# ============================================
# HEADER / HERO SECTION
# ============================================
st.markdown("""
<div class="hero-section">
    <div class="hero-title">Bali Fiber AI Assistant</div>
    <div class="hero-subtitle">
        Advanced customer segmentation analysis powered by RAG technology and Gemini AI.
        Get actionable business insights from your cluster data.
    </div>
</div>
""", unsafe_allow_html=True)

# ============================================
# KONFIGURASI API KEY
# ============================================
API_KEY = os.environ.get('GEMINI_API_KEY')

if not API_KEY:
    st.error('API key not found. Please configure GEMINI_API_KEY in your environment.')
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
    """Load embedding model (cached for performance)"""
    return HuggingFaceEmbeddings(
        model_name='sentence-transformers/all-MiniLM-L6-v2'
    )

# ============================================
# LOAD VECTOR DATABASE
# ============================================
@st.cache_resource
def load_vectordb(_embedding_fn):
    """Load pre-processed vector database (cached for performance)"""
    try:
        vectordb = Chroma(
            persist_directory='cluster_db',
            embedding_function=_embedding_fn
        )
        return vectordb
    except Exception as e:
        st.error(f'Failed to load vector database: {e}')
        st.info('Please run: python process_data.py to generate the database.')
        st.stop()

# Initialize embedding and vector database
with st.spinner('Loading AI models...'):
    embedding_function = load_embedding()
    vectordb = load_vectordb(embedding_function)
    retriever = vectordb.as_retriever(search_kwargs={'k': 3})

# ============================================
# REKOMENDASI PERTANYAAN
# ============================================
st.markdown('<div class="section-header">Suggested Questions</div>', unsafe_allow_html=True)

questions = [
    ('Which cluster has the highest potential?', 'Cluster mana yang paling potensial?'),
    ('Which cluster has the highest churn risk?', 'Cluster dengan risiko churn tertinggi?'),
    ('Which cluster has the most active customers?', 'Cluster mana yang memiliki pelanggan aktif terbanyak?'),
    ('What are the characteristics of Cluster 0?', 'Apa karakteristik Cluster 0?'),
    ('Which cluster should sales prioritize?', 'Cluster mana yang perlu diprioritaskan sales?'),
    ('Which cluster has the best performance?', 'Cluster dengan performa terbaik?'),
]

# Create 2-column grid for buttons
col1, col2 = st.columns(2)

for i, (label, query) in enumerate(questions):
    with col1 if i % 2 == 0 else col2:
        if st.button(label, key=f'btn_{i}', use_container_width=True):
            st.session_state.query = query

# ============================================
# INPUT USER
# ============================================
st.markdown('<div class="section-header">Ask a Question</div>', unsafe_allow_html=True)

query = st.text_input(
    'Enter your question about customer clusters',
    value=st.session_state.get('query', ''),
    placeholder='Example: Which cluster is most at risk of churn?',
    label_visibility='collapsed'
)

# ============================================
# VALIDASI KATA KUNCI
# ============================================
allowed_keywords = [
    'cluster', 'pelanggan', 'customer', 'sales', 'segmentasi', 'segmentation',
    'churn', 'potensial', 'potential', 'retensi', 'retention', 'strategi', 'strategy',
    'aktif', 'active', 'bali fiber', 'performa', 'performance', 'risk', 'risiko',
    'characteristics', 'karakteristik', 'prioritize', 'prioritas', 'best', 'terbaik',
    'highest', 'tertinggi', 'most', 'paling', 'which', 'what', 'apa', 'mana'
]

# ============================================
# PROSES RAG
# ============================================
if query:
    if not any(kw in query.lower() for kw in allowed_keywords):
        st.warning('This question is outside the scope of Bali Fiber business insights. Please ask questions related to customer clusters, business strategy, sales, or segmentation.')
    else:
        with st.spinner('Analyzing cluster data...'):
            try:
                docs = retriever.invoke(query)
                context = '\n'.join([doc.page_content for doc in docs])
                prompt = f"""
                You are an AI Business Analyst for Bali Fiber.
                Use the following context to answer the user's question.
                
                Context:
                {context}
                
                Question:
                {query}
                
                Provide:
                1. Business insights
                2. Cluster analysis
                3. Strategic recommendations
                """
                response = model.generate_content(prompt)
                hasil_ai = response.text
            except Exception as e:
                context = 'Cluster data temporarily unavailable.'
                st.warning(f'Error: {e}')
                hasil_ai = ''

        if hasil_ai:
            # Result Card
            st.markdown("""
            <div class="result-card">
                <div class="result-title">Analysis Results</div>
            </div>
            """, unsafe_allow_html=True)
            
            # Display result with proper formatting
            st.markdown(hasil_ai)
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            # Context Expander
            with st.expander('View Retrieved Context'):
                for i, doc in enumerate(docs):
                    st.markdown(f'**Cluster Context {i+1}**')
                    st.write(doc.page_content)
                    if i < len(docs) - 1:
                        st.divider()

# ============================================
# FOOTER
# ============================================
st.markdown("""
<div class="footer">
    Powered by K-Prototypes Clustering, RAG Architecture, and Gemini AI
</div>
""", unsafe_allow_html=True)
