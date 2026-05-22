# Quick Start Guide

Panduan cepat untuk menjalankan Bali Fiber AI Assistant.

## Setup Pertama Kali (5 menit)

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Setup API Key
Buat file `.streamlit/secrets.toml` dan isi dengan:
```toml
GEMINI_API_KEY = "your-api-key-here"
```

Dapatkan API key di: https://makersuite.google.com/app/apikey

### 3. Process Data (Sekali Aja!)
```bash
python process_data.py
```

Output yang diharapkan:
```
============================================================
BALI FIBER DATA PROCESSING PIPELINE
============================================================

[1/4] Loading dataset...
✓ Dataset loaded: 1060 rows, 10 columns

[2/4] Generating cluster documents...
✓ Generated 6 cluster documents
✓ Saved cluster_docs.pkl
✓ Saved cluster_metadata.pkl

[3/4] Creating embeddings...
✓ Embedding model loaded

[4/4] Creating vector database...
✓ Vector database created with 6 documents

============================================================
PROCESSING COMPLETE!
============================================================
```

### 4. Jalankan App
```bash
streamlit run app.py
```

Buka browser di: http://localhost:8501

## Penggunaan Sehari-hari

Setelah setup pertama, cukup jalankan:
```bash
streamlit run app.py
```

Data sudah di-process, jadi app langsung jalan cepat! ⚡

## Contoh Pertanyaan

Coba tanya:
- "Which cluster has the highest churn risk?"
- "Cluster mana yang paling potensial?"
- "Which cluster should sales prioritize?"
- "Apa karakteristik Cluster 0?"
- "Cluster dengan performa terbaik?"

## Troubleshooting

### Error: "API key not found"
**Solusi**: Pastikan file `.streamlit/secrets.toml` ada dan berisi API key

### Error: "Failed to load vector database"
**Solusi**: Jalankan `python process_data.py` dulu

### App lambat pertama kali
**Normal**: Download embedding model (~90MB), next time lebih cepat

### Pertanyaan "outside scope"
**Solusi**: Gunakan kata kunci: cluster, customer, sales, churn, potential, strategy

## Struktur File

```
tubes-ai/
├── app.py                    # Main app - jalankan ini
├── process_data.py           # Process data - run sekali
├── dataset/
│   └── data_hasil_preprocessing.csv  # Data source
├── cluster_db/               # Database (auto-generated)
├── cluster_docs.pkl          # Processed data (auto-generated)
├── cluster_metadata.pkl      # Metadata (auto-generated)
└── .streamlit/
    └── secrets.toml          # API key - buat manual
```

## Sharing dengan Teman

Kalau teman mau pakai tanpa process data sendiri:

### Kamu (yang punya data):
```bash
# Zip processed files
zip -r bali-fiber-data.zip cluster_db/ cluster_docs.pkl cluster_metadata.pkl

# Share via Google Drive / Dropbox
```

### Teman (yang terima):
```bash
# Extract files
unzip bali-fiber-data.zip

# Langsung jalankan app
streamlit run app.py
```

## Update Data

Kalau data CSV berubah:
```bash
# 1. Update file: dataset/data_hasil_preprocessing.csv
# 2. Re-process:
python process_data.py

# 3. Jalankan app:
streamlit run app.py
```

## Deploy ke Streamlit Cloud

1. Push ke GitHub
2. Buka https://streamlit.io/cloud
3. Connect repository
4. Add secrets (GEMINI_API_KEY)
5. Deploy!

**Note**: Jangan lupa run `process_data.py` dulu sebelum push, atau tambahkan ke deployment script.

## Bantuan Lebih Lanjut

- **README.md** - Dokumentasi lengkap
- **DATA_PIPELINE.md** - Penjelasan detail pipeline
- **OPTIMIZATION_SUMMARY.md** - Summary perubahan

## Checklist

Sebelum deploy atau share, pastikan:
- ✅ `requirements.txt` ada
- ✅ `.streamlit/secrets.toml` ada (tapi jangan di-commit!)
- ✅ `cluster_db/` folder ada
- ✅ `cluster_docs.pkl` dan `cluster_metadata.pkl` ada
- ✅ App bisa jalan di local
- ✅ Test beberapa query

## Tips

💡 **Tip 1**: Gunakan suggested questions untuk mulai
💡 **Tip 2**: Lihat "View Retrieved Context" untuk debug
💡 **Tip 3**: App cache model, jadi restart cepat
💡 **Tip 4**: Processed files kecil (~200KB total), aman di-share

## Selesai!

Kalau semua langkah di atas sudah, app siap dipakai! 🎉

Ada masalah? Cek troubleshooting di atas atau baca dokumentasi lengkap.
