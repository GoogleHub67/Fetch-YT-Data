@echo off
title YouTube to VLC Streamer
echo Checking python runtime dependencies...
pip install -r requirements.txt
echo.
echo Initializing playlist video link extractions...
python fetch_YT_playlistData.py
pause
