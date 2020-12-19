from pytube import Playlist
from pathlib import Path
def playlistDownloader():
    link = input("Enter the link of the playlist : ")
    download_path = str(Path.home()/"Downloads")
    try:
        pl = Playlist(link)
    except:
        print("Connection Error")

    print("Playlist Title : ",pl.title)
    print('Number of videos in playlist:',len(pl.video_urls))
    print("Downloading...")

    for p in pl.videos:
        prog_streams = p.streams.filter(progressive=True)
        q720 = prog_streams.get_by_resolution('720p')
        q720.download(download_path)
        print(f'{p.title}'," --Downloaded!")
    print("Download Completed!!")




