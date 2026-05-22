# 🎯 Cheat Sheet - Command Penting

## 🚀 Quick Commands

### Setup Awal
```bash
# Install dependencies
pip install -r requirements.txt

# Setup project (auto)
./setup.sh

# Setup API key
cp .streamlit/secrets.toml.example .streamlit/secrets.toml
# Edit .streamlit/secrets.toml dengan API key kamu
```

### Jalankan Lokal
```bash
# Cara mudah
./run_local.sh

# Cara manual
streamlit run app.py

# Dengan port custom
streamlit run app.py --server.port=8080
```

### Git & GitHub
```bash
# Init Git
git init
git add .
git commit -m "Initial commit"

# Push ke GitHub
git remote add origin https://github.com/USERNAME/REPO.git
git branch -M main
git push -u origin main

# Update setelah edit
git add .
git commit -m "Update: deskripsi perubahan"
git push
```

---

## 🌐 Deploy Commands

### Streamlit Cloud
```
1. Push ke GitHub (lihat command di atas)
2. Buka: https://share.streamlit.io/
3. Login → New app → Pilih repo
4. Add secret: GEMINI_API_KEY = "your-key"
5. Deploy!
```

### Heroku
```bash
# Login
heroku login

# Create app
heroku create app-name

# Set API key
heroku config:set GEMINI_API_KEY="your-key"

# Deploy
git push heroku main

# Open app
heroku open

# View logs
heroku logs --tail
```

### Railway
```bash
# Install CLI
npm install -g @railway/cli

# Login
railway login

# Init
railway init

# Deploy
railway up

# Set env
railway variables set GEMINI_API_KEY="your-key"
```

---

## 🔧 Maintenance Commands

### Update Dependencies
```bash
# Update semua
pip install --upgrade -r requirements.txt

# Update specific package
pip install --upgrade streamlit

# Freeze dependencies
pip freeze > requirements.txt
```

### Database Management
```bash
# Backup database
tar -czf cluster_db_backup.tar.gz cluster_db/

# Restore database
tar -xzf cluster_db_backup.tar.gz

# Check database size
du -sh cluster_db/
```

### Debugging
```bash
# Run dengan verbose logging
streamlit run app.py --logger.level=debug

# Check Python version
python --version

# Check installed packages
pip list

# Check specific package
pip show streamlit
```

---

## 🔑 Environment Variables

### Set API Key

**macOS/Linux:**
```bash
export GEMINI_API_KEY="AIza..."
```

**Windows CMD:**
```cmd
set GEMINI_API_KEY=AIza...
```

**Windows PowerShell:**
```powershell
$env:GEMINI_API_KEY="AIza..."
```

**Permanent (macOS/Linux):**
```bash
# Add to ~/.bashrc or ~/.zshrc
echo 'export GEMINI_API_KEY="AIza..."' >> ~/.zshrc
source ~/.zshrc
```

---

## 📦 Package Management

### Virtual Environment (Recommended)
```bash
# Create venv
python -m venv venv

# Activate
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# Deactivate
deactivate
```

### Conda
```bash
# Create environment
conda create -n bali-fiber python=3.11

# Activate
conda activate bali-fiber

# Install dependencies
pip install -r requirements.txt

# Deactivate
conda deactivate
```

---

## 🐛 Troubleshooting Commands

### Fix Common Issues
```bash
# Upgrade pip
pip install --upgrade pip

# Clear pip cache
pip cache purge

# Reinstall package
pip uninstall streamlit
pip install streamlit

# Check for conflicts
pip check

# Fix permissions (macOS/Linux)
sudo chown -R $USER:$USER .
```

### Streamlit Specific
```bash
# Clear cache
streamlit cache clear

# Reset config
rm -rf ~/.streamlit/

# Check version
streamlit --version

# Run health check
streamlit hello
```

---

## 📊 Monitoring

### Check App Status
```bash
# Local
curl http://localhost:8501/_stcore/health

# Production (ganti URL)
curl https://your-app.streamlit.app/_stcore/health
```

### View Logs
```bash
# Streamlit Cloud: Lihat di dashboard
# Heroku: heroku logs --tail
# Railway: railway logs
# Render: Lihat di dashboard
```

---

## 🔐 Security

### Check for Secrets in Git
```bash
# Scan for potential secrets
git log --all --full-history --source -- '*secrets*'

# Remove file from Git history (DANGEROUS!)
git filter-branch --force --index-filter \
  "git rm --cached --ignore-unmatch .streamlit/secrets.toml" \
  --prune-empty --tag-name-filter cat -- --all
```

### Validate .gitignore
```bash
# Check what will be committed
git status

# Check ignored files
git status --ignored
```

---

## 📝 Useful Aliases

Add to `~/.bashrc` or `~/.zshrc`:

```bash
# Streamlit shortcuts
alias st='streamlit run app.py'
alias stclear='streamlit cache clear'

# Git shortcuts
alias gs='git status'
alias ga='git add .'
alias gc='git commit -m'
alias gp='git push'

# Project shortcuts
alias cdproj='cd /Users/faiq/Documents/Projects/tubes-ai'
```

---

## 🎓 Learning Resources

### Documentation
- Streamlit: https://docs.streamlit.io/
- Gemini API: https://ai.google.dev/docs
- LangChain: https://python.langchain.com/docs/
- ChromaDB: https://docs.trychroma.com/

### Tutorials
- Streamlit Tutorial: https://docs.streamlit.io/get-started
- RAG Tutorial: https://python.langchain.com/docs/use_cases/question_answering/

### Community
- Streamlit Forum: https://discuss.streamlit.io/
- GitHub Issues: https://github.com/streamlit/streamlit/issues

---

## 💡 Pro Tips

1. **Always use virtual environment** untuk isolasi dependencies
2. **Test lokal dulu** sebelum deploy
3. **Commit often** dengan message yang jelas
4. **Backup database** sebelum update besar
5. **Monitor API usage** untuk avoid over-limit
6. **Use .gitignore** untuk protect secrets
7. **Read logs** saat debugging
8. **Keep dependencies updated** tapi test dulu

---

**Save file ini untuk referensi cepat! 📌**
