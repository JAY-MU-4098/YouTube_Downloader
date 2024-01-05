from pytube import YouTube
import os
from time import sleep

def download_youtube_video(url):
    yt = YouTube(url)
    try:
        video = yt.streams.get_highest_resolution()

        video.download("Downloaded-video")
        print(f"{yt.title} has been downloaded successfully.")

    except Exception:
        sleep(2)

        print(f"An error occurred : {yt.title} can not be download")
        with open("not-downloaded.txt", "a") as fl:
            fl.write(yt.title)


if __name__ == "__main__":
    print("Program started...")
    with open("links.txt") as file:
        links = file.readlines()

    for link in links:
        download_youtube_video(link)

    print("All the links have been downloaded.")
