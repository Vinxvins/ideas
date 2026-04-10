#!/bin/bash
set -e
echo "🚀 Stock Market Analyzer - One Click Setup"
echo "==========================================="
if [ ! -d "venv" ]; then
echo "📦 Creating virtual environment..."
python3 -m venv venv
echo "✅ Virtual environment created"
fi
echo "🔄 Activating virtual environment..."
source venv/bin/activate
echo "📥 Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt
echo "📂 Creating project directories..."
mkdir -p data logs reports
echo "🗄️  Initializing database..."
python3 -c "from src.database import init_db; init_db()"
echo "⚙️  Setting up environment variables..."
if [ ! -f ".env" ]; then
cp .env.example .env
echo "✅ Created .env file - please configure your settings"
else
echo "✅ .env file already exists"
fi
echo ""
echo "✨ Setup Complete!"
echo "==========================================="
echo "Run your first analysis with:"
echo "python3 -m src.main --symbol RELIANCE"