import os 
# pip install yt-dip
import yt_dlp
def download_playlist(playlist_url):
    try:
        ydl_opts = {
            'outtmpl': os.path.join(os.getcwd(), '%(playlist_title)s', '%(title)s.%(ext)s'),
            'format': 'best',
        }
        with yl_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Downloading playlist: {playlist_url}")
            ydl.download([playlist_url])
        print("Playlist download completed")
    except Exception as e:
        print(f"An error occured: {e}")

if __name__ == "__main__":
    playlist_url = input("Enter the youtube URL: "). strip()
    download_playlist(playlist_url)