from pytube import YouTube
import sys
import time

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage = (bytes_downloaded / total_size) * 100
    print(f"\rDownloading... {percentage:.2f}% complete", end='')
    sys.stdout.flush()

videoURL = ""
if len(sys.argv) > 1:
    videoURL = sys.argv[1]
if "youtube.com" not in videoURL:
    videoURL = input("Enter YouTube URL: ")

yt = YouTube(videoURL, use_oauth=True, allow_oauth_cache=True)
filename = yt.title.replace(" ", "_").replace("&", "'&'").replace("|","_")
output_path = r"C:\Users\mks11\Videos\YTvideos"  # Specified output directory

print("YouTube File to download :", yt.title)
yt.register_on_progress_callback(on_progress)


while True:
    reso = input("ENTER THE RESOLUTION YOU WANT (Example ==> 1080p or 720p or 480p or 2160p or 1440p and NO LOW QUALITY SHIT LOL) :::>> ")
    if reso == "1080p":
        itag = 137
        break
    elif reso == "720p":
        itag = 136
        break
    elif reso == "480p":
        itag = 135
        break
    elif reso == "360p":
        itag = 134
        break
    elif reso == "2160p":
        itag = 313
        break
    elif reso == "1440p":
        itag = 271
        break
    else: 
        print("ENTER A VALID RESOLUTION--> REFER EXAMPLE")
    
        
    


# Get all streams and filter only video streams
video_stream_list = yt.streams.filter(type="video").get_by_itag(itag=itag)



#https://www.youtube.com/watch?v=5OwOoQzLOyc charkha - wadali 
#https://www.youtube.com/watch?v=xiMN19yBj9o Travis - control 
#https://www.youtube.com/watch?v=ADVNZM-qrT4   -- joint in the booth SM
#https://www.youtube.com/watch?v=VEQ-XJWiQMM 11k SM

print("NOW DOWNLAODING ", yt.title," in ", reso," resolution")

current_time = time.strftime("%Y%m%d-%H%M%S")
unique_filename = f"{filename}_{current_time}.mp4".replace('!','').replace('-','').replace('+','')

  # Download the video to the specified output directory with the unique filename
if video_stream_list.download(output_path=output_path, filename=unique_filename):
    print("\nDownload completed!")
else :
    print("Please enter a valid resolution.")
