import os
import shutil
import tkinter as tk
from tkinter import filedialog
import zipfile


def choose_folder():
    root = tk.Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory()
    return folder_path


def create_image_archives(source_folder, destination_folder, max_archive_size):
    file_list = []
    total_size = 0
    archive_count = 1
    archive_size = 0

    # Получение списка jpg-файлов в указанной папке
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            if file.lower().endswith(".jpg"):
                file_path = os.path.join(root, file)
                file_size = os.path.getsize(file_path)
                file_list.append((file_path, file_size))

    # Сортировка списка файлов по размеру (от наименьшего к наибольшему)
    file_list.sort(key=lambda x: x[1])

    # Создание и заполнение архивов
    for file_path, file_size in file_list:
        if total_size + file_size > max_archive_size or archive_size == 0:
            # Создание нового архива
            archive_path = os.path.join(destination_folder, f"archive{archive_count}.zip")
            with zipfile.ZipFile(archive_path, "w", zipfile.ZIP_DEFLATED) as archive:
                archive_size = 0
                archive_count += 1

        # Добавление файла в текущий архив
        archive.write(file_path, os.path.basename(file_path))
        total_size += file_size
        archive_size += file_size

    print(f"Создано {archive_count - 1} архив(ов).")


# Выбор исходной папки через диалоговое окно
source_folder = choose_folder()

# Проверка, была ли выбрана папка
if source_folder:
    # Выбор папки назначения через диалоговое окно
    destination_folder = choose_folder()

    # Проверка, была ли выбрана папка назначения
    if destination_folder:
        max_archive_size = 19999 * 1024  # 19999 килобайт в байтах
        create_image_archives(source_folder, destination_folder, max_archive_size)
    else:
        print("Папка назначения не выбрана.")
else:
    print("Исходная папка не выбрана.")
