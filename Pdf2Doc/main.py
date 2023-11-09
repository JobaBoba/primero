import tkinter as tk
from tkinter import filedialog
import fitz  # PyMuPDF

def convert_pdf2docx(input_file: str, output_file: str):
    """ Конвертирует PDF в DOCX. """
    doc = fitz.open(input_file)
    doc.save(output_file, garbage=4, deflate=True, clean=True)

def browse_files():
    """ Открывает диалоговое окно для выбора файла. """
    root = tk.Tk()
    root.withdraw()  # Скрытие основного окна Tkinter
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    return file_path

if __name__ == "__main__":
    input_file = browse_files()
    if input_file:
        output_file = input_file.replace('.pdf', '.docx')
        convert_pdf2docx(input_file, output_file)
        print(f"Файл {output_file} был успешно создан.")
    else:
        print("Файл не выбран.")
