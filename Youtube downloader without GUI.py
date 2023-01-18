from pytube import Playlist
from pytube import YouTube


a = int(input("press 1 for playlist download and 2 for a song download\n"))

if a == 1:
    b = str(input("enter the playlist link\n"))
    p = Playlist(b)
    c = int(input("press 1 for mp3 format and 2 for mp4\n"))
    if c == 1:
        for i in p.video_urls:
            y = YouTube(i)
            y1 = y.streams.filter(type = "audio").all()
            y1[0].download()
    else:
        d = int(input("select the resolution of the vedio resolution\n 1 - 144p\n 2 - 360p\n 3 - 720p\n"))
        for i in p.video_urls:
            y = YouTube(i)
            y1 = y.streams.filter(progressive=True).all()
            if d == 1:
                y1[0].download()
            if d == 2:
                y1[1].download()
            if d == 3:
                y1[2].download()


else:
    b = str(input("enter the video link\n"))
    c = int(input("press 1 for mp3 format and 2 for mp4\n"))
    if c == 1:
        y = YouTube(b)
        y1 = y.streams.filter(type="audio").all()
        y1[0].download()
        j = input("is it done")
    else:
        d = int(input("select the resolution of the vedio resolution\n 1 - 144p\n 2 - 360p\n 3 - 720p\n"))
        y = YouTube(b)
        y1 = y.streams.filter(progressive=True).all()
        if d == 1:
            y1[0].download()
        if d == 2:
            y1[1].download()
        if d == 3:
            y1[2].download()



print("its been downloaded enjoy it")
g = int(input("Thank You"))