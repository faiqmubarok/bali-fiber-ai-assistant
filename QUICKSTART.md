# ⚡ Quick Start - 5 Menit Deploy!

## 🎯 Cara Tercepat Deploy ke Streamlit Cloud

### Step 1: Dapatkan API Key (2 menit)
1. Buka: https://makersuite.google.com/app/apikey
2. Klik "Create API Key"
3. Copy API key yang muncul (contoh: `AIzaSyC...`)

### Step 2: Push ke GitHub (1 menit)
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/USERNAME/REPO-NAME.git
git push -u origin main
```

### Step 3: Deploy di Streamlit Cloud (2 menit)
1. Buka: https://share.streamlit.io/
2. Login dengan GitHub
3. Klik "New app"
4. Pilih repository kamu
5. Main file: `app.py`
6. Klik "Advanced settings"
7. Di bagian Secrets, paste:
   ```
   GEMINI_API_KEY = "AIzaSyC..."
   ```
8. Klik "Deploy"!

### ✅ SELESAI!
Tunggu 2-3 menit, aplikasi kamu akan live! 🎉

---

## 🏠 Atau Jalankan Lokal (5 menit)

### Step 1: Install
```bash
pip install -r requirements.txt
```

### Step 2: Setup API Key
```bash
# Copy template
cp .streamlit/secrets.toml.example .streamlit/secrets.toml

# Edit file .streamlit/secrets.toml
# Ganti dengan API key kamu
```

### Step 3: Run
```bash
streamlit run app.py
```

Buka: http://localhost:8501

---

## ⚠️ Troubleshooting

**Error: "cluster_db not found"**
- Jalankan notebook `AI_2_FIXED.ipynb` dulu untuk generate database

**Error: "API key invalid"**
- Cek lagi API key kamu di https://makersuite.google.com/app/apikey
- Pastikan tidak ada spasi atau karakter aneh

**App lambat**
- Normal untuk pertama kali (download model ~90MB)
- Setelah itu akan cepat

---

## 📚 Dokumentasi Lengkap

- **README.md** - Overview project
- **DEPLOYMENT_GUIDE.md** - Panduan deploy lengkap
- **Streamlit Docs** - https://docs.streamlit.io/

---

**Need help?** Baca DEPLOYMENT_GUIDE.md untuk troubleshooting lengkap!
