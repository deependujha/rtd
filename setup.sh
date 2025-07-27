#!/bin/bash

# Setup script for documentation site
set -e

echo "🚀 Setting up documentation site..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not installed."
    exit 1
fi

# Create virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
    echo "📦 Creating virtual environment..."
    uv venv
fi

# Activate virtual environment
echo "🔄 Activating virtual environment..."
source .venv/bin/activate

# Install dependencies
echo "📚 Installing dependencies..."
uv pip install --upgrade pip
uv pip install -r requirements.txt

# Build documentation
echo "🔨 Building documentation..."
make html

echo ""
echo "✅ Setup complete!"
echo ""
echo "To view your documentation:"
echo "  1. Run: source .venv/bin/activate"
echo "  2. Run: make serve"
echo "  3. Open: http://localhost:8000"
echo ""
echo "To deploy to GitHub Pages:"
echo "  1. Push this repository to GitHub"
echo "  2. Go to Settings > Pages in your repo"
echo "  3. Set Source to 'GitHub Actions'"
echo "  4. Push to main branch to trigger deployment"
