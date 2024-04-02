import os
import platform
from tkinter.filedialog import askopenfilename
from tkinter import messagebox


def get_pdf_path():
    try:
        pdf_path = askopenfilename(filetypes=[("PDF files", "*.pdf")])
        return pdf_path
    except Exception as e:
        messagebox.showerror("Error", str(e))
        return None

def get_download_folder():
    if platform.system() == 'Windows':
        return os.path.join(os.path.join(os.environ['USERPROFILE']), 'Downloads')
    else:
        return os.path.join(os.path.join(os.path.expanduser('~')), 'Downloads')

def get_unique_filename(path):
    counter = 1
    new_path = path
    while os.path.exists(new_path):
        name, ext = os.path.splitext(path)
        new_path = f"{name}_{counter}{ext}"
        counter += 1
    return new_path

def get_txt_filename(pdf_path):
    pdf_filename = os.path.basename(pdf_path)
    pdf_filename_without_extension = os.path.splitext(pdf_filename)[0]
    txt_filename = f"{pdf_filename_without_extension}_converted.txt"
    return txt_filename

def save_str_to_txt(pdf_path, extracted_text):
    txt_filename = get_txt_filename(pdf_path)
    txt_path = os.path.join(get_download_folder(), txt_filename)
    txt_path = get_unique_filename(txt_path)
    with open(txt_path, "w", encoding='utf-8') as txt_file:
        txt_file.write(extracted_text)
    print(f"Text has been saved to: {txt_path}.")