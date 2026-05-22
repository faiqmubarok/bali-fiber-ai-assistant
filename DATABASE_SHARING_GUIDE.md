# Database Sharing Guide

## For the Data Owner (Your Friend)

### Option 1: ZIP File (Recommended)

1. Compress the `cluster_db` folder:
```bash
# On macOS/Linux
zip -r cluster_db.zip cluster_db/

# On Windows (PowerShell)
Compress-Archive -Path cluster_db -DestinationPath cluster_db.zip
```

2. Share via:
   - **Google Drive**: Upload `cluster_db.zip` and share the link
   - **Dropbox**: Upload and share the link
   - **WeTransfer**: Upload (free up to 2GB)
   - **Direct transfer**: USB drive, AirDrop, etc.

### Option 2: Google Drive Folder

1. Upload the entire `cluster_db` folder to Google Drive
2. Right-click → Share → Get link
3. Set permission to "Anyone with the link can view"
4. Share the link

### Option 3: GitHub (If database is small)

If the database is under 100MB:
```bash
git add cluster_db/
git commit -m "Add cluster database"
git push
```

**Note**: GitHub has file size limits. Use Git LFS for large files.

---

## For You (Receiver)

### If you receive a ZIP file:

1. Download `cluster_db.zip`
2. Extract to project root:
```bash
# On macOS/Linux
unzip cluster_db.zip

# On Windows
# Right-click → Extract All
```

3. Verify structure:
```
tubes-ai/
├── cluster_db/
│   ├── chroma.sqlite3
│   └── [other files]
└── app.py
```

### If you receive a Google Drive link:

1. Click the link
2. Download the folder/file
3. Extract if needed
4. Place in project root

### If database is in GitHub:

```bash
git pull origin main
```

---

## Verification

After placing the database, verify it works:

```bash
# Check if folder exists
ls -la cluster_db/

# Run the app
streamlit run app.py
```

If successful, you should be able to ask questions and get AI responses.

---

## Database Size

Typical `cluster_db` size: **10-100 MB** (depends on data volume)

If larger than 100MB, use:
- Google Drive
- Dropbox
- WeTransfer
- External storage

---

## Troubleshooting

**"cluster_db not found"**
- Make sure the folder is in the project root
- Check folder name is exactly `cluster_db` (lowercase)

**"Database corrupted"**
- Re-download from source
- Verify ZIP extraction completed successfully

**"Permission denied"**
- Check folder permissions:
```bash
chmod -R 755 cluster_db/
```
