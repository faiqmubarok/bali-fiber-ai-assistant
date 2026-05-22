# 🤖 Bali Fiber AI Assistant

Sistem AI berbasis RAG (Retrieval-Augmented Generation) untuk analisis segmentasi pelanggan dan rekomendasi strategi bisnis Bali Fiber menggunakan K-Prototypes Clustering + ChromaDB + Gemini LLM.

## 📋 Fitur

- ✅ Analisis cluster pelanggan secara real-time
- ✅ Rekomendasi strategi bisnis berbasis AI
- ✅ Semantic search menggunakan ChromaDB
- ✅ Interface modern dengan Streamlit
- ✅ Powered by Google Gemini LLM

## 🚀 Cara Deploy

### 1. Persiapan Lokal

#### Install Dependencies
```bash
# Pastikan Python 3.8+ sudah terinstall
python --version

# Install semua library yang dibutuhkan
pip install -r requirements.txt
```

#### Setup API Key
Kamu perlu API key dari Google Gemini. Dapatkan di: https://makersuite.google.com/app/apikey

**Cara 1: Menggunakan Environment Variable (Recommended)**
```bash
# macOS/Linux
export GEMINI_API_KEY="your-api-key-here"

# Windows (Command Prompt)
set GEMINI_API_KEY=your-api-key-here

# Windows (PowerShell)
$env:GEMINI_API_KEY="your-api-key-here"
```

**Cara 2: Menggunakan Streamlit Secrets**
```bash
# Copy file example
cp .streamlit/secrets.toml.example .streamlit/secrets.toml

# Edit file secrets.toml dan isi dengan API key kamu
# GEMINI_API_KEY = "your-api-key-here"
```

#### Jalankan Aplikasi Lokal
```bash
streamlit run app.py
```

Aplikasi akan berjalan di: http://localhost:8501

---

### 2. Deploy ke Streamlit Cloud (GRATIS!)

#### Langkah-langkah:

1. **Push ke GitHub**
   ```bash
   # Inisialisasi git (jika belum)
   git init
   
   # Add semua file
   git add .
   
   # Commit
   git commit -m "Initial commit: Bali Fiber AI Assistant"
   
   # Buat repository baru di GitHub, lalu:
   git remote add origin https://github.com/username/repo-name.git
   git branch -M main
   git push -u origin main
   ```

2. **Deploy di Streamlit Cloud**
   - Buka: https://share.streamlit.io/
   - Login dengan GitHub
   - Klik "New app"
   - Pilih repository kamu
   - Main file path: `app.py`
   - Klik "Advanced settings"
   - Tambahkan secrets:
     ```toml
     GEMINI_API_KEY = "your-api-key-here"
     ```
   - Klik "Deploy"!

3. **Selesai!** 🎉
   - Aplikasi kamu akan live dalam beberapa menit
   - URL akan seperti: `https://username-repo-name.streamlit.app`

---

### 3. Deploy ke Platform Lain

#### Heroku
```bash
# Install Heroku CLI
# Buat file Procfile
echo "web: streamlit run app.py --server.port=$PORT" > Procfile

# Deploy
heroku create your-app-name
heroku config:set GEMINI_API_KEY="your-api-key-here"
git push heroku main
```

#### Railway
1. Buka https://railway.app/
2. Connect GitHub repository
3. Add environment variable: `GEMINI_API_KEY`
4. Deploy!

#### Render
1. Buka https://render.com/
2. New Web Service
3. Connect repository
4. Build command: `pip install -r requirements.txt`
5. Start command: `streamlit run app.py --server.port=$PORT --server.address=0.0.0.0`
6. Add environment variable: `GEMINI_API_KEY`

---

## 📁 Struktur Project

```
tubes-ai/
├── app.py                          # Main Streamlit app
├── requirements.txt                # Python dependencies
├── README.md                       # Dokumentasi ini
├── .gitignore                      # File yang diabaikan Git
├── .streamlit/
│   ├── config.toml                # Konfigurasi Streamlit
│   └── secrets.toml.example       # Template untuk API key
├── cluster_db/                     # ChromaDB vector database (perlu dibuat)
└── AI_2_FIXED.ipynb               # Notebook original
```

---

## ⚠️ Troubleshooting

### Error: "GEMINI_API_KEY tidak ditemukan"
- Pastikan kamu sudah set environment variable atau secrets.toml
- Restart terminal/aplikasi setelah set environment variable

### Error: "cluster_db not found"
- Kamu perlu menjalankan notebook `AI_2_FIXED.ipynb` terlebih dahulu untuk generate database ChromaDB
- Atau copy folder `cluster_db` dari Google Colab ke local

### Error: Model tidak ditemukan
- Pastikan nama model Gemini valid: `gemini-2.0-flash-exp` atau `gemini-1.5-flash`
- Cek dokumentasi terbaru: https://ai.google.dev/models/gemini

### Aplikasi lambat saat pertama kali load
- Normal! Streamlit sedang download model embedding (±90MB)
- Setelah pertama kali, akan di-cache dan jadi cepat

---

## 🔧 Konfigurasi

### Ganti Model Gemini
Edit `app.py` baris 101:
```python
model = genai.GenerativeModel('models/gemini-1.5-flash')  # Ganti sesuai kebutuhan
```

### Ubah Jumlah Dokumen Retrieval
Edit `app.py` baris 120:
```python
retriever = vectordb.as_retriever(search_kwargs={'k': 5})  # Default: 3
```

---

## 📝 Catatan Penting

1. **API Key**: JANGAN commit API key ke Git! Selalu gunakan environment variable atau secrets
2. **Database**: Folder `cluster_db` harus ada dan berisi data ChromaDB yang sudah di-generate
3. **Model**: Pastikan menggunakan model Gemini yang valid dan aktif
4. **Gratis**: Streamlit Cloud gratis untuk public apps dengan resource terbatas

---

## 🤝 Kontribusi

Project ini dibuat untuk tugas AI. Feel free to fork dan modifikasi sesuai kebutuhan!

---

## 📞 Support

Jika ada masalah saat deploy:
1. Cek error message di terminal/logs
2. Pastikan semua dependencies terinstall
3. Verifikasi API key valid
4. Cek dokumentasi Streamlit: https://docs.streamlit.io/

---

**Developed using K-Prototypes Clustering + RAG + Gemini LLM** 🚀
