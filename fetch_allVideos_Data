import subprocess
import sys
import os
from yt_dlp import YoutubeDL

# ================= CONFIGURATION =================
VLC_PATH = r"C:\Program Files (x86)\VideoLAN\VLC\vlc.exe"
COOKIE_FILE = 'youtube_cookies.txt'
# =================================================

def stream_track():
    print("\n" + "=" * 60)
    print("      UNIVERSAL YOUTUBE TO VLC STREAMER (DISK SPACE: 0B)")
    print("      Type 'exit' or 'quit' anytime to close the player")
    print("=" * 60)
    
    while True:
        user_input = input("\nPaste ANY YouTube video or song link here: ").strip()
        
        if not user_input:
            continue
            
        if user_input.lower() in ['exit', 'quit', 'q', 'close']:
            print("Shutting down audio engine. Happy chess grinding!")
            break

        # Automatically converts your custom protocol mapping to secure https layout
        clean_url = user_input.replace("abcde://", "https://")

        # Fixed configuration explicitly setting options inside list structures
        ydl_opts = {
            'format': 'best',
            'quiet': True,
            'skip_download': True,
            # Wrapped cleanly inside a tuple block to prevent character splitting
            'remote_components': ('ejs:github',),
        }
        
        if os.path.exists(COOKIE_FILE):
            ydl_opts['cookiefile'] = COOKIE_FILE

        print("\nDecoding video stream from Google servers... Please wait...")
        
        try:
            with YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(clean_url, download=False)
                direct_stream_url = info.get('url')
        except Exception as e:
            print(f"Extraction failed: {e}")
            print("Make sure you are logged into YouTube and that your network link is valid.")
            continue

        if direct_stream_url:
            print("Launching VLC Player... Streaming live out of system memory.")
            try:
                vlc_args = [VLC_PATH, "--no-video-title-show", "--network-caching=3000", direct_stream_url]
                subprocess.Popen(vlc_args)
            except FileNotFoundError:
                try:
                    ALT_PATH = r"C:\Program Files\VideoLAN\VLC\vlc.exe"
                    subprocess.Popen([ALT_PATH, "--no-video-title-show", "--network-caching=3000", direct_stream_url])
                except Exception as system_error:
                    print(f"Could not locate VLC player profile: {system_error}")
        else:
            print("Could not resolve streaming components for this track.")

if __name__ == "__main__":
    stream_track()
