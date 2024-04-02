import os
import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox, Button, Label, PhotoImage
from tkinterdnd2 import DND_FILES, TkinterDnD

from components.file_io import *
from components.pdf_processor import *

def pdf_to_txt(pdf_file_path):
    extracted_text = pdf_to_str(pdf_file_path)
    save_str_to_txt(pdf_file_path, extracted_text)


def drag_and_drop_window(event):
    pdf_file_path = event.data.strip().replace('{', '').replace('}', '').replace('"', '')
    if pdf_file_path.lower().endswith('.pdf'):
        pdf_to_txt(pdf_file_path)
    else:
        messagebox.showerror("Error", "Please drop a PDF file.")


def update_window(initial_selection_made, root, file_label, process_button, pdf_file_path, image_label):
    if not initial_selection_made:
        file_label = Label(root, text=f"Selected File: {os.path.basename(pdf_file_path)}")
        #file_label.config(text=f"Selected File: {os.path.basename(pdf_file_path)}")
        file_label.pack(pady=10)

        image_label.forget()


        # Update the command for the existing Process button
        process_button = Button(root, text="Process")
        process_button.pack(side='bottom', pady=10)
        process_button.config(command=lambda: pdf_to_txt(pdf_file_path))
        initial_selection_made = True
    else:
        file_label.config(text=f"Selected File:\n {os.path.basename(pdf_file_path)}")


def main():
    root = TkinterDnD.Tk()
    root.title('PDF Translator')
    root.geometry('500x400')
    root.minsize(500, 400)
    root.maxsize(800, 400)

    def select_and_update():
        pdf_file_path = get_pdf_path()
        if pdf_file_path:
            update_window(initial_selection_made, root, file_label, process_button, pdf_file_path, image_label)
    
    instruction_label = tk.Label(root, text="Drag & Drop\n\n- OR - ")
    instruction_label.pack(side='top', pady=10)
    Button(root, text="Browse", command=select_and_update).pack(side='top')



    image = PhotoImage(file="img/drag_and_drop.png")
    image_label = tk.Label(root, image=image)
    image_label.pack()
    
    file_label = None
    initial_selection_made = False
    process_button = None

    Label(root, text="All processed TXT file will be saved under '~/Download' folder.\nCurrently, only programmatically generated PDFs are supported.", font=("Mono", 10)).pack(side='bottom', pady = 8)
    
    '''
    output_path = get_download_folder()
    output_label = Label(root, text="Output Path: {output_path}")
    output_label.pack(pady=10)
    output_label.config(text=f"Output Path: {output_path}")
    '''
    
    root.drop_target_register(DND_FILES)
    root.dnd_bind('<<Drop>>', lambda event: update_window(root, file_label, process_button, event.data.strip().replace('{', '').replace('}', '').replace('"', '')))
    
    root.mainloop()

if __name__ == "__main__":
    main()