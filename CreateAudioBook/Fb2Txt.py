import tkinter as tk
from tkinter import filedialog
import xml.etree.ElementTree as ET


def open_file():
    file_path = filedialog.askopenfilename(title="Выберите файл FB2", filetypes=[("FB2 files", "*.fb2")])
    if file_path:
        return file_path
    else:
        return None


def save_file():
    folder_path = filedialog.askdirectory(title="Выберите папку для сохранения")
    if folder_path:
        return folder_path
    else:
        return None


def convert_to_txt(fb2_path, txt_path):
    try:
        tree = ET.parse(fb2_path)
        root = tree.getroot()
        ns = {'fb': 'http://www.gribuser.ru/xml/fictionbook/2.0'}
        text_elements = root.findall('.//fb:p', ns)
        text = '\n'.join([elem.text for elem in text_elements if elem.text])

        with open(txt_path, 'w', encoding='utf-8') as txt_file:
            txt_file.write(text)

        print(f'Файл успешно сконвертирован и сохранен в {txt_path}')
    except Exception as e:
        print(f'Ошибка: {e}')


def main():
    root = tk.Tk()
    root.withdraw()  # скрыть основное окно Tkinter

    fb2_path = open_file()
    if fb2_path:
        folder_path = save_file()
        if folder_path:
            txt_path = f'{folder_path}/{fb2_path.split("/")[-1].replace(".fb2", ".txt")}'
            convert_to_txt(fb2_path, txt_path)
        else:
            print('Папка для сохранения не выбрана')
    else:
        print('Файл не выбран')


if __name__ == '__main__':
    main()
