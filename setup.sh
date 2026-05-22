#!/bin/bash

# Setup script untuk Bali Fiber AI Assistant
# Usage: ./setup.sh

echo "🚀 Bali Fiber AI Assistant - Setup Script"
echo "=========================================="
echo ""

# Cek Python
echo "1️⃣  Checking Python installation..."
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 tidak ditemukan!"
    echo "   Install Python dari: https://www.python.org/downloads/"
    exit 1
fi

PYTHON_VERSION=$(python3 --version)
echo "✅ $PYTHON_VERSION"
echo ""

# Cek pip
echo "2️⃣  Checking pip..."
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 tidak ditemukan!"
    exit 1
fi
echo "✅ pip3 found"
echo ""

# Install dependencies
echo "3️⃣  Installing dependencies..."
echo "   This may take a few minutes..."
pip3 install -r requirements.txt
if [ $? -eq 0 ]; then
    echo "✅ Dependencies installed successfully"
else
    echo "❌ Failed to install dependencies"
    exit 1
fi
echo ""

# Setup secrets
echo "4️⃣  Setting up secrets..."
if [ ! -f ".streamlit/secrets.toml" ]; then
    cp .streamlit/secrets.toml.example .streamlit/secrets.toml
    echo "✅ Created .streamlit/secrets.toml"
    echo "⚠️  IMPORTANT: Edit .streamlit/secrets.toml and add your GEMINI_API_KEY"
else
    echo "ℹ️  .streamlit/secrets.toml already exists"
fi
echo ""

# Check cluster_db
echo "5️⃣  Checking database..."
if [ -d "cluster_db" ]; then
    echo "✅ cluster_db found"
else
    echo "⚠️  cluster_db not found"
    echo "   You need to run AI_2_FIXED.ipynb to generate the database"
fi
echo ""

# Summary
echo "=========================================="
echo "✅ Setup completed!"
echo ""
echo "Next steps:"
echo "1. Get Gemini API key from: https://makersuite.google.com/app/apikey"
echo "2. Edit .streamlit/secrets.toml and add your API key"
echo "3. Run: ./run_local.sh"
echo ""
echo "For deployment guide, read: DEPLOYMENT_GUIDE.md"
echo "=========================================="
