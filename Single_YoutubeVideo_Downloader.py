from pytube import YouTube
import os
import asyncio

# link = "https://youtu.be/EAYlckSaviI"
link = input("Enter the link for the Youtube video to download: ")

downloadThisResolution = None

yt = YouTube(link)

# Create a folder with the name of playlist and execute the download code after navigating to the new Directory
currentDir = os.getcwd()
# print(currentDir)
if(os.path.exists(f"{currentDir}\{yt.title}")):
    print(f"Folder {yt.title} already exists")
    print(f"Folder changed to {yt.title}")
    os.chdir(yt.title)      #Change directory
else:    
    os.mkdir(yt.title)   	#Make directory
    os.chdir(yt.title)
    print(f"Folder {yt.title} created")
    print(f"Folder changed to {yt.title}")
# print(os.getcwd())

print(f"Downloading video: {yt.title}")

# get all the available resolutions of a video
pixels = yt.streams
availableResolutions = list(enumerate(pixels))
for pix in availableResolutions:
    # print(pix)
    checkRes = str(pix[1])
    # print(checkRes)
    if(len(checkRes.split("720p"))>1 and len(checkRes.split("video/mp4"))>1 and len(checkRes.split("progressive=\"True\""))>1):
        print(pix[0])
        downloadThisResolution = pix[0]

# print()
# print(downloadThisResolution)
asyncio.wait_for(pixels[downloadThisResolution].download())
print(f"Video {yt.title} downloaded successfully!")