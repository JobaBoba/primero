import tkinter as tk
from tkinter import filedialog
import subprocess

def choose_archive():
    root = tk.Tk()
    root.withdraw()  # Скрыть основное окно Tkinter

    archive_path = filedialog.askopenfilename(
        title="Выберите архив для разархивации",
        filetypes=(("RAR архивы", "*.rar"), ("Все файлы", "*.*"))
    )

    return archive_path

def choose_extraction_path():
    root = tk.Tk()
    root.withdraw()

    extraction_path = filedialog.askdirectory(
        title="Выберите папку для разархивации"
    )

    return extraction_path

def unrar_archive(archive_path, extraction_path):
    cmd = ["unrar", "x", archive_path, extraction_path]
    subprocess.run(cmd)

def main():
    archive_path = choose_archive()
    if not archive_path:
        print("Выбор архива отменен.")
        return

    extraction_path = choose_extraction_path()
    if not extraction_path:
        print("Выбор папки для разархивации отменен.")
        return

    unrar_archive(archive_path, extraction_path)
    print("Архив успешно разархивирован.")

if __name__ == "__main__":
    main()
