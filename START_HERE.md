# 👋 START HERE - Bali Fiber AI Assistant

## 🎯 Kamu Ada di Tempat yang Tepat!

Project ini **SUDAH SIAP DEPLOY**! Semua file yang dibutuhkan sudah dibuat.

---

## 📚 Pilih Panduan Sesuai Kebutuhan

### 🚀 Untuk Kamu yang Mau Deploy Cepat
**Baca:** [QUICKSTART.md](QUICKSTART.md)
- Panduan 5 menit
- Langsung to the point
- Deploy ke Streamlit Cloud (gratis!)

### 📖 Untuk Kamu yang Mau Paham Detail
**Baca:** [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)
- Panduan lengkap step-by-step
- Berbagai opsi deployment
- Troubleshooting detail

### 📋 Untuk Overview Project
**Baca:** [README.md](README.md)
- Apa itu project ini
- Fitur-fitur
- Struktur project

### 📝 Untuk Summary Cepat
**Baca:** [SUMMARY.md](SUMMARY.md)
- Ringkasan semua yang sudah dibuat
- Checklist sebelum deploy
- Tips & rekomendasi

### 🎯 Untuk Command Reference
**Baca:** [CHEATSHEET.md](CHEATSHEET.md)
- Command-command penting
- Git commands
- Troubleshooting commands

---

## ⚡ Quick Start (Paling Cepat!)

### Opsi 1: Deploy ke Cloud (5 menit)

1. **Dapatkan API Key**
   ```
   https://makersuite.google.com/app/apikey
   ```

2. **Push ke GitHub**
   ```bash
   git init
   git add .
   git commit -m "Deploy Bali Fiber AI"
   git remote add origin https://github.com/USERNAME/REPO.git
   git push -u origin main
   ```

3. **Deploy di Streamlit Cloud**
   ```
   https://share.streamlit.io/
   → Login → New app → Pilih repo
   → Add secret: GEMINI_API_KEY = "your-key"
   → Deploy!
   ```

### Opsi 2: Jalankan Lokal (5 menit)

```bash
# 1. Setup
./setup.sh

# 2. Edit API key di .streamlit/secrets.toml

# 3. Run
./run_local.sh
```

---

## 📁 File-File Penting

| File | Fungsi |
|------|--------|
| **app.py** | Aplikasi Streamlit utama |
| **requirements.txt** | Dependencies Python |
| **START_HERE.md** | File ini (entry point) |
| **QUICKSTART.md** | Panduan cepat 5 menit |
| **DEPLOYMENT_GUIDE.md** | Panduan deploy lengkap |
| **README.md** | Dokumentasi project |
| **SUMMARY.md** | Ringkasan & checklist |
| **CHEATSHEET.md** | Command reference |
| **.streamlit/secrets.toml.example** | Template API key |
| **setup.sh** | Auto setup script |
| **run_local.sh** | Run lokal script |

---

## ⚠️ PENTING! Sebelum Deploy

### ✅ Checklist:

- [ ] Sudah punya API key Gemini
- [ ] Sudah baca QUICKSTART.md atau DEPLOYMENT_GUIDE.md
- [ ] Folder `cluster_db` sudah ada (atau siap generate)
- [ ] Sudah test lokal (opsional tapi recommended)
- [ ] JANGAN commit API key ke Git!

### 🔑 Cara Dapatkan API Key:

1. Buka: https://makersuite.google.com/app/apikey
2. Klik "Create API Key"
3. Copy key yang muncul (format: `AIzaSyC...`)
4. Simpan di `.streamlit/secrets.toml` atau environment variable

### 📦 Cara Generate Database:

Jika folder `cluster_db` belum ada:
1. Buka notebook `AI_2_FIXED.ipynb`
2. Jalankan semua cell sampai bagian "Membuat Vector Database"
3. Folder `cluster_db` akan otomatis dibuat
4. Copy folder tersebut ke project ini

---

## 🆘 Butuh Bantuan?

### Kalau Stuck:

1. **Baca dokumentasi** yang sesuai (lihat daftar di atas)
2. **Cek CHEATSHEET.md** untuk command reference
3. **Lihat troubleshooting** di DEPLOYMENT_GUIDE.md
4. **Tanya di forum** Streamlit: https://discuss.streamlit.io/

### Error Umum:

| Error | Solusi |
|-------|--------|
| "API key not found" | Set di `.streamlit/secrets.toml` |
| "cluster_db not found" | Generate dari notebook |
| "Model not found" | Ganti ke `gemini-1.5-flash` |
| App lambat | Normal untuk pertama kali |

---

## 🎓 Rekomendasi Workflow

### Untuk Pemula:
1. Baca **QUICKSTART.md**
2. Deploy ke **Streamlit Cloud** (paling mudah)
3. Kalau ada masalah, baca **DEPLOYMENT_GUIDE.md**

### Untuk yang Berpengalaman:
1. Baca **SUMMARY.md** untuk overview
2. Setup lokal dengan `./setup.sh`
3. Test dengan `./run_local.sh`
4. Deploy ke platform pilihan
5. Gunakan **CHEATSHEET.md** untuk reference

---

## 🚀 Platform Deployment

| Platform | Gratis? | Kesulitan | Rekomendasi |
|----------|---------|-----------|-------------|
| **Streamlit Cloud** | ✅ Ya | ⭐ Mudah | ⭐⭐⭐⭐⭐ |
| Railway | 💰 $5 credit | ⭐⭐ Sedang | ⭐⭐⭐⭐ |
| Render | ✅ Free tier | ⭐⭐ Sedang | ⭐⭐⭐ |
| Heroku | 💰 $5/bulan | ⭐⭐⭐ Susah | ⭐⭐ |

**Rekomendasi: Streamlit Cloud** (gratis & paling mudah!)

---

## 💡 Tips Pro

1. **Selalu test lokal dulu** sebelum deploy
2. **Jangan commit secrets** ke Git
3. **Backup database** secara berkala
4. **Monitor API usage** untuk avoid over-limit
5. **Baca logs** kalau ada error

---

## 🎉 Siap Deploy!

Project ini **100% siap deploy**. Semua file sudah dibuat, tinggal:

1. Dapatkan API key
2. Pilih platform (recommend: Streamlit Cloud)
3. Follow panduan di QUICKSTART.md
4. Deploy!

**Good luck! 🚀**

---

## 📞 Resources

- **Streamlit Docs**: https://docs.streamlit.io/
- **Gemini API**: https://ai.google.dev/docs
- **Streamlit Forum**: https://discuss.streamlit.io/
- **GitHub Issues**: Untuk bug report

---

**Mulai dari QUICKSTART.md untuk deploy tercepat!** ⚡
