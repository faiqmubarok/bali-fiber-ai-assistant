#!/bin/bash

# Script untuk menjalankan aplikasi secara lokal
# Usage: ./run_local.sh

echo "🚀 Starting Bali Fiber AI Assistant..."
echo ""

# Cek apakah GEMINI_API_KEY sudah di-set
if [ -z "$GEMINI_API_KEY" ]; then
    echo "⚠️  GEMINI_API_KEY belum di-set!"
    echo ""
    echo "Cara set API key:"
    echo "  export GEMINI_API_KEY='your-api-key-here'"
    echo ""
    echo "Atau buat file .streamlit/secrets.toml dengan isi:"
    echo "  GEMINI_API_KEY = 'your-api-key-here'"
    echo ""
    read -p "Apakah kamu sudah set API key di secrets.toml? (y/n) " -n 1 -r
    echo ""
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

# Cek apakah cluster_db ada
if [ ! -d "cluster_db" ]; then
    echo "⚠️  Folder cluster_db tidak ditemukan!"
    echo "Kamu perlu menjalankan notebook AI_2_FIXED.ipynb terlebih dahulu"
    echo "untuk generate ChromaDB database."
    echo ""
    read -p "Lanjutkan tanpa database? (y/n) " -n 1 -r
    echo ""
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

# Jalankan Streamlit
echo "✅ Starting Streamlit..."
echo "📱 Aplikasi akan buka di: http://localhost:8501"
echo ""
streamlit run app.py
