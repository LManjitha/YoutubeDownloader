import time
from pytube import YouTube
import sys

def videoDownloader():
    link = input("Enter the link : ")
    # yt=YouTube(link)

    try:
        yt = YouTube(link)
    except:
        print("Connection Error")

    print("Titel :", yt.title)
    print("Views :", yt.views)
    print("Length :", yt.length / 60, "Minutes")

    audioStreams = yt.streams.filter(only_audio=True)
    videoStreams = yt.streams.filter(only_video=True)
    prog_videoStreams = videoStreams.filter(progressive=True)

    aOrv = input("What do you want to download audio or video ? (a/v) ")
    print("------------------------------------------------------")
    if aOrv.lower() == 'a':
        print("Available audios")
        print("-------------------------")
        for i in audioStreams:
            print(audioStreams.index(i) + 1, " ", i.mime_type, "  ", i.abr)
        q_num = int(input("Enter a number : "))
        for j in audioStreams:
            if audioStreams.index(j) == q_num - 1:
                d_audio = i
                c = 1
                while c < 5:
                    txt = "Downloading" + "." * c
                    c += 1
                    sys.stdout.write('\r' + txt)
                    time.sleep(1)
                    if (d_audio.download("C:\\Users\\ACER\\Downloads")):
                        c = 6
                    if c == 4:
                        c = 0
                print("Download completed!!")

    elif aOrv.lower() == 'v':
        print("Available video qualities")
        print("-------------------------")
        for i in videoStreams:
            print(i)
            if getattr(i, 'res', 'def'):
                print(videoStreams.index(i) + 1, " ", i.mime_type, " ", i.res)
        q_num = int(input("Enter a number : "))
        for j in videoStreams:
            if videoStreams.index(j) == q_num - 1:
                d_video = j
                print("Downloading...")
                d_video.download("C:\\Users\\ACER\\Downloads")
                print("Download completed!!")