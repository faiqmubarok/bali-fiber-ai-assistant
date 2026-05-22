#!/usr/bin/env python3
"""
Script untuk mengecek model Gemini yang tersedia dengan API key kamu
"""

import os
import google.generativeai as genai

# Load API key
API_KEY = os.environ.get('GEMINI_API_KEY')

if not API_KEY:
    # Try from secrets.toml
    try:
        import toml
        secrets = toml.load('.streamlit/secrets.toml')
        API_KEY = secrets.get('GEMINI_API_KEY')
    except:
        pass

if not API_KEY:
    print("❌ GEMINI_API_KEY tidak ditemukan!")
    print("Set environment variable atau buat .streamlit/secrets.toml")
    exit(1)

# Configure API
genai.configure(api_key=API_KEY)

print("🔍 Checking available Gemini models...\n")
print("=" * 70)

try:
    # List all models
    models = genai.list_models()
    
    print("\n✅ Available Models:\n")
    
    for model in models:
        # Filter hanya model yang support generateContent
        if 'generateContent' in model.supported_generation_methods:
            print(f"📌 {model.name}")
            print(f"   Display Name: {model.display_name}")
            print(f"   Description: {model.description}")
            print(f"   Supported: {', '.join(model.supported_generation_methods)}")
            print()
    
    print("=" * 70)
    print("\n💡 Rekomendasi untuk app.py:")
    print("   Gunakan salah satu nama model di atas (tanpa 'models/' prefix)")
    print("\n   Contoh:")
    print("   model = genai.GenerativeModel('gemini-1.5-flash-latest')")
    print("   atau")
    print("   model = genai.GenerativeModel('gemini-1.5-pro-latest')")
    
except Exception as e:
    print(f"❌ Error: {e}")
    print("\nKemungkinan masalah:")
    print("1. API key tidak valid")
    print("2. Koneksi internet bermasalah")
    print("3. API Gemini sedang down")
