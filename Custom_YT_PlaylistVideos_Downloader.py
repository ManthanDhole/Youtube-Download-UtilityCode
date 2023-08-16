from pytube import Playlist
import asyncio
import os
url_of_Playlist = input("Enter the Playlist URL: ")
# url_of_Playlist = "https://www.youtube.com/playlist?list=PL08903FB7ACA1C2FB" #Uncomment to add hardcode url for playlist

# Get all the links for video in the playlist
py = Playlist(url_of_Playlist)
downloadThisResolution = None  # Only download resolution mentioned in the below conditional check, i.e., Video_MP4 | 720p

# Create a folder with the name of playlist and execute the download code after navigating to the new Directory
currentDir = os.getcwd()
# print(currentDir)
if(os.path.exists(f"{currentDir}\{py.title}")):
    os.chdir(py.title)      #Change directory
else:    
    os.mkdir(py.title)   	#Make directory
    os.chdir(py.title)

print(f'Starting Playlist Download: {py.title}')
# print(py.videos)

videoList = list(enumerate(py.videos))
# print(videoList)
print("Please a range (in numbers) of the videos to download")
startRange = int(input("From: ")) 
endRange = int(input("To: "))

for vdo in videoList:
    video = (list(vdo))
    vdoCounter = video[0] + 1
    if(vdoCounter >= startRange and vdoCounter <= endRange):
        # print(video)
        # print(f"Video: {video}")
        # print(f"Video number: {video[0]}")
        # print(f"Video Counter: {vdoCounter}")
        print(f"Downloading: {video[1].title}")
        # Get the available resolutions for the video
        pixels = video[1].streams 
        availableResolutions = list(enumerate(pixels))  #Converted into a list of available resolutions
        for pix in availableResolutions:
            # print(pix)
            checkRes = str(pix[1])
            # print(checkRes) 

            # Conditional check for all the resolutions and get index number of High Resolution Stream
            if(len(checkRes.split("720p"))>1 and len(checkRes.split("video/mp4"))>1 and len(checkRes.split("progressive=\"True\""))>1):
                # print(pix[0])
                downloadThisResolution = pix[0]

        # print(downloadThisResolution)
        # Download the selected resolution
        asyncio.wait_for(pixels[downloadThisResolution].download(), timeout=None)
        print(f"Downloaded: {video[1].title}")
        print() 
    
print(f"Videos downloaded from {startRange} to {endRange} of the playlist {py.title}. Exiting Now!")