# 📦 Panduan Deployment Lengkap - Bali Fiber AI Assistant

## 🎯 Pilihan Deployment

Ada 3 cara deploy aplikasi ini:
1. **Lokal** - Untuk testing di komputer sendiri
2. **Streamlit Cloud** - GRATIS, paling mudah, recommended!
3. **Platform Lain** - Heroku, Railway, Render, dll

---

## 1️⃣ DEPLOYMENT LOKAL

### Langkah 1: Install Python & Dependencies

```bash
# Cek Python version (minimal 3.8)
python --version

# Install dependencies
pip install -r requirements.txt
```

### Langkah 2: Setup API Key

Dapatkan API key dari: https://makersuite.google.com/app/apikey

**Pilih salah satu cara:**

**Cara A: Environment Variable**
```bash
# macOS/Linux
export GEMINI_API_KEY="AIza..."

# Windows CMD
set GEMINI_API_KEY=AIza...

# Windows PowerShell
$env:GEMINI_API_KEY="AIza..."
```

**Cara B: Streamlit Secrets (Recommended)**
```bash
# Copy template
cp .streamlit/secrets.toml.example .streamlit/secrets.toml

# Edit file .streamlit/secrets.toml
# Ganti "your-gemini-api-key-here" dengan API key kamu
```

### Langkah 3: Jalankan Aplikasi

**Cara Mudah:**
```bash
./run_local.sh
```

**Cara Manual:**
```bash
streamlit run app.py
```

Buka browser: http://localhost:8501

---

## 2️⃣ DEPLOYMENT KE STREAMLIT CLOUD (RECOMMENDED) 🌟

### Kenapa Streamlit Cloud?
- ✅ 100% GRATIS
- ✅ Paling mudah
- ✅ Auto-deploy dari GitHub
- ✅ Dapat URL publik
- ✅ SSL/HTTPS otomatis

### Langkah 1: Push ke GitHub

```bash
# Inisialisasi Git (jika belum)
git init

# Add semua file
git add .

# Commit
git commit -m "Deploy Bali Fiber AI Assistant"

# Buat repository baru di GitHub (https://github.com/new)
# Lalu jalankan:
git remote add origin https://github.com/USERNAME/REPO-NAME.git
git branch -M main
git push -u origin main
```

### Langkah 2: Deploy di Streamlit Cloud

1. **Buka**: https://share.streamlit.io/
2. **Login** dengan akun GitHub kamu
3. Klik **"New app"**
4. **Pilih repository** yang baru kamu push
5. **Main file path**: `app.py`
6. Klik **"Advanced settings"**
7. Di bagian **Secrets**, paste ini:
   ```toml
   GEMINI_API_KEY = "AIza..."
   ```
   (Ganti dengan API key kamu yang asli)
8. Klik **"Deploy"**!

### Langkah 3: Tunggu Deploy Selesai

- Proses deploy: 2-5 menit
- Kamu akan dapat URL seperti: `https://username-repo.streamlit.app`
- Share URL ini ke siapa saja! 🎉

### Troubleshooting Streamlit Cloud

**Error: "No module named 'xxx'"**
- Pastikan semua library ada di `requirements.txt`
- Cek logs untuk library yang missing

**Error: "cluster_db not found"**
- Kamu perlu upload folder `cluster_db` ke repository
- Atau generate ulang di notebook lalu commit

**App terlalu lambat**
- Streamlit Cloud free tier punya resource terbatas
- Pertimbangkan upgrade atau deploy di platform lain

---

## 3️⃣ DEPLOYMENT KE PLATFORM LAIN

### Option A: Heroku

```bash
# Install Heroku CLI
# https://devcenter.heroku.com/articles/heroku-cli

# Login
heroku login

# Buat app
heroku create bali-fiber-ai

# Set API key
heroku config:set GEMINI_API_KEY="AIza..."

# Deploy
git push heroku main

# Buka app
heroku open
```

**Catatan**: Heroku tidak lagi gratis sejak 2022. Minimal $5/bulan.

### Option B: Railway

1. Buka: https://railway.app/
2. Klik "Start a New Project"
3. Pilih "Deploy from GitHub repo"
4. Pilih repository kamu
5. Add environment variable:
   - Key: `GEMINI_API_KEY`
   - Value: API key kamu
6. Railway akan auto-detect Streamlit dan deploy!

**Biaya**: $5 credit gratis/bulan

### Option C: Render

1. Buka: https://render.com/
2. Klik "New +" → "Web Service"
3. Connect repository
4. Settings:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `streamlit run app.py --server.port=$PORT --server.address=0.0.0.0`
5. Add environment variable:
   - Key: `GEMINI_API_KEY`
   - Value: API key kamu
6. Klik "Create Web Service"

**Biaya**: Free tier tersedia (dengan batasan)

---

## 🔧 KONFIGURASI LANJUTAN

### Mengubah Model Gemini

Edit `app.py` baris ~101:
```python
# Pilihan model:
# - gemini-2.0-flash-exp (terbaru, experimental)
# - gemini-1.5-flash (stabil)
# - gemini-1.5-pro (lebih pintar, lebih lambat)

model = genai.GenerativeModel('models/gemini-1.5-flash')
```

### Mengubah Jumlah Dokumen Retrieval

Edit `app.py` baris ~120:
```python
# Default: k=3 (ambil 3 dokumen terdekat)
# Bisa dinaikkan untuk hasil lebih detail
retriever = vectordb.as_retriever(search_kwargs={'k': 5})
```

### Custom Domain (Streamlit Cloud)

1. Beli domain (Namecheap, GoDaddy, dll)
2. Di Streamlit Cloud settings, add custom domain
3. Update DNS records sesuai instruksi
4. Tunggu propagasi DNS (1-48 jam)

---

## 📊 MONITORING & MAINTENANCE

### Cek Logs (Streamlit Cloud)
1. Buka app dashboard
2. Klik "Manage app"
3. Lihat logs di bagian bawah

### Update Aplikasi
```bash
# Edit file yang perlu diubah
git add .
git commit -m "Update: ..."
git push

# Streamlit Cloud akan auto-deploy!
```

### Backup Database
```bash
# Backup folder cluster_db
tar -czf cluster_db_backup.tar.gz cluster_db/

# Restore
tar -xzf cluster_db_backup.tar.gz
```

---

## ⚠️ CHECKLIST SEBELUM DEPLOY

- [ ] Python 3.8+ terinstall
- [ ] Semua dependencies di `requirements.txt` valid
- [ ] API key Gemini sudah didapat
- [ ] Folder `cluster_db` sudah ada (atau siap generate)
- [ ] File `.gitignore` sudah benar (jangan commit secrets!)
- [ ] Testing lokal berhasil
- [ ] Repository GitHub sudah dibuat
- [ ] README.md sudah diupdate

---

## 🆘 TROUBLESHOOTING UMUM

### "GEMINI_API_KEY tidak ditemukan"
✅ **Solusi**: Set environment variable atau buat `.streamlit/secrets.toml`

### "cluster_db not found"
✅ **Solusi**: Jalankan notebook untuk generate database, atau copy dari Colab

### "Model not found"
✅ **Solusi**: Ganti nama model ke `gemini-1.5-flash` (lebih stabil)

### App sangat lambat
✅ **Solusi**: 
- Pertama kali load memang lambat (download model)
- Setelah itu akan di-cache
- Atau upgrade ke paid tier

### Error saat install dependencies
✅ **Solusi**:
```bash
# Upgrade pip
pip install --upgrade pip

# Install satu per satu untuk debug
pip install streamlit
pip install google-generativeai
# dst...
```

---

## 📞 SUPPORT

**Dokumentasi:**
- Streamlit: https://docs.streamlit.io/
- Gemini API: https://ai.google.dev/docs
- LangChain: https://python.langchain.com/docs/

**Community:**
- Streamlit Forum: https://discuss.streamlit.io/
- Stack Overflow: Tag `streamlit` atau `google-gemini`

---

## 🎓 TIPS PRO

1. **Gunakan Streamlit Secrets** untuk API key, jangan hardcode
2. **Enable caching** dengan `@st.cache_resource` untuk model
3. **Monitor usage** API Gemini di Google Cloud Console
4. **Backup database** secara berkala
5. **Test lokal** sebelum deploy ke production
6. **Gunakan Git tags** untuk versioning

---

**Good luck dengan deployment! 🚀**

Jika ada pertanyaan, cek README.md atau dokumentasi official.
