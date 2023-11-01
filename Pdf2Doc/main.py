# Импорт библиотек
import tkinter as tk
from tkinter import filedialog
from pdf2docx import parse
from typing import Tuple

def convert_pdf2docx(input_file: str, output_file: str, pages: Tuple = None):
    """Конвертирует pdf в docx"""
    if pages:
        pages = [int(i) for i in list(pages) if i.isnumeric()]
    result = parse(pdf_file=input_file, docx_with_path=output_file, pages=pages)
    summary = {
        "File": input_file,
        "Pages": str(pages),
        "Output File": output_file
    }
    # Вывод результата
    print("## Summary ########################################################")
    print("\\n".join(" {}: {}".format(i, j) for i, j in summary.items()))
    print("###################################################################")
    return result

def browse_files():
    """Открывает диалоговое окно для выбора файла"""
    root = tk.Tk()
    root.withdraw()  # скрыть основное окно
    file_path = filedialog.askopenfilename()
    return file_path

if __name__ == "__main__":
    input_file = browse_files()
    output_file = input_file.replace('.pdf', '.docx')
    convert_pdf2docx(input_file, output_file)
