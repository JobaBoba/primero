import os
from tkinter import Tk, filedialog
from PIL import Image

def convert_images(source_folder, export_folder):
    # Создаем целевую папку для экспорта, если она не существует
    if not os.path.exists(export_folder):
        os.makedirs(export_folder)
    else:
        print("Такая папка уже существует. Выберите другую.")
        return

    # Получаем список файлов в исходной папке
    file_list = os.listdir(source_folder)

    for file_name in file_list:
        if file_name.endswith('.png'):
            # Открываем изображение и конвертируем его в градации серого
            image = Image.open(os.path.join(source_folder, file_name)).convert('L')

            # Создаем новое имя файла и сохраняем его в папке для экспорта
            new_file_name = file_name.replace('.png', '.jpg')
            export_path = os.path.join(export_folder, new_file_name)
            image.save(export_path, 'JPEG', quality=60)

    print("Конвертация завершена!")

# Инициализация окна выбора папок с использованием Tkinter
root = Tk()
root.withdraw()

# Диалоговое окно для выбора целевой папки
source_folder = filedialog.askdirectory(title="Выберите целевую папку")

# Диалоговое окно для выбора папки для экспорта
export_folder = filedialog.askdirectory(title="Выберите папку для экспорта")

# Вызываем функцию для конвертации изображений
convert_images(source_folder, export_folder)
