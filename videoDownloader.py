from pytube import YouTube
import subprocess
import ffmpeg
from pathlib import Path

def videoDownloader():
    link = input("Enter the link : ")

    try:
        yt = YouTube(link)
    except:
        print("Connection Error")

    print("Titel :", yt.title)
    print("Views :", yt.views)
    min,sec=divmod(yt.length,60)
    print("Length :",min, "Minutes",sec,"seconds")

    download_path=str(Path.home()/"Downloads")
    audioStreams = yt.streams.filter(only_audio=True)
    videoStreams = yt.streams.filter(only_video=True)
    prog_videoStreams = videoStreams.filter(progressive=True)

    aOrv = input("Do you want to download audio or video ? (a/v) ")
    print("------------------------------------------------------")
    if aOrv.lower() == 'a':
        print("Available audios")
        print("-------------------------")
        for i in audioStreams:
            print(audioStreams.index(i) + 1," ", i.mime_type,"  ", i.abr)
        q_num = int(input("Enter a number : "))
        for j in audioStreams:
            if audioStreams.index(j) == q_num - 1:
                d_audio=i
                print("Downloading...")
                d_audio.download(download_path)
                print("Download completed!!")

    elif aOrv.lower() == 'v':
        if len(prog_videoStreams)>0:
            print("Available video qualities")
            print("-------------------------")
            for i in prog_videoStreams:
                print(prog_videoStreams.index(i) + 1, " ", i.mime_type, " ", i.resolution)
            q_num = int(input("Enter a number : "))
            for j in prog_videoStreams:
                if prog_videoStreams.index(j) == q_num - 1:
                    d_video = j
                    print("Downloading...")
                    d_video.download(download_path)
                    print("Download completed!!")
        else:
            aud=audioStreams.filter(abr=("128kbps" or "160kbps"))
            audio_title=aud.first().title
            aud.first().download("audio")
            print("Available video qualities")
            print("-------------------------")
            for j in videoStreams:
                if j.resolution=="720p" and j.mime_type=="video/mp4":
                    print(1," ", j.mime_type, " ", j.resolution)
                elif j.resolution=="480p" and j.mime_type=="video/mp4":
                    print(2," ", j.mime_type, " ", j.resolution)
                elif j.resolution=="360p" and j.mime_type=="video/mp4":
                    print(3," ", j.mime_type, " ", j.resolution)
            q_num = int(input("Enter a number : "))
            mp4_video=videoStreams.filter(mime_type="video/mp4")
            #print(mp4_video)
            print("Downloading...")
            if q_num==1:
                vs = mp4_video.filter(res='720p')
                v_title=vs.first().title
                print(v_title)
                vs.first().download("video")
            elif q_num==2:
                vs = mp4_video.filter(res='480p')
                v_title = vs.first().title
                vs.first().download("video")
            elif q_num==3:
                vs = mp4_video.filter(res='360p')
                v_title = vs.first().title
                vs.first().download("video")
            print("Download is Completed wait for merging...")
            video = "video\\"+v_title+'.mp4'
            audio = "audio\\"+audio_title+'.mp4'
            return_value = subprocess.call([
                'ffmpeg',
                '-stream_loop', '1',
                '-i', video,
                '-i', audio,
                '-c:v', 'libx264',
                '-tune', 'stillimage',
                '-c:a', 'aac',
                '-strict', 'experimental',
                '-b:a', '192k',
                '-pix_fmt', 'yuv420p',
                '-shortest', f'{download_path}\\{v_title}.mp4',
            ])
            if return_value:
                print("Failure")
            else:
                print("Merged successfully")
