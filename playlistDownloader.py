from pytube import Playlist

def playlistDownloader():
    link = input("Enter the link of the playlist : ")
    try:
        pl = Playlist(link)
    except:
        print("Connection Error")

    print("Playlist Title : ",pl.title)
    print('Number of videos in playlist:',len(pl.video_urls))

    for p in pl.videos:
        prog_streams = p.streams.filter(progressive=True)
        q720 = prog_streams.get_by_resolution('720p')
        #print(q720)
        #print(p.title)
        q720.download("C:\\Users\\ACER\\Downloads")
        print(f'{p.title}'," Downloaded!")
    print("Download Completed!!")




