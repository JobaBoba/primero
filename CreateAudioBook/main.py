import pyttsx3
import tkinter as tk
from tkinter import filedialog

def open_file():
    file_path = filedialog.askopenfilename(title="Выберите файл", filetypes=(("Текстовые файлы", "*.txt"),))
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        return text
    return None

def convert_to_speech():
    text = open_file()
    if text:
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        for voice in voices:
            if "female" in voice.name.lower():  # Предполагается, что женский голос включает "female" в своем имени
                engine.setProperty('voice', voice.id)
                break
        engine.save_to_file(text, 'output.mp3')
        engine.runAndWait()

        file_path = filedialog.asksaveasfilename(title="Сохранить как", filetypes=(("MP3 файлы", "*.mp3"),), defaultextension=".mp3")
        if file_path:
            with open('output.mp3', 'rb') as read_file:
                with open(file_path, 'wb') as write_file:
                    write_file.write(read_file.read())

window = tk.Tk()
window.title("Текст в речь")

convert_button = tk.Button(window, text="Конвертировать", command=convert_to_speech)
convert_button.pack()

window.mainloop()