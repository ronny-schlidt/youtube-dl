import subprocess
import os

def get_download_path():
    with open("Your Download Path.txt", "r")as f:
        path = f.readline().split()
    print(path)

    if path[2] == "None":
        Download_Path = os.getcwd() + "\\" + "Downloads"
    else:
        Download_Path = path[2]
    print(Download_Path)
    return Download_Path


def start_download(link, file_format):
    if file_format == "m4a":
        cmd = f"youtube-dl -o \"{Download_Path}\%(title)s.%(ext)s\" -f 140 {link}"
        print(cmd)
        subprocess.run(cmd)
    if file_format == "mp3":
        cmd = f"youtube-dl -o \"{Download_Path}\%(title)s.%(ext)s\" --extract-audio --audio-format mp3 {link}"
        print(cmd)
        subprocess.run(cmd)
    if file_format == "video":
        cmd = f"youtube-dl -o \"{Download_Path}\%(title)s.%(ext)s\" {link} -f \"bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best\""
        print(cmd)
        subprocess.run(cmd)
    if file_format == "video-compressed":
        cmd = f"youtube-dl -o \"{Download_Path}\%(title)s.%(ext)s\" -f -best {link}"
        print(cmd)
        subprocess.run(cmd)



Download_Path = get_download_path()
link = input("Pls paste the youtube Link here: ")
file_format = input("Pls enter the desired file format (video, mp3, m4a, video-compressed): ")
print("Der Path ist:", Download_Path)
open_download_path = f"start explorer {Download_Path}"

# link = "https://www.youtube.com/watch?v=wgUczLEUWkA"
# file_format = "video"

start_download(link, file_format)
subprocess.run(open_download_path, shell=True)
