#!/usr/bin/env bash

# ==============================================================================
# YouTube to VLC Streamer - Unix Launcher (Linux / macOS)
# ==============================================================================

# Stop script execution immediately if any command fails
set -e

echo "=================================================="
echo "📺 Initializing YouTube to VLC Streamer Environment"
echo "=================================================="

# 1. Ensure Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: python3 could not be found. Please install Python 3."
    exit 1
fi

# 2. Setup/Activate Python Virtual Environment (Highly Recommended for Unix)
if [ ! -d ".venv" ]; then
    echo "📦 Creating isolated Python virtual environment (.venv)..."
    python3 -m venv .venv
fi

echo "🔄 Activating local environment architecture..."
source .venv/bin/activate

# 3. Handle Dependency Routing
if [ -f "requirements.txt" ]; then
    echo "📥 Verifying upstream repository requirements (yt-dlp)..."
    pip install --quiet --upgrade pip
    pip install -r requirements.txt --quiet
else
    echo "⚠️ Warning: requirements.txt not found. Installing yt-dlp fallback..."
    pip install yt-dlp --quiet
fi

# 4. Detect Host VLC Binary Platform Pathway
echo "🔍 Mapping local VideoLAN executable routing matrices..."
VLC_BIN=""

if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS application path
    VLC_BIN="/Applications/VLC.app/Contents/MacOS/VLC"
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    # Linux distribution tracking
    if command -v vlc &> /dev/null; then
        VLC_BIN="vlc"
    elif [ -f "/usr/bin/vlc" ]; then
        VLC_BIN="/usr/bin/vlc"
    fi
fi

if [ -z "$VLC_BIN" ] || ! command -v "$VLC_BIN" &> /dev/null && [ ! -f "$VLC_BIN" ]; then
    echo "⚠️ Warning: Could not explicitly map your local VLC runtime binary."
    echo "   Ensure VLC is installed. The Python platform backup arrays will take over."
fi

# 5. Drop Execution Shell into Python Array Core Engine
echo "🚀 Booting extraction mapping matrix..."
echo "--------------------------------------------------"
python3 fetch_YT_playlistData.py

# Deactivate venv upon manual stream termination
deactivate
