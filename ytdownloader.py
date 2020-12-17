from videoDownloader import videoDownloader
from playlistDownloader import playlistDownloader

print("""__  __           ______      __            ____                      __                __         
\ \/ /___  __  _/_  __/_  __/ /_  ___     / __ \____ _      ______  / /___  ____ _____/ /__  _____
 \  / __ \/ / / // / / / / / __ \/ _ \   / / / / __ \ | /| / / __ \/ / __ \/ __ `/ __  / _ \/ ___/
 / / /_/ / /_/ // / / /_/ / /_/ /  __/  / /_/ / /_/ / |/ |/ / / / / / /_/ / /_/ / /_/ /  __/ /    
/_/\____/\__,_//_/  \__,_/_.___/\___/  /_____/\____/|__/|__/_/ /_/_/\____/\__,_/\__,_/\___/_/                                                                                                                                                                       
""")

choice = input("Do you want to download a video or a playlist (v or p) ? ")
if choice.lower()=='v':
    videoDownloader()
elif choice.lower()=='p':
    playlistDownloader()
else:
    print("Invalid input")





