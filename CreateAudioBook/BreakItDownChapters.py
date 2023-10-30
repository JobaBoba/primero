import tkinter as tk
from tkinter import filedialog

def split_into_chapters(filename, save_directory):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()

    chapters = content.split('Глава')
    chapters = [chapter for chapter in chapters if chapter.strip()]

    for index, chapter in enumerate(chapters, start=1):
        chapter_filename = f'{save_directory}/Глава{index}.txt'
        with open(chapter_filename, 'w', encoding='utf-8') as file:
            file.write('Глава' + chapter)

def main():
    root = tk.Tk()
    root.withdraw()  # скрыть основное окно tkinter

    filename = filedialog.askopenfilename(title='Выберите файл txt', filetypes=[("Text files", "*.txt")])
    if not filename:
        return

    save_directory = filedialog.askdirectory(title='Выберите папку для сохранения глав')
    if not save_directory:
        return

    split_into_chapters(filename, save_directory)

if __name__ == "__main__":
    main()
