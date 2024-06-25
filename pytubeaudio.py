from pytube import YouTube
import re
import requests
from tqdm import tqdm

while True:
    print("Do you want to download:")
    print("1) Single audio")
    print("2) A Playlist of audios")
    print("3) Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        url = input("Enter the URL of the video file to be downloaded as audio: ")
        yt = YouTube(url)
        audio_stream = yt.streams.filter(only_audio=True).first()
        file_size = audio_stream.filesize
        print(f"Now downloading {audio_stream.title}")
        filename = audio_stream.title.replace("\\","/").replace("?","qq")
        audio_stream.download(output_path="C:/Songs/",filename=filename+".mp3")
        print("Audio downloaded successfully!")

    elif choice == 2:
        pl_url = input("Enter the URL of the playlist: ")
        response = requests.get(pl_url)
        if response.status_code == 200:
            video_urls = re.findall(r'watch\?v=[\w-]*', response.text)
            video_urls = list(set(video_urls))  # Remove duplicates
            print(f'Downloading {len(video_urls)} audios from the playlist...')
            for video_url in tqdm(video_urls, desc="Downloading audios"):
                video_url = 'https://www.youtube.com/' + video_url
                yt = YouTube(video_url)
                audio_stream = yt.streams.filter(only_audio=True).first()
                file_size = audio_stream.filesize
                ausio = audio_stream.title.replace("("," ").replace(")"," ").replace("|"," ").replace("\""," ").replace("-"," ").replace("@"," ").replace("/"," ")
                audio_stream.download(output_path="C:/Songs/", filename=f"{ausio}.mp3")
            print("All audios downloaded successfully from the playlist.")
        else:
            print("Failed to fetch playlist. Please check the URL and try again.")

    elif choice == 3:
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please enter a valid option.")
