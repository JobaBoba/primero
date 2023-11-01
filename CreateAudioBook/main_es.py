import pyttsx3
import tkinter as tk
from tkinter import filedialog

def open_file():
    file_path = filedialog.askopenfilename(title="Seleccione un archivo", filetypes=(("Archivos de texto", "*.txt"),))
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
            if "spanish" in voice.name.lower():
                engine.setProperty('voice', voice.id)
                break
        engine.setProperty('rate', 150)  # Устанавливает скорость воспроизведения на 150 слов в минуту
        engine.save_to_file(text, 'output.mp3')
        engine.runAndWait()

        file_path = filedialog.asksaveasfilename(title="Guardar como", filetypes=(("Archivos MP3", "*.mp3"),), defaultextension=".mp3")
        if file_path:
            with open('output.mp3', 'rb') as read_file:
                with open(file_path, 'wb') as write_file:
                    write_file.write(read_file.read())

window = tk.Tk()
window.title("Texto a voz")

convert_button = tk.Button(window, text="Convertir", command=convert_to_speech)
convert_button.pack()

window.mainloop()
