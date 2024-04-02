import os
import PyPDF2
from google.cloud import translate_v2 as translate

def pdf_to_str(pdf_path):
    translate_client = translate.Client()

    pdf_file = open(pdf_path, 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    total_pages = len(pdf_reader.pages)
    extracted_text = ""
    for page_num in range(total_pages):
        page = pdf_reader.pages[page_num]
        page_text = page.extract_text()
        page_text = translate_client.translate(page_text, target_language='zh-TW')
        page_text = f"\n--- Page {page_num + 1} ---\n{page_text}\n\n"
        extracted_text += page_text
    pdf_file.close()
    print(f"Text has been extracted.")
    return extracted_text


def list_languages() -> dict:
    """Lists all available languages."""
    from google.cloud import translate_v2 as translate

    translate_client = translate.Client()

    results = translate_client.get_languages()

    for language in results:
        print("{name} ({language})".format(**language))

    return results