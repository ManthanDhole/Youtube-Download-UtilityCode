from pytube import Playlist
import asyncio

url_of_Playlist = input("Enter the Playlist URL: ")

# Get all the links for video in the playlist
py = Playlist(url_of_Playlist)
downloadThisResolution = None  # Only download resolution in the below conditional check, i.e., Video_MP4 | 720p

print(f'Downloading Playlist: {py.title}')

for vdo in py.videos:
    print(f"Downloading: {vdo.title}")
    # Get the available resolutions for the video
    pixels = vdo.streams 
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
    print(f"Downloaded: {vdo.title}")

    print()  
    
print("Full Playlist Downloaded. Exiting Now!")