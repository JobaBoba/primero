import os
from moviepy.editor import *
import tkinter as tk
from tkinter import filedialog

def convert_mp4_to_mp3(input_folder, output_folder):
    for file_name in os.listdir(input_folder):
        if file_name.endswith(".mp4"):
            input_path = os.path.join(input_folder, file_name)
            output_path = os.path.join(output_folder, file_name.replace(".mp4", ".mp3"))
            video = VideoFileClip(input_path)
            audio = video.audio
            audio.write_audiofile(output_path)
            audio.close()
            video.close()

root = tk.Tk()
root.withdraw()

input_folder = filedialog.askdirectory(title="Выберите папку с файлами .mp4")
output_folder = filedialog.askdirectory(title="Выберите папку для сохранения файлов .mp3")
convert_mp4_to_mp3(input_folder, output_folder)
