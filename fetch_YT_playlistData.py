import subprocess
import os
import sys
from yt_dlp import YoutubeDL

# ================= CONFIGURATION =================
# Tell the script which browser you use to log into YouTube. 
# Choose one browser
# WARNING: BROWSER SHOULD BE INSTALLED ON YOUR SYSTEM!
BROWSER_NAME = "browser_name"                                                # "chrome", "brave", "firefox", "edge", "opera"... 

# Put your system shortcut codes or normal playlist IDs here!
PLAYLISTS = [
    "https://youtube.com/playlist?list=PLxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  # Playlist 1
    "https://youtube.com/playlist?list=PLxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  # Playlist 2
    "https://youtube.com/playlist?list=PLxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  # Playlist 3
    "https://www.youtube.com/playlist?list=WL",                              # Watch Later
    "https://www.youtube.com/playlist?list=LL",                              # Liked Videos
    "https://www.youtube.com/playlist?list=SS"                               # Sounds from Shorts
  
]

# Using your verified 32-bit x86 program files routing directly
VLC_PATH = r"C:\Program Files (x86)\VideoLAN\VLC\vlc.exe"
# =================================================

def verify_cookie_formatting(filepath):
    """Ensures the cookie file contains the valid Netscape header string."""
    if not os.path.exists(filepath):
        return False
    with open(filepath, 'r', encoding='utf-8') as f:
        first_line = f.readline()
        return "NETSCAPE" in first_line.upper() or "COOKIE" in first_line.upper()

def extract_and_stream():
    all_video_urls = []
    cookie_file = 'youtube_cookies.txt'
    
    ydl_opts = {
        'extract_flat': 'in_playlist',
        'quiet': True,
        'skip_download': True,
    }
    
    if verify_cookie_formatting(cookie_file):
        ydl_opts['cookiefile'] = cookie_file
    else:
        print("Warning: 'youtube_cookies.txt' missing valid format headers.")

    print(f"Reading active session parameters from targeted arrays...")
    
    with YoutubeDL(ydl_opts) as ydl:
        for playlist_url in PLAYLISTS:
            print(f"Extracting links from: {playlist_url}")
            try:
                playlist_data = ydl.extract_info(playlist_url, download=False)
                if 'entries' in playlist_data:
                    for entry in playlist_data['entries']:
                        if entry:
                            video_url = f"https://www.youtube.com/watch?v={entry['id']}"
                            all_video_urls.append(video_url)
            except Exception as e:
                print(f"Skipped a playlist link due to extraction hurdle: {e}")

    all_video_urls = list(set(all_video_urls))
    total_videos = len(all_video_urls)
    
    if total_videos == 0:
        print("\nZero videos extracted. Re-export your cookie file directly from an open tab!")
        return

    print(f"\nFound {total_videos} videos grand total across all your targeted arrays.")
    print("Writing text stream map to a lean virtual playlist layout...")
    
    # Generates a text document index of the links to safely bypass terminal length walls
    playlist_file = "vlc_stream_queue.m3u8"
    try:
        with open(playlist_file, "w", encoding="utf-8") as f:
            f.write("#EXTM3U\n")
            for url in all_video_urls:
                f.write(f"#EXTINF:-1,YouTube Video\n{url}\n")
        print(f"Successfully generated network map index: '{playlist_file}' (~{os.path.getsize(playlist_file) // 1024} KB)")
    except Exception as file_error:
        print(f"Failed to generate layout file mapping: {file_error}")
        return

    print("Launching VLC Media Player... Zero bytes hitting local storage.")
    
    # Drops shell execution and targets your verified VLC file location directly
    try:
        vlc_args = [VLC_PATH, "--no-video-title-show", "--network-caching=3000", playlist_file]
        subprocess.Popen(vlc_args)
    except FileNotFoundError:
        # Emergency backup fallback check in case of system profile duplication
        try:
            ALT_PATH = r"C:\Program Files\VideoLAN\VLC\vlc.exe"
            vlc_args = [ALT_PATH, "--no-video-title-show", "--network-caching=3000", playlist_file]
            subprocess.Popen(vlc_args)
        except Exception as system_error:
            print(f"\nError: Could not locate application paths. System message: {system_error}")

if __name__ == "__main__":
    extract_and_stream()
