import fitz     # to jest jak cos biblio PyMuPDF, niestety zainstalowac trza, ale czyta duzo wiecej niz pdf
import os

def handle_dropfile(window, file_path, text_input):
    last_element = os.path.basename(file_path.decode('utf-8'))
    file_extension = os.path.splitext(file_path.decode('utf-8'))[1]

    if file_extension == '.wav':
        print("Sciezka pliku: ", file_path)
        print("Nazwa: ", last_element)

    try:
        if text_input.collide_point(*window.mouse_pos):
            read_pdf(file_path, text_input)
    except Exception as e:
        text_input.text = f"Error: {str(e)}"


def read_pdf(file_path, text_input):
    try:
        byte_string = file_path
        proper_path = byte_string.decode('utf-8')
        doc = fitz.open(proper_path)
        pdf_text = ""
        for page_num in range(doc.page_count):
            page = doc[page_num]
            pdf_text += page.get_text()
        # v jakby cos w tym miejscu zwraca tez tak o text, dzieki bogu kivy, ze robisz za mnie aktualizacje
        text_input.text = pdf_text
    except Exception as e:
        text_input.text = f"Error: {str(e)}"